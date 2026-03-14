# Run Experiments A3–A6

Run all four experiments end-to-end. Each experiment follows the same 7-step protocol with **1 run per tier** (not 3).

**CRITICAL**: Each step of each experiment must be a **separate subagent with clean context**. Pipeline stages within Step 6 must EACH be a separate subagent — do NOT run multiple pipeline stages in a single subagent, as this defeats the purpose by creating context contamination.

---

## For each experiment (A3, A4, A5, A6):

### Step 1: Analyse — separate subagent
```
/analyse-prompt Analyse experiments/{EXPERIMENT}/original/SKILL.md
```
Save to `experiments/{EXPERIMENT}/analysis/prompt-architect-analysis.md`

### Step 2: Create Tier 2 (optimised) — separate subagent
```
/write-prompt Revise this prompt based on the analysis findings at experiments/{EXPERIMENT}/analysis/prompt-architect-analysis.md. Original prompt: experiments/{EXPERIMENT}/original/SKILL.md. Save the revised prompt to experiments/{EXPERIMENT}/optimised/SKILL.md and revision notes to experiments/{EXPERIMENT}/optimised/revision-notes.md
```

### Step 3: Create Tier 3 (pipeline) — separate subagent
```
/write-prompt Design a pipeline reconstruction based on the analysis at experiments/{EXPERIMENT}/analysis/prompt-architect-analysis.md. Original prompt: experiments/{EXPERIMENT}/original/SKILL.md. Save each agent prompt to experiments/{EXPERIMENT}/pipeline/ with a handoff-spec.md and design-notes.md
```

### Step 4: Run baseline — separate subagent
Read the original prompt at `experiments/{EXPERIMENT}/original/SKILL.md` and execute it against the test material at `experiments/{EXPERIMENT}/test-material/`. Save output to `experiments/{EXPERIMENT}/baseline-runs/run-1.md`.

### Step 5: Run Tier 2 — separate subagent
Read the optimised prompt at `experiments/{EXPERIMENT}/optimised/SKILL.md` and execute it against the same test material. Save output to `experiments/{EXPERIMENT}/optimised-runs/run-1.md`.

### Step 6: Run Tier 3 — SEPARATE SUBAGENT PER PIPELINE STAGE
Read the handoff-spec.md in `experiments/{EXPERIMENT}/pipeline/` for the stage sequence. Run each stage as a separate subagent, passing only the structured handoff output between stages. Save stage outputs to `experiments/{EXPERIMENT}/pipeline-runs/run-1/`.

### Step 7: Evaluate blind — separate subagent
Compare the final outputs from all three tiers. Score using the rubric at `evaluation/rubric.md` and the evaluator prompt at `evaluation/evaluator-prompt.md`. Save to `experiments/{EXPERIMENT}/evaluation/`.

---

## Experiment Details

### A3 — HR Performance Review
- **Prompt**: `experiments/A3-hr-performance-review/original/SKILL.md`
- **Test material**: `experiments/A3-hr-performance-review/test-material/performance-scenario.md`
- **Mode**: `manager` review for Jordan Chen
- **Expected pattern**: Mostly template generation — may show limited improvement (calibration case)

### A4 — Design Research Synthesis
- **Prompt**: `experiments/A4-design-research-synthesis/original/SKILL.md`
- **Test material**: `experiments/A4-design-research-synthesis/test-material/user-interviews.md`
- **Task**: Synthesise 6 user interviews into themes, insights, and recommendations
- **Expected pattern**: Synthesis constrained by fixed output structure — pipeline should free the synthesis

### A5 — Engineering Debug
- **Prompt**: `experiments/A5-engineering-debug/original/SKILL.md`
- **Test material**: `experiments/A5-engineering-debug/test-material/bug-report.md`
- **Task**: Debug an intermittent order processing failure
- **Expected pattern**: Clean 4-step sequence — may already be well-structured (calibration case)

### A6 — SecOps Incident Response
- **Prompt**: `experiments/A6-secops-incident-response/original/SKILL.md`
- **Test material**: `experiments/A6-secops-incident-response/test-material/incident-scenario.md`
- **Mode**: `postmortem` for resolved data exposure incident
- **Expected pattern**: 4-mode mixing, "5 Whys" anchor — pipeline should improve root cause analysis

---

## Execution Strategy

Steps 1-3 for each experiment are sequential (each depends on the previous). But you can run all four experiments in parallel — A3 Steps 1-3 alongside A4 Steps 1-3, etc.

Steps 4-5 can run in parallel within each experiment.

Step 6 stages must be sequential within each experiment but the four experiments' pipelines can run in parallel.

Step 7 runs after all outputs for that experiment are saved.

---

## After All Experiments Complete

Set up blind comparison for each experiment:
1. Copy the final output from each tier into `experiments/{EXPERIMENT}/blind-comparison/` with randomised 6-character IDs
2. Include a README.md with evaluation criteria appropriate to the domain
3. Include the test material
4. Include a KEY.md mapping IDs to tiers (not to be read before evaluation)

Commit and push everything when done.
