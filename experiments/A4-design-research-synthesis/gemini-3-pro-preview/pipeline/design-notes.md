# Pipeline Design Notes: Research Synthesis

## Problem: Cognitive Interference
The original single-prompt approach suffers from interference between **Broad Synthesis** (finding patterns across many inputs) and **Specific Citation** (finding exact evidence).

*   **Synthesis**: Requires high-level abstraction ("What does this mean?").
*   **Citation**: Requires low-level verification ("Where is the proof?").

When combined, the model tends to either:
1.  **Hallucinate Evidence**: Invent quotes to fit a compelling narrative (Synthesis > Verification).
2.  **Miss Themes**: Fail to identify subtle patterns because cognitive load is spent on quote hunting (Verification > Synthesis).
3.  **Generic Output**: Default to safe, obvious themes ("Users want ease of use") to avoid the risk of specific, unverifiable claims.

## Solution: The "Miner-Architect-Planner" Pipeline

This pipeline separates the concerns into distinct cognitive modes.

### Agent 1: The Research Miner (Extraction)
*   **Cognitive Mode**: Concrete, Detail-Oriented, Investigative.
*   **Task**: Read transcripts. Extract *atomic findings* (Need, Pain, Goal, Workaround) with *direct quotes*.
*   **Why Separate?**: It frees the model from the burden of *interpreting* meaning. It just needs to find signal in the noise. It ensures every downstream theme is built on a real, verifiable data point.

### Agent 2: The Research Architect (Synthesis)
*   **Cognitive Mode**: Abstract, Integrative, Structuring.
*   **Task**: Review the *findings* (not transcripts). Cluster them into *Themes* and *User Segments*.
*   **Why Separate?**: It works with pre-verified data. It can focus purely on relationships and patterns without getting lost in conversation flow. It cannot hallucinate quotes because it only sees the Miner's output.

### Agent 3: The Research Planner (Strategy)
*   **Cognitive Mode**: Evaluative, Strategic, Generative.
*   **Task**: Turn Themes/Segments into *Opportunities* and *Recommendations*.
*   **Why Separate?**: Strategy requires a shift from "What is?" to "What should be?". Separating this ensures we don't mix observation with prescription too early. It forces the model to base strategy on the synthesized model, not raw anecdotes.

## Execution Strategy
*   **Sequential**: The output of each stage is the input for the next.
*   **Volume Note**: For large studies (e.g., >10 transcripts), run multiple Miners in parallel on subsets, then feed all findings to one Architect. This design supports that scalability.
