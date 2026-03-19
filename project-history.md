# Project History

How this research project came to exist — pieced together from the git history, blog posts, reference materials, and the code itself.

---

## The Origin: A Conditional Access Tool (mid-2024 to early 2025)

It started as a practical problem. Matt Graham — a Microsoft systems and infrastructure engineer with 17 years of experience and no AI background — wanted to rebuild a Conditional Access policy management tool as AI-first. Not AI-assisted. AI-first.

He had an existing gitops-style tool (JSON config files, drift detection, Graph API deployment) that worked but was too hard for most people to use. The question was: what happens if you rethink it from scratch with AI at the centre?

The hard question — "can the AI actually do the work?" — was answered in the first week. Claude Code with the Graph API could pull down policies, compare configurations, explain differences, and deploy changes. The tool itself was plumbing.

But somewhere along the way, the project shifted. Instead of building the tool, Matt started pulling on a different thread: could AI actually *reason* about the complex, overlapping security configurations that make senior consultants reach for spreadsheets? 55 interdependent Conditional Access policies. That's the kind of thing humans struggle to hold in their heads.

He kept following that thread because progress never stopped and there were always hints at more.

---

## Seven Months of Wrong Turns (mid-2024 to Feb 2025)

The journey to a working system went through seven major iterations over roughly seven months of evenings and weekends:

1. **First attempt**: "Analyse these policies against Zero Trust." Hit the context window limit immediately — 55 CA policies blow through a context window in minutes.

2. **The hallucination disaster**: Solved the context problem with a Postgres database, got a >90% alignment score that looked fantastic — until he checked the working. The model had retrieved a subset of policies and inferred patterns from what it had. Impressive cheating.

3. **Three-layer architecture**: "How would I actually do this as a consultant?" led to per-policy analysis → cross-policy patterns → framework mapping. Genuine progress, but technically accurate output that was practically useless.

4. **Over-engineering phase**: Split into scanner + investigator, then four specialised agents with an orchestrator (semantic clustering, technical controls, misalignment detection, deep-dives). Technically impressive. Output was impossible to digest — organised around analytical decomposition, not around how a consultant would use it.

5. **The CTA breakthrough**: Stuck and venting to Claude, which suggested Cognitive Task Analysis — a methodology for extracting expert tacit knowledge. Matt ran sessions describing how he actually reviews CA policies: he thinks in *stories* ("What's the MFA story? What's the guest access story?"), not clusters. He produces handover documentation, not analytical artifacts. None of this was in his prompts. Four agents and an orchestrator became three agents with no orchestrator. The output changed immediately.

6. **The seeds crisis**: While writing the first blog post, Matt found seeded data in his prompts — expected findings and numbers he'd written months earlier and forgotten. He thought it unravelled everything. Working through it led to the convergent/divergent distinction and the seeds-vs-lenses framework.

7. **The V3→V4 experiment**: Removed a QA section from the synthesis prompt (making it *smaller*). Output went from 8 findings to 12, four entirely new themes, zero losses, register shift from "competent audit" to "consultant who understands the room." 70% of the context window was unused. This was not a capacity problem.

---

## The Insight That Changed Everything

The key realisation: **the stages weren't separated by token capacity — they were separated by type of thinking.** Every time different types of work shared the same context, the output got worse in ways that were hard to pin down.

This crystallised into the convergent/divergent framework:
- **Convergent** work compresses: classification, extraction, verification, pinning things down
- **Divergent** work explores: investigation, synthesis, following threads, connecting dots

And the critical observation: when these share a context, convergent dominates. The model pre-filters, only finding things it can already classify. The output looks fine — good enough that you'd never know it could be better. **Good output hides great output.**

The single word "observation" vs "finding" at the epistemic layer changed output from catastrophising to exploratory. Language carries cognitive mode.

---

## The Blog Series (18 Feb – 5 Mar 2026)

Matt wrote four blog posts documenting what he'd learned:

1. **"I Built an AI Tool That Does My Job Better Than Me"** (18 Feb 2026) — The story of what was built and the moment it produced output that scared him more than it impressed him.

