import pytest
import asyncio
from repository.cart_repository import *


@pytest.mark.asyncio
async def test_update_cart(mocker):

    data = {
        "user_name": "Jane Doe",
        "items": [
            {
                "item_name": "samosa",
                "quantity": 1,
                "price": 10
            }
        ]
    }
    mocker.patch('repository.cart_repository.update_or_add_cart',
                 return_value=data)
    result = await update_or_add_cart(data)
    assert result["grand_total"] == 10


@pytest.mark.asyncio
async def test_add_item_into_cart(mocker):
    mocker.patch('repository.cart_repository.update_or_add_cart',
                 return_value=data)
    # Test case 2: Item does not exist in cart, add it
    data = {
        "user_name": "user2",
        "items": [
            {
                "item_name": "item3",
                "quantity": 1,
                "price": 20
            }
        ]
    }
    result = await update_or_add_cart(data)
    assert result["items"][2]["item_name"] == data["items"][0]["item_name"]


@pytest.mark.asyncio
async def test_create_cart(mocker):
    # Test case 3: Cart does not exist for user, create cart and add item
    data = {
        "user_name": "user4",
        "items": [
            {
                "item_name": "item3",
                "quantity": 3,
                "price": 20
            }
        ]
    }
    result = await update_or_add_cart(data)
    assert result["username"] == data["user_name"]


@pytest.mark.asyncio
async def test_invalid_add_item_into_cart(mocker):
    # Test case 4: Exception when updating cart
    with pytest.raises(Exception) as e:
        data = {
            "user_name": "user3",
            "items": [
                {
                    "item_name": "item4",
                    "quantity": 4
                }
            ]
        }
        await update_or_add_cart(data)
    assert str(
        e.value) == "Error: Item Update failed", f"Expected {str(e.value)} to equal Error: Item Update failed"


@pytest.mark.asyncio
async def test_invalid_update_cart(mocker):
    with pytest.raises(Exception) as e:
        data = {
            "user_name": "Jane Doe",
            "items": [
                {
                    "item_name": "samosa",
                    "quantity": 1,
                    "price": 10
                }
            ]
        }
        mocker.patch(
            'repository.cart_repository.update_or_add_cart', return_value=data)
        # Test case 4: Exception when updating cart
        await update_or_add_cart(data)
        assert str(
            e.value) == "Error: Item Update failed", f"Expected {str(e.value)} to equal Error: Item Update failed"
