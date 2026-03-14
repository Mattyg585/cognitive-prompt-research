# Blind Evaluation: TaskFlow Usage Drop-Off Research Synthesis

**Task**: Synthesise 6 user interviews about TaskFlow (project management SaaS) into themes, insights, and recommendations. Research question: why do teams adopt TaskFlow enthusiastically but usage drops off after 3-4 months?

**Evaluator note**: Three outputs (A, B, C) were evaluated independently against the rubric's absolute scale. I read all three completely before scoring.

---

## Step 1: Initial Impressions

**Output A** reads like a well-structured consulting deliverable. It follows a clear template: executive summary, themes with prevalence counts and quotes, an insights-to-opportunities table, user segments, prioritised recommendations, research questions, and methodology notes. It is comprehensive and professionally formatted.

**Output B** reads like a senior researcher wrote it. The themes are fewer but more deeply argued. Each theme is developed as a narrative with connective reasoning rather than a list of evidence. It includes a separate "Insights and Opportunities" section that synthesises across themes rather than just listing them, a user segmentation section, detailed recommendations, and probing research questions. It has a discursive summary that builds an argument.

**Output C** reads like a strategic research report written for a product leadership audience. It organises findings as architecturally-framed insights, each with explicit "what this means for the product" and "what this means for the business" subsections plus evidence-strength ratings. It includes a "Tensions and Trade-offs" section, opportunities framed as strategic pivots, confidence-rated recommendations, and open questions. It builds a sustained argument about structural mismatch.

---

## Step 2: Dimension Scoring

### Depth (1-5)

**Output A: 3**
Output A finds all the expected themes competently. Update friction, compliance death spiral, feature overload, integration gap, admin-vs-user gap, notification failure -- these are the patterns a skilled researcher would identify. The themes are clearly stated and well-evidenced. However, the analysis stays at the level of pattern identification. The executive summary names the "vicious cycle" dynamic but the theme-by-theme treatment doesn't develop the structural relationships between themes. Each theme is treated as a separate finding rather than as a facet of a larger dynamic.

**Output B: 4**
Output B goes meaningfully deeper. Theme 1 (update friction) doesn't just document the four-click problem -- it identifies the value asymmetry: "The tool asks for contributions from the people it serves least." Theme 5 (visibility paradox) names the feedback loop precisely and traces the causal chain: unreliable data makes reports useless, which removes manager incentive, which removes the last source of pressure on contributors. The Insights and Opportunities section synthesises across themes to identify the structural nature of the problem: "TaskFlow's drop-off problem is structural, not cosmetic." The framing of Raj as "a rational actor choosing lower-friction alternatives" reframes the problem from user failure to product design failure. The summary builds an argument with a clear strategic conclusion.

**Output C: 5**
Output C achieves genuine reframing. Finding 2 ("Partial adoption does not produce partial value -- it produces negative value") articulates something none of the other outputs name: this is not a linear degradation but a threshold collapse. Finding 4 ("Users' workarounds collectively describe a product that does not yet exist") treats user workarounds not as coping mechanisms but as behavioural specifications for an unbuilt product -- a genuinely surprising analytical move. Finding 5 ("Power users experience a compound failure that occasional users avoid") inverts the expected narrative: the most engaged users are the most damaged, and their high engagement metrics may be masking imminent churn. The "Tensions and Trade-offs" section surfaces the "objectively better" paradox -- that the qualities that make the tool impressive in evaluation are the same qualities that make it burdensome in daily use, and this may be an irresolvable tension rather than an optimisable trade-off. These are insights that change how a product team would think about the problem.

### Specificity (1-5)

**Output A: 4**
Output A is well-grounded in the interview data. Every theme includes direct quotes from specific participants. The insights-to-opportunities table maps specific evidence to specific recommendations with impact/effort ratings. User segments are described with estimated proportions. Recommendations reference specific participants (P2, P3, P4, P5, P6) and specific interview moments. The methodology notes identify the specific sampling bias (3 of 6 are champions).

**Output B: 4**
Output B is similarly well-grounded. Quotes are used extensively and in context. The analysis traces specific causal chains through specific participant experiences -- Sarah's report-abandonment sequence, Marcus's "team view that's really Marcus's view," Deepa's transformation into "human integration layer." The Insights section references bright spots (board view, timeline view, mobile app) as specific evidence. The methodology section identifies the specific representational gap (4 of 6 are managers/leads, contributor perspective is indirect). One notable strength: the recommendation to make task updates "easier than the alternative" is a specific design criterion, not just "simpler."

