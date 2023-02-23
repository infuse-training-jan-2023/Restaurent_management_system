from models.response_model import ResponseModel
from models.error_model import ErrorResponseModel
from repository.order_repository import *
from fastapi.encoders import jsonable_encoder
from fastapi import Body, APIRouter

router = APIRouter()

@router.get("/{user_name}", response_description="get all orders of a user from database")
async def get_orders(user_name):
    data = await get_orders_by_name(user_name)
    if data:
        return ResponseModel(data, 200, "Items displayed Successfully")
    return ErrorResponseModel(data, 404, "No orders Found")
