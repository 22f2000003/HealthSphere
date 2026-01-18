import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = None
db = None
users_collection = None

def connect_db():
    global client, db, users_collection

    if not MONGO_URI or not DB_NAME:
        print("⚠️ MongoDB env vars not set")
        return

    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        users_collection = db["users"]
        print("✅ MongoDB connected successfully")
    except Exception as e:
        print("❌ MongoDB connection failed:", e)
