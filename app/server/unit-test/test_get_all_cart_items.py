import pytest
import asyncio
from unittest.mock import MagicMock
from repository.cart_repository import *

cart_data = [
    {
        "id": "63e8d45b0777795196266b5b",
        "username": "user3",
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
        "id": "63ec5beab86b3b61af693721",
        "username": "Jane Doe",
        "items": [
            {
              "item_name": "samosa",
              "quantity": 1,
              "price": 10,
              "total": 10
            }
        ],
        "grand_total": 10
    },
    {
        "id": "63ec70b1a098dbc788927ca9",
        "username": "user2",
        "items": [
            {
              "item_name": "item2",
              "quantity": 2,
              "price": 15,
              "total": 30
            },
            {
                "item_name": "item1",
                "quantity": 1,
                "price": 20,
                "total": 20
            },
            {
                "item_name": "item3",
                "quantity": 1,
                "price": 20,
                "total": 20
            }
        ],
        "grand_total": 70
    },
    {
        "id": "63ec7211c226d0a93e22db52",
        "username": "user4",
        "items": [
            {
              "item_name": "item3",
              "quantity": 3,
              "price": 20,
              "total": 60
            }
        ],
        "grand_total": 60
    }
]


@pytest.mark.asyncio
async def test_get_all_cart_items(mocker):
    order_db = mocker.patch(
        'repository.cart_repository.get_all_cart_items', return_value=cart_data)
    result = await get_all_cart_items()
    assert len(result) == len(cart_data)
    assert result[0]["items"] == cart_data[0]["items"]
    assert result[3]["grand_total"] == cart_data[3]["grand_total"]


@pytest.mark.asyncio
async def test_get_all_cart_items_failure(mocker):
    order_db = mocker.patch(
        'repository.cart_repository.get_all_cart_items', return_value=cart_data)
    order_db.find = MagicMock(side_effect=Exception(
        "Simulated database connection failure"))
    with pytest.raises(Exception) as exc_info:
        await get_all_cart_items()
    assert str(exc_info.value) == "Error occured: database connection failure"
