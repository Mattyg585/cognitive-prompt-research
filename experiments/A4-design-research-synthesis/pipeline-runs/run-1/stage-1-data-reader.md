# Stage 1: Data Reader Observations

**Study**: TaskFlow usage drop-off after 3-4 months
**Data**: 6 semi-structured interviews, 45 minutes each
**Participants**: Mix of power users and occasional users across companies of 70-200 employees

---

## Participant Observations

### P1 — Sarah, Engineering Manager, 85-person company

**Context**: Engineering manager at a small company. Led the TaskFlow rollout in January. By April, observed half the team reverting to Slack for task coordination. Speaks from both a management and team perspective.

**Key quotes**:
- "It's not that TaskFlow is bad — it's that updating a task takes four clicks. Open the task, click edit, change the status, save." -- Describing why engineers reverted to Slack. The specificity of "four clicks" suggests she has counted, has felt the friction repeatedly.
- "In Slack I just say 'done with the auth thing' and everyone knows. I know that's terrible for tracking but it's honest about how engineers work." -- Acknowledging the trade-off explicitly. The phrase "honest about how engineers work" signals she sees the tool as imposing dishonest workflow expectations.
- "The weekly report feature is something I love in theory." -- The qualifier "in theory" is doing significant work. She draws a direct causal chain: people don't update tasks, so reports are fiction, so she stopped looking, so she lost her reason to open the tool daily. A cascade failure.
- "The other 70% — time tracking, resource allocation, the Gantt chart — that's for a different kind of company. We're too small and too fast for that." -- Placing her company outside the tool's assumed user profile.

**Behavioural observations**:
- Team reverted to Slack threads for task coordination within approximately 3 months of rollout.
- Sarah estimates the team uses roughly 30% of available features.
- She stopped checking weekly reports after concluding they didn't reflect reality, which removed her primary reason for daily engagement with the tool.

**Pain points described**:
- Task status updates require too many interactions (four clicks) compared to the low-friction alternative (a Slack message).
- Weekly reports are unreliable because they depend on task data that isn't being maintained.
- Feature set is mismatched to company size and pace — most features feel designed for larger, slower organisations.

**Workarounds developed**:
- Team uses Slack threads instead of TaskFlow for real-time task coordination. This restores speed and low friction but sacrifices tracking and reporting.

**Emotional moments**:
- Resignation in the phrase "it's honest about how engineers work" — she's not fighting the reversion, she's explaining it as rational.
- "I love in theory" carries a note of disappointment — she wanted the reports to work.

**Contradictions or tensions**:
- She acknowledges Slack coordination is "terrible for tracking" but accepts it anyway. Values tracking in principle, prioritises speed in practice.
- The board view is "genuinely better than Jira" — she recognises the product's quality even while describing abandonment. The tool is good; it just doesn't fit.

**Noteworthy details**:
- She frames the drop-off as structural, not quality-related. The product isn't failing — the interaction cost model is wrong for her team's work rhythm.
- The cascade she describes (low updates -> bad reports -> no reason to open -> further drop in updates) suggests a feedback loop in disengagement.

---

### P2 — Marcus, Product Designer, 120-person company

**Context**: Self-described power user, "religiously" active in TaskFlow. Maintains his own tasks diligently but has watched the tool become effectively a single-user system because teammates don't keep their data current.

**Key quotes**:
- "The 'team view' is really just Marcus's view." -- Concise description of what happens when adoption is uneven. The tool's collaborative features collapse into a personal tool.
- "The thing I actually want is dead simple: who is working on what right now, and is anything blocked." -- Articulates his core need in one sentence. Notable that a product designer frames this as "dead simple" — implying the tool makes a simple question hard to answer.
- "The default view shows everything — completed tasks from three months ago, backlog items nobody's prioritised, stuff from archived sprints. It's like a cluttered desk." -- The metaphor "cluttered desk" suggests the tool's default state creates cognitive overload rather than clarity.
- "I gave up after twenty minutes. I'm a designer, not a systems architect." -- On the automation builder. The phrase "I gave up" is stark. The identity statement ("I'm a designer, not a systems architect") frames the tool as requiring the wrong kind of expertise.

**Behavioural observations**:
- Updates his own tasks consistently — is the most active user on his team.
- Attempted to set up custom filters and saved views to get the information he actually needs.
- Attempted to use the automation builder to maintain data hygiene but abandoned it.
- PMs on his team stopped checking TaskFlow because it didn't reflect team reality.

**Pain points described**:
- Default views are overloaded with stale and irrelevant information.
- Getting to the view he actually needs requires setting up custom filters, saving them, and then remembering to navigate to the custom view instead of the default.
- The automation builder is too complex for a non-technical user to configure.

