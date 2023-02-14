import sys
sys.path.append("../../")

import pytest, asyncio
from repository.database import fetch_all_tables

table_data = [
  {
    "table_no": 1,
    "capicity": 4,
    "date": "-",
    "from_time": "-",
    "to_time": "-",
    "available": True,
    "price": 10000
  },
  {
    "table_no": 2,
    "capicity": 4,
    "date": "09-02-2023",
    "from_time": "12:00 am",
    "to_time": "05:00 pm",
    "available": True,
    "price": 5000
  },
  {
    "table_no": 3,
    "capicity": 8,
    "date": "10-02-2023",
    "from_time": "11:00 am",
    "to_time": "03:00 pm",
    "available": False,
    "price": 15000
  }
]

async def mock_fetch_all_tables(mocker):
    cursor = mocker.MagicMock()
    cursor.__aiter__.return_value = iter(table_data)
    mocker.patch('repository.database.tables_data.find', return_value=cursor)

@pytest.mark.asyncio
async def test_fetch_all_tables(mocker):
    await mock_fetch_all_tables(mocker)
    tables = await fetch_all_tables()
    assert len(tables) == len(table_data)
    assert tables[0].price == table_data[0]["price"]
    assert tables[1].price == table_data[1]["price"]


# @pytest.mark.asyncio
# async def test_invalid_update_table(mocker):
#     mock = mocker.patch('repository.database.fetch_all_tables', return_value = table_data)
#     with pytest.raises(Exception) as e:
#       await fetch_all_tables({"table_no": 3, "capicity":4,"date":"09-02-2023"})

# @pytest.mark.asyncio
# async def test_invalid_datatype_update_table(mocker):
#     mock = mocker.patch('repository.database.fetch_all_tables', return_value = table_data)
#     with pytest.raises(Exception) as e:
#       await fetch_all_tables({"table_no": 3, "capicity":4,"date":"09-02-2023","from_time":"12:00 am","to_time":"05:00 pm","price": "5000"}) # price sent as string


