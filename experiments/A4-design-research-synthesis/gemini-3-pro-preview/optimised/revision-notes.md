# Revision Notes: Research Synthesis

**Optimised by:** Prompt Writer
**Based on Analysis by:** Prompt Architect (Gemini 3 Pro Preview)

## 1. Key Changes & Rationale

### Reordered Cognitive Process
*   **Original**: Asked for Executive Summary first, forcing premature synthesis (guessing the narrative before analyzing).
*   **Revision**: Explicitly moved Executive Summary to the **end** of the output.
*   **Why**: This enforces a "Compress (Analysis) → Reason (Recommendations) → Compress (Summary)" flow. The model can now write a summary that accurately reflects the themes it just generated, rather than hallucinating themes to fit a premature summary.

### Removed Numeric Anchors
*   **Original**: Template listed "Theme 1, Theme 2" and exactly 3 numbered recommendations.
*   **Revision**: Uses open-ended instructions: "*Identify as many distinct themes as the data supports... If there are 2, list 2. If there are 7, list 7.*"
*   **Why**: Prevents the "3-Bullet Effect" where the model ignores data or hallucinates fillers to hit an arbitrary target number.

### Separated Investigation from Judgment
*   **Original**: Combined insight generation with "Impact/Effort" scoring in the same visual scan.
*   **Revision**: Added "How to Think" instructions that explicitly separate the **Extraction** phase (finding what's there) from the **Evaluation** phase (judging its worth).
*   **Why**: Prevents high-impact filtering from blinding the model to subtle but important user friction points during the discovery phase.

### Softened Schema Constraints
*   **Original**: Rigid fill-in-the-blanks template.
*   **Revision**: Added instruction: "*Remove sections that aren't supported by the data.*" (e.g., for User Segments).
*   **Why**: Reduces hallucination where models invent "segments" just to fill a table row.

## 2. What to Watch For (Testing)

*   **Summary Quality**: Check if the Executive Summary at the end is more specific and evidence-backed than the original version.
*   **Theme Count**: Verify that the number of themes varies with the input size (natural variation).
*   **Recommendation Logic**: Ensure recommendations clearly link back to the identified themes (provenance).
