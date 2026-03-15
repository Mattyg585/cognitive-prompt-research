---
model: GPT-5.2
date: 2026-03-15
experiment: A3
tier: optimised
run: 1
---

## Performance Review: Jordan Chen
**Period:** July 2025 – December 2025 (H2) | **Manager:** You | **Role/Level:** Senior Software Engineer, IC4

### Snapshot (evidence-first)
- Primary scope this period: Platform Infrastructure; internal event bus reliability and adoption; on-call readiness.
- Most important outcomes:
  - Led the internal event bus migration from RabbitMQ to Kafka; delivered mid-November (3 weeks early); zero production incidents during cutover.
  - Reduced Kubernetes compute spend by ~$18K/month via right-sizing and spot instance adoption (self-initiated).
  - Improved on-call readiness through mentoring and runbook rewrites; documentation enabled self-serve adoption by three teams.
- Key strengths observed:
  - High-reliability execution on complex, cross-team infrastructure work
  - Force-multiplier behaviors (documentation, mentoring, operational rigor)
  - Proactive ownership when signals are clear (cost overrun)
- Biggest growth opportunities:
  - Framing and driving ambiguous problem spaces (IC4 → IC5 gap)
  - Audience-calibrated communication for non-technical stakeholders
  - Earlier capacity signaling and explicit tradeoff management

### Evidence log (recommended)
| Theme / competency | Observation (behavior) | Example / artifact | Impact | Notes |
|-------------------|-------------------------|--------------------|--------|------|
| Execution / Delivery | Plans and executes end-to-end; delivers ahead of schedule with operational rigor | RabbitMQ → Kafka migration delivered 3 weeks early; zero incidents during cutover | Reduced migration risk; enabled platform modernization | Strong coordination across teams; clean cutover |
| Documentation | Produces documentation that enables self-service adoption | Kafka/event bus documentation good enough that 3 teams adopted without needing Jordan | Reduced support burden; increased platform leverage | Clear indicator of durable, scalable work |
| Team development | Invests in readiness of others; improves operational safety | Mentored Priya + Marcus through first on-call rotations; runbook rewrites | Increased confidence and on-call effectiveness; reduced incident response stress | Marcus explicitly credited runbook rewrites |
| Ownership / Initiative | Identifies non-assigned operational issue and drives it | Volunteered to lead K8s cost optimisation after noticing 40% budget overrun | ~$18K/month recurring savings | Strong initiative; self-directed |
| Communication / Influence | Steps into broader visibility but delivery needs refinement | Presented Kafka migration at engineering all-hands (200+); feedback positive but nervous/rushed Q&A | Increased visibility of work; early influence building | Growth opportunity: pacing + Q&A structure |
| Ambiguity handling | Hesitates when the problem is “fuzzy”; waits for framing before engaging | “Observability strategy” / “rethink deployments” examples | Slower progress in strategic/undefined areas | Core IC4→IC5 gap per manager observations |
| Stakeholder communication | Over-indexes on implementation detail for exec audience | VP updates included WAL segments / consumer group rebalancing; required coaching twice | Misalignment risk; harder decision-making for stakeholders | Needs altitude control: status/risks/asks |
| Capacity management | Takes on too much without early escalation | October overlap (Kafka + cost initiative); overload surfaced in 1:1 rather than earlier | Sustainability risk; planning blind spots | Practice making constraints visible sooner |

### Performance Summary
Jordan delivered a high-impact half through excellent execution, operational rigor, and meaningful team leverage. The Kafka migration is standout evidence: it landed early, cut over without incidents, and shipped with documentation strong enough for other teams to adopt without ongoing support. In parallel, Jordan self-initiated a cost optimisation effort that materially reduced monthly spend, and strengthened team resilience by mentoring junior engineers and improving runbooks.

The primary developmental edge is not technical competence; it is operating effectively when the problem requires framing before execution. Building the “define the path” muscle—alongside improving communication altitude for non-technical stakeholders and surfacing capacity constraints earlier—will be the highest-leverage set of improvements for Jordan’s trajectory toward IC5.

### Key Strengths (0–N)
- **High-reliability delivery on complex infrastructure work** — Led the RabbitMQ → Kafka migration end-to-end, delivered 3 weeks early with zero production incidents during cutover.
- **Force-multiplier documentation practices** — Produced Kafka/event bus documentation that enabled three teams to adopt without needing Jordan’s direct support.
- **Proactive ownership with business impact** — Volunteered to lead Kubernetes cost optimisation after identifying a 40% budget overrun, resulting in ~$18K/month savings.
- **Team enablement through mentoring and operational readiness** — Mentored two junior engineers through first on-call rotations; runbook rewrites directly improved first-page experience.
- **Willingness to step into visibility** — Presented migration approach at company all-hands; content landed well even as delivery skills remain a growth area.

