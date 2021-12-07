import pandas as pd
from pandas import DataFrame
import re
from nltk.corpus import stopwords

def preprocess_text(document: str) -> str:
    """
    Function to clean text information, transforms to lowercase, removes special characters, strips the document, tokenizes and removes stopwords in Spanish.

    Parameters
    ----------
    document : str
        Input text.

    Returns
    -------
    cleaned_document : str
        Preprocessed text.
    """
    lower_document = document.lower()
    no_signs_document = re.sub(r"[^a-zA-Zéáíóúñ ]", "", lower_document)
    strip_document = no_signs_document.strip()
    tokens = strip_document.split()
    sws = stopwords.words("spanish") 
    white_list = ["nada", "tuvo", "tuve", "tendrá", "sentido"]
    sws = list(filter(lambda word: word not in white_list, sws))
    filtered_tokens = filter(lambda token: token not in sws, tokens)
    cleaned_document = " ".join(filtered_tokens)
    return cleaned_document

def preprocess_pipe(reviews_df: DataFrame) -> DataFrame:
    """
    Preprocess pipeline for the reviews dataset.

    Parameters
    ----------
    reviews_df : DataFrame
        Raw dataframe.

    Returns
    -------
    clean_reviews_df : DataFrame
        Preprocessed dasaset.
    """
    clean_reviews_df = (
        reviews_df
        .query("lan == 'es'")
        .drop(columns=["remarks", "orientation", "lan"])
        .fillna(0)
        .astype(
            {
                "confidence": "int", "evaluation": "int", 
                "id": "int", "paper_id": "int"
            }
        )
        .assign(
            timespan = lambda df: pd.to_datetime(df["timespan"], format="%Y-%m-%d"),
            text = lambda df: df["text"].apply(preprocess_text),
            n_words = lambda df: df["text"].apply(lambda document: len(document.split()))
        )
    )
    return clean_reviews_df
