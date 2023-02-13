from pydantic import BaseModel, Field

class Tables(BaseModel):
    table_no: int
    capicity: int
    price: int
    date: str
    slot:str
    