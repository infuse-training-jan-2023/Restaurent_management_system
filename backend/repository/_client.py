import motor.motor_asyncio

def _get_client():
    mongo_local_url = "mongodb://localhost:27017"
    mongo_cluster_url = 'mongodb+srv://dinesh_gawas:mongo123@restaurant.xw2cat1.mongodb.net/'
    client = motor.motor_asyncio.AsyncIOMotorClient(mongo_cluster_url)
    return client.Restaurant

def get_collection(collection: str):
    client = _get_client()
    return client.get_collection(collection)


