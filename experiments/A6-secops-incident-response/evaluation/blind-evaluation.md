# Blind Evaluation: A6 SecOps Incident Response (Postmortem)

**Evaluator**: Claude (blind evaluation -- version identities unknown)
**Date**: 2026-03-14
**Task**: Write a blameless postmortem for a resolved SEV1 incident -- customer data exposed via misconfigured API endpoint, 11-day exposure, 2,847 records.

---

## Initial Impressions

All three outputs produce a recognisable blameless postmortem. The differences emerge in how deeply each one interrogates the incident, how much analytical work the document does beyond restating what happened, and how well each one serves the actual audience of a postmortem (the engineering and security leadership who need to understand systemic risk, not just the sequence of events).

**Output A** reads as a competent, template-following postmortem. It covers all expected sections, includes a 5 Whys analysis, provides an action items table with owners and due dates. It is well-structured and would be acceptable as a draft.

**Output B** reads as an analytically richer document. It replaces the 5 Whys with a branching root cause analysis, adds a "What Was Known" column to the timeline, and produces lessons learned that go beyond the immediate incident to identify systemic patterns. The writing shows more independent reasoning about why the failure occurred.

**Output C** reads as the most thorough and analytically mature of the three. It identifies systemic vulnerabilities explicitly, distinguishes between root causes and contributing factors, introduces a human factors analysis, calls out gaps in the timeline record itself, includes a section on "findings not yet addressed by action items," and produces lessons learned that function as genuine organisational insights rather than summaries of what went wrong. The document feels like it was written by someone who has investigated incidents before, not someone following a template.

---

## Dimension Scores

### 1. Depth (1-5)

**Output A: 3**
Covers expected ground competently. The 5 Whys analysis follows the causal chain from annotation error to framework default, which is the right direction. But the analysis stays within the information provided -- it does not generate new analytical observations. The "Lessons Learned" section is a single paragraph that summarises the action items rather than extracting higher-order insights. The document tells you what happened; it does not reframe how you think about the system.

**Output B: 4**
Goes beyond the expected. The branching root cause analysis is a genuine analytical contribution -- it identifies five independent branches that had to co-exist for the incident to persist, which is a more accurate model than a linear 5 Whys chain. The observation about the Snyk "security scan" label creating false coverage is incisive: "Naming matters: if the pipeline step were called 'dependency vulnerability scan' instead of 'security scan,' the gap in authorization checking might have been more visible." The lessons learned section generates insights that reframe thinking (e.g., "testing from an authenticated session cannot verify authentication requirements" and "detection time, not response time, was the real failure").

**Output C: 5**
Produces genuinely surprising insights. Several observations reframe how you think about the incident and the organisation's security posture:
- "Confidence accumulates across checkpoints without coverage expanding" -- this is a general principle about safety architecture, not just a restatement of what went wrong.
- "Multiple independent checkpoints can produce less safety than a single well-scoped one when their coverage overlaps rather than complements" -- this inverts conventional wisdom about defense in depth.
- "The 11-day exposure window was not a detection failure -- it was a structural inevitability" -- this reframes the problem from "we were slow to detect" to "detection was impossible given the system's design."
- The observation about cognitive friction at the point of security decision is a genuinely novel contribution: "A decision that controls whether customer data is public should not be made in the same cognitive mode as selecting a variable name from autocomplete."
- The identification of "findings not yet addressed by action items" shows meta-level awareness -- the document acknowledges what it does not yet know.

### 2. Specificity (1-5)

**Output A: 3**
Grounded in the actual incident. References specific elements (the annotation, Snyk, the 23 requests, the 4 IPs). Action items are tied to specific tools and processes. But the analysis does not go beyond what was provided in the incident scenario -- the document is specific to this incident without generating new specific observations about why these particular failures occurred.

**Output B: 4**
Precise references throughout. Each branch of the root cause analysis is tied to a specific mechanism in the system. The timeline adds a "What Was Known" column that grounds each event in the informational context of the people involved -- this is a specificity contribution that goes beyond restating the timeline. The observation about authenticated-session QA testing is tied to the specific mechanism: "the endpoint behaves identically whether annotated `@Public` or `@AdminOnly`" from the tester's perspective. The lessons learned are specific enough to be actionable beyond this incident.

**Output C: 5**
Every observation is traceable to evidence. The document distinguishes between what the logs show and what remains unknown. It explicitly calls out gaps in the available evidence: "The distribution of the 23 requests across the 11-day window is not documented, so the pattern of access -- whether it was targeted or opportunistic -- is not characterised." The action items include rationale tied to specific root causes. The "contributing factors" section explains exactly why QA could not have caught this (not "QA missed it" but "the process was structurally incapable of detecting this class of error"). The human factors section is specific about the information environment the developer was operating in. The "findings not yet addressed" section is specific about what is unknown and why action items cannot yet be designed for those unknowns.

### 3. Completeness (1-5)

