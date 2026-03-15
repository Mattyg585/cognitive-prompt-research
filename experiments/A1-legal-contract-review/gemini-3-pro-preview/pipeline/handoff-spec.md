# Pipeline Handoff Specification

## Overview
This defines the structure passed from **Agent 1 (Auditor)** to **Agent 2 (Senior Counsel)**. The format is **JSON** to strip cognitive mode and enforce structured thinking.

## Agent 1 -> Agent 2

### Information Passed
*   **Identified Risks**: A list of clauses that deviate from the standard.
*   **Severity**: Green/Yellow/Red classification.
*   **Original Text**: The problematic clause text (verbatim).
*   **Explanation**: Why it deviates (the "Audit" finding).

### Format
Strict JSON array of objects.

```json
[
  {
    "clause_type": "Indemnity",
    "risk_level": "RED",
    "deviation_description": "Clause is uncapped and broad. Playbook requires cap at 12 months fees.",
    "current_text": "The Supplier shall indemnify the Customer against any and all claims...",
    "standard_reference": "Playbook Section 4.2: Indemnity must be mutual and capped."
  },
  {
    "clause_type": "Limitation of Liability",
    "risk_level": "YELLOW",
    "deviation_description": "Cap is 24 months, Playbook prefers 12 months but allows up to 36 for strategic deals.",
    "current_text": "Liability shall not exceed 24 months of fees paid.",
    "standard_reference": "Playbook Section 5.1: Cap at 12 months fees."
  }
]
```

### What gets Dropped
*   **The Full Contract**: Agent 2 only sees the relevant snippets unless context requires the whole document (which risks distraction). We assume Agent 1 has extracted the necessary context.
*   **Exploratory Threads**: Any "maybe this is okay because..." reasoning from Agent 1 is stripped. Agent 1 makes a definitive judgment (Red/Yellow/Green). Agent 2 can soften it later, but the input is a hard fact.
*   **Formatting/Style**: No prose or conversational elements. Just the data.
