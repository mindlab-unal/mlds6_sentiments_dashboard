from mlds6sentiment.database.clients import make_mongo_client
from mlds6sentiment.environment.base import get_mongo_credentials, get_data_paths
from mlds6sentiment.database.io import load_json_file
from mlds6sentiment.database.transform import transform_reviews
from mlds6sentiment.database.upload import upload_mongo_collection

def main():
    mongo_credentials = get_mongo_credentials()
    data_paths = get_data_paths()
    mongo_client = make_mongo_client(mongo_credentials)
    dataset = load_json_file(
            lake_path=data_paths.raw_data,
            file_name="reviews.json"
            )
    dataset_tr = transform_reviews(dataset)
    upload_mongo_collection(
            dataset=dataset_tr,
            mongo_client=mongo_client,
            mongo_database=mongo_credentials.mongo_database,
            mongo_collection="PapersReview"
            )

if __name__ == "__main__":
    main()
