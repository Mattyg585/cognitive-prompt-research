# Prompt Architect Analysis: Content Creation Skill (A2) — v3

**Prompt analysed**: `experiments/A2-marketing-content/original/SKILL.md`
**Framework version**: Updated toolkit with voice-continuity guidance, anti-pattern catalogue, and two-mechanism model
**Date**: 2026-03-18

---

## Threshold Questions

### Is this a recognition-primed or investigation-required task?

This prompt covers multiple content types that sit on different sides of the boundary.

**Recognition-primed dimension**: Channel conventions — what a press release looks like, email footer requirements, SEO technical rules — are known frameworks from training. Applying them requires no discovery from novel data. The model already has these patterns and is matching them to input. For this dimension, pipeline separation adds overhead without benefit. Tier 2 optimisation (better epistemic stance, scope boundaries) is sufficient.

**Investigation-required dimension**: The voice-building dimension — what makes this specific product interesting, what emotional territory this specific audience occupies, what angle this specific launch deserves — cannot be produced without engaging the specific brief. The correct angle for a SaaS product launch targeting fatigued IT managers is not in the model's training data. It requires genuine engagement with the brief before any structural decisions are made.

**The critical complication**: This prompt collapses both dimensions into one operation. It treats a recognition-primed question (what does a blog post look like) and an investigation-required question (what should this blog post actually say and feel like) as the same task. The structural knowledge crowds out the investigative space entirely.

**Threshold conclusion**: The channel-convention work is recognition-primed. The voice-building work is investigation-required. The prompt treats everything as recognition-primed by loading templates and applying them. This is the root cause of the most significant limitation — not mode interference within the prompt, but the wrong task architecture from the outset.

### What type of task is this?

This is a **creative/voice-building task**. Quality is primarily about sustained authorial presence, tone, and conviction — whether the output sounds like someone who understands this product and this audience, or like a template being filled. The reference framework is explicit: for creative tasks, investigation and generation can be compatible, pipeline separation can fragment voice, and Tier 2 may outperform Tier 3 on the dimension that matters most.

This changes the analysis significantly. The standard "investigation + evaluation = toxic pair" logic applies differently here. The harmful separation for this task type is not investigation from generation — it is creative work from compliance work. That determines what any pipeline reconstruction should look like.

### Does the declared architecture match the actual architecture?

The prompt is honestly convergent throughout. There are no declared phases, no "Phase 1 / Phase 2" labels that promise sequential cognitive separation they cannot deliver. This is unusual — most sophisticated prompts fall into the declared architecture anti-pattern. This one doesn't.

What it does instead is present itself as "guidelines and frameworks" (the skill description says "Guidelines and frameworks for creating effective marketing content") while functioning as a generation prompt loaded into a live context. This framing mismatch is subtler than phase-labelling. The reader thinks they're loading a reference document. The model uses it as generation instructions. The framing as reference rather than generative prompt may actually increase the template-following posture — reference documents carry a lookup-and-apply cognitive mode, not a create-from-first-principles mode.

---

## 1. What the Prompt is Actually Asking For

The prompt establishes a **template-completion posture** for what is fundamentally a **voice-building and generation task**.

The types of thinking actually required:
- **Investigation** — what makes this specific product interesting, what this specific audience cares about, what emotional territory the content should occupy (entirely absent from the prompt)
- **Generation** — produce content that creates genuine engagement and carries an authorial voice (nominally the intent, structurally suppressed)
- **Evaluation** — check against SEO rules, readability standards, character limits, keyword placement (heavily present throughout, interleaved with generation instructions)
- **Template-completion** — fill defined structural slots (the dominant posture the prompt actually establishes)

The generative intent is a single line in the skill description: "Draft marketing content across channels." Every section after that establishes a convergent, compliance-checking, template-filling posture. The model receives a brief, pattern-matches it to the nearest template, fills the slots while monitoring compliance criteria, and produces output that is structurally correct but cognitively hollow.

---

## 2. Where Modes Interfere

