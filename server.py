import grpc
from concurrent import futures
import pets_pb2
import pets_pb2_grpc
from pymongo import MongoClient
from bson import ObjectId
import time
from event_publisher import EventPublisher  

client = MongoClient("mongodb://localhost:27017/")
db = client["petlovers_db"]
pets_collection = db["pets"]

event_publisher = EventPublisher()

class PetService(pets_pb2_grpc.PetServiceServicer):

    def ListPets(self, request, context):
        """Lista todos os pets"""
        pets = []
        for pet_doc in pets_collection.find():
            pets.append(pets_pb2.Pet(
                id=str(pet_doc["_id"]),
                name=pet_doc.get("name", ""),
                photo=pet_doc.get("photo", ""),
                type=pet_doc.get("type", ""),
                breed=pet_doc.get("breed", ""),
                size=pet_doc.get("size", ""),
                sex=pet_doc.get("sex", ""),
                neutered=pet_doc.get("neutered", False),
                ownerId=pet_doc.get("owner_id", "")
            ))
        return pets_pb2.PetsList(pets=pets)

    def AddPet(self, request, context):
        """Cria um novo pet e publica um evento PetCreated"""
        new_pet = {
            "name": request.name,
            "photo": request.photo,
            "type": request.type,
            "breed": request.breed,
            "size": request.size,
            "sex": request.sex,
            "neutered": request.neutered,
            "owner_id": str(request.ownerId),  
            "created_at": int(time.time())
        }
        result = pets_collection.insert_one(new_pet)
        pet_id = str(result.inserted_id)

        event_data = {
            "eventType": "PetCreated",
            "petId": pet_id,
            "ownerId": str(request.ownerId),
            "name": request.name,
            "breed": request.breed,
            "timestamp": int(time.time())
        }

        event_publisher.publish_event("pet.created", event_data)

        return pets_pb2.Pet(
            id=pet_id,
            name=request.name,
            photo=request.photo,
            type=request.type,
            breed=request.breed,
            size=request.size,
            sex=request.sex,
            neutered=request.neutered
        )

    def GetPetById(self, request, context):
        """Busca um pet pelo ID e retorna todos os detalhes"""
        pet = pets_collection.find_one({"_id": ObjectId(request.petId)})
        if not pet:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Pet não encontrado")
            return pets_pb2.Pet()

        return pets_pb2.Pet(
            id=str(pet["_id"]),
            name=pet["name"],
            breed=pet["breed"],
            ownerId=pet["owner_id"],
            photo=pet.get("photo", ""),
            type=pet.get("type", ""),
            size=pet.get("size", ""),
            sex=pet.get("sex", ""),
            neutered=pet.get("neutered", False)
        )
    
    def DeletePet(self, request, context):
        try:
            filter_ = {"_id": ObjectId(request.id)}
            pets_collection.delete_one(filter_)
            return pets_pb2.Empty()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return pets_pb2.Empty() 
        
    def UpdatePet(self, request, context):
        try:
            filter_ = {"_id": ObjectId(request.id)}
            updated_data = {
                "name": request.name,
                "breed": request.breed,
                "photo": request.photo,
                "type": request.type,
                "size": request.size,
                "sex": request.sex,
                "neutered": request.neutered
            }
            pets_collection.update_one(filter_, {"$set": updated_data})
            return pets_pb2.Pet(
                id=request.id,
                name=request.name,
                breed=request.breed,
                photo=request.photo,
                type=request.type,
                size=request.size,
                sex=request.sex,
                neutered=request.neutered,
                ownerId=""  # ou recupere se necessário
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return pets_pb2.Pet()



def serve():
    """Inicia o servidor gRPC"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pets_pb2_grpc.add_PetServiceServicer_to_server(PetService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("🐶 Pet Service gRPC server started on port 50051.")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
