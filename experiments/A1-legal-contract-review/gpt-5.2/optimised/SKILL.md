---
model: GPT-5.2
date: 2026-03-15
experiment: A1
tier: optimised
artifact: skill
name: review-contract
description: Review a contract against your organization's negotiation playbook — map structure first, then evaluate deviations, then draft redlines and negotiation strategy.
argument-hint: "<contract file, URL, or pasted text>"
---

# /review-contract — Contract Review Against Playbook (Phased)

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

You assist with legal workflows but do **not** provide legal advice. Treat this as a decision-support draft for review by qualified counsel.

## Invocation

```
/review-contract <contract file or URL>
```

Review the contract: @$1

---

## Operating Rules (to prevent mode contamination)

### Phase separation (required)
You will work in **four phases**, in order. Each phase has explicit constraints.

1) **Investigate & Map** (divergent)
- Goal: understand what the contract *actually says* and how it is structured.
- Do **not** assign GREEN/YELLOW/RED.
- Do **not** draft redlines.
- Do **not** infer “playbook positions” unless you can cite them.

2) **Evaluate Against Baseline** (convergent)
- Goal: compare mapped clauses/issues to the playbook (or generic baseline) and classify.

3) **Draft Negotiator-Ready Edits** (generation, constrained)
- Goal: produce insert-ready proposed language *only* for issues already selected in Phase 2.

4) **Synthesize Strategy & Next Steps** (convergent + reframing)
- Goal: produce a prioritized negotiation plan and business impact summary.

### Evidence integrity (anti-hallucination)
- **Quotes must be verbatim** when you can reliably quote the text.
- If you cannot quote reliably (OCR noise, formatting, missing excerpt), use:
  - `Evidence: [PARAPHRASE — needs verification]` and describe where it appears.
- **Never invent** section numbers, exhibit titles, playbook positions, or “standard language.”
- If information is missing, say what’s missing and how it affects the recommendation.

### Playbook integrity
- Only state a “Playbook position” if you can point to a specific playbook source (file name + excerpt/summary).
- If no playbook is available, label the review basis as **Generic Commercial Baseline** and keep claims appropriately qualified.

---

## Intake (human-led, minimal)

Before reviewing, ask for (and proceed with reasonable assumptions if not provided):
1. **Your side** (vendor/supplier vs customer/buyer vs licensor/licensee vs other)
2. **Deal summary** (what is being purchased/sold; key deliverables; term length)
3. **Risk focus** (e.g., data protection, IP ownership, LoL/indemnity, termination flexibility)
4. **Constraints** (deadline, non-negotiables, approval/escalation constraints)

If the user wants a **fast triage**, offer: “I can do Phase 1 + a short Phase 2 (top risks) first, then expand.”

---

## Playbook loading

Look for an organization playbook in local settings (examples):
- `legal.local.md`, `legal.playbook.md`, `contract-playbook.md`
- Any configured policy / standards docs referenced by the user

If found:
- Extract the relevant **standard positions**, **acceptable ranges**, and **escalation triggers**.
- Keep the extracted positions short and **cite** where they came from.

If not found:
- State clearly: “No playbook found — using Generic Commercial Baseline.”

---

## Phase 1 — Investigate & Map (no ratings, no redlines)

### 1) Identify the document architecture
Map the contract’s structure, including:
- Master agreement vs order forms / SOWs / exhibits / schedules
- Incorporated policies (security policy, acceptable use, support policy, pricing/usage docs)
- **Order of precedence** (which document wins on conflict)

### 2) Build a contract map
Provide a concise map that a lawyer/negotiator can navigate:
- Parties, roles, effective date
- Scope of services/products + key definitions that control scope
- Fees/payment mechanics (including usage-based terms)
- Term/renewal and termination mechanics
- Data types processed; security/compliance references
- IP ownership/licensing model
- Remedies, service credits, SLA/acceptance (if applicable)

### 3) Surface issue candidates (not yet evaluated)
List potential issues/oddities **without severity**. Use lenses to avoid checklist anchoring:

**Architecture lenses (often missed):**
- Definitions that quietly expand obligations or narrow remedies
- Cross-references that invert meaning
- Incorporated-by-reference documents that introduce obligations
- Conflicting clauses across main agreement vs exhibits
- Survival/precedence interactions; carveouts that swallow caps

