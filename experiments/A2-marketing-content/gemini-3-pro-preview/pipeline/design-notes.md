# Pipeline Design: Marketing Content Generation

**Based on Analysis:** `experiments/A2-marketing-content/gemini-3-pro-preview/analysis/prompt-architect-analysis.md`
**Target:** High-quality marketing content that prioritizes strategy and persuasion over rigid formatting.

## Problem Diagnosis
The original prompt suffered from **Mode Interference** between:
1.  **Strategic Reasoning** (missing): Who is this for? Why do they care?
2.  **Storytelling** (suppressed): Narrative flow and persuasion.
3.  **Constraint Satisfaction** (dominant): Character counts, H2/H3 structure, SEO keywords.

The "Checklist" mode (3) was killing the "Storytelling" mode (2), resulting in generic, structure-heavy but insight-light content.

## Pipeline Architecture: The "Strategist-Writer-Editor" Chain

We separate the incompatible thinking types into three distinct agents:

### 1. The Strategist (Agent A)
*   **Function:** Strategic Reasoning & Synthesis.
*   **Cognitive Mode:** Divergent exploration of angles -> Convergent selection of the best approach.
*   **Goal:** Define the *soul* of the piece before a single word of copy is written.
*   **Why Separate:** Needs to ignore word counts and formatting to focus purely on the audience and the argument.

### 2. The Writer (Agent B)
*   **Function:** Generation & Storytelling.
*   **Cognitive Mode:** Divergent flow state.
*   **Goal:** Write compelling, persuasive prose that flows naturally.
*   **Why Separate:** "Writing for flow" and "Writing for SEO/Length" are opposing modes. If the writer worries about "60 characters", they stop worrying about "is this interesting?".

### 3. The Editor (Agent C)
*   **Function:** Evaluation & Constraint Satisfaction.
*   **Cognitive Mode:** Convergent auditing.
*   **Goal:** Polish the draft, apply formatting rules, ensure SEO compliance, and cut fluff.
*   **Why Separate:** This is where the rigid constraints belong. Applying them *after* the draft exists preserves the core idea while ensuring the final output is usable.

## Execution Strategy
**Sequential Execution:** The output of each stage is the necessary input for the next.
1.  User Input -> **Strategist** -> Creative Brief
2.  Creative Brief -> **Writer** -> First Draft
3.  First Draft + Original Constraints -> **Editor** -> Final Asset
