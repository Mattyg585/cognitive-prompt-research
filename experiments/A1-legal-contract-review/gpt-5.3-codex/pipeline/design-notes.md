---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A1
artifact: design-notes
---

# Design Notes — A1 Tier-3 Pipeline

## Why this split
The original monolithic prompt mixes investigation, evaluation, drafting, and strategy in one context. The pipeline isolates these modes to reduce cross-mode interference.

## Expected gains
- Better risk-identification breadth in Stage 1
- Cleaner risk classification in Stage 2
- Less boilerplate drafting in Stage 3
- More strategic (less repetitive) negotiation guidance in Stage 4

## Complexity trade-off
The pipeline introduces orchestration overhead and longer end-to-end runtime. It is justified for repeat contract-review workflows where quality delta matters.

## Quality checks
1. Stage 1 should include unusual/out-of-category findings.
2. Stage 2 should preserve those findings in an explicit section.
3. Stage 3 language should be specific and commercially calibrated.
4. Stage 4 should model counterparty behavior and sequencing, not just summarize tiers.
