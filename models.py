from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from fastapi.responses import FileResponse

class Opinion(BaseModel):
    id: int
    rating: int
    date: datetime
    description: Optional[str]

class SalesTip(BaseModel):
    id: int
    description: str

class Orders(BaseModel):
    unpaid: int
    unsent: int
    refunds: int
    pending: int

class Offer(BaseModel):
    id: int
    photo: FileResponse
    description: str
    sold: int
    turnover: int
    views: int

    class Config:
        arbitrary_types_allowed = True

class SalesQuality(BaseModel):
    category: str
    rating: int
    aspect: List[str]


