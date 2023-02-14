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