**Output A: 3**
Covers major points adequately. All expected sections are present. The 5 Whys reaches the framework default. Action items cover the discussed improvements. But some areas are thin: the "What Went Well" and "What Went Poorly" sections are near-verbatim reproductions of the input material rather than analytical expansions. The document does not address gaps in knowledge (e.g., what we still do not know about the unattributed IPs). Does not consider whether other endpoints might have similar issues. Does not address the code review process or its absence from the causal chain.

**Output B: 4**
Comprehensive without padding. Everything present earns its place. The branching root cause analysis is more complete than a linear chain because it identifies parallel failure modes rather than forcing them into a sequence. The response evaluation separates "what worked" from "what did not work" with analytical depth in both directions. The lessons learned cover four distinct dimensions. The document addresses the unattributed IP investigation as an action item. The one gap: it does not explicitly call out what is unknown or what the document itself cannot resolve.

**Output C: 5**
Comprehensive and appropriately weighted. More depth where it matters most (root cause analysis and lessons learned get the most space). Notably, it includes sections no other output has:
- "Gaps in the timeline record" -- explicitly noting what is undocumented
- "Contributing factors" vs. "root causes" -- a distinction that matters for action prioritisation
- "Human factors" -- examining the information environment shaping decisions
- "Systemic vulnerabilities" -- generalising from this incident to the class of failures it represents
- "Findings not yet addressed by action items" -- intellectual honesty about the limits of the document's own recommendations
- The action items are structured into immediate/near-term/longer-term tiers with explicit rationale for each
- The document even asks the meta-question: "why did a 247-test suite never include this trivially testable property?" -- probing whether the gap was a conscious trade-off or a conceptual blind spot

### 4. Audience Awareness (1-5)

**Output A: 3**
Appropriate register for a postmortem. Would be understood by the intended audience (engineering and security leadership). The tone is professional and blameless. However, it reads more like a template filled in than a document crafted for how the audience will use it. The action items table has due dates, which is practical. The document does not anticipate questions the audience would have (e.g., "could this be happening on other endpoints right now?").

**Output B: 4**
Tailored to the audience. The "What Was Known" column in the timeline anticipates the reader's question: "why didn't anyone notice?" By showing what each actor knew at each moment, it prevents the blame instinct that postmortems are supposed to avoid. The branching root cause analysis models how the audience thinks about systemic risk -- not as a single chain but as multiple gaps that coincided. The lessons learned are written for an audience that needs to make decisions about investment in security infrastructure, not just understand what happened.

**Output C: 5**
Models the audience's perspective. Several features demonstrate this:
- The summary is front-loaded with the systemic finding ("the root causes are architectural, not individual") -- this is what leadership needs to hear first, before the details.
- The "gaps in the timeline record" section anticipates the audience asking "is this the full picture?" and honestly answers "no, and here's what's missing."
- The "findings not yet addressed by action items" section anticipates the audience asking "does this cover everything?" and honestly answers "no, and here's what still needs investigation before we can act."
- The human factors section pre-empts the "why did the developer do this?" question by explaining the information environment -- this is blameless postmortem done correctly, not just by omitting names but by making the systemic explanation more compelling than any individual-blame explanation.
- The action items are structured by time horizon, matching how leadership prioritises work (what do we do this week vs. this quarter).
- The lessons learned are written at the level of organisational principles, not incident-specific observations -- they are useful beyond this incident, which is what leadership actually wants from a postmortem.

### 5. Vulnerability Detection (1-5) -- Domain-Specific

*Did the output identify the genuinely systemic issues, not just the surface failure?*

**Output A: 3**
Identifies the main systemic issues: annotation fragility, no authorization testing, security scan scope mismatch, no runtime detection, framework default permissiveness. The 5 Whys reaches the framework default, which is the right root. But the analysis stays at the level of "here's what we're missing" without examining why these gaps formed or what class of failures they represent. Does not generalise beyond this incident.

**Output B: 4**
Identifies all the systemic issues Output A finds, plus several additional ones: the false confidence created by the "security scan" label, the structural impossibility of detecting this from an authenticated session, the distinction between detection time and response time as the real metric. The branching analysis is a better model of the actual vulnerability landscape. The lessons learned generalise usefully ("IDE autocomplete errors will recur" reframes the proximate cause as a category, not a one-off). However, it does not fully explore the question of whether other endpoints are currently vulnerable or whether the monitoring gap was a known risk.

**Output C: 5**
Identifies the deepest systemic vulnerabilities:
- The single-point-of-failure nature of annotation-based access control, explicitly noting it applies to every endpoint in the system, not just this one.
- The "confidence accumulates without coverage expanding" pattern -- this is a vulnerability in the safety architecture itself, not just a gap in testing.
- The distinction between availability-oriented and confidentiality-oriented detection -- the monitoring architecture can detect outages but not leaks. This is a class of vulnerability, not a specific gap.
- The observation that "bad states with no symptoms" are invisible to a safety architecture that assumes bad states produce symptoms. This reframes the vulnerability as a category error in the organisation's safety model.
- The "category error in how the organisation thinks about its security scan" -- identifying that the label creates false coverage is a vulnerability in organisational cognition, not just in tooling.
- The "gap between incident resolved and questions answered" -- identifying that the incident process itself has a vulnerability (no handoff to post-incident investigation).

