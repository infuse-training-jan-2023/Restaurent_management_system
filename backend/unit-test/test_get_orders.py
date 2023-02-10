import pytest, asyncio
from repository.database import get_orders

order_data = [{
    "items": [
      "string"
    ],
    "price": 0,
    "status": "prep",
    "date": "2023-02-09 15:58:54.754442"
  },
  {
    "items": [
      "string"
    ],
    "price": 0,
    "status": "prep",
    "date": "2023-02-09 15:59:48.240620"
  }]

# @pytest.mark.asyncio
# async def test_get_orders(mocker):
#     mock = mocker.patch('repository.database.get_orders', return_value = order_data)
#     order_returned = await get_orders()
#     for i, order in order_returned:
#         assert order_data == order_returned
