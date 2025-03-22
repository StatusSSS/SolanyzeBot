import aio_pika
from src.core.config import settings




async def get_connection_and_channel():
    amqp_url = f"amqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{settings.RABBITMQ_HOST}:5672/"
    connection = await aio_pika.connect_robust(url=amqp_url)
    channel = await connection.channel()
    await channel.declare_queue("wallet_events", durable=True)
    print("Connect to RabbitMQ")
    return connection, channel


async def send_message(event_type, wallet, user_id):
    connection, channel = await get_connection_and_channel()
    message = f"{event_type}: User ID: {user_id}, Wallet: {wallet}"
    await channel.default_exchange.publish(
        message=aio_pika.Message(message.encode()),
        routing_key="wallet_events",
    )
    print(" [X] Message sent")

    await channel.close()
    await connection.close()