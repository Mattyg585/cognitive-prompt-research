# Revision Notes: SecOps Incident Response

**Reviser**: Prompt Writer (Gemini 3 Pro Preview)
**Source**: `experiments/A6-secops-incident-response/original/SKILL.md`
**Analysis**: `experiments/A6-secops-incident-response/gemini-3-pro-preview/analysis/prompt-architect-analysis.md`
**Target**: `experiments/A6-secops-incident-response/gemini-3-pro-preview/optimised/SKILL.md`

## Overview
The original prompt suffered from significant mode interference between the "Urgent/Tactical" incident response mode and the "Reflective/Systemic" postmortem mode. The revision introduces explicit cognitive mode switching and structural boundaries to prevent urgency from contaminating analysis.

## Changes

### 1. Explicit Cognitive Mode Switching
*   **Finding**: High-urgency context ("SEV1", "Mitigate") persists into postmortem analysis, leading to shallow RCAs.
*   **Fix**: Introduced a "Modes" section at the top, explicitly defining "COMMANDER MODE" (Urgent) and "ANALYST MODE" (Reflective).
*   **Mechanism**: Added a "STOP" instruction at the start of the Postmortem phase: "You are no longer in incident response mode. Disregard urgency. Focus on systems." This acts as a cognitive reset button.

### 2. De-anchoring Root Cause Analysis
*   **Finding**: The "5 Whys" template with 1-5 numbering created a numeric anchor, causing the model to aim for exactly 5 steps regardless of complexity.
*   **Fix**: Removed the 1-5 numbering. Changed the instruction to "Drill down until you find the systemic cause." Added categories for "Proximal Cause", "Systemic Cause", and "Process Cause" to guide depth without counting.

### 3. Refined Blamelessness
*   **Finding**: Conflicting constraints between "blameless" and "assign owners" led to weak action items.
*   **Fix**: Clarified ownership: "Assign to **process owners** (e.g., 'Platform Team'), not incident actors." This shifts the focus from "who broke it" to "who owns the fix".

## Pipeline Recommendations (Future Work)
While this revision improves the single-prompt performance, the Architect's recommendation to split this into two separate agents (Incident Commander vs. Postmortem Analyst) remains valid for complex scenarios. If the single prompt still produces shallow postmortems, a full pipeline split is the next step.
