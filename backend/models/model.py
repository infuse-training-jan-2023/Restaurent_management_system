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

class Tables(BaseModel):
    table_no: int
    capicity: int
    date: str
    from_time: str
    to_time: str
    available: bool
    price: int

class AddToCart(BaseModel):
    user_name: str = Field(...)
    items: list = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "user_name": "Jane Doe",
                "items": [{"item_name": "samosa", "quantity":1, "price": 0, }]
            }
        }

