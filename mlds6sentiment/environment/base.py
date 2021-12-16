import os, json
from mlds6sentiment.datamodels.environment import DataLakePaths
from mlds6sentiment.datamodels.database import MongoCredentials
from mlds6sentiment.datamodels.experiment import RandomKFoldExp, Hyperparameters

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
            results = os.environ["RESULTS_PATH"]
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

def get_kfold_params() -> RandomKFoldExp:
    """
    Function to collect the experimental setup.

    Parameters
    ----------
    type : str
        Type of hyperparameter to load.

    Returns
    -------
    experiment : RandomKFoldExp
        Object with the experimental setup.
    """
    path = os.path.join(
            os.environ["EXPERIMENTS_PATH"],
            "random_kfold.json"
            )
    with open(path) as f:
        random_kfold = json.load(f)
    experiment = RandomKFoldExp(
            **random_kfold
            )
    return experiment

def get_hyperparameters() -> Hyperparameters:
    path = os.path.join(
            os.environ["EXPERIMENTS_PATH"],
            "hyperparameters.json"
            )
    """
    Function to collect the hyperparameters.

    Returns
    -------
    hyperparameters : Hyperparameters
        Object with the hyperparameters.
    """
    with open(path) as f:
        hyperparameters = json.load(f)
    hyperparameters = Hyperparameters(
            **hyperparameters
            )
    return hyperparameters
