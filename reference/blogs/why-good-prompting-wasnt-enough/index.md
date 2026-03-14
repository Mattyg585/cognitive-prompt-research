---
title: "Why Good Prompting Wasn't Enough"
date: 2026-03-04
draft: false
description: "Seven months of building an AI pipeline for security policy analysis taught me that the architecture matters more than the prompts — and that the design decisions no framework gives you come from understanding how you actually think."
summary: "The prompts that run my AI system aren't special. The seven months it took to arrive at them is what this post is about — including the moment I found my own anchor bias hiding in a prompt I'd forgotten to revisit."
tags: ["AI", "Prompting", "Context Engineering", "Consulting", "Azure"]
series: "AI Reasoning Engine"
seriesOrder: 2
---

This is a companion piece to ["I Built an AI Tool That Does My Job Better Than Me"](/blog/what-i-learned-building-ai-tools-that-actually-think/). That post told the story of building an AI system that produces expert-level analysis of Conditional Access policies. If you haven't read it, start there — this one assumes you have.

After publishing the first post, a common theme emerged from the feedback: "Oh, so you landed on a good prompt." Said with genuine interest, not dismissal. But it's wrong in a way that matters. The prompts that run the current system aren't special. They're clear, they're well-structured, they describe who the agent should be and what the output serves. Anyone reading them would think "yeah, that's straightforward." And they'd be right.

The seven months it took to arrive at those prompts is what this post is about. Not the architecture diagram — the reason the architecture looks the way it does.

---

## The Wall I Kept Hitting

The first attempt was exactly what you'd expect. I had Claude Code, the Lokka MCP server hooked up to the Graph API, and 55 CA policies in a test tenant. "Analyse these policies against the Zero Trust Framework." Off it went — pulling down policies, running web searches, cross-referencing — it all looked incredibly promising and then: context window limit reached. 55 CA policies will blow through a context window in minutes. Lesson number one.

After some trial and error I solved the context problem. Exported the policies as JSON, stored them in a Postgres database, built queries to feed manageable chunks to the model. Then came the run that produced a >90% alignment score. The output looked fantastic. Detailed, structured, confident. I was thrilled — until I started checking the working. The model had only retrieved a subset of the policies and inferred patterns from what it had. It was hallucinating plausible analysis. Impressive cheating.

I went backwards for a long time after that. Trying things, breaking them, spending evenings and weekends on something that kept not quite working. The "how would I actually do this as a consultant?" question led me to a three-layer architecture: per-policy analysis first, then cross-policy patterns, then framework mapping. Each layer handles a manageable scope. Each feeds the next. That was genuinely useful progress.

But the output from each version kept having the same quality: technically accurate, practically useless. Correct observations about policies, organised in ways that nobody could actually use for a customer conversation.

---

## Getting Smarter About the Wrong Thing

I did what any engineer would do. I made the system more sophisticated.

The single cross-policy analysis prompt couldn't handle breadth and depth in one pass, so I split it into a scanner and an investigator. That was a real improvement. But it still didn't have enough dimensionality. Policies have two faces: what the name suggests they do (semantic intent) and what the JSON actually configures (technical reality). The most interesting findings live in the gap. So I redesigned again: four specialised agents running in parallel, coordinated by an orchestrator. One clustered by inferred intent, another by actual technical controls, a third compared the two to find misalignments, a fourth did targeted deep-dives. An orchestrator coordinated the whole thing with quality gates.

If you showed these prompts to someone who works with AI systems, they'd say "this person knows what they're doing." And they'd be right. The semantic-versus-technical split genuinely decomposes policy analysis into its natural analytical dimensions.

The output was technically correct. It was also impossible to digest on a screen. Clusters, alignment matrices, signal strength ratings, coverage maps — organised around how the analysis decomposed, not around how a consultant would actually use it in a customer meeting. Nobody walks into a meeting and says "let me show you the semantic-technical alignment matrix."

I'd been getting smarter about the wrong thing. Each iteration was a better answer to "how do I tell the AI what to do?" The question I hadn't asked was: "how do I actually think about this myself?"

