---
model: GPT-5.2
date: 2026-03-15
experiment: A3
tier: pipeline
run: 1
stage: stage-2-context-intake
---

## REVIEW_CONTEXT (YAML)
mode: manager
review_period: "July 2025 – December 2025 (H2)"
audience: "manager chain"
tone: "supportive, direct"

employee:
  name: "Jordan Chen"
  role: "Senior Software Engineer"
  level: "IC4 (Senior)"
  tenure: "2.5 years (promoted from IC3 to IC4 eight months ago)"
  manager: "You"

team:  # calibration only
  name: "Platform Infrastructure"
  members: []

rubric:
  provided: false
  summary: "No explicit competency rubric provided; role expectations implied (IC4 vs IC5 gap noted around ambiguity ownership and stakeholder communication)."
  rating_scale: "unknown"

goals_prior_cycle:
  provided: true
  items:
    - goal: "Lead a cross-team technical project end-to-end"
      success_criteria: "unknown"
    - goal: "Improve documentation practices on the team"
      success_criteria: "unknown"
    - goal: "Present at an engineering forum"
      success_criteria: "unknown"

constraints:
  confidentiality_notes: "Use standard performance-review confidentiality; avoid sensitive personal details not in provided notes."
  avoid_topics: "unknown"

data_sources:
  user_provided: ["notes", "metrics"]
  connectors_claimed_available: ["none"]

## RAW_NOTES
- Employee details: Jordan Chen, Senior Software Engineer, IC4 (Senior), Platform Infrastructure; manager is the reviewer; tenure 2.5 years; promoted from IC3 to IC4 eight months ago.
- Review period: July 2025 – December 2025 (H2).
- What went well:
  - Led migration of internal event bus from RabbitMQ to Kafka.
    - Originally scoped Q3–Q4; delivered mid-November (3 weeks early).
    - Zero production incidents during cutover.
    - Three other teams adopted the new event bus without needing Jordan’s help; documentation was sufficient.
  - Mentored two junior engineers (Priya and Marcus) through first on-call rotations.
    - Both reported feeling prepared.
    - Marcus credited Jordan’s runbook rewrites for making first page manageable.
  - Volunteered to lead Kubernetes cost optimisation initiative after noticing spend was 40% over budget.
    - Reduced monthly compute costs by $18K/month via right-sizing and spot instance adoption.
    - Self-initiated (“nobody asked Jordan to do this”).
  - Presented Kafka migration approach at company engineering all-hands.
    - First time presenting to ~200+ people.
    - Feedback positive, but Jordan was visibly nervous and rushed through Q&A.
- What needs work:
  - Struggles with ambiguity.
    - Executes excellently on well-defined technical problems.
    - When problem is fuzzy (e.g., “figure out our observability strategy”, “rethink deployments”), tends to stall and wait for someone else to define the approach; then executes well once path is clear.
    - Stated as main gap between IC4 and IC5.
  - Communication to non-technical stakeholders underdeveloped.
    - Kafka migration updates to VP of Engineering were overly technical (e.g., WAL segments, consumer group rebalancing).
    - Coaching required twice to reframe to schedule/risk-oriented updates.
  - Capacity signaling:
    - Took on cost optimisation alongside Kafka migration.
    - Two weeks in October: clearly overloaded; did not flag until surfaced in 1:1.
- Goals from last review (H1) and status:
  - Lead a cross-team technical project end-to-end — Met (Kafka migration).
  - Improve documentation practices on the team — Exceeded (runbook rewrites; Kafka docs adopted by 3 teams).
  - Present at an engineering forum — Met (all-hands presentation; room to grow on delivery).
- Promotion consideration:
  - Not ready for IC5 this cycle.
  - Rationale: ambiguity gap needs demonstrated progress.
  - Target: next review cycle (H1 2026) if initiative demonstrated on a problem where approach isn’t predefined.
- Compensation:
  - Merit increase recommended: standard 4%.
  - No equity refresh this cycle; save for promotion cycle.

## OPEN_QUESTIONS (only if needed)
- Please provide the exact `/performance-review manager Jordan Chen` template text/required sections (and any mandatory fields) that the final writeup must follow.
- Is there a formal rubric/competency framework for IC4/IC5 in this org (and any rating scale), or should the review be narrative-only?
- Any additional evidence to include (peer/customer feedback quotes, ticket links, incident notes, adoption metrics beyond what’s above), especially for ambiguity ownership and stakeholder communication?
- Any constraints on tone/length (e.g., word limit, required level of directness) and the intended audience (employee-only vs manager chain vs calibration)?
