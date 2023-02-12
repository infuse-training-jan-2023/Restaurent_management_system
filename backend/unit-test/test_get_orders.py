import pytest, asyncio
from repository.database import *
from unittest.mock import MagicMock
order_data = [
  {
    "items": ["string"],
    "price": 10,
    "status": "prep",
    "date": "2023-02-12T07:08:11.568+00:00"
  },
  {
    "items": ["string"],
    "price": 10,
    "status": "prep",
    "date": "2023-02-12T07:08:11.568+00:00"
  }
]

@pytest.mark.asyncio
async def test_get_orders(mocker):
  order_db = mocker.patch('repository.database.get_orders', return_value=order_data)
  result = await get_orders()
  assert len(result) == len(order_data)
  assert result[0].price == order_data[0]["price"]
  assert result[1].items == order_data[1]["items"]


@pytest.mark.asyncio
async def test_get_orders_failure(mocker):
    order_db = mocker.patch('repository.database.get_orders', return_value=order_data)
    order_db.find = MagicMock(side_effect=Exception("Simulated database connection failure"))
    with pytest.raises(Exception) as exc_info:
      await get_orders()
    assert str(exc_info.value) == "Error: database connection failure"
