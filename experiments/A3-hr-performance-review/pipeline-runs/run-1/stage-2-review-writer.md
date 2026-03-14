## Performance Review: Jordan Chen
**Period:** July 2025 -- December 2025 (H2) | **Role:** Senior Software Engineer, IC4 | **Team:** Platform Infrastructure

### Performance Summary

Jordan is eight months into the IC4 level and performing at the top of that band on the work that plays to current strengths. The Kafka migration -- a high-risk, cross-team infrastructure project -- was delivered three weeks early with zero production incidents. A self-initiated Kubernetes cost optimisation saved $18K/month. Two junior engineers were mentored through their first on-call rotations with artifacts (runbooks, documentation) that persist beyond the mentoring itself. A first all-hands presentation was delivered to 200+ people. The volume and quality of output in this period is unusually high for someone less than a year at a new level.

The picture is not uniformly strong. A clear boundary separates Jordan's performance on structured problems from performance on ambiguous ones. When a problem has defined edges -- migrate this system, reduce this spend, rewrite these runbooks -- execution is fast, reliable, and frequently exceeds expectations. When a problem is open-ended and requires framing before it can be solved, Jordan stalls and waits for someone else to define the approach. This is not a deficiency at IC4. It is the specific capability gap between IC4 and IC5, and it is visible now because Jordan's structured-problem performance is strong enough to make the contrast sharp.

A second pattern worth naming: Jordan's initiative and multiplier instincts coexist with underdeveloped capacity management. The same drive that produces outsized impact also produces unmanaged overload. Jordan does not yet proactively surface strain -- it emerged reactively during a 1:1, not before. For someone operating at this velocity, building the habit of trade-off communication is a near-term priority.

### Key Strengths

- **Disciplined execution on high-stakes infrastructure work**: The Kafka migration was scoped for Q3-Q4, delivered three weeks early, and cut over with zero production incidents. This is not just speed -- it demonstrates the judgment to execute a high-risk change reliably. The combination of pace and stability is what makes this noteworthy.

- **Self-directed initiative on concrete problems**: The Kubernetes cost optimisation was entirely self-initiated. Jordan noticed a 40% budget overrun, volunteered to lead the response, and delivered measurable savings. Nobody assigned this work. When a problem is legible and quantifiable, Jordan's instinct is to claim it and solve it.

