# A1: Legal Contract Review — How to Run

Each step should be a **fresh Claude session** to prevent context contamination between phases.

---

## Step 1: Analyse (DONE)
```
/analyse-prompt Analyse experiments/A1-legal-contract-review/original/SKILL.md
```
Output saved to: `analysis/prompt-architect-analysis.md`

---

## Step 2: Create Tier 2 (optimised) — FRESH SESSION
```
/write-prompt Revise this prompt based on the analysis findings at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md. Original prompt: experiments/A1-legal-contract-review/original/SKILL.md. Save the revised prompt to experiments/A1-legal-contract-review/optimised/SKILL.md
```

---

## Step 3: Create Tier 3 (pipeline) — FRESH SESSION
```
/write-prompt Design a pipeline reconstruction based on the analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md. Original prompt: experiments/A1-legal-contract-review/original/SKILL.md. Save each agent prompt to experiments/A1-legal-contract-review/pipeline/ and include a handoff-spec.md describing what crosses between stages.
```

---

## Step 4: Run Baseline (original prompt) — 3 FRESH SESSIONS

Run the original prompt 3 times, each in a fresh session. Copy-paste this into each session:

```
Read the prompt at experiments/A1-legal-contract-review/original/SKILL.md and execute it against the contract at experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md. The test scenario is defined at the top of the contract file. Save your full output to experiments/A1-legal-contract-review/baseline-runs/run-N.md (where N is 1, 2, or 3).
```

---

## Step 5: Run Tier 2 (optimised prompt) — 3 FRESH SESSIONS

Same as Step 4 but using the optimised prompt:

```
Read the prompt at experiments/A1-legal-contract-review/optimised/SKILL.md and execute it against the contract at experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md. The test scenario is defined at the top of the contract file. Save your full output to experiments/A1-legal-contract-review/optimised-runs/run-N.md (where N is 1, 2, or 3).
```

---

## Step 6: Run Tier 3 (pipeline) — 3 RUNS, EACH WITH FRESH SESSIONS PER AGENT

This is the most involved step. For each of the 3 runs, you run each pipeline agent in sequence, each in its own fresh session. Check the `pipeline/handoff-spec.md` for what output to pass between agents.

The general pattern for each pipeline agent:
```
Read the agent prompt at experiments/A1-legal-contract-review/pipeline/01-investigate.md. Your input is [the contract OR the previous agent's output]. Save your output to experiments/A1-legal-contract-review/pipeline-runs/run-N/01-investigate-output.md
```

Then start a fresh session for the next agent:
```
Read the agent prompt at experiments/A1-legal-contract-review/pipeline/02-evaluate.md. Your input is the previous agent's output at experiments/A1-legal-contract-review/pipeline-runs/run-N/01-investigate-output.md plus the contract at experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md. Save your output to experiments/A1-legal-contract-review/pipeline-runs/run-N/02-evaluate-output.md
```

And so on for each agent in the pipeline. The exact agent names and handoff details will be defined when you create the pipeline in Step 3.

---

## Step 7: Evaluate blind — FRESH SESSION
```
/evaluate-run Compare the outputs across all three tiers for experiment A1. Baseline runs are in experiments/A1-legal-contract-review/baseline-runs/. Optimised runs are in experiments/A1-legal-contract-review/optimised-runs/. Pipeline runs are in experiments/A1-legal-contract-review/pipeline-runs/. Use the final output from each pipeline run for comparison. Evaluate blind — do not look at which tier produced which output until after scoring.
```

Save the evaluation to `experiments/A1-legal-contract-review/evaluation/`.
