# import sys
# sys.path.append("../")

# from models.item import *
# from ._client import get_collection
# import base64

# item_collection = get_collection("item")

# async def get_image(file):
#     with open(file, "rb") as imageFile:
#         value = base64.b64encode(imageFile.read())
#     return value

# async def insert_items():
#     samosa = await  get_image("../images/samosa.webp")
#     vadapav = await get_image("../images/Vada-Pav-scaled.jpg")
#     values = [
#         {"item_name":"samosa", "description": "A fried South Asian pastry with a savoury filling, including ingredients such as spiced potatoes, onions, and peas.","price":20,"quantity":2,"img": samosa,"tag":"snacks","type":"veg"},
#         {"item_name":"Vadapav", "description": "The dish consists of a deep fried potato dumpling placed inside a bread bun.","price":30,"quantity":2,"img": vadapav,"tag":"snacks","type":"veg"}
#     ]
#     item_collection.insert_many(values) 

# async def fetch_all_items():
#     try:
#         items = []
#         cursor = item_collection.find({})
#         async for document in cursor:
#             items.append(Items(**document))
#         return items
#     except Exception as e:
#         raise Exception('Error occured: ',e)
