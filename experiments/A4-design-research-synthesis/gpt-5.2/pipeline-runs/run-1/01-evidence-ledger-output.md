---
model: GPT-5.2
date: 2026-03-15
experiment: A4
tier: pipeline
run: 1
stage: 01-evidence-ledger
---

# A4 — Stage 01: Evidence Ledger

## 1) Research Metadata (only what’s supported)
- **Product**: TaskFlow (project management SaaS for mid-market teams, 50–200 employees)
- **Method**: 45-minute semi-structured interviews
- **Participants**: 6 users (mix of power users and occasional users)
- **Research question**: Why do teams adopt TaskFlow enthusiastically but usage drops off after 3–4 months?
- **Data sources**:
  - **S1**: `test-material/user-interviews.md` (sections labeled P1–P6)

## 2) Evidence Ledger

| Evidence ID | Source | Type | Verbatim / Observation | Context | Open-codes (tags) |
|---|---|---|---|---|---|
| E1 | S1 — Study Details | observation | "Product: TaskFlow (project management SaaS for mid-market teams, 50-200 employees)" | Study framing line | product-scope, target-segment |
| E2 | S1 — Study Details | observation | "Method: 45-minute semi-structured interviews" | Study framing line | method, interview |
| E3 | S1 — Study Details | observation | "Participants: 6 users (mix of power users and occasional users)" | Study framing line | participant-count, usage-mix |
| E4 | S1 — Study Details | observation | "Research question: Why do teams adopt TaskFlow enthusiastically but usage drops off after 3-4 months?" | Study framing line | adoption-dropoff, retention |
| E5 | S1 — P1 (Sarah, Engineering Manager, 85-person company) | quote | "We rolled it out in January and everyone was excited." | Adoption / rollout recollection | initial-excitement, rollout |
| E6 | S1 — P1 (Sarah) | quote | "The board view is genuinely better than Jira for our workflow." | Comparative evaluation (workflow fit) | comparative-benchmark, board-view, workflow-fit |
| E7 | S1 — P1 (Sarah) | quote | "But by April, half the team was back to Slack threads for task coordination." | Reported reversion to alternative coordination channel | slack-workarounds, dropoff-timing |
| E8 | S1 — P1 (Sarah) | quote | "It's not that TaskFlow is bad — it's that updating a task takes four clicks." | Perceived root cause (interaction cost) | update-friction, interaction-cost |
| E9 | S1 — P1 (Sarah) | quote | "Open the task, click edit, change the status, save." | Steps describing update flow | workflow-steps, update-flow |
| E10 | S1 — P1 (Sarah) | quote | "In Slack I just say 'done with the auth thing' and everyone knows." | Alternative behavior in Slack | low-friction-updates, informal-status |
| E11 | S1 — P1 (Sarah) | quote | "The weekly report feature is something I love in theory." | Attitude to reporting feature | reporting-value, intent-vs-reality |
| E12 | S1 — P1 (Sarah) | quote | "But it pulls from task status, and if people aren't updating tasks, the report is fiction." | Dependency of reporting on data entry | data-quality-dependency, reporting-trust |
| E13 | S1 — P1 (Sarah) | quote | "So I stopped looking at it." | Behavioral change after trust loss | disengagement, stop-using-feature |
| E14 | S1 — P1 (Sarah) | quote | "Which means I stopped having a reason to open TaskFlow daily." | Reported feedback loop reducing daily use | habit-formation, daily-usage, value-loop |
| E15 | S1 — P1 (Sarah) | quote | "I'd say we use maybe 30% of the features." | Self-estimated feature usage | feature-utilization, perceived-bloat |
| E16 | S1 — P1 (Sarah) | quote | "The other 70% — time tracking, resource allocation, the Gantt chart — that's for a different kind of company." | Features perceived as mismatched to org type | feature-misalignment, overkill, persona-fit |
| E17 | S1 — P1 (Sarah) | quote | "We're too small and too fast for that." | Org context for mismatch | org-stage, speed, size-constraints |
| E18 | S1 — P2 (Marcus, Product Designer, 120-person company) | quote | "I use TaskFlow religiously." | Individual usage intensity | power-user, high-engagement |
| E19 | S1 — P2 (Marcus) | quote | "I'm probably the most active user on my team." | Self-positioning relative to team | uneven-adoption, adoption-disparity |
| E20 | S1 — P2 (Marcus) | quote | "But I've noticed I'm the only one who keeps my tasks updated" | Observation of low participation in upkeep | update-noncompliance, single-maintainer |
| E21 | S1 — P2 (Marcus) | quote | "which means the 'team view' is really just Marcus's view." | Consequence on shared visibility | visibility-breakdown, single-source-distortion |
| E22 | S1 — P2 (Marcus) | quote | "The PMs stopped checking it because it wasn't reflecting reality." | Stakeholders disengage due to mismatch | trust-loss, stakeholder-dropoff |
| E23 | S1 — P2 (Marcus) | quote | "The thing I actually want is dead simple: who is working on what right now, and is anything blocked." | Desired information outcome | now-view, ownership, blockers |
| E24 | S1 — P2 (Marcus) | quote | "TaskFlow can technically show me this but I have to set up a custom filter, save it as a view, and then remember to check that view instead of the default one." | Customization / cognitive overhead to get desired view | customization-overhead, saved-views, default-bias |
| E25 | S1 — P2 (Marcus) | quote | "The default view shows everything" | Perception of default information overload | default-view, information-overload |
| E26 | S1 — P2 (Marcus) | quote | "completed tasks from three months ago" | Example of irrelevant clutter | clutter-old-items, recency |
| E27 | S1 — P2 (Marcus) | quote | "backlog items nobody's prioritised" | Example of clutter / low-signal content | backlog-no-priority, signal-to-noise |
| E28 | S1 — P2 (Marcus) | quote | "stuff from archived sprints." | Example of clutter from inactive work | archived-content, lifecycle |
| E29 | S1 — P2 (Marcus) | quote | "It's like a cluttered desk." | Analogy expressing experience | clutter-metaphor, usability-perception |
| E30 | S1 — P2 (Marcus) | quote | "I tried setting up automations to keep things clean but the automation builder is... I gave up after twenty minutes." | Attempted mitigation; tool difficulty; time-to-abandon | automation-builder, setup-friction, abandonment-time |
| E31 | S1 — P2 (Marcus) | quote | "I'm a designer, not a systems architect." | Skill/identity mismatch with configuration demands | role-fit, configuration-complexity |
| E32 | S1 — P3 (Alex, VP of Operations, 200-person company) | quote | "We bought TaskFlow specifically for cross-team visibility." | Purchase intent | cross-team-visibility, buying-motive |
| E33 | S1 — P3 (Alex) | quote | "Marketing, engineering, ops — we wanted one place to see everything." | Scope of visibility goal | multi-team, single-view |
| E34 | S1 — P3 (Alex) | quote | "It works for that if, and only if, everyone puts their work in it." | Conditional dependency on participation | adoption-dependency, completeness |
| E35 | S1 — P3 (Alex) | quote | "We're at maybe 60% compliance and it's been stuck there for months." | Self-estimated participation level and plateau | compliance-rate, plateau |
| E36 | S1 — P3 (Alex) | quote | "The problem isn't the tool." | Attribution away from product defects (as framed by speaker) | attribution, framing |
| E37 | S1 — P3 (Alex) | quote | "It's that TaskFlow doesn't meet people where they are." | Core claim about fit with existing workflows | workflow-misalignment, context-switching |
| E38 | S1 — P3 (Alex) | quote | "Engineers live in GitHub." | Where work happens (engineering) | work-surface, github |
| E39 | S1 — P3 (Alex) | quote | "Marketers live in their Google Docs and Figma." | Where work happens (marketing) | work-surface, docs, figma |
| E40 | S1 — P3 (Alex) | quote | "Ops lives in Slack." | Where work happens (ops) | work-surface, slack |
| E41 | S1 — P3 (Alex) | quote | "TaskFlow is an extra tab they have to remember to update." | Description of overhead / remembrance burden | extra-tab, memory-burden, update-overhead |
| E42 | S1 — P3 (Alex) | quote | "We tried the integrations but the GitHub integration just creates a firehose of commits as tasks, which is worse than nothing." | Integration outcome described as noisy/negative | integration-noise, github-integration, firehose |
| E43 | S1 — P3 (Alex) | quote | "What I actually need is a layer that sits on top of where people already work and gives me the cross-team view without requiring everyone to change their habits." | Desired architecture / approach | overlay-layer, habit-preservation, passive-visibility |
| E44 | S1 — P3 (Alex) | quote | "TaskFlow wants to be the center." | Perceived product positioning | tool-as-hub, centralization |
| E45 | S1 — P3 (Alex) | quote | "It should be the lens." | Desired positioning metaphor | lens-metaphor, augmentation |
| E46 | S1 — P4 (Deepa, Project Manager, 90-person company) | quote | "I'm the TaskFlow champion on my team" | Role as internal advocate | champion, admin-role |
| E47 | S1 — P4 (Deepa) | quote | "which means I spend about 30 minutes a day nagging people to update their tasks." | Time cost + behavior described | enforcement-overhead, nagging, time-cost |
| E48 | S1 — P4 (Deepa) | quote | "That's my actual job now — not project management, task management enforcement." | Identity/job shift attributed to tool adoption | role-distortion, enforcement-work |
| E49 | S1 — P4 (Deepa) | quote | "The tool created a new overhead that didn't exist before." | Net-new overhead claim | overhead-created, adoption-cost |
| E50 | S1 — P4 (Deepa) | quote | "The irony is that before TaskFlow, we used a shared spreadsheet." | Prior tool/process | prior-workflow, spreadsheet |
| E51 | S1 — P4 (Deepa) | quote | "It was ugly and limited but everyone updated it because it was one tab in a sheet they already had open." | Prior workflow success condition | in-context-update, low-friction, ubiquity |
| E52 | S1 — P4 (Deepa) | quote | "TaskFlow is objectively better in every way except the one that matters: people actually using it." | Product capability vs adoption outcome | capability-vs-adoption, utilization-gap |
| E53 | S1 — P4 (Deepa) | quote | "I've started doing a thing where I update tasks on behalf of my team during standup." | Workaround behavior | proxy-updating, standup-process |
| E54 | S1 — P4 (Deepa) | quote | "I just listen to what they say and update TaskFlow in real time." | Description of workaround execution | live-updating, meeting-integration |
| E55 | S1 — P4 (Deepa) | quote | "It works but it defeats the purpose of a self-service tool." | Evaluation of workaround implications | self-service-failure, workaround-cost |
| E56 | S1 — P4 (Deepa) | quote | "I'm the human integration layer." | Metaphor for workaround role | human-integration, integration-gap |
| E57 | S1 — P4 (Deepa) | quote | "The notifications are a disaster." | Assessment of notification system | notifications, negative-valence |
| E58 | S1 — P4 (Deepa) | quote | "Everyone turned them off in the first week because they were getting pinged for every comment, every status change, every new task." | Reason for disabling notifications; triggers listed | notification-fatigue, noisy-alerts, opt-out |
| E59 | S1 — P4 (Deepa) | quote | "Now nobody gets notified about anything, including things they should actually know about." | Downstream effect of opt-out | missed-critical-notifs, communication-breakdown |
| E60 | S1 — P5 (Raj, Senior Engineer, 150-person company) | quote | "I tried TaskFlow for three months and went back to a text file." | Duration + abandonment; alternative tool | trial-duration, abandonment, personal-workflow |
| E61 | S1 — P5 (Raj) | quote | "My todo.txt is twelve lines and I know exactly what I'm doing today." | Preference for simplicity/clarity | simplicity, daily-focus, personal-todo |
| E62 | S1 — P5 (Raj) | quote | "TaskFlow showed me 47 tasks across 6 projects with 4 different priority levels" | Complexity described with counts | task-volume, multi-project, priority-complexity |
| E63 | S1 — P5 (Raj) | quote | "and I couldn't tell which ones actually mattered." | Consequence of complexity | prioritization-failure, low-clarity |
| E64 | S1 — P5 (Raj) | quote | "The mobile app is surprisingly good though." | Positive assessment of mobile | mobile-positive, platform |
| E65 | S1 — P5 (Raj) | quote | "I use it on my commute to check what's coming up." | Mobile usage context | commute-usage, preview |
| E66 | S1 — P5 (Raj) | quote | "If I could just mark things done from mobile with one tap, I'd probably use it more." | Conditional adoption lever | mobile-quick-complete, one-tap, retention-lever |
| E67 | S1 — P5 (Raj) | quote | "But marking a task done on mobile is the same four-click process as desktop." | Mobile interaction cost parity | mobile-friction, interaction-cost |
| E68 | S1 — P5 (Raj) | quote | "It's like they ported the UI without thinking about the use case." | Attribution about design approach | ported-ui, use-case-mismatch |
| E69 | S1 — P5 (Raj) | quote | "My manager uses TaskFlow to assign me work, which means I have to open it to see what's new." | TaskFlow used as assignment channel | assignment-inbox, forced-entry |
| E70 | S1 — P5 (Raj) | quote | "So I open it, check assignments, then close it and put the important ones in my text file." | Reported workflow integrating TaskFlow + external list | dual-system, extraction |
| E71 | S1 — P5 (Raj) | quote | "I'm using TaskFlow as an inbox, not a workspace." | Framing of role TaskFlow plays | inbox-not-workspace, limited-usage |
| E72 | S1 — P6 (Nina, Marketing Lead, 70-person company) | quote | "I love the timeline view for campaign planning." | Positive assessment of timeline for use case | timeline-view, campaign-planning |
| E73 | S1 — P6 (Nina) | quote | "It's genuinely the best I've seen — better than Asana, better than Monday." | Comparative benchmark | comparative-benchmark, timeline-best-in-class |
| E74 | S1 — P6 (Nina) | quote | "But my team of four people doesn't need project management software." | Size/context mismatch | small-team, tool-overkill |
| E75 | S1 — P6 (Nina) | quote | "We need a shared to-do list with due dates." | Stated need | simple-todo, due-dates |
| E76 | S1 — P6 (Nina) | quote | "TaskFlow gives us a Ferrari when we need a bicycle." | Metaphor for overpowered solution | overkill-metaphor, complexity |
| E77 | S1 — P6 (Nina) | quote | "The onboarding was overwhelming." | Onboarding experience | onboarding-overwhelm |
| E78 | S1 — P6 (Nina) | quote | "Five template options, custom field configuration, workflow setup, integration wizard" | Onboarding components listed | onboarding-steps, configuration |
| E79 | S1 — P6 (Nina) | quote | "we spent a full day setting it up and I'm still not sure we did it right." | Time cost + uncertainty | setup-time, uncertainty, confidence |
| E80 | S1 — P6 (Nina) | quote | "My previous tool (Todoist) took ten minutes." | Comparative onboarding time | onboarding-comparison, time-to-value |
| E81 | S1 — P6 (Nina) | quote | "I think the drop-off problem is that TaskFlow optimises for the 'set up and manage' person but not for the 'just do the work' person." | Hypothesis about persona optimization | admin-vs-doer, persona-mismatch |
| E82 | S1 — P6 (Nina) | quote | "I love setting it up." | Admin/setup affinity | setup-enjoyment, admin-persona |
| E83 | S1 — P6 (Nina) | quote | "My team hates living in it." | Reported team sentiment | resentment, day-to-day-usage |
| E84 | S1 — P6 (Nina) | quote | "The gap between the admin experience and the user experience is where adoption dies." | Claimed mechanism of drop-off | admin-user-gap, adoption-failure |

## 3) Unknowns & Data Gaps
- Interview date range is not provided (only a relative “rolled it out in January / by April” in P1).
- Recruiting/sampling criteria are not provided (how participants were selected; whether they represent typical customers).
- “Mix of power users and occasional users” is not operationalized (no definitions).
- No demographic details beyond role and company size.
- No quantitative product telemetry (DAU/WAU, retention cohorts, feature usage, notification opt-out rates).
- No baseline workflow artifacts (e.g., examples of Slack threads, spreadsheets, todo.txt) or how tasks were defined.
- “Compliance” (P3) is not defined (what behaviors count; how measured).
- Integration configuration details are missing (what GitHub integration mode/settings produced the “firehose”).
- No breakdown by team/function for drop-off timing or reasons.

## 4) Early anomalies (optional, non-thematic)
- Strong individual value alongside team-level non-adoption: P2 reports high personal use (E18–E19) while also reporting that others don’t update tasks (E20–E22).
- Best-in-class feature perceptions coexisting with overall “overkill” framing: P6 praises timeline view (E72–E73) while saying the tool is too heavy for a 4-person team (E74–E76).
- Mobile perceived as good (E64–E65) yet still blocked by the same completion friction as desktop (E66–E67).
