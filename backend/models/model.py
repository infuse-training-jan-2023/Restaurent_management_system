from pydantic import BaseModel

class Tables(BaseModel):
    capicity: int
    date: str
    from_time: str
    to_time: str
    available: bool
    price: int