2. **"Why Good Prompting Wasn't Enough"** (4 Mar 2026) — The seven months of wrong turns. The CTA breakthrough. The seeds crisis and the convergent/divergent distinction.

3. **"Context Carries Cognitive Mode"** (5 Mar 2026) — The V3→V4 evidence. The claim that separating cognitive modes improves output independently of token capacity.

4. **"Evidence & Methods"** (5 Mar 2026) — Companion post with full experiment designs, version comparisons, and claims tables.

---

## From One Project to a Research Repo (14 Mar 2026)

All the evidence came from one practitioner's project in one domain (Microsoft Conditional Access policy analysis). The question was: does this generalise?

On 14 March 2026, Matt created this repository to find out. The whole thing was co-authored with Claude (every commit carries `Co-Authored-By: Claude Opus 4.6`). What follows is the story of that day, reconstructed from the git log.

### The framework drops (13:59)

The initial commit contained the full research framework — not just scaffolding, but the theoretical model, experiment protocol, evaluation rubric, toolkit agents, and six experiment folders already identified. The `research-foundations.md` laid out the cognitive stack, mode interference, trust chains. The `experiment-design.md` specified the three-tier protocol. The toolkit agents (prompt-architect and prompt-writer) were grounded in cognitive science research citations. The experiments were sourced from Anthropic's own `knowledge-work-plugins` — same authorship, same quality bar, different domains. This wasn't a "let's figure it out as we go" repo. The framework was already crystallised from the blog series.

### A1: Legal contract review — the first full test (14:02–18:18)

A1 was the flagship experiment. The prompt architect analysed the original `/review-contract` prompt and found investigation + evaluation fusion, 54 seeded elements, and numeric anchors. Tier 2 optimised it. Tier 3 split it into four cognitively scoped agents: Contract Reader (investigation, no playbook in context), Playbook Comparator (evaluation with legitimate seeds), Redline Writer (generation shaped by deal dynamics), and Strategic Advisor (synthesis from compressed inputs).

A critical design decision was captured in a commit at 14:41: pipeline runs *must* use separate subagents per stage — one per agent — with only structured handoff output crossing between them. Running all four in a single subagent recreates the monolithic contamination the pipeline is designed to avoid. This became a core protocol rule.

The Tier 1 vs Tier 2 evaluation landed at 14:45 — optimised outperformed across all six dimensions, with the largest gaps in audience awareness (+1.5) and natural variation (+1.0). The register shifted from "checklist" to "lawyer preparing for negotiation."

By 17:48, all three tiers had full runs (3 each, 12 separate subagents for the pipeline). The scores told the story: Baseline 2.9/5, Optimised 3.3/5 (+0.4 incremental), Pipeline 4.5/5 (+1.2 leap). The commit message captured it: *"the pipeline discovers things the monolithic versions structurally cannot see."*

External blind evaluations followed. Outputs were randomised with opaque IDs and sent to Claude Web and Gemini with zero project context. Both independently ranked Pipeline 1st, Optimised 2nd, Baseline 3rd. Claude Web's verdict: the pipeline version *"treats the contract as a deal, not a document."*

### A2: Marketing content — the first boundary condition (18:22–18:56)

A2 tested creative-within-constraints work — a product launch blog post. Different interference pattern (template anchors suppressing creative generation rather than evaluation pre-filtering investigation).

The result was the first split decision. Claude Web ranked Optimised 1st, Pipeline 2nd. Gemini ranked Pipeline 1st, Optimised 2nd. Both ranked Baseline last. Matt's human judgment sided with Optimised — it had a more natural voice.

This produced the first entry in `findings.md`: creative work may not need Tier 3. The pipeline adds analytical sophistication but may over-process the voice. A genuine boundary condition, documented as it was found.

### A3–A6: Four experiments in rapid succession (19:32–20:29)

Test materials were committed at 19:32 — a manager performance review for a senior engineer not ready for promotion (A3), synthesis of 6 user interviews about project management tool adoption drop-off (A4), a production Lambda debugging scenario (A5), and a SEV1 customer data exposure postmortem (A6). These ran with single runs per tier to save tokens while mapping the pattern across domains.

