from server.models.cart_model import Cart
from server.models.response_model import ResponseModel
from server.models.error_model import ErrorResponseModel
from server.repository.cart_repository import *
from fastapi.encoders import jsonable_encoder
from fastapi import Body, APIRouter

router = APIRouter()


@router.post("", response_description="cart items added into the database")
async def add_to_cart(cart: Cart = Body(...)):
    cart = jsonable_encoder(cart)
    data = await update_or_add_cart(cart)
    if data:
        return ResponseModel(data, 201, "Item added in cart Successfully")
    return ErrorResponseModel(data, 400, "Could not insert items to cart")


@router.get("", response_description="display all the cart items from database")
async def get_cart():
    data = await get_all_cart_items()
    if data:
        return ResponseModel(data, 200, "Items displayed Successfully")
    return ErrorResponseModel(data, 404, "No items in cart")


@router.get("/{user_name}", response_description="get all cart items of a user from database")
async def get_cart(user_name):
    data = await get_cart_item_by_name(user_name)
    if data:
        return ResponseModel(data, 200, "Items displayed Successfully")
    return ErrorResponseModel(data, 404, "No Items found in the cart ")


@router.delete("/{user_name}/{item_name}", response_description="deleting an item from database")
async def delete_items_in_cart(user_name, item_name):
    data = await delete_item_in_cart(user_name, item_name)
    if data != None:
        return ResponseModel(data, 201, "Items deleted Successfully")
    return ErrorResponseModel("Not found", 404, "User/Item not found in database")
