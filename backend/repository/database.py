
import sys
sys.path.append("../")

from models.item import *
from ._client import get_collection
import base64
import motor.motor_asyncio

def _get_client():
    mongo_local_url = "mongodb://localhost:27017"
    mongo_cluster_url = 'mongodb+srv://dinesh_gawas:mongo123@restaurant.xw2cat1.mongodb.net/'
    client = motor.motor_asyncio.AsyncIOMotorClient(mongo_cluster_url)
    return client.Restaurant

def get_collection(collection: str):
    client = _get_client()    
    return client.get_collection(collection)


item_collection = get_collection("item")

async def get_image(file):
    with open(file, "rb") as imageFile:
        value = base64.b64encode(imageFile.read())
    return value

async def insert_items():
    samosa = await  get_image("../images/beverages/d1.png")
    vadapav = await get_image("../images/beverages/d2.png")
    values = [
        {"item_name":"coke", "description": "A fried South Asian pastry with a savoury filling, including ingredients such as spiced potatoes, onions, and peas.","price":20,"quantity":2,"img": samosa,"tag":"snacks","type":"veg"},
        {"item_name":"sprite", "description": "The dish consists of a deep fried potato dumpling placed inside a bread bun.","price":30,"quantity":2,"img": vadapav,"tag":"snacks","type":"veg"}
    ]
    item_collection.insert_many(values) 

async def fetch_all_items():
    try:
        items = []
        cursor = item_collection.find({})
        async for document in cursor:
            items.append(Items(**document))
        return items
    except Exception as e:
        raise Exception('Error occured: ',e)