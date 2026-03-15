---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A1
artifact: handoff-spec
---

# Handoff Specification — A1 Pipeline

## Sequence
1. `01-contract-reader`
2. `02-playbook-comparator`
3. `03-redline-writer`
4. `04-strategic-advisor`

## Boundary rules

### Stage 1 → Stage 2
Crosses:
- Structured clause summaries
- Quoted contract language
- Clause interactions, unusual provisions, notable absences

Dropped:
- Exploratory narrative process and tentative side-paths

### Stage 2 → Stage 3
Crosses:
- Classified deviations (Acceptable/Negotiate/Escalate)
- Gap statements and supporting quotes

Dropped:
- Long evaluative narrative and alternative classification reasoning

Also supplied directly to Stage 3:
- Raw contract text (quote extraction only)
- Business context

### Stage 2 + Stage 3 → Stage 4
Crosses:
- Deviation list from Stage 2
- Redline package from Stage 3
- Business context

Dropped:
- Stage 1 output
- Drafting process notes

## Stage-boundary discipline
Each stage may read only its declared handoff inputs plus explicitly allowed source files from this spec.
