# Handoff: Build L2/L3 Pattern Analysis - Phase 2

## Context

Phase 1 is complete. We built and tested the two clustering prompts:
- `docs/prompts/production/layer2-semantic-clustering.md` - groups by inferred intent
- `docs/prompts/production/layer2-technical-clustering.md` - groups by actual controls

18 L2 observations are now in the database (10 semantic, 8 technical).

## What Exists in DB

Clear L2/L3 before testing new work:
```sql
DELETE FROM observations WHERE layer IN (2, 3);
```

Or to see what's there:
```sql
SELECT observation_type, title, ai_confidence
FROM observations
WHERE layer = 2
ORDER BY observation_type, ai_confidence DESC;
```

## Phase 2 Goal

Build and test the **Alignment Analysis Agent** prompt.

**Job:** Compare semantic clusters to technical clusters, identify misalignments where:
- Policy name suggests one intent, but controls implement something different
- Semantic cluster exists (e.g., "BYOD policies") but technical implementation is weak/missing
- Multiple policies with same technical controls but different semantic purposes (consolidation signal)

**Key inputs from Phase 1:**
1. Semantic observation: "ACME Cloud - BYOD Users Allow Any Device" in BYOD semantic cluster
2. Technical observation: Same policy is in MFA-only technical cluster
3. **Alignment finding:** BYOD intent, MFA-only implementation = misalignment signal

## Read First

- `docs/architecture/pattern-analysis-redesign.md` - full design (updated with Phase 1 results)
- `docs/design-principles.md` - prompt engineering principles
- The two clustering prompts (to understand their output structure)

## Key Constraints

- Prompts must be portable to Azure AI Foundry
- Write observations as L2 (or L2.5 if we want to distinguish)
- Focus on surfacing "so what" - not just "these don't match" but "this matters because..."
- Frame as conversation prep, not audit findings

## After Alignment Analysis

If time permits, also build:
- **Deep Dive Agent** - investigates specific patterns when interesting

## Don't Build Yet

- Orchestrator (wire up after all pieces work)
- Zero Trust Mapping (Phase 3)
- Path Forward Synthesis (Phase 3)
