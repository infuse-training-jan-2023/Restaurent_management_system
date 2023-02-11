# import sys
# sys.path.append("../../")

# import pytest, asyncio
# from repository.database import update_tables

# table_data = {
#     "table_no":2,
#     "capicity":4,
#     "date":"09-02-2023",
#     "from_time":"12:00 am",
#     "to_time":"05:00 pm",
#     "price":5000
# }

# async def mock_update_tables(table_no, capicity, date, from_time, to_time, price):
#     return table_data

# @pytest.mark.asyncio
# async def test_update_table(mocker):
#     mocker.patch('repository.database.update_tables', mock_update_tables)
#     table_returned = await update_tables(2, 4, "09-02-2023", "12:00 am", "05:00 pm",True, 5000)
#     assert table_returned["price"] == table_data["price"]

# @pytest.mark.asyncio
# async def test_invalid_update_table(mocker):
#     mock = mocker.patch('repository.database.update_tables', return_value = table_data)
#     with pytest.raises(Exception) as e:
#       await update_tables({"table_no": 3, "capicity":4,"date":"09-02-2023"})

# @pytest.mark.asyncio
# async def test_invalid_datatype_update_table(mocker):
#     mock = mocker.patch('repository.database.update_tables', return_value = table_data)
#     with pytest.raises(Exception) as e:
#       await update_tables({"table_no": 3, "capicity":4,"date":"09-02-2023","from_time":"12:00 am","to_time":"05:00 pm","price": "5000"}) # price sent as string


