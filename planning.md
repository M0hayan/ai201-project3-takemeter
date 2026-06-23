**The Selected Community**
For this project I selected the R/AskReddit community as it is a popular subreddit with various different types of responses which allows me to find good and effective labels. It is a community where people ask questions of any type so it is fit for classifying.


**Definintion of the Labels**
1. Constructive / Substantive Answer
A comment that meaningfully answers the question with explanation, story, reasoning, or detail. It contributes real information or perspective beyond a simple reaction.

2. Low-Effort / Joke 
A response that is primarily humorous, sarcastic, or extremely brief without adding depth or reasoning. Includes memes, puns, or single-sentence reactions.

3. Off-topic / Meta / Rule-Discussion
A comment that shifts away from answering the question and instead discusses moderation, the subreddit itself, posting rules, or unrelated topics.

4. Disruptive / Uncivil 
A comment that includes insults, trolling, hostility, or clearly non-serious engagement intended to provoke rather than contribute.

**Examples of each label**
1) https://www.reddit.com/r/AskReddit/comments/1jo2r8t/what_askreddit_question_have_you_asked_but_the/
It fits because it contains long-form personal stories and users give detailed emotional or experiential answers (not just reactions)
https://www.reddit.com/r/AskReddit/comments/lu0zrx/whats_something_from_10_years_ago_that_doesnt/
This one also fits since it is a serious question and many of the answers directly answer it.

2) https://www.reddit.com/r/AskReddit/comments/ablzuq/people_who_havent_pooped_in_2019_yet_why_are_you/
   This post clearly is not serious and intended to be funny which is why most of the responses followed by also not being serious
https://www.reddit.com/r/AskReddit/comments/1jorjc6/what_is_your_best_joke/
This post is meant to garner funny posts that are supposed to be jokes.


4) https://www.reddit.com/r/AskReddit/comments/xzt76/modpost_askreddit_what_do_you_think_of_this/?utm_source=chatgpt.com
  The entire discussion is about how the subreddit works and many do not answering any AskReddit prompt.
https://www.reddit.com/r/AskReddit/comments/1uagxbu/removed_by_moderator/?utm_source=chatgpt.com
This post focuses on subreddit moderation rules, not the question itself.

4) https://www.reddit.com/r/AskReddit/comments/1u5o1xk/what_askreddit_question_have_you_asked_but_the/?utm_source=chatgpt.com
Threads often contain sarcastic dismissals or “this is dumb” replies. It also has a mix of bad-faith engagement and mockery appears frequently.
https://www.reddit.com/r/AskReddit/comments/1ommxw2/whats_something_that_instantly_makes_you_lose/
has comments like: sarcasm aimed at groups of people and bad-faith generalizations (“all X are idiots”).

**Edge 1s post examples (unsure about which label)**
Constructive Vs Low Effort
https://www.reddit.com/r/AskReddit/comments/145zqnb/whats_an_important_lesson_you_learnt_the_hard_way/

Low effort vs Disruptive
https://www.reddit.com/r/AskReddit/comments/1u5o1xk/what_askreddit_question_have_you_asked_but_the/
https://www.reddit.com/r/AskReddit/comments/1t0nm9z/how_do_we_know_the_earth_is_not_flat/

Construvtive vs Disruptive
https://www.reddit.com/r/AskReddit/comments/1u2q6zf/whats_something_that_is_socially_acceptable_but/

Low effort vs off-topic
https://www.reddit.com/r/AskReddit/comments/1gpvpgb/whats_a_question_youre_tired_of_seeing_on/

**Handling edge cases**
1. Use a strict “primary intent” rule (most important)

When a comment fits multiple labels, you do not average or split it. You assign the label based on:

What is the main purpose of the comment? What is it trying to do?

Priority order (use this as a tie-breaker)

If multiple labels seem possible, choose in this order:

Disruptive / Uncivil (if present)
Off-topic / Meta
Constructive / Substantive
Low-effort / Joke

