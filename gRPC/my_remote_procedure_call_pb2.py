# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my_remote_procedure_call.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='my_remote_procedure_call.proto',
  package='my_remote_procedure_call',
  syntax='proto3',
  serialized_pb=_b('\n\x1emy_remote_procedure_call.proto\x12\x18my_remote_procedure_call\" \n\x10IntNumberMessage\x12\x0c\n\x04item\x18\x01 \x01(\x05\"\xad\x01\n\x14TenIntNumbersMessage\x12\r\n\x05item1\x18\x01 \x01(\x05\x12\r\n\x05item2\x18\x02 \x01(\x05\x12\r\n\x05item3\x18\x03 \x01(\x05\x12\r\n\x05item4\x18\x04 \x01(\x05\x12\r\n\x05item5\x18\x05 \x01(\x05\x12\r\n\x05item6\x18\x06 \x01(\x05\x12\r\n\x05item7\x18\x07 \x01(\x05\x12\r\n\x05item8\x18\x08 \x01(\x05\x12\r\n\x05item9\x18\t \x01(\x05\x12\x0e\n\x06item10\x18\n \x01(\x05\"$\n\x14LongIntNumberMessage\x12\x0c\n\x04item\x18\x01 \x01(\x03\"\"\n\x12\x46loatNumberMessage\x12\x0c\n\x04item\x18\x01 \x01(\x02\"\x1d\n\rStringMessage\x12\x0c\n\x04item\x18\x01 \x01(\t\"\x1e\n\x0e\x42ooleanMessage\x12\x0c\n\x04item\x18\x01 \x01(\x08\"V\n\x08MyObject\x12\x15\n\rnameAttribute\x18\x01 \x01(\t\x12\x14\n\x0c\x61geAttribute\x18\x02 \x01(\x05\x12\x1d\n\x15isNicePersonAttribute\x18\x03 \x01(\x08\"A\n\rObjectMessage\x12\x30\n\x04item\x18\x01 \x01(\x0b\x32\".my_remote_procedure_call.MyObject2\xf8\x07\n\x19\x44iferentOperationsHandler\x12y\n\x1dtakeIntNumber_ReturnIntNumber\x12*.my_remote_procedure_call.IntNumberMessage\x1a*.my_remote_procedure_call.IntNumberMessage\"\x00\x12~\n\x1etakeIntNumbers_ReturnIntNumber\x12..my_remote_procedure_call.TenIntNumbersMessage\x1a*.my_remote_procedure_call.IntNumberMessage\"\x00\x12~\n\x1etakeIntNumber_ReturnIntNumbers\x12*.my_remote_procedure_call.IntNumberMessage\x1a..my_remote_procedure_call.TenIntNumbersMessage\"\x00\x12\x8a\x01\n&takeLongIntNumber_ReturnLongIntNumbers\x12..my_remote_procedure_call.LongIntNumberMessage\x1a..my_remote_procedure_call.LongIntNumberMessage\"\x00\x12\x81\x01\n!takeFloatNumber_ReturnFloatNumber\x12,.my_remote_procedure_call.FloatNumberMessage\x1a,.my_remote_procedure_call.FloatNumberMessage\"\x00\x12m\n\x17takeString_ReturnString\x12\'.my_remote_procedure_call.StringMessage\x1a\'.my_remote_procedure_call.StringMessage\"\x00\x12q\n\x19takeBoolean_ReturnBoolean\x12(.my_remote_procedure_call.BooleanMessage\x1a(.my_remote_procedure_call.BooleanMessage\"\x00\x12m\n\x17takeObject_ReturnObject\x12\'.my_remote_procedure_call.ObjectMessage\x1a\'.my_remote_procedure_call.ObjectMessage\"\x00\x42?\n\x1dgrpc.my_remote_procedure_callB\x15MyRemoteProcedureCallP\x01\xa2\x02\x04MRPCb\x06proto3')
)




_INTNUMBERMESSAGE = _descriptor.Descriptor(
  name='IntNumberMessage',
  full_name='my_remote_procedure_call.IntNumberMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='my_remote_procedure_call.IntNumberMessage.item', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=92,
)


_TENINTNUMBERSMESSAGE = _descriptor.Descriptor(
  name='TenIntNumbersMessage',
  full_name='my_remote_procedure_call.TenIntNumbersMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item1', full_name='my_remote_procedure_call.TenIntNumbersMessage.item1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item2', full_name='my_remote_procedure_call.TenIntNumbersMessage.item2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item3', full_name='my_remote_procedure_call.TenIntNumbersMessage.item3', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item4', full_name='my_remote_procedure_call.TenIntNumbersMessage.item4', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item5', full_name='my_remote_procedure_call.TenIntNumbersMessage.item5', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item6', full_name='my_remote_procedure_call.TenIntNumbersMessage.item6', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item7', full_name='my_remote_procedure_call.TenIntNumbersMessage.item7', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item8', full_name='my_remote_procedure_call.TenIntNumbersMessage.item8', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item9', full_name='my_remote_procedure_call.TenIntNumbersMessage.item9', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item10', full_name='my_remote_procedure_call.TenIntNumbersMessage.item10', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=268,
)


