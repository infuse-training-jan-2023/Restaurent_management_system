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
# from repository.item_repo import *
from repository.table_repo import *
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

@app.get("/")
def read_root():
    return {"Hello": "World"}


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