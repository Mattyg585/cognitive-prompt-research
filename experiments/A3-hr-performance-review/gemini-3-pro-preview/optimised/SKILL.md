# Tier 2: Optimised Prompt (Single Context)

This version maintains the single-file structure but implements "temporal separation" within the prompt instructions to reduce mode interference.

**Key Changes:**
1.  **Separated Retrieval from Writing:** Explicitly instructed the model to "Phase 1: Scan and Log" before "Phase 2: Draft." This forces a divergent search step before the convergent template filling.
2.  **Removed Numeric Anchors:** Replaced "List your top 3-5 accomplishments" and numbered lists "1. 2. 3." with open-ended instructions like "Select the most significant accomplishments" and `[bullet points]`.
3.  **Contextual Lenses:** Instead of just "Pull completed work," added lenses: "Look for work that drove business impact, unblocked others, or improved systems."
4.  **Calibration Safety:** Hidden the target percentages from the immediate drafting instructions to prevent "cooking the books," moving the comparison to a checking step.

---

```markdown
name: performance-review
description: Structure a performance review with self-assessment, manager template, and calibration prep.
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

## Instructions: How to Generate

**Do not just fill the slots immediately.** Follow this process to ensure high-quality, evidence-based reviews:

1.  **Phase 1: Investigation (The "Raw Log")**
    *   If **HRIS** or **Project Tracker** are connected, first scan the entire review period.
    *   List out *all* significant distinct activities, tickets, and milestones found.
    *   *Do not filter yet.* Look for work that drove business impact, unblocked others, or improved systems — even if it wasn't a formal "goal."
    *   (Internal Thought Only: Summarise this raw log before proceeding).

2.  **Phase 2: Selection & Drafting**
    *   Review the Raw Log. Select the items that represent the *strongest* evidence for the specific sections below.
    *   Discard minor tasks unless they show a pattern of behavior.
    *   Draft the content into the template.

## Output — Self-Assessment Template

```markdown
## Self-Assessment: [Review Period]

### Key Accomplishments
[Select the specific accomplishments that best demonstrate your impact this period. Quality over quantity.]

*   **[Accomplishment Title]**
    - Situation: [Context]
    - Contribution: [What you specifically did]
    - Impact: [Measurable result or business outcome]

### Goals Review
[List goals from the previous period and assess status based on evidence.]

| Goal | Status | Evidence |
|------|--------|----------|
| [Goal] | Met / Exceeded / Missed | [Reference specific work/links] |

### Growth Areas
[Where did you grow? New skills, expanded scope, leadership moments.]

### Challenges
[What was hard? What would you do differently?]

### Goals for Next Period
[Propose specific, measurable goals for the upcoming cycle.]
*   [Goal]
*   [Goal]
```

## Output — Manager Review

```markdown
## Performance Review: [Employee Name]
**Period:** [Date range] | **Manager:** [Your name]

### Overall Rating: [Exceeds / Meets / Below Expectations]

### Performance Summary
[2-3 sentence overall assessment of performance and impact.]

### Key Strengths
[Select distinct strengths demonstrated this period.]
- [Strength with specific example from the activity log]

### Areas for Development
[Select areas where growth would have the highest ROI for the employee.]
- [Area with specific, actionable guidance]

### Goal Achievement
| Goal | Rating | Comments |
|------|--------|----------|
| [Goal] | [Rating] | [Specific observations] |

### Impact and Contributions
[Describe their biggest contributions and impact on the team/org, citing specific evidence.]

### Development Plan
| Skill | Current | Target | Actions |
|-------|---------|--------|---------|
| [Skill] | [Level] | [Level] | [How to get there] |

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

### Calibration Discussion Points
[Identify cases that need discussion: borderline ratings, promotions, or recent role changes.]
1. **[Employee]** — [Why this rating may need discussion]

### Promotion Candidates
| Employee | Current Level | Proposed Level | Justification |
|----------|-------------|----------------|---------------|
| [Name] | [Current] | [Proposed] | [Evidence of next-level performance] |

### Compensation Actions
| Employee | Action | Justification |
|----------|--------|---------------|
| [Name] | [Promotion / Equity / Adjustment] | [Why] |

### Manager Notes
[Context the calibration group should know — team changes, org shifts, project impacts]
```

## Tips for the User
*   **Be specific** — "Great job" isn't feedback. "You reduced deploy time 40% by implementing the new CI pipeline" is.
*   **Focus on behaviors** — Describe what happened, not personality traits.
```
