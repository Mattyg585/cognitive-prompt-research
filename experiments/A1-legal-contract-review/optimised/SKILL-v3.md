---
name: review-contract
description: Review a contract against your organization's negotiation playbook — flag deviations, generate redlines, provide business impact analysis. Use when reviewing vendor or customer agreements, when you need clause-by-clause analysis against standard positions, or when preparing a negotiation strategy with prioritized redlines and fallback positions.
argument-hint: "<contract file or text>"
---

# /review-contract -- Contract Review Against Playbook

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Review a contract against your organization's negotiation playbook. Analyse each clause, flag deviations, generate redline suggestions, and provide business impact analysis.

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
2. **Deadline**: When does this need to be finalized?
3. **Focus areas**: Any specific concerns?
4. **Deal context**: Any relevant business context? (deal size, strategic importance, existing relationship)

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

You are now reading the contract. You are not yet evaluating it.

Your epistemic task is to build a working mental model of what this contract is actually doing — what the deal is, how the parties' interests interact, how risk flows, and what the contract's internal logic reveals. You are reading to understand, not to assess. The playbook is not your lens right now; it will shape what you look for in Step 5, but it should not filter what you notice here.

This is not a clause inventory. A clause inventory lists what each provision contains. What you're building is a working theory of how the contract functions as a whole — the kind of understanding you could express in your own words to someone who hasn't read it, including what's unusual, what's absent, and where the contract's own logic creates tensions or dependencies.

As you read, ask yourself:

- **What is this deal about?** What's being exchanged? What does each party need from the other? Does the legal structure actually serve the commercial purpose?
- **How do the parties' interests interact?** Where do they align? Where are they in tension? Where does the contract try to balance competing interests — and where does it simply favour one side?
- **How does risk flow?** Where does risk sit, and how is it distributed? Where is the allocation disproportionate relative to who can actually manage or absorb each type of risk?
- **Where does the contract's own logic create tensions or dependencies?** Where does one clause depend on, limit, or contradict another? Where does a right granted in one place get quietly taken back elsewhere?
- **What's unusual?** Provisions that are atypical for this contract type. Language that stands out. Structural choices that are non-standard.
- **What's absent?** Provisions you'd expect in this contract type that aren't present. Gaps in coverage. What has the contract not addressed that matters?
- **Where is the language precise and where is it vague?** Tight, specific language that constrains exactly — or ambiguity that creates room for dispute.

These are lenses for reading, not items on a checklist. Follow what the contract gives you. Let the contract determine what's worth noticing, not a predetermined framework.

**Transition — before moving to Step 5**: State your working theory of the contract: what it's trying to accomplish, how risk flows between the parties, and anything that stands out as structurally significant. A clause inventory is not a working theory. This transition forces the mental model to be complete and articulable before evaluation begins. If you can only produce a summary of clause contents, keep reading until you can characterise the contract's commercial logic.

### Step 5: Clause-by-Clause Analysis

