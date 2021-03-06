# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/user.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from distantbes.proto.proto import grp_pb2 as proto_dot_grp__pb2
from distantbes.proto.proto import user_id_pb2 as proto_dot_user__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/user.proto',
  package='user',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10proto/user.proto\x12\x04user\x1a\x0fproto/grp.proto\x1a\x13proto/user_id.proto\"/\n\x0eGetUserRequest\x12\x1d\n\x07user_id\x18\x01 \x01(\x0b\x32\x0c.user.UserId\"Z\n\x0fGetUserResponse\x12\'\n\x0c\x64isplay_user\x18\x01 \x01(\x0b\x32\x11.user.DisplayUser\x12\x1e\n\nuser_group\x18\x02 \x03(\x0b\x32\n.grp.Group\"\x13\n\x11\x43reateUserRequest\"=\n\x12\x43reateUserResponse\x12\'\n\x0c\x64isplay_user\x18\x01 \x01(\x0b\x32\x11.user.DisplayUserb\x06proto3'
  ,
  dependencies=[proto_dot_grp__pb2.DESCRIPTOR,proto_dot_user__id__pb2.DESCRIPTOR,])




_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='user.GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user.GetUserRequest.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=111,
)


_GETUSERRESPONSE = _descriptor.Descriptor(
  name='GetUserResponse',
  full_name='user.GetUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_user', full_name='user.GetUserResponse.display_user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_group', full_name='user.GetUserResponse.user_group', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=203,
)


_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='user.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=224,
)


_CREATEUSERRESPONSE = _descriptor.Descriptor(
  name='CreateUserResponse',
  full_name='user.CreateUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_user', full_name='user.CreateUserResponse.display_user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=287,
)

_GETUSERREQUEST.fields_by_name['user_id'].message_type = proto_dot_user__id__pb2._USERID
_GETUSERRESPONSE.fields_by_name['display_user'].message_type = proto_dot_user__id__pb2._DISPLAYUSER
_GETUSERRESPONSE.fields_by_name['user_group'].message_type = proto_dot_grp__pb2._GROUP
_CREATEUSERRESPONSE.fields_by_name['display_user'].message_type = proto_dot_user__id__pb2._DISPLAYUSER
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['GetUserResponse'] = _GETUSERRESPONSE
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreateUserResponse'] = _CREATEUSERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:user.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType('GetUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERRESPONSE,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:user.GetUserResponse)
  })
_sym_db.RegisterMessage(GetUserResponse)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:user.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserResponse = _reflection.GeneratedProtocolMessageType('CreateUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERRESPONSE,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:user.CreateUserResponse)
  })
_sym_db.RegisterMessage(CreateUserResponse)


# @@protoc_insertion_point(module_scope)
