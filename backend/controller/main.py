import sys
sys.path.append("../")
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.model import Orders

#app object
app = FastAPI()

from repository.database import *


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
def read_root():
    return "hey"

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
