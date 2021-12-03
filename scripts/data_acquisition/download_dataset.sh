#/bin/bash
rm ${RAW_DATA_PATH}*
wget https://archive.ics.uci.edu/ml/machine-learning-databases/00410/reviews.json -P "${RAW_DATA_PATH}"
