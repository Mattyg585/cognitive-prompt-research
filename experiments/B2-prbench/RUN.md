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
| Easy | TBD | Full set | TBD |
| Medium | TBD | Full set | TBD |
| Hard | TBD | Hard subset | TBD |

## PRBench Rubric Categories

PRBench evaluates across 11 dimensions. These map to cognitive modes:

| Rubric Category | Cognitive Mode | Pipeline Stage |
|----------------|---------------|---------------|
| Legal/Financial Accuracy | Convergent/Analytical | Analysis |
| Process Transparency | Meta-cognitive | All (but especially investigation) |
| Risk & Ethical Disclosure | Evaluative/Judgmental | Evaluation |
| Practical Applicability | Convergent/Synthetic | Synthesis |
| Completeness | Investigative/Divergent | Investigation |
| Clarity of Communication | Convergent/Expressive | Communication |

The rubric should reward pipeline approaches that make reasoning explicit at each stage.

## Protocol

### Tier 1: Baseline
Run each task with a standard zero-shot prompt. No special instructions.

### Tier 2: Optimised
Same single prompt with cognitive hygiene:
- Explicit scope boundaries between investigation and judgment
- Lenses instead of seeds for the investigation phase
- Ordered workflow: understand → investigate → analyse → synthesise → communicate
- No numeric anchors constraining depth

### Tier 3: Pipeline
Split into separate stages:
1. **Investigation agent** — understand the question, identify what information/frameworks are relevant, map the problem space
2. **Analysis agent** — given the investigation, apply domain knowledge, reason through the specifics
3. **Synthesis agent** — given the analysis, form a coherent judgment/recommendation
4. **Communication agent** — given the synthesis, produce a clear, well-structured response appropriate for a professional audience

Each stage runs in a clean session with structured handoff.

### Scoring
Use PRBench's evaluation rubric and LLM judge (or our own evaluator with PRBench criteria).

Run each tier 3 times per task.

## How to Run

### Baseline run
```bash
# In Claude Code
claude --print "$(cat tasks/task-easy.md)" > baseline-runs/easy-run1.md
```

### Optimised run
```bash
claude --print --system-prompt "$(cat optimised/system-prompt.md)" "$(cat tasks/task-easy.md)" > optimised-runs/easy-run1.md
```

### Pipeline run
```bash
# Stage 1: Investigation (clean session)
claude --print "$(cat pipeline/stage1-investigate.md)" > pipeline-runs/easy-investigation.md

# Stage 2: Analysis (clean session, receives investigation output)
claude --print "$(cat pipeline/stage2-analyse.md)" > pipeline-runs/easy-analysis.md

# Stage 3: Synthesis (clean session, receives analysis output)
claude --print "$(cat pipeline/stage3-synthesise.md)" > pipeline-runs/easy-synthesis.md

# Stage 4: Communication (clean session, receives synthesis output)
claude --print "$(cat pipeline/stage4-communicate.md)" > pipeline-runs/easy-run1.md
```

### Evaluation
Score each output against the PRBench rubric using the evaluator agent or PRBench's own o4-mini judge.

## Expected Results

Based on the mode-interference thesis:
- **Tier 1** will produce competent but opaque reasoning (matching PRBench's documented finding)
- **Tier 2** will improve process transparency and completeness through better cognitive hygiene
- **Tier 3** will produce qualitatively different reasoning — each stage's output will be deeper because the model wasn't trying to do everything at once. The investigation will be more thorough, the analysis more rigorous, the synthesis more coherent, and the communication clearer.

The rubric dimensions most likely to show improvement: Process Transparency, Completeness, Clarity of Communication.
