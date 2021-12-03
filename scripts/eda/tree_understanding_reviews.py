# # Reviews Tree Understanding

import json, os
os.chdir(os.environ["PROJECT_PATH"])

# ## Data Loading

with open(f"{os.environ['SENTIMENTS_DATASETS']}reviews.json") as f:
    data = json.load(f)

data["paper"][2]


