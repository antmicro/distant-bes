from distantbes.proto.proto import invocation_pb2 as iv
from distantbes import events
import requests

def get_bb_invocation(url, invocation_id):
    service_url = "{}/rpc/BuildBuddyService/GetInvocation".format(url)

    iv_request = iv.GetInvocationRequest()
    iv_request.lookup.invocation_id = invocation_id

    r = requests.post(service_url, data=iv_request.SerializeToString())

    iv_response = iv.GetInvocationResponse()
    iv_response.MergeFromString(r.content)

    return iv_response

def prepare_fake_invocation(invocation_id, success=False):
    ev = [
            events.started(invocation_id, 'dummy'),
            events.status_code(1),
            events.last_event(1)
            ]

    f_iv = iv.Invocation()
    f_iv.invocation_id = invocation_id
    f_iv.success = success
    f_iv.user = 'distant-bes'
    f_iv.command = 'dummy'
    f_iv.invocation_status = 1

    for e in ev:
        iv_ev = iv.InvocationEvent(build_event=e, sequence_number=ev.index(e))
        f_iv.event.append(iv_ev)

    return f_iv

def prepare_fake_invocation_response(invocation):
    iv_response = iv.GetInvocationResponse()
    iv_response.invocation.append(invocation)
    
    return iv_response
