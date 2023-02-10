import sys
sys.path.append("../")

from models.model import Tables
import json
from models.model import Orders
from datetime import datetime
from models.model import Items
import base64

#MONGOBD driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://anas_ahmed:mongo123@restaurant.xw2cat1.mongodb.net')

database = client.Restaurant
order_db = database.orders
tables_data = database.table
collection = database.items

async def insert_order(orders):
    try:
        date = datetime.utcnow()
        orders["date"] = date
        orders["status"] = "prep"
        await order_db.insert_one(orders)
        return orders
    except Exception as e:
        raise Exception("Error: ", e.__format__)

async def get_orders():
    try:
        orders = []
        result = order_db.find({})
        async for items in result:
            orders.append(Orders(**items))
        return orders
    except Exception as e:
        raise Exception("Error: ", e)


async def fetch_all_tables():
    tables = []
    cursor = tables_data.find({})

    async for document in cursor:
        tables.append(Tables(**document))
    return tables


async def create_table(table):
    document = table
    await tables_data.insert_one(document)
    return document

async def get_image(file):
    with open(file, "rb") as imageFile:
        value = base64.b64encode(imageFile.read())
    return value


async def insert_items():
    samosa = await  get_image("../images/samosa.webp")
    vadapav = await get_image("../images/Vada-Pav-scaled.jpg")
    values = [
        {"item_name":"samosa", "description": "A fried South Asian pastry with a savoury filling, including ingredients such as spiced potatoes, onions, and peas.","price":20,"quantity":2,"img": samosa,"tag":"snacks","type":"veg"},
        {"item_name":"Vadapav", "description": "The dish consists of a deep fried potato dumpling placed inside a bread bun.","price":30,"quantity":2,"img": vadapav,"tag":"snacks","type":"veg"}
    ]
    collection.insert_many(values)


async def fetch_all_items():
    try:
        items = []
        cursor = collection.find({})
        async for document in cursor:
            items.append(Items(**document))
        return items
    except Exception as e:
        raise Exception('Error occured: ',e)
