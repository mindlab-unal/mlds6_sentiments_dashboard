from mlds6sentiment.environment.base import get_data_paths
from mlds6sentiment.database.io import load_table, export_model, export_cv_results
from mlds6sentiment.models.feature_extraction import generate_feature_extractor, generate_feature_selector
from mlds6sentiment.models.model import generate_model_pipeline
from mlds6sentiment.models.experiment import generate_random_search
from mlds6sentiment.environment.base import get_kfold_params, get_hyperparameters
from sklearn.linear_model import LogisticRegression
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("--label", type=str)
    args = parser.parse_args()

    data_paths = get_data_paths()
    random_kfold_experiment = get_kfold_params()
    hyperparameters = get_hyperparameters()

    # 1. carga datos
    reviews_df = load_table(data_paths.preprocessed_data, "reviews", "parquet")

    extractor = generate_feature_extractor()
    selector = generate_feature_selector()
    classifier = LogisticRegression()

    # 2. definicion del modelo
    pipe = generate_model_pipeline(extractor, selector, classifier)

    # 3. generacion del experimento
    random_search = generate_random_search(pipe, hyperparameters, random_kfold_experiment)

    # 4. entrenamiento
    random_search.fit(reviews_df, reviews_df[args.label])

    # 5. guardar mejor modelo
    export_model(random_search.best_estimator_, data_paths.models, f"{args.label}.joblib")

    # 6. guardamos resultados
    export_cv_results(random_search, data_paths.results, f"{args.label}.csv")

if __name__ == "__main__":
    main()
