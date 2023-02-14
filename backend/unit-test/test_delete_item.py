import pytest, asyncio
from repository.database import *

@pytest.mark.asyncio
async def test_delete_item(mocker):
    username = "Jane Doe"
    item_to_delete = "samosa"
    result = await delete_item_in_cart(username, item_to_delete)
    assert result == {"msg": "Item deleted successfully"}

    username = "test"
    item_to_delete = "voda"
    result = await delete_item_in_cart(username, item_to_delete)
    assert result == {"msg": "Cart deleted as it was empty"}

    username = "user1"
    item_to_delete = "voda"
    result = await delete_item_in_cart(username, item_to_delete)
    assert result == {"msg": "Item not found in the cart"}

    username = "user4"
    item_to_delete = "voda"
    result = await delete_item_in_cart(username, item_to_delete)
    assert result == {"Error": "User not found"}

    with pytest.raises(Exception) as e:
        username = "test1"
        item_to_delete = "voda"
        await delete_item_in_cart(username, item_to_delete)
    assert str(e.value) == 'Error occured: database connection failure', f"Expected {str(e.value)} to equal Error: Item Update failed"
