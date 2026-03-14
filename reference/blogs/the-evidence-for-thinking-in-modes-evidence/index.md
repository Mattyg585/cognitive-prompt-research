---
title: "Context Carries Cognitive Mode — Evidence & Methods"
date: 2026-03-05
draft: false
description: "Full experiment designs, version comparisons, and claims tables documenting the evidence behind the convergent/divergent cognitive mode framework for AI pipeline design."
summary: "The companion evidence post to 'Context Carries Cognitive Mode' — containing the full experiment designs, version comparisons, and claims tables. Each section is self-contained. Every claim is mapped to its evidence and its limitations."
tags: ["AI", "Context Engineering", "Prompting", "Cognitive Modes", "LLM"]
series: "AI Reasoning Engine"
seriesOrder: 4
---

This is a companion to [Context Carries Cognitive Mode](/blog/context-carries-cognitive-mode/), the third post in a series about building AI systems around two cognitive modes — convergent (compress, ground, verify) and divergent (explore, connect, synthesise) — and the claim that separating these modes improves output quality. That post demonstrates the ideas. This one documents the evidence behind them.

What follows is organised as reference material, not narrative. Each section is self-contained. The claims table at the end maps every claim to its evidence and its limitations.

---

## 1. Landscape Agent — Four Versions

The landscape agent is the highest-level synthesis stage in the Conditional Access pipeline. It reads across all investigation output and produces the estate-level narrative. It went through four versions. Each was good enough to stop at. Each had a ceiling that only became visible when the next version revealed it.

### V1: Seeded

The prompt contained a "What Good Looks Like" section describing what the consultant should see when they open the output:

> *A consultant opens the landscape review section and within 60 seconds knows:*
> - *What the major themes are across the estate (**3 broken enabled policies, consolidation from 55 to ~40**, exclusion group architecture, report-only stalls)*
> - *Which themes are interesting enough to dig into*
> - *Where to find the evidence for each theme*
> - *How to walk the customer through this landscape*

The first bullet is the problem. Specific expected findings — a count and a number — written months earlier and forgotten they were there. The rest of the section is reasonable framing, but that one bullet seeded the output with targets.

Output: 6 database entries. Consolidation anchored at "~40 would provide equivalent or better coverage." The "3 broken enabled policies" lumped together as a single finding — two include/exclude conflicts and a missing device filter, three different error types counted as one category to match the seeded count. The narrative framing — "accretion without governance" — was strong, memorable, and matched the practitioner's own consultant review through a different evidence path.

### V2: Seeds removed, pipeline contaminated

Seeds removed from the prompt. Output landed on "25–30" — but the pipeline had a data contamination bug: the query was pulling consultant review entries that the landscape reviewer shouldn't have seen. V2's number may have been influenced by the practitioner's own analysis rather than independently derived.

### V3: Clean pipeline with investigation lenses

Seeds removed. Pipeline ordering fixed — consultant entries excluded. The "What Good Looks Like" section was replaced with investigation lenses — analytical angles that guide how the agent looks without prescribing what it should find. Three examples from the prompt:

> - *Consolidation arithmetic — Size the redundancy across the estate. How many policies are doing unique work? The number doesn't need to be precise — "roughly half" is more useful than a false-precision count.*
> - *Stated vs actual posture — Where does the estate's actual security posture diverge from what the policy names and structure suggest?*
> - *Retirement sequencing — Before calling anything a consolidation candidate, check whether it's the only policy providing a specific control for a specific population. Flag dependencies between retirements: which can be safely removed now, which need a replacement first.*

Compare this to V1's seed: "3 broken enabled policies, consolidation from 55 to ~40." The lens says *how to look*. The seed says *what to find*. Three variables changed between V1 and V3, not one.

