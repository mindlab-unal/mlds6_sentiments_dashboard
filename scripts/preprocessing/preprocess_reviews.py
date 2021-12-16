from mlds6sentiment.environment.base import get_mongo_credentials, get_data_paths
from mlds6sentiment.database.clients import make_mongo_client
from mlds6sentiment.database.fetch import fetch_from_mongo
from mlds6sentiment.database.transform import collection_to_dataframe
from mlds6sentiment.preprocessing.reviews import preprocess_pipe
from mlds6sentiment.database.io import export_table

def main():
    data_paths = get_data_paths()
    mongo_credentials = get_mongo_credentials()
    mongo_client = make_mongo_client(mongo_credentials)
    
    # Extract reviews collection from MongoDB.
    reviews_collection = fetch_from_mongo(
        mongo_client, mongo_credentials.mongo_database,
        "PapersReview",
        {}
    )
    # Transform into pandas dataframe.
    reviews_df = collection_to_dataframe(reviews_collection)

    # Preprocess data
    preprocess_df = preprocess_pipe(reviews_df)

    # Save the data
    export_table(
            base_path=data_paths.preprocessed_data,
            file_name="reviews",
            file_type="parquet",
            data=preprocess_df
            )

if __name__ == "__main__":
    main()
