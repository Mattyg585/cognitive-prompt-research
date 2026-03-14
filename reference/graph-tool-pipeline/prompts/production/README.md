# Production Prompts

**Last Updated**: 2026-02-06

---

## Current Prompt Inventory

### Analysis (Layer 1)

| Prompt | Purpose | Status |
|--------|---------|--------|
| `layer1-per-policy-analysis.md` | Per-policy analysis — infer intent, check implementation, detect patterns | Production. 198 observations generated. |

Layer 1 is the foundation. Observations are **anchors** — fixed reference points that stories and investigation tools drill down into. Run once per policy set, re-run when policies change.

### Story Grouping (Layer 2)

| Prompt | Purpose | Status |
|--------|---------|--------|
| `layer2-story-grouping.md` | Group policies into framework-driven archetypes + custom stories | Production. Initial grouping done, consultant adjusts. |

This is the **primary L2 prompt**. Stories are persistent, human-editable groupings of policies by security intent. Framework-driven (Zero Trust archetypes), with an Unknown bucket and consultant-created custom stories. See `docs/architecture/layer2-stories.md` for the full design.

### Framework Assessment (Layer 3)

| Prompt | Purpose | Status |
|--------|---------|--------|
| `layer3-framework-assessment.md` | Pillar-based ZT maturity assessment (CISA model) | Production. Runs after grouping, before investigation. |

Assesses per **framework pillar** (Identity, Devices, Networks, Applications, Data) not per story. Produces ~6 entries with maturity tier assessments and specific handoffs for the investigator. Framework source is parameterized — Zero Trust (CISA) by default, other frameworks (ASD Blueprint, CIS) swappable.

### Investigation (Layer 2)

| Prompt | Purpose | Status |
|--------|---------|--------|
| `layer2-story-investigator.md` | Deep investigation of the policy landscape, filed into stories | Production. Validated — 19 entries at 64% context. |
| `layer2-landscape-reviewer.md` | Quality gate + landscape synthesis + handover summary | Production. Validated — 6 entries including handover. |

The **investigator** follows threads across the estate, files findings into stories with headline convention (value-signaling topics, "so what" first sentence in every `found` field). The **landscape reviewer** runs last — silent QA cleanup, visible thematic breadcrumbs, and a handover summary that briefs the consultant in 30 seconds.

### Legacy Investigation Tools (Archived)

Moved to `archive/`. Superseded by the story investigator pipeline above.

### Triage & Reporting

| Prompt | Purpose | Status |
|--------|---------|--------|
| `triage-assistant.md` | Interactive review of observations via web app + Claude Code | Production. Powers the /triage workflow. |
| `strategic-assistant.md` | Executive framing — effort, roadmap, licensing implications | Production. Interactive thinking partner, not auto-generator. |
| `report-writer-assistant.md` | Customer-facing report generation | Production. |
| `flesh-out-assistant.md` | Expand shorthand triage notes into full observations | Production. |

### Policy Lifecycle

| Prompt | Purpose | Status |
|--------|---------|--------|
| `policy-generator.md` | Generate policy JSON from natural language | Production. |
| `policy-plan.md` | Show diff/plan before deploying policy changes | Production. |
| `policy-orchestrator.md` | End-to-end policy lifecycle coordination | Production. |
| `policy-lifecycle-orchestrator.md` | Full lifecycle: generate, validate, plan, deploy, drift | Production. |

---

## Workflow

```
ANALYZE → GROUP → ASSESS → INVESTIGATE → REVIEW → TRIAGE → STRATEGIC → REPORT → ACTION
  L1        L2      L3       Investigator   Landscape  Web UI    Exec      Output   GitOps
```

1. **Analyze** — Run `layer1-per-policy-analysis.md` on all policies
2. **Group** — Run `layer2-story-grouping.md` to create story archetypes
3. **Assess** — Run `layer3-framework-assessment.md` for pillar-based maturity assessment
4. **Investigate** — Run `layer2-story-investigator.md` for deep investigation filed into stories
5. **Review** — Run `layer2-landscape-reviewer.md` for quality gate, synthesis, and handover summary
6. **Triage** — Use web UI (/triage, /stories) + `triage-assistant.md` to review
7. **Strategic** — Use `strategic-assistant.md` for executive framing
8. **Report** — Use `report-writer-assistant.md` for deliverable
9. **Action** — Use policy lifecycle prompts to generate fixes

Steps 3-5 each run in a **separate AI session** (fresh context per agent). Each produces `investigation_log_entries` viewable at `/stories`.

---

## Archived Prompts

In `archive/`:

| Prompt | Why Archived |
|--------|-------------|
| `pattern-orchestrator.md` | Orchestrated the L2/L3 analytical pipeline. Superseded by story grouping model (Feb 2026). |
| `layer3-zero-trust-mapping.md` | Per-story ZT mapping. Superseded by pillar-based `layer3-framework-assessment.md` (Feb 2026). |
| `layer2-semantic-clustering.md` | Group by naming/intent. Superseded by story grouping + investigator pipeline (Feb 2026). |
| `layer2-technical-clustering.md` | Group by actual controls. Superseded by story grouping + investigator pipeline (Feb 2026). |
| `layer2-alignment-analysis.md` | Compare semantic vs technical. Superseded by story investigator (Feb 2026). |
| `layer2-deep-dive.md` | Deep investigation of patterns. Superseded by story investigator (Feb 2026). |
| `layer3-investigation-summary.md` | Generated investigation summaries from L2/L3 observations. Superseded by story investigation logs. |
| `layer3-modular-pivot/` | Earlier L3 modular approach. |
| `training-artifacts/` | Training/experiment artifacts. |
| `validation-loop/` | Validation loop experiments. |

In `docs/archive/`:

| Prompt | Why Archived |
|--------|-------------|
| `layer2a-pattern-scanner.md` | Original L2 — aggregated patterns without "so what". |
| `layer2b-pattern-investigator.md` | Original L2 investigation. |
| `layer3a-framework-scanner.md` | Original L3 framework scanning. |
| `layer3b-pattern-investigator.md` | Original L3 investigation. |
| `layer3c-gap-checker.md` | Original L3 gap checking. |
| `layer4-handoff-synthesis.md` | Replaced by triage/strategic/report workflow. |

---

## Key Design Principles

These are hard-won from months of iteration. See `docs/design-principles.md` for the full set.

- **Intelligence bootstrapping** — observations are conversation preparation, not audit findings
- **Trust autonomous reasoning** — explain the objective, don't prescribe steps
- **No numeric anchors** — "3-5 observations" creates anchor bias; "trust your judgment" creates natural variation
- **Don't trigger catastrophizing** — avoid priority/severity language without customer context
- **Prompts are portable** — must work on Azure AI Foundry, not just Claude Code

---

## References

- `docs/architecture/layer2-stories.md` — L2 story/archetype design (authoritative)
- `docs/architecture/pattern-analysis-redesign.md` — Previous L2/L3 analytical approach (superseded, retained as reference)
- `docs/design-principles.md` — Prompt engineering learnings
- `docs/learnings/triage-workflow.md` — Full workflow model
- `.claude/MISSION.md` — Current goals and success criteria