**Workarounds developed**:
- Created custom filtered views to approximate the "who's working on what / what's blocked" answer. The workaround exists but requires conscious navigation away from defaults.

**Emotional moments**:
- "I gave up" — frustration yielding to resignation about the automation builder.
- There's a quiet loneliness in being the only person maintaining their data in a collaborative tool. He doesn't name it as loneliness, but the image of "Marcus's view" captures it.

**Contradictions or tensions**:
- He uses the tool "religiously" but describes the outcome of that devotion as futile — the team view doesn't work because he's the only one contributing.
- He's a power user who can't get the tool to show him the simple thing he wants without significant setup. Power usage and basic-need frustration coexist.

**Noteworthy details**:
- His core need ("who is working on what right now, and is anything blocked") is a management question coming from a non-manager. He's looking for situational awareness, not control.
- The fact that PMs stopped checking suggests that the data-quality problem cascades upward — the people who most need the collaborative view are the first to abandon it when it's unreliable.

---

### P3 — Alex, VP of Operations, 200-person company

**Context**: VP-level buyer who chose TaskFlow specifically for cross-team visibility across marketing, engineering, and ops. Largest company in the sample (200 people). Speaks from an organisational and strategic perspective rather than a day-to-day user perspective.

**Key quotes**:
- "It works for that if, and only if, everyone puts their work in it. We're at maybe 60% compliance and it's been stuck there for months." -- The "if, and only if" is precise. He understands the dependency clearly. "Stuck there for months" suggests he's tried interventions that haven't moved the number.
- "TaskFlow doesn't meet people where they are. Engineers live in GitHub. Marketers live in their Google Docs and Figma. Ops lives in Slack." -- Describes each team's natural habitat. TaskFlow is positioned as foreign territory for everyone.
- "The GitHub integration just creates a firehose of commits as tasks, which is worse than nothing." -- An integration that was supposed to solve the adoption problem actively made it worse. "Worse than nothing" is a strong judgment.
- "TaskFlow wants to be the center. It should be the lens." -- Center vs. lens is a sharp conceptual distinction. He's articulating a product architecture critique, not a feature request.

**Behavioural observations**:
- Purchased TaskFlow as a cross-team visibility solution. The purchase was strategic, not organic adoption.
- Tried the integration approach (specifically GitHub) to reduce the "extra tab" problem. The attempt failed.
- Compliance has plateaued at roughly 60% and hasn't moved despite ongoing effort.

**Pain points described**:
- TaskFlow requires people to leave their primary work environment to update it — it's "an extra tab they have to remember to update."
- Integrations don't solve this because they bring in raw data (commits) rather than meaningful work-status information.
- Cross-team visibility, the purchased use case, is only achievable at 100% adoption — partial adoption produces partial (and therefore unreliable) visibility.

**Workarounds developed**:
- Tried GitHub integration as a workaround for manual engineer updates. It failed — replaced one problem (no data) with another (noisy, unusable data).

**Emotional moments**:
- "Worse than nothing" carries frustration — not just disappointment but a sense that the attempted solution backfired.
- The final quote ("TaskFlow wants to be the center. It should be the lens.") is said with the clarity of someone who has spent time thinking about why this isn't working. More analytical disappointment than raw frustration.

**Contradictions or tensions**:
- He bought a centralised tool but now articulates that centralisation is the wrong model. His current understanding contradicts his purchasing decision.
- He needs 100% compliance for the tool to serve its purpose but has no mechanism to get past 60%.

**Noteworthy details**:
- He's the only participant who frames the problem architecturally — center vs. lens. This is a product-philosophy observation, not a feature request.
- He describes people's existing work habitats with specificity (GitHub, Google Docs, Figma, Slack), suggesting he understands his teams' real workflows well. The tool doesn't.
- "Stuck there for months" implies the compliance plateau may be a natural ceiling, not a solvable problem within the current model.

---

### P4 — Deepa, Project Manager, 90-person company

**Context**: Self-described "TaskFlow champion" on her team. A project manager whose role has been reshaped by the tool — she now spends significant time on compliance enforcement rather than project management. The richest interview in the set in terms of emotional content and specific workarounds.