By 20:09, all four experiments were complete end-to-end. Pipeline scored highest in all four. At 20:12, `findings.md` was updated: **pipeline wins 6 of 6.**

Second evaluations at 20:21 pulled perfect scores down slightly (24/25 across the board) but rankings held unanimously. The second evaluations surfaced notable details:
- A3: The pipeline *exercised independent judgment* — it disagreed with the scenario's implied ratings and reframed the promotion message
- A5: Tier 2 added nothing to an already well-structured prompt, but Tier 3 still improved it — architecture matters even when individual prompts are already clean
- A6: The pipeline produced genuine organisational learning reframings (*"confidence accumulates across checkpoints without coverage expanding"*)

A4 got external blind evaluation at 20:29. Both Claude Web and Gemini independently ranked Pipeline 1st — unanimous. The pipeline uniquely produced compound cross-interview insights: *"workarounds are specifications written in behaviour,"* the *"destination vs lens"* architectural reframe, and the *"invisible non-adopter"* concept. The commit called it the *"strongest external validation of the qualitative leap claim."*

### Tooling and packaging (23:06–23:35)

Late that evening, the repo was packaged for reproducibility. `RUN-ALL.md` expanded all Claude Code slash commands inline so the full experiment suite could run without Claude Code dependencies — designed for GitHub Copilot CLI. Toolkit agents were published in both `.claude/agents/` (Claude Code subagents) and `.github/agents/` (Copilot format with handoff buttons wired for the architect → writer → evaluator chain). `USAGE.md` documented how to invoke from either platform.

### First external contribution (15 Mar)

On 15 March, PR #1 was merged — a methodology review. The repo was no longer a solo project.

### What the git history reveals about the process

The commit timestamps tell a story about pace. The entire A1 experiment — analysis, optimisation, pipeline design, 9 runs across 3 tiers (including 12 separate subagent invocations for the pipeline), internal evaluation, blind comparison setup, and external validation from two independent models — took roughly 4 hours. A3–A6 took under 2 hours combined. The framework was doing the heavy lifting; once the protocol was established, execution was fast.

The commit messages also reveal intellectual honesty in real time. Perfect scores were flagged as "suspicious" in the same commit that reported them. The A2 creative boundary condition was documented as a genuine limitation, not explained away. The caveats section of `findings.md` — single runs, same model, self-evaluating — was written alongside the results, not added later as a disclaimer.

---

## The Timeline, Compressed

| When | What |
|---|---|
| Mid-2024 | Started building an AI-first CA policy tool |
| Mid-2024 – Feb 2025 | ~7 months of iteration, 7 major versions, ~10,000 lines of prompt work (two-thirds discarded) |
| Somewhere in there | CTA breakthrough — stopped engineering decompositions, started describing how consultants think |
| Somewhere in there | Seeds crisis → convergent/divergent framework, seeds vs lenses |
| Somewhere in there | V3→V4 experiment — the strongest evidence that context carries cognitive mode |
| 18 Feb 2026 | Blog post 1: "I Built an AI Tool That Does My Job Better Than Me" |
| 4 Mar 2026 | Blog post 2: "Why Good Prompting Wasn't Enough" |
| 5 Mar 2026 | Blog posts 3 & 4: "Context Carries Cognitive Mode" + Evidence companion |
| 14 Mar 2026 | This repo created — research framework, all 6 experiments run in one day, pipeline wins 6/6 |
| 15 Mar 2026 | First PR merged (methodology review) |
| 18 Mar 2026 | Today |

---

## The Core Bet Behind This Repo

By the time the blog series was published, there was a provocative claim sitting on the table — but all the evidence came from one person, one project, one domain (Microsoft Conditional Access policies). The question that launched this repo was: **does any of this generalise, or was it a lucky break?**

### The thesis

The industry is trending toward bigger, more comprehensive single prompts. Skills, plugins, progressive loading — all mechanisms to make prompts effectively longer. The assumption: more context = better output.

The bet: **that assumption is backwards for complex tasks.** Not because of token limits — the V3→V4 experiment proved that with 70% of the context window empty. But because more context means more cognitive mode mixing, and mixing incompatible modes (investigation + evaluation, exploration + generation, synthesis + quality checking) creates distributional interference that degrades output in ways you can't see.

