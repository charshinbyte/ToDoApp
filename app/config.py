from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
print("MONGO_URI:", MONGO_URI)
client = AsyncIOMotorClient(MONGO_URI)
    
db = client.task_db
collection = db["task_data"]
