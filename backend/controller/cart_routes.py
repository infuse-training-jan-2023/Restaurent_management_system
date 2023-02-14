import sys
sys.path.append("../")

from fastapi import FastAPI, HTTPException , Response
from fastapi.middleware.cors import CORSMiddleware
import json

from models.cart import *
from models.table import *
from models.item import *
from actions.table_actions import *
from repository.cart_repo import *
from repository.item_repo import *
from repository.table_repo import *

@app.post("/cart", response_model=dict)
async def add_to_cart(cart: Cart):
    data = await updatecart(cart.dict())
    if data:
        return data
    raise HTTPException(400, "Could not insert items to cart")

@app.get("/cart")
async def get_cart():
    data = await get_all_cart_items()
    if data:
        return data
    raise HTTPException(400, "Could not get items in cart")

@app.get("/cart/{user_name}", response_model=Cart)
async def get_cart(user_name):
    data = await get_a_cart_item(user_name)
    if data:
        return data
    raise HTTPException(404, "Could not find username")
