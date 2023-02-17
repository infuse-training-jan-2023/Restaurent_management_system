import pytest
import asyncio
from repository.cart_repository import *

data = {
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
}


@pytest.mark.asyncio
async def test_cart_item_by_name(mocker):
    mocker.patch(
        'repository.cart_repository.get_cart_item_by_name', return_value=data)
    username = "user3"
    result = await get_cart_item_by_name(username)
    assert len(result) == len(data)
    assert result["username"] == data["username"]


@pytest.mark.asyncio
async def test_invalid_cart_item_by_name(mocker):
    mocker.patch(
        'repository.cart_repository.get_cart_item_by_name', return_value=data)
    username = "test"
    with pytest.raises(Exception) as e:
        await get_cart_item_by_name(username)
