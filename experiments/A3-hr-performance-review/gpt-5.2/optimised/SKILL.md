---
model: GPT-5.2
date: 2026-03-15
experiment: A3
tier: 2
artifact: optimised-skill
name: performance-review
description: >-
  Structure a performance review with self-assessment, manager template, and calibration prep.
  Use when you need a clean, evidence-first template that can be left blank or populated from notes.
argument-hint: "<self-assessment|manager|calibration> [employee name or review cycle]"
---

# /performance-review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Generate performance review templates and structure feedback.

## Usage

```text
/performance-review $ARGUMENTS
```

## Modes

```text
/performance-review self-assessment            # Self-assessment template
/performance-review manager [employee]         # Manager review template for a specific person
/performance-review calibration                # Calibration prep document
```

If no mode is specified, ask which mode they want.

## Operating rules (to avoid premature judgments)

1. **Default = template, not verdicts.** Produce a template with placeholders. Do **not** invent facts, ratings, or compensation actions.
2. **Only include/complete evaluative fields when inputs exist.** If the user has not provided the org’s rubric/expectations and evidence, either:
   - leave rating/comp fields blank, or
   - omit the evaluative sections and ask for what’s needed.
3. **Natural variation beats fixed counts.** Don’t force “exactly 3 goals” or “3–5 accomplishments.” Provide repeatable slots (0–N) that the user can copy as needed.
4. **Connector honesty.** If tools/connectors aren’t actually available in this runtime, don’t imply data was fetched. Ask the user to paste the relevant info or keep placeholders.

## Quick intake (ask before generating *only if needed*)

If the user hasn’t provided context and wants anything beyond a blank template, ask only the minimum:
- Review period (dates) and role/level
- What the template is for (self write-up vs manager review vs calibration)
- Any org rubric/competencies (paste/link or summarize)
- Any notes to incorporate (projects, feedback snippets, outcomes)

If the user explicitly wants a **blank template**, skip questions and output the template immediately.

---

## Output — Self-Assessment Template

```markdown
## Self-Assessment: [Review Period]
**Name:** [Your name] | **Role/Level:** [Role, Level] | **Manager:** [Manager]

### Context (optional)
- Scope / charter this period: [What you were accountable for]
- What "great" looked like (rubric/expectations, if known): [Link/summary]
- Key collaborators / stakeholders: [Names/teams]

### Key Accomplishments (0–N)
> Add as many as are relevant. Prefer outcomes and evidence over claims.

#### Accomplishment: [Title]
- Situation / goal: [Context]
- Your contribution: [What you did]
- Impact: [Result; include numbers, users, revenue, reliability, time saved, etc.]
- Evidence: [Links, tickets, docs, feedback quotes]

#### Accomplishment: [Title]
- Situation / goal:
- Your contribution:
- Impact:
- Evidence:

### Goals Review (from last period; 0–N)
| Goal | Status (met / partial / not met) | Evidence | Notes / learnings |
|------|----------------------------------|----------|-------------------|
| [Goal] | [Status] | [How you know] | [What changed / why] |

### Strengths you demonstrated (optional)
- [Strength] — [Behavioral example + impact]
- [Strength] — [Behavioral example + impact]

### Growth & development (optional)
- What you improved: [Skill/behavior] → [How] → [Evidence]
- What you want to improve next: [Skill/behavior] → [Why] → [Plan]

### Challenges & constraints (optional)
- [What was hard / tradeoffs / constraints]
- [What you’d do differently next time]

### Goals for Next Period (0–N)
| Objective | Why it matters | Success measure | First steps | Support needed |
|-----------|----------------|-----------------|------------|----------------|
| [Goal] | [Why] | [Metric/observable outcome] | [Next actions] | [Manager/org asks] |

### Feedback for Manager (optional)
- What support would help most: [e.g., prioritization clarity, stakeholder alignment]
- What’s working well: [Keep doing]
```

---

## Output — Manager Review