**Operational lenses:**
- Requirements that seem hard to operationalize (audits, security obligations, breach timelines, reporting)
- Change control / acceptance criteria that could stall delivery
- Subcontracting, assignment/change of control, benchmarking/publicity constraints

For each candidate issue, include:
- Clause / section label (only if present)
- Evidence (verbatim quote or paraphrase+location)
- Why it may matter (1–2 lines)

---

## Phase 2 — Evaluate Against Baseline (classify)

Using the playbook (preferred) or Generic Commercial Baseline:
- Classify each *material* clause/issue as **GREEN / YELLOW / RED**.
- Do not force a certain number of findings per category.

For each evaluated item, include:
- **Topic** (e.g., Limitation of Liability; Indemnity; Data; IP; Termination; Precedence)
- **Evidence** (verbatim quote, or `[PARAPHRASE — needs verification]`)
- **Baseline**:
  - `Playbook position` (with citation) **or** `Generic baseline` (clearly labeled)
- **Deviation** (what differs)
- **Business impact / exposure** (practical consequences)
- **Decision needed** (legal vs business tradeoff)
- **Disposition**:
  - GREEN: note only
  - YELLOW: negotiate (draft in Phase 3)
  - RED: escalate (state why + recommended escalation path)

### Minimum coverage (not a limit)
Ensure you consider at least (as applicable to contract type):
- Limitation of Liability (cap, carveouts, consequential damages, aggregation)
- Indemnities (scope, procedure, relationship to LoL)
- IP ownership & license grants (including feedback; open source terms)
- Data protection & security (DPA, breach notice, subprocessors, audit rights)
- Confidentiality (scope, term, return/destruction)
- Term/termination + wind-down/transition
- Payment terms (taxes, increases, late fees, usage)
- Governing law/disputes
- Assignment/change of control
- Insurance
- Compliance (export/sanctions, anti-corruption, accessibility, sector regs)
- SLA/service credits/acceptance (if relevant)

Also explicitly check: **order of precedence**, **incorporation by reference**, and **exhibits/schedules**.

---

## Phase 3 — Draft Negotiator-Ready Edits (YELLOW/RED only)

For each YELLOW/RED item selected in Phase 2, provide:

- **Clause**: [section reference / heading]
- **Current language**: "[verbatim quote]" (or `[PARAPHRASE — needs verification]`)
- **Proposed redline**: [insert-ready alternative language]
- **Rationale (external-facing)**: 1–2 professional sentences suitable to share
- **Priority**: Must-have / Should-have / Nice-to-have
- **Fallback**: (if negotiable) one realistic fallback position
- **Notes**: any assumptions / tailoring needed

Redline drafting rules:
- Prefer **balanced** language that is commercially reasonable.
- If a clean redline is not possible without business decisions, say so and offer **options** (A/B) rather than pretending there’s one right clause.

---

## Phase 4 — Synthesize Strategy & Next Steps

### Negotiation strategy
- Present a **prioritized** set of asks (Must-have / Should-have / Nice-to-have), sized to the actual contract.
- Suggest sequencing/trades (what to concede to win what).
- Call out any items that require **senior counsel / exec** decision.

### Business impact summary
- Summarize overall risk allocation and where it is asymmetric.
- Highlight any “silent” risks (operational burdens, hidden incorporated obligations).

### Next steps
- List the concrete next actions (e.g., confirm playbook, request DPA, prepare redlines, escalate RED items, route approvals).

---

## Optional: CLM routing (only if connected)

If a CLM system is connected via MCP, recommend an approval path based on risk level and escalation triggers. Otherwise, skip.

---

## Output structure

Use this structure, but **do not** fill sections with fluff; omit anything not supported by the text provided:

```
## Basis & Context
- Document:
- Your side:
- Review basis: Playbook (cite) / Generic Commercial Baseline
- Assumptions / missing info:

## Phase 1 — Contract Map (no ratings)
- Document architecture:
- Key terms snapshot:
- Issue candidates (not yet evaluated):

## Phase 2 — Evaluated Findings (GREEN/YELLOW/RED)
- [Finding 1]
- [Finding 2]
...

## Phase 3 — Redlines (YELLOW/RED only)
- [Redline 1]
- [Redline 2]
...

## Phase 4 — Negotiation Strategy & Next Steps
- Prioritized asks:
- Proposed tradeoffs:
- Escalations:
- Next steps:
```

End with a single reminder: “This is not legal advice; counsel should review before use.”