_LONGINTNUMBERMESSAGE = _descriptor.Descriptor(
  name='LongIntNumberMessage',
  full_name='my_remote_procedure_call.LongIntNumberMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='my_remote_procedure_call.LongIntNumberMessage.item', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=306,
)


_FLOATNUMBERMESSAGE = _descriptor.Descriptor(
  name='FloatNumberMessage',
  full_name='my_remote_procedure_call.FloatNumberMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='my_remote_procedure_call.FloatNumberMessage.item', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=342,
)


_STRINGMESSAGE = _descriptor.Descriptor(
  name='StringMessage',
  full_name='my_remote_procedure_call.StringMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='my_remote_procedure_call.StringMessage.item', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=373,
)


_BOOLEANMESSAGE = _descriptor.Descriptor(
  name='BooleanMessage',
  full_name='my_remote_procedure_call.BooleanMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='my_remote_procedure_call.BooleanMessage.item', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=405,
)


_MYOBJECT = _descriptor.Descriptor(
  name='MyObject',
  full_name='my_remote_procedure_call.MyObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nameAttribute', full_name='my_remote_procedure_call.MyObject.nameAttribute', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ageAttribute', full_name='my_remote_procedure_call.MyObject.ageAttribute', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isNicePersonAttribute', full_name='my_remote_procedure_call.MyObject.isNicePersonAttribute', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=493,
)


_OBJECTMESSAGE = _descriptor.Descriptor(
  name='ObjectMessage',
  full_name='my_remote_procedure_call.ObjectMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='my_remote_procedure_call.ObjectMessage.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=560,
)

_OBJECTMESSAGE.fields_by_name['item'].message_type = _MYOBJECT
DESCRIPTOR.message_types_by_name['IntNumberMessage'] = _INTNUMBERMESSAGE
DESCRIPTOR.message_types_by_name['TenIntNumbersMessage'] = _TENINTNUMBERSMESSAGE
DESCRIPTOR.message_types_by_name['LongIntNumberMessage'] = _LONGINTNUMBERMESSAGE
DESCRIPTOR.message_types_by_name['FloatNumberMessage'] = _FLOATNUMBERMESSAGE
DESCRIPTOR.message_types_by_name['StringMessage'] = _STRINGMESSAGE
DESCRIPTOR.message_types_by_name['BooleanMessage'] = _BOOLEANMESSAGE
DESCRIPTOR.message_types_by_name['MyObject'] = _MYOBJECT
DESCRIPTOR.message_types_by_name['ObjectMessage'] = _OBJECTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IntNumberMessage = _reflection.GeneratedProtocolMessageType('IntNumberMessage', (_message.Message,), dict(
  DESCRIPTOR = _INTNUMBERMESSAGE,
  __module__ = 'my_remote_procedure_call_pb2'
  # @@protoc_insertion_point(class_scope:my_remote_procedure_call.IntNumberMessage)
  ))
_sym_db.RegisterMessage(IntNumberMessage)

TenIntNumbersMessage = _reflection.GeneratedProtocolMessageType('TenIntNumbersMessage', (_message.Message,), dict(
  DESCRIPTOR = _TENINTNUMBERSMESSAGE,
  __module__ = 'my_remote_procedure_call_pb2'
  # @@protoc_insertion_point(class_scope:my_remote_procedure_call.TenIntNumbersMessage)
  ))
_sym_db.RegisterMessage(TenIntNumbersMessage)

LongIntNumberMessage = _reflection.GeneratedProtocolMessageType('LongIntNumberMessage', (_message.Message,), dict(
  DESCRIPTOR = _LONGINTNUMBERMESSAGE,
  __module__ = 'my_remote_procedure_call_pb2'
  # @@protoc_insertion_point(class_scope:my_remote_procedure_call.LongIntNumberMessage)
  ))
_sym_db.RegisterMessage(LongIntNumberMessage)

FloatNumberMessage = _reflection.GeneratedProtocolMessageType('FloatNumberMessage', (_message.Message,), dict(
  DESCRIPTOR = _FLOATNUMBERMESSAGE,
  __module__ = 'my_remote_procedure_call_pb2'
  # @@protoc_insertion_point(class_scope:my_remote_procedure_call.FloatNumberMessage)
  ))
