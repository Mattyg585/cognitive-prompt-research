# Tier 2 Revision Notes — v3

Generated from `prompt-architect-analysis-v3.md`.

## What the v3 Analysis Added

The v3 analysis sharpened two mechanisms that the v1 and v2 revisions addressed incompletely, and identified one that neither prior revision addressed:

**1. Anticipatory narrowing vs. attentional residue** — v1/v2 added a scope boundary ("you are reading to understand, not to evaluate") and a transition gate (state your working theory before proceeding). The v3 analysis identifies a more precise problem: the evaluation framework creates anticipatory awareness before the model reads the contract at all. The scope boundary addresses attentional residue during reading; it cannot prevent the decision architecture from having already shifted to criterion-referenced before reading begins. The v3 fix for this in Tier 2 is to restructure Step 4 so it operates as an epistemic posture — framing what kind of understanding to build — rather than as a scope boundary on evaluation. The lens questions replace the clause category table entirely in Step 4.

**2. The clause category table as a navigation frame** — v1/v2 kept the 12-category table in Step 5 (evaluation). v3 notes that the table in the original served double duty: it anchored both what to look for during investigation AND how to structure the evaluation. In v3 Tier 2, the table is replaced in Step 5 with a guiding-question format — each category paired with a lens rather than bullet-point keys. The detailed element checklists (formerly "Key elements to review") are retained for convergent evaluation work but moved cleanly under the classification step, where seeding is appropriate.

**3. Redline format as investigation + generation fusion** — neither v1 nor v2 addressed this. The v3 analysis identifies that the full redline output format (current language / proposed redline / rationale / priority / fallback) is present in context during the investigation phase. This shapes what gets noticed: findings without obvious redlines get deprioritised. The v3 fix: the redline generation step retains its format, but the format is no longer foreshadowed in the pre-investigation context. In the restructured prompt, Step 7 introduces the format at the point of use; it is not present in Step 4's context.

**4. Negotiation priority framework present during investigation** — v2 did not move the Tier 1/Tier 2/Tier 3 framework. v3 recommended moving it to the synthesis stage. In Tier 2 this is partly achievable: the detailed tier definitions remain (they're needed for classification), but the Step 8 strategy section now explicitly signals an epistemic posture shift — "set aside the deviation framework" — rather than presenting the tiers as a structural container for strategy.

---

## Finding → Change Mapping

| Architect Finding (v3) | What Changed in SKILL-v3.md |
|---|---|
| **Investigation + Evaluation fusion — decision architecture switch from recognition-primed to criterion-referenced** | Step 4 restructured as an epistemic posture ("you are reading to understand, not to assess") rather than a scope note. The 12-category table and all clause-level checklists are absent from Step 4. The investigative lens questions ("what's unusual?", "where does the contract's own logic create tensions?") are foregrounded. Evaluation criteria appear only in Steps 5–6. |
| **Clause coverage table and "Key elements to review" as prescribed threads** | In Step 4 (investigation): both removed entirely. In Step 5 (evaluation): the 12-category table is restructured with a "Guiding Question" column replacing the "Key Review Points" column — each category is now a lens, not a checklist target. The detailed element lists are retained under each clause section as systematic review aids for the convergent evaluation phase, where seeds are appropriate. |
| **"Common issues" seeds defining ceiling of discovery** | Removed in v1; confirmed absent in v3. Not reintroduced. |
| **Declared sequential architecture that doesn't match actual architecture** | Partially addressed. In Tier 2, the evaluation framework is still in context before reading. The v3 revision makes the declared architecture more honest: Step 4 is framed as building understanding; Steps 5–6 are explicitly framed as "now evaluate." The transition gate (state your working theory before proceeding to Step 5) is retained from v2. This is the residual gap that pipeline reconstruction fully addresses — acknowledged in the design notes. |
| **Redline format template present during investigation (investigation + generation fusion)** | The detailed redline output format is introduced in Step 7 at the point of use. It is not present in Step 4. Step 7 includes the deal-context reminder from v2 (relationship, strategic importance, deadline shape the drafting). |
| **Negotiation priority framework present during investigation** | The three-tier priority structure remains for classification in Step 6, but is no longer the structural container for Step 8's strategy. Step 8 now opens with an explicit posture shift ("set aside the deviation framework") before presenting the priority tiers as organisational suggestions for the redline list, not as a strategy template. |
| **"Top 3-5" numeric anchor** | Removed in v1; retained absent in v3. The Key Findings section guidance now says "as many or as few as the contract warrants" with explicit permission for the count to vary with complexity. |
| **Output template with fixed structural weight per clause** | The output format now instructs depth proportional to materiality and gives explicit permission to group unremarkable clauses (retained from v2). |
| **Synthesis contaminated by evaluative posture** | Step 8 strategy framing strengthened: explicit instruction to shift posture, model the counterparty, reason about sequencing and leverage. "This section should read as counsel who has thought about the other side of the table, not as a reorganised list of deviations." The Output Format block for Negotiation Strategy mirrors this. |
| **Epistemic stance not set** | Step 4 now opens with an explicit epistemic stance statement: "You are not yet evaluating it." The step is structured around the kind of understanding to build, not the procedure to follow. The transition gate forces the mental model to be complete before evaluation begins. |

---

## What Wasn't Changed

- Steps 1–3 (Accept, Gather Context, Load Playbook) — architect flagged these as clean across all three analyses
- CLM routing (Step 9) — practical, no cognitive issues
- Legal disclaimer — preserved
- The GREEN/YELLOW/RED classification definitions — legitimate convergent machinery; the issue was their presence during investigation, not their existence
- The detailed element checklists under each clause section — moved from investigation context to evaluation context, where seeds are appropriate for convergent work

---

## The Residual Gap

The v3 analysis is precise about what Tier 2 cannot fix: anticipatory narrowing created by the evaluation framework being in context before reading. The scope boundary and epistemic stance framing in Step 4 instruct the model to hold the playbook in the background during reading. But the model has already processed the playbook by the time it reads those instructions. The decision architecture has already shifted.

The v3 revision makes the best available use of Tier 2 mechanisms — epistemic stance, scope boundaries, transition gate, seed-to-lens conversion, anchor removal. It should produce meaningfully better output than v1 or v2. The gap between v3 Tier 2 and Tier 3 is precisely what the experiment tests: does the structural isolation in the pipeline produce findings that the improved monolithic prompt cannot?

---

## What to Watch for When Testing

- **Out-of-category findings**: Test with a contract containing unusual provisions (AI-generated content rights, novel regulatory constructions, unusual IP arrangements). The v3 revision should surface these better than v2 because the investigative frame in Step 4 is stronger. If all findings still map neatly to the 12 standard categories, the playbook is filtering during reading despite the framing.
- **Clause interaction findings**: Does the output surface findings that arise from the interaction between two clauses — findings that would not appear from reading each clause in isolation? These are the recognition-primed discoveries the investigation phase is supposed to enable.
- **Working theory quality**: Does the Step 4 transition produce a genuine characterisation of the contract's commercial logic, or a clause inventory in disguise? The "Working Theory" section in the output format makes this visible.
- **Count variation**: Run on a simple and a complex contract. If Key Findings consistently shows a similar count regardless of input complexity, the model is still anchoring to an implicit target.
- **Negotiation strategy register**: Does the strategy model the counterparty (their needs, constraints, BATNA, drafting-revealed priorities) or restate the deviation list in strategy language?
- **Redline calibration**: Are redlines shaped by the specific deal context (relationship, strategic importance, deadline) or generic market-standard boilerplate? The v3 revision positions deal-context awareness at the point of drafting rather than as a general note.
