from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from fastapi.responses import FileResponse


class User(BaseModel):
    id: int
    username: str
    password: str

class Opinion(BaseModel):
    id: int
    user_id: int
    rating: int
    date: datetime
    description: Optional[str]

class SalesTip(BaseModel):
    id: int
    user_id: int
    description: str

class Orders(BaseModel):
    user_id: int
    unpaid: int
    unsent: int
    refunds: int
    pending: int

class Offer(BaseModel):
    id: int
    user_id: int
    name: str
    photoBytes: str
    sold: int
    turnover: int
    views: int

class SalesQuality(BaseModel):
    user_id: int
    category: str
    rating: int
    aspect: List[str]

class DailyTip(BaseModel):
    id: int
    user_id: int
    tip : str

class Revenue(BaseModel):
    id :int
    user_id : int
    date :datetime
    n : float

class Turnover(BaseModel):
    id :int
    user_id : int
    date :datetime
    n : int