# B1: SWE-bench — Can Cognitive Mode Separation Improve Code Agent Performance?

## Background

SWE-bench is the industry-standard benchmark for evaluating AI coding agents on real GitHub issues. Models receive an issue description and must produce a patch that passes gold tests.

**Why this matters for our research**: The standard SWE-bench prompt asks models to simultaneously investigate a codebase, diagnose a bug, plan a fix, implement it, and verify it — multiple cognitive modes crammed into one context. Scaffold/prompt differences account for 10-25 percentage points on the same model. Arize AI already showed +10% from CLAUDE.md optimization alone.

**Key difference from A-series**: Scoring is objective (pass/fail on gold tests), not qualitative.

## Tasks

Three cherry-picked tasks from SWE-bench Verified:

| Task | Repo | Difficulty | Rationale |
|------|------|-----------|-----------|
| Easy | TBD | High solve rate | Calibration — all tiers should pass |
| Medium | TBD | Medium solve rate | The interesting middle — prompt quality should matter here |
| Hard | TBD | Low solve rate | Stretch — does pipeline unlock what monolithic can't? |

## Protocol

### Step 1: Analyse the baseline prompt
Run the prompt-architect on the standard SWE-bench prompt. Identify:
- Which cognitive modes are present
- Which combinations interfere (toxic pairs)
- Where numeric anchors or seeds constrain
- What the actual interference patterns are

This analysis determines everything that follows.

### Step 2: Tier 1 — Baseline
Run each task in Claude Code with the standard SWE-bench prompt (from Anthropic's scaffold). No CLAUDE.md, no special instructions.

### Step 3: Tier 2 — Optimised
Apply cognitive hygiene fixes identified by the architect analysis. The specific fixes depend on what the analysis finds — not predetermined. Likely candidates:
- Scope boundaries between incompatible modes
- Explicit mode transitions
- Seeds replaced with lenses where appropriate
- Reordering to prevent premature convergence

### Step 4: Tier 3 — Pipeline
Design the pipeline based on the architect analysis. **The number of stages and their boundaries come from the interference analysis, not from a template.** The A-series ranged from 2 stages (A5-debug) to 5 stages (A6-secops) — the right number depends on how many toxic pairs exist and which modes can safely coexist.

Each stage runs in a clean Claude Code session with structured handoff.

### Scoring
Binary pass/fail: does the generated patch pass the gold test suite?

Run each tier 3 times per task to account for non-determinism.

## How to Run

### Prerequisites
- Clone the target repo at the specified commit
- Have the gold test patch available for verification

### Baseline run
```bash
cd /path/to/cloned-repo
# Start Claude Code with the task prompt
claude "$(cat ../tasks/task-easy.md)"
# Capture the diff
git diff > ../baseline-runs/easy-run1.patch
```

### Optimised run
```bash
cd /path/to/cloned-repo
# Reset to base commit
git checkout <base_commit>
# Copy in the optimised CLAUDE.md
cp ../optimised/CLAUDE.md .
claude "$(cat ../tasks/task-easy.md)"
git diff > ../optimised-runs/easy-run1.patch
```

### Pipeline run
```bash
# Stages determined by architect analysis — see pipeline/ for the actual agent definitions
# Each stage runs in a clean session
# Example (actual stages will vary):
claude --print "$(cat ../pipeline/stage1-*.md)" > ../pipeline-runs/easy-stage1.md
claude --print "$(cat ../pipeline/stage2-*.md)" > ../pipeline-runs/easy-stage2.md
# ... continue for however many stages the analysis calls for
# Final stage produces the patch
git diff > ../pipeline-runs/easy-run1.patch
```

### Evaluation
```bash
# Apply patch and run gold tests
git apply ../baseline-runs/easy-run1.patch
python -m pytest <test_file> -x
```
