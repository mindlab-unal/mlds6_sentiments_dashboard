#/bin/bash
rm ${SENTIMENTS_DATASETS}*
wget https://archive.ics.uci.edu/ml/machine-learning-databases/00410/reviews.json -P "${SENTIMENTS_DATASETS}"