---

## The Question I Should Have Started With

This is where it gets hard to explain, because what happened next felt — and still feels — obvious. I was stuck and venting to Claude about it — I could see the AI had the raw capability but I couldn't articulate what was missing. Somewhere in that conversation, Claude said something like "what you're describing sounds like Cognitive Task Analysis" — a structured methodology for extracting expert tacit knowledge. I had no idea what that was. I asked Claude to research it, then said "let's run a session — I'll review the CA policies in real-time, and I'll be verbose about what i'm looking at, where I go and what I find interesting and boring, then nudge me about how I actually review CA policies and ask me about my processes and anything else you find interesting."

Over a few sessions, Claude asked me questions and documented what I described. How do I start a review? What catches my attention first? How do I decide what to investigate deeper? When do I stop?

What came out of those sessions surprised me. I don't think in clusters. I think in stories. "What's the MFA story in this tenant? What's the admin protection story? What's the guest access story?" I zoom in on a policy, zoom out to the landscape, zoom back in on something else. I follow threads — "this exclusion group appears everywhere, why?" I don't work through a checklist. I investigate, and I stop when I feel like I've understood the shape of things.

And critically: I don't produce analytical artifacts. I produce handover documentation. If I got hit by a bus tomorrow, the next consultant should be able to pick up my work and walk into the customer meeting. "Stories" aren't my analytical framework — they're the customer's map. "What's the MFA story in your tenant?" is how you start a conversation.

None of this was in my prompts. The prompts were organised around analytical dimensions — semantic, technical, alignment — because that's how I'd engineer a decomposition to find the information to guide my thinking. But that's not how I think.

The rewrite was dramatic. Four agents and an orchestrator became three agents with no orchestrator. Clustering became story-based investigation. The organising principle changed from analytical dimensions to cognitive units. The prompts didn't get more sophisticated. They got more honest. Instead of telling the AI how to decompose the analysis, I described who the agent is and what its output serves. The landscape reviewer, for example, is framed as the senior person at the widest altitude — the first thing in the pipeline that sees the full picture. Instead of numbered steps and quality thresholds, the prompt describes a role and a responsibility.

The output changed immediately. It read like a consultant wrote it. Because the prompts were designed from how a consultant thinks, not from how an engineer decomposes analysis.

---

## The Current System

The system that runs today has five stages, each in its own context window, each feeding the next through a Postgres database. I've since learned that what I built maps to established patterns — staged map-reduce compression, RAG-style retrieval, agentic orchestration. LangChain has had map-reduce chains for years. These aren't novel architectures. I arrived at them independently, by feel, which probably says more about the patterns being natural than about me being clever. Knowing what they're actually called gives me a foundation to be more intentional next time.

But two design decisions don't come from those patterns — and they're the ones that turned out to matter most.

The first is that the stages aren't separated by token capacity. They're separated by type of thinking. Structured extraction doesn't share a context with open-ended investigation. Classification doesn't share a context with synthesis. I didn't design it that way on principle — I designed it that way because every time I combined different types of work in the same context, the output got worse in ways I couldn't pin down. The database boundary between stages isn't just an engineering convenience. It's what keeps each stage's work clean.

The second is that the units of analysis — what the pipeline calls "stories" — didn't come from any framework. LangChain will tell you to chunk your documents. It won't tell you what your chunks should mean. Map-reduce says "process individually, then combine." It says nothing about what the units should represent. The CTA sessions produced that insight: the natural unit of expert reasoning about CA policies isn't "a policy" or "a cluster of similar configurations." It's a story — "what's the MFA story, what's the guest access story." No architecture pattern would generate that. The decomposition came from cognition, not from engineering.

Fifty-five Conditional Access policies is a wall of interdependent configuration. The meaning lives in the relationships between policies, not in any individual one. No human holds it all in their head at once, and no single context window holds it all either. The system's job is to compress that corpus in stages — each stage building on what the previous stage produced, each passing a smaller, more structured, more trustworthy version of the data forward. By the time the final stage sees it, 55 policies and their tangled relationships have been compressed into material it can actually reason over.

