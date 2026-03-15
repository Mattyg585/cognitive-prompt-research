# Revision Notes — A2 Optimised Skill (GPT-5.3-Codex)

Source analysis: `gpt-5.3-codex/analysis/prompt-architect-analysis.md`

## Finding → Change map

### 1) Template completion dominated generation
**Finding:** Fixed structures caused box-filling behavior and repetitive outputs.

**Change implemented:** Replaced rigid slot templates with phase-based guidance and purpose-driven blog requirements. The new prompt asks for required components (headline/opening/arc/close/meta) but no fixed section counts.

**Expected effect:** Better narrative fit per brief and healthier structural variation across runs.

---

### 2) Numeric anchors reduced natural variation
**Finding:** Many ranges/limits acted as hidden targets.

**Change implemented:** Removed non-essential numeric targets from drafting phase. Preserved only hard constraints that matter at polish time (e.g., meta description length).

**Expected effect:** Output length/structure should adapt to editorial need rather than midpoint anchors.

---

### 3) Seed formulas constrained headlines/hooks
**Finding:** Formula menus biased outputs toward predictable headline shapes.

**Change implemented:** Replaced formulas with principle-based headline/hook guidance (curiosity gap, concrete value, honesty to content).

**Expected effect:** More differentiated openings and less templated phrasing.

---

### 4) Evaluation mixed with generation
**Finding:** SEO/checklist language in writing context suppressed voice and engagement.

**Change implemented:** Explicit phase boundaries: Understand → Draft → Polish. SEO and compliance checks moved to Phase 3 only.

**Expected effect:** Draft quality improves (voice, rhythm, specificity) before optimization pass.

---

### 5) Investigation was implicit and under-weighted
**Finding:** Prompt jumped too quickly into production structure.

**Change implemented:** Added explicit discovery stage with five investigation lenses (friction, cost, difference, proof, adoption).

**Expected effect:** Stronger strategic angle selection and audience-state modeling.

## What to validate during runs

1. **Variation:** Run-to-run differences in sectioning and angle should increase.
2. **Voice:** Drafts should sound less procedural and more human.
3. **Specificity:** Feature mentions should be tied to lived workflow pain, not generic claims.
4. **SEO integration quality:** Keyword placement should feel natural in final pass.