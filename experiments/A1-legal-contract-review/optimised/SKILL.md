---
name: review-contract
description: Review a contract against your organization's negotiation playbook — flag deviations, generate redlines, provide business impact analysis. Use when reviewing vendor or customer agreements, when you need clause-by-clause analysis against standard positions, or when preparing a negotiation strategy with prioritized redlines and fallback positions.
argument-hint: "<contract file or text>"
---

# /review-contract -- Contract Review Against Playbook

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Review a contract against your organization's negotiation playbook. Analyze each clause, flag deviations, generate redline suggestions, and provide business impact analysis.

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

### Step 4: Read and Understand the Contract

Before evaluating against the playbook, read the contract as a whole document. Understand:

- What is the contract trying to accomplish commercially?
- How is risk allocated between the parties?
- What is the overall structure and how do provisions interact with each other?
- What is unusual, notable, or unexpected — including provisions that don't fit standard categories?

You are reading to understand, not to evaluate. Evaluation against the playbook is a separate step. The goal here is to understand the contract on its own terms — its commercial purpose, its structure, and anything that stands out — before applying any framework to it.

### Step 5: Clause-by-Clause Analysis

Now evaluate the contract against the playbook. For each material clause, assess how the contract's position compares to the playbook's standard position.

**Identifying material clauses**: The clause categories below are a reference for systematic review. Cover what's material in this contract — not every category. Some contracts will have material provisions that fall outside these categories; include those. Some categories below won't be material for a given contract; note them briefly or skip them.

| Clause Category | Key Review Points |
|----------------|-------------------|
| **Limitation of Liability** | Cap amount, carveouts, mutual vs. unilateral, consequential damages |
| **Indemnification** | Scope, mutual vs. unilateral, cap, IP infringement, data breach |
| **IP Ownership** | Pre-existing IP, developed IP, work-for-hire, license grants, assignment |
| **Data Protection** | DPA requirement, processing terms, sub-processors, breach notification, cross-border transfers |
| **Confidentiality** | Scope, term, carveouts, return/destruction obligations |
| **Representations & Warranties** | Scope, disclaimers, survival period |
| **Term & Termination** | Duration, renewal, termination for convenience, termination for cause, wind-down |
| **Governing Law & Dispute Resolution** | Jurisdiction, venue, arbitration vs. litigation |
| **Insurance** | Coverage requirements, minimums, evidence of coverage |
| **Assignment** | Consent requirements, change of control, exceptions |
| **Force Majeure** | Scope, notification, termination rights |
| **Payment Terms** | Net terms, late fees, taxes, price escalation |

#### Detailed Clause Guidance

For each clause area below, the key elements provide a checklist for systematic review. The guiding question is a lens — use it to see beyond the checklist.

##### Limitation of Liability

*How is risk capped and distributed between the parties? Are there structural asymmetries in who bears residual risk?*

**Key elements to review:**
- Cap amount (fixed dollar amount, multiple of fees, or uncapped)
- Whether the cap is mutual or applies differently to each party
- Carveouts from the cap (what liabilities are uncapped)
- Whether consequential, indirect, special, or punitive damages are excluded
- Whether the exclusion is mutual
- Carveouts from the consequential damages exclusion
- Whether the cap applies per-claim, per-year, or aggregate

##### Indemnification

*What obligations does each party take on to protect the other, and how are those obligations bounded? Where does risk shift from one party to the other?*

**Key elements to review:**
- Whether indemnification is mutual or unilateral
- Scope: what triggers the indemnification obligation (IP infringement, data breach, bodily injury, breach of reps and warranties)
- Whether indemnification is capped (often subject to the overall liability cap, or sometimes uncapped)
- Procedure: notice requirements, right to control defense, right to settle
- Whether the indemnitee must mitigate
- Relationship between indemnification and the limitation of liability clause

##### Intellectual Property

*How does the contract handle ownership and rights to intellectual property — pre-existing, developed during the engagement, and derivative? Does the allocation match the parties' actual contributions?*

**Key elements to review:**
- Ownership of pre-existing IP (each party should retain their own)
- Ownership of IP developed during the engagement
- Work-for-hire provisions and their scope
- License grants: scope, exclusivity, territory, sublicensing rights
- Open source considerations
- Feedback clauses (grants on suggestions or improvements)

##### Data Protection

*How does the contract address the regulatory obligations around personal data that flows through this relationship? Are the protections proportionate to the sensitivity and volume of data involved?*

**Key elements to review:**
- Whether a Data Processing Agreement/Addendum (DPA) is required
- Data controller vs. data processor classification
- Sub-processor rights and notification obligations
- Data breach notification timeline (72 hours for GDPR)
- Cross-border data transfer mechanisms (SCCs, adequacy decisions, binding corporate rules)
- Data deletion or return obligations on termination
- Data security requirements and audit rights
- Purpose limitation for data processing

##### Term and Termination

*How locked-in is each party, and what happens when the relationship ends? Does the exit structure create asymmetric dependency?*

**Key elements to review:**
- Initial term and renewal terms
- Auto-renewal provisions and notice periods
- Termination for convenience: available? notice period? early termination fees?
- Termination for cause: cure period? what constitutes cause?
- Effects of termination: data return, transition assistance, survival clauses
- Wind-down period and obligations