### Areas for Development (0–N)
- **Navigating ambiguity / problem framing** — *Behavior to change:* When the ask is fuzzy, Jordan tends to wait for others to define the approach. *Why it matters:* At IC5, impact depends on framing, proposing options, and driving alignment—before execution begins. *Next step:* Own one ambiguous initiative in H1 2026 (e.g., observability strategy) and start with a written framing memo (problem, options, tradeoffs, recommendation) before group discussion.
- **Non-technical stakeholder communication (altitude control)** — *Behavior to change:* Executive updates default to deep technical detail rather than outcomes/risks/asks. *Why it matters:* Decision-makers need clear status, risks, and decisions needed to unblock work. *Next step:* Use a standard format (Headline / Status / Risks & mitigations / Asks) for VP-facing updates; review first drafts with manager until consistent.
- **Capacity signaling and tradeoff management** — *Behavior to change:* Absorbs overload and surfaces it late. *Why it matters:* Hidden constraints become delivery and reliability risk; the team can’t route around what it can’t see. *Next step:* Proactively flag “yellow/red” capacity and propose what to defer/de-scope when taking on additional work.
- **Presentation delivery and Q&A pacing** — *Behavior to change:* Rushed Q&A under pressure. *Why it matters:* As influence grows, communicating clearly in high-visibility settings becomes part of the job. *Next step:* Rehearse with a peer, prepare likely questions, and use a repeat-question → 2–3 bullet answer structure.

### Goal Achievement (0–N)
| Goal / expectation | Result | Evidence | Comments |
|-------------------|--------|----------|----------|
| Lead a cross-team technical project end-to-end | Met | Kafka migration delivered mid-November (3 weeks early); zero incidents | Clear evidence of strong end-to-end delivery at IC4 |
| Improve documentation practices on the team | Exceeded | Kafka docs adopted by 3 teams without Jordan’s help; runbook rewrites | Durable documentation that reduced future support load |
| Present at an engineering forum | Met | Presented at engineering all-hands (200+); feedback positive | Good first step; delivery growth opportunity (nerves, Q&A) |

### Impact and Contributions
- Team/org impact: Safer, more scalable eventing platform via Kafka migration; reduced ongoing dependency on Jordan through strong documentation.
- Operational efficiency: ~$18K/month recurring compute savings from cost optimisation work.
- Collaboration: Cross-team migration delivery plus company-wide knowledge sharing via all-hands presentation.
- Ownership & judgment: Took on unassigned cost optimisation work; demonstrated strong execution judgment when scope was clear; needs growth in shaping ambiguous scopes.

### Development Plan (optional)
| Skill / behavior | Current observation | Target behavior | Actions | Timeline / check-ins |
|-----------------|---------------------|-----------------|---------|----------------------|
| Ambiguity framing | Waits for approach definition in fuzzy spaces | Defines framing, options, and recommendation; drives alignment | Own an ambiguous platform initiative; write a 1-page framing memo before implementation; manager coaches but does not provide the frame | H1 2026; review memo + decision outcome in monthly check-ins |
| Executive communication | Technical-detail-first updates | Outcome/risk/ask-first updates tailored to audience | Use “Status / Risks / Decisions needed” format for VP updates; review first 2–3 drafts | Next 6–8 weeks; iterate based on stakeholder feedback |
| Capacity signaling | Surfaces overload late | Flags constraints early; proposes tradeoffs | Add explicit green/yellow/red capacity check in weekly 1:1; when yellow/red, propose what to defer | Start immediately; revisit each 1:1 |
| Presentation delivery | Nervous pacing; rushed Q&A | Clear pacing; structured Q&A | Rehearse with peer; prepare top questions; practice structured Q&A responses | Next 1–2 presentations in H1 2026 |

### Rating & Compensation (optional — only if you have rubric + evidence)
> Org rating rubric/definitions were not provided in the input, so an “overall rating” cannot be assessed against a stated standard.

- Overall rating: Needs rubric/expectations to assess.
- Promotion: Not recommended for IC5 this cycle (key gap: ambiguity/framing). Target next cycle (H1 2026) contingent on demonstrated progress owning an ambiguous initiative and improving stakeholder communication.
- Merit increase: Recommend standard 4% (per provided guidance).
- Equity refresh: No equity refresh this cycle; revisit during promotion cycle.
