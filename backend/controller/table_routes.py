import sys
sys.path.append("../")

from fastapi import FastAPI, HTTPException , Response
from fastapi.middleware.cors import CORSMiddleware
import json

from models.cart import *
from models.table import *
from models.item import *
from actions.table_actions import *
from repository.database import *



@app.get("/tables")
async def get_tables():
    response = await fetch_all_tables()
    return response

@app.post("/tables",response_model=Tables)
async def post_table(table: Tables):
    response = await create_table(table.dict())
    if response:
        return response
    raise HTTPException(400, "Could not create table")

@app.put("/tables/{table_no}",response_model=Tables)
async def update_table(table_no:int,capacity:int,price:int,date:str,slot:str):
    response = await update_tables(table_no,capacity,price,date,slot)
    if response:
        return response
    raise HTTPException(404, f"no table with table no{table_no}")
