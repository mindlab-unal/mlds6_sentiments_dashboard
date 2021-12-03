SHELL=/bin/bash

data-acquisition:
	@echo "Collecting data."
	source env_vars.env && ./scripts/data_acquisition/download_dataset.sh

upload-data:
	@echo "Uploading data."
	source env_vars.env && python scripts/data_acquisition/upload_to_mongo.py

launch_jupyter:
	@echo "Spawining jupyter server"
	source env_vars.env && jupyter notebook
