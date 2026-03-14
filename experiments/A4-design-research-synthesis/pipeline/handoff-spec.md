# Pipeline Specification: Design Research Synthesis

## Pipeline Overview

Synthesises user research data (interview transcripts, survey results, usability notes) into themes, insights, and strategic recommendations through three cognitively separated stages: investigate the data openly, synthesise patterns across participants, then translate findings into product/business implications.

## Why a Pipeline

The original monolithic prompt fuses five incompatible types of thinking into a single context:

1. **Investigation** -- read transcripts, notice patterns, follow threads
2. **Structuring** -- group observations into themes, categorise segments
3. **Synthesis** -- compress observations into insights and a coherent narrative
4. **Evaluation** -- assess impact and effort, prioritise recommendations
5. **Reframing** -- translate findings for product/business stakeholders

All five are subordinated to a rigid output template that determines the shape of the output before any data is read. The template doesn't just format output -- it changes the kind of thinking the model does. Investigation becomes extraction. Synthesis becomes slot-filling.

The core interference: the output template (theme slots, Impact/Effort grid, 3-priority recommendations) is in context while the model reads transcripts, making evaluation and reframing a pre-filter on investigation. The model reads *through* the template, finding things that fit the slots and missing what doesn't. Patterns that resist easy classification get suppressed. Subtle, ambiguous, or surprising observations get dropped because they don't produce clean rows in the Insights-to-Opportunities table.

Prompt-level fixes (scope boundaries, responsive template, summary moved to end) improve the margins but can't eliminate the core interference. Investigation and evaluation criteria share a context. The pipeline separates them into clean contexts with compressed handoffs.

## Agent Map

| Agent | Thinking Type | Receives | Produces | Why Separate |
|-------|--------------|----------|----------|-------------|
| **Data Reader** | Investigation + light Structuring | Raw research data (transcripts, notes, surveys) | Structured observations per participant -- quotes, behaviours, pain points, workarounds, emotional moments | Investigation must be free from theme categories and output structure. Open exploration surfaces what extractive reading misses. |
| **Pattern Synthesiser** | Synthesis + Structuring | Structured observations from Data Reader | Themes with evidence mapping, inter-theme relationships, contradictions, unresolved questions | Synthesis without evaluation criteria or audience reframing allows genuine pattern recognition. The model identifies themes without immediately judging business value. |
| **Strategic Translator** | Reframing + Generation + light Evaluation | Themes and patterns from Pattern Synthesiser | Final synthesis report -- insights with implications, opportunities, recommendations, open questions | Reframing works best on pre-synthesised patterns, not raw data. Translation for stakeholders is a distinct cognitive act from pattern recognition. |

## Execution Order

```
Data Reader → Pattern Synthesiser → Strategic Translator
```

Sequential. Each agent depends on the previous agent's complete output.

**Rationale for sequential**: The dependencies are linear. The Pattern Synthesiser cannot find cross-participant patterns without the full set of per-participant observations. The Strategic Translator cannot reframe findings it hasn't received. The total wall-clock time is longer than a monolithic prompt, but each agent works in a clean context with compressed inputs, which should produce qualitatively different output -- particularly in investigation breadth and thematic depth.

For batch processing (synthesising multiple research studies), the full pipeline can be parallelised *across studies* while remaining sequential *within each study*.

## Handoff Specifications

### Handoff 1: Data Reader --> Pattern Synthesiser

**What crosses**: Structured observations per participant -- key quotes, behavioural observations, pain points described, workarounds developed, emotional moments, contradictions between what participants say and do. Includes specific quotes and concrete details.

**Format**: Structured sections by participant. Factual, observational tone. Each participant gets a consistent set of observation categories, but depth varies with what each participant surfaced.

**What gets dropped**: The reader's exploratory reasoning ("this is interesting because..."), tentative interpretations, analytical asides, the investigative journey. The observations cross; the exploration process does not. Exploratory framing would bias the synthesiser toward continued investigation rather than pattern recognition.

**Why this boundary matters**: The Data Reader explores openly, following whatever threads the data offers. Some of those threads will be dead ends. The structured handoff preserves findings while stripping the investigative posture, so the Pattern Synthesiser receives material it can reason across participants without being pulled into per-participant exploration.

### Handoff 2: Pattern Synthesiser --> Strategic Translator

**What crosses**: Identified themes with evidence mapping (which participants, which observations support each theme), inter-theme relationships, contradictions and tensions, unresolved questions, emerging patterns that may not yet be fully supported.

**Format**: Structured sections by theme. Each theme includes its evidence base (participant references and key observations), its relationship to other themes, and its current strength (well-supported vs. emerging). Also includes a section on cross-cutting tensions and open questions.

**What gets dropped**: The synthesis reasoning process, alternative theme groupings considered, the synthesiser's deliberation about how to cluster observations. The themes and their evidence cross; the process of arriving at them does not. Synthesis residue (the deliberative, "on the other hand" posture) would anchor the translator to continued analysis rather than decisive reframing for stakeholders.

**Why this boundary matters**: The Strategic Translator needs to know what the patterns are and how strong the evidence is. It does not need to know how the synthesiser arrived at those patterns. The translator's job is to ask "what does this mean for the product?" -- not to re-evaluate whether the themes are correct.

