import sys
sys.path.append("../")

from ._client import get_collection
from models.table import Tables

table_collection = get_collection('table')

async def fetch_all_tables():
    tables = []
    cursor = table_collection.find({})
    async for document in cursor:
        tables.append(Tables(**document))
    return tables

async def update_tables(table_no,capicity,price,date,slot):
    await table_collection.update_one({'table_no':table_no},{"$set":{'capicity':capicity,'price':price,'date':date,'slot':slot}})
    table = await table_collection.find_one({"table_no":table_no})
    return table

async def create_table(table):
    document = table
    await table_collection.insert_one(document)
    return document