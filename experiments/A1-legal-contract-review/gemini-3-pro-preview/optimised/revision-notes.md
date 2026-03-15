# Rationale for Revision: Legal Contract Review

## Overview

This revision addresses cognitive mode interference identified in the original prompt analysis. The core issue was the mixing of **Convergent Analysis** (Audit/Risk Assessment) with **Divergent Generation** (Drafting Redlines), leading to potential hallucinations and diluted reasoning.

## Key Changes

### 1. Separation of Concerns (Cognitive Phasing)
*   **Original**: Asked for analysis, risk assessment, and drafting simultaneously in a single pass.
*   **Revision**: Split into strict phases:
    *   **Phase 1 (Diagnosis)**: Pure analysis. Identify the gap. No drafting allowed. This preserves the "Auditor" stance.
    *   **Phase 2 (Treatment)**: Pure generation. Draft the fix based *only* on the diagnosis. This activates the "Drafter" stance without contaminating the audit.

### 2. Removal of "Phantom Tool" Instructions
*   **Original**: Instructed the model to "Look for... `legal.local.md`", causing it to hallucinate a file system search or invent policies.
*   **Revision**: Explicit instruction to use "Context Provided" or fallback to "Standard Commercial Defaults". This grounds the model in the available context.

### 3. Enforced Output Structure
*   **Original**: Loose instructions on format ("Classify... generate redlines").
*   **Revision**: Markdown table for Phase 1 (Diagnosis) and structured blocks for Phase 2 (Redlines). This visual separation reinforces the cognitive separation.

### 4. Strategic Prioritization
*   **Original**: Asked for "holistic" review alongside "clause-by-clause".
*   **Revision**: Moved "Strategy" to Phase 2, ensuring it is a *result* of the clause-by-clause analysis, not a competing parallel process.

## Expected Improvements
*   **Reduced Hallucination**: No more inventing file paths or policies.
*   **Higher Quality Redlines**: Drafting happens after the risk is fully understood, leading to more targeted edits.
*   **Clearer Audit Trail**: The user can see the "Diagnosis" separate from the "Fix", making it easier to verify the model's reasoning.
