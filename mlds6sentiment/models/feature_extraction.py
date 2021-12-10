from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import chi2, SelectKBest

def generate_feature_extractor() -> ColumnTransformer:
    """
    This function generates the feature extactor object for the papers reviews dataset.

    Returns
    -------
    column_transformer : ColumnTransformer
        Sklearn object to extract features.
    """
    column_transformer = ColumnTransformer(
            [
                ("text", TfidfVectorizer(), "text"),
                ("n_words", MinMaxScaler(), ["n_words"])
                ]
            )
    return column_transformer

def generate_feature_selector() -> SelectKBest:
    """
    This function generates the feature selector object for the papers reiews dataset.

    Returns
    -------
    selector : SelectKBest
        Sklearn object to select features.
    """
    selector = SelectKBest(chi2)
    return selector
