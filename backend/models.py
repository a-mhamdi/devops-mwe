from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class itemIn(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class itemOut(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    name: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True
