from typing import Dict, List

def transform_reviews(data: Dict) -> List[Dict]:
    """
    Transforms the data into a MongoDB collection.

    Parameters
    ----------
    data : Dict
        Papers reviews dataset.

    Returns
    -------
    data_collection : List[Dict]
        Dataset in MongoDB collection format.
    """
    data_collection = data["paper"]
    return data_collection