### A. Generation is outnumbered by evaluation — the compliance overlay

The Writing Best Practices section and SEO Fundamentals section function as evaluation criteria active during generation. While the model is attempting to write compelling copy, the following criteria are simultaneously in context:

> "Write at an 8th-grade reading level for broad audiences"
> "Use short paragraphs (2-4 sentences)"
> "Include subheadings every 200-300 words"
> "Write in active voice"
> "Use the primary keyword in: headline, first paragraph, one subheading, meta description, URL slug"
> "Include at least one data point, example, or quote per section"

This is generation + evaluation mixed in a single context. The evaluation criteria do not merely add load — they shift the decision architecture from generative (what do I want to say, and how do I want to say it?) to criterion-referenced (which criteria am I meeting?). The model monitors compliance continuously rather than writing freely and checking compliance afterwards.

The output effect: the copy will be technically compliant. Active voice, appropriate paragraph length, keyword in the right places. What gets suppressed is the voice — the sense that someone with a point of view is writing this. Compliance monitoring allocates cognitive capacity away from the more expensive work of finding the right register, building emotional momentum, and making the reader feel understood.

**For creative tasks specifically**, this is the most damaging interference in the prompt. The productive split for this task type is content/craft from compliance — and this prompt has them fully merged.

### B. Template structures are implicit convergent anchors

Every content type is given a numbered structural template with fixed slot counts and word-count ranges:

> "2. Introduction (100-150 words) — hook the reader with a question, statistic, bold claim, or relatable scenario. State what the post will cover."
> "3. Body sections (3-5 sections) — each with a descriptive subheading (H2). Use H3 for subsections."
> "4. Conclusion (75-100 words) — summarize key takeaways, reinforce the main message, include a call to action."

The reference framework is direct on this: output structure carries mode. Templates with fixed slots push toward convergent completion behaviour — "fill in all the boxes" — regardless of what the boxes are about. For convergent formats (press releases, email footers, case study snapshots) where the format is genuinely conventional, templates are appropriate. For divergent formats (blog post narrative, social media voice), the templates constrain the model to a mechanical shape when it should be finding the shape that fits this specific piece.

A product launch for a complex developer tool might want a long setup section, a short payoff. A simple consumer product might want brevity throughout. The 3-5 body sections / 100-150 word introduction template will produce the same rhythm regardless.

### C. Numeric anchors throughout — at least fifteen

The prompt contains: 60 characters (headline), 100-150 words (introduction), 3-5 sections (blog body), 200-300 words (subheading frequency), 75-100 words (conclusion), 160 characters (meta description), 3-5 hashtags, 50 characters (subject line), 2-3 content blocks (email), 3-4 value propositions (landing page), 2-4 sentences (paragraph), 1,300 characters (LinkedIn sweet spot), 80 characters (Facebook link posts), 2-3 internal links, 1-2 external links.

Every one is a target. The model will gravitate to midpoints. A simple launch brief and a complex technical migration announcement will produce blog posts with the same section count, similar word counts, and the same structural rhythm. Natural variation — which the framework identifies as a health signal — will be fully suppressed. Uniformity of output structure across varied inputs signals mechanical execution.

---

## 3. Anti-Patterns That Look Like Good Practice

### Anti-pattern 1: Prescribed threads posed as open questions — the headline formulas

The Headline Formulas section presents seven specific patterns with fully worked examples:

> "How to [achieve result] [without common obstacle]" — "How to Double Your Email Open Rates Without Sending More Emails"
> "[Number] [adjective] ways to [achieve result]" — "7 Proven Ways to Reduce Customer Churn"
> "Why [common belief] is wrong (and what to do instead)"

This looks like creative guidance. The examples are varied, the patterns are different. But this is the anti-pattern of prescribed threads posed as open questions. The model will pull toward these patterns because they are the most concrete, specific guidance in the prompt. The formula examples are more vivid than any principle-level guidance about what makes a headline work. The result is outputs that reach for formula headlines — which is exactly what the model would do without the prompt, making this section actively harmful: it narrows to a specific set of formulaic shapes while appearing to provide creative latitude.

