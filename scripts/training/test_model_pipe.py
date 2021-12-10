from mlds6sentiment.environment.base import get_data_paths
from mlds6sentiment.database.io import load_table
from mlds6sentiment.models.feature_extraction import generate_feature_extractor, generate_feature_selector
from mlds6sentiment.models.model import generate_model_pipeline
from sklearn.linear_model import LogisticRegression
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("--label", type=str)
    args = parser.parse_args()

    data_paths = get_data_paths()
    # 1. carga datos
    reviews_df = load_table(data_paths.preprocessed_data, "reviews", "parquet")

    extractor = generate_feature_extractor()
    selector = generate_feature_selector()
    classifier = LogisticRegression()

    # 2. definicion del modelo
    pipe = generate_model_pipeline(extractor, selector, classifier)

    # 3. Entrenamiento
    pipe.fit(reviews_df, reviews_df[args.label])
    print(pipe.score(reviews_df, reviews_df[args.label]))

if __name__ == "__main__":
    main()
