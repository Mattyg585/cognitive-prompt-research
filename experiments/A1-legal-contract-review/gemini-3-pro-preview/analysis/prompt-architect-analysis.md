# Prompt Architect Analysis: Legal Contract Review

## 1. Thinking Process Analysis

The prompt requires a complex chain of cognitive operations:
1.  **Context Extraction**: Parsing the user's role, deal parameters, and document type.
2.  **Clause Classification**: Identifying text segments as specific legal concepts (e.g., "Indemnity", "Limitation of Liability").
3.  **Rule Application (Comparator)**: Comparing extracted clauses against a reference standard (Playbook).
4.  **Risk Assessment**: Evaluating the gap between *Current* and *Standard* (Green/Yellow/Red).
5.  **Creative Generation**: Drafting specific legal text (Redlines) to close that gap.
6.  **Strategic Synthesis**: Prioritizing issues for negotiation.

These are distinct cognitive modes. Steps 1-3 are **Convergent/Analytical** (matching facts to rules). Steps 5-6 are **Divergent/Generative** (creating new text/strategies).

## 2. Mode Interference & Stance Drift

### A. The "Phantom Tool" Conflict
**Quote:** "Look for the organization's contract review playbook in local settings (e.g., `legal.local.md`...)"
**Mechanism:** The prompt instructs the model to perform a file system operation it likely cannot do (depending on the environment). Even if it has tools, asking a *chat model* to "look for" configuration inside its system prompt logic confuses "Context Loading" with "Reasoning".
**Result:** The model will likely hallucinate that it *has* found a playbook, or immediately default to generic standards without explicitly stating it, blurring the line between "Client Policy" and "General Knowledge".

### B. Analytical vs. Generative Bleed (Step 5 vs Step 6)
**Quote (Step 5):** "Action: Generate specific redline language."
**Quote (Step 6):** "For each YELLOW and RED deviation, provide... Suggested redline"
**Mechanism:** The prompt asks for the output (Redlines) during the analysis phase (Step 5) and then asks for it again in a dedicated generation phase (Step 6).
**Result:**
*   **Redundancy:** The model may output redlines twice (inline in analysis AND in a summary).
*   **Context Dilution:** By asking for the *fix* while still diagnosing the *problem*, the model devotes token budget to drafting before it has finished holistic risk assessment.

### C. The "Holistic" Drift
**Quote:** "Consider the contract holistically: Are the overall risk allocation and commercial terms balanced?"
**Mechanism:** This instruction (Step 4.5) contradicts the strict "Clause-by-Clause" structure (Step 4.4).
**Result:** The model may oscillate between being a "Strict Auditor" (flagging every minor deviation) and a "Deal Maker" (ignoring deviations for "balance"), leading to inconsistent flagging.

## 3. Diagnostic Signals (What to look for in output)

1.  **The "Default Standard" Hallucination:** Does the model invent specific numeric standards (e.g., "Your standard cap is 12 months") when none were provided in the prompt? This indicates the model is treating the *concept* of a playbook as a *fact*.
2.  **Structural Duplication:** Look for redlines appearing in the "Analysis" section *and* the "Summary" section, often with slight wording variations.
3.  **Vague "Business Impact":** Watch for generic fluff like "This increases risk" vs specific impact like "This exposes the company to IP theft lawsuits."
4.  **Inconsistent Severity:** Does it flag a clause as RED but then describe it as "common market practice"? This signals a conflict between the "Playbook" stance (strict) and "General Knowledge" stance (permissive).

## 4. Remediation Strategy

### Prompt-Level Fixes (Immediate)
1.  **Remove "File Search" Logic:** Change the instruction to: "Use the playbook provided in context. If no playbook is provided, use the following Default Commercial Standards: [List 3-5 defaults]." This grounds the comparison.
2.  **Decouple Analysis and Generation:**
    *   *Phase 1 (Diagnosis):* Identify clauses, Compare to Standard, Assign Color. *Do not draft text.*
    *   *Phase 2 (Treatment):* For every Yellow/Red item identified in Phase 1, generate the Redline.
3.  **Enforce Output Structure:** Use a strict XML or Markdown schema that separates "Findings" from "Actions".

### Pipeline-Level Interventions (High Value)
1.  **Context Injection Step:** Do not ask the LLM to "load" the playbook. A pre-processing step should read `legal.local.md` and insert it into the System Prompt.
2.  **Split Agent Workflow:**
    *   **Agent A (Auditor):** Reads contract + Playbook. Outputs a list of Deviations (JSON).
    *   **Agent B (Lawyer):** Reads Deviations. Drafts Redlines and Negotiation Strategy.
    *   *Why?* This prevents the "Drafting" mode from corrupting the "Auditing" mode. An auditor should be dispassionate; a drafter should be strategic.
