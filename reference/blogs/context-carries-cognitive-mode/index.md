---
title: "Context Carries Cognitive Mode"
date: 2026-03-05
draft: false
description: "Evidence that separating convergent and divergent cognitive modes in AI contexts improves output quality — not because of token management, but because the type of thinking in the context shapes what the model produces."
summary: "I removed a quality-checking section from an AI prompt. The prompt got smaller. The output got deeper. Same model, same data, 70% of the context window unused. This wasn't a capacity problem."
tags: ["AI", "Context Engineering", "Prompting", "Cognitive Modes", "LLM"]
series: "AI Reasoning Engine"
seriesOrder: 3
---

This is the third and final post in a series. The [first post](/blog/what-i-learned-building-ai-tools-that-actually-think/) told the story of what was built — an AI system that produces expert-level analysis of Conditional Access policies. The [second post](/blog/why-good-prompting-wasnt-enough/) told the story of building it — seven months of wrong turns, dead ends, and the architecture that fell out of them. This post is about the evidence. A companion post — [Evidence & Methods](/blog/the-evidence-for-thinking-in-modes-evidence/) — contains the full experiment designs, version comparisons, and claims tables. This post demonstrates. That one documents.

If you're reading this without the first two posts, here's the short version. I'm a cloud consultant — Microsoft infrastructure, seventeen years, no AI background. Over seven months of evenings and weekends, I built a multi-stage AI pipeline that analyses Conditional Access policies. The pipeline architecture itself — staged compression, database as trust boundary, retrieval augmentation — maps to established patterns. But two design decisions don't come from any framework. The first: the stages are separated by type of thinking, not just by token capacity. Some stages compress, classify, and pin things down — I call this **convergent** work. Others explore, follow threads, and synthesise — **divergent** work. When these share a context, the convergent posture tends to dominate, even with plenty of room left. The second: the units of analysis came from interviewing myself about how I actually do this work, and they turned out to be stories, not clusters or categories. The [second post](/blog/why-good-prompting-wasnt-enough/) tells the full story of how I got there. This one tests whether the convergent/divergent distinction actually holds up.

---
## Separate contexts by how they think, not how much fits

I built a multi-stage AI pipeline over seven months. The architecture — staged compression, retrieval augmentation, database as trust boundary — maps to patterns the field already knows. But the design decision that actually changed the output quality had nothing to do with token management.

When I separated two cognitive modes into their own contexts, the output changed immediately.

Convergent work compresses — verification, classification, pinning things down.

Divergent work explores — synthesis, pattern discovery, following threads.

Mixing them in the same context suppressed the divergent output. Separating them made the prompt smaller - and the output deeper. The capability was always there. The context was suppressing it.

---
## Good Output Hiding Great Output

The highest-level agent from the conditional access policy pipeline that I built, reads across all the analysis output from the prior agents and produces an estate-level narrative — the big picture of what's going on across dozens of interdependent security policies. Each finding it produces is a distinct security insight: a pattern, a risk, a theme that emerges from reading across the whole estate.

By the third iteration of this agent, the agent was already genuinely good. Good enough that an earlier version's output had been published in the first blog post. But at some point, I realised that V3's prompt was doing two jobs in the same pass: convergent quality-gate work and divergent synthesis.

The convergent/divergent labels said that this should matter. My gut said it probably wouldn't — the output was already strong.

So I ran an experiment. I took the V3 prompt, removed the QA section, and changed one line. Same role framing. Same analytical angles. Same output format. Same data. Same model.

The synthesis agent produced twelve findings instead of eight. Four entirely new themes the combined agent hadn't surfaced. Zero losses — everything V3 found, V4 found too. The QA agent, running separately, also went deeper when it wasn't trying to synthesise. Both agents improved when separated.

The combined agent had only been using about 30% of its available context window. It had room. This wasn't a capacity problem. It was a contamination problem.

But the numbers aren't even the interesting part. The register shift is.

