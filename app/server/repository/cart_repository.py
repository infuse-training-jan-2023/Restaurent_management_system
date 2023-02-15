from ._client import get_collection

cart_collection = get_collection("cart")

def _cart_helper(cart_items: dict) -> dict:
    return {
        "id": str(cart_items["_id"]),
        "username": cart_items["user_name"],
        "items": cart_items["items"], # is a lst
        "grand_total": cart_items["grand_total"]
    }

async def add_to_cart(cart_data: dict) -> dict:
    try:
        result = await cart_collection.insert_one(cart_data)
        return result
    except Exception as e:
        raise Exception("Error: ", e.__format__)

async def update_or_add_cart(data: dict) -> dict:
    try:
        username = data["user_name"]
        item = data["items"][0]
        item_name = item["item_name"]
        quantity = item["quantity"]
        price = item["price"]
        total = quantity * price

        cart = await cart_collection.find_one({"user_name": username})
        if not cart:
            # create a new cart if the user doesn't have one
            new_cart = {
                "user_name": username,
                "items": [{"item_name": item_name, "quantity": quantity, "price": price, "total": total}],
                "grand_total": total
            }
            result = await add_to_cart(new_cart)
            result = await cart_collection.find_one({"_id": result.inserted_id})
            return _cart_helper(result)

        item_exists = False
        for cart_item in cart["items"]:
            if cart_item["item_name"] == item_name:
                item_exists = True
                cart_item["quantity"] = quantity
                cart_item["total"] = total
                break

        if item_exists:
            result = await cart_collection.update_one({"_id": cart["_id"]}, {"$set": {"items": cart["items"]}})
            if result.modified_count == 1:
                grand_total = sum([item["total"] for item in cart["items"]])
                await cart_collection.update_one({"_id": cart["_id"]}, {"$set": {"grand_total": grand_total}})
                result = await cart_collection.find_one({"_id": cart["_id"]})
                return _cart_helper(result)
        else:
            result = await cart_collection.update_one({"_id": cart["_id"]}, {"$push": {"items": {"item_name": item_name, "quantity": quantity, "price": price, "total": total}}})
            if result.modified_count == 1:
                grand_total = cart["grand_total"] + total
                await cart_collection.update_one({"_id": cart["_id"]}, {"$set": {"grand_total": grand_total}})
                result = await cart_collection.find_one({"_id": cart["_id"]})
                return _cart_helper(result)
    except Exception as e:
        raise Exception("Error: Item Update failed")

async def get_all_cart_items() -> list:
    try:
        data = [_cart_helper(item) async for item in  cart_collection.find()]
        return data if data else None
    except Exception as e:
        raise Exception('Error occured: database connection failure')

async def get_cart_item_by_name(user_name: str) -> dict:
        cart = await cart_collection.find_one({"user_name": user_name})
        if cart:
            return _cart_helper(cart)
        else:
            return None

async def delete_item_in_cart(username: str, item_name:str) -> dict:
    cart = await cart_collection.find_one({"user_name": username})
    if cart:
        item_exists = False
        for cart_item in cart["items"]:
            if cart_item["item_name"] == item_name:
                item_exists = True
                break
        if item_exists:
            result = await cart_collection.update_one({"user_name": username}, {"$pull": {"items": {"item_name": item_name}}})
            if result.modified_count == 1:
                items = cart["items"]
                items = [item for item in items if item["item_name"] != item_name]
                if len(items) == 0:
                    result = await cart_collection.delete_one({"user_name": username})
                    return {"msg": "Cart deleted as it was empty"}
                else:
                    grand_total = sum([item["total"] for item in items])
                    await cart_collection.update_one({"user_name": username}, {"$set": {"items": items, "grand_total": grand_total}})
                    result  = await cart_collection.find_one({"user_name": username})
                    return {"msg": "Item deleted successfully"}
    else:
        return None
