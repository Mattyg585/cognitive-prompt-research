# Cognitive Prompt Research

## What This Is

An empirical study testing whether the monolithic-prompt-plus-skills paradigm is fundamentally flawed for complex tasks — and whether smaller, cognitively scoped pipelines produce better output.

**The core insight**: Language carries cognitive mode. LLMs learned the language patterns that different types of human thinking produce. Mixing incompatible patterns (from incompatible cognitive modes) in the same context creates distributional interference that degrades output. The degradation is invisible — the output looks fine. The gap only appears when you separate the modes and compare.

**Read `research-foundations.md` for the full theoretical framework.**

## The Three-Tier Experiment Model

Each experiment tests three levels of intervention:

1. **Original** — the prompt as-is (baseline)
2. **Optimised** — same structure, better cognitive hygiene (remove anchors, replace seeds with lenses, add scope boundaries)
3. **Pipeline reconstruction** — split into multiple agents with clean contexts and deliberate handoffs

If Tier 2 improves incrementally and Tier 3 produces a qualitative leap, the finding is: the monolithic prompt is the ceiling, not the floor.

## Repo Structure

```
├── research-foundations.md     # Theoretical framework, the cognitive stack, evidence so far
├── experiment-design.md        # Protocol, experiment portfolio, methodology
├── toolkit/                    # Analysis and writing agents
│   ├── prompt-architect-agent.md    # Analyses prompts for mode interference
│   ├── prompt-writer-agent.md       # Writes/revises prompts with mode principles
│   ├── cognitive-stance-reference.md # The theory — loaded by both agents
│   └── cognitive-science-research.md # Research citations and grounding
├── evaluation/                 # Scoring tools
│   ├── rubric.md               # 5-dimension evaluation rubric
│   └── evaluator-prompt.md     # Blind LLM-as-judge prompt
├── experiments/                # One folder per experiment
│   └── A1-legal-contract-review/
│       ├── original/           # The monolithic prompt
│       ├── optimised/          # Tier 2 revision
│       ├── pipeline/           # Tier 3 pipeline agents + handoff spec
│       ├── test-material/      # Input data for runs
│       ├── baseline-runs/      # Outputs from original
│       ├── optimised-runs/     # Outputs from Tier 2
│       ├── pipeline-runs/      # Outputs from Tier 3
│       └── evaluation/         # Blind comparison results
├── reference/                  # Context from the original project (read-only)
│   ├── blogs/                  # Published blog posts about the CA pipeline
│   ├── v3-v4-comparison/       # The V3→V4 prompts and outputs (strongest evidence)
│   └── graph-tool-pipeline/    # Full production prompt set from the CA pipeline
└── .claude/commands/           # Slash commands for running experiments
```

## How to Run an Experiment

### 1. Analyse the original prompt
```
/analyse-prompt experiments/A1-legal-contract-review/original/SKILL.md
```

### 2. Create Tier 2 (optimised) version
```
/write-prompt Revise based on analysis findings. Original: experiments/A1-legal-contract-review/original/SKILL.md
```

### 3. Create Tier 3 (pipeline) version
Design a pipeline that splits the prompt into cognitively scoped agents. Save each agent as a separate file in `pipeline/` with a `handoff-spec.md` describing what crosses between stages.

### 4. Run baselines and comparisons
Run each version against the same test material. Save outputs in the corresponding `*-runs/` directories.

### 5. Evaluate blind
```
/evaluate-run Compare outputs for experiment A1
```

## Key Conventions

- **Document as you go.** Raw observations over polished narratives.
- **Negative results are results.** If optimisation doesn't help or hurts, document why.
- **Three tiers, not two.** Always test pipeline reconstruction, not just prompt optimisation.
- **No numeric anchors in prompts.** Practice what we test.
- **Natural variation is healthy.** Output should vary with input complexity.

## Key Concepts (Quick Reference)

- **Cognitive stack**: Epistemic stance → Intent → Expertise/posture → Cognitive mode → Register → Language patterns → Tokens. Higher interventions cascade further.
- **Mode interference**: Investigation + evaluation is the classic toxic pair. The model pre-filters, only finding things it can already classify.
- **Seeds vs lenses**: Seeds (content prescription) constrain divergent work. Lenses (structural guidance) open it. Seeds are fine for convergent work.
- **Trust chain**: In a pipeline, each layer's cognitive quality cascades to the layers above and below it.
- **Good output hides great output**: Mode contamination produces competent results that prevent you from seeing what's possible. The gap is invisible until you split and compare.
