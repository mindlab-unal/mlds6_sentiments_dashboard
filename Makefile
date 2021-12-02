SHELL=/bin/bash

data-acquisition:
	@echo "Collecting data."
	source env_vars.env && ./scripts/data_acquisition/download_dataset.sh
