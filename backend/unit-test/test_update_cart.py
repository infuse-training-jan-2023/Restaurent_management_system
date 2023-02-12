import pytest, asyncio
from repository.database import *

@pytest.mark.asyncio
async def test_updatecart():
    # Test case 1: Item already exists in cart, update quantity and total
    data = {
        "user_name": "Jane Doe",
        "items": [
            {
                "item_name": "samosa",
                "quantity": 2,
                "price": 10
            }
        ]
    }
    result = await update_cart(data)
    assert result == {"msg": "Item Updated successfully"}, f'Expected {result} to equal {{"msg": "Item Updated successfully"}}'

    # Test case 2: Item does not exist in cart, add it
    data = {
        "user_name": "user2",
        "items": [
            {
                "item_name": "item2",
                "quantity": 2,
                "price": 15
            }
        ]
    }
    result = await update_cart(data)
    assert result == {"msg": "Item added successfully"}, f'Expected {result} to equal {{"msg": "Item added successfully"}}'

    # Test case 3: Cart does not exist for user, create cart and add item
    data = {
        "user_name": "user3",
        "items": [
            {
                "item_name": "item3",
                "quantity": 3,
                "price": 20
            }
        ]
    }
    result = await update_cart(data)
    assert result == {"message": "Cart created and item added successfully"}, f'Expected {result} to equal {{"message": "Cart created and item added successfully"}}'

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
        await update_cart(data)
    assert str(e.value) == "Error: Item Update failed", f"Expected {str(e.value)} to equal Error: Item Update failed"
