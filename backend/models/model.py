from pydantic import BaseModel

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
    date: str

class Tables(BaseModel):
    user_name: str
    table_no: int
    capicity: int
    date: str
    price: int
    slot: str
    
