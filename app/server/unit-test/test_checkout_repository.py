import pytest, asyncio
from repository.checkout_repository import *

data = {
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

@pytest.mark.asyncio
async def test_insert_order_history(mocker):
    mocker.patch('repository.checkout_repository.insert_order_history', return_value = data)
    result = await insert_order_history(data)
    assert result == {"Success": "Order history inserted successfully"}


@pytest.mark.asyncio
async def test_invalid_insert_order_history(mocker):
    mocker.patch('repository.checkout_repository.insert_order_history', return_value = data)
    with pytest.raises(Exception) as e:
        await insert_order_history()

@pytest.mark.asyncio
async def test_delete_cart(mocker):
    mocker.patch('repository.checkout_repository.delete_cart', return_value = {"msg": "user deleted successfully"})
    username = "user2"
    result = await delete_cart(username)
    assert result == {"msg": "user deleted successfully"}

@pytest.mark.asyncio
async def test_invalid_username_delete_cart(mocker):
    mocker.patch('repository.checkout_repository.delete_cart', return_value = None)
    result = await delete_cart("test")
    assert result == None

