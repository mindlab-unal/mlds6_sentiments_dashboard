SHELL=/bin/bash

pipeline: data-acquisition upload-data preprocess train

data-acquisition:
	@echo "Collecting data."
	source env_vars.env &&\
		./scripts/data_acquisition/download_dataset.sh

upload-data:
	@echo "Uploading data."
	source env_vars.env &&\
		python scripts/data_acquisition/upload_to_mongo.py

preprocess:
	@echo "Preprocessing data."
	source env_vars.env &&\
		python scripts/preprocessing/preprocess_reviews.py

test-evaluation-pipe:
	@echo "Traning evaluation model"
	source env_vars.env &&\
		python scripts/training/test_model_pipe.py --label evaluation

test-confidence-pipe:
	@echo "Traning confidence model"
	source env_vars.env &&\
		python scripts/training/test_model_pipe.py --label confidence

test-pipe: test-evaluation-pipe test-confidence-pipe

train-evaluation:
	@echo "Traning evaluation model"
	source env_vars.env &&\
		python scripts/training/training.py --label evaluation

train-confidence:
	@echo "Traning evaluation model"
	source env_vars.env &&\
		python scripts/training/training.py --label confidence

train: train-evaluation train-confidence

test-dashboard:
	@echo "Launching dashboard"
	source env_vars.env &&\
		python scripts/dashboard/main.py

launch_jupyter:
	@echo "Spawning jupyter server"
	source env_vars.env && jupyter notebook

