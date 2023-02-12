
from repository.database import insert_order
import pytest
import asyncio

order_data = {
  "items": [{"item_id": 1, "quantity": 2}],
  "price": 10
}

@pytest.mark.asyncio
async def test_insert_order(mocker):
    mock = mocker.patch('repository.database.insert_order', return_value = order_data)
    order_returned = await insert_order(order_data)
    assert order_returned["price"] == order_data["price"]
    assert order_returned["date"] == order_data["date"]

@pytest.mark.asyncio
async def test_invalid_insert_order(mocker):
    mock = mocker.patch('repository.database.insert_order', return_value = order_data)
    with pytest.raises(Exception) as e:
      await insert_order({"items": {"string"}, "price": 0, "status": "prep"})

@pytest.mark.asyncio
async def test_invalid_data_insert_order(mocker):
    mock = mocker.patch('repository.database.insert_order', return_value = order_data)
    with pytest.raises(Exception) as e:
      order_returned= await insert_order({"items": ["string"], "price": "0", "status": "delivered", "date": '{2023-02-09 11:36:10.260068}'})

