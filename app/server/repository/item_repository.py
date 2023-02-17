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
    pepsi = await get_image("server/images/d1.png")
    coke = await get_image("server/images/d2.png")
    redbull = await get_image("server/images/d3.png")
    coldcoffe = await get_image("server/images/d4.png")
    raspberrypunch = await get_image("server/images/d5.png")
    kiwiSmoothie = await get_image("server/images/d6.png")
    pizza = await get_image("server/images/p2.png")
    sandwich = await get_image("server/images/s5.png")
    wrap = await get_image("server/images/sh4.png")
    burger = await get_image("server/images/b5.png")
    d1 = await get_image("server/images/dinner5.png")
    d2 = await get_image("server/images/dinner2.png")
    d3 = await get_image("server/images/lunch5.png")

    items = values = [
        {"item_name": "Pepsi", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 120, "quantity": 1, "img": pepsi, "tag": "beverages", "type": "veg"},
        {"item_name": "Coke", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 140, "quantity": 1, "img": coke, "tag": "beverages", "type": "veg"},
        {"item_name": "Red Bull", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 180, "quantity": 1, "img": redbull, "tag": "beverages", "type": "veg"},
        {"item_name": "Cold Coffee", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 450, "quantity": 1, "img": coldcoffe, "tag": "beverages", "type": "veg"},
        {"item_name": "Raspberry Punch", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 300, "quantity": 1, "img": raspberrypunch, "tag": "beverages", "type": "veg"},
        {"item_name": "Kiwi Smootie", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 500, "quantity": 1, "img": kiwiSmoothie, "tag": "beverages", "type": "veg"},
        {"item_name": "Chicken and Veggie with Microgreens", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 450, "quantity": 1, "img": d1, "tag": "meals", "type": "non-veg"},
        {"item_name": "Grilled Salmon Salad", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 250, "quantity": 1, "img": d2, "tag": "meals", "type": "non-veg"},
        {"item_name": "Chicken Platter with corn and fries", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 560, "quantity": 1, "img": d3, "tag": "meals", "type": "non-veg"},
        {"item_name": "Burger", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 150, "quantity": 1, "img": burger, "tag": "snacks", "type": "veg"},
        {"item_name": "Chicken Wrap", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 180, "quantity": 1, "img": wrap, "tag": "snacks", "type": "non-veg"},
        {"item_name": "Pizza", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 100, "quantity": 1, "img": pizza, "tag": "snacks", "type": "veg"},
        {"item_name": "Sandwich", "description": "Pepsi has a slight citrusy tang that makes it taste crisp and delicious.",
            "price": 80, "quantity": 1, "img": sandwich, "tag": "snacks", "type": "veg"},
    ]
    item = item_collection.insert_many(items)
    return ('Item add seccessfully')


async def fetch_all_items() -> list:
    try:
        data = [_item_helper(item) async for item in item_collection.find()]
        return data if data else None
    except Exception as e:
        raise Exception('Error occured: ', e)
