# from repository.database import TableRepo

# class TableActions:
#     def __init__(self) -> None:
#         self.repo = TableRepo

#     def get_tables(self):
        
#         cursor = TableRepo.get_tables()
#         tables = []
#         for table in cursor:
#             tables.append({
#                 'capicity': table['capicity'],
#                 'columns': table['columns'],
#             })
#         # cursor = TableRepo.tables_data.find({})
#         async for document in cursor:
#             tables.append(Tables(**document))
#         return tables