Here's what V3 produced in its handover to the consultant — not a snippet, but the full handover. It's worth reading in full because the quality is the point:

> *This is a 55-policy Entra ID Conditional Access estate built organically over at least three authorship eras, each leaving its own naming convention and exclusion group patterns. The result is an environment where roughly half the policies duplicate baseline controls — three global MFA policies, three legacy auth blocks, two guest-deny policies, five admin MFA layers — all enforced, all slightly different in their exclusion lists. The redundancy provides accidental safety (no single point of failure for any control) but makes the estate hard to reason about and harder to maintain.*
>
> *The most significant cross-estate theme is the gap between stated and actual posture. Six policies have names that promise security controls their configurations don't deliver — phishing-resistant MFA that's actually standard MFA, device compliance that's actually MFA, app protection that's actually MFA. Two enabled policies apply to nobody due to include/exclude conflicts on the same group. Together, these mean the policy list as documentation overstates what's actually enforced. Anyone making security decisions based on policy names alone would miscalculate their coverage.*
>
> *The finding that warrants the most care is buried in the Ticket/Temporary Access story: two ticket-prefixed policies (TKT-76543 and REQ-99887) have accidentally become the primary device compliance enforcement for the entire tenant. If a cleanup effort retires "temporary" policies first — a natural instinct — it would silently remove device compliance requirements for all users.*
>
> *Start the customer conversation with the naming families — it's the non-threatening entry point that explains everything else. Then quick wins: fix the two broken policies, consolidate legacy auth to one policy, correct the report-only config mismatches. Then the strategic conversations: exclusion group reconciliation across naming families, guest access validation, and whether the stalled report-only policies are still on the roadmap. The ticket policies and their accidental load-bearing role should come last — by then the customer understands the organic growth pattern that explains how this happened.*

That's genuinely good work. Nobody reading that in isolation would say it's incomplete. It finds the structural patterns, identifies the risks, sequences a customer conversation. It's the output of a competent senior consultant.

Now here's V4, same data, freed from QA:

> *This is a 55-policy Conditional Access estate that grew organically over at least three implementation phases, each adding its own layer without retiring what came before. The result is an environment with a solid security foundation — universal MFA, legacy auth blocking, risk-based access, geo-fencing, and a guest default-deny model — buried under enough redundancy and configuration drift that the actual posture is harder to read than it should be.*
>
> *The dominant theme is layered redundancy. Three naming families (CA0xx, ACME Cloud, CORP_) run through the entire estate, and each family brought its own version of the same controls: three global MFA policies, three legacy auth blocks, two guest blocks, five admin MFA policies, two Salesforce policies. Each layer uses different exclusion groups, different targeting approaches, and slightly different configurations. The security intent is sound in every case — the problem is not what was built, but that nobody went back to consolidate. Roughly 25 of the 55 policies carry the estate's actual security value; the rest are duplicates, stalled rollouts, or broken configurations.*
>
> *The second theme is a stalled rollout toward Advanced maturity. Five report-only policies represent a coherent set of improvements — phishing-resistant MFA for admins, device compliance for all users, app protection for BYOD, per-application authentication strength, and automated risk remediation. Three of these have name-config mismatches where the grant controls were never updated to match the policy name. These five are the clearest path forward, and they connect directly to the framework assessment's finding of an estate at Initial maturity with Advanced-tier ambitions.*
>
> *The third theme is accidental dependencies. Two ticket-prefixed policies (TKT-76543 and REQ-99887) provide tenant-wide device compliance — a function their names completely obscure. Removing them during ticket cleanup would silently drop device requirements for every user.*
>
> *Start with the conversation framework entry for the recommended walkthrough order. The quick wins are the broken policies that apply to nobody (easy fixes, immediate value), the pure-duplicate app-named MFA policies (safe to remove), and the orphaned directory references (governance hygiene). The strategic work is completing the stalled rollout and replacing the accidentally load-bearing ticket policies with intentional device compliance. The guest access interaction needs its own focused session with test validation.*
>
> *This estate was built by people who were solving real problems in real time. The redundancy is not negligence — it is the natural result of iterative improvement without dedicated policy lifecycle management. The remediation path is configuration work against existing capabilities. No new products, no new licenses, no architectural changes. Just completion of work that was started and consolidation of work that accumulated.*

