---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A1
tier: pipeline
run: 0
---

# Tier 3 Pipeline Design — A1 Legal Contract Review

## Pipeline overview
Separate clause discovery from evaluation and from drafting so that evaluation criteria and redline language do not pre‑filter what gets surfaced.

## Agent map

| Agent | Thinking modes | Receives | Produces | Why separate |
|---|---|---|---|---|
| **clause-mapper** | Investigation + light structuring | Contract text + deal context | Descriptive clause map + nonstandard items | Protects discovery from evaluation/generation bias |
| **playbook-evaluator** | Evaluation + structuring | Clause map + playbook positions | Deviations list with GREEN/YELLOW/RED classifications | Keeps classification clean and criteria-driven |
| **redline-strategist** | Generation + synthesis | Deviations list + clause excerpts | Redlines, fallback positions, and negotiation strategy | Prevents drafting/strategy from shaping discovery or classification |

## Execution order
1. **clause-mapper** → 2. **playbook-evaluator** → 3. **redline-strategist**

Sequential execution is required because each stage depends on the previous stage’s structured output.

## Handoff design (summary)
- **Clause map → Evaluator**: structured clause entries only; no ratings or recommendations.
- **Evaluator → Redline strategist**: deviations table with classification, impact, and target positions; no exploratory notes.

Detailed formats are in `handoff-spec.md`.

## Execution method
**Sequential** because each stage requires the prior stage’s full output.

For very long contracts, the **clause-mapper** can run in parallel on sections, then merge into a single clause map before evaluation.

## Context window notes
- **Compression is essential**: pass concise clause summaries and short excerpts, not full clause text.
- **Long contracts**: chunk the contract for mapping, then merge and deduplicate before evaluation.
- **Avoid mode bleed**: do not include evaluative language in the clause map or drafting language in the deviations list.

## Files produced
- `clause-mapper.md` + `clause-mapper.agent.md`
- `playbook-evaluator.md` + `playbook-evaluator.agent.md`
- `redline-strategist.md` + `redline-strategist.agent.md`
- `handoff-spec.md`
