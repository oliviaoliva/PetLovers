import grpc
from concurrent import futures
import pets_pb2
import pets_pb2_grpc

# Implementação do serviço PetService
class PetServiceImpl(pets_pb2_grpc.PetServiceServicer):
    def ListPets(self, request, context):
        # MOCK: lista fixa de pets
        pets_data = [
            {"id": "1", "name": "Rex", "breed": "Labrador"},
            {"id": "2", "name": "Fofinho", "breed": "Poodle"},
            {"id": "3", "name": "Snow", "breed": "Husky"}
        ]

        # Convertendo para objetos Pet definidos no .proto
        pet_list = []
        for p in pets_data:
            pet = pets_pb2.Pet(
                id=p["id"],
                name=p["name"],
                breed=p["breed"]
            )
            pet_list.append(pet)

        return pets_pb2.PetsList(pets=pet_list)

# Configuração do servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pets_pb2_grpc.add_PetServiceServicer_to_server(PetServiceImpl(), server)
    server.add_insecure_port('[::]:50051')  # Porta padrão do gRPC
    server.start()
    print("Pet Service gRPC server started on port 50051.")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