Why this order works:
Harmful content should never be “downgraded” to humor or low effort
Meta content is structurally different from answering behavior
Constructive answers are your “signal class”
Low-effort is the default fallback when nothing meaningful is happening
2. Define “hard rules” for common ambiguity
A. Sarcasm vs insult
“People are idiots” → Disruptive
“Yeah sure, because that totally makes sense” → Low-effort

Rule:

If it attacks a person/group → Disruptive
If it mocks without a clear target → Low-effort

B. Short but meaningful answers
“Don’t trust people easily” → Low-effort
“Don’t trust people easily—I learned that after being scammed in college…” → Constructive

Rule:

No explanation = Low-effort
Any reasoning/story = Constructive

C. Meta complaints vs jokes
“Mods always delete everything here” → Off-topic/meta
“This sub is trash lol” → Low-effort (unless hostile/explosive tone)

Rule:

If it talks about subreddit rules/mods → Off-topic/meta
If it’s just a throwaway insult → Low-effort or Disruptive (depending on severity)

3. Introduce a “no overthinking” rule

This is important for consistency:

If you are unsure after 10–15 seconds of reading, choose the simplest applicable label

Why:

prevents inconsistent deep reasoning across annotators
keeps dataset decision boundaries sharp
4. Create a “write-down ambiguity log” (very important for your report)

Every time you hit an edge case, you record:

comment text
which labels you considered
final label
1 sentence why

Example:

“This comment could be Low-effort or Disruptive. Chose Disruptive because it directly insults a group.”

we would need ~15–30 of these for the report.

*Edge case descriptions and summary of handling rules for each:*
1. Constructive vs Low-Effort
Edge Case Description

Short answers that express a “correct-sounding” idea but lack explanation or context.

Ambiguity
Could be seen as a valid insight (Constructive)
Or as a generic one-liner (Low-Effort)
Examples
“Don’t trust people too easily.”
“Money doesn’t buy happiness.”
Decision Rule
If there is no explanation, story, or reasoning → Low-Effort
If there is context, example, or explanation → Constructive
2. Low-Effort vs Disruptive
Edge Case Description

Sarcastic or humorous comments that may sound insulting but are not clearly targeted.

Ambiguity
Could be joke (Low-Effort)
Could be hostile (Disruptive)
Examples
“People are idiots lol”
“Yeah because that totally worked out great 🙄”
Decision Rule
If it includes direct insult toward a person/group → Disruptive
If it is generic sarcasm or joke without clear target → Low-Effort
3. Constructive vs Disruptive
Edge Case Description

Strong opinions expressed in an argumentative or emotionally charged way.

Ambiguity
Could be valid reasoning (Constructive)
Could be moralized insult or hostility (Disruptive)
Examples
“Anyone who thinks this is okay is selfish and ignorant.”
“I disagree because this ignores the social context…”
Decision Rule
If the comment includes personal attacks or moral condemnation → Disruptive
If it presents reasoning without attacking individuals → Constructive
4. Off-topic / Meta vs Low-Effort
Edge Case Description

Comments that criticize the subreddit or the question itself, sometimes in humorous ways.

Ambiguity
Could be subreddit discussion (Off-topic)
Could be casual joke or complaint (Low-Effort)
Examples
“This sub has gone downhill lately.”
“Another recycled AskReddit question…”
Decision Rule
If it refers to rules, moderation, or subreddit structure → Off-topic
If it is just a casual complaint or joke → Low-Effort
5. Off-topic vs Disruptive
Edge Case Description

Comments that criticize the post or users in a hostile way instead of engaging the question.

Ambiguity
Could be meta criticism (Off-topic)
Could be insulting or aggressive (Disruptive)
Examples
“Only idiots would ask this.”
“This question is stupid and so are the people answering it.”
Decision Rule
If tone includes insults or hostility → Disruptive
If it is neutral discussion of subreddit behavior → Off-topic
6. Joke vs Disruptive Humor
Edge Case Description

Dark humor or edgy jokes that may appear offensive but are not direct attacks.

