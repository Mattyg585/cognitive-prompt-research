# A2: Marketing Content — How to Run

Each step should be a **fresh Claude session** to prevent context contamination between phases.

---

## Step 1: Analyse — FRESH SESSION
```
/analyse-prompt Analyse experiments/A2-marketing-content/original/SKILL.md
```
Save output to `experiments/A2-marketing-content/analysis/prompt-architect-analysis.md`

---

## Step 2: Create Tier 2 (optimised) — FRESH SESSION
```
/write-prompt Revise this prompt based on the analysis findings at experiments/A2-marketing-content/analysis/prompt-architect-analysis.md. Original prompt: experiments/A2-marketing-content/original/SKILL.md. Save the revised prompt to experiments/A2-marketing-content/optimised/SKILL.md and save revision notes to experiments/A2-marketing-content/optimised/revision-notes.md
```

---

## Step 3: Create Tier 3 (pipeline) — FRESH SESSION
```
/write-prompt Design a pipeline reconstruction based on the analysis at experiments/A2-marketing-content/analysis/prompt-architect-analysis.md. Original prompt: experiments/A2-marketing-content/original/SKILL.md. Save each agent prompt to experiments/A2-marketing-content/pipeline/ and include a handoff-spec.md describing what crosses between stages and a design-notes.md with rationale.
```

---

## Step 4: Run Baseline (original prompt) — 3 RUNS

Run the original prompt 3 times, each in its own clean context (fresh session or separate subagent).

```
Read the prompt at experiments/A2-marketing-content/original/SKILL.md and execute it. The task is to create a blog post based on the product launch brief at experiments/A2-marketing-content/test-material/product-launch-brief.md. Follow the blog post structure from the prompt. Save your full output to experiments/A2-marketing-content/baseline-runs/run-N.md (where N is 1, 2, or 3).
```

---

## Step 5: Run Tier 2 (optimised prompt) — 3 RUNS

Same as Step 4 but using the optimised prompt:

```
Read the prompt at experiments/A2-marketing-content/optimised/SKILL.md and execute it. The task is to create a blog post based on the product launch brief at experiments/A2-marketing-content/test-material/product-launch-brief.md. Save your full output to experiments/A2-marketing-content/optimised-runs/run-N.md (where N is 1, 2, or 3).
```

---

## Step 6: Run Tier 3 (pipeline) — CRITICAL: SEPARATE SUBAGENT PER STAGE

**Each pipeline stage MUST run in its own clean context (separate subagent or fresh session).** Running all stages in a single subagent defeats the purpose — it creates the same monolithic contamination the pipeline is designed to avoid.

Refer to `experiments/A2-marketing-content/pipeline/handoff-spec.md` for the exact agent sequence, what input each agent receives, and what structured output crosses between stages.

For each of the 3 runs, execute each pipeline agent as a separate subagent, passing only the structured handoff output between them. The 3 runs can be parallelised, but within each run the stages must be sequential.

Save stage outputs to `experiments/A2-marketing-content/pipeline-runs/run-N/` with filenames matching the agent names.

---

## Step 7: Evaluate blind — FRESH SESSION

```
/evaluate-run Compare the outputs across all three tiers for experiment A2. Baseline runs are in experiments/A2-marketing-content/baseline-runs/. Optimised runs are in experiments/A2-marketing-content/optimised-runs/. Pipeline runs — use the final stage output from each run in experiments/A2-marketing-content/pipeline-runs/. Evaluate blind — do not look at which tier produced which output until after scoring. Add domain-specific dimension: Voice and Engagement — does it read well? Would you keep reading?
```

Save the evaluation to `experiments/A2-marketing-content/evaluation/`.

---

## Automation notes

When orchestrating with subagents:
- Steps 4 and 5: 3 subagents each, can run in parallel
- Step 6: 3 runs x N stages (defined in handoff-spec.md). Runs can be parallelised, stages within a run must be sequential. **Each stage MUST be a separate subagent.**
- Step 7: 1 subagent, runs after all outputs are saved