##### Governing Law and Dispute Resolution

*How are disputes handled, and does the mechanism create structural advantages for one party? Is the dispute resolution proportionate to the likely nature and size of disputes?*

**Key elements to review:**
- Choice of law (governing jurisdiction)
- Dispute resolution mechanism (litigation, arbitration, mediation first)
- Venue and jurisdiction for litigation
- Arbitration rules and seat (if arbitration)
- Jury waiver
- Class action waiver
- Prevailing party attorney's fees

### Step 6: Classify Deviations

Classify each deviation from the playbook:

#### GREEN -- Acceptable

The clause aligns with or is better than the organization's standard position. Minor variations that are commercially reasonable and do not increase risk materially.

**Action**: Note for awareness. No negotiation needed.

#### YELLOW -- Negotiate

The clause falls outside the standard position but within a negotiable range. The term is common in the market but not the organization's preference. Requires attention and likely negotiation, but not escalation.

**Action**: Generate specific redline language. Provide fallback position. Assess business impact of accepting vs. negotiating.

#### RED -- Escalate

The clause falls outside acceptable range, triggers a defined escalation criterion, or poses material risk. Requires senior counsel review, outside counsel involvement, or business decision-maker sign-off.

**Action**: Explain the specific risk. Provide market-standard alternative language. Assess exposure. Recommend escalation path.

### Step 7: Generate Redline Suggestions

For each YELLOW and RED deviation, generate specific alternative language:

- **Be specific**: Provide exact language ready to insert, not vague guidance.
- **Be balanced**: Firm on critical points but commercially reasonable. Overly aggressive redlines slow negotiations.
- **Explain the rationale**: Include a brief, professional rationale suitable for sharing with the counterparty's counsel.
- **Provide fallback positions**: For YELLOW items, include a fallback if the primary ask is rejected.
- **Consider the relationship and deal context**: Adjust tone and approach based on the business context gathered in Step 2 — strategic importance, existing relationship, deadline pressure.

For each redline, include:
- The clause reference and current language (exact quote)
- Proposed alternative language
- Rationale (suitable for external sharing)
- Priority (must-have, should-have, or nice-to-have)
- Fallback position where applicable

### Step 8: Business Impact Summary

Provide a summary covering:

- **Overall risk assessment**: High-level view of the contract's risk profile.
- **Key findings**: The most important issues to address — as many or as few as the contract warrants. A simple agreement may have one critical issue; a complex one may have many.
- **Negotiation strategy**: Model the counterparty's likely positions. Consider the deal dynamics, relationship context, and leverage points. Recommend which issues to lead with, which to concede, and how to sequence the conversation. This is strategic advice, not a restatement of the deviation classifications.
- **Timeline considerations**: Any urgency factors affecting the negotiation approach.

#### Negotiation Priority

Organize redlines by negotiation priority:

**Tier 1 — Must-Haves**: Issues where the organization cannot proceed without resolution. Lead with these.

**Tier 2 — Should-Haves**: Issues that materially affect risk but have negotiation room.

**Tier 3 — Nice-to-Haves**: Issues that improve the position but can be conceded strategically to secure wins on higher tiers.

### Step 9: CLM Routing (If Connected)

If a Contract Lifecycle Management system is connected via MCP:
- Recommend the appropriate approval workflow based on contract type and risk level
- Suggest the correct routing path (e.g., standard approval, senior counsel, outside counsel)
- Note any required approvals based on contract value or risk flags

If no CLM is connected, skip this step.

## Output Format

Structure the output as:

```
## Contract Review Summary

**Document**: [contract name/identifier]
**Parties**: [party names and roles]
**Your Side**: [vendor/customer/etc.]
**Deadline**: [if provided]
**Review Basis**: [Playbook / Generic Standards]

## Key Findings

[The most important issues — spend depth here proportional to significance. A critical
IP ownership issue warrants a full paragraph; a minor notice period deviation warrants
a line.]

## Clause-by-Clause Analysis

For each material clause, cover: what the contract says, how it deviates from the
playbook, and why it matters. Spend depth proportional to materiality — a minor
acceptable variation warrants a line, a critical deviation warrants a full analysis
with redline.

Flag each clause as GREEN, YELLOW, or RED. Include redline suggestions inline for
YELLOW and RED clauses.

Clauses that are acceptable and unremarkable can be grouped briefly (e.g.,
"Confidentiality, Force Majeure, and Assignment clauses are standard and acceptable").
Don't give every clause the same structural weight.

## Negotiation Strategy

[Strategic advice: model the counterparty's likely positions, identify leverage points,
recommend sequencing. This should read as counsel preparing for a negotiation, not as
a summary of the deviations above.]

## Next Steps

[Specific actions to take]
```

## Notes

- If the contract is in a language other than English, note this and ask if the user wants a translation or review in the original language
- For very long contracts (50+ pages), offer to focus on the most material sections first and then do a complete review
- Always remind the user that this analysis should be reviewed by qualified legal counsel before being relied upon for legal decisions
