# Pipeline Design Notes: HR Performance Review

## Problem Analysis
The original prompt suffered from **Mode Interference** between *Divergent Search* (finding work) and *Convergent Formatting* (filling the template).
*   **Symptom 1: Shallow Grab.** The model would grab the first few tickets it found to fill the "Accomplishment" slots, ignoring potentially more impactful work later in the context or further down the list.
*   **Symptom 2: Numeric Anchoring.** The template's numbered lists (1, 2, 3) forced the model to hallucinate or omit items to fit the count exactly.
*   **Symptom 3: Tone Drift.** Trying to evaluate performance while fighting formatting constraints often led to generic or biased language.

## Design Strategy
We employ a **Tier 3 Pipeline** to split these conflicting modes into dedicated agents.

### Agent 1: `1-activity-logger` (The Investigator)
*   **Role:** Pure Divergent Search.
*   **Reasoning:** By removing the requirement to "evaluate" or "format", we free the model's context window to focus entirely on *retrieval*. It scans all provided documents/logs and dumps them into a raw list.
*   **Prevention:** Prevents "Recency Bias" and "First-Found Bias" by explicitly demanding a *comprehensive* log before any selection happens.

### Agent 2: `2-impact-analyst` (The Judge)
*   **Role:** Analytic Convergence.
*   **Reasoning:** This agent takes the raw log and applies business logic to select the *best* examples, not just the *first* ones. It groups related small tasks into larger "projects" to see the full picture.
*   **Prevention:** Prevents "Fake Specificity" by checking if the evidence actually supports the impact claims. It decides *what* goes into the review.

### Agent 3: `3-review-writer` (The Scribe)
*   **Role:** Convergent Construction.
*   **Reasoning:** This agent focuses solely on tone, phrasing, and template compliance. It doesn't need to search or judge; it just translates the Analyst's structured findings into the final corporate speak.
*   **Prevention:** Prevents formatting errors and ensures the final output matches the strict template without compromising the content quality.

## Cognitive Mode Mapping
| Agent | Primary Mode | Secondary Mode |
|-------|--------------|----------------|
| `1-activity-logger` | **Divergent Research** | Concrete Organization |
| `2-impact-analyst` | **Convergent Analysis** | Conceptual Evaluation |
| `3-review-writer` | **Convergent Construction** | Creative Refinement |
