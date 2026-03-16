# B1: SWE-bench — Can Cognitive Mode Separation Improve Code Agent Performance?

## Background

SWE-bench is the industry-standard benchmark for evaluating AI coding agents on real GitHub issues. Models receive an issue description and must produce a patch that passes gold tests.

**Why this matters for our research**: The standard SWE-bench prompt asks models to simultaneously investigate a codebase, diagnose a bug, plan a fix, implement it, and verify it — five incompatible cognitive modes in one context. Scaffold/prompt differences account for 10-25 percentage points on the same model. Arize AI already showed +10% from CLAUDE.md optimization alone.

**Key difference from A-series**: Scoring is objective (pass/fail on gold tests), not qualitative.

## Tasks

Three cherry-picked tasks from SWE-bench Verified:

| Task | Repo | Difficulty | Rationale |
|------|------|-----------|-----------|
| Easy | TBD | High solve rate | Calibration — all tiers should pass |
| Medium | TBD | Medium solve rate | The interesting middle — prompt quality should matter here |
| Hard | TBD | Low solve rate | Stretch — does pipeline unlock what monolithic can't? |

## Protocol

### Tier 1: Baseline
Run each task in Claude Code with the standard SWE-bench prompt (from Anthropic's scaffold). No CLAUDE.md, no special instructions.

### Tier 2: Optimised
Same prompt structure with cognitive hygiene applied:
- Scope boundaries between investigation and implementation
- Explicit mode transitions ("you are now diagnosing, not exploring")
- Seeds replaced with lenses where appropriate

### Tier 3: Pipeline
Split into separate stages via CLAUDE.md instructions:
1. **Investigation agent** — explore the codebase, understand the issue, map relevant files
2. **Diagnosis agent** — given the investigation output, identify root cause
3. **Implementation agent** — given the diagnosis, produce a minimal fix
4. **Verification agent** — given the fix, test and validate

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
# Stage 1: Investigation (clean session)
claude --print "$(cat ../pipeline/stage1-investigate.md)" > ../pipeline-runs/easy-investigation.md

# Stage 2: Diagnosis (clean session)
claude --print "$(cat ../pipeline/stage2-diagnose.md)" > ../pipeline-runs/easy-diagnosis.md

# Stage 3: Implementation (clean session)
claude "$(cat ../pipeline/stage3-implement.md)"
git diff > ../pipeline-runs/easy-run1.patch

# Stage 4: Verification (clean session)
claude "$(cat ../pipeline/stage4-verify.md)"
```

### Evaluation
```bash
# Apply patch and run gold tests
git apply ../baseline-runs/easy-run1.patch
python -m pytest <test_file> -x
```
