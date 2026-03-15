# Prompt Architect Analysis: HR Performance Review

## 1. Thinking Types
This prompt acts as a **structure generator** and **contextual filler**. It asks the model to:
1.  **Recall/Search**: Look up employee data and work history (via Connectors).
2.  **Evaluate**: Assess performance against goals (implied in "Pre-populate...").
3.  **Format**: Fit this information into rigid Markdown templates.

The dominant mode is **Convergent Construction** (filling boxes).

## 2. Mode Interference
The primary interference sits in the **Connectors** section interacting with the **Templates**.

> **Quote:**
> "If **~~project tracker** is connected:
> - Pull completed work and contributions for the review period
> - Reference specific tickets and project milestones as evidence"

**The Mechanism:**
The prompt provides a rigid destination (the template with specific slots) and asks the model to fetch data to fill it.
*   **Search vs. Formatting:** The model is asked to "Pull completed work" (Divergent search) and immediately put it into "1. **[Accomplishment]**" (Convergent formatting).
*   **Result:** The model will likely perform a "shallow grab" — finding the first few tickets that fit the "Accomplishment" slot and stopping. It won't perform a comprehensive review of the period to find the *most significant* work because the cognitive pressure is to "fill the template," not "analyse performance."

## 3. What to Look For (Diagnostics)
*   **The "First-Found" Bias:** In the `manager` mode with a project tracker, look for whether the "Key Accomplishments" are just the most recent or most obvious tickets, ignoring more impactful work from earlier in the quarter.
*   **Numeric Anchoring:** The `self-assessment` template lists exactly **3** numbered slots for "Goals for Next Period". Expect the output to contain exactly 3 goals every time, regardless of the employee's actual context.
*   **Forced Distribution:** In `calibration` mode, the prompt lists company targets (e.g., "~15-20% Exceeds"). Check if the model forces the "Proposed Rating" counts to match these percentages exactly, potentially misrepresenting the actual performance data to fit the distribution.
*   **Fake Specificity:** The template demands "Impact: [Measurable result]". If the source data doesn't have metrics, look for the model hallucinating or vaguely inferring numbers to satisfy the constraint.

## 4. Interventions

### Option A: Prompt-Level Fixes (Low Cost)
*   **Remove Numeric Anchors:** Replace numbered lists ("1., 2., 3.") in the templates with open bullets or instructions like `[List 3-5 key goals]`.
*   **Separate Retrieval from Writing:** In the instructions, explicitly tell the model to "First, scan the project tracker to create a summary of work. *Then*, select the most impactful items to populate the template." This creates a temporal separation of modes within one prompt.

### Option B: Pipeline-Level Interventions (High Value)
*   **Split the "Manager" Review:**
    1.  **Agent 1 (Investigator):** "Review the project tracker and HRIS. Produce a raw log of all significant activities, completed goals, and dropped balls for this period. Do not evaluate yet."
    2.  **Agent 2 (Evaluator/Writer):** "Using the activity log, draft the performance review. Select the top 3 accomplishments based on business impact."
    
    *Trade-off:* Slower and more token-intensive, but prevents the "shallow grab" and ensures the review reflects the whole period, not just the recent context window.

### Option C: Calibration Safety
*   **Hide Targets Initially:** For the calibration prep, do not show the "Company Target" percentages in the context while the model is aggregating the "Proposed Ratings." Only reveal or compare them *after* the raw data is tabled. This prevents the model from "cooking the books" to match the target.
