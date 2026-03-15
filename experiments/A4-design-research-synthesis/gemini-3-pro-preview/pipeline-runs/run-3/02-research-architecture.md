---
model: gemini-3-pro-preview
date: 2026-03-15
experiment: A4
tier: pipeline
run: 3
stage: 02-research-architect
---

# Research Architecture: Themes & User Models

Based on the analysis of 6 user interviews (P1-P6), the following themes, user segments, and insights have been identified.

### 1. Key Themes

#### Theme 1: High Friction & Cognitive Load ("Work about Work")
*   **Description**: The act of managing tasks requires excessive clicks, navigation, and cognitive effort, leading users to perceive the tool as an impediment rather than an aid. The interface is cluttered with irrelevant historical data and complex features.
*   **Prevalence**: High (P1, P2, P5, P6)
*   **Evidence**:
    *   "It's not that TaskFlow is bad — it's that updating a task takes four clicks. Open the task, click edit, change the status, save." — P1
    *   "The default view shows everything — completed tasks from three months ago... It's like a cluttered desk." — P2
    *   "TaskFlow showed me 47 tasks across 6 projects with 4 different priority levels and I couldn't tell which ones actually mattered." — P5
*   **Underlying Need**: Simplicity, speed, and immediate clarity (signal over noise).

#### Theme 2: Context Switching & Workflow Isolation ("Not Where We Work")
*   **Description**: The tool exists as a destination island, separated from where the actual work happens (Slack, GitHub, Figma). This separation creates a "context switching tax" that users are unwilling to pay, leading them to update status in their native tools instead.
*   **Prevalence**: High (P1, P3, P4)
*   **Evidence**:
    *   "In Slack I just say 'done with the auth thing' and everyone knows. I know that's terrible for tracking but it's honest about how engineers work." — P1
    *   "Engineers live in GitHub. Marketers live in their Google Docs and Figma. Ops lives in Slack. TaskFlow is an extra tab they have to remember to update." — P3
    *   "It was ugly and limited but everyone updated [the spreadsheet] because it was one tab in a sheet they already had open." — P4
*   **Underlying Need**: Seamless workflow integration; tools that meet users in their existing environments.

#### Theme 3: The Compliance-Value Vicious Cycle
*   **Description**: Because friction is high and integration is poor, compliance drops. Low compliance means data is stale, rendering reports and views useless. This lack of value drives further disengagement, forcing managers into an "enforcement" role.
*   **Prevalence**: High (P1, P2, P3, P4)
*   **Evidence**:
    *   "But it pulls from task status, and if people aren't updating tasks, the report is fiction." — P1
    *   "I've noticed I'm the only one who keeps my tasks updated, which means the 'team view' is really just Marcus's view." — P2
    *   "That's my actual job now — not project management, task management enforcement." — P4
*   **Underlying Need**: Trustworthy data that provides shared value, not just administrative overhead.

#### Theme 4: Feature Overkill & Mismatch of Scale
*   **Description**: The tool provides enterprise-grade complexity (Gantt charts, resource allocation, complex automation) for teams that need simple lists. This "bloat" intimidates users and complicates simple actions.
*   **Prevalence**: Medium (P1, P5, P6)
*   **Evidence**:
    *   "I'd say we use maybe 30% of the features. The other 70% — time tracking, resource allocation, the Gantt chart — that's for a different kind of company." — P1
    *   "TaskFlow gives us a Ferrari when we need a bicycle." — P6
    *   "I think the drop-off problem is that TaskFlow optimises for the 'set up and manage' person but not for the 'just do the work' person." — P6
*   **Underlying Need**: Right-sized tooling; minimalism and focus.

### 2. User Segments

#### Segment A: The "Just Do Work" Contributor
*   **Description**: Individual contributors (Engineers, Designers, Marketers) focused on execution. They view administrative tasks as a distraction from their "real" work.
*   **Key Behaviors**: Updates status in Slack, ignores formal tool, reverts to text files/personal lists, uses mobile for read-only access.
*   **Primary Needs**: Speed (1-click updates), workflow integration (don't make me leave my tab), clarity (what do I do *now*?).
*   **Pain Points**: Excessive clicks, irrelevant notifications, clutter/noise, context switching.
*   **Representative Quote**: "I tried TaskFlow for three months and went back to a text file." — P5

#### Segment B: The "Herder" Manager
*   **Description**: Team Leads and Project Managers responsible for visibility and reporting. They are the primary purchasers/advocates but suffer when the team doesn't engage.
*   **Key Behaviors**: Nags for updates, manually updates tasks for others during meetings, tries to configure views/automations to fix data quality.
*   **Primary Needs**: Accurate visibility ("who is working on what?"), blocked status, single source of truth to report upwards/outwards.
*   **Pain Points**: Stale data (making them look bad), being the "bad guy" (enforcer), blind spots in team activity.
*   **Representative Quote**: "The thing I actually want is dead simple: who is working on what right now, and is anything blocked." — P2

### 3. Insight Summary

*   **Friction is the root cause of data rot**: The core failure mode is high interaction cost (clicks/switching) -> low compliance -> stale data -> zero value. You cannot solve the "stale data" problem without solving the "too many clicks" problem.
*   **The "Destination" model is obsolete**: Users reject the idea of a central destination for work management. They demand a "meta-layer" that aggregates signal from where work actually happens (GitHub, Slack, etc.) without forcing context switches.
*   **Admin-User Value Asymmetry**: The tool is designed to sell to the "Herder" (features, reports) but fails the "Contributor" (usability, speed). Since the Herder relies on the Contributor for data, this asymmetry destroys the value for *both* parties.