Read them side by side. V3 is a competent audit. V4 is a consultant who understands the humans on the other side of the table.

"The security intent is sound in every case — the problem is not what was built, but that nobody went back to consolidate." "This estate was built by people who were solving real problems in real time. The redundancy is not negligence." That's not analysis. That's empathy applied to technical findings — a model of how the customer team will receive this information, used to shape how it's delivered. And it emerged from *removing* a section of the prompt, not adding one.

The shift goes deeper than the handover. Both versions also produced a conversation framework — how to walk the customer through the findings. The version-by-version comparison is in the [evidence companion](/blog/the-evidence-for-thinking-in-modes-evidence/), but the opening lines tell the story. V3 opened with:

> *Open with the naming families (builds trust, no judgment). Show the customer their own history.*

V4 opened with:

> *Open with what works well. This estate has a working security foundation... The redundancy that makes this estate larger than it needs to be also means coverage gaps are rare — overlapping policies create safety nets. Start here to establish credibility and avoid triggering defensiveness.*

V3 tells you the sequence. V4 is modelling the room — anticipating how the customer will feel at each stage and shaping the delivery to manage that. "Frame this as simplification, not criticism. The people who built this were solving real problems; the issue is that nobody went back to retire the old solutions." That's not just sequencing a conversation. It's anticipating that this feedback could trigger a defensive reaction and preemptively reframing it.

V3 used the same model, the same data, and the same training. It produced "Open with the naming families (builds trust, no judgment)" — competent, correct, going nowhere. The capability was latent. The context determined whether it surfaced.

Remember what changed between V3 and V4. Not the model. Not the data. Not the role framing or the analytical angles or the output format. The QA section was removed. That's it. The convergent quality-gate work was split into its own separate agent. The prompt got *smaller*. The output got deeper. The agent didn't gain new capabilities. It gained the cognitive space to use capabilities it already had.

This is the finding that keeps surprising me. The mixed-mode output was *good*. Nobody looking at V3 in isolation would say it's incomplete. The gap only appears when you split and compare. Mode contamination doesn't produce bad output. It produces good output that prevents you from seeing what great output looks like.

The distinction is sharper than "V4 was better." V3 found the structural patterns — three naming families, the duplication across the estate, the ticket policy risk. Those are emergent: properties that become visible when you compress fifty-five policies into cross-estate insight, but that don't exist in any single policy. Emergence is what the compression chain produces. V3 had it because the pipeline had already done that work. What V3 couldn't do was go somewhere generative with those patterns. "The customer team will feel defensive" isn't in any policy JSON. That's the divergent stage producing something that didn't exist in the input or even in the relationships between inputs — and it needed the cognitive space that the convergent QA work was consuming. The evidence companion unpacks this distinction further.

---

## What to Tell the Model vs How to Tell It

Post 2 ended with a distinction between seeds and lenses — telling the model what to find versus guiding how to look. That distinction showed up everywhere once I could see it, and the per-policy analysis stage became the clearest experiment.

The per-policy stage examines each of the 55 security policies individually. Across three prompt versions, the same model analysed the same policies with the same analytical angles. Only the instruction style changed.

The first version gave the agent analytical lenses with numeric guidance: "for a simple policy, write 2–3 observations; for a complex one, expect 5–6 or more." The output: three observations per policy, every time. Zero variance. A complex policy with scope misconfiguration, re-authentication anomalies, and naming confusion got the same count as a straightforward admin portal policy. The numbers had become the target.