- **Knowledge transfer as a working habit**: Across the Kafka migration documentation (adopted by three teams without Jordan's help), the rewritten runbooks (credited by a junior engineer as directly useful during a live page), and the mentoring of Priya and Marcus, a consistent pattern emerges: Jordan invests in making knowledge accessible independent of Jordan's own availability. This is a multiplier instinct that shows up as a natural orientation rather than a checked box.

- **Mentorship that produces downstream outcomes**: Both mentees reported feeling prepared for on-call. Marcus specifically credited Jordan's runbook rewrites for making his first page manageable. The evidence here is outcome-based -- the mentoring produced engineers who could operate independently -- not just activity-based.

### Areas for Development

- **Navigating ambiguity and framing unstructured problems**: When problems lack defined boundaries -- "figure out our observability strategy," "rethink how we do deployments" -- Jordan's pattern is to wait for someone else to frame the approach, then execute well once the path is clear. This is the defining capability gap between IC4 and IC5. Jordan's initiative fires reliably when the problem is already legible (visible overspend, a system to migrate). The next growth edge is developing the ability to take an ambiguous space and impose structure on it -- to be the person who frames the problem, not just the person who solves it. This does not require a personality change; it requires practice in structured problem-framing on progressively less defined challenges.

- **Audience-calibrated communication**: Jordan's technical communication to engineers is consistently strong -- documentation, runbooks, and team-level presentations all land well. Communication to non-technical stakeholders is a different picture. VP updates on the Kafka migration defaulted to implementation details (WAL segments, consumer group rebalancing) when the audience needed status, risk, and decision-relevant context. This required coaching twice on the same pattern. The gap is not in communication skill but in audience modeling: Jordan defaults to the register of the work rather than translating for the listener's decision-making needs. The instinct to shift register does not yet fire automatically.

- **Proactive capacity management**: During October, Jordan was clearly overloaded from overlapping the cost optimisation with the Kafka migration but did not surface this until a 1:1 check-in. The pattern -- takes on too much, does not flag -- is described as an occasional tendency, not a one-off. Jordan's drive to claim and solve problems needs to be paired with the discipline to trade off or sequence against existing commitments, and to communicate strain proactively rather than absorbing it silently.

### Goal Achievement

| Goal | Assessment | Evidence |
|------|-----------|----------|
| Lead a cross-team technical project end-to-end | **Exceeded** | The Kafka migration was cross-team (three teams adopted the output), led by Jordan from scoping through delivery, completed 3 weeks ahead of schedule with zero production incidents. Execution exceeded the bar implied by the goal. |
| Improve documentation practices on the team | **Exceeded** | Runbook rewrites were credited by a junior engineer as directly useful during on-call. Kafka migration documentation was sufficient for three teams to adopt the event bus independently -- no direct support from Jordan required. Impact extended beyond personal documentation into a measurable change in team-level documentation quality. |
| Present at an engineering forum | **Met** | Jordan presented the Kafka migration approach at the company all-hands to 200+ people. This was a first presentation at that scale. Feedback was positive. Delivery showed visible nervousness and a rushed Q&A, indicating this is an emerging capability rather than a mature one. The goal was met on action; the growth opportunity in delivery quality is real. |

### Impact and Contributions

Jordan's most significant contribution in H2 was the Kafka migration: a high-risk infrastructure change that replaced RabbitMQ across the platform, delivered early and cleanly. The downstream effect -- three teams adopting the new event bus using Jordan's documentation alone -- extends the impact beyond the migration itself into the team's ability to operate independently on the new system.

The Kubernetes cost optimisation, while smaller in scope, is significant for what it signals: Jordan is scanning for problems at the team and organisational level, not just executing assigned work. The $18K/month savings was a tangible organisational contribution that nobody asked for.

The mentoring work with Priya and Marcus improved the team's on-call resilience. The runbook rewrites are persistent artifacts -- they will continue to reduce on-call friction long after the mentoring relationship has concluded.

Taken together, the picture is of someone operating across individual delivery, team capability, and cost efficiency -- a breadth of impact that is characteristic of strong IC4 performance and beginning to touch the edges of IC5 scope.

### Development Plan

| Focus Area | Current State | Target State | Actions |
|------------|--------------|-------------|---------|
| Problem framing in ambiguous spaces | Executes well once a problem is defined; stalls when the problem requires framing before it can be solved. Initiative fires on legible, quantifiable problems but not on open-ended ones. | Can take an ambiguous challenge (e.g., "improve our observability story") and independently produce a problem frame: what the problem is, what the options are, what they trade off, and a recommended path. Does not need to get it right on the first try -- needs to be willing to propose a frame and iterate. | 1. Manager assigns one explicitly ambiguous problem next half with the instruction "frame this before solving it." Start with a bounded ambiguity (e.g., propose an approach for deployment pipeline improvements) rather than a fully open space. 2. Jordan writes a one-page problem frame before beginning execution -- what is the problem, what are the options, what do they trade off. Review this together before Jordan begins work. 3. Repeat with a second, less bounded problem in Q2. |
| Stakeholder communication | Technical communication to engineers is strong. Defaults to implementation-level detail when communicating to non-technical stakeholders. Required coaching twice on the same pattern during VP updates. | Independently adjusts communication register based on audience. VP updates lead with status, risk, and decisions needed -- technical detail is available on request but not the default frame. | 1. Before each VP or cross-functional update, Jordan drafts the communication and asks: "What does this person need to decide, and what do they need to know to decide it?" 2. Manager reviews the first two stakeholder updates of Q1 with Jordan to calibrate. 3. Jordan identifies one non-engineering stakeholder to build a recurring communication relationship with next half (e.g., product counterpart, finance partner on infra costs). |
| Capacity management and trade-off signaling | Takes on new work without sequencing against existing commitments. Does not proactively surface overload -- strain appeared only in a reactive 1:1. | When taking on new work, explicitly names what it displaces or delays. Surfaces capacity constraints proactively before they become visible in delivery or wellbeing. | 1. Adopt a practice of stating capacity trade-offs when volunteering for new work: "I can take this on if we push X to next sprint" or "This will create a two-week overlap where I'm at capacity -- flagging that now." 2. Manager checks in on capacity explicitly during 1:1s for the first two months until the proactive signaling habit is established. |

### Overall Rating: Exceeds Expectations

Jordan is performing at the top of the IC4 band eight months after promotion. The volume, quality, and scope of output in H2 -- a major cross-team migration delivered early with zero incidents, a self-initiated cost savings of $18K/month, meaningful mentorship of two junior engineers, and a first company-wide presentation -- is unusually strong for someone less than a year at a new level. All three goals from the prior cycle were met, two of them exceeded.

The development areas are real and clearly identified -- ambiguity tolerance, stakeholder communication, capacity management -- but they are growth edges appropriate to someone building toward IC5, not deficiencies in IC4 performance. The evidence across this half supports a rating of Exceeds Expectations with clarity about where the next level of growth lies.

### Compensation Recommendation

**Equity refresh** -- Jordan's output this half significantly exceeds the expectations for a recently promoted IC4. An equity refresh recognises the current trajectory and provides retention value for someone who is likely to receive external interest at this performance level. A promotion to IC5 is not yet warranted -- the ambiguity-navigation and stakeholder-communication capabilities that define that level are not yet demonstrated -- but the gap is identifiable and closable within the next two to three review cycles if the development plan is followed. Revisit promotion readiness at the H1 2026 review.
