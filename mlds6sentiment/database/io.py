import json, os, joblib
import pandas as pd
from typing import Dict
from pandas import DataFrame
from sklearn.pipeline import Pipeline
from sklearn.model_selection import RandomizedSearchCV

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

def load_table(
        base_path: str,
        file_name: str,
        file_type: str,
        **kwargs
        ) -> DataFrame:
    """
    This function loads any dataframe from a given format.

    Parameters
    ----------
    base_path : str
        Path of the dataset.
    file_name : str
        File name without extention.
    file_type : str
        File type to upload.

    Returns
    -------
    table : DataFrame
        Uploaded data.
    """
    file = f"{file_name}.{file_type}"
    file_path = os.path.join(base_path, file)
    load_fn = eval(f"pd.read_{file_type}")
    table = load_fn(file_path, **kwargs)
    return table

def export_table(
        base_path: str,
        file_name: str,
        file_type: str,
        data : DataFrame,
        **kwargs
        ):
    """
    This function loads any dataframe from a given format.

    Parameters
    ----------
    base_path : str
        Path of the dataset.
    file_name : str
        File name without extention.
    file_type : str
        File type to upload.

    Returns
    -------
    table : DataFrame
        Uploaded data.
    """
    file = f"{file_name}.{file_type}"
    file_path = os.path.join(base_path, file)
    load_fn = eval(f"data.to_{file_type}")
    table = load_fn(file_path, **kwargs)
    return table

def export_model(
        model: Pipeline, base_path: str, file_name: str
        ):
    """
    This function exports a model to a file.

    Parameters
    ----------
    model : Pipeline
        Model to export.
    base_path : str
        Path of the models.
    file_name : str
        File name for the model.
    """
    file_path = os.path.join(base_path, file_name)
    joblib.dump(model, file_path)

def export_cv_results(grid_search: RandomizedSearchCV, base_path: str, file_name: str):
    """
    This function exports a model to a file.

    Parameters
    ----------
    model : Pipeline
        Model to export.
    base_path : str
        Path of the models.
    file_name : str
        File name for the model.
    """
    results = pd.DataFrame(grid_search.cv_results_)
    save_path = os.path.join(base_path, file_name)
    results.to_csv(save_path)
