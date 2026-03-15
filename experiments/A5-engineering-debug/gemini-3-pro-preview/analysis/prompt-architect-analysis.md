# Prompt Architect Analysis: Debug Skill

**Prompt:** `experiments/A5-engineering-debug/original/SKILL.md`
**Type:** System Prompt / Skill Definition
**Goal:** Structured debugging session (Reproduce -> Isolate -> Diagnose -> Fix)

## 1. Cognitive Mode Analysis

The prompt attempts to compress a complete engineering workflow into a single context. It requires four distinct types of thinking:

1.  **Exploratory Investigation:** (Step 1-2) "Understand expected vs actual", "Narrow down component", "Review logs". This requires divergent thinking to map the problem space.
2.  **Evaluative Diagnosis:** (Step 3) "Form hypotheses", "Trace code path", "Identify root cause". This requires analytical thinking to rule out possibilities and find the truth.
3.  **Convergent Repair:** (Step 4) "Propose a fix", "Suggest tests". This requires creative/constructive thinking to generate a solution.
4.  **Synthesized Reporting:** (Output Format) "Write a Debug Report". This requires summarization and formatting.

**The Structural Conflict:**
The prompt frames these as sequential steps in "How It Works" (which is correct), but the `## Output` section demands the **final result** immediately. It asks the model to output a `## Debug Report` containing the `### Root Cause` and `### Fix` in the very first turn.

This forces the model to **skip the investigation**. It cannot "Isolate" or "Diagnose" iteratively because the output format demands the answer *now*. The investigation becomes a hallucination to justify the fix, rather than a process to find it.

## 2. Mode Interference

### Investigating while Fixing
> "Step 3: DIAGNOSE ... Step 4: FIX ... Output: ### Root Cause ... ### Fix"

The prompt asks for the diagnosis and the fix in the same artifact. This triggers **solution-bias**. The model will gravitate towards diagnoses that have easy, obvious fixes (e.g., "typo in config") rather than complex, systemic issues that require deep investigation. The desire to fill the `### Fix` slot suppresses the rigorous thinking required for `### Root Cause`.

### Synthesizing while Investigating
> "Output ... ## Debug Report: [Issue Summary]"

The prompt defines a "Debugging Session" (a process) but demands a "Debug Report" (a product). By enforcing the report structure as the *primary output*, it signals to the model: "The investigation is already done. Summarize it."

This is a **temporal collapse**. The model is asked to act as if it has *already* reproduced, isolated, and diagnosed the issue, even though it just received the error message.

### Seeds vs. Lenses
The `## Output` section acts as a strong set of **seeds**:
- `### Reproduction` -> `Steps`
- `### Root Cause`
- `### Fix`

These slots force the model to fill them. If the user only provides a vague error, the model is pressured to *invent* reproduction steps to fill the template, rather than asking the user for them. The structure "tells the model what to find" (a fix) rather than "guiding how to look" (an investigation strategy).

## 3. Diagnostic Signals (What to look for in output)

1.  **Premature Commitment:** The model proposes a specific code fix based solely on the initial error message, without asking for code snippets, logs, or environment details.
2.  **Hallucinated Context:** The `### Reproduction` section contains steps that were not provided by the user and are likely guessed (e.g., "1. Run the app. 2. Click the button.").
3.  **Shallow Root Cause:** The `### Root Cause` is a restatement of the error message (e.g., "The error is caused by a null pointer exception") rather than an explanation of *why* it happened (e.g., "The user object is uninitialized in the async flow because...").
4.  **Missing "Isolate" Phase:** There is no visible evidence of "Step 2: ISOLATE" in the output. The model jumps from Symptom -> Fix.

## 4. Recommendations

### Fix 1: Separate Process from Product (Temporal Separation)
Don't demand the "Debug Report" immediately. Change the Output section to define a **Conversation Strategy**, not a **Document Template**.

*   **Current:** "Output: ## Debug Report..."
*   **Proposed:** "Your goal is to drive the debugging session. Start by asking for necessary context. Only produce the 'Debug Report' when the root cause is confirmed and a fix is verified."

### Fix 2: Use Lenses for Investigation
Replace the static `Step 1... Step 4` with dynamic lenses that guide the *next step* of the investigation.

*   **Lens:** "If the error is vague, ask for reproduction steps."
*   **Lens:** "If the scope is unclear, ask 'when did this start?'"
*   **Lens:** "If a fix is proposed, ask 'what are the side effects?'"

### Fix 3: Pipeline Intervention (Structural Separation)
If this must be an automated tool (not a chat), split it into two agents:
1.  **Investigator Agent:** Given error -> Produces "Investigation Notes" (Hypotheses, requested logs, potential causes). *Mode: Exploratory.*
2.  **Resolver Agent:** Given Investigation Notes -> Produces "Debug Report" (Fix, Root Cause). *Mode: Convergent.*

### Recommended Immediate Action (Prompt Level)
Remove the `## Output` template from the *system prompt* and replace it with instructions on how to *conduct* the session. Add a specific trigger: "When you have identified the root cause and fix, output the final report in this format: [Template]."

This allows the model to stay in "Investigation Mode" (asking questions, exploring) until it has enough information to switch to "Reporting Mode".
