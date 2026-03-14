# Second Evaluation: SecOps Incident Response Postmortem

## Context

**Task**: Write a blameless postmortem for a SEV1 incident where a customer data export endpoint was deployed with `@Public` instead of `@AdminOnly`, exposing 2,847 customer records for 11 days before a security researcher reported it.

**Outputs evaluated**:
- Output A (baseline)
- Output B (optimised)
- Output C (pipeline, final stage)

All scored independently against the rubric's absolute scale.

---

## Dimension 1: Depth (1-5)

### Output A: 3

Output A covers the expected ground. The 5 Whys analysis correctly walks from the proximate cause (wrong annotation) down to the architectural issue (permissive default). It identifies the key systemic gaps: testing blind spot, Snyk scope mismatch, no runtime detection. But it does this in a fairly linear, mechanical way. Each "why" advances one level, arriving at the framework default on the fifth why. It reads like a well-executed template rather than a genuine investigation. The Lessons Learned section is a single paragraph that summarises the findings without surfacing new insight beyond what the 5 Whys already stated.

### Output B: 4

Output B goes meaningfully beyond the expected. The root cause analysis abandons the linear 5 Whys format in favour of a branching causal structure with five independently articulated branches, each with its own analysis of why that particular safeguard failed. It finds things that Output A does not: the observation that the `@Public` annotation "appeared intentional in context" during code review, the explicit framing that "security testing requires adversarial conditions, not just functional conditions," and the insight that naming the pipeline step "security scan" instead of "dependency vulnerability scan" creates an illusion of coverage. The Lessons Learned section surfaces genuinely reusable principles (e.g., "detection time, not response time, was the real failure"; "IDE autocomplete errors will recur"). These are non-obvious framings that would change how the reader thinks about similar incidents.

### Output C: 5

Output C produces surprising depth. Several observations reframe the problem in ways the other outputs do not reach:

- "Confidence accumulates across checkpoints without coverage expanding" -- this is a general principle about safety systems that goes well beyond this incident.
- "The misconfiguration caused zero functional symptoms" -- Output C identifies that the entire safety architecture has an implicit axiom ("if nothing is broken, nothing is wrong") that is false for security failures. This is a genuine insight about the organisation's mental model, not just a finding about the incident.
- "Multiple independent checkpoints can produce less safety than a single well-scoped one when their coverage overlaps rather than complements" -- this is counterintuitive and well-argued. It identifies that accumulated confidence from overlapping checks is actively worse than knowing you have one limited check, because it suppresses vigilance.
- "A decision that controls whether customer data is public should not be made in the same cognitive mode as selecting a variable name from autocomplete" -- this connects the annotation error to a principle about cognitive friction in security decisions.
- The "Gaps in the timeline record" section calls out what is unknown, which is itself a form of analytical depth.
- The "Findings not yet addressed by action items" section explicitly names residual unknowns.

This output finds things that would change how you design safety systems, not just how you fix this incident.

---

## Dimension 2: Specificity (1-5)

### Output A: 3

Output A is grounded in the specifics of the incident. It references the endpoint, the annotation, the IP count, the Snyk scan, and the QA methodology. Action items are assigned to owners with due dates and priorities. However, many of the observations are stated at a level of generality that could apply to any authorization misconfiguration incident. The "What Went Poorly" section, for example, lists the gaps but does not explain precisely why each gap existed in this particular organisation's context.

### Output B: 4

Output B is more precisely grounded. Specific examples: the timeline adds a "What Was Known" column that captures the subjective state of the team at each moment (e.g., "Developer believed the annotation was correct," "QA confirmed the endpoint worked correctly. Testing was performed from an authenticated session, so the missing authentication requirement was invisible"). The root cause analysis explains exactly why Snyk's scope does not cover this ("Snyk scans for known vulnerabilities in dependencies. It does not examine application-level authorization configuration. This is not a failing of Snyk -- it's doing what it's designed to do"). The action items include rationale columns that tie each action to a specific branch of the root cause analysis. Each observation is traceable to evidence in the incident scenario.

