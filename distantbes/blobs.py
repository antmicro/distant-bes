from distantbes.proto.proto import (
        remote_execution_pb2 as re,
        remote_execution_pb2_grpc as re_grpc,
        build_event_stream_pb2 as bes,
        )
from distantbes.proto.google.bytestream import (
        bytestream_pb2 as bstr,
        bytestream_pb2_grpc as bstr_grpc
        )
from hashlib import sha256
import grpc

MAX_REQUEST_SIZE = 4 * 1024 * 1024 - 1024

class Uploader:
    def __init__(self, grpc_url=None, force_localhost_in_msg=False):
        self.grpc_url = grpc_url
        if self.grpc_url is None:
            self.grpc_url = 'localhost:1985'
        channel = grpc.insecure_channel(self.grpc_url)
        self.stub = bstr_grpc.ByteStreamStub(channel)
        self.__force_localhost = force_localhost_in_msg

    def put_string(self, string, bes_file_name=None):
        return self.put_blob(string.encode(), bes_file_name=bes_file_name)

    def put_blob(self, blob, bes_file_name=None):
        blob_digest = re.Digest()
        blob_digest.hash = sha256(blob).hexdigest()
        blob_digest.size_bytes = len(blob)

        resource_name =  "/".join(['blobs', blob_digest.hash, str(blob_digest.size_bytes)])

        def __write_request_stream(resource, content):
            offset = 0
            finished = False
            remaining = len(content)

            while not finished:
                chunk_size = min(remaining, MAX_REQUEST_SIZE)
                remaining -= chunk_size

                request = bstr.WriteRequest()
                request.resource_name = resource
                request.data = content[offset:offset + chunk_size]
                request.write_offset = offset
                request.finish_write = remaining <= 0

                yield request

                offset += chunk_size
                finished = request.finish_write

        write_requests = __write_request_stream(resource_name, blob)

        write_response = self.stub.Write(write_requests)

        if bes_file_name is not None:
            if self.__force_localhost:
                cas_url = "localhost:1985"
            else:
                cas_url = self.grpc_url
                
            bes_file = bes.File(
                    name=bes_file_name,
                    uri="bytestream://{}/{}".format(cas_url, resource_name),
                    )
            return bes_file
        else:
            return resource_name