But the compression had to be grounded. The hallucination disaster from my first attempt — the model inferring patterns from a subset and presenting them as analysis of the whole — taught me that convincing output means nothing if you can't trace it back to the source. So every observation at every stage links back through the layers to the specific JSON field that generated it. Nothing is floating. If the landscape reviewer says "two policies apply to nobody," you can follow that claim backward through the investigation, through the story grouping, through the per-policy analysis, all the way down to the `includeGroups` and `excludeGroups` fields in the raw policy JSON. The database isn't just storage between stages — it's the chain of evidence.

The five stages move from narrow to wide: per-policy extraction (what does each policy actually configure?), story grouping (what are these policies trying to achieve together?), framework assessment (how does this map against Zero Trust maturity?), investigation (follow threads through each story — no checklist, no numbered steps), and landscape review (see everything together for the first time and synthesise). Each stage does one type of work. The early stages pin things down. The later stages explore. MCP servers give each agent live tooling — Graph API queries, Microsoft Learn, web search — so they can check their work against reality.

There's also a triage agent and a web app. The web app displays everything from the database — observations, stories, links between layers. When I'm sitting in front of it reading through the analysis and I disagree with something or want to follow up, the triage agent has all the database tooling plus all the MCP servers. I push back, it investigates, and its conclusions get documented as consultant-assessed entries. The human layer, tracked.

That last part matters more than it sounds. The system doesn't end with a report. It ends with me — sitting with compressed, grounded material where every claim traces back to the source, following my own threads, pushing back where my experience disagrees, adding the judgment that no AI system generates on its own. The pipeline doesn't produce answers. It produces the starting conditions for informed reasoning. The human at the end isn't reading conclusions. They're investigating through them.

---

## The Thing That Nearly Unravelled It

While writing this post, I went back and read the actual prompts for the first time in a while. I found something I wasn't expecting: seeded data.

The landscape review prompt had expected themes listed in a "What Good Looks Like" section, including specific examples and numbers — "3 broken enabled policies, consolidation from 55 to ~40." I'd written these examples months ago and forgotten they were there. The story grouping prompt had pre-defined archetypes that I'd been presenting as emergent.

I thought I'd found the thing that unravelled the whole project. If the system was just finding what I'd told it to find, none of the results meant what I thought they did.

Working through the disappointment took a few hours. And working through it taught me something I didn't have vocabulary for at the time, but do now.

The story grouping prompt seeds framework-driven archetypes — Zero Trust pillars as starting categories. That's a *classification* task. You're giving the model known buckets to sort into, not constraining what it discovers within each bucket. The investigation within each story was still genuinely emergent. Seeding was appropriate for this type of work.

The landscape review was different. That's *exploration* — the agent following threads wherever the evidence leads, synthesising across the full estate, finding the story of the environment. Seeding expected findings for that kind of work is exactly the anchor bias I'd spent months learning to avoid in the pipeline prompts. I'd encoded the principle everywhere except in the one prompt I wrote earliest and never revisited.

There's a distinction here that turned out to matter for everything I built afterward. Classification and extraction are one type of cognitive work — compressing, pinning things down, sorting into known structures. Investigation and synthesis are another type — exploring, following threads, connecting things that nobody told you to connect. I started calling them **convergent** and **divergent**.

Convergent work compresses. It takes messy input and produces structured, trusted output. *Classify these policies into groups. Extract what the JSON configures. Reconcile duplicates.* Divergent work explores. It takes trusted input and produces insight. *What's the story of this environment? What patterns emerge across these findings? What would you tell the team that built this?*

Seeding the grouping prompt — a convergent task — was fine. The known categories gave the model a structure to sort into. Seeding the landscape review — a divergent task — was anchor bias. I was telling an exploration agent what to find instead of letting it explore.

I didn't just strip the seeds and leave a vacuum. I replaced them with what I started calling investigation lenses — guidance on *how to look* rather than *what to find*. Instead of "look for 3 broken policies" or "expect consolidation to ~40," the prompt now says something more like "look for where stated posture diverges from actual posture." The lens tells the agent what angle to investigate from. It doesn't tell it what the answer should be.