## Pre-Pipeline: Context Gathering

Before running the pipeline, gather:

1. The research data (transcripts, notes, survey results)
2. Study context (research question, method, participant count, any relevant background)

**Routing**:
- Items 1-2 --> Data Reader (the study context helps orient investigation without biasing it)
- No additional inputs to Pattern Synthesiser (it works from the Data Reader's output only)
- No additional inputs to Strategic Translator (it works from the Pattern Synthesiser's output only)

The Pattern Synthesiser and Strategic Translator do **not** receive the raw research data. The Data Reader's structured observations are the canonical representation of what the data contains. This prevents later agents from re-investigating the data through the lens of themes they've already committed to.

## Execution Instructions

For each run (N = 1, 2, 3):

1. **Stage 1**: Spawn a subagent with `stage-1-data-reader.md` as the prompt. Input: the research data (e.g., `test-material/user-interviews.md`). Save output to `pipeline-runs/run-N/stage-1-data-reader.md`.

2. **Stage 2**: Spawn a NEW subagent with `stage-2-pattern-synthesiser.md` as the prompt. Input: the Data Reader output from Stage 1. Save output to `pipeline-runs/run-N/stage-2-pattern-synthesiser.md`.

3. **Stage 3**: Spawn a NEW subagent with `stage-3-strategic-translator.md` as the prompt. Input: the Pattern Synthesiser output from Stage 2. Save output to `pipeline-runs/run-N/stage-3-strategic-translator.md`.

**Each stage MUST be a separate subagent** -- running stages in the same context creates the exact monolithic contamination the pipeline is designed to avoid.

The Stage 3 output is the final synthesis report. This is the output that should be evaluated against the baseline and optimised versions.

## Context Window Notes

- **Data Reader**: May face context pressure with very large research datasets (dozens of transcripts, thousands of survey responses). For studies exceeding context capacity, run multiple Reader instances on subsets of participants with a lightweight merge step that combines the structured observations. Most studies (under 20 interviews, or surveys with summary data) fit in a single pass.
- **Pattern Synthesiser**: Receives compressed observations (substantially smaller than raw transcripts). Manageable in all cases.
- **Strategic Translator**: Receives only themed patterns with evidence mapping. The lightest context load of all agents. No capacity concerns.

---

## Mapping: Architect Findings --> Pipeline Design

Each finding from the architect analysis maps to a specific pipeline design decision:

| Architect Finding | Pipeline Response |
|---|---|
| **Output template forces premature convergence** (High) -- fixed theme slots, Impact/Effort grid, 3-priority recommendations shape investigation | Eliminated entirely from investigation. The Data Reader has no output template beyond "structured observations per participant." Theme structure only appears in the Pattern Synthesiser. The final report structure only appears in the Strategic Translator. No agent's output format pre-determines the investigation. |
| **Investigation + Evaluation simultaneous** (High) -- Impact/Effort columns bias investigation toward easily-evaluable patterns | Separated across all three agents. The Data Reader investigates without evaluation criteria. The Pattern Synthesiser identifies themes without judging business impact. The Strategic Translator evaluates implications only after patterns are fully formed. |
| **Insights-to-Opportunities table conflates four thinking types** (Moderate) -- synthesis, generation, and evaluation forced into a linear 1:1 grid | Each thinking type in its own agent. Insights emerge in the Pattern Synthesiser. Opportunities are generated by the Strategic Translator. The relationship between insights and opportunities is narrative, not tabular. |
| **Executive Summary appears first** (Moderate) -- premature narrative commitment anchors everything | No summary appears in any agent until the final output. The Strategic Translator writes the summary last, as a genuine distillation of the translated findings. |
| **Implicit count anchors** (Moderate) -- 3-5 themes, 2 quotes, 3 recommendations | All numeric anchors removed across all agents. No "top N" in any agent. Observation counts, theme counts, and recommendation counts respond to the data. |
| **Recommendations mix generation with evaluation** (Moderate) -- prioritisation constrains generation | Separated. The Strategic Translator generates recommendations based on pattern strength from the Synthesiser, not from a forced High/Med/Low scheme. |

### What to Watch for When Testing

- **Data Reader breadth**: Does it surface observations that don't fit standard UX research categories? Does it notice emotional signals, workarounds, contradictions between said and done? If it produces only standard "pain point / need / feature request" categories, the lenses aren't working.
- **Theme surprise**: Does the Pattern Synthesiser find themes the monolithic version misses? Not just more themes, but DIFFERENT themes -- ones that emerge from open investigation rather than template-shaped extraction.
- **Cross-theme tensions**: Does the Synthesiser identify contradictions and tensions between themes, or does it present themes as independent, cleanly separated categories? Real research data is messy. The themes should reflect that.
- **Strategic depth**: Does the Translator produce genuine product/business implications, or does it restate the themes with "we should fix this" bolted on? The translator should reason about what patterns mean, not just relay them.
- **Natural variation**: Run on different datasets. Does the pipeline produce different numbers of themes, different amounts of evidence, different levels of recommendation specificity? If output volume is uniform across datasets, something is anchoring.
