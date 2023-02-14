import sys
sys.path.append("../")

from ._client import get_collection
from fastapi import HTTPException
from models.cart import *

cart_collection = get_collection("cart")

async def addto_cart(cart_data):
    try:
        await cart_collection.insert_one(cart_data)
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

        cart = await cart_collection.find_one({"user_name": username})
        if cart:

            item_exists = False
            for item in cart["items"]:
                if item["item_name"] == item_name:
                    item_exists = True
                    item["quantity"] = quantity
                    item["total"] = item["quantity"] * price
                    break
            if item_exists:
                result = await cart_collection.update_one({"_id": cart["_id"]}, {"$set": {"items": cart["items"]}})
                if result.modified_count == 1:
                    grand_total = 0
                    for item in cart["items"]:
                        grand_total += item["total"]
                    result = await cart_collection.update_one({"_id": cart["_id"]}, {"$set": {"grand_total": grand_total}})
                    return {"msg": "Item Updated successfully"}
                else:
                    return {"msg": "Item Update failed"}
            else:
                new_item = {"item_name": item_name, "quantity": quantity, "price": price, "total": quantity * price}
                result = await cart_collection.update_one({"_id": cart["_id"]}, {"$push": {"items": new_item}})
                grand_total = cart["grand_total"] + new_item["total"]
                result = await cart_collection.update_one({"_id": cart["_id"]}, {"$set": {"grand_total": grand_total}})

                if result.modified_count == 1:
                    return {"msg": "Item added successfully"}
                else:
                    return {"msg": "Item add failed"}
        else:
            new_cart = {"user_name": username, "items": [{"item_name": item_name, "quantity": quantity, "price": price, "total": quantity * price}], "grand_total": quantity * price}
            result = await cart_collection.insert_one(new_cart)
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
        cursor = cart_collection.find({})
        async for document in cursor:
            items_in_cart.append(Cart(**document))
        return items_in_cart
    except Exception as e:
        raise Exception('Error occured: ',e)


async def get_a_cart_item(user_name):
    try:
        cursor = await cart_collection.find_one({"user_name": user_name})
        print(cursor)
        return cursor
    except Exception as e:
        raise Exception('Error occured: ',e)
