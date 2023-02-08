from model import Orders

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.Resturant
collection = database.orders


async def orders_data(items):
    document = items
    result = await collection.insert_one(document)
    return document
