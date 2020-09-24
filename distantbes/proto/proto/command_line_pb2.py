# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/command_line.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from distantbes.proto.proto import option_filters_pb2 as proto_dot_option__filters__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/command_line.proto',
  package='command_line',
  syntax='proto3',
  serialized_options=b'\n+com.google.devtools.build.lib.runtime.proto',
  serialized_pb=b'\n\x18proto/command_line.proto\x12\x0c\x63ommand_line\x1a\x1aproto/option_filters.proto\"]\n\x0b\x43ommandLine\x12\x1a\n\x12\x63ommand_line_label\x18\x01 \x01(\t\x12\x32\n\x08sections\x18\x02 \x03(\x0b\x32 .command_line.CommandLineSection\"\x9b\x01\n\x12\x43ommandLineSection\x12\x15\n\rsection_label\x18\x01 \x01(\t\x12-\n\nchunk_list\x18\x02 \x01(\x0b\x32\x17.command_line.ChunkListH\x00\x12/\n\x0boption_list\x18\x03 \x01(\x0b\x32\x18.command_line.OptionListH\x00\x42\x0e\n\x0csection_type\"\x1a\n\tChunkList\x12\r\n\x05\x63hunk\x18\x01 \x03(\t\"2\n\nOptionList\x12$\n\x06option\x18\x01 \x03(\x0b\x32\x14.command_line.Option\"\xac\x01\n\x06Option\x12\x15\n\rcombined_form\x18\x01 \x01(\t\x12\x13\n\x0boption_name\x18\x02 \x01(\t\x12\x14\n\x0coption_value\x18\x03 \x01(\t\x12-\n\x0b\x65\x66\x66\x65\x63t_tags\x18\x04 \x03(\x0e\x32\x18.options.OptionEffectTag\x12\x31\n\rmetadata_tags\x18\x05 \x03(\x0e\x32\x1a.options.OptionMetadataTagB-\n+com.google.devtools.build.lib.runtime.protob\x06proto3'
  ,
  dependencies=[proto_dot_option__filters__pb2.DESCRIPTOR,])




_COMMANDLINE = _descriptor.Descriptor(
  name='CommandLine',
  full_name='command_line.CommandLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_line_label', full_name='command_line.CommandLine.command_line_label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sections', full_name='command_line.CommandLine.sections', index=1,
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
  serialized_start=70,
  serialized_end=163,
)


_COMMANDLINESECTION = _descriptor.Descriptor(
  name='CommandLineSection',
  full_name='command_line.CommandLineSection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='section_label', full_name='command_line.CommandLineSection.section_label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_list', full_name='command_line.CommandLineSection.chunk_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='option_list', full_name='command_line.CommandLineSection.option_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='section_type', full_name='command_line.CommandLineSection.section_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=166,
  serialized_end=321,
)


_CHUNKLIST = _descriptor.Descriptor(
  name='ChunkList',
  full_name='command_line.ChunkList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk', full_name='command_line.ChunkList.chunk', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=323,
  serialized_end=349,
)


_OPTIONLIST = _descriptor.Descriptor(
  name='OptionList',
  full_name='command_line.OptionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='option', full_name='command_line.OptionList.option', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=351,
  serialized_end=401,
)


_OPTION = _descriptor.Descriptor(
  name='Option',
  full_name='command_line.Option',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='combined_form', full_name='command_line.Option.combined_form', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='option_name', full_name='command_line.Option.option_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='option_value', full_name='command_line.Option.option_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effect_tags', full_name='command_line.Option.effect_tags', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata_tags', full_name='command_line.Option.metadata_tags', index=4,
      number=5, type=14, cpp_type=8, label=3,
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
  serialized_start=404,
  serialized_end=576,
)

_COMMANDLINE.fields_by_name['sections'].message_type = _COMMANDLINESECTION
_COMMANDLINESECTION.fields_by_name['chunk_list'].message_type = _CHUNKLIST
_COMMANDLINESECTION.fields_by_name['option_list'].message_type = _OPTIONLIST
_COMMANDLINESECTION.oneofs_by_name['section_type'].fields.append(
  _COMMANDLINESECTION.fields_by_name['chunk_list'])
_COMMANDLINESECTION.fields_by_name['chunk_list'].containing_oneof = _COMMANDLINESECTION.oneofs_by_name['section_type']
_COMMANDLINESECTION.oneofs_by_name['section_type'].fields.append(
  _COMMANDLINESECTION.fields_by_name['option_list'])
_COMMANDLINESECTION.fields_by_name['option_list'].containing_oneof = _COMMANDLINESECTION.oneofs_by_name['section_type']
_OPTIONLIST.fields_by_name['option'].message_type = _OPTION
_OPTION.fields_by_name['effect_tags'].enum_type = proto_dot_option__filters__pb2._OPTIONEFFECTTAG
_OPTION.fields_by_name['metadata_tags'].enum_type = proto_dot_option__filters__pb2._OPTIONMETADATATAG
DESCRIPTOR.message_types_by_name['CommandLine'] = _COMMANDLINE
DESCRIPTOR.message_types_by_name['CommandLineSection'] = _COMMANDLINESECTION
DESCRIPTOR.message_types_by_name['ChunkList'] = _CHUNKLIST
DESCRIPTOR.message_types_by_name['OptionList'] = _OPTIONLIST
DESCRIPTOR.message_types_by_name['Option'] = _OPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommandLine = _reflection.GeneratedProtocolMessageType('CommandLine', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDLINE,
  '__module__' : 'proto.command_line_pb2'
  # @@protoc_insertion_point(class_scope:command_line.CommandLine)
  })
_sym_db.RegisterMessage(CommandLine)

CommandLineSection = _reflection.GeneratedProtocolMessageType('CommandLineSection', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDLINESECTION,
  '__module__' : 'proto.command_line_pb2'
  # @@protoc_insertion_point(class_scope:command_line.CommandLineSection)
  })
_sym_db.RegisterMessage(CommandLineSection)

ChunkList = _reflection.GeneratedProtocolMessageType('ChunkList', (_message.Message,), {
  'DESCRIPTOR' : _CHUNKLIST,
  '__module__' : 'proto.command_line_pb2'
  # @@protoc_insertion_point(class_scope:command_line.ChunkList)
  })
_sym_db.RegisterMessage(ChunkList)

OptionList = _reflection.GeneratedProtocolMessageType('OptionList', (_message.Message,), {
  'DESCRIPTOR' : _OPTIONLIST,
  '__module__' : 'proto.command_line_pb2'
  # @@protoc_insertion_point(class_scope:command_line.OptionList)
  })
_sym_db.RegisterMessage(OptionList)

Option = _reflection.GeneratedProtocolMessageType('Option', (_message.Message,), {
  'DESCRIPTOR' : _OPTION,
  '__module__' : 'proto.command_line_pb2'
  # @@protoc_insertion_point(class_scope:command_line.Option)
  })
_sym_db.RegisterMessage(Option)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
