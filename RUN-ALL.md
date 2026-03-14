# RUN-ALL: Full Experiment Suite (A1–A6)

This file covers running all six experiments end-to-end on any model via GitHub Copilot CLI (or Copilot Chat in VS Code/JetBrains). It is designed to be self-contained — no external slash commands, no Claude Code dependencies. Everything is expanded inline.

---

## How GitHub Copilot CLI Works for This Experiment

### Starting a session

```bash
copilot
```

Copilot will ask you to confirm you trust the files in the current directory.

### Key session commands (these control the CLI, not the AI)

| Command | What it does |
|---|---|
| `/add-dir <path>` | Grant Copilot access to a directory |
| `/model` | Select which model to use — do this before starting |
| `/clear` | Reset the conversation context (fresh session equivalent) |
| `/exit` | End the session |
| `/session` | Show session metadata including model in use |

### Slash commands vs. prompts

Copilot CLI slash commands (`/clear`, `/model`, etc.) are session management instructions — they do **not** invoke AI. All AI work happens through natural language prompts that you type or paste. There are no custom skill slash commands like `/analyse-prompt` in Copilot — those are Claude Code-specific. This file contains the expanded inline equivalents.

### Getting fresh context between steps

**Within a session**: Use `/clear` to reset context between steps. This is sufficient for most steps.

**For pipeline stages (Step 6 in each experiment)**: Start a **new terminal session** (`copilot`) for each pipeline stage. This is not optional — `/clear` between stages in the same session leaves residual context that recreates the contamination you're testing against. The whole point of the pipeline is clean context at each stage boundary.

---

## Before You Start

### 1. Add the repository directory

At the start of your Copilot session:
```
/add-dir /path/to/cognitive-prompt-research
```

### 2. Select your model

```
/model
```

Select the model you want to test. Note the exact model name shown.

### 3. Record your metadata

Every output file in this experiment should begin with this header. Ask Copilot to include it at the top of every saved file, or add it manually.

```
---
model: [exact model name from /model]
date: [YYYY-MM-DD]
experiment: [A1 / A2 / A3 / A4 / A5 / A6]
tier: [baseline / optimised / pipeline]
run: [1 / 2 / 3]
stage: [for pipeline only: e.g. 01-contract-reader]
---
```

This metadata is critical for cross-model comparison. Without it, outputs become ambiguous.

---

## Protocol

Each experiment follows the same 7-step protocol. Steps 1–3 create the three tiers. Steps 4–6 run them. Step 7 evaluates blind.

- **Steps 1–3**: Sequential within an experiment (each depends on the previous)
- **Steps 4–5**: Can run in parallel (two sessions, one per tier)
- **Step 6**: Pipeline stages must be sequential within a run, but multiple runs can be parallelised
- **Step 7**: After all outputs are saved

For A1 and A2: run 3 times per tier. For A3–A6: run once per tier (or 3 times if you want variation data).

---

## A1: Legal Contract Review

**Test material**: `experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md`
**Test scenario**: Customer/buyer perspective, $150K/year, 2-week deadline, priorities are data protection and IP ownership.
**Domain dimension**: Risk identification accuracy

### Step 1: Analyse — fresh session

```
Read the analysis framework at toolkit/prompt-architect-agent.md. Also read the theoretical foundation at toolkit/cognitive-stance-reference.md. You are acting as the Prompt Architect described in those files.

Apply this framework to analyse the prompt at experiments/A1-legal-contract-review/original/SKILL.md.

Your analysis should cover:
1. What the prompt is actually asking for — what types of thinking it requires and how they relate (not a list of tasks, a description of cognitive posture)
2. Where modes interfere — specific, evidence-based observations quoting the prompt and explaining the interference mechanism
3. What to look for in the output — diagnostic signals that contamination is happening, testable predictions
4. What to do about it — interventions at prompt level (scope boundaries, seed-to-lens conversions, anchor removal) and pipeline level (when and how to split), with trade-offs stated

Save your full analysis to experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md
```

### Step 2: Create Tier 2 (optimised) — /clear or new session

```
Read the prompt writer framework at toolkit/prompt-writer-agent.md and the theoretical foundation at toolkit/cognitive-stance-reference.md. You are acting as the Prompt Writer described in those files.

Read the architect's analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md. Read the original prompt at experiments/A1-legal-contract-review/original/SKILL.md.

Your job is to implement the prompt-level optimisations identified in the analysis. Produce a revised version that:
- Addresses the specific interference mechanisms identified
- Preserves what the architect found to be working
- Does not restructure the whole prompt — fix what needs fixing

Also produce revision notes documenting: each finding → what changed → why.

Save the revised prompt to experiments/A1-legal-contract-review/optimised/SKILL.md
Save the revision notes to experiments/A1-legal-contract-review/optimised/revision-notes.md
```

