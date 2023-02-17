# MONGOBD driver
import motor.motor_asyncio


def _establish_connection():
    connection_url = 'mongodb+srv://anis:anis%40123@mydb.tpgkpds.mongodb.net/test'
    client = motor.motor_asyncio.AsyncIOMotorClient(connection_url)
    return client.Restaurant


def get_collection(collection: str):
    client = _establish_connection()
    return client.get_collection(collection)