A lens version would ask: what gap does this headline need to open in the reader's mind? What specific value does it promise? What assumption does it challenge? These guide *how to think about the headline* without prescribing the shape the headline takes.

### Anti-pattern 2: Vivid seed examples bleed backward through the generation context

The Hook Formulas section gives six specific formula types with fully written examples:

> "Surprising statistic: '73% of marketers say their biggest challenge is not budget — it is focus.'"
> "Bold claim: 'Most landing pages lose half their visitors in the first three seconds.'"

These are vivid, specific, ready-to-use. They are in context during the entire generation of any marketing content this skill is loaded for. A model writing an opening for a logistics software launch will have these examples active in its context window. The pull toward these patterns is strong precisely because they are fully formed rather than abstract. The "surprising statistic" and "bold claim" framings will recur at a rate not warranted by the content — the model reaches for familiar patterns rather than finding the opening this specific piece needs.

### Anti-pattern 3: The SEO checklist is a criterion gate inside generation

The On-Page SEO Checklist is a checklist:

> "Title tag: under 60 characters, includes primary keyword"
> "Meta description: under 160 characters, includes primary keyword, compels click"
> "H1: one per page, matches or closely reflects the title tag"
> "Image alt text: descriptive, includes keyword where relevant"
> "Internal links: 2-3 links to related content on your site"

This functions as a criterion gate inside the generation context. The model cannot "move past" this checklist — it is simultaneously in context with the generation task. The checklist converts a generation context into a generation-plus-evaluation context. The model does not write and then check; it writes while checking, allocating part of its generative capacity to compliance monitoring throughout.

---

## 4. The Voice-Continuity Question

This is a creative writing task. Voice-continuity deserves specific analysis.

**The fundamental problem**: the prompt has no investigation phase. There is nothing that guides the model to engage with the brief before structural decisions are made. The model receives a product brief and immediately begins filling templates. Voice is not something that can be prescribed into a template — it emerges from genuine engagement with the material. "What makes this product interesting? What does the audience feel? What register will earn their trust?" — none of these questions appear anywhere in the prompt.

The reference framework is explicit on this: "the investigation IS the voice-finding process. The writer discovers the voice by engaging with the product, the audience, the emotional territory." When that investigation phase is absent, the model begins writing without having developed a voice. The template fills the gap — the voice defaults to "competent marketing professional" because the template is what's most active in context.

**What this produces**: copy that sounds like marketing content rather than copy that sounds like this specific product. The distinctive angle — the human story, the challenger framing, the vulnerability that builds trust — only emerges when the model has had space to find it before structure is imposed. This prompt imposes structure at step zero.

**Voice and pipeline separation**: The reference framework notes empirically that in the A2 experiment, Tier 2 (single context with scope boundaries) produced stronger voice than Tier 3 (four-agent pipeline). This is the voice-continuity effect: pipeline separation cleaned the context, but it also cleaned the voice — each agent started fresh and had to reconstruct voice from descriptions rather than carry it forward as lived experience. This matters for the Tier 3 recommendation.

**The correct split for this task type** is content/craft from compliance — not thinking from writing, and not investigation from generation. A pipeline that separates the creative work (exploration + writing in a single agent that can develop voice) from the compliance work (SEO, formatting, channel conventions in a separate agent that refines without suppressing) will outperform one that separates thinking from writing.

---

## 5. Seeds vs Lenses — Full Inventory

