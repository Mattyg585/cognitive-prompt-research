# PRBench Dataset Analysis — Raw Research Data

## Sources

- Paper: [arxiv.org/abs/2511.11562](https://arxiv.org/abs/2511.11562)
- Dataset: [huggingface.co/datasets/ScaleAI/PRBench](https://huggingface.co/datasets/ScaleAI/PRBench)
- Code: [github.com/scaleapi/PRBench](https://github.com/scaleapi/PRBench)
- Explorer: [prbench-explorer.vercel.app](https://prbench-explorer.vercel.app/)
- Leaderboard (Finance): [labs.scale.com/leaderboard/prbench-finance](https://labs.scale.com/leaderboard/prbench-finance)
- Leaderboard (Legal): [labs.scale.com/leaderboard/prbench-legal](https://labs.scale.com/leaderboard/prbench-legal)

---

## 1. Dataset Structure

### Splits (Parquet files)

| Split | File | Size | Rows |
|-------|------|------|------|
| finance | finance-00000-of-00001.parquet | 5.53 MB | ~550 |
| finance_hard | finance_hard-00000-of-00001.parquet | 3.05 MB | 300 |
| legal | legal-00000-of-00001.parquet | 4.83 MB | ~550 |
| legal_hard | legal_hard-00000-of-00001.parquet | 2.6 MB | 250 |

Total: 1,100 tasks (finance + legal), with 550 Hard subset (300 Finance, 250 Legal).
Hard subset is a strict subset of the full set (the most challenging cases).

### Schema — Top-Level Fields

| Field | Type | Description |
|-------|------|-------------|
| `task` | string | Unique task identifier |
| `turns` | int64 | Number of conversation turns |
| `field` | string | Domain: "Finance" or "Legal" |
| `topic` | string | Specific topic within domain |
| `expert` | string | Expert identifier |
| `scratchpad` | string | Expert notes/scratchpad |
| `rubric` | list[struct] | List of rubric criterion objects |
| `id` | string | Unique ID |
| `title` | string | Task title |
| `prompt_0` | string | First user prompt (the question) |
| `response_0` | string | First assistant response (for multi-turn context) |
| `model_0` | string | Model used for response_0 |
| `reference_texts_0` | list[string] | Reference texts prepended to prompt_0 |
| `prompt_1` | string | Second user prompt (if multi-turn) |
| `response_1` | string | Second assistant response (if multi-turn) |
| `model_1` | string | Model used for response_1 |
| `reference_texts_1` | list[string] | Reference texts for turn 1 |

Multi-turn fields continue through `prompt_9` / `response_9` (up to 10 turns).
~30% of tasks are multi-turn.

### Schema — Rubric Criterion (Nested struct within `rubric` list)

Each rubric entry is a struct with an `annotations` sub-struct containing:

| Nested Field | Type | Description |
|-------------|------|-------------|
| `criteria_category` | string | One of the 11 rubric categories |
| `criteria_description` | string | The criterion text (what to evaluate) |
| `weight_class` | string | Severity level (see below) |
| `critically_important_weight` | int64 | Weight if weight_class = "critically important" |
| `important_weight` | int64 | Weight if weight_class = "important" |
| `slightly_important_weight` | int64 | Weight if weight_class = "slightly important" |
| `slightly_detrimental_weight` | int64 | Weight if weight_class = "slightly detrimental" |
| `detrimental_weight` | int64 | Weight if weight_class = "detrimental" |
| `critically_detrimental_weight` | int64 | Weight if weight_class = "critically detrimental" |
| `field_for_category` | string | Domain-specific category qualifier |

The actual weight used is determined by `weight_class`: the code does `d[weight_class.replace(" ", "_") + "_weight"]` to look up the appropriate weight column.

---

## 2. Weight Classes (Severity Levels)

Six severity levels, from Table 2 of the paper:

### Positive (desirable qualities)

| Weight Class | Description | Weight Range |
|-------------|-------------|--------------|
| **Critically Important** | Essential criteria without which the response would fail to adequately address the prompt. Defines the minimally viable rubric set — the core, indispensable aspects. | +7 to +10 |
| **Important** | Criteria that meaningfully strengthen a response by adding depth, accuracy, or completeness. Materially shape quality but not strictly required for acceptability. | +4 to +6 |
| **Slightly Important** | Optional enhancements or "nice-to-have" details that improve clarity or precision but do not affect core correctness. | +1 to +3 |

### Negative (undesirable properties)

| Weight Class | Description | Weight Range |
|-------------|-------------|--------------|
| **Slightly Detrimental** | Minor issues or irrelevant tangents that slightly detract from quality or focus. | -1 to -3 |
| **Detrimental** | Significant errors or omissions that meaningfully weaken the response — misleading reasoning, incorrect facts, major structural flaws — though the response remains generally valid. | -4 to -6 |
| **Critically Detrimental** | Severe errors that render the response fundamentally invalid, harmful, or unethical. Issues that directly contradict the prompt or destroy the credibility of the reasoning. | -7 to -10 |

Note: Weights are integers in [-10, +10], excluding 0. The weight range per class is inferred from the schema (each class has its own column) and the paper's statement that weights range from -10 to +10.

---

## 3. Rubric Categories (11 Total)

### 5 Shared categories (both Finance and Legal):

1. **Practical Utility** — Is the response actionable and useful for the professional scenario?
2. **Handling Uncertainty** — Does the response appropriately acknowledge and manage ambiguity, unknowns, and limitations?
3. **Supplemental Insight** — Does the response provide additional valuable context, connections, or considerations beyond the direct question?
4. **Instruction Following** — Does the response follow the specific instructions and constraints in the prompt?
5. *(Fifth shared category name not explicitly stated in available sources — likely "Completeness" or "Clarity of Communication")*

### Legal-specific categories (3-4):

6. **Legal Accuracy** — Is the legal analysis correct?
7. **Procedural Correctness** — Are procedures, filings, and process steps accurate?
8. **Risk & Ethical Disclosure** — Are risks, ethical considerations, and limitations properly disclosed?
9. **Application of Law to the Facts** — Is the legal reasoning properly applied to the specific facts of the scenario? (Similar to "Rule Application" from LegalBench)

### Finance-specific categories (3):

10. **Financial Accuracy** — Are financial calculations, concepts, and analysis correct?
11. **Process Transparency & Auditability** — Is the reasoning process transparent and could be audited?
12. **Risk & Regulatory Disclosure** — Are financial risks and regulatory considerations properly disclosed?

(Note: 11 total unique categories, some domain-specific)

---

## 4. Scoring System

### Judge Prompt (GRADER_TEMPLATE)

The complete judge prompt from `constants.py`:

```
Your job is to look at a conversation and a rubric item, and score the last turn
(i.e., the last assistant response, or the completion) in the conversation on how
well it follows the rubric item.

# Conversation
<<conversation>>

# Rubric item
<<rubric_item>>

# Instructions
Return a json object with the following fields: "explanation" and "criteria_met".
- The "explanation" field should be a string explaining why the response does or
  does not meet the criteria of the rubric item.
- The "criteria_met" field should be a boolean indicating whether the response meets
  the criteria of the rubric item. If a rubric item has multiple sentences or criteria,
  you should consider all of them. If any of the criteria is not met, the answer should
  be false. Only return true is all of the criteria are met.
- One important exception: if a criteria says "such as", "for example", or "including",
  the response does not have to include all of the examples listed to meet the criteria.

# Example 1
[Positive criterion example — response doesn't match, returns false]

# Example 2
[Negative criterion example — criteria_met is about whether the BAD thing happened,
not whether the response is good. So a good response that avoids the bad thing = false]

Return just the json object in markdown format. Do not include any other text.
```

### Judge Model

o4-mini (OpenAI)

### Scoring Formula

For each task T_i with rubric criteria {c_1, ..., c_n}:

1. **Per-criterion grading**: Judge returns `criteria_met: true/false` for each criterion
2. **Binary to numeric**: `true` -> 1, `false` -> 0
3. **Weighted sum**: `total_points = sum(grade_j * weight_j)` for all criteria j
4. **Clipped score**: `score = total_points / sum(weight_j for weight_j > 0)`, clipped to [0, 1]
5. **Normalized score** (for category-level): `score = (total_points - min_possible) / (max_possible - min_possible)`

The **reported metric is `mean_clipped`** — the mean of clipped scores across all tasks.

### Validation

- Rubric Validation: 93.9% agreement between independent experts on criterion clarity/validity
- Judge Validation (IRA): o4-mini judge achieves 80.2% agreement with human experts (vs 79.6% human-human agreement)

---

## 5. Difficulty Determination

PRBench does NOT use explicit easy/medium/hard labels per task. Instead:

- The **full set** (finance, legal) contains all 1,100 tasks
- The **Hard subset** (finance_hard, legal_hard) contains the 550 most challenging tasks (300 Finance, 250 Legal), selected "following the methodology of HealthBench"
- Tasks NOT in the Hard subset are implicitly "easier"

For our experiment, we define difficulty by:
- **EASY**: A task from the full set that is NOT in the Hard subset, single-turn, with fewer rubric criteria (~10-15)
- **MEDIUM**: A task from the full set that IS in the Hard subset OR is multi-turn with moderate complexity
- **HARD**: A task from the Hard subset that is multi-turn with many rubric criteria (~25-30) spanning multiple categories

### Current best model performance by difficulty:

| Metric | Finance (Full) | Finance (Hard) | Legal (Full) | Legal (Hard) |
|--------|---------------|----------------|-------------|-------------|
| GPT-5 Pro | 0.51 | 0.39 | 0.50 | 0.37 |
| GPT-5 | 0.51 | 0.39 | 0.49 | 0.36 |
| o3 High | 0.47 | 0.35 | 0.47 | 0.35 |

---

## 6. Topics Covered

### Finance (13 topics):
Specific topic names not enumerated in available sources, but tasks span: investment analysis, tax planning, financial reporting, regulatory compliance, risk management, portfolio management, corporate finance, auditing, derivatives, banking, insurance, wealth management, fintech.

### Legal (12 topics):
Specific topic names not enumerated in available sources, but tasks span: contract law, criminal law, employment law, intellectual property, real estate, family law, tax law, immigration, environmental law, corporate governance, litigation strategy, regulatory compliance.

Tasks span 114 countries and 47 US jurisdictions.

---

## 7. How to Load the Dataset

```python
from datasets import load_dataset

# Full finance set
ds_finance = load_dataset("ScaleAI/PRBench", split="finance")

# Hard finance subset
ds_finance_hard = load_dataset("ScaleAI/PRBench", split="finance_hard")

# Full legal set
ds_legal = load_dataset("ScaleAI/PRBench", split="legal")

# Hard legal subset
ds_legal_hard = load_dataset("ScaleAI/PRBench", split="legal_hard")
```

### Extracting task data for our experiment:

```python
import json

ds = load_dataset("ScaleAI/PRBench", split="finance")

for row in ds:
    task_id = row['task']
    title = row['title']
    field = row['field']
    topic = row['topic']
    turns = row['turns']
    prompt = row['prompt_0']
    rubric = row['rubric']  # list of criterion dicts

    # Each criterion in rubric:
    for criterion in rubric:
        ann = criterion['annotations']
        desc = ann['criteria_description']
        cat = ann['criteria_category']
        wclass = ann['weight_class']
        # Get actual weight:
        weight_key = wclass.replace(" ", "_") + "_weight"
        weight = ann[weight_key]
        print(f"  [{wclass}] ({weight}) [{cat}] {desc}")
```

---

## 8. Task Selection Strategy

### Requirements:
1. One EASY (Finance, single-turn, not in Hard subset, ~10-15 criteria)
2. One MEDIUM (Legal, could be multi-turn, in Hard subset, ~15-20 criteria)
3. One HARD (Finance or Legal, multi-turn, in Hard subset, ~25-30 criteria, multiple rubric categories)

### Selection criteria:
- Different domains (Finance and Legal)
- Different topics within those domains
- Tasks that require multi-mode reasoning (investigation + analysis + synthesis)
- Tasks where the rubric categories span multiple cognitive modes

### How to select:

```python
from datasets import load_dataset
import json

# Load both full and hard sets
finance = load_dataset("ScaleAI/PRBench", split="finance")
finance_hard = load_dataset("ScaleAI/PRBench", split="finance_hard")
legal = load_dataset("ScaleAI/PRBench", split="legal")
legal_hard = load_dataset("ScaleAI/PRBench", split="legal_hard")

hard_finance_ids = set(r['task'] for r in finance_hard)
hard_legal_ids = set(r['task'] for r in legal_hard)

# EASY: Finance task NOT in hard subset, single-turn, fewer criteria
easy_candidates = [r for r in finance
                   if r['task'] not in hard_finance_ids
                   and r['turns'] == 1
                   and len(r['rubric']) <= 15]

# MEDIUM: Legal task IN hard subset, moderate criteria count
medium_candidates = [r for r in legal_hard
                     if 15 <= len(r['rubric']) <= 22]

# HARD: Either domain, in hard subset, multi-turn, many criteria, multi-category
hard_candidates = [r for r in list(finance_hard) + list(legal_hard)
                   if r['turns'] >= 2
                   and len(r['rubric']) >= 22]

# Sort by number of unique rubric categories (more diverse = more interesting)
def category_diversity(row):
    cats = set()
    for c in row['rubric']:
        cats.add(c['annotations']['criteria_category'])
    return len(cats)

hard_candidates.sort(key=category_diversity, reverse=True)

# Print top candidates for each
for label, candidates in [("EASY", easy_candidates[:5]),
                           ("MEDIUM", medium_candidates[:5]),
                           ("HARD", hard_candidates[:5])]:
    print(f"\n=== {label} ===")
    for r in candidates:
        n_crit = len(r['rubric'])
        n_cats = category_diversity(r)
        print(f"  {r['task']} | {r['field']} | {r['topic']} | turns={r['turns']} | criteria={n_crit} | categories={n_cats}")
        print(f"    Title: {r['title']}")
        print(f"    Prompt: {r['prompt_0'][:200]}...")
```

---

## 9. Mapping Rubric Categories to Cognitive Modes

This is a hypothesis to be tested, not assumed:

| Rubric Category | Likely Cognitive Mode | Interference Risk |
|----------------|----------------------|-------------------|
| Legal/Financial Accuracy | Analytical (convergent) | Interferes with exploratory investigation |
| Process Transparency & Auditability | Meta-cognitive / Reflective | Interferes with generative synthesis |
| Risk & Ethical/Regulatory Disclosure | Evaluative (judgment) | Classic toxic pair with Investigation |
| Handling Uncertainty | Epistemic (stance-setting) | Interferes with confident assertion |
| Supplemental Insight | Divergent / Creative | Interferes with focused analysis |
| Practical Utility | Applied / Pragmatic | Interferes with thorough investigation |
| Instruction Following | Procedural / Compliance | Generally compatible with all modes |
| Procedural Correctness | Analytical (convergent) | — |
| Application of Law to the Facts | Synthetic (bridging) | Requires clean handoff from investigation |

The key prediction: **Process Transparency, Handling Uncertainty, and Supplemental Insight** are the categories most likely to improve under pipeline separation, because they require cognitive modes that directly interfere with the accuracy-focused modes that dominate monolithic prompts.

---

## 10. PRBench Evaluation Infrastructure (from GitHub)

### Key files:

| File | Purpose |
|------|---------|
| `evals.py` | Main entry point — response generation, LLM-judge scoring, caching, reporting |
| `criteria.py` | `Criterion` class — parses rubric annotations, extracts weights by weight_class |
| `constants.py` | `GRADER_TEMPLATE` (judge prompt), `GRADE_MAP`, domain classification templates |
| `config.py` | `Config` dataclass — model names, API settings, debug mode |
| `config.yaml` | Default config — o4-mini judge, 20 response models, timeout 3600s |
| `util.py` | Async query, caching, grading pipeline, scoring functions |

### Running PRBench evaluation:

```bash
pip install -r requirements.txt
# Configure config.yaml with API keys
python evals.py config.yaml
```

### Using prefilled responses (for our experiment):

```yaml
# config.yaml
final_response_source: prefilled
filename: our_responses  # looks for our_responses.json
```

```json
// our_responses.json — task ID -> response text
{
  "task_id_1": "Our model response for task 1...",
  "task_id_2": "Our model response for task 2..."
}
```

---

## 11. What We Still Need

**CRITICAL: The actual task data must be loaded from HuggingFace.** This environment cannot access HuggingFace directly. To complete task selection:

1. Run the selection script from Section 8 in an environment with internet access
2. For each selected task, extract:
   - Full `prompt_0` (and `prompt_1` etc. if multi-turn)
   - Full `response_0` (the pre-filled assistant turn for multi-turn context)
   - All `reference_texts_0` (prepended to prompts)
   - Complete rubric with all criteria, categories, weights
   - Task metadata (topic, turns, field)
3. Save each task as a standalone markdown file in `tasks/`

### Recommended selection approach:

Pick tasks that maximize cognitive mode diversity in their rubrics:
- **EASY (Finance)**: A single-turn tax or financial reporting question with clear analytical focus. Look for tasks with topic like "Tax" or "Financial Reporting" that are NOT in finance_hard.
- **MEDIUM (Legal)**: A legal analysis task requiring both investigation of applicable law AND application to facts. Look for tasks in legal_hard with topics like "Employment Law" or "Contract Law" with 15-20 criteria.
- **HARD (Finance or Legal)**: A multi-turn task that requires investigation, analysis, risk assessment, AND practical recommendations. Look for multi-turn tasks in the hard subsets with 25+ criteria spanning 5+ rubric categories.
