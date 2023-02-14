from fastapi import APIRouter
from server.models.response_model import ResponseModel
from server.models.error_model import ErrorResponseModel
from server.repository.checkout_repository import *
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.delete("/{user_name}", response_description="delete items from cart and insert into order database")
async def delete_all_items_in_cart(user_name):
    data = await delete_cart(user_name)
    if data != None:
        return ResponseModel(data, 200, "Cart deleted Successfully")
    return ErrorResponseModel("Not found",404,"User not found in database")
