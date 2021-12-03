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
        Folders to save the models.
    """
    raw_data : str
    preprocessed_data : str
    models : str
