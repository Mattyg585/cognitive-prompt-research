# Quick Start: Evaluate Your Own Prompts

You have a prompt (or an agent with skills, or a pipeline). You want to know if it's fighting itself and what to do about it.

---

## 1. Analyse

Point the architect agent at your prompt:

**Claude Code:**
```
Use the prompt-architect agent to analyse path/to/your/prompt.md
```

**GitHub Copilot:**
```
@prompt-architect analyse path/to/your/prompt.md
```

The architect reads your prompt and tells you:
- What types of thinking it requires and how they relate
- Where modes interfere (with specific line references and mechanisms)
- What to check for in the output (diagnostic signals)
- What to do about it — both prompt-level fixes and pipeline reconstruction

### Agents with skills or sub-agents

If your prompt loads skills at runtime (Claude Code skills, Copilot agents, MCP tools), tell the architect about them:

```
Use the prompt-architect agent to analyse my-agent.md as an agent with skills.
It loads these skills at runtime:
- /investigate at .claude/commands/investigate.md
- /evaluate at .claude/commands/evaluate.md
```

The architect checks whether skill combinations create mode conflicts that don't exist in any single file — they emerge when files combine at runtime.

### Pipelines

If you have multiple agents that work together:

```
Use the prompt-architect agent to analyse this pipeline:
1. Agent 1: path/to/agent-1.md
2. Agent 2: path/to/agent-2.md
3. Agent 3: path/to/agent-3.md
```

The architect analyses each prompt individually, then zooms out to check sequencing, handoff contamination, and missing compression stages.

---

## 2. Fix

Two paths depending on what the analysis found:

### Prompt-level fixes (Tier 2)

For interference that can be addressed within the existing prompt:

```
Use the prompt-writer agent to revise path/to/your/prompt.md based on the analysis
```

The writer implements the fixes — removing anchors, replacing seeds with lenses, adding scope boundaries — and documents what changed and why.

### Pipeline reconstruction (Tier 3)

For fundamental mode conflicts where the single-prompt architecture is the ceiling:

```
Use the prompt-writer agent to design a pipeline reconstruction for path/to/your/prompt.md based on the analysis
```

The writer designs a multi-agent pipeline — one agent per thinking type, structured handoffs between stages, a handoff spec documenting what crosses and what gets stripped.

---

## 3. Compare (optional but recommended)

Run your original prompt and the revised version(s) against the same input. Use the evaluator for blind comparison:

```
Use the evaluator agent to compare the outputs in output-a.md and output-b.md
```

The evaluator scores both without knowing which is which, using a 5-dimension rubric (depth, specificity, natural variation, completeness, audience awareness).

---

## What the agents look for

The core patterns that degrade output:

| Pattern | What happens | Example |
|---------|-------------|---------|
| **Investigation + Evaluation** | Evaluation pre-filters investigation. Only finds things it can already classify. | "Read the contract and classify each clause as GREEN/YELLOW/RED" |
| **Investigation + Generation** | Only investigates things it can fix. Investigation becomes a funnel for recommendations. | "Identify problems and recommend solutions" |
| **Numeric anchors** | Output gravitates to the midpoint regardless of input. | "Find 3-5 issues" → always finds 4 |
| **Seeds in divergent work** | Model anchors to prescribed findings and stops. | "Look for: missing MFA, weak passwords, orphaned accounts..." |
| **Synthesis + QA in same context** | QA posture suppresses exploratory synthesis. Output is competent but predictable. | "Quality-check the investigation, then synthesise findings" |
| **Skills contamination** | Loaded skills carry incompatible cognitive postures into the same context. | Investigation agent + evaluation skill loaded simultaneously |

Not every prompt has these problems. Not every instance needs fixing. The architect tells you which patterns are present and whether they're likely to matter.

---

## What you don't need

- You don't need to understand cognitive science or linguistics
- You don't need to restructure everything as a pipeline
- You don't need to run the full experiment protocol (that's in RUN-ALL.md for research purposes)
- You don't need to use Claude — the principles apply to any LLM, though the agents currently run in Claude Code and Copilot

Point the architect at your prompt. Read what it says. Decide if the fixes are worth it for your use case. That's it.
