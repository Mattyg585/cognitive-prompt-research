# How to Use the Toolkit

This project has three toolkit agents — Prompt Excavator, Prompt Architect, and Prompt Writer — that can be invoked from Claude Code or GitHub Copilot (Chat or CLI). This document covers how to invoke them from each tool.

---

## The Three Agents

| Agent | What it does | When to use it |
|---|---|---|
| **prompt-excavator** | Helps articulate what you need from AI — surfaces tacit knowledge, judgment calls, edge cases | Before you have a prompt; when starting from a vague idea |
| **prompt-architect** | Analyses a prompt for cognitive mode conflicts, anchors, seed/lens issues | Before revising any prompt |
| **prompt-writer** | Revises prompts and designs pipelines from architect findings | After analysis; to build Tier 2 or Tier 3 |

The natural flow: **Excavate** (figure out what you need) → **Architect** (analyse the prompt) → **Writer** (build or revise). You don't always need all three — if you already have a prompt, start with the architect. If you already know what you need, start with the writer. The excavator is for when you're starting from scratch or a vague idea.

Analyse, revise, run, compare. You're the domain expert — you'll know if the output is better.

> **For research replication:** An evaluator agent and rubric also exist (`evaluation/`, `.claude/agents/evaluator.md`) for the formal blind comparison protocol. See `RUN-ALL.md` for the full experiment methodology.

---

## Claude Code

### How subagents work in Claude Code

Subagents in `.claude/agents/` run in **isolated contexts** — they start fresh, without the current conversation in their window. This is important: it's the same isolation principle the research is testing. The architect runs clean, the writer runs clean, the evaluator runs clean.

Claude will sometimes delegate automatically based on your request. You can also invoke explicitly.

### Invoking

**Explicit invocation** (most reliable):
```
Use the prompt-excavator agent to help me define what I need for a quoting automation system
```

```
Use the prompt-excavator agent in primer mode — I'm meeting a builder about their quoting process
```

```
Use the prompt-architect agent to analyse experiments/A1-legal-contract-review/original/SKILL.md
```

```
Use the prompt-writer agent to revise the prompt at experiments/A1-legal-contract-review/original/SKILL.md based on the analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md
```

**Via legacy slash commands** (still work, but run in current context — less clean):
```
/analyse-prompt experiments/A1-legal-contract-review/original/SKILL.md
/write-prompt Revise based on analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md. Original: experiments/A1-legal-contract-review/original/SKILL.md
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
@prompt-excavator Help me define what I need for a quoting automation system
```

```
@prompt-architect Analyse experiments/A1-legal-contract-review/original/SKILL.md
```

```
@prompt-writer Revise the prompt at experiments/A1-legal-contract-review/original/SKILL.md based on the analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md
```

### Using handoffs

The Copilot agents are wired with handoffs. After `@prompt-excavator` produces a structured brief, a "Hand off to prompt-writer" button will appear. After `@prompt-architect` completes its analysis, a "Hand off to prompt-writer" button will appear. Click it to transition — the structured output carries over without the exploratory prose.

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
@prompt-excavator help me define what I need for an invoice processing system
```

```
@prompt-architect analyse experiments/A1-legal-contract-review/original/SKILL.md
```

```
@prompt-writer revise the prompt at experiments/A1-legal-contract-review/original/SKILL.md using the analysis at experiments/A1-legal-contract-review/analysis/prompt-architect-analysis.md
```

If `@agent-name` syntax doesn't work in your CLI version, use natural language and the CLI will route automatically:
```
Help me figure out what I need for an invoice processing automation
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
Use the prompt-excavator agent to [describe what you need / prepare for a meeting]
Use the prompt-architect agent to analyse [file]
Use the prompt-writer agent to [revise / design pipeline] based on [analysis file]

# Copilot Chat — @ mention
@prompt-excavator [describe what you need]
@prompt-architect [instruction]
@prompt-writer [instruction]

# Copilot CLI — @ mention or natural language
@prompt-excavator [describe what you need]
@prompt-architect [instruction]
/clear   ← between steps
[new terminal session] ← between pipeline stages
```

---

## File Locations

```
.claude/agents/
├── prompt-excavator.md     # Claude Code subagent
├── prompt-architect.md      # Claude Code subagent
├── prompt-writer.md         # Claude Code subagent
└── evaluator.md             # Claude Code subagent (research use)

.github/agents/
├── prompt-excavator.agent.md  # Copilot Chat + CLI agent
├── prompt-architect.agent.md   # Copilot Chat + CLI agent
├── prompt-writer.agent.md      # Copilot Chat + CLI agent
└── evaluator.agent.md          # Copilot Chat + CLI agent (research use)

.claude/commands/               # Legacy slash commands (still work)
├── analyse-prompt.md
├── write-prompt.md
└── evaluate-run.md             # Research use

toolkit/
├── prompt-excavator-agent.md   # Full framework loaded by excavator agents
├── prompt-architect-agent.md   # Full framework loaded by architect agents
├── prompt-writer-agent.md      # Full framework loaded by writer agents
├── cognitive-stance-reference.md
├── cognitive-science-research.md
├── excavation-research-elicitation.md    # Research: CTA, MI, design thinking
├── excavation-research-conversational.md # Research: dialogue design, gap detection
└── excavation-research-bridging.md       # Research: task decomposition, triage
```
