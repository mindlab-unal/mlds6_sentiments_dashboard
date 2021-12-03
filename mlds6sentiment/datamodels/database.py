from pydantic import BaseModel

class MongoCredentials(BaseModel):
    """
    Class for MongoDB connection and access.

    Attributes
    ----------
    mongo_url : str
        Host name for MongoDB database.
    mongo_user : str
        User name for MongoDB database.
    mongo_password : str
        Password for MongoDB database.
    mongo_database : str
        Database to use in MongoDB.
    """
    mongo_url : str
    mongo_user : str
    mongo_password : str
    mongo_database : str
