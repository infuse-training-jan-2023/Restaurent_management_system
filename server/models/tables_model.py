from pydantic import BaseModel, Field

class Tables(BaseModel):
    user_name: str = Field(...)
    table_no: int = Field(...)
    capacity: int = Field(...)
    price: int = Field(...)
    date: str = Field(...)
    slot:str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "user_name": "Jane Doe",
                "table_no": 1,
                "capacity": 2,
                "price": 2000,
                "date": "2020-01-01",
                "slot": "Evening"
            }
        }


class DeleteTables(BaseModel):
    user_name: str = Field(...)
    table_no: int = Field(...)
    date: str = Field(...)
    slot:str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "user_name": "Jane Doe",
                "table_no": 1,
                "date": "2020-01-01",
                "slot": "Evening"
            }
        }