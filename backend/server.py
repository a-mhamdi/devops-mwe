from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.get("/")
async def root():
    print("Root endpoint accessed")
    return {"message": "This is the backend server."}


@app.get("/get_items/")
async def get_items():
    print("get_items endpoint accessed")
    return [{"name": "Item1", "price": 10.0}, {"name": "Item2", "price": 20.0}]


@app.post("/set_items/")
async def create_item(item: Item):
    print(f"Received item: {item}")
    return item
