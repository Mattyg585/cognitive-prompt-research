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
├── .claude/
│   ├── agents/             # Predefined subagents (prompt-architect, prompt-writer, evaluator)
│   └── commands/           # Legacy slash commands (still work)
├── .github/
│   └── agents/             # Copilot Chat + CLI agents (same three agents, .agent.md format)
├── USAGE.md                # How to invoke agents from Claude Code, Copilot Chat, Copilot CLI
└── RUN-ALL.md              # Full experiment runner for all 6 experiments, any model
```

## How to Run an Experiment

**Full instructions**: `RUN-ALL.md` (all 6 experiments, works in Claude Code and Copilot)
**Agent invocation reference**: `USAGE.md`

### Quick version

**In Claude Code** — use predefined subagents (isolated context, same as ad-hoc but pre-configured):
```
Use the prompt-architect agent to analyse experiments/A1-legal-contract-review/original/SKILL.md
Use the prompt-writer agent to revise based on that analysis
Use the evaluator agent to compare outputs across all three tiers
```

**In Copilot Chat / CLI** — use @ mention:
```
@prompt-architect analyse experiments/A1-legal-contract-review/original/SKILL.md
@prompt-writer revise based on the analysis
@evaluator compare outputs
```
Copilot has handoff buttons between agents (architect → writer → evaluator). Use them — they carry structured output forward without the exploratory prose.

**Legacy slash commands** (still work in Claude Code, but run in current context — less clean):
```
/analyse-prompt    /write-prompt    /evaluate-run
```

### Key isolation rule
Each pipeline stage (Tier 3, Step 6) **must** run in a completely separate session — not just `/clear`. The pipeline's whole value is clean context at each stage boundary. Contaminating it recreates the monolithic pattern you're testing against.

### Agent files
```
.claude/agents/          ← Claude Code subagents (predefined isolated agents)
.github/agents/          ← Copilot Chat + CLI agents (same agents, different format)
toolkit/                 ← Full framework files loaded by both
.claude/commands/        ← Legacy slash commands (still work, less preferred)
```

### What "subagent" means here
A `.claude/agents/` file is a saved version of the ad-hoc subagents you spin up in conversation. Same isolation mechanism — fresh context window — just pre-configured with a system prompt and tool restrictions so you don't have to re-specify every time. Invoke with "Use the X agent to..." and Claude handles the rest.

**Handoffs are Copilot-only** (UI buttons between agents). In Claude Code, the orchestration is conversational — you pass the structured output from one agent to the next manually. Same isolation, different mechanism.

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
