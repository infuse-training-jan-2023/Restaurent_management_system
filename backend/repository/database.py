# import sys
# sys.path.append("../")
from models.model import Orders
from datetime import datetime

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.Resturant
order_db = database.orders

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
