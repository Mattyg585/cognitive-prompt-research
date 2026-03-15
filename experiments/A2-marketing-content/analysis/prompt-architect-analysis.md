# Prompt Architect Analysis: Content Creation Skill (A2)

## 1. What the prompt is actually asking for

This prompt is framed as a **reference guide** but used as a **generation prompt**. It's loaded into context when the model needs to write marketing content — a blog post, social media copy, an email newsletter, etc. The actual cognitive task is **generation**: produce compelling content for a specific product, audience, and channel.

But the prompt doesn't establish a generative posture. It establishes a **template-completion posture**. The model is given rigid structural templates with fixed slot counts, word-count ranges, and character limits for every content type — and then expected to produce creative, engaging copy within those constraints.

The thinking required:
- **Investigation** — understand the product, audience, and what makes this story interesting (not present in the prompt at all)
- **Generation** — write content that connects with readers (nominally the goal, but structurally suppressed)
- **Evaluation** — simultaneously check against SEO rules, readability guidelines, character limits, keyword placement, and best practices (heavily present, interleaved throughout)
- **Template-filling** — complete each slot in the prescribed structure (the dominant posture the prompt actually establishes)

## 2. Where modes interfere

### A. Template slots suppress generative freedom

The entire prompt is structured as fixed-slot templates. Every content type has a numbered sequence of required elements with specific counts:

> `3. **Body sections** (3-5 sections) — each with a descriptive subheading (H2). Use H3 for subsections. One core idea per section with supporting evidence, examples, or data.`
> `4. **Conclusion** (75-100 words) — summarize key takeaways, reinforce the main message, include a call to action.`

This is the "output structure carries mode" pattern. The templates with fixed slots push toward convergent completion — "fill in all the boxes" — regardless of what the boxes are about. The model will produce a blog post with exactly 4 body sections (midpoint of 3-5), an introduction of exactly 125 words (midpoint of 100-150), and a conclusion of exactly 87 words (midpoint of 75-100). Every time. Regardless of whether the product launch warrants a tight 3-section post or an expansive 6-section one.

For **convergent** work (press release formatting, email footer structure), fixed templates are appropriate — those formats genuinely have rigid conventions. For **divergent** work (blog post narrative, social media voice), the templates constrain the model to a mechanical structure when it should be finding the right shape for *this specific piece*.

### B. Numeric anchors throughout

The prompt contains at least 15 specific numeric targets:

- Headlines: 60 characters
- Introduction: 100-150 words
- Body: 3-5 sections
- Subheadings: every 200-300 words
- Conclusion: 75-100 words
- Meta description: 160 characters
- Hashtags: 3-5
- Subject line: 50 characters
- Email body: 2-3 content blocks
- Value propositions: 3-4
- Paragraphs: 2-4 sentences
- LinkedIn: 1,300 characters
- Facebook: 80 characters
- Internal links: 2-3
- External links: 1-2

Every one of these becomes a target. The model will hit the midpoint of every range. Natural variation — the health signal that the output is responding to the input rather than to the prompt — will be suppressed. A simple product launch and a complex enterprise platform will get blog posts with the same word count, section count, and structure.

### C. Headline/hook formulas are seeds constraining creative generation

Lines 119-134 provide 7 headline formulas and 6 hook formulas with specific examples:

> `- **How to [achieve result] [without common obstacle]** — "How to Double Your Email Open Rates Without Sending More Emails"`
> `- **[Number] [adjective] ways to [achieve result]** — "7 Proven Ways to Reduce Customer Churn"`

These are classic **seeds** applied to **divergent work**. The model will select from these formulas rather than finding the headline that's right for the specific product. A product launch announcement doesn't naturally fit "How to..." or "X Ways to..." — but the seeds will pull the model toward these patterns because they're the most concrete guidance available.