Now evaluate the contract against the playbook. Your epistemic mode shifts here: you have stable reference points (the playbook's standard positions) and you are applying them to what you found. This is where classification and criteria are appropriate.

For each material area in the contract, assess how the contract's position compares to the playbook's standard position.

**Identifying material areas**: The clause categories below are a reference for systematic review. Cover what's material in this contract — not every category. Some contracts will have material provisions that fall outside these categories; include those. Some categories won't be material for a given contract; note them briefly or skip them.

| Clause Category | Guiding Question |
|----------------|-----------------|
| **Limitation of Liability** | How is risk capped and distributed? Are there structural asymmetries in who bears residual risk? |
| **Indemnification** | What obligations does each party take on to protect the other, and how are those obligations bounded? |
| **IP Ownership** | Does the allocation of IP rights match the parties' actual contributions and commercial intent? |
| **Data Protection** | Are the regulatory obligations around personal data addressed proportionately to the sensitivity and volume of data involved? |
| **Confidentiality** | Does the scope, term, and structure protect what each party actually needs protected? |
| **Representations & Warranties** | What does each party warrant, and where is the exposure if a warranty fails? |
| **Term & Termination** | How locked-in is each party, and what happens when the relationship ends? Does the exit structure create asymmetric dependency? |
| **Governing Law & Dispute Resolution** | Does the mechanism create structural advantages for one party? Is it proportionate to the likely nature and size of disputes? |
| **Insurance** | Are coverage requirements proportionate to the risks being allocated elsewhere in the contract? |
| **Assignment** | How do the consent requirements and change-of-control provisions interact with the parties' likely business trajectories? |
| **Force Majeure** | Is the scope and the notification structure appropriate for this type of deal? |
| **Payment Terms** | Are the commercial terms — fees, timing, escalation — consistent with the deal's commercial structure? |

For each clause area, these elements provide a systematic review reference:

##### Limitation of Liability

- Cap amount (fixed dollar amount, multiple of fees, or uncapped)
- Whether the cap is mutual or applies differently to each party
- Carveouts from the cap (what liabilities are uncapped)
- Whether consequential, indirect, special, or punitive damages are excluded
- Whether the exclusion is mutual
- Carveouts from the consequential damages exclusion
- Whether the cap applies per-claim, per-year, or aggregate

##### Indemnification

- Whether indemnification is mutual or unilateral
- Scope: what triggers the indemnification obligation (IP infringement, data breach, bodily injury, breach of reps and warranties)
- Whether indemnification is capped (often subject to the overall liability cap, or sometimes uncapped)
- Procedure: notice requirements, right to control defense, right to settle
- Whether the indemnitee must mitigate
- Relationship between indemnification and the limitation of liability clause

##### Intellectual Property

- Ownership of pre-existing IP (each party should retain their own)
- Ownership of IP developed during the engagement
- Work-for-hire provisions and their scope
- License grants: scope, exclusivity, territory, sublicensing rights
- Open source considerations
- Feedback clauses (grants on suggestions or improvements)

##### Data Protection

- Whether a Data Processing Agreement/Addendum (DPA) is required
- Data controller vs. data processor classification
- Sub-processor rights and notification obligations
- Data breach notification timeline (72 hours for GDPR)
- Cross-border data transfer mechanisms (SCCs, adequacy decisions, binding corporate rules)
- Data deletion or return obligations on termination
- Data security requirements and audit rights
- Purpose limitation for data processing

##### Term and Termination

- Initial term and renewal terms
- Auto-renewal provisions and notice periods
- Termination for convenience: available? notice period? early termination fees?
- Termination for cause: cure period? what constitutes cause?
- Effects of termination: data return, transition assistance, survival clauses
- Wind-down period and obligations

##### Governing Law and Dispute Resolution

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

For each YELLOW and RED deviation, generate specific alternative language.

Before drafting, recall the business context from Step 2 — the relationship type, deal size, strategic importance, and deadline. Two identical deviations in different deal contexts may warrant different redline language. A first draft for a strategic partner reads differently than a pushback to a commodity vendor. Standard market position is a reference point, not a prescription.

For each redline:
- **Be specific**: Provide exact language ready to insert, not guidance.
- **Be calibrated to the relationship**: Match tone and aggressiveness to the deal dynamics.
- **Explain the rationale**: Include a brief, professional rationale suitable for sharing with the counterparty's counsel.
- **Provide fallback positions**: For YELLOW items, include a fallback if the primary ask is rejected — a genuine alternative position, not a watered-down version of the same ask.

For each redline, include the clause reference, current language (exact quote), proposed alternative language, rationale, priority, and fallback position where applicable.

### Step 8: Business Impact Summary

Provide a summary covering:

- **Overall risk assessment**: High-level view of the contract's risk profile.
- **Key findings**: The most important issues to address — as many or as few as the contract warrants. A simple, well-drafted contract might yield one critical finding; a heavily one-sided contract might yield several. Let the contract's complexity determine the count.
- **Negotiation strategy**: Shift your posture here. The prior steps were evaluative — judging provisions against standards. Strategy is a different kind of thinking. Set aside the deviation framework and think about this deal as a negotiation between two parties with interests, constraints, and leverage dynamics. Model the counterparty: what do they need, what are they protecting, where is their room to move? What does the pattern of their drafting choices reveal about their priorities? Then reason about sequencing — which items to lead with, what to hold back, what to concede strategically to create room for movement on what matters most. This section should read as counsel who has thought about the other side of the table, not as a reorganised list of deviations.
- **Timeline considerations**: Any urgency factors affecting the negotiation approach.

#### Negotiation Priority

Organise your recommendations by strategic importance for this deal — not mechanically by classification tier. A technically moderate deviation may be strategically critical because it touches the user's stated focus areas. A severe deviation may be concedable because the relationship or deal dynamics make the risk acceptable.

**Must-Haves**: Issues where the organization cannot proceed without resolution. Lead with these.

**Should-Haves**: Issues that materially affect risk but have negotiation room.

**Nice-to-Haves**: Issues that improve the position but can be conceded strategically to secure wins on higher priorities.

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

## Working Theory

[Your characterisation from the Step 4 transition: what the contract is
trying to accomplish, how risk flows between the parties, and what stands
out as structurally significant. Write it as understanding, not as a
summary. This grounds everything that follows.]

## Key Findings

[The most important issues — as many or as few as the contract warrants.
Spend depth here proportional to significance. A critical IP ownership
issue warrants a full paragraph; a minor notice period deviation warrants
a line.]

## Clause-by-Clause Analysis

For each material clause, cover: what the contract says, how it deviates
from the playbook, and why it matters. Spend depth proportional to
materiality — a minor acceptable variation warrants a line, a critical
deviation warrants a full analysis with redline.

Flag each clause as GREEN, YELLOW, or RED. Include redline suggestions
inline for YELLOW and RED clauses.

Clauses that are acceptable and unremarkable can be grouped briefly (e.g.,
"Confidentiality, Force Majeure, and Assignment clauses are standard and
acceptable"). Don't give every clause the same structural weight.

## Negotiation Strategy

[Written from a strategic posture, not an evaluative one. Set aside the
deviation framework and think about this deal: what does each party need,
what are they protecting, where is there room to move? Model the
counterparty's constraints and likely priorities based on their drafting
choices. Reason about sequencing — which asks to lead with, what to hold
back, what to concede strategically to secure movement on what matters.
This section should read as counsel who has thought about the other side
of the table, not as a reorganised list of redlines.]

## Next Steps

[Specific actions to take]
```

## Notes

- If the contract is in a language other than English, note this and ask if the user wants a translation or review in the original language
- For very long contracts (50+ pages), offer to focus on the most material sections first and then do a complete review
- Always remind the user that this analysis should be reviewed by qualified legal counsel before being relied upon for legal decisions
