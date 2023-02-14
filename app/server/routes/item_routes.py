from fastapi import APIRouter
from server.models.response_model import ResponseModel
from server.models.error_model import ErrorResponseModel
from server.repository.item_repository import *

router = APIRouter()

@router.post("", response_description="Insert items to the database")
async def insert():
    data = await insert_items()
    return ResponseModel(data, 201, "Items inserted Successfully")

@router.get("")
async def display_items():
    try:
        response = await fetch_all_items()
        if response != None:
            return ResponseModel(response, 200, "Items displayed Successfully")
        return ErrorResponseModel(response, 400, "No items in the database")
    except Exception as e:
        raise Exception('Error occured: ',e)