### Output C: 4

Output C matches Output B's specificity and in some areas exceeds it. The root cause analysis references the specific testing count ("247 automated tests") and explains exactly how confidence was constructed from overlapping signals. The action items are organised into immediate/near-term/longer-term with explicit rationale. The "Findings not yet addressed by action items" section is notably specific -- it identifies three threads that need investigation before an action item can even be designed (code review process, access pattern characterisation, why the 247-test suite never included authorization testing). However, some of the Lessons Learned entries, while insightful, drift slightly from the specifics of this incident into general principles. This is valuable but slightly reduces traceability to the concrete evidence.

---

## Dimension 3: Completeness (1-5)

### Output A: 3

Output A covers the major points. It has the expected sections: Summary, Impact, Timeline, Root Cause, 5 Whys, What Went Well, What Went Poorly, Action Items, Lessons Learned. All the key facts from the incident scenario are represented. However, there are notable gaps: no explicit discussion of reputational risk, no callout of timeline uncertainties, no discussion of whether other endpoints might have the same issue, and no formal evaluation of what went well/poorly in the response (as distinct from what went wrong in the incident itself). The Lessons Learned section is a single paragraph rather than a structured analysis.

### Output B: 4

Output B is comprehensive without padding. It adds several elements not present in Output A: a "reputational risk" line in Impact, a "Response Evaluation" section that separates what worked in the response from what failed in prevention/detection, and Lessons Learned broken into four distinct, well-developed observations. The action items include a rationale column. Every section earns its place. The one gap: it does not call out open questions that remain unresolved (the code review process, the access pattern distribution, whether other endpoints have the same issue).

### Output C: 5

Output C is the most complete and is appropriately weighted -- it gives more depth where it matters most. It includes everything Output B includes, plus several elements neither other output covers:

- "Gaps in the timeline record" section that calls out what is not known
- "Contributing factors" separated from root causes, with proper distinction
- "Human factors" section that analyses the cognitive context of each actor's decisions
- "Findings not yet addressed by action items" -- an explicit acknowledgment of residual gaps
- "Unknown impact" in the Impact section, distinguishing what is known from what cannot be determined
- Action items categorised by time horizon (immediate/near-term/longer-term) with clear rationale
- The observation that the incident was closed before investigative threads were resolved, and the recommendation for a formal handoff process

The weighting is appropriate: the root cause analysis and lessons learned receive the most depth, which is correct for a postmortem whose value lies in organisational learning.

---

## Dimension 4: Audience Awareness (1-5)

### Output A: 3

Output A reads as an appropriate postmortem for a security engineering audience. The register is correct -- technical but not overly jargon-heavy. It follows a standard postmortem template. However, it does not particularly anticipate what the audience cares about beyond the facts. A senior engineering leader reading this would get the facts but would need to do their own synthesis to understand the systemic implications. The Lessons Learned section tells the audience what to think rather than showing them the reasoning.

### Output B: 4

Output B is tailored to its audience. The Summary explicitly frames why this incident matters ("not because of the severity of the data exposed... but because it reveals multiple gaps"). This tells a VP of Engineering or CISO exactly why they should care even though the data exposed was relatively low-sensitivity. The Lessons Learned entries anticipate the audience's likely objections (e.g., "IDE autocomplete errors will recur" preempts the response "we'll train developers to be more careful"). The "What Was Known" column in the timeline anticipates the question "why didn't anyone notice?" by showing the information landscape at each step. The action items include rationale, which shows the audience why each action matters, not just what to do.

### Output C: 5

Output C models the audience's perspective. It understands not just what a security/engineering leadership audience needs but how they will receive it. Several design choices demonstrate this:

