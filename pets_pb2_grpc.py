# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import pets_pb2 as pets__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in pets_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PetServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListPets = channel.unary_unary(
                '/pets.PetService/ListPets',
                request_serializer=pets__pb2.Empty.SerializeToString,
                response_deserializer=pets__pb2.PetsList.FromString,
                _registered_method=True)
        self.AddPet = channel.unary_unary(
                '/pets.PetService/AddPet',
                request_serializer=pets__pb2.AddPetRequest.SerializeToString,
                response_deserializer=pets__pb2.AddPetResponse.FromString,
                _registered_method=True)


class PetServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListPets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListPets': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPets,
                    request_deserializer=pets__pb2.Empty.FromString,
                    response_serializer=pets__pb2.PetsList.SerializeToString,
            ),
            'AddPet': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPet,
                    request_deserializer=pets__pb2.AddPetRequest.FromString,
                    response_serializer=pets__pb2.AddPetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pets.PetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('pets.PetService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PetService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListPets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pets.PetService/ListPets',
            pets__pb2.Empty.SerializeToString,
            pets__pb2.PetsList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddPet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pets.PetService/AddPet',
            pets__pb2.AddPetRequest.SerializeToString,
            pets__pb2.AddPetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
