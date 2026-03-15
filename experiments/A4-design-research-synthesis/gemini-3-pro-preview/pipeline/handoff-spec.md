# Pipeline Handoff Specification

## Overview
This pipeline separates the extraction of evidence (citation) from the synthesis of patterns (meaning). This prevents the "hallucinated quote" problem where models invent evidence to support a narrative, and the "missed insight" problem where the cognitive load of citation tracking crowds out pattern recognition.

## 1. Miner → Architect

**Goal**: Pass verifiable data points without the noise of full transcripts.

*   **What crosses**: A structured list of *atomic findings* (Needs, Pain Points, Goals, Workarounds). Each finding MUST have:
    *   Direct Quote (verbatim)
    *   Participant ID
    *   Context (1 sentence)
*   **Format**: Structured Markdown List.
    *   `* [P1] "Quote": Context/Observation`
*   **What gets dropped**:
    *   Full conversational filler.
    *   Interviewer questions (unless necessary for context).
    *   Irrelevant tangents.
*   **Why**: The Architect needs *content* to group, not *conversation* to read. By filtering to findings first, we reduce context load and ensure every theme is built on a real quote.

## 2. Architect → Planner

**Goal**: Pass synthesized meaning and structure, dropping the "messy middle" of analysis.

*   **What crosses**:
    *   **Defined Themes**: Name, Description, Prevalence (count of findings).
    *   **Supporting Evidence**: The *best* quotes selected from the Miner's output for each theme.
    *   **User Segments**: Clusters of needs/behaviors identified from the findings.
*   **Format**: Hierarchical Markdown (Themes > Evidence).
*   **What gets dropped**:
    *   Isolated findings that didn't fit a pattern (outliers are noted separately if critical, otherwise dropped for clarity).
    *   The "working out" of how groups were formed.
*   **Why**: The Planner needs a *model* of the user to strategize against, not a bag of quotes. It trusts the Architect's synthesis.

## 3. Planner → Output

**Goal**: Strategic direction and executive communication.

*   **What is produced**:
    *   **Executive Summary**: High-level narrative.
    *   **Strategic Recommendations**: Prioritized actions based on the Themes/Segments.
    *   **Opportunities**: "How Might We" questions or feature ideas.
*   **Format**: Professional Report.
