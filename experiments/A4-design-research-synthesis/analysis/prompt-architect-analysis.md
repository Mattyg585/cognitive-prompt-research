# Prompt Architect Analysis: Design Research Synthesis

## 1. What the Prompt Is Actually Asking For

This prompt asks the model to perform five distinct types of thinking simultaneously in a single pass:

- **Investigation** — reading transcripts, noticing patterns, following threads across participants
- **Structuring** — grouping observations into themes, categorising segments
- **Synthesis** — compressing observations into insights and a coherent narrative
- **Evaluation** — assessing impact and effort of opportunities, prioritising recommendations
- **Reframing** — translating findings for product/business stakeholders (Executive Summary, Recommendations)

All five are subordinated to a rigid output template that determines the shape of the output before any data is read.

## 2. Where Modes Interfere

### 2.1 The Output Template Forces Premature Convergence (High)

The template is the most significant interference source. It defines the structure of the output — numbered theme slots, a fixed evidence format (2 quotes per theme), an Impact/Effort grid, exactly 3 prioritised recommendations — before any data has been read. The model reads the transcripts extractively, looking for "things that could be Theme 1" rather than exploring openly.

**Mechanism**: The template acts as a convergent container around fundamentally divergent work. Research synthesis should begin with open investigation (what's in this data?), progress through structuring (how do these observations relate?), then synthesis (what does this mean?), and finally reframing (what should we do about it?). The template collapses this sequence into a single simultaneous operation: "fill in these boxes."

**Severity**: High. This is the classic "output structure carries mode" finding. The template isn't just formatting the output — it's changing the KIND of thinking the model does. Investigation becomes extraction. Synthesis becomes slot-filling.

### 2.2 Investigation + Evaluation Are Simultaneous (High)

The Insights → Opportunities table forces evaluation (Impact: High/Med/Low, Effort: High/Med/Low) alongside investigation and synthesis. This biases investigation toward patterns that are easy to evaluate — clear, actionable findings get surfaced while subtle, ambiguous, or surprising patterns get dropped because they don't fit neatly into an Impact/Effort grid.

**Mechanism**: The Impact/Effort columns become a pre-filter on investigation. The model only surfaces insights it can already classify by impact and effort. Novel findings that resist easy classification get suppressed. This is the classic investigation + evaluation toxic pair.

### 2.3 The Insights-to-Opportunities Table Conflates Four Types of Thinking (Moderate)

Each row of the table requires: insight (synthesis), opportunity (generation), impact (evaluation), effort (evaluation). These are forced into a linear one-to-one mapping — each insight gets exactly one opportunity, one impact rating, one effort rating. Reality is messier: one insight might suggest three opportunities; two insights might converge on the same opportunity; some insights have no clear opportunity but are important to document.

**Mechanism**: The grid structure forces premature commitment and artificial linearity on a fundamentally networked set of relationships.

### 2.4 The Executive Summary Appears First (Moderate)

The Executive Summary is the first substantive section but requires the entire analysis to be done. In a single-pass generation, the model must commit to a narrative framing before building the evidence base. This anchors everything that follows.

**Mechanism**: Whatever the model writes in the Executive Summary becomes the lens through which it writes the rest. If the summary emphasises "adoption drop-off," the themes will cluster around adoption. If it emphasises "feature gap," themes cluster differently. The summary should be the LAST thing written, as a synthesis of the synthesis.

### 2.5 Implicit Count Anchors (Moderate)

- The template implies 3-5 themes (Theme 1, Theme 2, "[Same format]")
- Exactly 3 recommendations (High, Medium, Lower priority)
- 2 quotes per theme (Supporting Evidence shows 2 bullets)
- The User Segments table implies multiple segments

**Mechanism**: These counts anchor the model regardless of what the data warrants. Six interviews might yield 2 strong themes or 7. The data should determine the count, not the template.

### 2.6 Recommendations Mix Generation with Evaluation (Moderate)

The Recommendations section asks the model to both generate actionable recommendations AND prioritise them (High/Medium/Lower) in the same breath. The prioritisation becomes a constraint on generation — the model generates recommendations that fit neatly into a priority hierarchy rather than generating the best recommendations and then assessing priority separately.

## 3. What to Check For in the Output

- **Theme count uniformity**: Run on different datasets. If theme count is always 3-5 regardless of data richness, the template is anchoring.
- **Quote selection**: Are quotes genuinely the most revealing, or are they the most theme-confirmatory? Extractive investigation selects quotes that support pre-committed themes.
- **Insight-opportunity linearity**: Does every insight map 1:1 to an opportunity? If so, the grid is forcing artificial correspondence.
- **Executive Summary coherence with body**: Does the body feel like it was written to support the summary, or does the summary feel like it emerged from the body? If the former, premature commitment is at work.
- **Missing surprises**: The most diagnostic signal. After reading the output, re-read the transcripts. Are there interesting patterns in the data that the synthesis missed? If so, the template's convergent structure likely filtered them out.
- **Segment artificiality**: Do the user segments feel genuinely distinct, or do they feel forced to fill the table?

## 4. What to Do About It

### Tier 2 — Prompt-Level Optimisation

1. **Loosen the template to be responsive rather than fixed**: Replace fixed-slot themes with "Surface the themes you find — as many or few as the data warrants. Some themes may have extensive evidence; others may be emerging patterns worth noting with less support."
2. **Move the Executive Summary to the end**: Relabel as "Summary" and place it after all analysis sections. Let it be a genuine synthesis rather than a premature anchor.
3. **Replace the Insights → Opportunities grid with a narrative section**: "For each significant insight, explore what it suggests for the product. Some insights may point to clear opportunities; others may raise questions that need further investigation. Not every insight has an actionable recommendation."
4. **Remove Impact/Effort/Size columns**: These force evaluation during investigation. If impact assessment is needed, it should be a separate section after all insights are documented.
5. **Add a scope boundary**: Before the output template, add: "Start from the data, not from the template. Read the research material fully before structuring your response. Let the patterns emerge from the data rather than fitting data into pre-existing categories."
6. **Remove implicit count anchors**: Replace "2 quotes per theme" with "supporting evidence as warranted." Replace exactly 3 recommendations with "recommendations — ordered by what the data most strongly supports."

### Tier 3 — Pipeline Reconstruction

This experiment is where pipeline reconstruction should show the most dramatic improvement. The five types of thinking are genuinely incompatible when simultaneous, but they sequence naturally.

**Agent 1 — Data Reader** (Investigation + light Structuring)
- Receives: raw interview transcripts
- Does: reads each transcript openly, noting what's interesting — patterns, contradictions, surprising moments, emotional signals, repeated language. Uses lenses: "What are people actually doing vs what they say they do? Where do participants agree? Where do they contradict each other? What's unsaid?"
- Produces: structured observations per participant — key quotes, behavioural observations, pain points, workarounds, emotional moments. NOT themes (that's premature synthesis).
- Why separate: investigation without theme categories or output structure in context allows open exploration. The model follows threads instead of extracting for pre-committed categories.

**Agent 2 — Pattern Synthesiser** (Synthesis + Structuring)
- Receives: structured observations from Agent 1
- Does: looks across all participant observations for patterns — what clusters? What contradicts? What's surprising? Identifies themes, but also identifies tensions, contradictions, and open questions.
- Produces: themes with evidence mapping, inter-theme relationships, contradictions, and unresolved questions. Themes are sized by the evidence (some large, some emerging).
- Why separate: synthesis without evaluation criteria (impact/effort) or audience reframing (recommendations) in context allows genuine pattern recognition. The model can identify a theme without immediately having to judge its business value.

**Agent 3 — Strategic Translator** (Reframing + Generation + light Evaluation)
- Receives: themes and patterns from Agent 2
- Does: translates research findings into product/business implications. What do these patterns mean for the product? What opportunities do they suggest? What should be investigated further?
- Produces: insights with implications, opportunities, recommendations, open questions. Priority emerges from the strength of the evidence, not a forced High/Med/Low grid.
- Why separate: reframing and generation work best when they receive pre-synthesised patterns. The model doesn't need to simultaneously investigate, synthesise, AND translate. It can focus on "what does this mean for the audience?"

**Handoff Design**:
- Agent 1 → Agent 2: structured observations (bullets per participant, not prose). Strips investigative tone.
- Agent 2 → Agent 3: themes with evidence mapping (structured, not narrative). Strips synthesis process.

**Execution**: Sequential. Each agent depends on the previous agent's full output.

## 5. Composition Signature

Single-prompt skill, no runtime composition concerns. Within the prompt:
- Investigation + Evaluation (incompatible — simultaneous)
- Investigation + Synthesis (incompatible — simultaneous, premature convergence)
- Synthesis + Reframing (moderately compatible but simultaneous execution degrades both)
- Generation + Evaluation (moderately compatible but the grid structure forces them into conflict)

## 6. Overall Assessment

**Severity: High.** This is the strongest candidate for demonstrating pipeline improvement. The prompt asks for five types of thinking simultaneously, all constrained by a rigid output template that forces premature convergence. The template doesn't just format output — it changes the kind of thinking the model does.

**Expected experimental outcome**: Tier 2 should show moderate improvement (loosened template allows more natural synthesis). Tier 3 should show a qualitative leap — the separation of investigation from synthesis from reframing should produce themes and insights that the monolithic prompt cannot reach, because the monolithic version pre-filters investigation through the template's convergent structure.

The key signal to watch: does the pipeline version find patterns in the interview data that the monolithic version misses? Not just more themes, but DIFFERENT themes — ones that emerge from open investigation rather than template-shaped extraction.
