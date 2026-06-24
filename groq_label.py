import os
import pandas as pd
from groq import Groq
from dotenv import load_dotenv
from tqdm import tqdm
import time
import json
import re

# =========================
# CONFIG
# =========================
INPUT_FILE = "askreddit_dataset.csv"
OUTPUT_FILE = "askreddit_labeled.csv"

BATCH_SIZE = 10
SLEEP_TIME = 1.2

# =========================
# LOAD ENV
# =========================
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(INPUT_FILE)

# 🔥 CRITICAL FIX: force string dtype
df["llm_label"] = df.get("llm_label", "").astype("string")

# =========================
# LABEL SET
# =========================
LABELS = [
    "Constructive",
    "Low-Effort",
    "Off-topic",
    "Disruptive"
]

# =========================
# PROMPT
# =========================
def build_prompt(texts):
    formatted = "\n\n".join(
        [f"{i+1}. {t[:400]}" for i, t in enumerate(texts)]
    )

    return f"""
You are a strict classifier.

Return ONLY valid JSON.

Format:
{{
  "results": [
    {{"label": "Constructive"}},
    {{"label": "Low-Effort"}},
    {{"label": "Off-topic"}},
    {{"label": "Disruptive"}}
  ]
}}

Rules:
- one label per item
- same order
- no extra text

TEXTS:
{formatted}
""".strip()

# =========================
# JSON PARSER
# =========================
def extract_json(text):
    try:
        return json.loads(text)
    except:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except:
                return None
        return None

# =========================
# GROQ CALL
# =========================
def classify_batch(texts):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": build_prompt(texts)}],
        temperature=0
    )

    content = response.choices[0].message.content

    print("\nRAW SAMPLE:\n", content[:200])

    data = extract_json(content)

    if not data:
        print("❌ JSON parse failed")
        return []

    return data.get("results", [])

# =========================
# MAIN LOOP
# =========================
for start in tqdm(range(0, len(df), BATCH_SIZE)):
    batch = df.iloc[start:start + BATCH_SIZE]
    texts = batch["text"].tolist()

    results = classify_batch(texts)

    for i, r in enumerate(results):
        if i >= len(batch):
            continue

        label = r.get("label", "")

        # 🔥 CRITICAL FIX: ensure string assignment
        df.at[start + i, "llm_label"] = str(label)

    time.sleep(SLEEP_TIME)

# =========================
# SAVE
# =========================
df.to_csv(OUTPUT_FILE, index=False)

print(f"Saved → {OUTPUT_FILE}")
print(df["llm_label"].value_counts())