The second version added investigative mindset prose but kept the numeric examples. Still anchored.

The third version removed all numeric guidance and condensed the instructions to four open-ended analytical questions — lenses like "what's the gap between this policy's stated intent and its actual configuration?" Same lenses as before, same policies, same model. For the first time, a simple policy got two findings — because two was right. One critical issue, one positive observation, done. A complex policy got seven. The output responded to what was actually in the data instead of what the prompt suggested should be there.

One structural change — removing numeric anchors while keeping the lenses as orientation rather than checklist — and the output went from mechanically uniform to genuinely responsive.

The same pattern showed up at the pipeline's highest level. The synthesis agent's first version contained seeded themes — specific expected findings I'd written months earlier and forgotten were there. The output anchored to the seeds. Replace the seeds with lenses, and the agent independently arrived at numbers that matched my own expert review, plus findings the seeded version had missed entirely. Post 2 covered this in detail — the moment I found the seeds in my own prompt and had to work through whether my results were real.

This connects back to the V3/V4 experiment. Content prescription — telling the model what to find — shapes the context toward convergent work. Structural prescription — guiding how to look — keeps space open for divergent work. Two types of instruction that sound similar but move in opposite directions. The V3 prompt wasn't prescribing specific findings, but its QA section was prescribing a convergent posture that carried into the synthesis. The numeric anchors in the per-policy prompt were doing the same thing at a different scale. Same mechanism, different expressions.

---

## How You Detect It

Mode contamination is invisible in the output. V3 looked complete. The numeric anchoring produced clean, consistent results. You can't see what you're missing by reading what you have. So how do you know when convergent and divergent work are interfering with each other?

The method I used throughout both pipelines was simple: build a prompt, run it on real work, then debrief in the same conversation. Not "did it work?" but: where was the tension? What felt forced? Where did you guess? What would you change? The agent's answers become raw diagnostic material. My job was deciding what's signal — the "hold up a sec" moments where my domain expertise caught something that didn't match reality.

Once I had the convergent/divergent labels, the debrief became sharper. Not just "where was the tension" but: is this agent doing convergent work when I need divergent? Are the investigation lenses opening exploration, or is the agent treating them as a checklist? Is the output flat because the task is hard, or because the prompt is triggering compression when I need synthesis? These questions pointed to a specific fix every time I asked them. The labels turned "something's off" into "what mode is this actually doing?"

The method works by reconstruction. The agent and I are both working from the output, not from the process — the same way I could read another consultant's CA policy review and make educated guesses about where they struggled or what they missed. Domain expertise applied to output, not memory of process. That's a real limitation. But it was enough to build two working pipelines and diagnose mode contamination across both of them.

---

## What I Think Is in the Discard Pile

There's something the debrief method can't reach.

When I ask an agent "where was the tension," it reconstructs from the conversation history — the original prompt, its output, and my question. What it can't reconstruct is its own reasoning during generation — the threads it weighed and didn't follow, the framings it considered and discarded, the moment a convergent posture took hold instead of an exploratory one. I believe those are in the thinking tokens — the reasoning traces that are generated during a response and then, as far as I can tell, discarded.

I tried to approximate access. I asked the agent to maintain a running narrative log during investigation — externalising its reasoning process as it worked. The log surfaced things the debrief alone didn't: triage decisions about why threads weren't followed, the specific moment an insight crystallised, the negative space of what was noticed and deliberately set aside. The output appeared useful. But I genuinely don't know how much of it reflected actual reasoning and how much was plausible reconstruction generated alongside the work. I have no way to verify that from the outside — which is precisely the point.

I don't know enough about how these models work internally to make a technical claim here. But I can describe what I've seen from the outside. The debrief method — output plus domain expertise plus pointed questions — was enough to diagnose mode contamination after the fact. A rough approximation of externalised thinking added signal the debrief couldn't reach, even with the uncertainty about what was real. If native access to what gets worked through during generation were available as diagnostic material, I think you'd be able to see contamination as it happens — not reconstruct it afterward, but watch a convergent posture take hold in real time.

