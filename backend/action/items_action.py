import sys
from models.model import Items
sys.path.append("../")
from repository.database import fetch_all_items , insert_items
import json

class ItemActions:
 async def get_all_items():
    try:
      items = []
      cursor = await fetch_all_items()
      #items.append(Items(**cursor))
      cursor= json.loads(cursor)
      for document in cursor:
       items.append(Items(**document))
      return items
    except Exception as e:
     raise Exception('Error occured: ',e)

async def insert_items():
    insert_items
    
