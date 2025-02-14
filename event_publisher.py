import pika
import json

class EventPublisher:
    def __init__(self):
        """Inicializa a conexão com RabbitMQ e declara exchange"""
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
            self.channel = self.connection.channel()

            #Exchange do tipo "topic"
            self.channel.exchange_declare(exchange="pet-exchange", exchange_type="topic", durable=True)

            self.channel.queue_declare(queue="pet_created", durable=True)
            self.channel.queue_declare(queue="pet_updated", durable=True)

            self.channel.queue_bind(exchange="pet-exchange", queue="pet_created", routing_key="pet.created")
            self.channel.queue_bind(exchange="pet-exchange", queue="pet_updated", routing_key="pet.updated")

            print("✅ Conectado ao RabbitMQ e filas declaradas.")

        except Exception as e:
            print(f"❌ Erro ao conectar ao RabbitMQ: {e}")

    def publish_event(self, routing_key, event_data):
        """Publica um evento no RabbitMQ"""
        try:
            if self.channel.is_open:
                self.channel.basic_publish(
                    exchange="pet-exchange",
                    routing_key=routing_key,
                    body=json.dumps(event_data),
                    properties=pika.BasicProperties(
                        delivery_mode=2 #persistencia
                    )
                )
                print(f"📢 Evento publicado: {routing_key} -> {event_data}")
            else:
                print("⚠ Conexão com RabbitMQ fechada. Tentando reconectar...")
                self.__init__()
                self.publish_event(routing_key, event_data)

        except Exception as e:
            print(f"❌ Erro ao publicar evento no RabbitMQ: {e}")

    def close(self):
        """Fecha a conexão com RabbitMQ"""
        if self.connection.is_open:
            self.connection.close()
            print("🔌 Conexão com RabbitMQ fechada.")
