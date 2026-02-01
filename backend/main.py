from datetime import datetime

from bson import ObjectId
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .db import lifespan
from .models import itemIn  # , itemOut

app = FastAPI(lifespan=lifespan)

# Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    print("Root endpoint accessed")
    return {"message": "This is the backend server."}


@app.get("/get_items/latest")
async def get_latest_item():
    item = await app.state.db.items.find_one({}, sort=[("created_at", -1)])
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/get_items/{name}")
async def get_items(name: str):
    item = await app.state.db.items.find_one({"name": name})
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/set_items")
async def create_item(payload: itemIn):
    doc = payload.model_dump()
    doc.update({"_id": str(ObjectId()), "created_at": datetime.now()})
    await app.state.db.items.insert_one(doc)
    return {"message": "Item created successfully."}
