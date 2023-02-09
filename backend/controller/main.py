from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys 
sys.path.append("../")
from repository.database import  insert_items, fetch_all_items

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
def read_root():

    return "hey"

@app.get("/item")
async def insert():
    await insert_items()


@app.get("/items")
async def display_items():
    try: 
        response = await fetch_all_items()
        return response
    except Exception as e:
        raise Exception('Error occured: ',e)
