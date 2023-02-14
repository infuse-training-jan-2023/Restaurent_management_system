import base64
from ._client import get_collection

item_collection = get_collection("item")

def _item_helper(items: dict) -> dict:
    return {
        "id": str(items["_id"]),
        "item_name": items["item_name"],
        "description": items["description"],
        "price": items["price"],
        "quantity": items["quantity"],
        "img": items["img"],
        "tag": items["tag"],
        "type": items["tag"]
    }

async def get_image(file: str) -> str:
    with open(file, "rb") as imageFile:
        base_encoded_img = base64.b64encode(imageFile.read())
    return base_encoded_img

async def insert_items():
    samosa = await  get_image("app/server/images/samosa.webp")
    vadapav = await get_image("app/server/images/Vada-Pav-scaled.jpg")
    items = [
        {"item_name":"coke", "description": "A fried South Asian pastry with a savoury filling, including ingredients such as spiced potatoes, onions, and peas.","price":20,"quantity":2,"img": samosa,"tag":"snacks","type":"veg"},
        {"item_name":"sprite", "description": "The dish consists of a deep fried potato dumpling placed inside a bread bun.","price":30,"quantity":2,"img": vadapav,"tag":"snacks","type":"veg"}
    ]
    item = item_collection.insert_many(items)
    return ('Item add seccessfully')

async def fetch_all_items() -> list:
    try:
        data = [_item_helper(item) async for item in  item_collection.find()]
        return data if data else None
    except Exception as e:
        raise Exception('Error occured: ',e)
