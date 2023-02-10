from pydantic import BaseModel
from datetime import datetime

class Items(BaseModel):
    item_name : str
    description : str
    price : int
    quantity : int
    img : str
    tag : str
    type : str

class Orders(BaseModel):
    items: list
    price: int
    status: str
    date: datetime

class Tables(BaseModel):
    table_no: int
    capicity: int
    date: str
    from_time: str
    to_time: str
    available: bool
    price: int
