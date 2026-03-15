---
model: GPT-5.2
date: 2026-03-15
experiment: A1
artifact: blind-evaluation
---

# Blind evaluation — A1 (Legal contract review)

## Method (A1 rule)
- **Set 1 (baseline)**: scored dimensions **1, 2, 4, 5** on the **median-quality run**; scored **3 Natural Variation** across all baseline runs.
  - Median run used for dims 1/2/4/5: **baseline run-2**.
- **Set 2 (optimised)**: scored dimensions **1, 2, 4, 5** on the **median-quality run**; scored **3 Natural Variation** across all optimised runs.
  - Median run used for dims 1/2/4/5: **optimised run-2**.
- **Set 3 (pipeline finals)**: scored **each** final negotiation brief (runs 1–3) on dims **1, 2, 4, 5** and took the **median score** per dimension; scored **3 Natural Variation** across all pipeline runs.

Rubric dimensions: **Depth, Specificity, Natural Variation, Completeness, Audience Awareness**.
Domain-specific dimension for A1: **Risk Identification Accuracy** (including cross-clause interactions).

---

## Set 1 — Scores (baseline; median run = run-2)

### 1) Depth — **3/5**
Covers the expected issues for a SaaS vendor paper (AI/ML training rights, missing cap variables, DPA dependency, suspension, deletion) and provides sensible negotiation posture. It rarely goes beyond the obvious into second-order implications (e.g., how the warranty disclaimer interacts with security posture, or how incorporated documents can shift obligations) compared to the stronger sets.

### 2) Specificity — **4/5**
Grounded in the actual text with frequent clause references (e.g., §§1.6, 3.1, 5.5(b), 7.1, 8, 9, 12.8, 13.1) and concrete redline language. Most recommendations are traceable to specific provisions rather than generic “SaaS contract” advice.

### 3) Natural Variation (across runs 1–3) — **3/5**
Runs share a very similar top-level structure (summary → key findings → clause-by-clause → negotiation strategy), but there is some meaningful variation in emphasis and issue count (e.g., one run surfaces insurance and force majeure more explicitly). Variation is present, but the overall approach feels fairly templated.

### 4) Completeness — **3/5**
Hits major hot spots, but some common “gaps-and-incorporation” risks are not consistently elevated in the median run (notably the incorporated Documentation/Use Limitations and the operational procurement mechanics that flow from that). The coverage is adequate but not fully comprehensive given how many terms are explicitly variable or externalized.

### 5) Audience Awareness — **3/5**
Register is appropriate for a customer-side legal/procurement workflow and includes a usable prioritization and next steps. It’s less explicitly “brief-ready” for stakeholder escalation than the best sets (e.g., fewer crisp bundles/trades and dependency framing).

### [Legal] Risk Identification Accuracy — **4/5**
Correctly flags the genuinely high-risk clauses (AI/ML training on Customer Content; DPA gating; missing cap/definitions; unclear indemnity scope; suspension; deletion) and recognizes a key interaction (ML rights surviving termination). Cross-section interactions are noted, but not as systematically as the pipeline’s dependency mapping.

---

## Set 2 — Scores (optimised; median run = run-2)

### 1) Depth — **4/5**
Consistently goes beyond surface findings by mapping the contract architecture (missing cover page/variables, referenced documents), then evaluating and redlining. It also surfaces several non-obvious second-order risks (e.g., incorporation-by-reference / moving-target obligations; survival of ML rights; order-of-precedence gaps) and frames concrete decision points.

### 2) Specificity — **4/5**
Strong grounding with clause-level evidence, plus “decision needed” prompts that are tied to identified text gaps (caps/definitions; DPA existence; prohibited data scope). Some proposed redlines necessarily become structural placeholders because key definitions/variables are missing, but the output still stays anchored to the excerpt.

### 3) Natural Variation (across runs 1–3) — **2/5**
Across runs, the structure is highly consistent (“Basis/Context → Contract Map → Evaluated Findings → Redlines → Negotiation Strategy”), with mostly phrasing/ordering changes rather than meaningful shifts in analysis approach. It reads like a robust template applied to the same excerpt.

### 4) Completeness — **4/5**
Comprehensively covers the major risk allocation areas (data/AI, privacy/DPA, liability caps, indemnity, suspension, deletion/retention, publicity, security testing restrictions, missing governing law/venue variables, incorporation by reference). It also repeatedly reinforces the “cannot finalize without missing documents” gating items, which is practically important.

