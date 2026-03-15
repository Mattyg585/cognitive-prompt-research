---
model: GPT-5.2
date: 2026-03-15
experiment: A3
tier: pipeline
run: 1
stage: stage-4-template-drafter
---

# Manager performance review draft — Jordan Chen

## Context
- Period: July 2025 – December 2025 (H2)
- Review mode: Manager
- Audience: Manager chain
- Tone: Supportive, direct
- Employee: Jordan Chen — Senior Software Engineer (IC4)
- Team: Platform Infrastructure
- Tenure / level context: Tenured engineer; promoted from IC3 → IC4 earlier in the year (timing per notes)
- Rubric: No explicit competency rubric or rating scale provided in inputs
- Data sources used: Manager-provided notes and metrics as written (no connector pulls)

## Evidence snapshot (high-confidence; from provided notes)
- Delivered a cross-team migration of the internal event bus from RabbitMQ to Kafka, ahead of the original plan (per notes).
- Executed the production cutover without reported production incidents during the cutover window (per notes).
- Produced adoption documentation that enabled other teams to self-serve adoption without ongoing dependency on Jordan (per notes).
- Identified a concrete cost problem signal in Kubernetes spend and voluntarily led an optimisation effort (per notes).
- Achieved ongoing monthly compute cost reduction via right-sizing and spot instance adoption (exact figure per notes; include if needed) .

## Summary (draft narrative; no rating)
Jordan delivered strong outcomes on well-scoped, cross-team technical work during the period, with an emphasis on operational safety and documentation that scales beyond a single engineer. In parallel, Jordan demonstrated ownership by proactively identifying and driving a cost optimisation initiative that produced recurring savings.

The primary development opportunities for the next period are to increase ownership when the problem framing is ambiguous, to consistently tailor communication for non-technical and executive stakeholders, and to signal capacity constraints earlier when load is trending unsustainably.

## Impact & accomplishments (prefilled where supported)

### Kafka event bus migration (RabbitMQ → Kafka)
- What happened (draft): Led a cross-team migration of the internal event bus from RabbitMQ to Kafka.
- Outcomes observed (draft): Delivered ahead of the original plan; cutover completed with no reported production incidents.
- Enablement (draft): Produced documentation sufficient for other teams to adopt without needing Jordan’s direct support.
- Evidence anchors: E1, E2, E3
- Artifacts to link (optional, if available): [migration plan], [cutover runbook], [adoption guide], [retro/postmortem], [availability/incident report]

### Kubernetes cost optimisation initiative
- What happened (draft): Noticed Kubernetes spend was above expectations and volunteered to lead a cost optimisation initiative.
- Approach (draft): Right-sizing and spot instance adoption (implementation details not provided).
- Outcome (draft): Ongoing monthly compute cost reduction (insert exact value and before/after timeframe if needed).
- Evidence anchors: E6, E7
- Artifacts to link (optional, if available): [spend dashboard before/after], [FinOps report], [PRs/tickets for policy changes]

### Additional accomplishments (add as needed)
- [Accomplishment title]
  - What happened: …
  - Outcome: …
  - Evidence anchors (if any): …
  - Artifacts/links (optional): …

## Goal progress (from prior cycle; draft status to confirm)

| Prior-cycle goal | Draft status (confirm in Stage 5) | Evidence-based notes | Evidence IDs | Missing details / links (optional) |
|---|---|---|---|---|
| Lead a cross-team technical project end-to-end | [Met / Exceeded / Partial / Not met] | Kafka migration delivered ahead of plan with safe cutover; cross-team adoption enabled via docs. | E1, E2, E3 | [migration artifacts/links] |
| Improve documentation practices on the team | [Met / Exceeded / Partial / Not met] | Adoption documentation enabled other teams to self-serve; runbook improvements are reported but would benefit from links/diffs. | E3; (runbooks: E5) | [doc links], [runbook diffs] |
| Present at an engineering forum | [Met / Exceeded / Partial / Not met] | Presented Kafka migration approach at engineering all-hands; feedback reported positive; opportunity to improve Q&A pacing/confidence. | (presentation: E8, E9) | [recording], [feedback notes] |
| Add another goal row as needed |  |  |  |  |

## Strengths (evidence-based)

### Execution on defined technical scope with operational safety
Jordan executed effectively on a well-defined, cross-team infrastructure migration and delivered the change with attention to reliability during production cutover.
- Evidence: E1, E2

