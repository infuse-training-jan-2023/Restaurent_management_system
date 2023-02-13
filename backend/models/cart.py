from pydantic import BaseModel, Field

class Item(BaseModel):
    item_name: str
    quantity: int
    price: int
    total: int = None

class Cart(BaseModel):
    user_name: str = Field(...)
    items: list[Item] = Field(...)
    grand_total: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "user_name": "Jane Doe",
                "items": [{"item_name": "samosa", "quantity":1, "price": 0, "total": 1 * 1}],
                "grand_total": 0
            }
        }

