# Revision Notes: Debug Skill Optimisation

**Architect Analysis:** xperiments/A5-engineering-debug/gemini-3-pro-preview/analysis/prompt-architect-analysis.md
**Original:** xperiments/A5-engineering-debug/original/SKILL.md

## Key Changes

1.  **Removed Immediate Output Template:** The original prompt forced the model to output a ## Debug Report in the first turn. This caused "temporal collapse," where the model hallucinated investigation steps to justify a premature fix.
2.  **Implemented Process-Oriented Structure:** The prompt now explicitly instructs the model to follow a phased approach (Triage -> Isolation -> Confirmation -> Resolution).
3.  **Added Cognitive Lenses:**
    *   *Skeptic Lens:* To prevent blindly trusting error messages.
    *   *Temporal Lens:* To focus on recent changes.
    *   *Boundary Lens:* To distinguish internal vs. external errors.
4.  **Conditional Output:** The final report template is now "gated." The instructions explicitly state: "**ONLY** when you have confirmed the root cause... output the final report."
5.  **Interaction Guidelines:** Added explicit instruction to "Drive the investigation" and "Ask targeted questions," shifting the mode from "Reporting" to "Inquiry."

## Expected Impact

*   **Reduced Hallucination:** The model won't invent reproduction steps because it's allowed to ask for them.
*   **Deeper Diagnosis:** By enforcing the "Skeptic Lens" and "Root Cause Confirmation," we expect fewer "Band-Aid" fixes and more systemic solutions.
*   **Better User Experience:** The model will act like a partner (asking questions) rather than a search engine (spitting out a generic answer).
