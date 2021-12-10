from sklearn.base import TransformerMixin, ClassifierMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

def generate_model_pipeline(
        extractor : ColumnTransformer,
        selector : TransformerMixin,
        classifier : ClassifierMixin
        ) -> Pipeline:
    """
    This function defines the model pipeline.

    Parameters
    ----------
    extractor : ColumnTransformer
        Extracts features from a dataframe.
    selector : TransformerMixin
        Selects the most important features.
    classifier : ClassifierMixin
        Classifiaction model.
    """
    pipe = Pipeline(
            [
                ("extractor", extractor),
                ("selector", selector),
                ("classifier", classifier)
                ]
            )
    return pipe
