import pytest
import asyncio
from repository.cart_repository import *


@pytest.mark.asyncio
async def test_delete_item(mocker):
    username = "Jane Doe"
    item_to_delete = "samosa"
    result = await delete_item_in_cart(username, item_to_delete)
    assert result == {"msg": "Item deleted successfully"}


@pytest.mark.asyncio
async def test_delete_item(mocker):
    username = "user3"
    item_to_delete = "item3"
    result = await delete_item_in_cart(username, item_to_delete)
    assert result == {"msg": "Cart deleted as it was empty"}


@pytest.mark.asyncio
async def test_delete_item(mocker):
    username = "Jane Doe"
    item_to_delete = "voda"
    result = await delete_item_in_cart(username, item_to_delete)
    assert result == None


@pytest.mark.asyncio
async def test_delete_item(mocker):
    username = "user4"
    item_to_delete = "voda"
    result = await delete_item_in_cart(username, item_to_delete)
    assert result == None
