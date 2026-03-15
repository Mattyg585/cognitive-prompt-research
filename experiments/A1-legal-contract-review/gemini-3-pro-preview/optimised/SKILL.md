---
name: review-contract
description: Review a contract against your organization's negotiation playbook. Uses a strict two-phase process: (1) Diagnosis (identifying deviations and risk) and (2) Treatment (drafting redlines and strategy).
argument-hint: "<contract file or text>"
---

# /review-contract -- Contract Review Against Playbook

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Review a contract against your organization's negotiation playbook. Analyze each clause, flag deviations, generate redline suggestions, and provide business impact analysis.

**Important**: You assist with legal workflows but do not provide legal advice. All analysis should be reviewed by qualified legal professionals before being relied upon.

## Invocation

```
/review-contract <contract file or URL>
```

Review the contract: @$1

## Workflow

This review process has two strictly separated phases:
1.  **Diagnosis (Analysis & Risk Assessment)**: Read, classify, and compare. NO drafting.
2.  **Treatment (Redlining & Strategy)**: Draft language and strategy based *only* on the diagnosis.

### Step 1: Context & Playbook Loading

First, determine the context and the standard to apply.

1.  **Extract Context**:
    *   **User's Side**: Vendor/Supplier, Customer/Buyer, Licensor, Licensee, etc.
    *   **Deal Parameters**: Deadline, deal size, strategic importance (ask if not provided).
    *   **Document Type**: SaaS Agreement, MSA, NDA, DPA, etc.

2.  **Load the Standard**:
    *   **Priority**: Use the organization's Playbook if provided in the current context/conversation.
    *   **Fallback**: If NO playbook is provided, explicitly state: "No specific playbook found. Using Standard Commercial positions for [User's Side] in [Document Type]."
    *   **Standard Commercial Defaults** (use these if no playbook exists):
        *   *Limitation of Liability*: Mutual, capped at 12 months' fees. Super-cap for data breach/IP (2-3x).
        *   *Indemnification*: Mutual for IP infringement (Vendor) and material breach (Both).
        *   *Governing Law*: Defendant's venue or neutral major commercial hub (e.g., NY, DE, London).
        *   *Term*: Annual auto-renewal with 60-day notice for non-renewal.

### Step 2: Phase 1 - Diagnosis (Strict Audit)

**Mode: Analytical / Convergent**
*Goal: Identify gaps. Do not fix them yet.*

Read the contract clause-by-clause. For each material clause:
1.  **Classify**: Identify the legal concept (e.g., "Indemnity", "Warranties").
2.  **Compare**: Measure the specific text against the Playbook (or Standard Defaults).
3.  **Assess Risk**: Assign a status based on the gap.

**Risk Classifications:**
*   **GREEN (Acceptable)**: Aligns with or beats the standard.
*   **YELLOW (Negotiate)**: Deviates from standard but is market-reasonable. Needs editing.
*   **RED (Escalate)**: Material risk, uncapped liability, missing critical protections, or strictly prohibited terms.

**Critical Instruction:** Do not draft redlines or "fix" the text in this step. Output *only* the analysis of the gap.

### Step 3: Phase 2 - Treatment (Drafting & Strategy)

**Mode: Generative / Divergent**
*Goal: Fix the identified gaps.*

Only AFTER the diagnosis is complete, process the **YELLOW** and **RED** items:

1.  **Draft Redlines**:
    *   Create specific, insertable text to close the gap identified in Phase 1.
    *   Be precise: "Replace Section 5.1 with..."
    *   Include a **Rationale** for the counterparty (neutral, professional).
    *   Include a **Fallback Position** for negotiation.

2.  **Formulate Strategy**:
    *   Group issues into **Tier 1 (Deal Breakers)**, **Tier 2 (Important)**, and **Tier 3 (Nice-to-Have)**.
    *   Define the trade-offs (e.g., "Concede on Venue to win on Liability Cap").

## Output Format

Structure your response exactly as follows to maintain cognitive separation:

```markdown
# Contract Review: [Document Name]

**Context**: [Role] | [Deal Type] | [Standard Used: Playbook/Generic]

## Phase 1: Diagnosis & Risk Assessment

| Clause | Status | Gap Analysis (Current vs Standard) | Business Impact |
| :--- | :--- | :--- | :--- |
| **Limitation of Liability** | 🔴 RED | Current: Uncapped. Standard: 12mo fees. | Extreme financial exposure. |
| **Indemnity** | 🟡 YELLOW | Current: Unilateral. Standard: Mutual. | Unbalanced risk transfer. |
| **Governing Law** | 🟢 GREEN | Current: Delaware. Standard: Delaware. | None. |
| ... | ... | ... | ... |

*(Note: Only list material clauses. Do not draft text here.)*

## Phase 2: Recommended Redlines & Strategy

### High Priority Issues (Red/Yellow)

**1. Limitation of Liability**
*   **Current Text**: "[Quote relevant snippet]"
*   **Redline**: "[Specific replacement text]"
*   **Rationale (External)**: "Market standard cap aligns with deal value."
*   **Fallback**: 24 months' fees.

**2. Indemnity**
*   ...

### Negotiation Strategy
*   **Must-Haves**: [List Tier 1 issues]
*   **Trade-Offs**: [List Tier 2/3 items to concede]
*   **Next Steps**: [Specific actions]
```

## Notes
- If the contract is scanned/image-based, ask for a text version.
- If the user provides new facts during the conversation, re-run Phase 1 (Diagnosis) on affected clauses before generating new Phase 2 (Redlines).
