from pymongo import MongoClient
from typing import List, Dict

def fetch_from_mongo(
        mongo_client: MongoClient,
        mongo_database: str,
        mongo_collection: str,
        query: Dict
        ) -> List[Dict]:
    """
    Function to retrieve a query from MongoDB.

    Parameters
    ----------
    mongo_client : MongoClient
    mongo_database : str
    mongo_collection : str
    query : Dict
        MongoDB query.
    """
    database = mongo_client[mongo_database]
    collection = database[mongo_collection]
    result = list(collection.find(query))
    return result