- The Summary starts with what happened, immediately frames the systemic significance, then previews the action plan. A senior leader can read the Summary alone and understand the incident's importance.
- The "Unknown impact" subsection in Impact anticipates the question leadership will ask: "could this be worse than we think?" It gives an honest answer without either minimising or catastrophising.
- The Lessons Learned entries are written as organisational learning, not just incident findings. Each one articulates a principle that applies beyond this incident. This is what a CISO or VP of Engineering actually needs from a postmortem -- not "here's what happened" but "here's what we now understand about our system that we didn't before."
- The "Findings not yet addressed by action items" section anticipates the reader who will check whether every open thread has an owner. By explicitly calling out threads that need investigation before an action can be designed, it demonstrates that incompleteness is deliberate, not an oversight.
- The human factors section is blameless without being evasive. It explains why each actor made reasonable decisions given their context, which is exactly what a postmortem audience needs to hear to trust the document.

---

## Dimension 5: Vulnerability Detection (Domain-Specific) (1-5)

*Did it identify the real systemic issues, not just the immediate cause?*

### Output A: 3

Output A identifies the key systemic issues through the 5 Whys: no authorization testing, Snyk scope mismatch, permissive framework default. These are real issues. But the 5 Whys format constrains the analysis to a single causal chain, which misses the converging nature of the failure. The format imposes a linear narrative (each "why" leads to the next) when the actual causal structure is a set of independent gaps that all had to coexist. The result is that the framework default gets identified as "the" root cause at level 5, when in reality it is one of several independent systemic issues. The analysis is correct but incomplete in its causal model.

### Output B: 4

Output B identifies all the systemic issues Output A finds, plus additional ones: the code review gap (the annotation "appeared intentional in context"), the false sense of security from the Snyk label, and the detection-vs-response distinction. The branching analysis model is more faithful to the actual causal structure. The observation that "the gap between 'security scan passes' and 'the application is secure' is larger than assumed" is a genuine systemic finding about how the organisation understands its own security posture. The connection from the annotation mistake to deeper problems (secure-by-default architecture, testing gaps, detection gaps) is explicit and well-argued.

### Output C: 5

Output C finds systemic issues that the other outputs do not reach:

- The observation that the safety architecture assumes bad states produce symptoms -- and that this assumption is false for security failures -- is a category-level finding. It identifies a flaw in the organisation's mental model of safety, not just a missing test or a misconfigured tool.
- "Confidence accumulates across checkpoints without coverage expanding" identifies a systemic vulnerability in how the organisation evaluates its own safety. This is meta-level: it is a vulnerability in how they think about their vulnerabilities.
- The distinction between "delayed detection" and "outsourced detection" (relying on responsible disclosure) reframes the detection gap as structural rather than operational.
- The observation that the incident was closed with investigative threads unresolved identifies a gap in the organisation's learning process, not just its technical systems.
- The insight about cognitive friction -- that a security decision with major consequences should not be made in the same cognitive mode as selecting a variable name -- connects the technical failure to organisational design principles.

Output C treats the postmortem as genuine organisational learning. It does not just list what went wrong; it identifies the mental models and assumptions that made the failure inevitable.

---

## Summary

| Dimension | Output A | Output B | Output C |
|-----------|----------|----------|----------|
| Depth | 3 | 4 | 5 |
| Specificity | 3 | 4 | 4 |
| Completeness | 3 | 4 | 5 |
| Audience Awareness | 3 | 4 | 5 |
| Vulnerability Detection | 3 | 4 | 5 |
| **Total** | **15** | **20** | **24** |

**Overall preference**: C > B > A. Clear stratification across all dimensions.

**Key differences**:

Output A is a competent postmortem that follows a standard template and identifies the major issues. It is the kind of postmortem that satisfies a compliance requirement. It tells you what happened and what to fix.

Output B is a good postmortem that goes beyond the template. It understands that the causal structure is branching, not linear. It anticipates the audience's questions. It surfaces reusable principles. It tells you what happened, why the system allowed it, and what to think differently.

