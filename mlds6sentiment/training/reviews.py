from mlds6sentiment.datamodels.experiment import RandomKFoldExp 
from pandas import DataFrame
from sklearn.pipeline import Pipeline

def train(
        reviews_df: DataFrame, label: str,
        model_pipeline: Pipeline, experiment: RandomKFoldExp
        ) -> Pipeline:
    return model_pipeline