| Location | Type | Effect |
|---|---|---|
| Blog post structure | Seed (fixed template) | Constrains structure to 5 specific elements with word counts |
| Social media structure | Seed (fixed template) | Constrains to hook/body/CTA/hashtags with counts |
| Email newsletter structure | Seed (fixed template) | Appropriate — email conventions are genuinely rigid |
| Landing page structure | Seed (fixed template) | Partially appropriate — landing pages have structural conventions |
| Press release structure | Seed (fixed template) | Appropriate — press releases have strict conventions |
| Case study structure | Seed (fixed template) | Appropriate — case study format is conventional |
| Headline formulas | Seed (prescribes shapes) | Harmful for divergent generation — constrains to 7 patterns |
| Hook formulas | Seed (prescribes shapes) | Harmful for divergent generation — vivid examples pull toward patterns |
| SEO keyword placement | Seed (prescribes locations) | Appropriate for SEO — these are genuine technical requirements |
| CTA examples by context | Seed (prescribes copy) | Harmful — constrains CTA language to the listed examples |

The pattern: seeds are appropriate for formats with genuine conventions (press releases, emails, case studies, technical SEO). They are harmful for divergent creative work (blog post narrative shape, headline generation, opening hook, CTA language). The prompt treats all formats identically.

---

## 6. What to Check for in the Output

**Voice uniformity across briefs**: Run the prompt on two different briefs — a simple consumer product and a complex B2B platform. Does the voice feel different? Does the opening of the B2B piece have a different register, rhythm, and emotional approach than the consumer piece? If both feel like "competent marketing content" with the same generic professional tone, the template-completion posture is dominating.

**Headline formula adherence**: Do generated headlines match the seven formula shapes? "How to...", "[Number] ways to...", "The Complete Guide to..." appearing repeatedly is the seed effect.

**Numeric uniformity**: Compare section count, introduction word count, and conclusion word count across multiple runs on different briefs. If these are similar regardless of brief complexity, the anchors are dominating.

**Opening hooks**: Are they drawn from the six formula types? Surprising statistic, contrarian statement, question, scenario, bold claim, story opening — do these rotate predictably? That's the hook formula seed at work.

**The compliance feel**: Read a generated blog post and ask: does this feel like someone who has something to say about this product, or like someone filling out a form correctly? The template-filling posture produces output that passes all structural criteria while missing the animating quality — the sense that the writer cares about this specific thing.

---

## 7. What to Do About It

### Prompt-level optimisation (Tier 2)

Tier 2 is the recommended starting point for this task type. Given the voice-continuity evidence, a well-structured single-context prompt with the right epistemic stance may outperform a pipeline on the dimension that matters most (voice). The following interventions, applied together, should produce meaningful improvement:

**1. Add an investigation boundary before any template.** This is the highest-leverage intervention. Before any structural guidance, add a section that establishes an investigative epistemic stance:

"Before any structure, engage with this brief. What makes this product genuinely interesting? What does this audience actually care about? What is the emotional experience of the problem this product solves? What angle would make someone stop and read? Explore before you structure. The structure should serve what you find, not the reverse."

This one addition changes the cognitive posture from template-completion to investigation-led generation. The templates become options to reach for after the angle is found, not the first thing in context.

**2. Replace numeric ranges with qualitative guidance.** Remove all word counts, section counts, and character limits from the generative sections. Replace with qualitative principles: "as long as the topic warrants — let the content's logic dictate the length." Keep technical SEO requirements (meta description character limits, title tag length) because these are genuine platform constraints, not creative anchors.

**3. Move compliance criteria to a post-generation phase.** Restructure so evaluation criteria come after generation instructions, with an explicit scope boundary: "Write the content for the reader first. Once the draft exists, check it against the guidelines below." This is a scope boundary — lightweight, but it changes the order in which criteria enter the cognitive context.

**4. Replace headline formulas with lenses.** Replace the seven formula patterns with: "What gap does this headline need to open in the reader's mind? What specific outcome does it promise? What assumption does it challenge or confirm? Find the headline that fits this specific product and audience — it may match one of these familiar patterns or it may not." Keep the formula examples as illustrations, not prescriptions, and add explicit framing that they are starting points not targets.

**5. Remove or relocate CTA examples by context.** The specific CTA copy examples ("Read our complete guide to [topic]", "Start free trial") are too prescriptive for divergent creative work. Replace with principles about what effective CTAs accomplish for each context.