### 5) Audience Awareness — **4/5**
Well-tuned to a customer-side legal/procurement audience: it separates “evidence,” “business impact,” “decision needed,” and “disposition,” which makes internal routing and escalation easier. The negotiation steps and tradeoffs are clearer and more operational than in Set 1.

### [Legal] Risk Identification Accuracy — **4/5**
Finds the genuinely risky clauses and treats “missing definitions/variables” as a first-class risk rather than a footnote, which is accurate for this contract style. It also captures key interactions (ML clause + survival; DPA + security posture; caps + indemnity), though it still can’t validate specific cap outcomes without the missing cover page.

---

## Set 3 — Scores (pipeline finals; median across runs 1–3)

### 1) Depth — **4/5**
Strong at negotiation-level synthesis: prioritization, sequencing, bundles, and explicit dependency mapping (e.g., AI/ML ↔ content rights/usage data ↔ DPA; liability ↔ indemnity). It demonstrates “thread-following” across issues rather than a clause-by-clause checklist.

### 2) Specificity — **3/5**
The briefs are specific to the *issue set* (I-### items, redline pack references), but comparatively less specific to the underlying contract text (few direct clause quotes in the final). This makes it slightly harder to audit whether the brief faithfully reflects the source agreement versus the intermediate artifacts.

### 3) Natural Variation (across runs 1–3) — **3/5**
All runs produce a similar negotiation brief scaffold, but there is real variation in which issues are “Must-have” vs “Escalate,” and how the bundles are framed. One concerning type of variation is inconsistency in issue numbering/mapping across runs, which can introduce operational confusion.

### 4) Completeness — **4/5**
Covers all the major risk buckets and, importantly, highlights “gating” missing documents/variables as the first move—appropriate for provider-friendly paper with externalized terms. It also includes practical open questions and next steps that support execution.

### 5) Audience Awareness — **4/5**
The format is very usable for real negotiation planning: one-paragraph risk posture, prioritized issues, sequencing, trades, dependencies, and escalation prompts. This feels tailored to the internal stakeholder audience that needs to run a vendor call and align approvals quickly.

### [Legal] Risk Identification Accuracy — **4/5**
The core risk calls are accurate and the cross-section interaction awareness is strong (especially liability–indemnity and AI/ML–data governance–DPA). The main accuracy risk is process-related: because the final relies on intermediate issue IDs rather than quoting clauses, any mismatch in the issue map propagates into the brief.

---

## Summary

| Dimension | Set 1 | Set 2 | Set 3 |
|---|---:|---:|---:|
| 1. Depth | 3 | 4 | 4 |
| 2. Specificity | 4 | 4 | 3 |
| 3. Natural Variation | 3 | 2 | 3 |
| 4. Completeness | 3 | 4 | 4 |
| 5. Audience Awareness | 3 | 4 | 4 |
| Risk Identification Accuracy | 4 | 4 | 4 |

**Overall preference**: **Set 2**, narrowly.

**Key differences**:
- Set 2 is the most balanced “do the review + make it actionable” output: clause-grounded, comprehensive, and structured for internal decisions.
- Set 3 is the most *negotiation-ready* (sequencing/bundling/dependencies), but is less directly auditable against the contract text because it leans on intermediate issue IDs.
- Set 1 is solid and clause-specific, but is less comprehensive and less explicitly dependency-aware in its median run.

**Magnitude**:
- **Set 2 vs Set 1**: **Moderate** improvement (depth/completeness/audience awareness are meaningfully better).
- **Set 2 vs Set 3**: **Small to moderate** difference depending on use-case (review artifact vs negotiation brief). In practice, I’d want Set 2’s clause-grounding *plus* Set 3’s negotiation packaging.

## Diagnostic observations (not fully captured by the rubric)
- **Process fidelity / traceability**: Set 3’s finals rarely quote the underlying agreement, so the reader must trust the upstream issue extraction; inconsistency in issue numbering across runs increases the chance of operational mistakes (e.g., referencing the wrong “I-###” in negotiation).
- **Templated feel**: Set 2 is high quality but structurally very templated across runs, which lowers the Natural Variation score even though the template is useful.
- **Potential ungrounded detail**: One optimised run mentions a specific release date for the Standard Terms; if that date wasn’t in the excerpt, it would be an avoidable hallucination risk (minor but worth watching in a legal context).
