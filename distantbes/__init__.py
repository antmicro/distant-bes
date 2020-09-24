from distantbes.proto.proto import publish_build_event_pb2_grpc as pbe_grpc
from distantbes.proto.proto import build_event_stream_pb2 as bes
from distantbes.blobs import Uploader
from distantbes.utils import generate_stream_id, pack_bazel_event, generate_last_message
from queue import Queue
from threading import Thread
import distantbes.events
import distantbes.enums
import grpc
import time
import os

class Invocation:
    def __init__(
            self, 
            grpc_bes_url, 
            grpc_cas_enabled=True, 
            grpc_cas_url=None, 
            command="distant-bes",
            force_localhost_in_cas_msg=False,
            cpu=distantbes.enums.CPU.k8,
            compilation_mode=distantbes.enums.CompilationMode.fastbuild,
            uuid=None,
            hostname=None,
            channel_timeout=3,
            ):
        self.grpc_bes_url = grpc_bes_url
        self.grpc_cas_enabled = grpc_cas_enabled

        if self.grpc_cas_enabled:
            if grpc_cas_url is None:
                self.grpc_cas_url = grpc_bes_url
            else:
                self.grpc_cas_url = grpc_cas_url
            self.cas_uploader = Uploader(self.grpc_cas_url, force_localhost_in_cas_msg)

        self.channel = grpc.insecure_channel(self.grpc_bes_url)
        self.channel_timeout = channel_timeout
        self.stub = pbe_grpc.PublishBuildEventStub(self.channel)
        self.__send_queue = Queue()
        self.__stub_thread = None
        self.__command = command
        self.__stream_id = generate_stream_id(uuid)

        self.invocation_id = self.__stream_id.invocation_id
        self.build_id = self.__stream_id.build_id

        self.transmitted_events = []
        self.targets = []

        self.grpc_failure = False
        self.grpc_exception = None

        self.__sequence = 0
        self.__stdout_count = 0
        self.__start_time = time.monotonic()
        self.__cpu = cpu
        self.__compilation_mode = compilation_mode
        self.__hostname = hostname

    def __queue_to_stub(self):
        pbt_event_stream = self.stub.PublishBuildToolEventStream(
                iter(self.__send_queue.get, None))
        try:
            next(pbt_event_stream)
        except Exception as e:
            self.grpc_failure = True
            self.grpc_exception = e

    def __send_last_pbtesr(self):
        self.__sequence += 1
        ev = generate_last_message(self.__sequence, self.__stream_id)
        self.__send_queue.put(ev)
        self.__send_queue.put(None)

    def check_grpc_channel(self):
        try:
            grpc.channel_ready_future(self.channel).result(timeout=self.channel_timeout)
            return True
        except grpc.FutureTimeoutError:
            return False

    def send_bazel_event(self, bazel_event):
        self.__sequence += 1
        self.transmitted_events.append(bazel_event)
        packed = pack_bazel_event(self.__sequence, self.__stream_id, bazel_event)
        self.__send_queue.put(packed)

    def open(self):
        self.__stub_thread = Thread(target=self.__queue_to_stub)
        self.__stub_thread.start()

        init_event = events.started(self.invocation_id, self.__command)
        if self.__hostname is not None:
            workspace_event = events.workspace_status(build_host=self.__hostname)
        else:
            workspace_event = events.workspace_status()
        config_event = events.config(self.__cpu, self.__compilation_mode)

        self.send_bazel_event(init_event)
        self.send_bazel_event(workspace_event)
        self.send_bazel_event(config_event)

    def close(self, status_code=0, elapsed=None):
        if elapsed is None:
            elapsed = round(time.monotonic() - self.__start_time, 6)

        last_bazel_event = events.last_event(elapsed)
        status_event = events.status_code(status_code)
        
        self.send_bazel_event(status_event)
        self.send_bazel_event(last_bazel_event)
        self.__send_last_pbtesr()

    def add_stdout(self, string, append_newline=True):
        self.__stdout_count += 1

        if append_newline:
            string = string + '\n'

        progress = events.progress(self.__stdout_count, string)
        self.send_bazel_event(progress)

    def flush(self):
        ### WARNING: this is non-standard!
        d = {"flush":"yes"}
        bm_ev = events.build_metadata(d)

        self.send_bazel_event(bm_ev)

    def announce_target(self, target_name):
        target_event = events.target_announce(target_name)

        self.send_bazel_event(target_event)
        self.targets.append(target_name)

    def finalize_target(self, target_name, success, artifacts=None):
        completed_target_event = events.target_complete(target_name, success, artifacts)

        self.send_bazel_event(completed_target_event)

    def finalize_target_upload_files(self, target_name, success, artifacts=None):
        uploaded_artifacts = []

        # If we received a list of artifacts, 
        # it will be understood as a list of files to be uploaded.
        # If we received a dictionary, we'll treat it as strings.
        # The user, therefore, may attach links to files hosted using
        # any protocol they wish, e.g. http, ftp, gopher, etc.
        if isinstance(artifacts, list):
            for a in artifacts:
                with open(a, 'rb') as f:
                    base_name = os.path.basename(a)
                    file_msg = self.cas_uploader.put_blob(f.read(), base_name)
                    uploaded_artifacts.append(file_msg)
        elif isinstance(artifacts, dict):
            for key, value in artifacts.items():
                bes_file = bes.File(name=key, uri=value)
                uploaded_artifacts.append(bes_file)

        completed_target_event = events.target_complete(target_name, success, uploaded_artifacts)

        self.send_bazel_event(completed_target_event)

    def add_test_to_target(self, target_name, status=1, duration=1000, total_duration=1000, logstr=None):
        if logstr is not None:
            logmsg = self.cas_uploader.put_string(logstr, "test.log")
        else:
            logmsg = None

        test_events_tuple = events.test_events(target_name, status, duration, total_duration, logmsg)

        self.send_bazel_event(test_events_tuple[0])
        self.send_bazel_event(test_events_tuple[1])

    def add_build_metrics(self, a_created, a_executed, t_loaded, t_configured, p_loaded):
        build_metrics_event = events.build_metrics(
                a_created, a_executed, t_loaded, t_configured, p_loaded)

        self.send_bazel_event(build_metrics_event)
