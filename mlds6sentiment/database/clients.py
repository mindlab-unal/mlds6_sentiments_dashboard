from pymongo import MongoClient
from mlds6sentiment.datamodels.database import MongoCredentials

def make_mongo_client(mongo_credentials: MongoCredentials) -> MongoClient:
    """
    This functon creates the client for mongodb.

    Parameters
    ----------
    mongo_credentials : MongoCredentials
        Object with the fields for mongodb authentication.

    Returns
    -------
    client : MongoClient
        Pymongo client.
    """
    client = MongoClient(
            mongo_credentials.mongo_url.format(
                mongo_credentials.mongo_user, mongo_credentials.mongo_password
                )
            ) 
    return client
