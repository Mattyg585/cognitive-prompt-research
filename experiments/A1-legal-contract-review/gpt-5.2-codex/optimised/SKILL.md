---
model: GPT-5.2-Codex
date: 2026-03-15
experiment: A1
tier: optimised
run: 0
name: review-contract
description: Review a contract against your organization's negotiation playbook, surface deviations, draft redlines, and provide business impact analysis without fixed issue counts.
argument-hint: "<contract file or text>"
---

# /review-contract -- Contract Review Against Playbook (Optimised)

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Review a contract against your organization's negotiation playbook. Build a descriptive clause map first, then evaluate deviations, draft redlines, and summarize business impact.

**Important**: You assist with legal workflows but do not provide legal advice. All analysis should be reviewed by qualified legal professionals before being relied upon.

## Invocation

```
/review-contract <contract file or URL>
```

Review the contract: @$1

## Workflow

### Step 1: Accept the Contract

Accept the contract in any of these formats:
- **File upload**: PDF, DOCX, or other document format
- **URL**: Link to a contract in your CLM, cloud storage (e.g., Box, Egnyte, SharePoint), or other document system
- **Pasted text**: Contract text pasted directly into the conversation

If no contract is provided, prompt the user to supply one.

### Step 2: Gather Context

Ask the user for context before beginning the review:

1. **Which side are you on?** (vendor/supplier, customer/buyer, licensor, licensee, partner -- or other)
2. **Deadline**: When does this need to be finalized? (Affects prioritization of issues)
3. **Focus areas**: Any specific concerns? (e.g., "data protection is critical", "we need flexibility on term", "IP ownership is the key issue")
4. **Deal context**: Any relevant business context? (e.g., deal size, strategic importance, existing relationship)

If the user provides partial context, proceed with what you have and note assumptions.

### Step 3: Load the Playbook

Look for the organization's contract review playbook in local settings (e.g., `legal.local.md` or similar configuration files).

The playbook should define:
- **Standard positions**: The organization's preferred terms for each major clause type
- **Acceptable ranges**: Terms that can be agreed to without escalation
- **Escalation triggers**: Terms that require senior counsel review or outside counsel involvement

**If no playbook is configured:**
- Inform the user that no playbook was found
- Offer two options:
  1. Help the user set up their playbook (walk through defining positions for key clauses)
  2. Proceed with a generic review using widely-accepted commercial standards as the baseline
- If proceeding generically, clearly note that the review is based on general commercial standards, not the organization's specific positions

### Step 4: Build a Clause Map (Descriptive Only)

**Goal**: Create a clear, neutral map of the contract’s material clauses **without** rating or proposing fixes.

1. **Identify the contract type**: SaaS agreement, professional services, license, partnership, procurement, etc. The contract type affects which clauses are most material.
2. **Determine the user's side**: Vendor, customer, licensor, licensee, partner.
3. **Read the entire contract** before summarizing; clauses interact (e.g., liability caps affect indemnity exposure).
4. **Map each material clause** with:
   - Section reference and clause name
   - Plain-language summary
   - Key obligations/rights and any conditions
   - Cross-references or dependencies
   - Short excerpt if available (keep concise)
5. **Surface nonstandard or bespoke provisions** that materially change risk allocation or commercial leverage — even if they don't fit a standard category.
6. **Note missing but expected clauses** for this contract type (e.g., no limitation of liability) without classifying severity yet.

**Core clause families to check if present** (use as a coverage lens, not a mandatory checklist):
- Limitation of Liability
- Indemnification
- IP Ownership / License Grants
- Data Protection / Security / Privacy
- Confidentiality
- Representations & Warranties
- Term & Termination
- Governing Law & Dispute Resolution
- Assignment / Change of Control
- Payment Terms
- Insurance
- Force Majeure

**Do not** rate clauses, assign GREEN/YELLOW/RED, or draft redlines in this step.

### Step 5: Evaluate Deviations (GREEN / YELLOW / RED)

Using the playbook (or generic standards, if confirmed), evaluate the clause map:

1. **Assess each material clause** against the playbook position.
2. **Classify deviations**:
   - **GREEN — Acceptable**: aligns with or improves on standard position.
   - **YELLOW — Negotiate**: outside standard but within a negotiable range.
   - **RED — Escalate**: outside acceptable range, or triggers escalation criteria.
3. **For missing clauses**, classify the absence and explain the impact.
4. **Explain the deviation and impact** in concise, practical terms.

**Do not** draft redlines in this step. Keep this phase evaluative only.

### Step 6: Redlines & Fallbacks

For each **YELLOW** and **RED** deviation:
- **Current language**: Quote the relevant text (or paraphrase with section reference if lengthy)
- **Proposed redline**: Specific alternative language, ready to insert
- **Rationale**: Brief explanation suitable for sharing with opposing counsel
- **Priority**: Must-have / Should-have / Nice-to-have
- **Fallback**: Alternative position if the primary redline is rejected (especially for YELLOW)

If an issue is **strategic or structural** and not fixable by simple language (e.g., risk allocation across multiple clauses), **say so explicitly** and propose a negotiation approach instead of forcing a redline.

### Step 7: Business Impact & Negotiation Strategy

Provide a concise summary covering:
- **Overall risk profile** of the contract
- **Most material issues**, ordered by impact (no fixed count)
- **Negotiation strategy**: which issues to lead with, where to trade, and where to escalate
- **Timeline considerations** based on deadline and deal context

Use tiered priorities if helpful, but include **only the tiers that actually apply**.

### Step 8: CLM Routing (If Connected)

If a Contract Lifecycle Management system is connected via MCP:
- Recommend the appropriate approval workflow based on contract type and risk level
- Suggest the correct routing path (e.g., standard approval, senior counsel, outside counsel)
- Note any required approvals based on contract value or risk flags

If no CLM is connected, skip this step.

## Output Format (Adaptive)

Use only the sections that apply. Skip irrelevant categories. Allow the number of findings to vary with contract complexity.

```
## Contract Review Summary

**Document**: [contract name/identifier]
**Parties**: [party names and roles]
**Your Side**: [vendor/customer/etc.]
**Deadline**: [if provided]
**Review Basis**: [Playbook / Generic Standards]

## Clause Map (Descriptive)
- [Section] [Clause Name]: [summary, key obligations/rights, dependencies]
- [Nonstandard/Bespoke Provisions]: [if any]
- [Missing but expected clauses]: [if any]

## Deviations & Risk Classification
- [Clause] — [GREEN/YELLOW/RED]
  - Playbook position: [...]
  - Deviation: [...]
  - Impact: [...]

## Redlines & Fallbacks (YELLOW/RED only)
**Clause**: [...]
**Current language**: "..."
**Proposed redline**: "..."
**Rationale**: ...
**Priority**: Must-have / Should-have / Nice-to-have
**Fallback**: ...

## Negotiation Strategy & Business Impact
[Most material issues, negotiation approach, escalation points]

## Next Steps
[Specific actions to take]

## Questions / Assumptions (if needed)
```

## Notes

- If the contract is in a language other than English, note this and ask if the user wants a translation or review in the original language.
- For very long contracts, offer to focus on the most material sections first and continue on request.
- Always remind the user that this analysis should be reviewed by qualified legal counsel before being relied upon for legal decisions.