**Output C: 5**
Output C achieves the highest specificity by grounding every claim in evidence and then pushing beyond evidence to traceable inferences. Each finding has an explicit evidence-strength rating ("well-supported," "emerging"), which is itself a specificity discipline. The "what this means for the product" and "what this means for the business" subsections translate findings into specific implications for specific audiences. Finding 5 includes a specific metric-gaming warning: "One participant registers as a daily active user while contributing almost no data" -- this translates a participant observation into a specific analytics problem the product team can investigate. The recommendation for a Slack bot with a specific interaction pattern ("/done auth module") provides a concrete product specification rather than a general direction. The open question about "invisible non-adopters" identifies a specific gap between engagement metrics and data-contribution metrics that is directly actionable.

### Completeness (1-5)

**Output A: 4**
Output A covers all major patterns in the data: update friction, compliance spiral, feature overload, integration gap, admin-user gap, and notification failure. It identifies four user segments. It provides ten specific opportunities with impact/effort ratings. It includes six research questions and a methodology critique. Nothing obvious is missing. The coverage is slightly too uniform -- each theme gets roughly equal treatment regardless of how strongly it is supported by the data.

**Output B: 5**
Output B covers the same ground but with more appropriate weighting. The first two themes (update friction, destination-vs-layer) get the most development because they are the most strongly supported patterns. The notification theme (less evidence) gets proportionally less space. The summary section synthesises rather than repeating, adding the "two directions" strategic frame (reduce friction vs. shift architecture) that gives the recommendations a hierarchy the flat list in Output A lacks. The methodology section is more substantive, identifying the specific analytical limitation of champions-describing-contributors and the implications for what the data can and cannot support.

**Output C: 5**
Output C achieves comprehensive coverage with strong weighting. The six findings are ordered by structural importance rather than prevalence, which gives the reader a clearer picture of what matters most. The "Tensions and Trade-offs" section adds coverage that neither A nor B provide -- specifically the tension between the sales motion and the retention motion, which is a business-level insight absent from both other outputs. The open question about "invisible non-adopters" identifies a coverage gap in the research itself that neither other output flags. The confidence ratings on recommendations provide a completeness discipline: the reader knows which recommendations are strongly supported and which are more speculative.

### Audience Awareness (1-5)

**Output A: 3**
Output A reads like a competent research deliverable. The structure (executive summary, themes, opportunities table, recommendations, research questions) is appropriate for a product team. The impact/effort matrix in the opportunities table is a useful artifact for prioritisation. However, the tone is somewhat neutral and report-like -- it presents findings rather than making a case. A product leader reading this would know what the users said but might not feel the urgency of the structural problem. The user segment descriptions are useful but the estimated percentages feel like placeholders rather than evidence-based estimates.

**Output B: 4**
Output B is more attuned to how a product team would receive and use the findings. The framing of Raj as "a rational actor" rather than a failed user reframes the problem in a way that prevents the product team from dismissing the findings as a training or onboarding issue. The distinction between "incremental improvements will produce incremental results" and "strategic reorientation" gives the audience a decision framework, not just data. The bright-spots paragraph near the end of the insights section anticipates a likely objection ("but users like our features!") and preemptively addresses it. The summary is written as an argument, building from diagnosis to implication to direction, which models how a product leader would need to communicate these findings internally.

**Output C: 5**
Output C is the most audience-aware. The dual-track structure ("what this means for the product" / "what this means for the business") explicitly addresses the two audiences who will read a research synthesis at this level: the product team and the business leadership. The "Tensions and Trade-offs" section anticipates the political reality: the sales team will resist simplification because feature density wins deals. By naming this tension explicitly, the output gives the product leader language to navigate an internal conversation rather than just data to present. The recommendation to "investigate" the lens architecture (rather than "build" it) shows understanding that a research synthesis cannot mandate strategic pivots -- it can only make the case and recommend exploration. The confidence ratings prevent a product team from treating all recommendations as equally validated, which is a failure mode of research reports that treat all findings as equally important.

---

## Step 3: Summary

| Dimension | Output A | Output B | Output C |
|-----------|----------|----------|----------|
| Depth | 3 | 4 | 5 |
| Specificity | 4 | 4 | 5 |
| Completeness | 4 | 5 | 5 |
| Audience Awareness | 3 | 4 | 5 |

**Overall preference**: C > B > A

**Key differences**:

Output A identifies the right patterns and organises them competently but stays at the level of pattern cataloguing. It tells you what users said; it does not build an argument about what it means.