**Trade-off**: Tier 2 is the appropriate recommendation for this task type given the voice-continuity finding. A more structured pipeline (Tier 3) risks fragmenting voice even while improving technical dimensions like specificity, data interpretation, and SEO. If the primary quality criterion is voice and sustained authorial presence, Tier 2 with a strong investigative stance and compliance separation is the correct intervention.

### Pipeline reconstruction (Tier 3)

Tier 3 is appropriate if the primary quality criterion is technical execution rather than voice — or if the use case is high-volume production where consistent structure matters more than distinctive voice.

The split must be content/craft from compliance, not investigation from generation:

**Stage 1: Creative Agent** — Receives the brief. Investigates what makes this product interesting, finds the angle, writes the draft. Investigation and generation in a single context so voice can develop through engagement with the material. No compliance criteria in context. Output: the draft plus a brief note on the angle and tone discovered.

**Stage 2: Compliance Editor** — Receives the draft and the original brief's technical requirements. Applies SEO, channel formatting, character limits, CTA placement. Does not rewrite for voice — refines for distribution. Output: the polished draft.

**What this pipeline is not**: it is not a four-stage pipeline separating brief normalisation, angle ideation, concept selection, drafting, and copy optimisation. That level of separation fragments the voice-finding process across too many context boundaries. The voice that emerges from genuine engagement with the material in Stage 1 should not be compressed, handed off, reconstructed, and handed off again. The creative work needs sustained engagement in a single context.

**Handoff design**: Between Stage 1 and Stage 2, pass the complete draft alongside the technical requirements from the original brief (keywords, channel, audience). Do not compress the draft to a structured summary — the draft itself is the handoff, and for creative work, the prose carries the voice. The Stage 2 editor should receive the same material a human copy editor would receive: the full draft and the distribution requirements.

---

## Composition Signature

This is a single skill prompt loaded into a generation context. No multi-agent composition to analyse.

| Component | Cognitive Mode | Role |
|---|---|---|
| Content type templates | Convergent (template-filling) | Prescribes output structure |
| Writing best practices | Evaluation (criteria-checking) | Active during generation |
| SEO fundamentals / checklist | Evaluation (compliance-checking) | Active during generation |
| Headline/hook formulas | Convergent (seed-based) | Prescribes creative output shapes |
| CTA examples | Convergent (seed-based) | Prescribes creative copy |
| Actual generation task | Generation (divergent) | The intended output |
| Missing: investigation phase | — | Absent entirely |

**Primary conflict**: Convergent + evaluation posture (all sections) against divergent generation (the task). The generative intent is the single line "Draft marketing content." Everything else in the prompt establishes a posture that works against it.

**Secondary issue**: The posture established is appropriate for formats with genuine conventions (press releases, emails, technical SEO) but harmful for formats requiring distinctive voice (blog posts, social media content). The prompt treats all formats identically.

---

## Summary

The SKILL.md prompt has a clear structure problem but the problem is not mode interference in the classic investigation-evaluation sense. It is the wrong task architecture: a prompt built for recognition-primed template completion being used for a task that requires investigation-led voice building.

The most important single intervention is adding an investigation boundary before any template. The most important structural understanding is that for this task type, investigation and generation should remain in the same context — the voice emerges from their interaction, not from separating them. The productive pipeline split is creative work from compliance work, which is a smaller, later separation than most analytical-task pipelines.

The anti-patterns are clear: headline formulas are prescribed threads posed as open questions; the SEO checklist is a criterion gate inside generation; the numeric anchors throughout will produce mechanical uniformity. These are addressable at Tier 2. Pipeline reconstruction (Tier 3) should be considered only with the content/craft vs compliance split, and should be expected to score higher on technical dimensions while potentially producing weaker voice — consistent with the empirical finding noted in the reference framework.

---

*Analysis produced using the updated toolkit: `toolkit/prompt-architect-agent.md` and `toolkit/cognitive-stance-reference.md`*