Output: 8 database entries (vs V1's 6). The consolidation finding, independently arrived at:

> *"Of 55 unique policies, **roughly 25–30 are doing genuinely distinct security work** — the rest duplicate baseline controls or duplicate each other."*

This matched the practitioner's own expert review. V1's ~40 had been wrong — the model had been constrained to a worse answer by the seed.

| | V1 (seeded) | V3 (lens-guided) |
|---|---|---|
| Entries | 6 | 8 |
| Naming families | 3 identified | 3 + bare-name fourth family |
| Error disaggregation | 3 error types lumped into one entry | Separated cleanly (self-cancelling policies, name-config mismatches, orphaned refs) |
| Ticket policy finding | One policy (TKT-76543) | Both (TKT-76543 + REQ-99887) with retirement sequencing |
| Consolidation | "~40" (anchored to seed) | "25–30" with three-category breakdown |
| New findings absent from V1 | — | Policy names overstating controls (6 policies), orphaned directory references as deprovisioning gap |

**Analysis:** Three variables changed between V1 and V3: content prescription removed (seeds), data contamination fixed (pipeline ordering), and structural prescription added (investigation lenses). The improvement came from all three working together — removing what to find, fixing what the agent could see, and adding how to look.

The seeded themes were content prescription in a divergent stage — telling the model what to find during open-ended investigation. The lenses were structural prescription — analytical angles that guided how the agent investigated without prescribing what it should find.

Nuance: seeds work for convergent stages. The story grouping prompt still seeds Zero Trust archetypes as starting categories — classification into known buckets. Seeding is harmful specifically when applied to divergent work.

### V4: Convergent/Divergent Split

V3's prompt explicitly structured two jobs in the same pass:

> *You have two jobs:*
>
> ***Job 1: Quality Gate (silent)***
> *Clean up the investigation output. This work is invisible to the consultant — they see the result, not the process.*
> - *Reconcile duplicate threads*
> - *Fix misleading topics/headlines*
> - *Flag missed signal*
> - *Connect fragmented threads — the investigator's `not_checked` in one story may be answered by a `found` in another*
>
> ***Job 2: Landscape Synthesis (visible)***
> *Produce thematic summaries that orient the consultant. These are breadcrumbs — each one tells the consultant "here's a pattern, here's why it matters, here's where to look."*

Job 1 is convergent: reconcile, fix, flag, connect. Job 2 is divergent: thematic synthesis, pattern discovery, "occasionally something genuinely new surfaces because no earlier layer had the full picture."

The V4 experiment removed Job 1. No new lenses added. No structural changes to how synthesis was described. Same data, same model. One line adjusted: "If they don't, that itself is a quality issue to address in Job 1" became "If they don't, note it factually and work with what you have."

| | V3 (combined) | V4 (synthesis only) | QA Gate (separate) |
|---|---|---|---|
| Entries | 8 | 12 | Text report (no DB entries) |
| Core themes | 8 | All 8 of V3's, plus 4 new | — |
| Non-functional policies found | 2 | 3 (caught CA012) | Noted CA012 as missed |
| Losses vs V3 | — | Zero | — |
| Context usage | ~30% | Not measured | Not measured |

**V4's new findings:** Stalled rollout (5 report-only policies as a coherent improvement set — V3 folded this into other entries). Guest access (block policies with incompatible exclusion logic — V3: one sentence in the handover). Exclusion groups as attack surface (same bypass groups recur everywhere, membership unknown — V3: not surfaced at all). Retirement sequencing as explicit safe/unsafe removal categories (V3: embedded within ticket policy entry).

**V4 expanded one finding:** "Two enabled policies apply to nobody" became three — V4 caught CA012's missing device filter as the same error class.

**The QA gate found things neither landscape agent found:** Platform bypass patterns (SAP, Tableau browser-only scoping). Medium sign-in risk gap. ACSC Essential Eight compliance context (relevant for the Australian tenant). 8 cross-story thread connections between `not_checked` and `found` entries.

The combined agent had room (30% context). Both agents produced better output when separated. Not a capacity problem — a contamination problem.

The register shift is visible in the handover text. V3: *"The result is an environment where roughly half the policies duplicate baseline controls."* V4: *"The security intent is sound in every case — the problem is not what was built, but that nobody went back to consolidate."* V3's handover was already strong — six paragraphs, actionable conversation walkthrough. V4 didn't fix weak output; it shifted register from auditor to advisor.

### V3 vs V4 — Entry Headlines

**V3 (8 entries):**
1. Three Naming Families Reveal How This Estate Grew
2. Roughly Half the Estate Duplicates the Baseline
3. Policy Names That Overstate Actual Security Controls
4. Two Enabled Policies Silently Apply to Nobody
5. Ticket Policies Are Accidentally Load-Bearing for Device Compliance
6. Orphaned Directory References Signal a Deprovisioning Gap
7. How to Walk the Customer Through This Landscape
8. Landscape Summary

**V4 (12 entries):**
1. Three Naming Families Tell the History of This Estate
2. Of 55 Policies, Roughly 25 Do Unique Work
3. Policy Names That Overstate What the Controls Actually Do
4. Three Enabled Policies Silently Apply to Nobody *(V3 found 2; V4 caught CA012)*
5. **The Stalled Rollout — Five Report-Only Policies Are the Next Maturity Step** *(new)*
6. Ticket Policies Accidentally Carry Tenant-Wide Device Compliance
7. Orphaned Directory Objects Across the Estate Signal Missing Lifecycle Governance
8. **Guest Access May Be Broken by Design — Two Block Policies With Incompatible Exclusion Logic** *(new)*
9. **Exclusion Groups Are the Real Attack Surface — Same Groups Recur Everywhere** *(new)*
10. **Retirement Sequencing — What Can Be Safely Removed and What Cannot** *(new)*
11. Walking the Customer Through This Landscape
12. Landscape Summary

The four new entries (bold) are themes V3 either missed entirely or folded into a single sentence within another entry. V4 gave each its own finding because the synthesis agent had cognitive space to develop them.

### Conversation Framework Comparison

Both versions produced a conversation framework — how to walk the customer through the findings. The opening lines show the register shift:

V3: *"Open with the naming families (builds trust, no judgment). Show the customer their own history."*

V4: *"Open with what works well. This estate has a working security foundation... The redundancy that makes this estate larger than it needs to be also means coverage gaps are rare — overlapping policies create safety nets. Start here to establish credibility and avoid triggering defensiveness."*

V3 sequences the conversation. V4 models the room — anticipating how the customer will feel at each stage and shaping delivery to manage that.

### Full Lineage

0. **Pre-CTA** (Oct 2025): ~20 per-policy observations, no landscape synthesis (different pipeline shape — no convergent/divergent separation, no database, no multi-stage processing)
1. **V1** (Feb 11, seeded): 6 entries, ~40 consolidation number, errors lumped
2. **V2** (Feb 20, seeds removed, pipeline contaminated): 6 entries, 25–30 from contaminated data
3. **V3** (Feb 20, lenses + clean pipeline): 8 entries, 25–30 independent, quality jump across the board
4. **V4** (Feb 27, convergent/divergent split): 12 entries, 4 new themes, zero losses vs V3

---

## 2. The Agent Split — Mode Separation in Practice

### The combined configuration

The knowledge-capture pipeline (the second build — analysing the complete history of building the first project, on unstructured data) initially ran investigation as a single step. The investigation prompt directed the agent to read raw sources AND follow threads in the same pass:

> *"Someone spent seven months building something they don't fully understand. The compressed history is in front of you — case files with grounded evidence, gathering files with raw detail... Your job is to find what's actually here."*

The prompt listed primary sources — gathering files, case files, production prompts, git history, schema files — and then said to follow threads wherever they led. Evidence-gathering and thread-following shared the same context.

### What the combined agent produced

Three threads per session. The agent's opening move in a typical thread:

> *"I read all six core pipeline prompts end to end (L1, story grouping, story investigator, L3 framework assessment, landscape reviewer, triage assistant), looking for where the convergent/divergent distinction creates real differences in prompting style."*
> — Thread 005, session 5

Good findings. But the agent self-diagnosed its own constraint:

> *"Every thread cost context and time to write up, which made me ration threads. Ration = converge."*

The gathering work consumed the context that should have gone to thread-following. Promised threads were abandoned because the session "felt done" after three threads. The agent had identified its own convergent prison.

### The split configuration

Two prompts replaced one. A new convergent evidence-preparation step was inserted upstream.

**The evidence gatherer** (convergent — new step):

> *"You're preparing the ground for an investigator. The investigator's job is to follow threads, notice patterns, chase connections — divergent work that requires focus and context. Your job is to make sure they don't have to gather evidence while they're trying to think.*
>
> *You are not investigating. You are not following threads. You are not interpreting. When you notice something interesting — and you will — note it as a lead for the investigator, don't chase it yourself."*

**The investigation prompt** was rewritten to assume pre-loaded evidence:

> *"The evidence has been gathered and organized for you — evidence briefs with cited sources, case files with grounded claims... You're not gathering evidence — that's already done. You're following threads through evidence and seeing where they lead."*

### What the split produced

The investigator went straight to cross-thread connections:

> *"Started from: Evidence briefs for invisible scaffolding, enforcement gradient, expert workflow alignment, context windows as forcing function. Three patterns from different evidence briefs kept intersecting — the visibility gradient, the enforcement gradient, and the build/consumption inversion. They collapsed into one structure."*
> — Thread 007, session 8

One thread at genuine depth instead of three rationed threads. No reported thread-rationing. The trust chain finding — one of the investigation's central discoveries — emerged from seeing patterns across four pre-organized evidence briefs. That cross-brief pattern recognition couldn't have happened in the combined configuration, where the agent was spending context on reading primary sources sequentially.

### Analysis

The convergent/divergent framework predicts that combining evidence-gathering (convergent) with thread-following (divergent) in the same context will degrade both — not because there isn't room, but because the cognitive postures interfere. The gathering anchors toward completion and documentation. The thread-following needs open space for connections.

The prediction held. The agent diagnosed the problem before the framework named it. The fix was what the framework predicts: insert a convergent trust-building step upstream so the divergent step can consume trusted material instead of building it. Same diagnosis, same fix, different project from the original CA pipeline — where framework assessment was moved before investigation for exactly the same reason.

### A note on emergence vs divergence

The pipeline evidence reveals two distinct phenomena that the main post groups under "divergent" but are worth separating here.

**Emergence** is when properties become visible at a level above the components. "This environment was built three times by three different teams" is emergent — it's in the data (three naming families, overlapping objectives, different exclusion groups) but doesn't exist in any single policy. The load-bearing "Temporary Full Access" finding is the same: the dependency only becomes visible when you reason across both it and the policy it's accidentally covering for. Emergence is closer to convergent work — it's compressing fifty-five policies into structural insight. The trust chain makes it possible by preserving relationships while compressing, so cross-policy patterns are available to higher-level stages.

**Divergent generation** is what happens next. The V4 handover sequencing isn't in the data at all. No policy JSON contains "the customer team will feel defensive." The agent inferred human intent from naming patterns and overlapping objectives, then made a strategic communication decision about how to present the findings. That's generative — producing something that didn't exist in the input or even in the relationships between inputs.

The chain is: convergent compression → preserves relationships → makes emergent patterns visible → divergent stage recognises those patterns AND generates novel framings that weren't in the data at any level. Emergence is the precondition. Divergence is what you do with emergent patterns once they're visible.

This distinction sharpens the contamination finding. When V3 had both modes in the same context, the emergence was there (it found the naming families, the duplication). But the divergent generation was muted — "roughly half the policies duplicate baseline controls" is true and emergent, but not generative. V4, freed from convergent work, took the same emergent patterns and went somewhere with them.

---

## 3. Thinking Externalisation Experiment

### The practice

Every prompt in both pipelines was developed through the same cycle:

1. **Build** a prompt
2. **Run** it on real work
3. **Debrief** the agent — pointed questions about tension, decisions, uncertainty, forced behaviour
4. Agent produces **informed reconstruction** of its process (not introspection — reconstruction from conversation context + domain knowledge)
5. Human applies **judgment** ("hold up a sec") to separate signal from noise
6. **Harden** the prompt at the uncertainty points found in the debrief
7. **Repeat** until the debrief is boring

### The legitimacy question

The mechanism sits on shaky ground. LLMs can't introspect. As far as can be observed, the internal reasoning that shapes each response doesn't persist — it isn't available to the agent in subsequent turns, and it isn't accessible externally. This is inferred from behaviour, not from knowledge of the architecture. When asked "where was the tension," the agent reconstructs from the conversation history (tool calls, visible text) and its pattern knowledge about failure modes. Same-session reflection is reconstruction, not recall.

Why it works despite this: the reconstruction is informed by the full conversation context AND deep knowledge about failure modes in the kind of work being done. It's like giving a survey to a respondent who is also a survey design expert — they can tell you "I was confused here" AND "here's why the question structure caused it." The human's role is critical: the agent produces raw diagnostic material, the human decides what's signal.

### Experiment design

Two runs of the same investigation prompt against the same data (CA pipeline investigator):

- **Run A** (baseline): Standard investigator prompt, same-session debrief questions afterward
- **Run B** (thinking externalised): Same prompt + instructions to maintain a narrative process log during investigation, same debrief questions + re-read of the thinking log

### Results

- Investigation output: marginal difference (12 vs 10 findings, slightly sharper headlines in Run B)
- Reflection quality: comparably good in both runs
- **The thinking log's unique contribution** — preserved three things reflection alone didn't:
  1. **Triage reasoning** — WHY threads were not followed (not just that they weren't)
  2. **Reframing moments** — WHEN insights crystallised (the "All Apps = consolidation risk" shift happened during GUID resolution, not during writeup)
  3. **Complete negative space** — what was noticed but deliberately not pursued, with reasons

### Additional finding: schema fields as convergent constraint

Both experiment runs independently confirmed: the investigator prompt's required four fields (found/checked/assumed/not_checked) force convergent behaviour in a divergent agent — the same pattern the main post describes, showing up in the database schema rather than the prompt. The assumed and not_checked fields are genuinely useful when there's a real inference or gap, and they're padding when the finding is straightforward. The agent fills them because the schema demands it, not because there's something to say. Fix direction: make fields responsive rather than required.

---

## 4. Claims Reference

*Each claim with its label, supporting evidence, and honest limitations.*

### Architectural Claims

| Claim | Label | Evidence | Limits |
|-------|-------|----------|--------|
| Mode separation improves pipeline output | Convergent/divergent as design principle | Per-policy analysis batches (0% variance with anchors → genuine variation without). Investigation pipeline split — agent diagnosed own constraint, separated modes produced deeper findings *(Section 2)*. CA pipeline framework assessment reordering. Landscape reviewer split — same prompt minus QA section, 8→12 entries, zero losses *(Section 1)*. | The boundary is porous. Three "convergent" stages use three different prompting styles. The binary is useful but oversimplifies. Mixed-mode output is good enough that the gap is invisible without comparison. |
| Context isolation prevents mode contamination, not just token overflow | Context-as-environment vs context-as-resource | Agent self-diagnosis ("ration = converge"). Evidence briefs improved quality in sessions that weren't context-limited. Landscape split at 30% context usage — not capacity-limited, still improved when separated. Two of three split tests had no context pressure. | The mechanism is independent of capacity in all tests so far, but hasn't been tested with a formal control for context pressure as the sole variable. |
| The pipeline is a trust chain | Trust chain architecture | Three independently documented gradients (visibility, enforcement, build/consumption) collapse into one structure. Predicts missing stages — tested three times, same diagnosis, same fix. | Agent's own check: "correlated properties, not identical." Two schema changes relaxed enforcement with no visible quality impact. |

### Prompting Claims

| Claim | Label | Evidence | Limits |
|-------|-------|----------|--------|
| Content and structural prescription have opposite effects | Content vs structural prescription | Per-policy validation loop. Landscape three-run comparison — seeding removal + pipeline fix + lens addition *(Section 1)*. | Tested within one project. Not tested across different models or unrelated domains. Three variables changed between V1 and V3, not one. |
| Category lists work better as orientation than as checklists | Lenses not checklists | Appears in per-policy analysis, framework assessment, and investigation stages. Worked four months before the framework was named. | Whether it's "convergent-resistance" or just good prompting practice is genuinely fuzzy. |
| The labels enable intentional design, not just description | Good vs intentional | The agent split was diagnosed using the labels. The second pipeline was built in two days using them as design decisions. Without them, the same fixes arrived through months of trial and error. | Single practitioner. Others might reach the same designs through different vocabulary. |

### Broader Claims

| Claim | Label | Evidence | Limits |
|-------|-------|----------|--------|
| The architecture emerged through iterative precision, not design | Emergent architecture through iterative articulation | 142 commits, 7 months. Practices predated labels by 4+ months. CTA produced one immediate structural change (stories not clusters) and instilled the reflective practice that surfaced mode boundaries over months. 7-month timeline vs 2-day rebuild shows portability. | Whether the process was "iterative articulation" or "trial and error with good feedback" is an interpretive choice. CTA's contribution was indirect — a reflective habit, not a direct discovery. |
| The method generalises to unstructured data | Knowledge compression method | CA pipeline (structured JSON) and knowledge-capture pipeline (unstructured project history) used the same pattern. Same principles, different data. Second build needed an additional evidence/interpretation separation step. | Two experiments. One practitioner. Different enough that coincidence is strained, but not enough to call it proven. |

---

## 5. Honest Limitations

- **The recursive confirmation problem.** The investigation kept demonstrating the hypothesis while testing it. A system built on mode separation, investigating itself, found mode separation matters. Real pattern or self-reflection? The investigation flagged this and couldn't resolve it from inside.

- **Single practitioner.** All evidence comes from one person's projects. Replication by others would be stronger evidence than any amount of self-investigation.

- **The "just good engineering" boundary.** Where cognitive mode design ends and good software architecture begins is genuinely unclear. The labels may name something real or just relabel established practice.

- **What wasn't tested.** The content/structural distinction hasn't been tested across different models. The trust chain predictions haven't been tested outside these two projects. The convergent-resistance framing hasn't been independently validated.

- **The literature claim.** The practitioner searched for these specific framings — multi-mode cognitive decomposition beyond System 1/System 2 applied to AI agent design, context isolation framed as mode contamination rather than token management, CTA-derived cognitive observation applied to prompt architecture — and couldn't find them framed this way. "I couldn't find it" and "it isn't there" are different statements, and this is the first one.

---

*Primary source material — session transcripts, investigation prompts, and experiment designs — exists for all claims in this series. If something here interests you enough to want to see the raw evidence, [get in touch](https://www.linkedin.com/in/matthewgrahamau/).*
