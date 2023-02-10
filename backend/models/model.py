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
    table_no: int
    capicity: int
    date: str
    from_time: str
    to_time: str
    available: bool
    price: int

# from bson import ObjectId

# class Items(BaseModel):
#     def __init__(self, item_name, description, price, quantity, img, tag, type):
#         self.item_name = item_name
#         self.description = description
#         self.price = price
#         self.quantity = quantity
#         self.img = img
#         self.tag = tag
#         self.type = type

# class Orders(BaseModel):
#     def __init__(self, items, status, date, table_id):
#         self.items = items
#         self.status = status
#         self.date = date
#         self.table_id = ObjectId(table_id)

# class Tables(BaseModel):
#     def __init__(self, table_no, capicity, date, from_time, to_time, available):
#         self.table_no = table_no
#         self.capicity = capicity
#         self.date = date
#         self.from_time = from_time
#         self.to_time = to_time
#         self.available = available
