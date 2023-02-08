from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Orders
#app object
app = FastAPI()

from database import orders_data

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

@app.post("/api/orders", response_model=Orders)
async def order_details(orders:Orders):
    response = await orders_data(orders.dict())
    if  response:
        return response
    raise HTTPException(400, "Something went wrong")
