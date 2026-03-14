---
name: performance-review
description: Structure a performance review with self-assessment, manager template, and calibration prep. Use when review season kicks off and you need a self-assessment template, writing a manager review for a direct report, prepping rating distributions and promotion cases for calibration, or turning vague feedback into specific behavioral examples.
argument-hint: "<employee name or review cycle>"
---

# /performance-review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Generate performance review templates and help structure feedback.

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

If no mode is specified, ask what type of review they need.

## Output — Self-Assessment Template

```markdown
## Self-Assessment: [Review Period]

### Key Accomplishments
[List key accomplishments from this period — as many as are genuinely significant. For each, describe the situation, your contribution, and the impact.]

1. **[Accomplishment]**
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
[Set goals that are specific and measurable — as many as are meaningful for the upcoming period.]

1. [Goal]

### Feedback for Manager
[How can your manager better support you?]
```

## Output — Manager Review

Before filling in the template, investigate the performance data. Don't start with a rating or summary — start with the evidence and let the picture emerge.

Consider:
- **Trajectory** — Is this person's performance accelerating, steady, or plateauing? What does the trend look like, not just the snapshot?
- **Growth patterns** — Where have they stretched beyond their current level? Where are they still operating within it?
- **Gap between perception and impact** — How does this person see their own contributions compared to how the team and stakeholders experience them?
- **Next-level readiness** — What does this person's work reveal about whether they're ready for the next level? What's the specific gap, if any?
- **Contradictory signals** — Where does the data tell conflicting stories? Strong individual output but weak team impact? Great execution but limited initiative? Name the tension rather than resolving it prematurely.

Let this investigation shape the review — the strengths you highlight, the development areas you choose, and the rating you arrive at should all follow from what the evidence reveals.

```markdown
## Performance Review: [Employee Name]
**Period:** [Date range] | **Manager:** [Your name]

### Performance Summary
[2-3 sentence overall assessment — synthesise from the evidence, don't just restate the rating]

### Key Strengths
[Note what stands out from the evidence — as many or few as the data warrants. Each with a specific example.]

- [Strength with specific example]

### Areas for Development
[Note what the evidence reveals — as many or few as are genuine. Each with specific, actionable guidance.]

- [Area with specific, actionable guidance]

### Goal Achievement
| Goal | Rating | Comments |
|------|--------|----------|
| [Goal] | [Rating] | [Specific observations] |

### Impact and Contributions
[Describe their biggest contributions and impact on the team/org]

### Development Plan
| Skill | Current | Target | Actions |
|-------|---------|--------|---------|
| [Skill] | [Level] | [Level] | [How to get there] |

### Overall Rating: [Exceeds / Meets / Below Expectations]
[Brief justification — this should feel like a conclusion the evidence leads to, not a premise the evidence was selected to support.]

### Compensation Recommendation
[Promotion / Equity refresh / Adjustment / No change — with justification]
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
| Rating | Count | % of Team |
|--------|-------|-----------|
| Exceeds Expectations | [X] | [X]% |
| Meets Expectations | [X] | [X]% |
| Below Expectations | [X] | [X]% |

Company distributions typically fall in the range of 15-20% Exceeds, 60-70% Meets, 10-15% Below. Note any significant deviation from these ranges for discussion — but don't adjust ratings to fit. The team's actual distribution is more useful for calibration than a forced fit.

### Calibration Discussion Points
[Flag employees whose ratings may need discussion — borderline cases, first review at level, recent role changes, ratings that deviate from patterns. Include as many or few as the team warrants.]

- **[Employee]** — [Why this rating may need discussion]

### Promotion Candidates
| Employee | Current Level | Proposed Level | Justification |
|----------|-------------|----------------|---------------|
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

## Tips

1. **Be specific** — "Great job" isn't feedback. "You reduced deploy time 40% by implementing the new CI pipeline" is.
2. **Balance positive and constructive** — Both are essential. Neither should be a surprise.
3. **Focus on behaviors, not personality** — "Your documentation has been incomplete" vs. "You're careless."
4. **Make development actionable** — "Improve communication" is vague. "Present at the next team all-hands" is actionable.