_sym_db.RegisterMessage(FloatNumberMessage)

StringMessage = _reflection.GeneratedProtocolMessageType('StringMessage', (_message.Message,), dict(
  DESCRIPTOR = _STRINGMESSAGE,
  __module__ = 'my_remote_procedure_call_pb2'
  # @@protoc_insertion_point(class_scope:my_remote_procedure_call.StringMessage)
  ))
_sym_db.RegisterMessage(StringMessage)

BooleanMessage = _reflection.GeneratedProtocolMessageType('BooleanMessage', (_message.Message,), dict(
  DESCRIPTOR = _BOOLEANMESSAGE,
  __module__ = 'my_remote_procedure_call_pb2'
  # @@protoc_insertion_point(class_scope:my_remote_procedure_call.BooleanMessage)
  ))
_sym_db.RegisterMessage(BooleanMessage)

MyObject = _reflection.GeneratedProtocolMessageType('MyObject', (_message.Message,), dict(
  DESCRIPTOR = _MYOBJECT,
  __module__ = 'my_remote_procedure_call_pb2'
  # @@protoc_insertion_point(class_scope:my_remote_procedure_call.MyObject)
  ))
_sym_db.RegisterMessage(MyObject)

ObjectMessage = _reflection.GeneratedProtocolMessageType('ObjectMessage', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTMESSAGE,
  __module__ = 'my_remote_procedure_call_pb2'
  # @@protoc_insertion_point(class_scope:my_remote_procedure_call.ObjectMessage)
  ))
_sym_db.RegisterMessage(ObjectMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\035grpc.my_remote_procedure_callB\025MyRemoteProcedureCallP\001\242\002\004MRPC'))

_DIFERENTOPERATIONSHANDLER = _descriptor.ServiceDescriptor(
  name='DiferentOperationsHandler',
  full_name='my_remote_procedure_call.DiferentOperationsHandler',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=563,
  serialized_end=1579,
  methods=[
  _descriptor.MethodDescriptor(
    name='takeIntNumber_ReturnIntNumber',
    full_name='my_remote_procedure_call.DiferentOperationsHandler.takeIntNumber_ReturnIntNumber',
    index=0,
    containing_service=None,
    input_type=_INTNUMBERMESSAGE,
    output_type=_INTNUMBERMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='takeIntNumbers_ReturnIntNumber',
    full_name='my_remote_procedure_call.DiferentOperationsHandler.takeIntNumbers_ReturnIntNumber',
    index=1,
    containing_service=None,
    input_type=_TENINTNUMBERSMESSAGE,
    output_type=_INTNUMBERMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='takeIntNumber_ReturnIntNumbers',
    full_name='my_remote_procedure_call.DiferentOperationsHandler.takeIntNumber_ReturnIntNumbers',
    index=2,
    containing_service=None,
    input_type=_INTNUMBERMESSAGE,
    output_type=_TENINTNUMBERSMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='takeLongIntNumber_ReturnLongIntNumbers',
    full_name='my_remote_procedure_call.DiferentOperationsHandler.takeLongIntNumber_ReturnLongIntNumbers',
    index=3,
    containing_service=None,
    input_type=_LONGINTNUMBERMESSAGE,
    output_type=_LONGINTNUMBERMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='takeFloatNumber_ReturnFloatNumber',
    full_name='my_remote_procedure_call.DiferentOperationsHandler.takeFloatNumber_ReturnFloatNumber',
    index=4,
    containing_service=None,
    input_type=_FLOATNUMBERMESSAGE,
    output_type=_FLOATNUMBERMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='takeString_ReturnString',
    full_name='my_remote_procedure_call.DiferentOperationsHandler.takeString_ReturnString',
    index=5,
    containing_service=None,
    input_type=_STRINGMESSAGE,
    output_type=_STRINGMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='takeBoolean_ReturnBoolean',
    full_name='my_remote_procedure_call.DiferentOperationsHandler.takeBoolean_ReturnBoolean',
    index=6,
    containing_service=None,
    input_type=_BOOLEANMESSAGE,
    output_type=_BOOLEANMESSAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='takeObject_ReturnObject',
    full_name='my_remote_procedure_call.DiferentOperationsHandler.takeObject_ReturnObject',
    index=7,
    containing_service=None,
    input_type=_OBJECTMESSAGE,
    output_type=_OBJECTMESSAGE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIFERENTOPERATIONSHANDLER)

DESCRIPTOR.services_by_name['DiferentOperationsHandler'] = _DIFERENTOPERATIONSHANDLER

# @@protoc_insertion_point(module_scope)
