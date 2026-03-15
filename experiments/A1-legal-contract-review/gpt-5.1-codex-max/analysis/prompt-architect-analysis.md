---
model: GPT-5.1-Codex-Max
date: 2026-03-15
experiment: A1
tier: analysis
---

# Prompt Architect Analysis — `experiments/A1-legal-contract-review/original/SKILL.md`

## What the prompt is asking for (thinking types & relationships)
- **Investigation → Evaluation → Generation → Strategy** in one pass: ingest contract (“Read the entire contract” — lines 67-69), map to playbook criteria (evaluation vs standard positions), classify deviations (GREEN/YELLOW/RED — lines 196-239), then **generate** redlines (lines 242-271) and **synthesize/reframe** into business impact and negotiation strategy (lines 273-307, 321-352). These modes are sequentially listed but share the same context, so they can run concurrently.
- **Structuring/Classification** via seeded clause taxonomy (table lines 73-87) plus colored severity labels. This is convergent scaffolding.
- **Orchestration + Intake** (Step 2 context gathering, Step 3 playbook loading) coexists with the downstream evaluative/generative work; no clean boundary between the orchestrator posture and the execution posture.
- **Reframing** is embedded: business impact and counterparty-suitable rationales (lines 244-249, 273-280) translate findings for stakeholders.

## Where modes interfere (evidence & mechanism)
1) **Investigation pre-filtered by evaluation criteria and taxonomy**
   - Seeds: fixed clause list (lines 73-87) and triage colors (lines 196-241). Mechanism: evaluation + structuring ride in context before and during investigation → investigation becomes a search for known categories and colorable deviations. Expect missed non-standard or cross-cutting issues (e.g., unusual audit rights, exclusivity quirks).
2) **Investigation entangled with generation**
   - Redlines are requested alongside clause analysis (lines 244-249, 263-271). Mechanism: investigation + generation → solution-shaped investigation; model favors issues with obvious fixes, drops ambiguous risks.
3) **Evaluation + generation + strategy in one context**
   - After classifying, it immediately must produce negotiation strategy and business impact (lines 273-307, 321-352). Mechanism: synthesis/strategy posture may back-propagate, pushing early commitment and confirmation bias; findings molded to fit a negotiation narrative.
4) **Orchestration mixed with execution**
   - Gathering user context (lines 36-44) and playbook discovery/branching (lines 45-59) sit in same context as downstream work. Mechanism: orchestration tone (questions, gating) coexists with evaluative/generative tone, adding extraneous load and diluting a decisive review posture.
5) **Output-format anchors**
   - Fixed sections and explicit “Top 3 issues” (lines 273-280, 321-352) plus per-clause template (lines 263-271). Mechanism: implicit numeric/slot anchors → uniform issue counts and template-filling behavior, regardless of contract complexity.

## Output diagnostics / predictions
- **Uniform coverage of seeded clauses** even when irrelevant; sparse attention to unlisted clauses or cross-clause interactions.
- **Stable issue counts and severity distributions** across simple/complex contracts (anchor effect from colors and “Top 3”).
- **Redlines skew to “fixable” items**; subtle or systemic risks (e.g., interlocking indemnity + insurance gaps) under-represented.
- **Negotiation strategy mirrors severity colors** rather than bespoke leverage; may feel templated.
- **Tone blending** (question-asking + decisive recommendations) if orchestration residue persists into findings.

## Fixes (prompt-level vs pipeline-level, with trade-offs)
### Prompt-level (lighter weight)
- **Separate instructions for phases**: add explicit scope boundaries (“investigate without judging or redlining yet; judgment/redlines come after a clean pass”) to reduce pre-filtering. Trade-off: modest gains; residual contamination remains because context stays shared.
- **Convert seeded list to lenses + optional seeds**: frame clause categories as “use these lenses; add others as needed,” and invite discovery of unlisted clauses/interactions. Trade-off: may slightly reduce checklist completeness; improves coverage of atypical risks.
- **Defer generation cues**: move redline and strategy instructions after evaluation text, with a transitional delimiter, to reduce solution-shaped investigation. Trade-off: minor complexity increase; keeps single-call simplicity.
- **Relax numeric/slot anchors**: make “Top issues” count responsive (“surface the most material issues, don’t force to three”) and allow omission of irrelevant sections. Trade-off: less uniform output; more input-responsive variation.

### Pipeline-level (heavier, clearer separation)
- **Two-pass or tri-pass architecture**: 
  1) **Investigation + structuring** agent: extract clause map and anomalies (no severity, no fixes). 
  2) **Evaluation/triage** agent: apply playbook, assign GREEN/YELLOW/RED, articulate risks. 
  3) **Generation/strategy** agent: craft redlines and negotiation plan from structured findings.
  - Trade-off: higher orchestration cost; gains in depth, coverage of non-seeded issues, and tailored negotiation guidance.
- **Compression handoffs**: pass structured findings (clause, text snippet, concern) instead of raw prose to strip exploratory tone before evaluation/generation. Trade-off: added schema design; reduces mode bleed.
- **Orchestrator isolation**: keep context-gathering and playbook selection in a pre-step that emits a compact config for downstream agents. Trade-off: extra call; cleaner execution posture.

## Ready for handoff
Analysis complete; ready for `prompt-writer` to produce revisions.