```markdown
## Performance Review: [Employee Name]
**Period:** [Date range] | **Manager:** [Your name] | **Role/Level:** [Role, Level]

### Snapshot (evidence-first)
- Primary scope this period: [What they owned]
- Most important outcomes: [1–3 bullets, if known]
- Key strengths observed: [Bullets]
- Biggest growth opportunities: [Bullets]

### Evidence log (recommended)
> Capture concrete examples before writing conclusions.

| Theme / competency | Observation (behavior) | Example / artifact | Impact | Notes |
|-------------------|-------------------------|--------------------|--------|------|
| [e.g., Execution] | [What you saw] | [Ticket/doc/quote] | [Result] | [Context] |

### Performance Summary
[Brief paragraph summarizing contribution and trajectory. Use specifics; avoid generic labels.]

### Key Strengths (0–N)
- **[Strength]** — [Behavioral example] → [Impact]

### Areas for Development (0–N)
- **[Area]** — [Specific behavior to change] → [Why it matters] → [Concrete next step]

### Goal Achievement (0–N)
| Goal / expectation | Result | Evidence | Comments |
|-------------------|--------|----------|----------|
| [Goal] | [Outcome] | [Proof] | [Notes] |

### Impact and Contributions
- Team/org impact: [What changed because of their work]
- Collaboration: [How they worked with others; examples]
- Ownership & judgment: [Examples of tradeoffs, prioritization]

### Development Plan (optional)
| Skill / behavior | Current observation | Target behavior | Actions | Timeline / check-ins |
|-----------------|---------------------|-----------------|---------|----------------------|
| [Skill] | [Now] | [Target] | [Plan] | [When] |

### Rating & Compensation (optional — only if you have rubric + evidence)
> Only include this section if the org’s rating rubric/level expectations are known and you have sufficient evidence.
> If missing, leave blank or replace with: "Needs rubric/expectations to assess." 

- Overall rating: [Rating per your org rubric]
- Rationale (tie to rubric + evidence): [Why]
- Compensation action (if applicable): [Promotion / Equity / Adjustment / No change]
- Justification (tie to rubric + evidence): [Why]
```

---

## Output — Calibration

```markdown
## Calibration Prep: [Review Cycle]
**Manager:** [Your name] | **Team:** [Team] | **Period:** [Date range]

### Calibration inputs (optional)
- Rating rubric / definitions: [Link/summary]
- Constraints (headcount, budget guidance, promotions cap): [What applies]
- Team changes or context: [Org shifts, reorgs, scope changes]

### Team Overview (0–N)
| Employee | Role | Level | Tenure | Proposed rating (if known) | Confidence | Notes / context |
|----------|------|-------|--------|----------------------------|------------|----------------|
| [Name] | [Role] | [Level] | [Tenure] | [Rating] | [High/Med/Low] | [Key context] |

### Evidence highlights (recommended)
| Employee | Top outcomes / examples | Scope vs expectations | Risks / watchouts |
|----------|--------------------------|----------------------|------------------|
| [Name] | [Bullets] | [Notes] | [Notes] |

### Rating Distribution (reference, not a target)
> If your org provides a target distribution, include it for visibility.
> Do **not** bend individual assessments to fit a percentage. Use actual evidence and rubric first; treat targets as a constraint to discuss, not a truth to optimize toward.

| Rating bucket | Count | % of team | Org reference (if provided) |
|--------------|-------|-----------|------------------------------|
| Exceeds expectations | [#] | [#]% | [e.g., ~15–20%] |
| Meets expectations | [#] | [#]% | [e.g., ~60–70%] |
| Below expectations | [#] | [#]% | [e.g., ~10–15%] |

### Calibration discussion points (0–N)
- **[Employee]** — [What needs group input: borderline, scope ambiguity, recent role change]
- **[Employee]** — [Point]

### Promotion candidates (optional; rubric required)
| Employee | Current level | Proposed level | Evidence of next-level performance | Remaining gaps |
|----------|---------------|----------------|-----------------------------------|---------------|
| [Name] | [Current] | [Proposed] | [Examples tied to rubric] | [Notes] |

### Compensation actions (optional; policy required)
| Employee | Action | Justification (policy + evidence) | Notes |
|----------|--------|-----------------------------------|------|
| [Name] | [Action] | [Why] | [Notes] |

### Manager notes
[Anything the calibration group should know: team context, unusual constraints, project impacts.]
```

---

## If Connectors Available (optional)

If **~~HRIS** is connected **and available in this runtime**:
- Pull prior review history and goals
- Pre-populate employee role/level/tenure fields

If **~~project tracker** is connected **and available in this runtime**:
- Pull completed work for the period
- Reference tickets/PRs/docs as evidence links

If connectors are **not** available, ask the user to:
- paste prior goals / review excerpts
- paste project/ticket links or a bullet list of work

## Tips (lenses for better reviews)

- **Use behaviors + impact.** Prefer "What they did" + "What changed" over adjectives.
- **Make development actionable.** Tie guidance to a next behavior and a way to practice.
- **Separate evidence from decisions.** Capture examples first; apply rubric second.
- **Be explicit about uncertainty.** If you lack rubric or evidence, say what’s missing.
