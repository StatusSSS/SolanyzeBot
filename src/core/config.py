import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
    RABBITMQ_USER = os.getenv("RABBITMQ_USER")
    RABBITMQ_PASS = os.getenv("RABBITMQ_PASSWORD")



settings = Settings()