Ambiguity
Could be humor (Low-Effort)
Could be uncivil (Disruptive)
Examples
“My life choices, apparently.”
“Society is a dumpster fire and I’m just here for the ride.”
Decision Rule
If it is self-referential or general humor → Low-Effort
If it targets identifiable groups or individuals → Disruptive

**Data collection plan**

All examples will come from r/AskReddit on Reddit.

Data will be collected using:

The Reddit website (manual sampling for labeling control)
The Reddit API (PRAW) or Pushshift-style archives if needed
Sorting methods:
“Top” posts (to get high-engagement, diverse comments)
“Hot” posts (to capture current discourse patterns)
“Rising” posts (to avoid only popular meme-heavy content)

Each selected post will contribute multiple comments to ensure variety within threads.

Dataset size target

Total dataset: ~200–300 labeled comments

Planned split:
Training: 70% (~140–210 examples)
Validation: 15% (~30–45 examples)
Test: 15% (~30–45 examples)

*Target distribution:*
| Label                      | Target Count | Notes                                                                   |
| -------------------------- | ------------ | ----------------------------------------------------------------------- |
| Constructive / Substantive | ~60          | harder to find in AskReddit, may require sampling longer threads        |
| Low-Effort / Joke          | ~60          | very common, likely easiest to collect                                  |
| Off-topic / Meta           | ~40          | moderately common, especially in moderation-heavy threads               |
| Disruptive / Uncivil       | ~40          | less frequent in top posts, may require searching controversial threads |

If after collecting ~200 examples a label is underrepresented, we will use targeted re-sampling instead of random collection.

1. Constructive too low

If not enough high-quality answers:

sample posts like:
“What life lesson did you learn the hard way?”
“What changed your perspective on life?”
focus on:
“Top” comments (higher likelihood of detailed answers)
2. Low-Effort too low

This is unlikely, but if it happens:

sample joke-heavy prompts:
“What’s something you can say in X and Y situations?”
“Funny questions / pun-based AskReddit threads”
3. Off-topic / Meta too low

If underrepresented:

explicitly search for:
“AskReddit meta”
moderator announcement threads
“why was my post removed”
include comment sections discussing rules/mod behavior
4. Disruptive / Uncivil too low (most likely issue)

If underrepresented:

sample controversial prompts:
moral judgment questions
relationship advice questions
opinion polarizers (“What’s socially acceptable but shouldn’t be?”)
include more:
controversial sorting (not just “Top” but “Controversial” if available)

**Evaluation metrics**
1. Overall Accuracy (baseline metric)

What it measures: Percentage of correctly classified comments.

Why we include it:

Easy to interpret
Good high-level sanity check
Lets us compare quickly against the zero-shot Groq baseline

Why it is insufficient:

Can be misleading if one class dominates (e.g., lots of Low-Effort jokes)
Doesn’t show which labels the model is actually good or bad at
2. Macro-Averaged F1 Score (primary metric)

What it measures:

F1 score computed per class, then averaged equally across all classes

Why it matters for this task:

Treats all labels equally regardless of frequency
Forces the model to perform well on rare but important classes (especially Disruptive and Off-topic)

Why it’s better than accuracy:

Prevents the model from “cheating” by over-predicting the most common label (likely Low-Effort)
3. Per-Class Precision, Recall, and F1

we will report these for each label:

Constructive / Substantive
Low-Effort / Joke
Off-topic / Meta
Disruptive / Uncivil
Why this is necessary:

It helps answer diagnostic questions like:

Does the model over-label sarcasm as Disruptive? → low precision on Disruptive
Does it miss constructive answers? → low recall on Constructive
Does it confuse jokes with insults? → cross-class errors
4. Confusion Matrix (critical for error analysis)

What it shows:
A full breakdown of:

what the model predicted
vs what the true label was
Why it matters:

This is where we will see systematic issues like:

Low-Effort ↔ Disruptive confusion (very common in Reddit data)
Constructive being misclassified as Low-Effort when answers are short
Off-topic being confused with Disruptive in meta threads

5. Zero-shot vs Fine-tuned Comparison (requirement)

we will evaluate both:

