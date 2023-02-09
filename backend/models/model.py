from pydantic import BaseModel

class Orders(BaseModel):
    items: list
    price: int
    status: str
    date: str

class Tables(BaseModel):
    capicity: int
    date: str
    from_time: str
    to_time: str
    available: bool
    price: int
