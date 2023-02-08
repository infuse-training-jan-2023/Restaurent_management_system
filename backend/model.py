from pydantic import BaseModel


class Orders(BaseModel):
    items: list
    price: list
    timestamp: str
    status: bool