The contamination is invisible because the output still looks fine. You only discover the gap when you split and compare. **Good output hides great output.**

### The mechanism

LLMs are language models. Language carries the cognitive mode of whoever produced it. Exploratory text has different statistical properties than evaluative text — different hedging, different commitment levels, different sentence structures. The model learned these distributions from training data. When evaluative language sits in the context, it activates evaluative patterns. You don't need the model to "be cognitive" — you just need it to have learned that evaluative language predicts more evaluative language. Which it has.

This gives a concrete, testable prediction: prompts that mix incompatible cognitive modes should produce worse output than the same work split across clean contexts, even when there's plenty of room in the context window.

### The alternative

Smaller, cognitively scoped agents in a pipeline. Each does one type of thinking in a clean context. Structured handoffs strip cognitive residue between stages. The database (or structured output) between stages is the cognitive boundary — a JSON record doesn't carry the exploratory tone of the investigation that produced it.

### What the three tiers test

The experiment design is deliberately structured to isolate the effect:

- **Tier 1 (Original)**: The prompt as-is. Establishes the baseline.
- **Tier 2 (Optimised)**: Same structure, better cognitive hygiene — remove numeric anchors, replace seeds with lenses, add scope boundaries. Tests whether you can improve output by fixing interference *within* a single prompt.
- **Tier 3 (Pipeline)**: Split into multiple agents, each doing one type of thinking in a clean context. Tests whether the single-prompt architecture itself is the ceiling.

**The key prediction**: If Tier 2 improves incrementally (confirming that mode interference exists and can be partially mitigated) and Tier 3 produces a qualitative leap (confirming that full separation unlocks capabilities the single prompt suppresses), then the headline finding is: **the monolithic prompt is the ceiling, not the floor.**

If Tier 3 doesn't outperform Tier 2, the framework's explanatory power is weaker than claimed. Negative results are results.

### The skills contamination corollary

There's a secondary bet: that skills/plugins loaded on demand are a contamination vector. A base agent with an investigative posture loads a skill with evaluative framing — now investigation and evaluation share the context. The contamination is non-deterministic (depends on which skills load in which session), which could explain why agents sometimes "day-drink" (hallucinate, go off-rails) on some runs but not others.

### Why these six experiments

The experiments were deliberately chosen from Anthropic's own knowledge-work-plugins — same authorship, same quality bar, different domains:

| # | Domain | Why it was chosen |
|---|---|---|
| A1 | Legal contract review | Investigation + evaluation + generation fused together; 12 fixed categories; "3-5 Key Findings" anchor |
| A2 | Marketing content | Template anchors suppressing creative generation ("3-5 sections", "3-4 value propositions") |
| A3 | HR performance review | Mostly template generation — expected to show limited improvement (boundary case) |
| A4 | Design research synthesis | Synthesis constrained by fixed output structure |
| A5 | Engineering debug | Clean 4-step sequence — expected to already be well-structured (calibration) |
| A6 | SecOps incident response | 4-mode mixing; "5 Whys" forces exactly 5 depth levels |

The portfolio covers a spread: high-interference prompts (A1, A6), creative work (A2), boundary cases where the effect might not show up (A3, A5), and synthesis tasks (A4). If the framework has predictive power, the improvement should correlate with the predicted interference — biggest gaps where mode mixing is worst, smallest where the prompt is already clean.

### What's in the repo

- `reference/` — The evidence from the original CA project (blogs, V3/V4 prompts and outputs, full production prompt set). Read-only context.
- `research-foundations.md` — The theoretical framework: the cognitive stack, mode interference, trust chains, the convergent/divergent distinction.
- `experiment-design.md` — The three-tier protocol, evaluation rubric, experiment portfolio.
- `toolkit/` — The prompt-architect and prompt-writer agents, grounded in cognitive science research. These *are* the methodology, packaged as agents anyone can run.
- `experiments/` — One folder per experiment, each containing the original prompt, optimised version, pipeline agents, test material, run outputs, and blind evaluations.
