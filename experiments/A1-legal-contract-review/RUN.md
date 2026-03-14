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

Run the original prompt 3 times, each in a fresh session (or as 3 parallel subagents, each with its own clean context).

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

## Step 6: Run Tier 3 (pipeline) — CRITICAL: 4 SEPARATE SUBAGENTS PER RUN

**Each pipeline stage MUST run in its own clean context (separate subagent or fresh session).** Running all 4 stages in a single subagent defeats the entire purpose — it becomes another monolithic prompt with accumulated cognitive residue. The whole point of the pipeline is that each agent gets a clean context without the previous stage's cognitive mode contaminating it.

For each of the 3 runs, execute 4 sequential subagents:

### Stage 1: Contract Reader (Investigation)
```
Read the agent prompt at experiments/A1-legal-contract-review/pipeline/01-contract-reader.md. Your input is the contract at experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md plus the test scenario defined at the top of that file. Save your output to experiments/A1-legal-contract-review/pipeline-runs/run-N/01-contract-reader-output.md
```

### Stage 2: Playbook Comparator (Evaluation)
**New subagent — clean context.** Input is the previous stage's output only.
```
Read the agent prompt at experiments/A1-legal-contract-review/pipeline/02-playbook-comparator.md. Your input is the Contract Reader's output at experiments/A1-legal-contract-review/pipeline-runs/run-N/01-contract-reader-output.md. Save your output to experiments/A1-legal-contract-review/pipeline-runs/run-N/02-playbook-comparator-output.md
```

### Stage 3: Redline Writer (Generation)
**New subagent — clean context.** Input is the Comparator's output plus the original contract (for quoting) and business context from the test scenario.
```
Read the agent prompt at experiments/A1-legal-contract-review/pipeline/03-redline-writer.md. Your inputs are: the Playbook Comparator's output at experiments/A1-legal-contract-review/pipeline-runs/run-N/02-playbook-comparator-output.md, the original contract at experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md, and the business context from the test scenario at the top of the contract file. Save your output to experiments/A1-legal-contract-review/pipeline-runs/run-N/03-redline-writer-output.md
```

### Stage 4: Strategic Advisor (Synthesis + Reframing)
**New subagent — clean context.** Input is all previous outputs plus business context.
```
Read the agent prompt at experiments/A1-legal-contract-review/pipeline/04-strategic-advisor.md. Your inputs are: the Playbook Comparator's output at experiments/A1-legal-contract-review/pipeline-runs/run-N/02-playbook-comparator-output.md, the Redline Writer's output at experiments/A1-legal-contract-review/pipeline-runs/run-N/03-redline-writer-output.md, and the business context from the test scenario at the top of experiments/A1-legal-contract-review/test-material/common-paper-csa-v2.1.md. Save your output to experiments/A1-legal-contract-review/pipeline-runs/run-N/04-strategic-advisor-output.md
```

### Why this matters

A single subagent running all 4 stages has the Contract Reader's exploratory prose in context when the Comparator evaluates, the Comparator's classifications in context when the Redline Writer generates, and ALL of that accumulated residue when the Strategic Advisor tries to synthesise. That's the same contamination pattern as the monolithic prompt — just with the stages labelled differently. Separate subagents strip the cognitive residue at each boundary because only the structured output crosses, not the full context.

The handoff-spec.md in the pipeline directory defines exactly what structured output crosses between stages.

---

## Step 7: Evaluate blind — FRESH SESSION
```
/evaluate-run Compare the outputs across all three tiers for experiment A1. Baseline runs are in experiments/A1-legal-contract-review/baseline-runs/. Optimised runs are in experiments/A1-legal-contract-review/optimised-runs/. Pipeline runs — use the Stage 4 (Strategic Advisor) output as the final output from each run, at experiments/A1-legal-contract-review/pipeline-runs/run-N/04-strategic-advisor-output.md. Evaluate blind — do not look at which tier produced which output until after scoring.
```

Save the evaluation to `experiments/A1-legal-contract-review/evaluation/`.

---

## Automation notes

When orchestrating with subagents:
- Steps 4 and 5: 3 subagents each, can run in parallel (each gets clean context naturally)
- Step 6: 3 runs x 4 stages = 12 subagents. The 3 runs can be parallelised, but within each run the 4 stages must be sequential (each depends on the previous stage's output). **Each stage MUST be a separate subagent.**
- Step 7: 1 subagent, runs after all outputs are saved