### Step 3: Create Tier 3 (pipeline) — /clear or new session

```
Read the prompt writer framework at toolkit/prompt-writer-agent.md and the theoretical foundation at toolkit/cognitive-stance-reference.md. You are acting as the Prompt Writer designing a multi-agent pipeline.

Read the architect's analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md. Read the original prompt at experiments/A1-legal-contract-review/original/SKILL.md.

Design a pipeline that separates incompatible cognitive modes into distinct agents with clean contexts. For each agent:
- Name it by function, not position
- Specify what types of thinking it handles
- Specify what it receives as input (format matters — structured data strips cognitive mode, prose carries it)
- Specify what it produces as output
- Explain why it is separate (what interference it avoids)

Save each agent as a separate file in experiments/A1-legal-contract-review/pipeline/
Save a handoff-spec.md describing: the agent sequence, what structured output crosses between each stage, and what gets dropped at each boundary
Save a design-notes.md explaining the pipeline architecture decisions
```

### Step 4: Run baseline — 3 fresh sessions (can run in parallel)

For each of runs 1, 2, 3 — start a new session or /clear:

```
Read the prompt at experiments/A1-legal-contract-review/original/SKILL.md and execute it.

Your input is the contract at experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md. The test scenario is defined at the top of that file: customer/buyer perspective, $150K/year, 2-week deadline, priorities are data protection and IP ownership.

Begin your output with this metadata header:
---
model: [the model you are using]
date: [today's date]
experiment: A1
tier: baseline
run: [1 / 2 / 3]
---

Save your full output to experiments/A1-legal-contract-review/baseline-runs/run-N.md
```

### Step 5: Run Tier 2 — 3 fresh sessions (can run in parallel with Step 4)

Same as Step 4, using the optimised prompt:

```
Read the prompt at experiments/A1-legal-contract-review/optimised/SKILL.md and execute it.

Your input is the contract at experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md. The test scenario is at the top of that file.

Begin your output with this metadata header:
---
model: [the model you are using]
date: [today's date]
experiment: A1
tier: optimised
run: [1 / 2 / 3]
---

Save your full output to experiments/A1-legal-contract-review/optimised-runs/run-N.md
```

### Step 6: Run Tier 3 (pipeline) — NEW SESSION PER STAGE

**Each stage must be a completely new `copilot` session.** Not `/clear` — a new terminal session. Running stages in the same session recreates the contamination the pipeline is designed to prevent.

For each of 3 runs, execute these stages sequentially in separate sessions:

#### Stage 1 — new session

```
Read the agent prompt at experiments/A1-legal-contract-review/pipeline/01-contract-reader.md (or the first agent in that directory — check handoff-spec.md for the sequence).

Your input is the contract at experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md and the test scenario at the top of that file.

Begin your output with:
---
model: [model name]
date: [today's date]
experiment: A1
tier: pipeline
run: [N]
stage: 01-contract-reader
---

Save your output to experiments/A1-legal-contract-review/pipeline-runs/run-N/01-contract-reader-output.md
```

#### Stage 2 — new session

```
Read the agent prompt at experiments/A1-legal-contract-review/pipeline/02-playbook-comparator.md.

Your input is the previous stage's output at experiments/A1-legal-contract-review/pipeline-runs/run-N/01-contract-reader-output.md. Do not read the original contract or any other context from Stage 1 — only the structured output that crossed the boundary.

Begin your output with:
---
model: [model name]
date: [today's date]
experiment: A1
tier: pipeline
run: [N]
stage: 02-playbook-comparator
---

Save your output to experiments/A1-legal-contract-review/pipeline-runs/run-N/02-playbook-comparator-output.md
```

#### Stage 3 — new session

```
Read the agent prompt at experiments/A1-legal-contract-review/pipeline/03-redline-writer.md.

Your inputs are:
- The Playbook Comparator's output at experiments/A1-legal-contract-review/pipeline-runs/run-N/02-playbook-comparator-output.md
- The original contract at experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md (for quoting specific language)
- The business context from the test scenario at the top of the contract file

Begin your output with:
---
model: [model name]
date: [today's date]
experiment: A1
tier: pipeline
run: [N]
stage: 03-redline-writer
---

Save your output to experiments/A1-legal-contract-review/pipeline-runs/run-N/03-redline-writer-output.md
```

#### Stage 4 — new session

