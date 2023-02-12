from pydantic import BaseModel, Field
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

class OrderList(BaseModel):
    user_name: str = Field(...)
    items: list = Field(...)
    grand_total: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "user_name": "Jane Doe",
                "items": [{"item_name": "samosa", "quantity":1, "price": 0, "total": 0}],
                "grand_total": 0
            }
        }

class Tables(BaseModel):
    table_no: int
    capicity: int
    date: str
    from_time: str
    to_time: str
    available: bool
    price: int

class Item(BaseModel):
    item_name: str
    quantity: int
    price: int
    total: int = None

class AddToCart(BaseModel):
    user_name: str = Field(...)
    items: list[Item] = Field(...)
    grand_total: int = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "user_name": "Jane Doe",
                "items": [{"item_name": "samosa", "quantity":1, "price": 0, "total": 0}],
                "grand_total": 0
            }
        }