The prompt should provide **lenses** instead: what makes a headline work (creates tension, promises specific value, matches the reader's mental state) rather than what shapes a headline takes.

### D. Evaluation criteria interleaved with generation

The "Writing Best Practices" section (lines 63-91) and "SEO Fundamentals" section (lines 93-116) function as **evaluation criteria present during generation**. While the model is trying to write compelling copy, it's simultaneously checking:

- Am I at 8th-grade reading level?
- Are my paragraphs 2-4 sentences?
- Have I used active voice?
- Did I put the primary keyword in the first paragraph, one subheading, and the meta description?
- Do I have 2-3 internal links?

This is generation + evaluation mixing. The evaluation criteria become a **convergent overlay** on divergent creative work. The model optimises for checklist compliance rather than for reader engagement. The output will be technically correct — proper keyword density, appropriate reading level, correct paragraph length — but the voice, the emotional arc, the thing that makes someone actually *want to keep reading* gets suppressed because the model is allocating cognitive capacity to compliance checking.

### E. No investigation phase

The prompt goes straight to structure and format. There's no guidance for understanding the brief — what makes this product interesting, what pain the audience feels, what the emotional journey of the reader should be. The model jumps directly from "here's a brief" to "fill in the template."

This means the model never explores the space divergently before committing to a structure. It doesn't think about whether the product launch is best told as a problem-solution narrative, a vision piece, a data-driven credibility play, or a human story. It just starts filling in: Headline, Introduction (100-150 words), Body sections (3-5)...

The missing investigation phase means the generative work has no strategic foundation. The model produces structurally correct content without first understanding what the content needs to *do*.

## 3. What to check for in the output

**Run the prompt on two different briefs — one simple, one complex.** If both blog posts have the same number of sections, similar word counts, and the same structural rhythm, the templates are dominating.

**Check the headlines.** Do they match the formula patterns ("How to...", "X Ways to...", "The Complete Guide to...")? If so, the seeds are anchoring.

**Read for voice.** Is the output competent-but-generic, or does it sound like it *understands* the specific product and audience? Template-completion produces "correct marketing copy." Actual generation produces copy that sounds like someone who's excited about this specific thing.

**Check the introduction.** Count the words. If it's 120-130 words (midpoint of 100-150), the anchor is working. More importantly: does it hook you? Or does it feel like a template being filled?

**Look at the CTA.** Is it one of the examples from lines 146-150, slightly adapted? Or does it emerge naturally from the content's emotional arc?

## 4. What to do about it

### Prompt-level optimisation (Tier 2)

These changes stay within the single-prompt structure but reduce the interference:

1. **Replace numeric ranges with qualitative guidance.** "100-150 words" → "concise enough to respect the reader's time, long enough to earn their attention." "3-5 sections" → "as many sections as the topic warrants — let the content dictate the structure." This removes the anchors and lets the output respond to the input.

2. **Replace headline/hook formulas with lenses.** Instead of 7 formula patterns, guide *what makes a headline work*: "The headline should create a gap between what the reader knows and what they want to know. It should promise specific value for the reader's time." This opens creative space rather than constraining it.

3. **Add an explicit investigation-before-generation boundary.** Before any template, add: "First, understand the brief. What makes this product interesting? What does the audience care about? What's the emotional journey? Then choose the right structure for *this specific piece* — not every blog post needs the same shape." This creates space for divergent exploration before convergent execution.

4. **Move SEO and best practices to a post-generation checklist.** Separate the evaluation criteria from the generative context. "Write the content first for the reader. Then review against these guidelines." This is a scope boundary — lightweight but effective.

5. **Remove the fixed template structures for divergent content types.** Keep templates for genuinely convergent formats (press release, case study snapshot) where the format is conventional. Replace templates for divergent formats (blog post, social media) with principles and lenses.

### Pipeline reconstruction (Tier 3)

The fundamental problem — generation + evaluation + template-filling all in one context — likely needs structural separation for best results:

**Stage 1: Brief Explorer** (investigation, divergent) — Read the product brief. Understand the product, the audience, the competitive landscape, the emotional pain points. No structure, no template — just exploration. Output: a strategic brief noting what's interesting, what resonates, what the angle should be.

**Stage 2: Content Architect** (synthesis, convergent) — Take the strategic brief and decide on the narrative arc, structure, and voice for this specific piece. Not a generic template — a bespoke structure for this content. Output: an outline with the narrative logic, key beats, and tone.

**Stage 3: Writer** (generation, divergent) — Write the actual content based on the outline. Focus entirely on voice, flow, engagement, and the reader's experience. No SEO checklist, no word-count targets, no evaluation criteria in context. Just write. Output: the draft.

**Stage 4: Editor** (evaluation, convergent) — Take the draft and polish. Apply SEO requirements, check CTA placement, verify keyword usage, adjust for channel conventions. This is where the convergent checklist work belongs — after the creative work is done, where it can refine without suppressing.

**Why the pipeline is worth it here:** The core tension in this prompt is that creative writing and checklist compliance are fundamentally different cognitive modes. The prompt treats them as one task. Separating the "understand and create" phases from the "check and polish" phases lets each phase do its best work. The explorer finds the real story. The writer tells it with conviction. The editor makes it findable and compliant. No phase is fighting against the posture of another.

**The handoff design matters.** Between Stage 1 and Stage 2, pass structured observations (not exploratory prose). Between Stage 2 and Stage 3, pass the outline and voice notes (not the analysis that produced them). Between Stage 3 and Stage 4, pass the draft with the original brief's SEO requirements. Each handoff strips cognitive residue from the previous phase.

## Composition signature

This is a single skill prompt, not a multi-agent system. No composition analysis needed. The conflicts are all internal to the single prompt.

| Component | Cognitive Mode |
|-----------|---------------|
| Content type templates | Convergent (template-filling) |
| Writing best practices | Evaluation (criteria-checking) |
| SEO fundamentals | Evaluation (compliance-checking) |
| Headline/hook formulas | Convergent (seed-based selection) |
| CTA best practices | Evaluation (criteria-checking) |
| Actual task (write content) | Generation (divergent) |

**Primary conflict:** The prompt establishes a convergent template-filling + evaluation posture for what is fundamentally divergent generative work. Every section of the prompt pushes toward convergence except the actual task itself. The generative intent is outnumbered and outweighed by convergent instructions.
