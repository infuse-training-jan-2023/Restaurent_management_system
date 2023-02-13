import pytest, asyncio
from repository.database import insert_order

order_data = {
  "items": [
    "string"
  ],
  "price": 0,
  "status": "prep",
  "date": "2023-02-09 11:36:10.260068"
}

@pytest.mark.asyncio
async def test_insert_order(mocker):
    mock = mocker.patch('repository.database.insert_order', return_value = order_data)
    order_returned = await insert_order({"items": ["string"], "price": 0, "status": "prep", "date": "2023-02-09 11:36:10.260068"})
    assert order_returned["price"] == order_data["price"]

@pytest.mark.asyncio
async def test_invalid_insert_order(mocker):
    mock = mocker.patch('repository.database.insert_order', return_value = order_data)
    with pytest.raises(Exception) as e:
      await insert_order({"items": ["string"], "price": 0, "status": "prep"})

@pytest.mark.asyncio
async def test_invalid_data_insert_order(mocker):
    mock = mocker.patch('repository.database.insert_order', return_value = order_data)
    with pytest.raises(Exception) as e:
      order_returned= await insert_order({"items": ["string"], "price": "0", "status": "prep", "date": "2023-02-09 11:36:10.260068"})
