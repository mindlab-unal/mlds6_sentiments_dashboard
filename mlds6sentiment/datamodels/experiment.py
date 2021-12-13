from pydantic import BaseModel

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
    k : int
    n_combinations : int
    metric : str
    stratify : bool

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
    extractor: str
    selector: str
    model: str
