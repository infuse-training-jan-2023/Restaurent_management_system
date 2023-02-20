from ._client import get_collection

order_history_collection = get_collection("orderhistory")

def _order_history_helper(cart_items: dict) -> dict:
    return {
        
        "id": str(cart_items["_id"]),
        "username": cart_items["user_name"],
        "items": cart_items["items"],
        "grand_total": cart_items["grand_total"]
    }

async def get_orders_by_name(user_name: str) -> dict:
    data = [_order_history_helper(orders) async for orders in  order_history_collection.find({"user_name": user_name})]
    return data if data else None
