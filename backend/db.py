import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app.state.client = AsyncIOMotorClient(MONGODB_URI)
    app.state.db = app.state.client[str(MONGODB_DB)]
    await app.state.db.command("ping")
    print("Connected to MongoDB")
    yield
    # Shutdown
    app.state.client.close()
    print("Disconnected from MongoDB")
