import pytest, asyncio
from unittest.mock import MagicMock
from repository.database import *

cart_data = {

  "user_name": "Jane Doe",
  "items": [
    {
      "item_name": "samosa",
      "quantity": 1,
      "price": 10,
      "total": 10
    },
    {
      "item_name": "voda",
      "quantity": 2,
      "price": 20,
      "total": 40
    }
  ],
  "grand_total": 50
}

@pytest.mark.asyncio
async def test_get_a_cart_item(mocker):
  order_db = mocker.patch('repository.database.get_a_cart_item', return_value=cart_data)
  result = await get_a_cart_item("Jane Doe")
  assert result["user_name"] == cart_data["user_name"]


@pytest.mark.asyncio
async def test_get_a_cart_item_failure(mocker):
    order_db.find = MagicMock(side_effect=Exception("Simulated database connection failure"))
    with pytest.raises(Exception) as exc_info:
      await get_a_cart_item("Jane Doe")
    assert str(exc_info.value) == "Error occured: database connection failure"