Seeds for convergent work. Lenses for divergent work. That distinction didn't exist in my vocabulary six months ago. Now it's one of the design principles I'd start with if I rebuilt from scratch.

Then I re-ran the pipeline. The results got better on every dimension.

The seeded "~40" consolidation number had been anchoring the model to exactly ~40. Without the seed, it independently arrived at "roughly 25–30 doing genuinely distinct work" — which matched the number my own consultant review produced. The seeded number was wrong, and it had been constraining the model to a worse answer.

Two entirely new findings emerged that the seeded version had missed: a standalone theme about policy names overstating security controls (six policies with names that promise things their configurations don't deliver), and a retirement sequencing entry covering both ticket policies with explicit safe-removal ordering. The seeded version had only found one of the two ticket policies.

This is anchor bias. The exact design principle I'd spent months learning about — remove numeric targets, don't seed expected findings, trust the model to find its own stopping point — applied to the prompt I'd overlooked. The methodology caught its own mistake. The same feedback loop that built the system also corrected the system.

---

## What Actually Came Out

A few examples, direct from the lens-guided pipeline, unedited. All synthetic test data. The version comparison and methodology are documented in the [evidence companion](/blog/the-evidence-for-thinking-in-modes-evidence/).

The ticket policy finding — the one where the seeded version only found one of two:

> *Two ticket-prefixed policies targeting All Users have become accidental pillars of the tenant's device compliance posture — removing them during a "temporary policy cleanup" would silently drop device requirements for most users. The safe retirement order: fix CA003's configuration and enable it before touching either ticket policy.*

The naming-versus-reality finding — the one the seeded version missed entirely:

> *At least six policies across the estate have names that promise security controls their configurations don't deliver. Three are aspirational (report-only, never completed). Three are enabled and actively misleading. The risk is operational: anyone reading the policy list builds a mental model based on names. That mental model will overstate phishing-resistant MFA coverage, device compliance breadth, and app protection for mobile.*

And the conversation framework the system produced without being asked:

> *Open with the naming families (builds trust, no judgment). Show the customer their own history. This positions the conversation as collaborative forensics, not an audit.*

"Collaborative forensics, not an audit." That's consultant framing. I didn't prompt for it. The system arrived at it because the prompts describe who to be — a senior reviewer preparing handover documentation for a customer conversation — not what to produce.

---

## Why This Took Seven Months

About 10,000 lines of prompt work over seven major iterations, two-thirds discarded. The current system is what survived, not what was designed. The prompts that survived aren't clever — they describe a role, what the output serves, and guardrails on language and scope. Anyone reading them would think "that's straightforward." And they'd be right. The seven months was figuring out that these were the right straightforward things to say.

Every failure taught me something about how different types of work need different types of guidance — and that the difference maps to whether the work is convergent or divergent. Looking back, the architecture that actually worked was already splitting along those lines. Extraction and classification are convergent: compress, sort, pin things down. Investigation and synthesis are divergent: follow threads, make connections, find the story. I'd been designing for the distinction without having a name for it.

The name matters because it turns instinct into method. Without it, I had "something feels off about this prompt" and months of iteration to work through it. With it, I have a specific question: is this convergent or divergent work, and does the prompt match? That question pointed to a specific fix every time I asked it.

---

What if you strip the Conditional Access policies out of this? What's left? Not the pipeline — that's map-reduce compression, and the field already knows how to do that. What's left is a question I hadn't seen asked: does the type of thinking matter independently of the content? Does a convergent task in the same context as a divergent task actually change the output, even when there's room, even when the topic is the same? The next post is the evidence that it does.

---

*[Matt Graham](https://www.linkedin.com/in/matthewgrahamau/) is a cloud consultant specialising in the Microsoft ecosystem, based on the Sunshine Coast, Australia. The system described in this post analyses Conditional Access policies using the Microsoft Graph API with AI-powered reasoning. All analysis was produced against a test tenant built to represent a realistic enterprise environment. No customer data was used.*
