from fastapi import FastAPI, HTTPException , Response   
import json
from fastapi.middleware.cors import CORSMiddleware


import sys
sys.path.append("../")

from models.model import Tables
# from actions.table_actions import TableActions
# from repository.database import TableRepo
# table_repo = TableRepo

from repository.database import (
    create_table,
    fetch_all_tables,
    fetch_available_tables
)

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

@app.get("/avail_tables")
async def get_avail_tables():
    response = await fetch_available_tables()
    return response

@app.post("/tables",response_model=Tables)
async def post_table(table: Tables):
    response = await create_table(table.dict())
    if response:
        return response
    raise HTTPException(400, "Could not create table")
