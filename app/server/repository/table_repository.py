from ._client import get_collection
from server.models.tables_model import Tables

table_collection = get_collection('table')

def _table_helper(table_items: dict) -> dict:
    return {
        "id": str(table_items["_id"]),
        "user_name": table_items["user_name"],
        "table_no": table_items["table_no"],
        "capacity": table_items["capacity"],
        "price": table_items["price"],
        "date": table_items["date"],
        "slot": table_items["slot"]
    }

async def fetch_all_tables():
    data = [_table_helper(item) async for item in  table_collection.find()]
    return data if data else None

async def create_table(table: dict) -> dict:
    result = await table_collection.insert_one(table)
    result = await table_collection.find_one({"_id": result.inserted_id})
    return _table_helper(result)