Output C finds vulnerabilities at three levels: technical (the annotation system), procedural (the testing and detection gaps), and organisational (how the team thinks about security coverage, how confidence accumulates, how incidents are closed). The other outputs primarily operate at the technical and procedural levels.

---

## Summary

| Dimension | Output A | Output B | Output C |
|-----------|----------|----------|----------|
| Depth | 3 | 4 | 5 |
| Specificity | 3 | 4 | 5 |
| Completeness | 3 | 4 | 5 |
| Audience Awareness | 3 | 4 | 5 |
| Vulnerability Detection | 3 | 4 | 5 |
| **Total** | **15** | **20** | **25** |

**Overall preference**: C > B > A

**Key differences**:

Output A is a competent postmortem that covers expected ground. It follows a template well and would be serviceable as a draft. Its analysis stays within the information provided and does not generate new insights.

Output B adds genuine analytical value. The branching root cause analysis, the "What Was Known" timeline column, and the lessons learned all represent independent reasoning about the incident. It finds things a knowledgeable reader would recognise as important but might not have articulated.

Output C operates at a qualitatively different level. It does not just analyse this incident -- it uses this incident to identify organisational vulnerabilities that extend far beyond the specific failure. The observations about confidence accumulation, symptomatic vs. asymptomatic failures, cognitive friction at decision points, and the gap between incident closure and question resolution are contributions that change how the reader thinks about their security posture. The document also has intellectual honesty that the others lack: it explicitly names what it does not know, what evidence is missing from the record, and what action items it cannot yet design.

**Magnitude**: Large

The difference between A and B is moderate -- B is a better version of the same kind of document. The difference between B and C is large and qualitative -- C is a different kind of document. A is a template-following postmortem. B is a thoughtful postmortem. C is a postmortem that functions as an organisational learning document. The gap is most visible in the lessons learned sections: A summarises the action items, B extracts useful principles, C generates insights that would change how the organisation designs its safety architecture.

---

## Diagnostic Observations

**Templated vs. analytical thinking.** Output A follows the postmortem template faithfully -- every section is present, the 5 Whys proceeds linearly, the action items have due dates. But the document feels like it was generated by applying a template to the incident data rather than by thinking about the incident. Outputs B and C show visible evidence of analytical reasoning: they question assumptions, identify structural patterns, and generate observations not present in the input material.

**The 5 Whys limitation.** Output A uses a traditional 5 Whys format. Output B replaces it with a branching analysis. Output C uses a multi-root-cause structure with contributing factors. The branching/multi-root approach is more accurate for this incident, which genuinely has multiple independent causal branches. The 5 Whys format forces a linear chain that makes the analysis feel artificially sequential -- as if one cause "led to" the next, when in reality several independent gaps coexisted.

**Treatment of uncertainty.** Output A does not address what is unknown. Output B mentions the unattributed IPs as an action item but does not discuss uncertainty broadly. Output C explicitly names multiple categories of uncertainty: the unattributed IPs, the undocumented code review process, the uncharacterised access pattern, and the unknown organisational history of why the testing gap exists. This is a significant quality difference -- a postmortem that acknowledges its own limits is more trustworthy and more useful than one that presents itself as complete.

**Blamelessness quality.** All three outputs are nominally blameless (no names, no blame language). But the quality of blamelessness differs. Output A achieves blamelessness by omission -- it does not mention individuals. Output B achieves it by explaining the information environment: "the reviewer had no way to know the developer intended `@AdminOnly` unless they independently reasoned about what authorization the endpoint should have." Output C achieves the deepest form by making systemic explanations so compelling that individual blame becomes structurally incoherent: "In this information environment, the error is predictable -- a reasonable developer working at normal speed would make this error at some non-trivial rate." This is the gold standard for blameless postmortems -- not just avoiding blame but making the systemic explanation obviously correct.

**One surprise.** Output C identifies something genuinely unexpected: "Multiple independent checkpoints can produce less safety than a single well-scoped one when their coverage overlaps rather than complements." This inverts the standard defense-in-depth argument. It is specific enough to be testable and general enough to apply beyond this incident. Neither A nor B produces an observation at this level.

**Actionability.** Output A's action items are the most prescriptive (specific due dates, clear owners). Output C's are the most thoughtfully structured (tiered by time horizon, with explicit rationale, plus acknowledgment of items that cannot yet be designed). Output B falls between. For a real incident, Output C's approach is more useful because it distinguishes between "do this now" and "scope this first, then act" -- which matches how engineering organisations actually prioritise.
