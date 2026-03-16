# Experiment Design

## The Question

**Is the monolithic-prompt-plus-skills paradigm fundamentally flawed for complex tasks?**

The industry trend is toward bigger, more comprehensive single prompts. Skills, plugins, and progressive loading make prompts effectively longer without hitting token limits. The assumption: more context = better output.

Our hypothesis: for tasks that require incompatible types of thinking, that assumption is backwards. More context means more cognitive mode mixing. More instructions means more interference. Skills loaded on demand contaminate the context with whatever cognitive posture they carry. And the contamination is invisible because the output still looks fine.

The alternative: smaller, cognitively scoped agents in a pipeline, each doing one type of thinking in a clean context, with structured handoffs that strip cognitive residue between stages.

See `research-foundations.md` for the full theoretical framework.

---

## Three-Tier Testing

Each experiment tests three levels of intervention:

### Tier 1: Original (Baseline)
The prompt as-is. Run it, capture output, score it.

### Tier 2: Optimised (Prompt-Level Fixes)
Same prompt structure, better cognitive hygiene:
- Remove numeric anchors
- Replace seeds with lenses (for divergent work)
- Add scope boundaries ("you are investigating, not assessing")
- Reorder sections so exploration precedes judgment
- Soften fixed category lists and template structures

Tests: can you improve output by fixing interference *within* a single prompt?

### Tier 3: Pipeline Reconstruction
Split the prompt into multiple agents, each doing one type of thinking:
- Identify what types of thinking the prompt requires
- Separate incompatible types into different agents
- Design structured handoffs (what crosses, in what form, what gets stripped)
- Each agent runs in a clean context

Tests: is the single-prompt architecture itself the ceiling?

**The key comparison**: If Tier 2 improves incrementally and Tier 3 produces a qualitative shift, the monolithic prompt is the bottleneck.

---

## Protocol

Keep it simple. Don't let methodology become overhead.

### For each experiment:

1. **Analyse** — Run `/analyse-prompt` on the original. Document what it finds.
2. **Predict** — Before running anything, write down what you expect to improve and why.
3. **Baseline** — Run the original prompt 3 times against test material. Save outputs.
4. **Optimise** — Create Tier 2 version using `/write-prompt`. Document changes.
5. **Reconstruct** — Design Tier 3 pipeline. Document the agent split and handoff design.
6. **Compare** — Run Tier 2 and Tier 3 each 3 times against same test material. Save outputs.
7. **Evaluate** — Blind evaluation using `/evaluate-run`. Score all three tiers.
8. **Reflect** — What happened? Did predictions hold? What does this tell us?

### Running a pipeline (Tier 3)

Each pipeline agent is a markdown prompt file. Run them in separate sessions (clean context between stages). The handoff is manual: Agent 1's output gets saved to a file, relevant structured output is loaded into Agent 2's context. No orchestration framework needed.

This is the purest test — zero contamination between stages. Automation can come later.

### Controls

- **Multiple runs**: 3 runs per version per tier to account for non-determinism
- **Same test material**: All tiers run against identical input
- **Blind evaluation**: The evaluator doesn't know which output came from which tier

---

## Evaluation

### Qualitative rubric (all experiments)

| Dimension | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
|-----------|----------|---------------|----------------|
| **Depth** | Surface-level, obvious only | Covers expected ground | Surprising insights, follows threads |
| **Specificity** | Generic, could apply to anything | Grounded in actual input | Precise, every observation traceable to evidence |
| **Natural variation** | Identical across runs | Some variation | Output complexity matches input complexity |
| **Completeness** | Misses obvious things | Covers major points | Comprehensive, appropriately weighted |
| **Audience awareness** | Wrong register | Acceptable | Models the audience's perspective |

### LLM-as-judge

- Separate evaluator (not the model that generated output)
- Blind — evaluator doesn't know which tier produced which output
- Uses the rubric, provides scores + reasoning
- See `evaluation/evaluator-prompt.md`

### What to watch for beyond the rubric

- **Register shifts** — Does Tier 3 produce qualitatively different *tone*, not just better scores? (The V3→V4 register shift from "competent audit" to "consultant who understands the room" was the strongest signal.)
- **Emergent findings** — Does Tier 3 find things Tier 1 and 2 missed entirely?
- **Zero losses** — Does Tier 3 lose anything that Tier 1 found? (V3→V4 had zero losses.)

---

## Experiment Portfolio

### Primary: Anthropic Knowledge Work Plugins

Same authorship, same quality bar — controlled comparison across domains.

