# A6 SecOps Incident Response — Tier 3 Pipeline (Handoff Spec)

This pipeline is for **post-incident analysis** (security incident postmortems / after-action reviews). It cleanly separates incompatible cognitive modes to avoid: (a) evaluation pre-filtering investigation, (b) solution-shaped investigation, (c) premature narrative lock-in, and (d) **5-Whys anchoring**.

## Execution order (sequential)

| Seq | File base name | Stage | Primary mode(s) | Output artifact (handoff block) |
|---:|---|---|---|---|
| 01 | `01-evidence-reconstruction` | Evidence reconstruction (timeline + evidence ledger) | investigation + light structuring | `EVIDENCE_RECONSTRUCTION` |
| 02 | `02-causal-analysis` | Causal analysis (branching causal model) | deep investigation + synthesis (model-building) | `CAUSAL_ANALYSIS` |
| 03 | `03-contributing-factors` | Contributing factors & systemic issues | structuring + investigation (systems lens) | `CONTRIBUTING_FACTORS` |
| 04 | `04-learning-actions` | Organisational learning & actions | reframing + generation (planning) | `LEARNING_ACTIONS` |

**Constraint:** Stage prompts exist in **two formats** per stage:
- `NN-<stage>.md` (Claude Code subagent format)
- `NN-<stage>.agent.md` (Copilot agent format)

## Handoff rules (critical)

1. **Pass only the final handoff block** (`yaml`) to the next stage.
   - Do **not** pass exploratory prose, brainstorms, or “thinking out loud”.
2. **Do not add evaluation or actions upstream.**
   - Stages 01–03 must not contain action items, owners, priorities, or “what went well/poorly”.
3. **No 5 Whys.**
   - Causality must be represented at **natural depth** with **branching** where warranted.
4. **Uncertainty is allowed and preferred over invention.**
   - Use `unknown`, `not provided`, `needs confirmation`, and cite missing evidence.

## Artifact schemas (what crosses between stages)

### 01 → 02: `EVIDENCE_RECONSTRUCTION`
The goal is a **fact-grounded reconstruction** with explicit provenance.

```yaml
EVIDENCE_RECONSTRUCTION:
  incident:
    title: <string | unknown>
    incident_id: <string | unknown>
    timezone: <IANA tz | unknown>
    date_range:
      start: <timestamp | unknown>
      end: <timestamp | unknown>
  sources_used:
    - source_id: <string>
      source_type: <alert | log | ticket | chat | email | doc | other>
      reference: <url/path/snippet>
  timeline_events:
    - event_id: E01
      time: <timestamp | unknown>
      system_or_surface: <string | unknown>
      observation: <what was observed; no causal language>
      evidence_refs: [S1, S3]
      confidence: <high|medium|low>
  evidence_ledger:
    - evidence_id: S1
      source_type: <...>
      reference: <...>
      excerpt_or_summary: <short>
      reliability_notes: <optional>
  gaps_and_questions:
    - gap_id: G1
      question: <what data is missing?>
      why_it_matters: <what timeline/claim it would confirm/deny>
      suggested_sources: <logs/tools/people>
```

### 02 → 03: `CAUSAL_ANALYSIS`
The goal is a **branching causal model** anchored to evidence (not to templates).

```yaml
CAUSAL_ANALYSIS:
  outcome_and_impact:
    outcome: <what bad thing happened>
    impact: <who/what was affected; unknown allowed>
  causal_map:
    notes: <1–3 sentences; optional>
    paths:
      - path_id: P1
        description: <plain language>
        steps:
          - node_id: N1
            claim: <causal claim>
            supported_by: [E01, S2]
            confidence: <high|medium|low>
            gaps: [G2]
        preconditions: [<factor refs or event ids>]
        failed_or_missing_controls: [<control statements; evidence-linked>]
  alternative_hypotheses:
    - hypothesis_id: H2
      claim: <competing explanation>
      disconfirming_evidence: [<refs>]
      status: <plausible|unlikely|ruled_out|unknown>
  decision_environment:
    - moment_id: D1
      time_window: <timestamp/relative>
      decision: <what was decided>
      info_available_then: <what responders could reasonably know>
      constraints: <time pressure, tool limits, paging noise, etc>
      why_it_made_sense_then: <systems lens; no blame>
```

### 03 → 04: `CONTRIBUTING_FACTORS`
The goal is to surface **latent conditions** and **systemic enablers** (tech + org) with evidence links.

```yaml
CONTRIBUTING_FACTORS:
  factor_groups:
    - group: <Detection & Monitoring | Identity & Access | Change Mgmt | SDLC | Infra | Data | Process | Org & Incentives | Vendor | Other>
      factors:
        - factor_id: F1
          statement: <systemic condition>
          enabled_paths: [P1]
          evidence_refs: [S4, E07]
          scope: <local|team|org|ecosystem>
          confidence: <high|medium|low>
          notes: <optional>
  systemic_themes:
    - theme_id: T1
      statement: <cross-cutting pattern>
      factors: [F1, F7]
      evidence_refs: [S4]
  open_risks_or_unknowns:
    - item: <what remains uncertain but important>
      evidence_needed: <...>
```

### 04 final: `LEARNING_ACTIONS`
The goal is an **organisational learning artifact** plus an actionable plan with verification.

```yaml
LEARNING_ACTIONS:
  learning_summary:
    - learning_id: L1
      statement: <what the org should learn>
      derived_from: [T1, F1, P1]
  actions:
    - action_id: A1
      title: <action>
      type: <prevent|detect|respond|recover|govern>
      rationale: <why this action addresses the causal model>
      addresses: [F1, T1, P1]
      effort: <small|medium|large|unknown>
      priority: <high|medium|low>
      owner: <TBD>
      due: <TBD>
      verification:
        success_metric: <how we’ll know it worked>
        test_or_drill: <how to validate>
  followups_and_decisions:
    - item: <decision needed / tradeoff>
      options: [<...>]
      recommendation: <optional>
      decision_owner: <TBD>
```
