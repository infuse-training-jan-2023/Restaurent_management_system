from ._client import get_collection
from datetime import datetime

cart_collection = get_collection("cart")
order_history = get_collection("orderhistory")

async def insert_order_history(order: dict) -> dict:
    try:
        order["date"] = datetime.now()
        await order_history.insert_one(order)
        return {"Success": "Order history inserted successfully"}
    except Exception as e:
        raise Exception('Error occured: database connection failure')

async def delete_cart(user_name: str) -> dict:
    try:
        cart = await cart_collection.find_one({"user_name": user_name})
        if cart:
            print(cart)
            await insert_order_history(cart)
            await cart_collection.delete_one({"user_name": user_name})
            return {"msg": "user deleted successfully"}
        else:
            return None
    except:
        return {"Error": "User not found"}