Output C is an exceptional postmortem that treats the incident as a window into the organisation's assumptions about safety, detection, and decision-making. It identifies systemic vulnerabilities that would not appear in a standard root cause analysis. It calls out its own gaps (unknown timeline details, findings not yet addressable). It frames lessons as organisational learning, not just incident findings. It tells you what happened, why the system made it inevitable, what mental models need to change, and what questions remain open.

**Magnitude**: Large.

The difference between A and B is moderate -- B is a meaningfully better document that would drive better outcomes. The difference between B and C is also moderate but qualitatively different -- C reaches a level of systemic analysis that changes how you think about the organisation's safety architecture, not just how you fix this particular incident. The cumulative difference between A and C is large and would be immediately apparent to a senior security or engineering leader.

---

## Diagnostic Observations

### Does any output go beyond the "5 Whys" template to find systemic issues?

Output A uses the 5 Whys format and stays within it. The format produces a reasonable linear chain but constrains the analysis to a single causal thread.

Output B explicitly abandons the 5 Whys format in favour of a branching analysis with five independently articulated "branches." This is a better fit for the actual causal structure and surfaces more systemic issues.

Output C goes furthest. Its root cause analysis identifies three primary root causes, then separately articulates contributing factors, systemic vulnerabilities, and human factors. It explicitly states that the causal structure is "converging, not linear" and analyses each branch independently. The Lessons Learned section then synthesises these into organisational principles that transcend the incident.

### Does any output treat the postmortem as organisational learning vs compliance document?

Output A reads as a compliance document. It has all the right sections, all the right facts, and reasonable action items. It would satisfy an audit. But it does not change how the reader thinks about the organisation's systems.

Output B is transitional. It has elements of organisational learning (the Lessons Learned entries are genuinely insightful) but the overall structure still feels like a well-executed postmortem template.

Output C is fully oriented toward organisational learning. The Lessons Learned section contains five extended observations, each of which articulates a principle about how the organisation's systems and assumptions create risk. The "Findings not yet addressed by action items" section is particularly telling -- a compliance document would not call attention to its own gaps.

### Does any output connect the annotation mistake to the deeper problem?

All three outputs make this connection to varying degrees. Output A reaches "permissive default" as the fifth why. Output B reaches it through a dedicated branch ("The annotation system itself is fragile") and elaborates on the architectural history. Output C goes further by connecting it to the absence of cognitive friction in security decisions, the assumption that bad states produce symptoms, and the broader pattern of confidence accumulating without coverage expanding.

### Does the root cause analysis feel mechanistic or genuinely investigative?

Output A's analysis feels mechanistic. The 5 Whys proceed in orderly steps, each building on the last. The fifth why arrives at a reasonable conclusion, but the format itself constrains the analysis. It reads like someone filling in a template, albeit doing so competently.

Output B's analysis feels investigative. The branching structure shows evidence of following the evidence rather than filling in a form. The observation about code review ("the annotation appeared intentional in context") and the Snyk naming issue ("if the pipeline step were called 'dependency vulnerability scan'...") feel like genuine discoveries.

Output C's analysis feels deeply investigative. It identifies causal patterns (overlapping coverage, false confidence), cognitive factors (autocomplete as a decision context), and organisational patterns (closing incidents before resolving questions). The "Contributing factors" and "Human factors" sections show a sophistication in causal reasoning that goes beyond what any standard template would produce. The analysis of why QA's process was structurally incapable of detecting the issue (not a judgment failure but a process design failure) is particularly strong.

### Other observations

- Output C is substantially longer than the others. In this case, the length is warranted -- virtually every paragraph adds analytical value. There is very little padding. However, for some organisational contexts, the length itself could be a barrier to the document being read.
- Output A assigns due dates and priorities to action items, which is a practical detail the other outputs omit. Output C categorises actions by time horizon (immediate/near-term/longer-term) which serves a similar practical purpose.
- Output C is the only output that calls out the gap between "incident resolved" and "questions answered" as an organisational process issue. This is a meta-level finding about how the organisation does postmortems, surfaced within a postmortem.
- All three outputs are blameless in tone, consistent with the task requirement.
