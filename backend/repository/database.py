import sys
sys.path.append("../")

from models.model import Tables
import json

#MONGOBD driver
import motor.motor_asyncio

# class TableRepo:

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.Restaurent
tables_data = database.table

async def fetch_all_tables():
    tables = []
    cursor = tables_data.find({})

    # cursor = TableRepo.tables_data.find({})
    async for document in cursor:
        tables.append(Tables(**document))
    return tables

async def fetch_available_tables():
    tables = []
    cursor = tables_data.find({"available":True})
    async for document in cursor:
        print (document["_id"])
        # json_data = {"id":document["_id"],"capicity":document["capicity"],"price":document["price"]}
        # tables.append((json_data))
        # tables.append(document)
    return tables

async def create_table(table):
    document = table
    await tables_data.insert_one(document)
    return document


