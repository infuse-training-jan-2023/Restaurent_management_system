#MONGOBD driver
import motor.motor_asyncio

def _establish_connection():
    connection_url = 'mongodb+srv://dinesh_gawas:mongo123@restaurant.xw2cat1.mongodb.net'
    # connection_url = 'mongodb://localhost:27017/'
    client = motor.motor_asyncio.AsyncIOMotorClient(connection_url)
    return client.Restaurant

def get_collection(collection : str):
    client = _establish_connection()
    return client.get_collection(collection)
