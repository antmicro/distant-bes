from distantbes.proto.proto import (
        build_event_stream_pb2 as bes,
        build_events_pb2 as be,
        publish_build_event_pb2 as pbe, 
        )
from google.protobuf.timestamp_pb2 import Timestamp
import uuid

def dict_to_workspace_status(ws_dict):
    ws = bes.WorkspaceStatus()

    for key, value in ws_dict.items():
        if value is not None:
            wsi = bes.WorkspaceStatus.Item(key=key, value=value)
            ws.item.append(wsi)

    return ws

def get_current_timestamp():
    now = Timestamp()
    now.GetCurrentTime()
    return now.ToMilliseconds()

def generate_last_message(sequence_number, stream_id):
    build_event = be.BuildEvent()
    finish = be.BuildEvent.BuildComponentStreamFinished(type=1)
    build_event.component_stream_finished.CopyFrom(finish)

    obe = pbe.OrderedBuildEvent()
    obe.sequence_number = sequence_number
    obe.event.CopyFrom(build_event)
    obe.stream_id.CopyFrom(stream_id)

    pbtesr = pbe.PublishBuildToolEventStreamRequest()
    pbtesr.ordered_build_event.CopyFrom(obe)

    return pbtesr

def generate_stream_id(invocation_id=None, build_id=None):
    if invocation_id is None:
        invocation_id = str(uuid.uuid4())

    if build_id is None:
        build_id = str(uuid.uuid4())

    sid = be.StreamId()
    sid.invocation_id = invocation_id
    sid.build_id = build_id
    sid.component = 3
    
    return sid

def pack_bazel_event(sequence_number, stream_id, bazel_event, project_id="distant-bes"):
    build_event = be.BuildEvent()
    build_event.bazel_event.Pack(bazel_event)

    build_event.event_time.GetCurrentTime()

    obe = pbe.OrderedBuildEvent()
    obe.sequence_number = sequence_number
    obe.event.CopyFrom(build_event)
    obe.stream_id.CopyFrom(stream_id)

    pbtesr = pbe.PublishBuildToolEventStreamRequest()
    pbtesr.ordered_build_event.CopyFrom(obe)
    
    pbtesr.project_id = project_id

    return pbtesr
