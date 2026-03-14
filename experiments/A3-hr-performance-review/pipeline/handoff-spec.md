# Pipeline Specification: Manager Performance Review

## Pipeline Overview

Produces a manager performance review by separating performance investigation from review writing. The pipeline applies only to the manager review mode — self-assessment and calibration remain single-prompt tasks (see [design notes](design-notes.md) for why).

## Why a Pipeline

The original manager review fuses five types of thinking into one context: investigation (understanding the employee's performance), evaluation (rating and goal assessment), synthesis (performance narrative), generation (development plans, compensation recommendations), and reframing (translating observations into constructive feedback).

The core interference: the template's evaluation slots — rating, goal ratings, development areas — are in context while the model investigates performance data. The model reads performance observations through the template, mapping data to slots rather than genuinely investigating the person's trajectory, contradictions, and growth patterns. The output looks like a thorough review. The gap only appears when investigation happens in a clean context and the review is written from genuinely investigated material.

Tier 2 fixes (reordering the template, adding investigation lenses, removing numeric anchors) improve the margins. But the investigation lenses and the evaluation template still share a context. The model knows it will need to produce a rating, strengths, and development areas — and this knowledge shapes what it notices during investigation. The pipeline separates them into clean contexts.

## Agent Map

| Agent | Thinking Type | Receives | Produces | Why Separate |
|-------|--------------|----------|----------|-------------|
| **Performance Investigator** | Investigation + light Structuring | Employee data, performance observations, goals, context | Structured findings: observations, evidence, patterns, tensions | Investigation without evaluation criteria in context allows the model to notice patterns it would otherwise pre-filter — contradictory signals, trajectory shifts, gaps between perception and impact |
| **Review Writer** | Synthesis + Evaluation + Generation | Structured findings from Agent 1 | Complete manager performance review | Evaluation and synthesis are compatible (both convergent). The writer receives pre-investigated rich material rather than doing shallow template-filling from raw data |

## Execution Order

```
Performance Investigator → Review Writer
```

Sequential. The Review Writer depends entirely on the Investigator's output.

**Rationale for two agents, not more**: The architect analysis found that the manager review has one primary interference — investigation mixed with evaluation. Synthesis, evaluation, and generation are all convergent work that can coexist in the same context. Splitting those into separate agents would add orchestration overhead without resolving a real interference. Two agents is the minimum that separates the toxic pair.

## Handoff Specification

### Handoff: Performance Investigator --> Review Writer

**What crosses**: Structured findings — observations organized by theme, specific evidence with quotes and examples, patterns identified, tensions and contradictions named, trajectory assessment, team impact observations. Bullets and short descriptions, not prose narrative.

**Format**: Structured sections with compressed observations. Factual and descriptive. Each observation backed by specific evidence. Organized by what the investigation surfaced, not by review template sections.

**What gets dropped**: The investigator's exploratory reasoning ("this is interesting because..."), tentative threads that didn't resolve, the investigative journey. The structured findings strip the investigative cognitive mode so the Review Writer gets clean material for synthesis.

**What the Review Writer also receives (not from the pipeline)**: The employee's basic details (name, role, level, team, tenure, review period) and the goals from the prior review cycle. These are factual inputs, not cognitive contaminants — the writer needs them for the template header and goal assessment table.

**What the Review Writer does NOT receive**: The raw performance observations. The writer works from the Investigator's structured findings, not from the original data. If the writer also had the raw data, it would re-investigate in an evaluative context — exactly the contamination the pipeline is designed to prevent.

## Pre-Pipeline: What the Manager Provides

Before running the pipeline, gather from the manager:

1. Employee details (name, role, level, team, tenure)
2. Review period
3. Performance observations — what went well, what needs work, specific examples
4. Goals from the prior review cycle and their status
5. Any promotion or compensation considerations

**Routing**:
- Items 1-4 go to the Performance Investigator (the full picture for investigation)
- Items 1-2 and prior goals go to the Review Writer (factual details for the template, goal assessment)
- Items 3 and 5 do NOT go to the Review Writer — the writer works from investigated findings, not raw observations

The Performance Investigator does not receive promotion or compensation guidance (item 5). These are evaluative conclusions that would bias investigation — the investigator should surface what the evidence shows about readiness and trajectory, not confirm a pre-made decision.

## Execution Instructions

For each run (N = 1, 2, 3):

1. **Stage 1**: Spawn a subagent with `stage-1-investigator.md` as the prompt. Input: the full test material (`test-material/performance-scenario.md`), excluding the "Promotion consideration" and "Compensation" sections. Save output to `pipeline-runs/run-N/stage-1-investigator.md`.

2. **Stage 2**: Spawn a NEW subagent with `stage-2-review-writer.md` as the prompt. Input: the structured findings from Stage 1, plus the employee details section and the goals section from the test material. Save output to `pipeline-runs/run-N/stage-2-review-writer.md`.

**Each stage MUST be a separate subagent** — running both stages in the same context creates the investigation + evaluation fusion the pipeline is designed to avoid.

## Context Window Notes

No volume concerns. Both agents receive modest inputs — the performance scenario is under a page, and the structured findings will be a page or two of compressed observations. No compression checkpoints or external storage needed.

---

## Mapping: Architect Findings --> Pipeline Design

| Architect Finding | Pipeline Response |
|---|---|
| **Investigation + Evaluation fusion** — template structure pre-filters what the model notices | Separated into Performance Investigator (investigation, no template or rating criteria) and Review Writer (evaluation + synthesis, from pre-investigated material). The review template never enters the investigation context. |
| **Evaluation-first ordering** — rating before evidence | The Investigator produces findings with no rating. The Review Writer receives findings and arrives at a rating as a conclusion. The evaluation-first problem is structurally eliminated, not just reordered. |
| **Missing investigation guidance** — prompt treats review as template-filling | The Performance Investigator is entirely devoted to investigation, with lenses for trajectory, growth patterns, contradictory signals, team impact, and the gap between potential and current level. Investigation is the whole job, not a prefix to template-filling. |
| **Numeric anchors** — fixed slot counts for strengths and development areas | Both agents use open-ended formats. The Investigator surfaces as many or few patterns as the evidence warrants. The Review Writer produces strengths and development areas proportional to the findings, not to template slots. |
| **Template-filling replacing genuine investigation** — mapping data to slots | The pipeline makes this structurally impossible. The Investigator has no template to fill. The Review Writer has a template but works from rich investigated material rather than raw data, so the template is shaped by findings rather than the other way around. |

### What to Watch for When Testing

- **Investigation breadth**: Does the Investigator surface patterns beyond what the raw observations explicitly state? For example, does it notice the tension between Jordan's technical excellence and ambiguity-avoidance as a single pattern (comfort with defined problems, discomfort with open ones), or does it just list them as separate items?
- **Contradictory signals**: Does the Investigator name tensions — took on cost optimization voluntarily (initiative) but stalls on ambiguous problems (lack of initiative in a different register)? The monolithic version tends to resolve these prematurely; the pipeline should surface them.
- **Review depth**: Does the Review Writer's Performance Summary feel like genuine synthesis of investigated material, or like a restatement of "meets expectations"? Rich input from the Investigator should produce a summary that captures trajectory and nuance.
- **Development plan specificity**: Are the development actions specific to what the investigation revealed about this person, or are they generic ("improve communication")? The Investigator's findings about the specific gap between IC4 and IC5 should produce a development plan that names the actual capability to build.
- **Natural variation**: If run on a different employee profile, does the pipeline produce different investigation depths and different numbers of findings? Healthy variation signals that the output responds to the evidence, not to the format.
