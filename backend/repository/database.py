import sys
sys.path.append("../")

from models.model import *
import json
from datetime import datetime
import base64
from fastapi import HTTPException

#MONGOBD driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://anis:anis%40123@mydb.tpgkpds.mongodb.net')

database = client.Restaurant
order_db = database.orders
tables_data = database.table
collection = database.items
cart_items = database.cart

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

async def addto_cart(cart_data):
    try:
        await cart_items.insert_one(cart_data)
        return cart_data
    except Exception as e:
        raise Exception("Error: ", e.__format__)

async def updatecart(data):
    try:
        # print(data["items"])
        item = data["items"]
        username = data["user_name"]
        item_name=item[0]["item_name"]
        quantity=item[0]["quantity"]
        price=item[0]["price"]
        total = item[0]["total"]

        cart = await cart_items.find_one({"user_name": username})
        if cart:

            item_exists = False
            for item in cart["items"]:
                if item["item_name"] == item_name:
                    item_exists = True
                    item["quantity"] = quantity
                    item["total"] = item["quantity"] * price
                    break
            if item_exists:
                result = await cart_items.update_one({"_id": cart["_id"]}, {"$set": {"items": cart["items"]}})
                if result.modified_count == 1:
                    grand_total = 0
                    for item in cart["items"]:
                        grand_total += item["total"]
                    result = await cart_items.update_one({"_id": cart["_id"]}, {"$set": {"grand_total": grand_total}})
                    return {"msg": "Item Updated successfully"}
                else:
                    return {"msg": "Item Update failed"}
            else:
                new_item = {"item_name": item_name, "quantity": quantity, "price": price, "total": quantity * price}
                result = await cart_items.update_one({"_id": cart["_id"]}, {"$push": {"items": new_item}})
                grand_total = cart["grand_total"] + new_item["total"]
                result = await cart_items.update_one({"_id": cart["_id"]}, {"$set": {"grand_total": grand_total}})

                if result.modified_count == 1:
                    return {"msg": "Item added successfully"}
                else:
                    return {"msg": "Item add failed"}
        else:
            new_cart = {"user_name": username, "items": [{"item_name": item_name, "quantity": quantity, "price": price, "total": quantity * price}], "grand_total": quantity * price}
            result = await cart_items.insert_one(new_cart)
            # Check if the insert was successful
        if result.acknowledged:
            return {"message": "Cart created and item added successfully"}
        else:
            raise HTTPException(status_code=500, detail="Cart creation and item add failed")
    except Exception as e:
        raise Exception('Error occured: ',e.__format__)

async def get_all_cart_items():
    try:
        items_in_cart = []
        cursor = cart_items.find({})
        async for document in cursor:
            items_in_cart.append(AddToCart(**document))
        return items_in_cart
    except Exception as e:
        raise Exception('Error occured: ',e)


async def get_a_cart_item(user_name):
    try:
        cursor = await cart_items.find_one({"user_name": user_name})
        print(cursor)
        return cursor
    except Exception as e:
        raise Exception('Error occured: ',e)
