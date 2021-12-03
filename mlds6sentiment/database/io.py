import json, os
from typing import Dict

def load_json_file(lake_path: str, file_name: str) -> Dict:
    """
    This function loads a json dataset as a Dict.

    Parameters
    ----------
    lake_path : str
        Path to the data lake.
    file_name : str
        Name of the file to upload.

    Returns
    -------
    data : Dict
        Loaded dataset.
    """
    file_path = os.path.join(lake_path, file_name)
    with open(file_path) as f:
        data = json.load(f)
    return data