The reasoning that gets discarded during generation isn't waste. It's telemetry. And the people building these models are better positioned than I am to know whether that's naive, obvious, or worth investigating.

---

## Where the Labels Are Wrong

The labels are imprecise. I'd rather say that here than have you discover it.

The convergent/divergent boundary is porous. Three stages I'd call convergent use three different prompting styles. The binary is useful but it oversimplifies. After the CA pipeline was finished, I built a second pipeline using the same principles to investigate the first — convergent stages to extract patterns from the prompts and outputs, divergent stages to explore what they meant. "Scope control" emerged as possibly the real mechanism underneath the labels. They may be pointing at something real without naming it precisely.

And there's a deeper problem. I used the system I built to investigate the system I built. Any finding could be the system seeing its own shape instead of a real pattern. The investigation flagged this explicitly: *"I keep arriving back at the same place from different directions. Every time I try to complicate the hypothesis, I end up demonstrating it. That might be because the hypothesis is more right than my investigation gave it credit for. Or it might be because I'm inside the system and can't see outside it. I genuinely don't know which."*

I don't know either. This is the best evidence I can produce from inside. Someone else applying these labels to their own pipelines and measuring what happens would be better evidence than anything in this post. The [evidence companion](/blog/the-evidence-for-thinking-in-modes-evidence/) contains the full claims table with every limitation I've identified.

There's also a trust problem worth naming. At one point I realised I hadn't checked a single piece of raw policy JSON in weeks. The pipeline's analysis felt so coherent that I'd stopped verifying. When I went back, everything checked out. But the fact that the output was convincing enough to short-circuit my verification instinct is a failure mode the architecture doesn't solve. Coherent output isn't the same as correct output. The trust chain's success contains its own risk.

---

## What This Adds Up To

I started with a real problem — 55 interdependent security policies that no single context window could reason over. I built a system to compress them in stages, each stage grounding its work in what the previous one produced. I found the output quality depended less on what I told the model and more on the cognitive environment each prompt landed in. Two labels — convergent and divergent — gave me a way to see that and design for it.

The V3/V4 experiment is the strongest evidence. Not because it proves a theory about how language models work, but because it's a concrete, reproducible demonstration: same model, same data, same role, smaller prompt, better output. The improvement came from removing a convergent task that was contaminating divergent work. The content prescription experiments tell the same story at a different level — numeric anchors constraining output that lenses set free.

I built the first pipeline in seven months of stolen hours. When I applied the labels intentionally — designing a second pipeline to investigate the first — the architecture came together in two days. Not because the second project was simpler. Because I could design instead of iterate. The labels turned "something's off" into a question I could ask and a fix I could apply.

I don't know if convergent and divergent are the right names. I don't know if someone with deeper knowledge of how these models work would read this and say "that's the mechanism" or "you're describing a real effect but the reason is something else." I'd genuinely like to know. If the framing is useful but the explanation is wrong, I'd rather learn the right explanation and keep the utility than defend the label.

What I know is this: the labels work. The method works. The evidence is [here](/blog/the-evidence-for-thinking-in-modes-evidence/) — including the parts that complicate the claims. If you build AI systems and something in this resonates, I'd be interested in hearing from you — whether that's "you've named something I've been seeing" or "here's what you're actually describing." Both would move this forward.

The output was always good enough to stop at. Until you see what it looks like when the modes aren't fighting each other.

---

*[Matt Graham](https://www.linkedin.com/in/matthewgrahamau/) is a cloud consultant specialising in the Microsoft ecosystem, based on the Sunshine Coast, Australia. The systems described in this series analyse Conditional Access policies and project knowledge using AI-powered reasoning pipelines. All CA policy analysis was produced against a test tenant built to represent a realistic enterprise environment. No customer data was used.*