A. Fine-tuned DistilBERT
trained on the labeled dataset
B. Groq Llama-3.3-70B zero-shot classifier

Prompt example:

“Classify this Reddit comment into one of: Constructive, Low-Effort, Off-topic, Disruptive. Return only the label.”

Why this matters:
Shows whether fine-tuning actually adds value
Establishes a strong baseline for comparison
Helps justify the dataset creation effort
6. Error Analysis (qualitative metric, but required)

we will manually inspect at least 3–10 misclassified examples, and categorize errors like:

sarcasm misunderstood as Disruptive
short constructive answers labeled Low-Effort
meta comments misclassified as normal discourse
Why this matters:
Metrics alone won’t explain why the model fails
This connects model behavior back to the label design choices


**Definition of success**
A “successful” model here is not one that is perfect—it’s one that is reliably better than a naive baseline and stable enough to be useful for surfacing discourse quality patterns in real threads.

Because this is a 4-class subjective NLP task, “good enough” should be defined in terms of comparative performance, consistency, and error tolerance, not just raw accuracy.
A model is considered working / usable for analysis if:

1. It clearly beats zero-shot baseline
Fine-tuned model improves over Groq Llama-3.3-70B on:
overall accuracy
macro-F1 score
Even a modest improvement (e.g., +5–10%) is meaningful.
2. Macro-F1 ≥ 0.65 (minimum acceptable threshold)
This ensures the model is not just predicting the majority class
It indicates reasonable performance across all 4 labels

Why this matters:

Random guessing ≈ 0.25
Majority-class guessing could look “okay” in accuracy but fail in practice
0.65 macro-F1 shows real signal learning
3. No “collapsed classes”

The model must NOT:

ignore Disruptive entirely
or overpredict Low-Effort for everything

Minimum requirement:

each class should have non-trivial recall (>0.4)

This ensures the classifier is actually learning distinctions between discourse types.

4. Confusion matrix shows interpretable structure

A successful model should show:

reasonable confusion between similar classes (expected)
Low-Effort ↔ Constructive (short answers)
Low-Effort ↔ Disruptive (sarcasm)
but NOT chaotic behavior (everything predicted as everything)

**AI Tool Plan**
Stress testing and example posts: 1. Constructive vs Low-Effort
Post:
“Honestly, most people overthink confidence—it just comes from doing things repeatedly.”
Why it’s a boundary case: Could be seen as a useful psychological insight (Constructive), but lacks explanation or grounding (Low-Effort).

2. Constructive vs Low-Effort
Post:
“Sleep is basically the most underrated productivity hack.”
Why: Sounds like advice, but no reasoning or detail.

3. Low-Effort vs Disruptive
Post:
“Yeah sure, because that always works out so well 🙄”
Why: Could be sarcastic general reaction (Low-Effort), but may imply criticism depending on context (Disruptive).

4. Low-Effort vs Disruptive
Post:
“People really think this is a good idea lol”
Why: Could be casual mockery (Low-Effort) or directed ridicule (Disruptive if target is implied).

5. Constructive vs Disruptive
Post:
“I think this approach fails because it ignores how incentives actually shape behavior.”
Why: Reasoned critique (Constructive), but in heated discussions could be interpreted as dismissive (Disruptive).

*Annotation assitance*
I will use Groq (llama-3.3-70b-versatile) with a strict prompt like: 
a strict prompt like:
Classify this AskReddit comment into one of:
Constructive, Low-Effort, Off-topic, Disruptive.
Return ONLY the label.

For each example I'll:
check LLM label
confirm or override
optionally mark as:
“correct”
“changed”
“edge case”
I will have to make csv columns like 
| id | text | llm_label | final_label | label_changed | notes |
| -- | ---- | --------- | ----------- | ------------- | ----- |

*Failure analysis:*
I will use the tool  aggressively for:
Low-Effort (very reliable)
Disruptive (usually obvious)
Off-topic/meta (also fairly rule-based)
But I'll have to double check and be careful for:
Constructive vs Low-Effort boundary
sarcasm detection
short-but-meaningful answers
