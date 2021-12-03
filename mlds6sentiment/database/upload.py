from typing import List, Dict
from pymongo import MongoClient

def upload_mongo_collection(
        dataset: List[Dict],
        mongo_client: MongoClient,
        mongo_database: str,
        mongo_collection: str
        ):
    """
    This function uploads a collection into MongoDB

    Parameters
    ----------
    dataset : List[Dict]
        Dataset to upload.
    mongo_client : MongoClient
        Client to MongoDB.
    mongo_database : str
        Database in MongoDb
    mongo_collection : str
        Collection name.
    """
    database = mongo_client[mongo_database]
    # delete collection if exists
    collection = database[mongo_collection]
    collection.drop()

    # create collection
    collection = database[mongo_collection]
    collection.insert_many(dataset)
