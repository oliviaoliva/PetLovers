# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pets.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'pets.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\npets.proto\x12\x04pets\"\x89\x01\n\x03Pet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05photo\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\r\n\x05\x62reed\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\t\x12\x0b\n\x03sex\x18\x07 \x01(\t\x12\x10\n\x08neutered\x18\x08 \x01(\x08\x12\x0f\n\x07ownerId\x18\t \x01(\t\"#\n\x08PetsList\x12\x17\n\x04pets\x18\x01 \x03(\x0b\x32\t.pets.Pet\"\x87\x01\n\rAddPetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05photo\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\r\n\x05\x62reed\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\t\x12\x0b\n\x03sex\x18\x06 \x01(\t\x12\x10\n\x08neutered\x18\x07 \x01(\x08\x12\x0f\n\x07ownerId\x18\x08 \x01(\t\"\x83\x01\n\x0e\x41\x64\x64PetResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05photo\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\r\n\x05\x62reed\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\t\x12\x0b\n\x03sex\x18\x07 \x01(\t\x12\x10\n\x08neutered\x18\x08 \x01(\x08\"\x85\x01\n\x10UpdatePetRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05photo\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\r\n\x05\x62reed\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\t\x12\x0b\n\x03sex\x18\x07 \x01(\t\x12\x10\n\x08neutered\x18\x08 \x01(\x08\"\x1e\n\x10\x44\x65letePetRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1d\n\x0cPetIdRequest\x12\r\n\x05petId\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\xf9\x01\n\nPetService\x12\'\n\x08ListPets\x12\x0b.pets.Empty\x1a\x0e.pets.PetsList\x12\x33\n\x06\x41\x64\x64Pet\x12\x13.pets.AddPetRequest\x1a\x14.pets.AddPetResponse\x12.\n\tUpdatePet\x12\x16.pets.UpdatePetRequest\x1a\t.pets.Pet\x12\x30\n\tDeletePet\x12\x16.pets.DeletePetRequest\x1a\x0b.pets.Empty\x12+\n\nGetPetById\x12\x12.pets.PetIdRequest\x1a\t.pets.Petb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pets_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PET']._serialized_start=21
  _globals['_PET']._serialized_end=158
  _globals['_PETSLIST']._serialized_start=160
  _globals['_PETSLIST']._serialized_end=195
  _globals['_ADDPETREQUEST']._serialized_start=198
  _globals['_ADDPETREQUEST']._serialized_end=333
  _globals['_ADDPETRESPONSE']._serialized_start=336
  _globals['_ADDPETRESPONSE']._serialized_end=467
  _globals['_UPDATEPETREQUEST']._serialized_start=470
  _globals['_UPDATEPETREQUEST']._serialized_end=603
  _globals['_DELETEPETREQUEST']._serialized_start=605
  _globals['_DELETEPETREQUEST']._serialized_end=635
  _globals['_PETIDREQUEST']._serialized_start=637
  _globals['_PETIDREQUEST']._serialized_end=666
  _globals['_EMPTY']._serialized_start=668
  _globals['_EMPTY']._serialized_end=675
  _globals['_PETSERVICE']._serialized_start=678
  _globals['_PETSERVICE']._serialized_end=927
# @@protoc_insertion_point(module_scope)
