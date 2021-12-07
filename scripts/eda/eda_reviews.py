# -*- coding: utf-8 -*-
# # EDA for Papers Reviews Data

# +
from mlds6sentiment.environment.base import get_mongo_credentials
from mlds6sentiment.database.clients import make_mongo_client
from mlds6sentiment.database.fetch import fetch_from_mongo

from collections import Counter
from wordcloud import WordCloud
from nltk.corpus import stopwords
import nltk, re
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
plt.style.use("ggplot")
nltk.download('stopwords')
# -



mongo_credentials = get_mongo_credentials()
mongo_client = make_mongo_client(mongo_credentials)

result = fetch_from_mongo(
    mongo_client, mongo_credentials.mongo_database,
    "PapersReview",
    {}
)


def review_parse(dataset, field):
    field_raw = list(
        map(
            lambda paper: [review[field] for review in paper["review"]],
            result
        )
    )
    field = field_raw.pop(0)
    for item in field_raw:
        field.extend(item)
    return field


def counts_hist(values, xlabel, ylabel):
    counts = Counter(values)
    counts = {key: value for key, value in counts.items() if key is not None}
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.bar(counts.keys(), counts.values())
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


# ## Evaluations

evaluations = review_parse(result, "evaluation")

counts_hist(evaluations, "Evaluation", "Count")

# # Language

language = review_parse(result, "lan")

counts_hist(language, "Language", "Counts")

# # Confidence

confidence = review_parse(result, "confidence")

counts_hist(confidence, "Language", "Confidence")

# # Orientation

orientation = review_parse(result, "orientation")

counts_hist(orientation, "Language", "Orientation")

result[0].keys()

# # Denormalized data

result

reviews = []
for paper in result:
    paper_dn = paper["review"]
    for review in paper_dn:
        review["paper_id"] = paper["id"]
        review["preliminary_decision"] = paper["preliminary_decision"]
        reviews.append(review)

len(reviews)

reviews_df = pd.DataFrame(reviews)

reviews_df

reviews_df["lan"].value_counts()





# +
# reviews_df[(reviews_df["lan"] == "es") & (reviews_df["orientation"] == "0")].copy()
# df = (reviews_df.query("lan == 'es' and orientation == '0'")
# -

# # Preprocessing

sws = stopwords.words("spanish")
print(sws)


def preprocess_text(document):
    lower_document = document.lower()
    no_signs_document = re.sub(r"[^a-zA-Zéáíóúñ ]", "", lower_document)
    strip_document = no_signs_document.strip()
    tokens = strip_document.split()
    sws = stopwords.words("spanish") 
    white_list = ["nada", "tuvo", "tuve", "tendrá", "sentido"]
    sws = list(filter(lambda word: word not in white_list, sws))
    filtered_tokens = filter(lambda token: token not in sws, tokens)
    return " ".join(filtered_tokens)


clean_reviews_df = (
    reviews_df
    .query("lan == 'es'")
    .drop(columns=["remarks", "orientation", "lan"])
    .fillna(0)
    .astype(
        {
            "confidence": "int", "evaluation": "int", 
            "id": "int", "paper_id": "int"
        }
    )
    .assign(
        timespan = lambda df: pd.to_datetime(df["timespan"], format="%Y-%m-%d"),
        text = lambda df: df["text"].apply(preprocess_text),
        n_words = lambda df: df["text"].apply(lambda document: len(document.split()))
    )
)

clean_reviews_df

# ## Preliminary Decision counts

decisions_df = (
    clean_reviews_df
    .filter(["preliminary_decision", "paper_id"])
    .groupby("paper_id")
    .agg({"preliminary_decision": "first"})
    .reset_index()
)

counts = decisions_df["preliminary_decision"].value_counts()

plt.bar(counts.index, counts)

# # Word Clouds

all_text = " ".join(clean_reviews_df["text"])

wc = WordCloud(width=600, height=600)

im = wc.generate_from_text(all_text)

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.imshow(im)
ax.axis("off")

# ## Word Clouds Evaluation

texts_evaluation = (
    clean_reviews_df
    .groupby("evaluation")
    .agg({"text": lambda texts: " ".join(texts)})
    .reset_index()
) 

texts_evaluation

idxs = texts_evaluation.index
wc = WordCloud(width=600, height=600)

fig, ax = plt.subplots(5, 1, figsize=(5, 25))
for i in idxs:
    row = texts_evaluation.loc[i]
    im = wc.generate(row["text"])
    ax[i].imshow(im)
    ax[i].axis("off")
    ax[i].set_title(f"Evaluation: {row['evaluation']}")

# # Word Clouds Confidence

texts_confidence = (
    clean_reviews_df
    .groupby("confidence")
    .agg({"text": lambda texts: " ".join(texts)})
    .reset_index()
) 

idxs = texts_confidence.index
wc = WordCloud(width=600, height=600)

idxs

fig, ax = plt.subplots(6, 1, figsize=(5, 25))
for i in idxs:
    row = texts_confidence.loc[i]
    im = wc.generate(row["text"])
    ax[i].imshow(im)
    ax[i].axis("off")
    ax[i].set_title(f"Confidence: {row['confidence']}")

# # Word Clouds Decision

texts_decision = (
    clean_reviews_df
    .groupby("preliminary_decision")
    .agg({"text": lambda texts: " ".join(texts)})
    .reset_index()
) 

idxs = texts_decision.index
wc = WordCloud(width=600, height=600)

fig, ax = plt.subplots(4, 1, figsize=(5, 25))
for i in idxs:
    row = texts_decision.loc[i]
    im = wc.generate(row["text"])
    ax[i].imshow(im)
    ax[i].axis("off")
    ax[i].set_title(f"Decision: {row['preliminary_decision']}")

# # Number of words and Evaluation

avg_words_evaluation = (
    clean_reviews_df
    .groupby("evaluation")
    .agg({"n_words": "mean"})
    .reset_index()
)

plt.bar(avg_words_evaluation["evaluation"], avg_words_evaluation["n_words"])
plt.xlabel("Evaluation");
plt.ylabel("Average number of words");

# # Number of words and Confidence

avg_words_confidence = (
    clean_reviews_df
    .groupby("confidence")
    .agg({"n_words": "mean"})
    .reset_index()
)

plt.bar(avg_words_evaluation["confidence"], avg_words_evaluation["n_words"])
plt.xlabel("Confidence");
plt.ylabel("Average number of words");


