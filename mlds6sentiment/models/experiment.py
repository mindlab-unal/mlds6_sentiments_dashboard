from sklearn.pipeline import Pipeline
from sklearn.model_selection import RandomizedSearchCV
from mlds6sentiment.datamodels.experiment import Hyperparameters, RandomKFoldExp

def generate_random_search(
        pipe: Pipeline,
        hyperparameters: Hyperparameters,
        random_kfold_experiment: RandomKFoldExp
        ) -> RandomizedSearchCV:
    """
    Generates a randomized search object.

    Parameters
    ----------
    pipe : Pipeline
        The pipeline to use.
    hyperparameters : Hyperparameters
        The hyperparameters to use.
    random_kfold_experiment : RandomKFoldExp
        The random kfold experiment to use.

    Returns
    -------
    random_search : RandomizedSearchCV
        The randomized search object.
    """
    random_search = RandomizedSearchCV(
        estimator=pipe,
        param_distributions=hyperparameters.dict(),
        **random_kfold_experiment.dict()
    )
    return random_search
