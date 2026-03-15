# Pipeline Design: Legal Contract Review (Tier 3)

## Overview
This pipeline separates the analytical task of **Audit** (identifying deviations from a standard) from the generative task of **Redline Drafting** (proposing specific text fixes). This split resolves the primary cognitive conflict identified in the architect analysis: the "Analytical vs. Generative Bleed," where asking for fixes during diagnosis dilutes the quality of both.

## Agents

### 1. Contract Auditor (Analytical/Convergent)
*   **Role**: Dispassionate evaluator. Reads the contract and compares it strictly against the provided Playbook (or defaults).
*   **Thinking Types**:
    *   **Structuring**: Categorizing clauses (e.g., "This is an Indemnity clause").
    *   **Evaluation**: Judging current text against the standard (Green/Yellow/Red).
*   **Why Separate**: Prevents the "Drafting" mode from corrupting the "Auditing" mode. An auditor must be precise and rule-bound; blending this with creative drafting leads to hallucinated standards or weak enforcement.
*   **Input**: Full Contract Text + Playbook Rules.
*   **Output**: Structured list of deviations (JSON).

### 2. Senior Counsel (Generative/Divergent)
*   **Role**: Strategic negotiator. Takes the identified risks and drafts the specific redlines and negotiation strategy.
*   **Thinking Types**:
    *   **Generation**: Drafting specific legal text to close the gap.
    *   **Synthesis**: Prioritizing issues for negotiation (the "Holistic" view).
*   **Why Separate**: This layer requires "Deal Making" logic (balance, strategy) which conflicts with the "Strict Auditor" logic of Agent 1. By isolating it, we allow Agent 2 to be strategic without compromising the initial fact-finding.
*   **Input**: JSON List of Deviations from Agent 1.
*   **Output**: Redlines, explanatory comments, and a negotiation summary.

## Execution Flow
1.  **Ingest**: User provides contract text.
2.  **Audit**: Agent 1 scans the text against the Playbook rules. It produces a rigid JSON list of findings.
3.  **Handoff**: The JSON structure strips the "reasoning" trace, passing only the *facts* (Clause X is Red because Y).
4.  **Draft**: Agent 2 reads the findings and generates the redlines and strategy note.

## Key Design Decisions
*   **JSON Handoff**: We use JSON to enforce a "cognitive firewall." Agent 2 should not see Agent 1's "thinking process," only its *conclusions*. This prevents Agent 2 from re-litigating the findings.
*   **Explicit Playbook Injection**: We assume the Playbook is provided in the context or system prompt of Agent 1, resolving the "Phantom Tool" issue where the model tries to "look for" a file.
*   **Separation of Concerns**: Agent 1 is the "Bad Cop" (strict rules). Agent 2 is the "Good Cop" (constructive solutions).
