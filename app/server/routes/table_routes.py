from fastapi import APIRouter, Body
from server.models.tables_model import Tables, DeleteTables
from server.models.response_model import ResponseModel
from server.models.error_model import ErrorResponseModel
from server.repository.table_repository import *
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.get("", response_description="Get all Table orders from the database")
async def get_tables():
    data = await fetch_all_tables()
    if data != None:
        return ResponseModel(data, 200, "Table Orders displayed Successfully")
    return ErrorResponseModel(data, 404, "No Orders in database")

@router.post("", response_description="Table order added into the database")
async def post_table(table: Tables = Body(...)):
    table = jsonable_encoder(table)
    data = await create_table(table)
    if data:
        return ResponseModel(data, 201, "Table added Successfully")
    return ErrorResponseModel(data, 400, "Could not create table")

@router.put("")
async def delete_table_reservation(table: DeleteTables = Body(...)):
    table = jsonable_encoder(table)
    data = await delete_table(table)
    if data:
        return ResponseModel(data, 200, "Table Deleted Successfully") 
    return ErrorResponseModel(data,404, "Could not delete the record in tables")

