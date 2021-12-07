from typing import Dict, List
from pandas import DataFrame

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

def collection_to_dataframe(collection: List[Dict]) -> DataFrame:
    """
    Transforms the reviews mongo collection into a pandas dataframe.

    Parameters
    ----------
    collection : List[Dict]
        Collection extracted from MongoDB.

    Returns
    -------
    reviews_df : DataFrame
        Denormalized version of the dataset.
    """
    reviews = []
    for paper in collection:
        paper_dn = paper["review"]
        for review in paper_dn:
            review["paper_id"] = paper["id"]
            review["preliminary_decision"] = paper["preliminary_decision"]
            reviews.append(review)
    reviews_df = DataFrame(reviews)
    return reviews_df
