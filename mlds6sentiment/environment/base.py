import os
from mlds6sentiment.datamodels.environment import DataLakePaths
from mlds6sentiment.datamodels.database import MongoCredentials

def get_data_paths() -> DataLakePaths:
    """
    Function to collect path environment variables.

    Returns
    -------
    paths : DataLakePaths
        Object with the required data paths.
    """
    paths = DataLakePaths(
            raw_data = os.environ["RAW_DATA_PATH"],
            preprocessed_data = os.environ["PREPROCESSED_DATA_PATH"],
            models = os.environ["MODELS_PATH"],
            features = os.environ["FEATURES_PATH"]
            )
    return paths

def get_mongo_credentials() -> MongoCredentials:
    """
    Function to collect environment variables for Mongo access.

    Returns
    -------
    creds : MongoCredentials
        Object with the MongoDB credentials.
    """
    creds = MongoCredentials(
            mongo_url=os.environ["MONGO_URL"],
            mongo_user=os.environ["MONGO_USER"],
            mongo_password=os.environ["MONGO_PASSWORD"],
            mongo_database=os.environ["MONGO_DATABASE"]
            )
    return creds
