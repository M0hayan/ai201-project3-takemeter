import os
import pandas as pd
import zipfile

# =========================
# CONFIG
# =========================
TARGET_SIZE = 250
RANDOM_STATE = 42
q_path = "data_q/one-million-reddit-questions.csv"
c_path = "data_c/kaggle_RC_2019-05.csv"
# Kaggle dataset names
QUESTIONS_DATASET = "pavellexyr/one-million-reddit-questions"
COMMENTS_DATASET = "smagnan/1-million-reddit-comments-from-40-subreddits"

# =========================
# STEP 1: DOWNLOAD DATASETS
# =========================
print("Downloading datasets from Kaggle...")

os.system(f"kaggle datasets download -d {QUESTIONS_DATASET} -q")
os.system(f"kaggle datasets download -d {COMMENTS_DATASET} -q")
with zipfile.ZipFile("one-million-reddit-questions.zip", "r") as z:
    z.extractall("data_q")

with zipfile.ZipFile("1-million-reddit-comments-from-40-subreddits.zip", "r") as z:
    z.extractall("data_c")


print("Download complete.")

# =========================
# STEP 2: LOAD QUESTIONS DATASET
# =========================
print("Loading questions dataset...")

q_df = pd.read_csv(q_path, engine="python", on_bad_lines="skip")

# combine title + selftext into one text field
q_df["text"] = (
    q_df["title"].fillna("") + " " + q_df["selftext"].fillna("")
)

q_df = q_df[["text"]]
q_df = q_df[q_df["text"].str.len() > 20]

q_sample = q_df.sample(TARGET_SIZE, random_state=RANDOM_STATE)

q_sample["source"] = "question"
q_sample["llm_label"] = ""
q_sample["final_label"] = ""
q_sample["label_changed"] = ""
q_sample["notes"] = ""

print(f"Questions sample size: {len(q_sample)}")

# =========================
# STEP 3: LOAD COMMENTS DATASET
# =========================
print("Loading comments dataset...")

c_path = "data_c/kaggle_RC_2019-05.csv"
c_df = pd.read_csv(c_path, on_bad_lines="skip", dtype=str)
print("COMMENTS:", c_df.columns)
# filter AskReddit only
c_df = c_df[c_df["subreddit"] == "AskReddit"]

c_df = c_df[["body"]].dropna()
c_df = c_df.rename(columns={"body": "text"})
c_df = c_df[c_df["text"].str.len() > 20]

c_sample = c_df.sample(TARGET_SIZE, random_state=RANDOM_STATE)

c_sample["source"] = "comment"
c_sample["llm_label"] = ""
c_sample["final_label"] = ""
c_sample["label_changed"] = ""
c_sample["notes"] = ""

print(f"Comments sample size: {len(c_sample)}")

# =========================
# STEP 4: MERGE DATASETS
# =========================
print("Merging datasets...")

df = pd.concat([q_sample, c_sample], ignore_index=True)

# shuffle final dataset
df = df.sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)

# add required fields
df["post_id"] = range(len(df))

# limit final size if needed
df = df.head(300)

# =========================
# STEP 5: SAVE
# =========================
output_path = "askreddit_dataset.csv"
df.to_csv(output_path, index=False)

print(f"Saved final dataset → {output_path}")
print(df.head())
print(f"Final size: {len(df)}")