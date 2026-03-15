# How to Use the Toolkit

This project has three toolkit agents — Prompt Architect, Prompt Writer, and Evaluator — that can be invoked from Claude Code or GitHub Copilot (Chat or CLI). This document covers how to invoke them from each tool.

---

## The Three Agents

| Agent | What it does | When to use it |
|---|---|---|
| **prompt-architect** | Analyses a prompt for cognitive mode conflicts, anchors, seed/lens issues | Before revising any prompt |
| **prompt-writer** | Revises prompts and designs pipelines from architect findings | After analysis; to build Tier 2 or Tier 3 |
| **evaluator** | Scores outputs blind against the rubric | After all tiers have been run |

These map directly to Steps 1–3 and Step 7 of the experiment protocol.

---

## Claude Code

### How subagents work in Claude Code

Subagents in `.claude/agents/` run in **isolated contexts** — they start fresh, without the current conversation in their window. This is important: it's the same isolation principle the research is testing. The architect runs clean, the writer runs clean, the evaluator runs clean.

Claude will sometimes delegate automatically based on your request. You can also invoke explicitly.

### Invoking

**Explicit invocation** (most reliable):
```
Use the prompt-architect agent to analyse experiments/A1-legal-contract-review/original/SKILL.md
```

```
Use the prompt-writer agent to revise the prompt at experiments/A1-legal-contract-review/original/SKILL.md based on the analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md
```

```
Use the evaluator agent to compare outputs for experiment A1. Baseline: experiments/A1-legal-contract-review/baseline-runs/. Optimised: experiments/A1-legal-contract-review/optimised-runs/. Pipeline final stage: experiments/A1-legal-contract-review/pipeline-runs/run-N/04-strategic-advisor-output.md
```

**Via legacy slash commands** (still work, but run in current context — less clean):
```
/analyse-prompt experiments/A1-legal-contract-review/original/SKILL.md
/write-prompt Revise based on analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md. Original: experiments/A1-legal-contract-review/original/SKILL.md
/evaluate-run Compare outputs for experiment A1 [paths...]
```

**Prefer the explicit "Use the X agent" form.** The legacy slash commands work but run in the current conversation context, which means the architect's output is in context when the writer runs. That's a mild version of the contamination the research documents.

### Running the full experiment sequence

For clean results, run each step as a separate agent invocation. You don't need to manually start new sessions — the subagent system handles isolation automatically when you use "Use the X agent" syntax.

For pipeline stages (Step 6), the isolation is more critical. Each pipeline stage should still be a separate top-level request or a separate Claude Code session, because pipeline stage prompts are not registered as subagents — they're one-off experiment agents.

---

## GitHub Copilot Chat (VS Code / JetBrains)

### How agents work in Copilot Chat

Custom agents in `.github/agents/` are available in the Copilot Chat panel. You switch to an agent using `@` mention. Each agent has its own system prompt and context.

### Invoking

In the Copilot Chat panel, type:

```
@prompt-architect Analyse experiments/A1-legal-contract-review/original/SKILL.md
```

```
@prompt-writer Revise the prompt at experiments/A1-legal-contract-review/original/SKILL.md based on the analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md
```

```
@evaluator Compare outputs for experiment A1. Baseline in experiments/A1-legal-contract-review/baseline-runs/, optimised in experiments/A1-legal-contract-review/optimised-runs/, pipeline final output at experiments/A1-legal-contract-review/pipeline-runs/run-1/04-strategic-advisor-output.md
```

### Using handoffs

The Copilot agents are wired with handoffs. After the `@prompt-architect` completes its analysis, a "Hand off to prompt-writer" button will appear. Click it to transition — the structured output carries over without the exploratory prose.

This is the pipeline pattern applied to the meta-level: the research tooling itself uses scoped contexts and deliberate handoffs.

---

## GitHub Copilot CLI

### How agents work in Copilot CLI

Start a Copilot CLI session:
```bash
copilot
```

Add the repository directory:
```
/add-dir /path/to/cognitive-prompt-research
```

Select your model:
```
/model
```

### Invoking agents

Copilot CLI delegates to custom agents automatically based on your request. You can also invoke explicitly:

```
@prompt-architect analyse experiments/A1-legal-contract-review/original/SKILL.md
```

```
@prompt-writer revise the prompt at experiments/A1-legal-contract-review/original/SKILL.md using the analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md
```

```
@evaluator compare outputs for experiment A1 [paths]
```

If `@agent-name` syntax doesn't work in your CLI version, use natural language and the CLI will route automatically:
```
Analyse the prompt at experiments/A1-legal-contract-review/original/SKILL.md for cognitive mode conflicts
```

### Fresh context between steps

Use `/clear` between steps to reset context. For pipeline stage runs (Step 6 in RUN-ALL.md), start a new `copilot` terminal session for each stage — `/clear` is not sufficient for pipeline stage isolation.

---

## Designing a Pipeline for a New Experiment

To add a new experiment and have the writer produce platform-ready agent files:

**In Claude Code:**
```
Use the prompt-architect agent to analyse [path/to/original/SKILL.md]. Save analysis to [path/to/analysis/].

Then use the prompt-writer agent to design a Tier 3 pipeline from that analysis. Produce agent files in both Claude Code subagent format (.claude/agents/) and Copilot agent format (.github/agents/). Save experiment-specific agents to [path/to/pipeline/] in both formats.
```

**In Copilot Chat:**
```
@prompt-architect analyse [path/to/SKILL.md]
[handoff to prompt-writer]
@prompt-writer design a pipeline from that analysis. Produce agent files in both Claude Code and Copilot formats.
```

The writer knows both formats. It will output correctly structured files with the right frontmatter for each platform.

---

## Quick Reference

```
# Claude Code — explicit subagent invocation
Use the prompt-architect agent to analyse [file]
Use the prompt-writer agent to [revise / design pipeline] based on [analysis file]
Use the evaluator agent to compare [baseline / optimised / pipeline outputs]

# Copilot Chat — @ mention
@prompt-architect [instruction]
@prompt-writer [instruction]
@evaluator [instruction]

# Copilot CLI — @ mention or natural language
@prompt-architect [instruction]
/clear   ← between steps
[new terminal session] ← between pipeline stages
```

---

## File Locations

```
.claude/agents/
├── prompt-architect.md      # Claude Code subagent
├── prompt-writer.md         # Claude Code subagent
└── evaluator.md             # Claude Code subagent

.github/agents/
├── prompt-architect.agent.md   # Copilot Chat + CLI agent
├── prompt-writer.agent.md      # Copilot Chat + CLI agent
└── evaluator.agent.md          # Copilot Chat + CLI agent

.claude/commands/               # Legacy slash commands (still work)
├── analyse-prompt.md
├── write-prompt.md
└── evaluate-run.md

toolkit/
├── prompt-architect-agent.md   # Full framework loaded by both agent formats
├── prompt-writer-agent.md      # Full framework loaded by both agent formats
├── cognitive-stance-reference.md
└── cognitive-science-research.md
```
