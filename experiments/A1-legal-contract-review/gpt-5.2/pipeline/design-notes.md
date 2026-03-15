# Design Notes — A1 Tier 3 (Pipeline)

## Why this is a pipeline (vs a single prompt)
The original A1 skill fuses **investigation + evaluation + drafting + synthesis** in one context. Per the architect analysis, this creates predictable failure modes:
- **Pre-filtering** (evaluation criteria present during discovery)
- **Solution-shaped discovery** (must draft redlines while still finding issues)
- **Checklist anchoring** (dense seeded clause guidance)
- **Numeric anchoring** (fixed “Top 3” / “3–5”) 
- **Template pressure hallucination** ("exact quote" and “playbook position” slots)

This Tier 3 design separates incompatible cognitive modes into sequential stages and enforces structured handoffs so later stages can’t contaminate earlier thinking.

## Cognitive mode allocation by stage
1. **01 Intake & Basis** — Orchestration
   - Gather context; decide playbook vs generic baseline.
   - Output is a compact *Context & Basis Pack*.

2. **02 Contract Map & Issue Spotting** — Investigation + light structuring
   - Read/parse the whole contract; map structure; surface candidate issues.
   - No severities, no playbook positions, no redlines.
   - Creates an *Evidence Index* (EX ids) to prevent invented quotes later.

3. **03 Playbook Evaluation** — Evaluation (convergent)
   - Compare candidate issues (and any missing-but-material clause categories) to playbook or generic standards.
   - Assign GREEN/YELLOW/RED + escalation triggers.
   - No drafting.

4. **04 Redline Drafting** — Generation (bounded)
   - Draft insert-ready clause language, fallbacks, and external rationales *only* for issues already evaluated.
   - Quotes must come from EX references; otherwise explicitly mark `NEEDS VERIFICATION`.

5. **05 Negotiation Brief** — Synthesis / Reframing
   - Produce an executive summary, prioritized plan, and next steps.
   - Avoid fixed counts; let output scale to contract complexity.

## How the pipeline addresses the architect’s key findings
- **A/B (Investigation interleaved with evaluation/generation):** strict stage boundaries ensure discovery happens before judgment, and judgment happens before drafting.
- **C (Heavy seeding):** Stage 02 uses *lenses* (definitions, precedence, incorporation, exhibits, cross-references) rather than only a checklist; Stage 03 can still ensure minimum coverage without anchoring discovery.
- **D (Numeric anchors):** Stage 05 forbids fixed counts unless explicitly requested.
- **E (Template-driven fabrication):** Evidence Index + EX-only quoting rule; playbook assertions must be cited or labeled `GENERIC`.
- **F (Stance drift):** keep the “not legal advice” reminder once, globally; do not spam disclaimers in every section.

## Execution notes
- **Default sequential run** keeps the cognitive boundary clean.
- For very long contracts, Stage 02 can be run in multiple passes by section/exhibit and merged into one Contract Map & Evidence Pack before evaluation.

## What to watch for during testing
- Do Stage 02 outputs include non-obvious architecture (precedence, incorporation, exhibits)?
- Do Stage 03 findings vary in count and severity with contract complexity (no “always 3” pattern)?
- Are all “Current language” quotes in Stage 04 traceable to EX excerpts?
- When no playbook is present, are positions clearly labeled `GENERIC`?
