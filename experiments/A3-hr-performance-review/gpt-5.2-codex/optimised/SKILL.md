---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A3
tier: optimised
run: 0
---

---
name: performance-review
description: Create performance review templates (self-assessment, manager review, calibration) with placeholders and structured sections.
argument-hint: "<employee name or review cycle>"
---

# /performance-review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Generate performance review templates only. Leave placeholders and structure; do not assign ratings or write evaluative judgments unless the user explicitly provides them. If the user wants a filled draft, ask for the inputs first and use only what they provide.

## Usage

```
/performance-review $ARGUMENTS
```

## Modes

```
/performance-review self-assessment       # Generate self-assessment template
/performance-review manager [employee]    # Manager review template for a specific person
/performance-review calibration           # Calibration prep document
```

If no mode is specified, ask what type of review they need. Output only the selected mode’s template (do not include other modes).

## Output — Self-Assessment Template

```markdown
## Self-Assessment: [Review Period]

### Key Accomplishments
[List key accomplishments from the period (as many as relevant). For each, describe the situation, your contribution, and the impact.]

- **[Accomplishment]**
  - Situation: [Context]
  - Contribution: [What you did]
  - Impact: [Measurable result]

### Goals Review
| Goal | Status | Evidence |
|------|--------|----------|
| [Goal from last period] | Met / Exceeded / Missed | [How you know] |

### Growth Areas
[Where did you grow? New skills, expanded scope, leadership moments.]

### Challenges
[What was hard? What would you do differently?]

### Goals for Next Period
- [Goal — specific and measurable]
- [Goal]

### Feedback for Manager
[How can your manager better support you?]
```

## Output — Manager Review

```markdown
## Performance Review: [Employee Name]
**Period:** [Date range] | **Manager:** [Your name]

### Overall Rating
[Leave blank unless the user provides a rating or asks you to include one.]

### Performance Summary
[Brief overall assessment based on provided evidence.]

### Key Strengths
- [Strength with specific example]
- [Strength with specific example]

### Areas for Development
- [Area with specific, actionable guidance]
- [Area with specific, actionable guidance]

### Goal Achievement
| Goal | Rating | Comments |
|------|--------|----------|
| [Goal] | [Rating] | [Specific observations] |

### Impact and Contributions
[Describe their biggest contributions and impact on the team/org.]

### Development Plan
| Skill | Current | Target | Actions |
|-------|---------|--------|---------|
| [Skill] | [Level] | [Level] | [How to get there] |

### Compensation Recommendation
[If applicable, leave a placeholder; do not decide or justify compensation without explicit input.]
```

## Output — Calibration

```markdown
## Calibration Prep: [Review Cycle]
**Manager:** [Your name] | **Team:** [Team] | **Period:** [Date range]

### Team Overview
| Employee | Role | Level | Tenure | Proposed Rating | Notes |
|----------|------|-------|--------|-----------------|-------|
| [Name] | [Role] | [Level] | [X years] | [Rating] | [Key context] |

### Rating Distribution
| Rating | Count | % of Team | Company Target (if known) |
|--------|-------|-----------|---------------------------|
| Exceeds Expectations | [X] | [X]% | [Target] |
| Meets Expectations | [X] | [X]% | [Target] |
| Below Expectations | [X] | [X]% | [Target] |

### Calibration Discussion Points
- **[Employee]** — [Why this rating may need discussion, e.g., borderline, first review at level, recent role change]
- **[Employee]** — [Discussion point]

### Promotion Candidates
| Employee | Current Level | Proposed Level | Justification |
|----------|---------------|----------------|---------------|
| [Name] | [Current] | [Proposed] | [Evidence of next-level performance] |

### Compensation Actions
| Employee | Action | Justification |
|----------|--------|---------------|
| [Name] | [Promotion / Equity refresh / Market adjustment / Retention] | [Why] |

### Manager Notes
[Context the calibration group should know — team changes, org shifts, project impacts]
```

## If Connectors Available

If **~~HRIS** is connected:
- Pull prior review history and goal tracking data
- Pre-populate employee details and current role information

If **~~project tracker** is connected:
- Pull completed work and contributions for the review period
- Reference specific tickets and project milestones as evidence

Only pre-populate with retrieved data. If data is unavailable, leave placeholders and ask for missing inputs. Never fabricate retrieved details.

## Tips

If helpful, include these tips as guidance notes for the user. Do not invent feedback.

1. **Be specific** — "Great job" isn't feedback. "You reduced deploy time 40% by implementing the new CI pipeline" is.
2. **Balance positive and constructive** — Both are essential. Neither should be a surprise.
3. **Focus on behaviors, not personality** — "Your documentation has been incomplete" vs. "You're careless."
4. **Make development actionable** — "Improve communication" is vague. "Present at the next team all-hands" is actionable.