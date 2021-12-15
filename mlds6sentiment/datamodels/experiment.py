from pydantic import BaseModel
from typing import List

class RandomKFoldExp(BaseModel):
    """
    Class to describe for a single experiment.

    Arguments
    ---------
    k : int
        Number of partitions for K-Fold.
    n_combinations : int
        Number of hyperparemeter combinations to consider.
    metric : str
        Metric to evaluate.
    stratify : bool
        Specifies if the training must be stritified.
    """
    cv : int
    n_iter : int
    scoring : str

class Hyperparameters(BaseModel):
    """
    Class to store information of the model pipeline hyperparemeters.

    Arguments
    ---------
    extractor : str
        Path for the extractor hyperparemeters.
    selector : str
        Path for the selector hyperparemeters.
    model : str
        Path for the model hyperparemeters.
    """
    extractor__text__use_idf: List[bool]
    extractor__text__sublinear_tf: List[bool]
    selector__k: List[int]
    classifier__penalty: List[str]
    classifier__C: List[float]
