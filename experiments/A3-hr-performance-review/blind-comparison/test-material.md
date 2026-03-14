# Test Material: Performance Review Scenario

## Mode: Manager Review

Write a manager performance review for the following direct report.

## Employee Details

- **Name**: Jordan Chen
- **Role**: Senior Software Engineer
- **Level**: IC4 (Senior)
- **Team**: Platform Infrastructure
- **Manager**: You
- **Tenure**: 2.5 years (promoted from IC3 to IC4 eight months ago)
- **Review Period**: July 2025 – December 2025 (H2)

## Context You Have

### What went well
- Led the migration of the internal event bus from RabbitMQ to Kafka. Project was scoped for Q3-Q4, delivered mid-November (3 weeks early). Zero production incidents during cutover. Three other teams have since adopted the new event bus without needing Jordan's help — the documentation was good enough.
- Mentored two junior engineers (Priya and Marcus) through their first on-call rotations. Both reported feeling prepared. Marcus specifically credited Jordan's runbook rewrites for making his first page manageable.
- Volunteered to lead the team's Kubernetes cost optimisation initiative after noticing spend was 40% over budget. Reduced monthly compute costs by $18K/month through right-sizing and spot instance adoption. Nobody asked Jordan to do this.
- Presented the Kafka migration approach at the company engineering all-hands. First time presenting to 200+ people. Feedback was positive but Jordan was visibly nervous and rushed through the Q&A.

### What needs work
- Jordan struggles with ambiguity. When given a well-defined technical problem, execution is excellent. When the problem is fuzzy — "figure out our observability strategy" or "we need to rethink how we do deployments" — Jordan stalls. Tends to wait for someone else to define the approach, then executes well once the path is clear. This is the main gap between IC4 and IC5.
- Communication to non-technical stakeholders is underdeveloped. The Kafka migration updates to the VP of Engineering were overly technical. Jordan described WAL segments and consumer group rebalancing when the VP wanted to know "is it on track and what are the risks." Had to coach Jordan on this twice.
- Occasionally takes on too much and doesn't flag when capacity is stretched. The cost optimisation work happened alongside the Kafka migration, and there were two weeks in October where Jordan was clearly overloaded but didn't say anything until a 1:1 check-in surfaced it.

### Goals from last review (H1)
1. Lead a cross-team technical project end-to-end — **Met** (Kafka migration)
2. Improve documentation practices on the team — **Exceeded** (runbook rewrites, Kafka docs adopted by 3 teams)
3. Present at an engineering forum — **Met** (all-hands presentation, with room to grow on delivery)

### Promotion consideration
Not ready for IC5 this cycle. The ambiguity gap is real and needs demonstrated progress. Target: next review cycle (H1 2026) if Jordan can show initiative on a problem where the approach isn't predefined.

### Compensation
Merit increase recommended (standard 4%). No equity refresh this cycle — save that for the promotion cycle.

## The Task

Write the full manager performance review using the `/performance-review manager Jordan Chen` template from the prompt.