Output B moves from cataloguing to analysis. It identifies structural dynamics (value asymmetry, feedback loops, rational actor framing) and builds an argument that the problem is structural, not cosmetic. It understands that the findings are interrelated, not independent.

Output C moves from analysis to strategic reframing. It treats user workarounds as product specifications. It identifies the "objectively better" paradox -- that evaluation-time quality and daily-use quality may be in genuine tension rather than just misaligned. It surfaces the tension between the sales motion and the retention motion, which is a business-level insight the other outputs don't reach. It provides confidence ratings that demonstrate understanding of the evidentiary limits of qualitative research. It writes for the actual decision-makers who will receive this document, not for a generic audience.

**Magnitude**: Large.

The difference between A and B is moderate -- B does the same work as A but with deeper analysis and better synthesis. Both are recognisably the same type of document.

The difference between B and C is a qualitative leap. C produces insights that reframe the problem rather than just characterising it. The "workarounds as specifications" insight, the non-linear value collapse insight, and the sales-vs-retention tension are the kinds of findings that change what a product team decides to do, not just how they prioritise their existing roadmap. C reads like it was written by someone who deeply understands both research methodology and the business context in which research findings land.

---

## Step 4: Diagnostic Observations

**Structural differences**: Output A uses a flat theme-by-theme structure with an opportunities matrix. Output B uses a narrative theme structure with a separate synthesis section. Output C uses a findings-with-dual-implications structure plus a tensions section. The structural choices themselves reveal something: A treats themes as independent items to catalogue; B treats them as connected findings to synthesise; C treats them as facets of a structural argument to build. The structure mirrors the depth of thinking.

**The "workarounds as specifications" move**: Output C's treatment of workarounds is the single most impressive analytical move across all three outputs. Every output notes that users have workarounds. A and B treat them as evidence of friction. C treats them as behavioural data about an unbuilt product: "They are specifications, written in behaviour, for the product people actually need." This reframes workarounds from a symptom to an asset. It is the kind of insight that would change a product strategy conversation.

**The non-linear collapse insight**: Output C's framing that partial adoption produces "negative value" rather than partial value is a genuine analytical contribution. A and B describe the compliance death spiral as a feedback loop (which it is), but C goes further: the value doesn't degrade linearly, it collapses once adoption drops below a threshold. This is a different mental model with different strategic implications -- it means incremental adoption improvements may produce no value improvement until they cross the threshold.

**The invisible non-adopter**: Output C identifies a specific danger that neither A nor B flags: users who appear active in engagement metrics (daily logins, mobile usage) but contribute almost no data. This is a concrete, testable hypothesis about a gap in the company's analytics that could change how they measure retention. It demonstrates understanding of how engagement metrics can be misleading.

**Evidence handling**: All three outputs use quotes from the interviews. A uses them as supporting evidence for pre-stated themes. B weaves them into narrative analysis. C uses them more sparingly but with greater analytical leverage -- each quote does more work. C also explicitly rates evidence strength, which none of the others do. This is a methodological sophistication that matters for how the findings will be received and actioned.

**What A does that B and C don't**: The impact/effort matrix in A's opportunities table is a useful practical artifact. Neither B nor C provides this. In a real product team context, this matrix would be immediately useful for sprint planning, even if the underlying analysis is shallower. A also provides user segment size estimates, which B and C are more cautious about. These are practical touches that serve a specific audience need.

**What B does that A doesn't**: B's methodology section is substantially more rigorous than A's. It identifies the specific analytical limitation that much contributor insight comes secondhand (champions describing teammates), names the sample size limitation explicitly, and notes the selection bias toward dissatisfaction. This level of methodological self-awareness helps the reader calibrate how much weight to place on the findings.

**Templated vs. emergent structure**: Output A feels like it was produced by filling a well-designed template. The sections are predictable, the prevalence counts are consistent, the opportunities table is neatly formatted. This is not a criticism -- it produces a useful document. But it means the structure came first and the analysis was fitted into it. Outputs B and C feel like the structure emerged from the analysis. The themes in B are titled as insights ("The update tax," "The champion gap") rather than categories. The findings in C are titled as assertions ("Partial adoption does not produce partial value -- it produces negative value"). These titling choices reveal deeper engagement with the material.

**Overall assessment**: This is a case where the gap between outputs is clear and meaningful. A is competent work that would be useful to a product team. B is strong analytical work that would change how a product team thinks about the problem. C is exceptional strategic work that would change what a product team decides to do about the problem. The progression from A to B to C is not just "more analysis" -- it is qualitatively different thinking at each level.
