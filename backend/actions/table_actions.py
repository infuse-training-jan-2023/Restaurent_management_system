from repository.database import *


def get_tables():
    cursor = get_tables()
    tables = []
    for table in cursor:
        tables.append({
            tables.append({
                "capicity" : table[0],
                "date" : table[1],
                "from_time" : table[2],
                "to_time" : table[3],
                "available" : table[4],
                "price" : table[5],
            })
        })
    return tables