# Pipeline Specification: Engineering Debug

## Pipeline Overview

Debug a production issue by separating investigation from fix generation into two agents with a compressed handoff between stages.

## Why a Pipeline

The original monolithic prompt fuses two incompatible types of thinking into a single context:

1. **Investigation** — reproduce, isolate, diagnose (Steps 1-3)
2. **Generation + Evaluation** — propose a fix, assess side effects, suggest prevention (Step 4)

The core interference: the Fix section is visible in the output template from the start, so the model investigates with fix-generation in mind. Investigation becomes solution-shaped — the model follows threads that lead toward fixable causes and drops threads that lead toward systemic issues, architectural problems, or root causes that require larger interventions. The investigation becomes a funnel for the fix recommendation.

The original prompt's sequential step structure provides partial natural separation, making this a low-to-moderate severity case. But the steps are described and executed in one context with one output template. The model doesn't truly context-switch — it fills the template in order, with the full template (including Fix) visible throughout.

Prompt-level fixes (Tier 2: scope boundary, diagnosis section, reframed fix guidance) reduce fix-shaped investigation but can't eliminate it. The fix destination is still in the context during investigation. The pipeline removes it entirely.

## Agent Map

| Agent | Thinking Type | Receives | Produces | Why Separate |
|-------|--------------|----------|----------|-------------|
| **Investigator** | Investigation + Structuring | Bug report, error messages, logs, system context | Structured investigation findings: reproduction, isolation, hypotheses with evidence, root cause with confidence | Investigation without fix-generation in context allows the model to follow threads that lead to uncomfortable conclusions — architectural issues, systemic problems, process failures. Not every thread needs to terminate in a fixable cause. |
| **Fix Designer** | Generation + Evaluation | Structured investigation findings from Agent 1 | Fix proposal with rationale, side effects, edge cases, regression risks, prevention measures, tests | Generation works best when it receives fully investigated input. The fix designer doesn't need to simultaneously investigate — it receives a clear root cause and designs the appropriate intervention at the appropriate level. |

## Execution Order

```
Investigator → Fix Designer
```

Sequential — the Fix Designer depends on the Investigator's complete output.

**Rationale for two agents, not more**: The original prompt's investigation sequence (Reproduce → Isolate → Diagnose) is internally coherent — all three steps are investigation work with compatible cognitive modes (Investigation + Structuring). Splitting them into separate agents would add orchestration overhead without resolving any mode interference. Similarly, fix generation and side-effect evaluation are both convergent and compatible. Two agents is the minimum that addresses the actual interference. Not one, not three.

## Handoff Specification

### Handoff: Investigator → Fix Designer

**What crosses**: Structured investigation findings — reproduction steps, component isolation, hypotheses with evidence for and against, root cause analysis with confidence levels, scope and blast radius assessment.

**Format**: Structured sections with compressed factual content. Specific evidence quoted directly (error messages, metrics, log entries). Hypotheses presented with evidence, not as narrative exploration.

**What gets dropped**: The investigative process itself — exploratory threads that were followed and abandoned, tentative hypotheses that were discarded early, the investigator's reasoning journey. The structured findings represent the *results* of investigation, not the investigation itself. Investigative tone and open-ended framing would pull the Fix Designer back into exploration rather than letting it focus on designing the intervention.

**What the Fix Designer also receives**: Nothing beyond the structured findings. The Fix Designer does not receive the original bug report — it would reactivate investigative impulses. The investigation findings contain everything the Fix Designer needs: what the problem is, what causes it, how confident we are, and what the blast radius looks like.

## Pre-Pipeline: Input Preparation

Before running the pipeline, gather the bug report and any available context:

- Error messages, stack traces, log entries (exact text, not paraphrased)
- Expected vs. actual behaviour
- Steps to reproduce (if known)
- What changed recently (deploys, config changes, dependency updates)
- System context (architecture, services involved, infrastructure)
- What's been tried so far

All of this goes to the Investigator. The Fix Designer receives only the Investigator's structured output.

## Execution Instructions

For each run (N = 1, 2, 3):

1. **Stage 1**: Spawn a subagent with `stage-1-investigator.md` as the prompt. Input: the bug report (`test-material/bug-report.md`). Save output to `pipeline-runs/run-N/stage-1-investigator.md`.

2. **Stage 2**: Spawn a NEW subagent with `stage-2-fix-designer.md` as the prompt. Input: the structured investigation findings from Stage 1. Save output to `pipeline-runs/run-N/stage-2-fix-designer.md`.

**Each stage MUST be a separate subagent** — running stages in the same context creates the exact monolithic contamination the pipeline is designed to avoid.

## Context Window Notes

No volume concerns. Both agents receive manageable input — the Investigator gets a bug report (typically a page or two), and the Fix Designer gets compressed investigation findings (substantially smaller than the raw investigation). No compression checkpoints or external storage needed.

---

## Mapping: Architect Findings → Pipeline Design

| Architect Finding | Pipeline Response |
|---|---|
| **Investigation + Generation in shared context** — fix destination shapes investigation | Separated into Investigator (investigation only, no fix awareness) and Fix Designer (generation + evaluation, no investigative work). The fix template never enters the investigation context. |
| **Output template visible during investigation** — model fills template with fix section in view | Each agent has its own output format. The Investigator's format has no fix section. The Fix Designer's format has no investigation section. |
| **Missing investigation output** — original template jumped from Reproduction to Root Cause | The Investigator's entire output IS the investigation — hypotheses, evidence, threads followed. The diagnosis process is the primary product, not compressed into a conclusion. |
| **Fix scoped to code/config level** — original framing defaulted to proximate-cause fixes | The Fix Designer explicitly considers what level the fix should operate at: code, configuration, architecture, process, or organisational. The fix matches the root cause. |

### What to Watch for When Testing

- **Investigation depth**: Does the Investigator follow threads that don't lead to simple code fixes? If the root cause analysis only surfaces causes with clean code-level solutions, the separation may not be working (or training priors for "debugging" are anchoring toward code fixes regardless of context).
- **Hypothesis breadth**: Does the Investigator document multiple hypotheses with evidence, or present a single linear path from symptom to root cause? Multiple hypotheses with evidence for and against is the signal that investigation is genuinely open.
- **Root cause level**: Does the root cause analysis identify systemic factors (shared resource contention, missing circuit breakers, absent capacity planning) or only the proximate trigger? The Investigator has no fix to aim at — it should go as deep as the evidence supports.
- **Fix-root cause match**: Does the Fix Designer's intervention match the level of the root cause? If the Investigator identifies a systemic issue and the Fix Designer proposes only a code patch, the handoff may be losing information.
- **Prevention specificity**: Are prevention measures specific to the failure mode discovered, or generic? "Add monitoring" is generic. "Add connection pool monitoring with alerts when active connections exceed a threshold relative to the pool's maximum" is specific.
- **Comparison with Tier 2**: The key experimental question is whether the pipeline produces qualitatively different root cause analysis from the Tier 2 prompt. The Tier 2 version added a scope boundary and diagnosis section — the pipeline removes fix-awareness entirely. If the outputs are similar, the scope boundary may be sufficient for this level of interference. If they differ meaningfully (deeper systemic analysis, broader hypothesis space), the pipeline separation adds value even for well-structured prompts.