### Documentation that reduces single-threaded dependency
Jordan produced platform documentation that enabled other teams to adopt the new event bus without requiring ongoing, direct support.
- Evidence: E3

### Ownership and initiative when a concrete signal is present
Jordan identified a cost problem signal and initiated an optimisation effort that produced recurring savings.
- Evidence: E6, E7

## Growth areas (development-focused; keep behavior-based)

### Owning ambiguity and problem framing earlier
- Observation (draft): When the problem is fuzzy (examples referenced: observability strategy, deployments), Jordan can stall while waiting for others to define an approach, then executes strongly once direction is provided.
- Impact (draft): Delays momentum on ambiguous initiatives and reduces visible ownership at the next level.
- Evidence status: Needs concrete examples with timelines and artifacts to cite precisely.
- Evidence: E10 (medium)
- Insert example(s) (as available): [what was asked], [what Jordan proposed], [where it stalled], [what unblocked it]

### Tailoring stakeholder communication to audience
- Observation (draft): Some upward updates during the Kafka migration were overly technical and benefited from coaching toward schedule/risk/decision framing.
- Impact (draft): Increases risk of misalignment with non-technical stakeholders and adds rework to communication cycles.
- Evidence status: Would benefit from before/after examples of written updates.
- Evidence: E11, E12 (medium)
- Insert example(s) (as available): [VP update before], [VP update after], [key reframes]

### Capacity and load signalling
- Observation (draft): When taking on overlapping initiatives, Jordan did not surface overload early, and it was identified later in a 1:1.
- Impact (draft): Can create delivery and sustainability risk when load is not proactively managed.
- Evidence status: Would benefit from dates/context and what tradeoffs were available.
- Evidence: E13 (medium)

### Presence and Q&A pacing in high-visibility forums
- Observation (draft): First large-audience presentation was a positive step; there is an opportunity to build confidence and pacing during Q&A.
- Evidence status: Would benefit from feedback notes or recording review.
- Evidence: E8, E9 (medium)

## Development plan (draft; repeatable)

| Development theme | Current behavior (draft) | Evidence | Growth actions (repeatable) | Manager / org support | Success signals (non-numeric) | Target timeframe |
|---|---|---|---|---|---|---|
| Ambiguity ownership | Tends to wait for framing on fuzzy problems; executes well once direction is set. | E10 | - Propose an initial framing doc early (problem statement, constraints, options, recommended path)
- Identify stakeholders and decision points; drive alignment
- Run a lightweight discovery loop (as needed) and converge on a plan | - Provide a sponsor for an ambiguous initiative
- Regular check-ins focused on framing, not execution
- Feedback on early drafts | - Independently proposes viable approaches without waiting for full direction
- Stakeholders report clarity on goals/tradeoffs | [next period / next cycle] |
| Stakeholder communication | Technical detail can dominate upward updates without clear risk/schedule framing. | E11, E12 | - Use an audience-first update format (context → decision/risk → timeline → asks)
- Prepare a “technical appendix” separately for deep dives
- Practice translating technical changes into impact language | - Review a small number of updates early in the cycle
- Provide examples of strong exec updates | - Updates land with non-technical stakeholders; fewer rewrites needed
- Clear articulation of risks and mitigation | [as needed] |
| Capacity signalling | Overload surfaced late while running overlapping initiatives. | E13 | - Maintain a visible commitments list and proactively flag red/yellow status
- Propose tradeoffs when new work appears
- Request sequencing decisions earlier | - Reinforce that early flagging is expected
- Help negotiate scope/priority across stakeholders | - Load discussions happen before crunch points
- Work is sequenced without last-minute escalation | [as needed] |
| Presentation/Q&A presence | Opportunity to improve pacing and confidence in Q&A settings. | E8, E9 | - Rehearse Q&A scenarios; prepare a small set of bridging phrases
- Run a debrief after presentations to capture improvements
- Seek smaller forums to iterate (optional) | - Provide coaching or speaking resources (optional)
- Help select venues aligned to growth goals | - Q&A handled with calm pacing; questions reframed clearly
- Audience feedback reflects clarity and confidence | [next opportunities] |
| Add another row as needed |  |  |  |  |  |  |

## Optional / To be decided (Stage 5)
- Overall rating: [to be completed in Stage 5]
- Competency/expectations assessment (if rubric is provided later): [to be completed in Stage 5]
- Compensation action: [to be completed in Stage 5]
- Promotion / level readiness: [to be completed in Stage 5]
- Calibration notes / distribution constraints: [to be completed in Stage 5]
