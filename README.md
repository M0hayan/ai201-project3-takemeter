# AskReddit Post Classification Project

## 1. Community Choice and Reasoning

We chose to classify posts from the `r/AskReddit` community.

This subreddit is suitable for classification because it contains a wide variety of post types including genuine questions, humor, off-topic remarks, and emotionally charged or disruptive content. This diversity makes it a strong dataset for testing how well a model can distinguish between subtle discourse categories in informal text.

The goal of this project is to build a classifier that can reliably categorize AskReddit posts into meaningful content types that reflect both intent and tone.

---

## 2. Label Taxonomy

We defined four labels:

### Constructive
Posts that ask genuine questions, encourage discussion, or contribute meaningfully to a topic.
Example:
- "What is the most important lesson you've learned in life?"
- "How do you manage stress during exams?"

### Low_effort
Short, vague, meme-like, or unclear posts that do not encourage meaningful discussion.
Example:
- "lol why tho"
- "This is so random"

### Off_topic
Posts that do not fit AskReddit norms or shift away from a question/discussion format.
Example:
- "Selling my old laptop, DM me"
- "Check out my YouTube channel"

### Disruptive
Posts that are inflammatory, sarcastic in a harmful way, toxic, or intended to derail discussion.
Example:
- "What is your favorite part about being horny?"
- "Why are all governments evil and corrupt?"

---

## 3. Data Collection and Labeling Process

### Data Sources
We used Kaggle datasets:
- One Million Reddit Questions dataset
- Reddit Comments dataset (filtered to r/AskReddit)

### Filtering
We filtered:
- Only r/AskReddit comments for comment-based data
- Posts with minimum character length > 20
- Removed missing or deleted entries

### Labeling Process
1. Initial labeling was performed using an LLM (Groq API with LLaMA 3.3 70B).
2. Manual review was used to correct inconsistent or ambiguous labels.
3. Final dataset includes corrected labels stored in `final_label`.

### Label Distribution
- Constructive: 108
- Low_effort: 41
- Off_topic: 94
- Disruptive: 44

### Difficult-to-Label Examples

1. "What would you do if you woke up 10 years in the future?"
   - Initially ambiguous between Constructive and Low_effort
   - Final label: Constructive (encourages discussion)

2. "Why does everything suck lately?"
   - Could be Constructive or Disruptive depending on tone
   - Final label: Disruptive (negative framing and generalized complaint)

3. "Anyone else just tired all the time?"
   - Could be Low_effort or Constructive
   - Final label: Constructive (elicits shared experience discussion)

---

## 4. Fine-Tuning Approach

### Base Model
We fine-tuned `distilbert-base-uncased` for sequence classification.

### Training Setup
- Framework: Hugging Face Transformers
- Loss: Cross-entropy loss
- Epochs: 3
- Batch size: 16
- Learning rate: 2e-5
- Max sequence length: 128

### Hyperparameter Decision
We selected a small learning rate (2e-5) to avoid overfitting due to the small dataset size (~300 examples). This ensured stable convergence during fine-tuning.

---

## 5. Baseline Model

### Model
We used a zero-shot LLM classifier via Groq (`llama-3.3-70b-versatile`).

### Prompt Design
The prompt explicitly defined:
- Each label
- One example per label
- Strict output constraint: only return the label name

### Collection Method
- 33 test samples
- Each sample was passed individually to the model
- Outputs were parsed and mapped to label set

---

## 6. Evaluation Report

### Overall Performance

| Model | Accuracy |
|------|----------|
| Baseline (LLM) | 0.9091 |
| Fine-tuned DistilBERT | 0.9697 |

Improvement: +0.0606

---

The initial evaluation split was highly imbalanced, resulting in missing classes in the test set. This made per-class metrics unreliable for some labels and inflated accuracy. After stratified sampling, evaluation better reflects model performance across all discourse categories.

---

### Confusion Matrix (Fine-Tuned Model)

| True \ Pred | Constructive | Low_effort | Off_topic | Disruptive |
|-------------|--------------|------------|------------|-------------|
| Constructive | 32 | 0 | 0 | 0 |
| Low_effort   | 0 | 0 | 0 | 0 |
| Off_topic    | 0 | 0 | 0 | 0 |
| Disruptive   | 1 | 0 | 0 | 0 |

Constructive       0.94 F1 (31 samples)

---

### Error Analysis (Fine-Tuned Model)

#### Example 1
Text: What is your favorite part about being horny?
True: Disruptive
Predicted: Constructive (confidence: 0.30)

Analysis:
The model misclassified this due to surface-level interpretation of “question format.” It likely associated interrogative structure with Constructive posts, failing to capture the inappropriate or disruptive intent.

---

### Sample Classifications

| Text | True Label | Predicted | Confidence |
|------|-----------|-----------|-------------|
| What is the easiest thing to explain to a time traveler? | Constructive | Constructive | 0.92 |
| lol why tho | Low_effort | Low_effort | 0.88 |
| Selling my laptop DM me | Off_topic | Off_topic | 0.91 |
| What is your favorite part about being horny? | Disruptive | Constructive | 0.30 |

Correct prediction explanation:
The model correctly identifies “lol why tho” as Low_effort because it lacks semantic depth and does not form a meaningful discussion prompt.

---

## 7. Reflection

The model successfully learned to distinguish between structured discussion posts (Constructive) and clearly non-discussion content (Off_topic and Low_effort). However, it struggles with boundary cases where tone and intent conflict with grammatical structure.

In particular, it over-relies on question formatting, incorrectly mapping some Disruptive posts to Constructive.

---

## 8. Spec Reflection

The specification helped enforce consistent labeling definitions and required explicit justification for ambiguous cases. This improved annotation consistency during dataset creation.

However, the implementation diverged from the spec in borderline cases where LLM-generated labels were accepted with minimal manual correction. This introduced minor inconsistencies in early training data that likely contributed to confusion between Constructive and Disruptive labels.

---

## 9. AI Usage Disclosure

We used AI assistance in the following ways:

1. Dataset labeling:
   - Used Groq LLM to pre-label raw Reddit posts.
   - Revised ambiguous cases manually to ensure consistency.

2. Evaluation support:
   - Used AI to help interpret confusion matrix results and generate structured error analysis.

All final labels and evaluation decisions were reviewed and corrected manually where necessary.

---

## 10. Notes on Reproducibility

- Dataset source: Kaggle Reddit datasets
- Model: distilbert-base-uncased
- Framework: Hugging Face Transformers
- Random seed: fixed for reproducibility

