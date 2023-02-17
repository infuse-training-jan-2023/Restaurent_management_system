import pytest
import asyncio
from unittest.mock import MagicMock
from repository.table_repository import *

table_data = [
    {
        "id": "63eb3c70d88df88be82e7be4",
        "user_name": "Anis",
        "table_no": 1,
        "capacity": 2,
        "price": 2000,
        "date": "14-02-2023",
        "slot": "Evening"
    }
]


async def mock_fetch_all_tables(mocker):
    cursor = mocker.MagicMock()
    cursor.__aiter__.return_value = iter(table_data)
    mocker.patch('repository.table_repository.fetch_all_tables',
                 return_value=cursor)


@pytest.mark.asyncio
async def test_fetch_all_tables(mocker):
    await mock_fetch_all_tables(mocker)
    tables = await fetch_all_tables()
    assert len(tables) == len(table_data)
    assert tables[0]["price"] == table_data[0]["price"]


@pytest.mark.asyncio
async def test_invalid_update_table(mocker):
    mock = mocker.patch(
        'repository.table_repository.fetch_all_tables', return_value=table_data)
    with pytest.raises(Exception) as e:
        await fetch_all_tables({"table_no": 3, "capicity": 4, "date": "09-02-2023"})


@pytest.mark.asyncio
async def test_invalid_datatype_update_table(mocker):
    mock = mocker.patch(
        'repository.table_repository.fetch_all_tables', return_value=table_data)
    with pytest.raises(Exception) as e:
        # price sent as string
        await fetch_all_tables({"table_no": 3, "capicity": 4, "date": "09-02-2023", "from_time": "12:00 am", "to_time": "05:00 pm", "price": "5000"})

table_data = {

    "id": "63eb3c70d88df88be82e7be4",
    "user_name": "Vibhav",
    "table_no": 2,
    "capacity": 4,
    "price": 8000,
    "date": "15-02-2023",
    "slot": "Afternoon"
}


async def mock_create_table(mocker):
    cursor = mocker.MagicMock()
    cursor.__aiter__.return_value = iter(table_data)
    mocker.patch('repository.table_repository.create_table',
                 return_value=cursor)


@pytest.mark.asyncio
async def test_create_table(mocker):
    await mock_create_table(mocker)
    tables = await create_table(table_data)
    assert tables["price"] == table_data["price"]

table_data = {

    "id": "63eb3c70d88df88be82e7be4",
    "user_name": "Vibhav",
    "table_no": 2,
    "capacity": 4,
    "price": 8000
}


@pytest.mark.asyncio
async def test_invalid_create_table(mocker):
    await mock_create_table(mocker)
    with pytest.raises(Exception) as e:
        tables = await create_table(table_data)
