SHELL=/bin/bash

data-pipeline: data-acquisition upload-data 

data-acquisition:
	@echo "Collecting data."
	source env_vars.env && ./scripts/data_acquisition/download_dataset.sh

upload-data:
	@echo "Uploading data."
	source env_vars.env && python scripts/data_acquisition/upload_to_mongo.py

launch_jupyter:
	@echo "Spawning jupyter server"
	source env_vars.env && jupyter notebook
