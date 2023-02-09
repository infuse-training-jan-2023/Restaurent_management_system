import sys
sys.path.append("../")

from models.model import Tables
import json
from models.model import Orders
from datetime import datetime

#MONGOBD driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.Resturant
order_db = database.orders
tables_data = database.table

async def insert_order(orders):
    try:
        date = str(datetime.utcnow())
        orders["date"] = date
        orders["status"] = "prep"
        await order_db.insert_one(orders)
        return orders
    except Exception as e:
        raise Exception("Error: ", e)

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
