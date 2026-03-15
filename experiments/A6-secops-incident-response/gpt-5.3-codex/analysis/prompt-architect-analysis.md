---
model: GPT-5.3-Codex (gpt-5.3-codex)
date: 2026-03-15
experiment: A6
phase: step-1-analysis
---

# Prompt Architect Analysis — A6 SecOps Incident Response

Source prompt analysed: `experiments/A6-secops-incident-response/original/SKILL.md`

## 1) What thinking types the prompt requires

The prompt is a single skill that spans three user modes (`new`, `update`, `postmortem`) but keeps all phase guidance and templates in one context.

In postmortem mode specifically, it combines:

- **Investigation + structuring** (timeline reconstruction)
- **Deep causal investigation** (root cause)
- **Convergent evaluation** (what went well / poorly)
- **Constrained causal template filling** (5 Whys)
- **Generative planning** (action items with owner/priority/due date)
- **Synthesis/reframing** (lessons learned)

This is a high-density cognitive blend. It can produce competent output, but the design strongly favors template completion over discovery.

## 2) Where modes interfere (with mechanism)

### A. 5 Whys imposes both numeric and structural anchors (High)

Prompt evidence:

- `### 5 Whys`
- `1. Why did [symptom]? ... 5. Why did [cause 4]? ...`

Mechanism:

- Numeric anchor: pushes toward exactly five steps regardless of natural depth.
- Structural anchor: pushes toward one linear chain when incidents are often branching/converging.

Likely effect: causal analysis becomes “fit to five” rather than “follow evidence.”

### B. Investigation is contaminated by evaluation and generation (High)

Prompt evidence (all in one output template): Timeline, Root Cause, 5 Whys, What Went Well, What Went Poorly, Action Items, Lessons Learned.

Mechanism:

- Evaluation language in context pre-filters causal exploration toward blame-adjacent or easily judged items.
- Action-item generation pressure nudges causes toward neat, fixable statements.

Likely effect: deeper systemic findings are softened in favor of “cause → ticket” compliance structure.

### C. Cross-mode template residue (Moderate)

Prompt evidence:

- Status update and postmortem templates are both present irrespective of mode execution.

Mechanism:

- Operational reporting posture (“what’s happening now”) remains in context while reflective postmortem is being written.

Likely effect: postmortem reads like an incident report plus checklist, not an organizational learning artifact.

### D. Blameless instruction can be misread as “avoid human factors” (Moderate)

Prompt evidence:

- `Postmortems are blameless — Focus on systems and processes, not individuals.`

Mechanism:

- Good cultural intent, but can suppress analysis of decision environment (“what was known then,” ambiguity, time pressure, tooling affordances).

Likely effect: postmortem omits how normal human behavior interacted with brittle system design.

## 3) Diagnostic signals to look for in output

1. **Linearity signal**: root cause reads as a tidy 5-step chain despite multiple independent control failures.
2. **Actionability bias**: causes are phrased mainly as things with immediate tickets; architecture/cognition issues are underweighted.
3. **Template echo**: sections are complete but similar in depth regardless of section importance.
4. **Hindsight bias**: limited “what was known at the time” framing.
5. **Report-vs-learning signal**: document is operationally correct but yields few reusable organizational principles.

## 4) Recommended interventions

### Tier 2 (single-prompt optimisation)

1. Replace fixed 5 Whys with open causal analysis (“trace to natural depth; branch where causes branch”).
2. Add mode boundary text so postmortem mode ignores status-update framing.
3. Reframe blamelessness to include human factors through a systems lens.
4. Keep template sections but relax rigid expectations and avoid numeric anchors.
5. Add “What was known” context in timeline to reduce hindsight distortion.

Trade-off: better depth with low operational overhead, but incompatible modes still coexist in one context.

### Tier 3 (pipeline reconstruction)

Use five scoped agents:

1. Timeline Reconstructor (investigation + structuring)
2. Causal Analyst (deep causal inquiry)
3. Response Evaluator (evaluation only)
4. Action Item Generator (intervention design)
5. Postmortem Synthesiser (composition/synthesis)

Key handoff rule: structured findings cross boundaries; exploratory reasoning residue is dropped.

Trade-off: more orchestration/time, but strongest protection against mode interference.

## 5) Expected pattern across tiers

- **Baseline**: solid, compliant postmortem; likely linear 5-Whys framing and checklist-heavy lessons.
- **Optimised**: stronger causal depth and better blameless framing, but still some one-pass contamination.
- **Pipeline**: best chance of producing organizational-learning quality (not just incident reporting quality), especially around structural detection gaps and control-design failure patterns.
