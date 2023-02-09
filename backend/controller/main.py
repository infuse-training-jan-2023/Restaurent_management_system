import sys
sys.path.append("../")

from fastapi import FastAPI, HTTPException , Response
from fastapi.middleware.cors import CORSMiddleware
import json


from models.model import *
from actions.table_actions import *
from repository.database import *

#app object
app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

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

@app.post("/orders", response_model=Orders)
async def order_details(orders:Orders):
    response = await insert_order(orders.dict())
    if  response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.get("/orders")
async def get_order_details():
    response = await get_orders()
    if  response:
        return response
    raise HTTPException(400, "Something went wrong")

