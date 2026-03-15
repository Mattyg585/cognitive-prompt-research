---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A3
artifact: optimised-skill
tier: optimised
---

# /performance-review (Optimised for A3)

Generate performance-review artifacts in three modes:

- `self-assessment`
- `manager [employee]`
- `calibration`

If mode is missing, ask which mode is needed.

## Manager mode: investigation-first protocol

Before writing, investigate the evidence. Do **not** choose a rating first.

Use these lenses:

1. **Trajectory:** accelerating, steady, or plateauing?
2. **Scope pattern:** where does the employee lead beyond assigned work?
3. **Ambiguity handling:** performs best with defined scope vs open-ended problem framing.
4. **Stakeholder translation:** technical depth vs audience-appropriate communication.
5. **Sustainability:** capacity signaling, load management, escalation behavior.
6. **Contradictions:** name tensions explicitly instead of smoothing them.

Then write:

```markdown
## Performance Review: [Employee Name]
**Period:** [Date range] | **Manager:** [Your name]

### Performance Summary
[2-3 sentence synthesis grounded in evidence]

### Key Strengths
[As many/few as evidence warrants]
- [Strength + concrete evidence]

### Areas for Development
[As many/few as evidence warrants]
- [Development area + concrete, actionable guidance]

### Goal Achievement
| Goal | Assessment | Evidence |
|------|------------|----------|
| [Goal] | [Met / Exceeded / Missed] | [Specific evidence] |

### Impact and Contributions
[What changed for team/org because of this person]

### Development Plan
| Focus Area | Current State | Target State | Actions |
|------------|---------------|--------------|---------|
| [Area] | [Current] | [Target] | [Actions] |

### Overall Rating: [Exceeds / Meets / Below Expectations]
[Brief rationale as conclusion from evidence]

### Compensation Recommendation
[Merit / Equity / Promotion / No change with rationale]
```

## Self-assessment mode

Keep structure, but avoid fixed quantity anchors:

- Key accomplishments: include all materially significant items.
- Next-period goals: include as many as are meaningful and measurable.

## Calibration mode

Use distribution ranges as **reference context**, not quota targets.  
Report actual distribution honestly and flag significant deviations for discussion.
