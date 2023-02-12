import sys
sys.path.append("../")

from models.model import *
import json
from datetime import datetime
import base64

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
        orders["status"] = "prep"
        orders["date"] = datetime.now()
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
        raise Exception("Error: database connection failure")

async def fetch_all_tables():
    tables = []
    cursor = tables_data.find({})
    async for document in cursor:
        tables.append(Tables(**document))
    return tables

async def update_tables(table_no,capicity,date,from_date,to_date,available,price):
    await tables_data.update_one({'table_no':table_no},{"$set":{'capicity':capicity,'date':date, 'from_time':from_date, 'to_time':to_date,'available':available, 'price':price}})
    table = await tables_data.find_one({"table_no":table_no})
    return table

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

async def update_cart(data):
    try:
        username = data["user_name"]
        item = data["items"][0]
        item_name = item["item_name"]
        quantity = item["quantity"]
        price = item["price"]
        total = quantity * price

        cart = await cart_items.find_one({"user_name": username})
        if not cart:
            # create a new cart if the user doesn't have one
            new_cart = {
                "user_name": username,
                "items": [{"item_name": item_name, "quantity": quantity, "price": price, "total": total}],
                "grand_total": total
            }
            result = await cart_items.insert_one(new_cart)
            if result.acknowledged:
                return {"message": "Cart created and item added successfully"}
            else:
                raise {"message": "Cart creation and item add failed"}

        item_exists = False
        for cart_item in cart["items"]:
            if cart_item["item_name"] == item_name:
                item_exists = True
                cart_item["quantity"] = quantity
                cart_item["total"] = total
                break

        if item_exists:
            result = await cart_items.update_one({"_id": cart["_id"]}, {"$set": {"items": cart["items"]}})
            if result.modified_count == 1:
                grand_total = sum([item["total"] for item in cart["items"]])
                result = await cart_items.update_one({"_id": cart["_id"]}, {"$set": {"grand_total": grand_total}})
                return {"msg": "Item updated successfully"}
            else:
                return {"msg": "Item update failed"}
        else:
            result = await cart_items.update_one({"_id": cart["_id"]}, {"$push": {"items": {"item_name": item_name, "quantity": quantity, "price": price, "total": total}}})
            if result.modified_count == 1:
                grand_total = cart["grand_total"] + total
                result = await cart_items.update_one({"_id": cart["_id"]}, {"$set": {"grand_total": grand_total}})
                return {"msg": "Item added successfully"}
            else:
                return {"msg": "Item add failed"}
    except Exception as e:
        raise Exception("Error: Item Update failed")


async def get_all_cart_items():
    try:
        items_in_cart = []
        cursor = cart_items.find({})
        async for document in cursor:
            items_in_cart.append(AddToCart(**document))
        return items_in_cart
    except Exception as e:
        raise Exception('Error occured: database connection failure')


async def get_a_cart_item(user_name):
    try:
        cursor = await cart_items.find_one({"user_name": user_name})
        print(cursor)
        return cursor
    except Exception as e:
        raise Exception('Error occured: database connection failure')

async def delete_item_in_cart(username, item_name):
    try:
        cart = await cart_items.find_one({"user_name": username})
        if cart:
            item_exists = False
            for cart_item in cart["items"]:
                if cart_item["item_name"] == item_name:
                    item_exists = True
                    break
            if item_exists:
                result = await cart_items.update_one({"user_name": username}, {"$pull": {"items": {"item_name": item_name}}})
                if result.modified_count == 1:
                    items = cart["items"]
                    items = [item for item in items if item["item_name"] != item_name]
                    if len(items) == 0:
                        result = await cart_items.delete_one({"user_name": username})
                        return {"msg": "Cart deleted as it was empty"}
                    else:
                        grand_total = sum([item["total"] for item in items])
                        result = await cart_items.update_one({"user_name": username}, {"$set": {"items": items, "grand_total": grand_total}})
                        return {"msg": "Item deleted successfully"}
                else:
                    return {"msg": "Item deletion failed"}
            else:
                return {"msg": "Item not found in the cart"}
        else:
            return {"Error": "User not found"}
    except Exception as e:
        raise Exception('Error occured: database connection failure')