```
Read the agent prompt at experiments/A1-legal-contract-review/pipeline/04-strategic-advisor.md.

Your inputs are:
- The Playbook Comparator's output at experiments/A1-legal-contract-review/pipeline-runs/run-N/02-playbook-comparator-output.md
- The Redline Writer's output at experiments/A1-legal-contract-review/pipeline-runs/run-N/03-redline-writer-output.md
- The business context from the test scenario at the top of experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md

Do not read Stage 1's exploratory output. Only what is listed above crosses this boundary.

Begin your output with:
---
model: [model name]
date: [today's date]
experiment: A1
tier: pipeline
run: [N]
stage: 04-strategic-advisor
---

Save your output to experiments/A1-legal-contract-review/pipeline-runs/run-N/04-strategic-advisor-output.md
```

### Step 7: Evaluate blind — fresh session

```
Read the evaluator instructions at evaluation/evaluator-prompt.md. Read the rubric at evaluation/rubric.md. You are the independent evaluator described in those files.

You are comparing three outputs for experiment A1 (legal contract review). You do not know which version is which — evaluate each independently before looking at patterns.

The outputs to compare are:
- Output Set 1: experiments/A1-legal-contract-review/baseline-runs/ (use the median-quality run for scoring dimensions 1,2,4,5 — score all 3 runs for dimension 3, Natural Variation)
- Output Set 2: experiments/A1-legal-contract-review/optimised-runs/ (same approach)
- Output Set 3: The final stage output from each pipeline run — experiments/A1-legal-contract-review/pipeline-runs/run-N/04-strategic-advisor-output.md

For this experiment, add a domain-specific dimension: Risk Identification Accuracy — did the output find the genuinely risky clauses, including ones that interact across sections?

Score each set independently. Produce a comparison table. State your overall preference and the magnitude. Note what the better version does that the others do not.

Save your evaluation to experiments/A1-legal-contract-review/evaluation/blind-evaluation-[model-name]-[date].md
```

---

## A2: Marketing Content

**Test material**: `experiments/A2-marketing-content/test-material/product-launch-brief.md`
**Domain dimension**: Voice and Engagement — does it read well? Would you keep reading?
**Pipeline stages**: Check `experiments/A2-marketing-content/pipeline/handoff-spec.md` for the exact stage sequence.

### Step 1: Analyse — fresh session

```
Read the analysis framework at toolkit/prompt-architect-agent.md and the theoretical foundation at toolkit/cognitive-stance-reference.md. You are acting as the Prompt Architect.

Apply this framework to analyse experiments/A2-marketing-content/original/SKILL.md.

Cover: what types of thinking the prompt requires, where modes interfere, what to look for in the output, and what to do about it. For creative work specifically, consider whether convergent constraints (voice guidelines, format requirements, SEO objectives) are suppressing or supporting the generation.

Save your analysis to experiments/A2-marketing-content/analysis/prompt-architect-analysis.md
```

### Step 2: Create Tier 2 (optimised) — /clear or new session

```
Read toolkit/prompt-writer-agent.md and toolkit/cognitive-stance-reference.md. You are the Prompt Writer.

Read the architect's analysis at experiments/A2-marketing-content/analysis/prompt-architect-analysis.md and the original prompt at experiments/A2-marketing-content/original/SKILL.md.

Implement prompt-level optimisations. For creative work, pay particular attention to whether constraints are functioning as seeds (constraining generation) or lenses (guiding voice without dictating output). Preserve what's working.

Save the revised prompt to experiments/A2-marketing-content/optimised/SKILL.md
Save revision notes to experiments/A2-marketing-content/optimised/revision-notes.md
```

### Step 3: Create Tier 3 (pipeline) — /clear or new session

```
Read toolkit/prompt-writer-agent.md and toolkit/cognitive-stance-reference.md. You are the Prompt Writer designing a pipeline.

Read experiments/A2-marketing-content/analysis/prompt-architect-analysis.md and experiments/A2-marketing-content/original/SKILL.md.

Design a pipeline for this marketing content task. Note: creative work may require different pipeline logic than analytical work — consider whether stage separation adds or removes creative coherence.

Save each agent to experiments/A2-marketing-content/pipeline/
Save handoff-spec.md (stage sequence, what crosses, what gets dropped)
Save design-notes.md (architecture decisions, including any trade-offs for creative work)
```

### Steps 4–7

Follow the same pattern as A1. Replace all A1 paths with A2 paths. For Step 6, check `experiments/A2-marketing-content/pipeline/handoff-spec.md` for the stage sequence and use the final stage output for evaluation. For Step 7 evaluation, use the final stage output for each pipeline run and add the domain dimension: **Voice and Engagement**.

---

## A3: HR Performance Review

**Test material**: `experiments/A3-hr-performance-review/test-material/performance-scenario.md`
**Test scenario**: Manager mode, reviewing Jordan Chen
**Domain dimension**: Bias and fairness — does the output avoid problematic assumptions?
**Expected pattern**: Template generation task — calibration case for whether the pipeline adds value to constrained output

