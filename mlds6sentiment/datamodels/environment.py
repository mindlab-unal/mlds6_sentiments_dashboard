from pydantic import BaseModel

class DataLakePaths(BaseModel):
    """
    Class for data lake paths.

    Attributes
    ----------
    raw_data : str
        Folder to store raw datasets.
    preprocessed_data : str
        Folder to store preprocessed data.
    models : str
        Folder to save the models.
    features : str
        Folder to save the extracted features.
    """
    raw_data : str
    preprocessed_data : str
    models : str
    features : str
    results : str
