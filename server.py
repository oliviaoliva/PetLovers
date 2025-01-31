import grpc
from concurrent import futures
import pets_pb2
import pets_pb2_grpc
from pymongo import MongoClient
import bson

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["petlovers_db"]  
pets_collection = db["pets"]  


class PetService(pets_pb2_grpc.PetServiceServicer):
    def ListPets(self, request, context):
        pets = []
        for pet in pets_collection.find():
            pets.append(pets_pb2.Pet(id=str(pet["_id"]), name=pet["name"], breed=pet["breed"]))
        return pets_pb2.PetsList(pets=pets)

    def AddPet(self, request, context):
        new_pet = {
            "name": request.name,
            "breed": request.breed
        }
        result = pets_collection.insert_one(new_pet)
        return pets_pb2.Pet(id=str(result.inserted_id), name=request.name, breed=request.breed)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pets_pb2_grpc.add_PetServiceServicer_to_server(PetService(), server)
    server.add_insecure_port('[::]:50051')  # Porta padrão do gRPC
    server.start()
    print("Pet Service gRPC server started on port 50051.")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