Follow Steps 1–7 as per the A1 template, substituting A3 paths throughout. For Step 6, check `experiments/A3-hr-performance-review/pipeline/handoff-spec.md` for stage sequence. Use the final stage output for evaluation.

---

## A4: Design Research Synthesis

**Test material**: `experiments/A4-design-research-synthesis/test-material/user-interviews.md`
**Task**: Synthesise 6 user interviews into themes, insights, and recommendations
**Domain dimension**: none beyond core rubric
**Expected pattern**: Synthesis constrained by fixed output structure — pipeline should free the synthesis to reframe rather than catalogue

Follow Steps 1–7 as per the A1 template, substituting A4 paths throughout. For Step 7 evaluation, note specifically whether the output catalogues themes versus reframes them strategically.

---

## A5: Engineering Debug

**Test material**: `experiments/A5-engineering-debug/test-material/bug-report.md`
**Task**: Debug an intermittent order processing failure
**Domain dimension**: Correctness — does the diagnosis and fix hold up?
**Expected pattern**: Sequential task that may already be well-structured — calibration case

Follow Steps 1–7 as per the A1 template, substituting A5 paths throughout.

---

## A6: SecOps Incident Response

**Test material**: `experiments/A6-secops-incident-response/test-material/incident-scenario.md`
**Test scenario**: Postmortem mode, resolved data exposure incident
**Domain dimension**: none beyond core rubric
**Expected pattern**: 4-mode mixing, "5 Whys" anchor — should show the largest baseline-to-pipeline gap

Follow Steps 1–7 as per the A1 template, substituting A6 paths throughout. For Step 7 evaluation, note specifically whether the output is a standard incident report versus an organisational learning artifact.

---

## Cross-Experiment Synthesis

After all experiments complete, run a synthesis pass:

```
Read the evaluation outputs for all six experiments:
- experiments/A1-legal-contract-review/evaluation/
- experiments/A2-marketing-content/evaluation/
- experiments/A3-hr-performance-review/evaluation/
- experiments/A4-design-research-synthesis/evaluation/
- experiments/A5-engineering-debug/evaluation/
- experiments/A6-secops-incident-response/evaluation/

Also read the existing findings at findings.md for context on what previous runs found.

Produce a cross-experiment summary covering:
1. Results table: baseline / optimised / pipeline scores for each experiment
2. Consistent patterns across experiments
3. Exceptions and boundary conditions
4. Any differences from previous runs (the findings.md baseline was produced by a different model — note where this model diverged)
5. What the findings suggest about whether the pattern is model-specific or model-agnostic

Save to findings-[model-name]-[date].md in the root directory. Do not overwrite the existing findings.md.
```

---

## Parallelisation Guide

If you have multiple terminal windows available:

**Maximum parallelisation — 6 experiments simultaneously:**
- Open 6 terminals, each running `copilot`
- Each terminal handles one experiment (A1–A6) through all 7 steps sequentially
- Steps 4 and 5 within each experiment can themselves run in parallel (open a 7th terminal for the second tier run)

**Minimal parallelisation — sequential:**
- Run each experiment fully (Steps 1–7) before starting the next
- This is slower but easier to track and debug if something goes wrong

**Step 6 (pipeline) within any experiment:**
- Cannot be parallelised within a run (Stage 2 needs Stage 1's output)
- Different runs (run-1, run-2, run-3) can run in parallel — open a separate terminal for each run, but each terminal must start a new session for each stage

**Evaluation (Step 7):**
- Can run in parallel across experiments once that experiment's outputs are complete
- Does not need to wait for other experiments

---

## Troubleshooting

**"The model isn't following the agent instructions"**
Copilot may compress long file reads. If the model seems to be ignoring the toolkit agent files, paste the key sections of the agent file directly into your prompt rather than asking it to read them.

**"The output doesn't have the metadata header"**
Add the metadata manually after the fact. The header is for your records, not for the model's output quality.

**"The pipeline stage output doesn't seem clean — it mentions things from earlier stages"**
This means you ran multiple stages in the same session. Discard that run and restart in a new terminal session. This is not a minor issue — contaminated pipeline runs defeat the purpose of the comparison.

**"Steps 1–3 produced very similar analysis/optimisation to the previous run (Claude)"**
This is expected and is a finding: the architect and writer agents are producing consistent outputs across models. Note it in findings.

**"Perfect scores (all 25/25) for pipeline again"**
Flag it. It suggests ceiling effect in the rubric or evaluator bias. Add a note: "if pipeline scores 25/25, note which specific output elements justify each 5/5 score so the reasoning is auditable."
