from pydantic import BaseModel, Field


class Items(BaseModel):
    item_name: str = Field(...)
    description: str = Field(...)
    price: int = Field(...)
    quantity: int = Field(...)
    img: str = Field(...)
    tag: str = Field(...)
    type: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "item_name": "Samosa",
                "description": "Crispy triangular south indian dish with potatoes filled inside",
                "price": 20,
                "quantity": 1,
                "img": "url of img",
                "tag": "snacks",
                "type": "veg"
            }
        }
