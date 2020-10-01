from distantbes.proto.proto import build_event_stream_pb2 as bes
from distantbes.utils import dict_to_workspace_status, get_current_timestamp
from distantbes.enums import CPU, CompilationMode, EXIT_CODES
from platform import node

def file_message(name, contents):
    file_msg = bes.File()
    file_msg.name = name
    file_msg.contents = contents.encode()
    return file_msg

def started(uuid, command, build_tool_version="0.0.1", start_time=None, pattern=[]):
    if start_time is None:
        start_time = get_current_timestamp()

    event = bes.BuildEvent()
    event.id.started.SetInParent()

    event.started.uuid = uuid
    event.started.start_time_millis = start_time
    event.started.build_tool_version = build_tool_version
    event.started.command = command

    if len(pattern) > 0:
        pattern_e = bes.BuildEventId()
        pattern_e.pattern.SetInParent()
        pattern_e.pattern.pattern.extend(pattern)
        event.children.append(pattern_e)

    return event

def workspace_status(build_user="distant", build_host=node()):
    event = bes.BuildEvent()
    event.id.workspace_status.SetInParent()
    
    ws_dict = {"BUILD_USER":build_user, "BUILD_HOST":build_host}
    ws_proto = dict_to_workspace_status(ws_dict)

    event.workspace_status.CopyFrom(ws_proto)

    return event

def progress(count, stdout):
    event = bes.BuildEvent()
    event.id.progress.opaque_count = count

    event.progress.stdout = stdout

    return event

def config(
        cpu=CPU.k8, 
        compilation_mode=CompilationMode.fastbuild, 
        gendir="/usr/bin/distant-bes", 
        bindir="/usr/bin/distant-bes"
        ):
    cpu = str(cpu)
    compilation_mode = str(compilation_mode)

    config_dict = {
            'TARGET_CPU':cpu,
            'COMPILATION_MODE':compilation_mode,
            'GENDIR':gendir,
            'BINDIR':bindir,
            }

    event = bes.BuildEvent()
    event.id.configuration.SetInParent()
    event.id.configuration.id = ""
    
    event.configuration.cpu = cpu
    event.configuration.platform_name = cpu
    event.configuration.make_variable.update(config_dict)
    event.configuration.mnemonic = "{}-{}".format(cpu, compilation_mode)

    return event

def target_announce(label, kind="distant_target"):
    event = bes.BuildEvent()
    event.id.target_configured.label = label
    event.configured.target_kind = kind

    return event

def target_complete(label, success, artifacts=None):
    event = bes.BuildEvent()
    event.id.target_completed.label = label
    event.completed.SetInParent()

    if success:
        event.completed.success = success
    if isinstance(artifacts, list):
        event.completed.important_output.extend(artifacts)

    return event

def test_events(label, status=1, duration=1, total_duration=None, log=None):
    if total_duration is None:
        total_duration = duration

    epoch = get_current_timestamp()

    bazel_event_test = bes.BuildEvent()
    bazel_event_test.id.test_result.label = label
    bazel_event_test.id.test_result.run = 1
    bazel_event_test.id.test_result.shard = 1
    bazel_event_test.id.test_result.attempt = 1

    bazel_event_test.test_result.test_attempt_duration_millis = duration
    bazel_event_test.test_result.status = status
    bazel_event_test.test_result.test_attempt_start_millis_epoch = epoch

    if log is not None:
        bazel_event_test.test_result.test_action_output.append(log)

    bazel_event_test_s = bes.BuildEvent()
    bazel_event_test_s.id.test_summary.label = label

    bazel_event_test_s.test_summary.overall_status = status
    bazel_event_test_s.test_summary.total_run_count = 1

    if log is not None:
        bazel_event_test_s.test_summary.passed.append(log)

    bazel_event_test_s.test_summary.total_num_cached = 1
    bazel_event_test_s.test_summary.first_start_time_millis = epoch
    bazel_event_test_s.test_summary.last_stop_time_millis = epoch+total_duration
    bazel_event_test_s.test_summary.total_run_duration_millis = total_duration

    return bazel_event_test, bazel_event_test_s

def status_code(status_code):
    event = bes.BuildEvent()
    event.id.build_finished.SetInParent()

    event.finished.exit_code.name = EXIT_CODES[status_code]
    event.finished.exit_code.code = status_code

    return event

def build_metrics(a_created, a_executed, t_loaded, t_configured, p_loaded):
    event = bes.BuildEvent()
    event.id.build_metrics.SetInParent()

    event.build_metrics.SetInParent()
    event.build_metrics.action_summary.actions_created = a_created
    event.build_metrics.action_summary.actions_executed = a_executed

    event.build_metrics.target_metrics.targets_loaded = t_loaded
    event.build_metrics.target_metrics.targets_configured = t_configured

    event.build_metrics.package_metrics.packages_loaded = p_loaded

    return event

def build_metadata(dictionary):
    event = bes.BuildEvent()
    event.id.build_metadata.SetInParent()

    event.build_metadata.metadata.update(dictionary)

    return event

def last_event(elapsed_time):
    event = bes.BuildEvent()
    event.id.build_tool_logs.SetInParent()
    
    event.last_message = True

    file1 = bes.File(name="elapsed time", contents=str(elapsed_time).encode())
    file2 = bes.File(name="command.profile.gz", uri="file:///dev/null")

    event.build_tool_logs.log.append(file1)
    event.build_tool_logs.log.append(file2)

    return event
