# B2: PRBench — Can Cognitive Mode Separation Improve Professional Reasoning?

## Background

PRBench (Scale AI) is a professional reasoning benchmark with 1,100 expert-authored tasks in Law (550) and Finance (550). Tasks are derived from real professional workflows across 114 countries and 47 US jurisdictions.

**Why this matters for our research**:
- Top models score only 37-39% on the Hard subset — massive headroom
- Rubric-based scoring across 11 dimensions captures reasoning quality, not just correctness
- The benchmark's own paper documents our exact phenomenon: *"models frequently reach correct conclusions through incomplete or opaque reasoning"* — this is "good output hides great output"
- Professional reasoning tasks require investigation + analysis + synthesis — classic multi-mode work

**Key difference from A-series**: Expert-curated rubrics with weighted criteria, scored by LLM judge. More rigorous than our qualitative rubric, and the phenomenon we predict is already documented in the benchmark's own findings.

## Tasks

Three cherry-picked tasks from PRBench:

| Task | Domain | Difficulty | Cognitive Modes Required |
|------|--------|-----------|------------------------|
| Easy | TBD | Full set | TBD — determined by architect analysis |
| Medium | TBD | Full set | TBD — determined by architect analysis |
| Hard | TBD | Hard subset | TBD — determined by architect analysis |

## PRBench Rubric Categories

PRBench evaluates across 11 dimensions. How these map to cognitive modes is part of the analysis — not assumed in advance.

Known rubric dimensions include:
- Legal/Financial Accuracy
- Process Transparency
- Risk & Ethical Disclosure
- Practical Applicability
- Completeness
- Clarity of Communication

The mapping between rubric dimensions and pipeline stages is an output of the architect analysis.

## Protocol

### Step 1: Analyse the baseline prompt
Run the prompt-architect on the standard PRBench prompting approach (zero-shot or CoT). Identify:
- Which cognitive modes the task requires
- Which combinations interfere
- Where the monolithic prompt forces premature convergence or mode mixing
- What specific interference patterns exist

This analysis determines the Tier 2 fixes and Tier 3 pipeline design.

### Step 2: Tier 1 — Baseline
Run each task with a standard zero-shot prompt. No special instructions.

### Step 3: Tier 2 — Optimised
Apply cognitive hygiene fixes identified by the architect analysis. Not predetermined — the specific interventions come from the specific interference patterns found.

### Step 4: Tier 3 — Pipeline
Design the pipeline based on the architect analysis. **The number of stages comes from the interference analysis.** The A-series ranged from 2 stages (simple toxic pair) to 5 stages (six thinking types with five interferences). The right number depends on what the analysis finds for professional reasoning tasks.

Each stage runs in a clean session with structured handoff.

### Scoring
Use PRBench's evaluation rubric and LLM judge (or our own evaluator with PRBench criteria).

Run each tier 3 times per task.

## How to Run

### Baseline run
```bash
claude --print "$(cat tasks/task-easy.md)" > baseline-runs/easy-run1.md
```

### Optimised run
```bash
claude --print --system-prompt "$(cat optimised/system-prompt.md)" "$(cat tasks/task-easy.md)" > optimised-runs/easy-run1.md
```

### Pipeline run
```bash
# Stages determined by architect analysis — see pipeline/ for the actual agent definitions
# Each stage runs in a clean session, output feeds into next stage
# Example (actual stages will vary):
claude --print "$(cat pipeline/stage1-*.md)" > pipeline-runs/easy-stage1.md
claude --print "$(cat pipeline/stage2-*.md)" > pipeline-runs/easy-stage2.md
# ... continue for however many stages the analysis calls for
# Final stage output is the scored response
cp pipeline-runs/easy-stageN.md pipeline-runs/easy-run1.md
```

### Evaluation
Score each output against the PRBench rubric using the evaluator agent or PRBench's own o4-mini judge.

## Expected Results

Based on the mode-interference thesis:
- **Tier 1** will produce competent but opaque reasoning (matching PRBench's documented finding)
- **Tier 2** will improve on dimensions the architect analysis identifies as interference-affected
- **Tier 3** improvements depend on pipeline design — but the rubric dimensions most sensitive to mode separation should show the biggest gains

The specific predictions will be written after the architect analysis, before running any tiers. Predictions first, then data.