**Key quotes**:
- "I spend about 30 minutes a day nagging people to update their tasks. That's my actual job now — not project management, task management enforcement." -- The word "nagging" is loaded. She has reframed her professional role in diminishing terms. "Actual job now" signals that the tool has redefined her work, not supported it.
- "The tool created a new overhead that didn't exist before." -- Direct attribution. The tool added work rather than removing it.
- "It was ugly and limited but everyone updated it because it was one tab in a sheet they already had open." -- Describing the previous spreadsheet. "Ugly and limited" conceded freely; the criterion that matters is whether people used it.
- "TaskFlow is objectively better in every way except the one that matters: people actually using it." -- The structure of this sentence — "objectively better in every way except the one that matters" — is striking. She's naming a hierarchy of product qualities where adoption trumps capability.
- "I'm the human integration layer." -- On updating tasks during standup on behalf of her team. She has named what she's become. The phrase is both precise and weary.
- "The notifications are a disaster." -- Strong, unqualified. Immediately supported by a specific failure cascade: everyone turned them off in week one, now nobody gets any notifications at all, including important ones.

**Behavioural observations**:
- Spends approximately 30 minutes daily reminding teammates to update tasks.
- Has developed a standup workaround: she listens to team members' verbal updates and enters them into TaskFlow in real time.
- Previously used a shared spreadsheet that had higher adoption despite lower capability.

**Pain points described**:
- The tool has turned her role into "task management enforcement" — overhead that didn't exist before the tool was adopted.
- Notification system failed immediately: binary choice between all notifications (overwhelming) and no notifications (missing important ones). No useful middle ground found.
- Self-service promise is unrealised — the tool requires a human intermediary to function.

**Workarounds developed**:
- Updates TaskFlow on behalf of her team during standup meetings, listening to verbal reports and translating them into task updates. This fills the adoption gap but makes her the bottleneck and "defeats the purpose of a self-service tool" (her words).
- The previous shared spreadsheet itself was a simpler tool that worked because it lived inside an already-open context (a Google Sheet tab).

**Emotional moments**:
- "Nagging" — self-deprecation about her current role. The emotional charge is in the gap between what she signed up for (project management) and what she does (enforcement).
- "I'm the human integration layer" — said with what reads as tired self-awareness. She has a clear-eyed view of her situation and it's not a good one.
- "The notifications are a disaster" — unhedged frustration. No qualifiers, no "to be fair." She's not being diplomatic.

**Contradictions or tensions**:
- She is the "TaskFlow champion" who has concluded the tool created overhead that didn't exist before. Champion and critic simultaneously.
- She acknowledges the previous spreadsheet was "ugly and limited" and TaskFlow is "objectively better" — yet the inferior tool had the property that mattered. She's living inside this contradiction daily.
- Her standup workaround makes the tool functional but undermines its stated purpose. The workaround succeeds by abandoning the tool's model.

**Noteworthy details**:
- The notification failure is described as a binary collapse: everything on -> everything off. This suggests the notification system lacks meaningful granularity.
- Her description of the spreadsheet era reveals that the spreadsheet succeeded because of context proximity (already in an open tab), not because of feature quality. This echoes Alex's (P3) observation about meeting people where they are.
- "The tool created a new overhead that didn't exist before" is a direct inversion of the tool's value proposition. The tool was presumably adopted to reduce overhead.

---

### P5 — Raj, Senior Engineer, 150-person company

**Context**: Senior engineer who tried TaskFlow for three months and reverted to a personal text file (todo.txt) for task management. Uses TaskFlow only as an inbox for manager-assigned work. Represents the "just do the work" user perspective.

**Key quotes**:
- "My todo.txt is twelve lines and I know exactly what I'm doing today. TaskFlow showed me 47 tasks across 6 projects with 4 different priority levels and I couldn't tell which ones actually mattered." -- The contrast between 12 lines and 47 tasks / 6 projects / 4 priority levels is stark. He uses specific numbers for both sides, suggesting both are vivid to him. "Couldn't tell which ones actually mattered" — the tool's comprehensiveness obscured rather than clarified.
- "It's like they ported the UI without thinking about the use case." -- On the mobile app's four-click task completion. He recognises the mobile app as "surprisingly good" in general but sees the interaction design as a straight desktop port. "Without thinking about the use case" is a design critique from an engineer.
- "I'm using TaskFlow as an inbox, not a workspace." -- Clean self-description of his actual relationship with the tool. He has redefined its role in his workflow to the minimum viable function.

**Behavioural observations**:
- Tried TaskFlow for three months, then reverted to a personal text file for daily task management.
- Uses TaskFlow only to check new assignments from his manager, then transfers important items to his text file.
- Uses the mobile app during his commute to preview upcoming work.
- Does not mark tasks done in TaskFlow (or does so rarely — the four-click friction discourages it).

**Pain points described**:
- Information overload: 47 tasks across 6 projects with 4 priority levels, with no clear signal about what matters today.
- Task completion requires four clicks on both desktop and mobile, which is disproportionate friction for a "done" action.
- The tool's scope (all tasks, all projects, all priorities) is the opposite of what he needs (today's work, clear priority).

