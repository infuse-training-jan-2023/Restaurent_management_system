import pytest, asyncio
from unittest.mock import MagicMock
from repository.database import *

cart_data =[
    {
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
    },
    {
        "user_name": "user1",
        "items": [
        {
            "item_name": "item2",
            "quantity": 2,
            "price": 15,
            "total": 30
        },
        {
            "item_name": "item1",
            "quantity": 2,
            "price": 15,
            "total": 30
        },
        {
            "item_name": "item3",
            "quantity": 2,
            "price": 15,
            "total": 30
        }
        ],
        "grand_total": 90
    },
    {
        "user_name": "user2",
        "items": [
        {
            "item_name": "item3",
            "quantity": 2,
            "price": 20,
            "total": 30
        },
        {
            "item_name": "item2",
            "quantity": 2,
            "price": 15,
            "total": 30
        }
        ],
        "grand_total": 60
    },
    {
        "user_name": "user3",
        "items": [
        {
            "item_name": "item3",
            "quantity": 3,
            "price": 20,
            "total": 60
        }
        ],
        "grand_total": 60
    },
    {
        "user_name": "test",
        "items": [
        {
            "item_name": "voda",
            "quantity": 2,
            "price": 20,
            "total": 40
        }
        ],
        "grand_total": 40
    }
]

@pytest.mark.asyncio
async def test_get_all_cart_items(mocker):
  order_db = mocker.patch('repository.database.get_all_cart_items', return_value=cart_data)
  result = await get_all_cart_items()
  assert len(result) == len(cart_data)
  assert result[0].items == cart_data[0]["items"]
  assert result[4].grand_total == cart_data[4]["grand_total"]


@pytest.mark.asyncio
async def test_get_all_cart_items_failure(mocker):
    order_db.find = MagicMock(side_effect=Exception("Simulated database connection failure"))
    with pytest.raises(Exception) as exc_info:
      await get_all_cart_items()
    assert str(exc_info.value) == "Error occured: database connection failure"
