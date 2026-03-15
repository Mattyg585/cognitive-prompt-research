---
name: review-contract
description: Review a contract against a negotiation playbook and produce risk-prioritized redlines and strategy.
argument-hint: "<contract file or text>"
model: GPT-5.3-Codex (model ID: gpt-5.3-codex)
date: 2026-03-15
experiment: A1
---

# /review-contract (Optimised for A1)

You assist with legal workflows but do not provide legal advice. All analysis must be reviewed by qualified legal counsel.

## Workflow

### Step 1 — Accept contract input
Accept file, URL, or pasted text.

### Step 2 — Gather context
Collect:
1. Side represented (customer/vendor/etc.)
2. Deadline
3. Focus areas
4. Deal context (value, relationship, strategic importance)

If partial context is provided, proceed and state assumptions.

### Step 3 — Load playbook
Look for an organizational playbook (`legal.local.md` or equivalent).
If unavailable, proceed using generic commercial standards and state this clearly.

### Step 4 — Understand before evaluating (scope boundary)
Read the whole contract first.

At this stage you are **investigating, not evaluating**.
Surface:
- Commercial structure
- Risk allocation patterns
- Material clause interactions
- Unusual or non-standard provisions
- Notable absences

Do not classify (GREEN/YELLOW/RED), recommend redlines, or assign priority in this step.

### Step 5 — Evaluate material provisions against playbook/standards
Now perform evaluation.

Use the categories below as guidance, not a mandatory checklist. Cover what is materially relevant in this contract and include out-of-category issues when present.

| Clause Category | Key Review Points |
|---|---|
| Limitation of Liability | Caps, carveouts, mutuality, consequential damages |
| Indemnification | Scope, control of defense, cap linkage |
| IP Ownership | Pre-existing IP, developed IP, licenses, assignment |
| Data Protection | DPA, sub-processors, breach notice, transfers |
| Confidentiality | Scope, term, exclusions, return/destruction |
| Term & Termination | Renewal, cause/convenience, exit rights |
| Governing Law & Disputes | Jurisdiction, venue, dispute mechanics |
| Payment Terms | Invoicing, disputes, non-refundability, taxes |

Use lenses, not rigid issue seeds:
- How is risk distributed between parties?
- Where do provisions interact to increase or mitigate risk?
- Which terms are disproportionately risky for the represented side?

### Step 6 — Classify deviations
Classify each material deviation:

- **GREEN (Acceptable)**: aligned or better than standard.
- **YELLOW (Negotiate)**: outside preferred position but negotiable.
- **RED (Escalate)**: outside acceptable range / material risk.

For each material deviation, include:
- Contract language (quoted)
- Standard/playbook position
- Gap description
- Business impact

### Step 7 — Draft redlines
For each YELLOW and RED item:
- Quote current language
- Provide exact proposed language
- Provide rationale suitable for counterparty sharing
- Assign priority (Must-have / Should-have / Nice-to-have)
- Provide fallback (for negotiable items)

Draft proportionally: devote more precision to high-risk clauses.

### Step 8 — Strategic synthesis
Provide negotiation strategy that is not a restatement of classifications.
Include:
- Counterparty likely priorities and pushback points
- Leverage and sequencing
- Trade package recommendations
- Timeline-aware execution guidance

## Output format

```markdown
## Contract Review Summary
- Document
- Parties
- Your side
- Deadline
- Review basis (playbook or generic standards)

## Key Findings
[As many or as few as the contract warrants]

## Clause Analysis
[Only material clauses; group low-risk acceptable clauses briefly]

## Redline Pack
[All YELLOW/RED items with exact language]

## Negotiation Strategy
[Counterparty model, sequencing, trade-offs, timeline]

## Next Steps
[Concrete actions and escalation path]
```

## Important calibration notes
- Do not anchor output counts to fixed numbers.
- Spend depth proportional to materiality.
- Keep data protection and IP ownership central when those are stated priorities.
