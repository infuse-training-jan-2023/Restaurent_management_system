# import sys
# sys.path.append("../../")

# import pytest, asyncio
# from repository.database import create_table

# table_data = {
#     "table_no":2,
#     "capicity":4,
#     "date":"09-02-2023",
#     "from_time":"12:00 am",
#     "to_time":"05:00 pm",
#     "price":5000
# }

# @pytest.mark.asyncio
# async def test_insert_table(mocker):
#     mock = mocker.patch('repository.database.create_table', return_value = table_data)
#     table_returned = await create_table({"table_no": 2, "capicity":4,"date":"09-02-2023","from_time":"12:00 am","to_time":"05:00 pm","price": 5000})
#     assert table_returned["price"] == table_data["price"]

# @pytest.mark.asyncio
# async def test_invalid_insert_table(mocker):
#     mock = mocker.patch('repository.database.create_table', return_value = table_data)
#     with pytest.raises(Exception) as e:
#       await create_table({"table_no": 2, "capicity":4,"date":"09-02-2023"})


# @pytest.mark.asyncio
# async def test_invalid_datatype_insert_table(mocker):
#     mock = mocker.patch('repository.database.create_table', return_value = table_data)
#     with pytest.raises(Exception) as e:
#       await create_table({"table_no": 2, "capicity":4,"date":"09-02-2023","from_time":"12:00 am","to_time":"05:00 pm","price": "5000"}) # price sent as string

# if __name__ == "__main__":
#     asyncio.run(pytest.main())