Source: [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

| # | Domain | Prompt | Expected interference | Priority |
|---|--------|--------|----------------------|----------|
| A1 | Legal | `/review-contract` | Investigation + evaluation + generation fusion; 12 fixed clause categories; "3-5 Key Findings" anchor | **Start here** |
| A2 | Marketing | `/content-creation` | Template anchors suppress creative generation ("3-5 sections", "3-4 value propositions") | High |
| A3 | HR | `/performance-review` | Mostly template generation — may show limited improvement (boundary case) | Medium |
| A4 | Design | `/research-synthesis` | Synthesis constrained by fixed output structure | Medium |
| A5 | Engineering | `/debug` | Clean 4-step sequence — may already be well-structured (calibration) | Medium |
| A6 | SecOps | `/incident-response` | 4-mode mixing; "5 Whys" forces exactly 5 depth levels | High |

### B-Series: Benchmark Validation

Can cognitive mode separation move the needle on established benchmarks? The A-series tested knowledge-worker plugins with qualitative scoring. The B-series tests the same principles against benchmarks with objective/expert-rubric scoring.

**Key difference**: A-series asks "is the output better?" (subjective). B-series asks "does it pass?" or "does it score higher on expert rubrics?" (objective).

| # | Benchmark | Domain | Scoring | Why |
|---|-----------|--------|---------|-----|
| B1 | SWE-bench Verified | Code (real GitHub issues) | Pass/fail on gold tests | Industry-standard coding benchmark; scaffold differences account for 10-25pp; Arize showed +10% from CLAUDE.md alone |
| B2 | PRBench (Scale AI) | Law & Finance | Expert rubric (11 dimensions) | Top models at 37-39% on hard set; benchmark's own paper documents "correct conclusions through opaque reasoning" — our exact phenomenon |

**Prior art**: Arize AI achieved +10% on SWE-bench via automated prompt optimization. Aider's Architect mode (cognitive split: reasoning vs editing) produced SOTA results. Agentless (pipeline: localize → repair → validate) outperformed agent approaches at 1/10th the cost. These teams accidentally discovered what our theory predicts — nobody has done it systematically.

### Future: Independent Validation

| # | Domain | Source | Why |
|---|--------|--------|-----|
| O1 | Code review | PR-Agent (Qodo) | Real-world, high-usage tool with investigation + evaluation mixing |
| O2 | Vulnerability discovery | Vulnhuntr | Multi-step investigation → synthesis → evaluation |
| C1 | Creative writing | TBD | Boundary test — where mode separation might hurt |

### Priority Order

1. **A1 (Legal)** — richest test case, genuine interleaving of investigation + evaluation + generation (DONE)
2. **A6 (SecOps)** — 4-mode mixing, numeric anchor ("5 Whys"), adjacent to original project domain (DONE)
3. **A2 (Marketing)** — creative generation domain, tests template anchor suppression (DONE)
4. **B1 (SWE-bench)** — objective pass/fail scoring on industry benchmark
5. **B2 (PRBench)** — expert rubric scoring on professional reasoning benchmark
6. **C1 (Creative)** — boundary test, most theoretically interesting
7. Remaining as capacity allows

---

## When Things Don't Work

| What happens | What it means | What to do |
|-------------|--------------|-----------|
| Tier 2 improves but Tier 3 doesn't add value | Pipeline overhead isn't worth it for this type of task. Prompt-level fixes are sufficient. | Document the boundary — which task types need pipelines vs prompt fixes? |
| Tier 3 improves analytical prompts but not creative ones | Boundary condition found. Mode separation has domain limits. | Look at creativity research for alternative frameworks. |
| "More detail" control performs as well as mode separation | The value is in prompt expansion, not mode principles. | Honest finding. Revise claims. |
| Everything improves everywhere | Too good to be true. Check for confirmation bias. | Add more negative controls. Tighten evaluation. |
| Analysis finds interference but neither tier improves output | Detection right, intervention wrong. | Go back to the theory — is there a different mechanism? |

---

## What Success Looks Like

**Strong result**: Tier 3 (pipeline) produces qualitatively different output from Tier 1 (original) across multiple domains — not just better scores, but register shifts, emergent findings, and zero losses. Tier 2 (optimised) provides incremental improvement. The pattern is consistent: monolithic prompts are the ceiling for complex tasks.

**Equally valuable**: The pattern holds for analytical work but not creative work. Clear boundary condition identified.

**Honest negative**: Improvements are indistinguishable from simply adding more detail. The mechanism isn't mode separation — it's prompt expansion. Still publishable, still valuable.

**The worst outcome isn't failure — it's ambiguity.** If we can't tell whether changes helped, the evaluation methodology needs work.
