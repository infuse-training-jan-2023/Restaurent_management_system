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

origins = ['http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
       return  response
    raise HTTPException(400, "Something went wrong")

@app.get("/orders")
async def get_order_details():
    response = await get_orders()
    if  response:
        return  response
    raise HTTPException(400, "Something went wrong")

@app.post("/item")
async def insert():
    await insert_items()

@app.get("/items")
async def display_items():
    try:
        response = await fetch_all_items()
        return response
    except Exception as e:
        raise Exception('Error occured: ',e)

@app.post("/cart", response_model=dict)
async def add_to_cart(cart: AddToCart):
    data = await updatecart(cart.dict())
    if data:
        return data
    raise HTTPException(400, "Could not insert items to cart")

@app.get("/cart/{user_name}", response_model=AddToCart)
async def get_cart(user_name):
    data = await get_a_cart_item(user_name)
    if data:
        return data
    raise HTTPException(404, "Could not find username")

@app.delete("/cart/{user_name}/{item_name}")
async def delete_items_in_cart(user_name,item_name):
    data = await delete_item_in_cart(user_name, item_name)
    if data:
        return data
    raise HTTPException(404, detail=f"Could not find username {user_name}/item in the cart")

@app.delete("/checkout/{user_name}")
async def delete_all_items_in_cart(user_name):
    data = await delete_cart(user_name)
    if data:
        return data
    raise HTTPException(400, "No Items in the Cart to be deleted")