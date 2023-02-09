from pydantic import BaseModel


class Orders(BaseModel):
    items: list
    price: int
    status: str
    date: str
