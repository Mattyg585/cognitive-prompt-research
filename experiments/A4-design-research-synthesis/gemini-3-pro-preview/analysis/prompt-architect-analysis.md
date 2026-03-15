# Prompt Architect Analysis: Research Synthesis

## 1. Cognitive Mode Analysis

### Required Thinking Types
This prompt requires a complex chain of cognitive modes:
1.  **Divergent Extraction**: Reading raw inputs (transcripts, notes) to find significant data points.
2.  **Pattern Recognition**: Clustering these points into "Key Themes" and "User Segments".
3.  **Evaluative Judgment**: Assessing "Impact", "Effort", and "Priority" for recommendations.
4.  **Convergent Synthesis**: Summarizing findings into an "Executive Summary".
5.  **Formatting/Reporting**: Adhering to a strict Markdown structure.

### The Conflict: Simultaneous Divergence and Convergence
The prompt asks the model to perform all these distinct cognitive tasks in a single pass.
*   It must **explore** the data to find themes.
*   It must **judge** the themes to prioritize recommendations.
*   It must **synthesize** the whole into a summary.

Crucially, because LLMs generate linearly, the prompt structure forces **premature synthesis**.

## 2. Mode Interference & Mechanisms

### A. The "Executive Summary" Trap (Synthesis before Analysis)
*   **Quote**: The output template places `### Executive Summary` at the very top, before `### Key Themes` or `### Recommendations`.
*   **Mechanism**: The model is forced to write the summary of its findings *before* it has generated the findings. It essentially has to guess the narrative before it has done the analysis. This causes the subsequent analysis to be "confirmation bias" generation to support the premature summary, rather than the summary emerging from the analysis.

### B. Investigating while Judging (The Recommendation Filter)
*   **Quote**: `### Recommendations` with `1. **[High priority]**` and `### Insights → Opportunities` table with `Impact | Effort`.
*   **Mechanism**: The explicit requirement to produce prioritized, high-impact recommendations acts as a filter on the investigation. The model is incentivized to find themes that lead to easy recommendations, potentially ignoring complex, messy, or subtle insights that don't fit the "Problem -> Fix" template but are actually more valuable for research.

### C. Numeric Anchoring
*   **Quote**:
    ```markdown
    #### Theme 1: [Name]
    ...
    #### Theme 2: [Name]
    ...
    ### Recommendations
    1. **[High priority]**
    2. **[Medium priority]**
    3. **[Lower priority]**
    ```
*   **Mechanism**: The template explicitly numbers "Theme 1" and "Theme 2" and lists exactly three priority levels. This anchors the model to produce ~2-3 themes and exactly 3 recommendations, regardless of whether the data supports 1 theme or 10. Natural variation is suppressed.

### D. Schema as Cognitive Constraint
*   **Quote**: The rigid "fill-in-the-blanks" template.
*   **Mechanism**: The model switches into "form-filling" mode. Instead of thinking "What is true about this user?", it thinks "What fits in the 'Characteristics' column?". This creates shallow, plausible-sounding content that fits the box but lacks depth.

## 3. Diagnostic Signals (What to Look For)

*   **The "3-Bullet" Effect**: Does every output have exactly 3 recommendations? (High/Med/Low)?
*   **Vague Summaries**: Is the Executive Summary generic ("Users faced challenges but found value...") rather than specific?
*   **Theme Uniformity**: Are there always 2-4 themes, never 1 or 8?
*   **Forced Quantification**: Do "User Segments" have arbitrary "Rough %" numbers that don't seem derived from actual counting?
*   **Justification Alignment**: Do the themes feel chosen specifically to justify the pre-determined recommendation slots?

## 4. Recommendations for Prompt Writer

### Phase 1: Break the Linear Dependency (Prompt-Level)
*   **Reorder the Output**: Ask the model to generate the **Themes and Evidence FIRST**, then the Recommendations, and the **Executive Summary LAST**. Even if the user wants the summary at the top, the model *must* generate it last to make it accurate. (Or use a scratchpad approach).
*   **Remove Numeric Anchors**: Change the template to use loose lists or "Themes (as many as identified)" rather than "Theme 1, Theme 2".
*   **Soften the Schema**: explicit instruction: "The structure below is a guide. Add or remove sections as the data dictates. Do not force data into these boxes if it doesn't fit."

### Phase 2: Pipeline Architecture (System-Level)
For high-quality research synthesis, a single prompt is insufficient. A pipeline approach is superior:

1.  **Agent 1 (divergent):** "Read these transcripts. List every distinct pain point, quote, and observation. Do not group them yet. Just extract."
2.  **Agent 2 (clustering):** "Read these observations. Group them into affinity clusters. What are the emerging themes? Name them."
3.  **Agent 3 (evaluative):** "Review these themes. Which have the highest impact on product goals? Draft recommendations."
4.  **Agent 4 (convergent):** "Write the Executive Summary and format the final report."

**Trade-off**: The pipeline is slower and more expensive but avoids the "Summary before Analysis" cognitive trap. For a "Quick Synthesis" tool, the Prompt-Level fixes (Reorder Output) are the best balance.