**Workarounds developed**:
- Maintains a 12-line todo.txt file as his actual task management system. TaskFlow is demoted to an assignment-notification channel.
- Manually transfers relevant assignments from TaskFlow to his text file — a human copy-paste integration between systems.

**Emotional moments**:
- "Surprisingly good" about the mobile app — a moment of positive surprise that makes the subsequent criticism (four-click completion) sharper by contrast.
- The return to todo.txt reads as relief, not defeat. He presents it as a rational choice, not a workaround born of frustration.

**Contradictions or tensions**:
- He finds the mobile app "surprisingly good" but describes its core interaction (completing a task) as poorly designed. Good overall, broken at the point of use.
- His manager uses TaskFlow to assign work, creating a dependency that keeps him opening the tool even though he doesn't use it as intended. He can't fully leave.

**Noteworthy details**:
- The specific numbers he cites (12 lines vs. 47 tasks, 6 projects, 4 priority levels) suggest the contrast between clarity and overload is something he feels viscerally.
- His usage pattern (inbox only) means TaskFlow's data on his work is perpetually incomplete — he checks assignments but doesn't update status. From the tool's perspective, his tasks are permanently in-progress.
- He represents a quiet form of non-adoption: he opens the tool regularly but uses almost none of its functionality. Usage metrics might show him as an active user.

---

### P6 — Nina, Marketing Lead, 70-person company

**Context**: Marketing lead at the smallest company in the sample (70 people), managing a team of four. Chose TaskFlow for campaign planning and appreciates the timeline view specifically. Speaks from both the setup/admin perspective and the team-adoption perspective.

**Key quotes**:
- "TaskFlow gives us a Ferrari when we need a bicycle." -- On the mismatch between the tool's capability and her team's needs. The metaphor implies the tool isn't just too much — it's the wrong category of thing.
- "We spent a full day setting it up and I'm still not sure we did it right." -- The time investment (a full day) and lingering uncertainty ("still not sure") suggest onboarding that's effortful without being confidence-building.
- "My previous tool (Todoist) took ten minutes." -- Direct comparison. The ratio (full day vs. ten minutes) frames TaskFlow's setup as orders of magnitude more demanding than what she came from.
- "TaskFlow optimises for the 'set up and manage' person but not for the 'just do the work' person. I love setting it up. My team hates living in it." -- She names two distinct user types and identifies which one the tool serves. "I love setting it up" — she is the beneficiary. "My team hates living in it" — they bear the cost.
- "The gap between the admin experience and the user experience is where adoption dies." -- A precise location for the failure. She's describing a product that serves its buyer but not its users.

**Behavioural observations**:
- Uses the timeline view for campaign planning and considers it best-in-class ("better than Asana, better than Monday").
- Spent a full day on initial setup (templates, custom fields, workflow configuration, integrations).
- Her team of four is living in a tool built for much larger teams.

**Pain points described**:
- Onboarding was overwhelming: five template options, custom field configuration, workflow setup, integration wizard — all presented during initial setup.
- The tool's capability dramatically exceeds her team's needs. A four-person marketing team doesn't need project management software; they need a shared to-do list with due dates.
- Her team members — the daily users — find the tool hostile to their actual work, even though she (the admin/setup person) enjoys it.

**Workarounds developed**:
- None described explicitly. She hasn't built workarounds so much as identified the structural problem. Her previous tool (Todoist) is mentioned as the implicit alternative, not as a current workaround.

**Emotional moments**:
- "Overwhelming" about onboarding — direct statement of emotional state during setup.
- "I love setting it up. My team hates living in it." — the juxtaposition carries guilt or at least uncomfortable awareness. She chose the tool; her team suffers it.
- The "Ferrari when we need a bicycle" metaphor is delivered with clarity, not anger. She admires the tool while recognising it's wrong for her context.

**Contradictions or tensions**:
- She loves the timeline view ("genuinely the best I've seen") but says her team doesn't need project management software at all. The feature she values most belongs to a category of tool she's arguing against.
- She "loves setting it up" but her team "hates living in it" — she and her team have opposite experiences of the same tool. The person who chose the tool is the person it works for.
- She spent a full day on setup and "still isn't sure we did it right" — high effort without corresponding confidence.

**Noteworthy details**:
- Her distinction between the "set up and manage" person and the "just do the work" person articulates a buyer-user split. The person who evaluates and purchases the tool has fundamentally different needs from the people who must use it daily.
- Her team size (4 people) makes the mismatch extreme. The tool's minimum viable complexity exceeds her team's maximum useful complexity.
- She explicitly locates the adoption failure in the gap between admin experience and user experience — not in any single feature or flaw, but in a structural asymmetry in who the product serves.
