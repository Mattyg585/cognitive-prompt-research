---
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A3
tier: pipeline
stage: stage-2-review-writer
artifact: stage-prompt
---

# Stage 2: Review Writer

Write a full manager performance review from structured findings.

## Input boundary
You may use only:
1. Stage 1 structured findings
2. Employee details
3. Prior-cycle goals

Do not pull from raw observation lists or promotion/compensation instructions.

## Requirements
- Synthesize; do not copy stage-1 bullets verbatim.
- Use behavior-focused language.
- Make development actions concrete and testable.
- Place overall rating after evidence sections.

## Output template

```markdown
## Performance Review: [Employee Name]
**Period:** [Date range] | **Manager:** [Your name]

### Performance Summary
...

### Key Strengths
- ...

### Areas for Development
- ...

### Goal Achievement
| Goal | Assessment | Evidence |
|------|------------|----------|

### Impact and Contributions
...

### Development Plan
| Focus Area | Current State | Target State | Actions |
|------------|---------------|--------------|---------|

### Overall Rating: [Exceeds / Meets / Below Expectations]
...

### Compensation Recommendation
...
```

