# Prompt Architect Analysis: Engineering Debug

## 1. What the Prompt Is Actually Asking For

This prompt asks the model to run a structured debugging session through four sequential steps:

1. **Reproduce** — understand expected vs actual behaviour, identify scope (Investigation + Structuring)
2. **Isolate** — narrow down component/code path, check recent changes (Investigation)
3. **Diagnose** — form hypotheses, trace code paths, identify root cause (deep Investigation + Synthesis)
4. **Fix** — propose fix, consider side effects, suggest tests (Generation + Evaluation)

The cognitive sequence is: Investigation → Investigation → Investigation+Synthesis → Generation+Evaluation.

## 2. Where Modes Interfere

### 2.1 Investigation + Generation Coexistence (Moderate)

The core interference is between diagnosis (Steps 1-3, investigation) and fixing (Step 4, generation). These share a single context. The presence of "Fix" in the prompt — and particularly the output template's `### Fix` section — means the model investigates with fix-generation in mind. This is the classic "investigation + generation" toxic pair: the model only investigates things it can fix, and skips findings that don't have obvious solutions.

**Mechanism**: When the model knows it needs to produce a fix, its investigation becomes solution-shaped. It follows threads that lead toward fixable causes and drops threads that lead toward systemic issues, architectural problems, or root causes that require larger interventions. The investigation becomes a funnel for the fix recommendation.

**Severity**: Moderate. The sequential step structure provides some natural separation — Step 1 is clearly "reproduce," Step 3 is clearly "diagnose." But the output template is visible from the start, so the model knows during investigation that it will need to produce a `### Fix` section. The fix destination shapes the investigation journey.

### 2.2 The Sequential Steps Provide Partial Natural Separation (Mitigating)

Unlike many prompts, this one has a genuinely well-structured sequence. Reproduce → Isolate → Diagnose → Fix follows a natural debugging workflow. Each step has a clear cognitive boundary. This is significantly better than prompts that ask for all four simultaneously.

**However**: the steps are described in one context with one output template. The model doesn't truly context-switch between steps — it fills the template in order, with the full template (including Fix) visible throughout. The sequential DESCRIPTION is good, but the sequential EXECUTION is not enforced. The model sees the fix section while investigating.

### 2.3 The Output Template Is Lightweight (Positive)

The output template is minimal: Reproduction, Root Cause, Fix, Prevention. Four sections, no fixed slot counts, no numeric anchors. This is well-designed — it doesn't over-constrain the output. The model has space to write as much or as little as the problem warrants in each section.

**One concern**: the template omits an explicit "Diagnosis/Investigation" section. The model goes straight from Reproduction to Root Cause, which implicitly asks it to compress investigation into a conclusion. There's no space to document the investigative process — hypotheses considered, threads followed, evidence weighed. The template asks for the RESULT of investigation (root cause) without the investigation itself.

### 2.4 Prevention Section Mixes Evaluation with Generation (Low)

The `### Prevention` section asks for tests and guards — this is generation informed by evaluation of what went wrong. These are compatible (both convergent, focused on the same problem). Low interference.

### 2.5 No Numeric Anchors (Positive)

The prompt contains no specific numbers acting as targets. The Tips section doesn't suggest counts. The output template doesn't fix slot numbers. This is clean.

### 2.6 No Seeds (Positive)

The prompt doesn't seed specific types of bugs or causes to look for. It provides lenses ("What changed recently?", "Expected vs actual") rather than lists of specific things to check. This is good design for investigative work.

## 3. What to Check For in the Output

- **Fix-shaped investigation**: Does the root cause section describe a cause that conveniently has a clean fix? If the root cause feels too neat — perfectly matching the fix — the investigation may have been shaped by the fix destination. Real debugging often reveals messy root causes that require multi-part fixes or systemic changes.
- **Missing hypotheses**: Does the output mention hypotheses that were considered and rejected, or does it present a single linear path from symptom to root cause? Real debugging involves testing multiple hypotheses. If the output shows only the winning hypothesis, the template's lack of an investigation section may be suppressing the diagnostic process.
- **Prevention depth**: Are the prevention suggestions specific to this bug, or generic? ("Add tests" is generic. "Add an integration test that verifies inventory reservation under concurrent load with a timeout lower than the Lambda's expected runtime" is specific.)
- **Systemic vs local root cause**: Does the root cause section address only the proximate cause, or does it consider systemic factors? If the model stops at the immediate fix and doesn't explore why the system was vulnerable to this failure mode, fix-shaped investigation may be limiting the depth.

## 4. What to Do About It

### Tier 2 — Prompt-Level Optimisation

1. **Add scope boundary**: Before the steps, add: "Your primary job is to understand WHY this is happening. The fix follows from understanding — don't let the desire for a fix shape your investigation. Investigate thoroughly, including threads that might not lead to simple fixes."
2. **Add investigation output section**: Between Reproduction and Root Cause in the template, add a `### Diagnosis` section: "Hypotheses considered, evidence for and against, investigation threads followed. Show your reasoning — what did you consider and why did you narrow to this root cause?"
3. **Reframe the Fix section**: Change from "Code changes or configuration fixes needed" to "What should change, and at what level? Some fixes are code changes. Some are architectural. Some are process changes. Match the fix to the root cause — if the root cause is systemic, a code patch is treating symptoms."
4. **Keep the sequential structure**: The 4-step sequence is well-designed. Don't change it.

### Tier 3 — Pipeline Reconstruction

This is a calibration case — the prompt is already reasonably well-structured. Pipeline reconstruction provides moderate value.

**Agent 1 — Investigator** (Investigation + Structuring)
- Receives: bug report, error messages, logs, context
- Does: reproduces the issue, isolates the component, forms and tests hypotheses, traces code paths. Investigates freely without needing to produce a fix.
- Produces: structured investigation findings — reproduction steps, component isolation, hypotheses with evidence, root cause analysis with confidence levels
- Why separate: investigation without fix-generation in context allows the model to follow threads that might lead to uncomfortable conclusions (architectural issues, systemic problems, process failures). The model doesn't need every thread to terminate in a fixable cause.

**Agent 2 — Fix Designer** (Generation + Evaluation)
- Receives: structured investigation findings from Agent 1
- Does: designs a fix (or fixes) that addresses the root cause at the appropriate level. Considers side effects, edge cases, regression risks. Suggests tests.
- Produces: fix proposal with rationale, prevention measures
- Why separate: generation works best when it receives fully investigated input. The fix designer doesn't need to simultaneously investigate — it receives a clear root cause and designs the appropriate intervention.

**Handoff**: Agent 1 → structured findings (hypotheses, evidence, root cause with confidence) → Agent 2. Structured format strips investigative tone so Agent 2 gets clean input for fix generation.

**Execution**: Sequential. Agent 2 depends on Agent 1's complete output.

## 5. Composition Signature

Single-prompt skill, no runtime composition concerns. Within the prompt:
- Investigation + Generation (moderate interference — sequential structure mitigates but doesn't eliminate)
- Investigation + Structuring (compatible)
- Generation + Evaluation (compatible — both convergent in the fix context)

## 6. Overall Assessment

**Severity: Low-to-moderate.** This is a calibration case. The prompt has several things going for it:
- Clean sequential structure that mirrors real debugging workflow
- No numeric anchors or seeds
- Lightweight output template
- Lenses rather than prescribed categories

The main interference is Investigation + Generation sharing context, with the fix destination shaping how the model investigates. This is real but partially mitigated by the sequential step structure.

**Expected experimental outcome**: Tier 2 should show modest improvement (scope boundary and investigation output section help). Tier 3 may show moderate improvement — separating investigation from fix-generation should produce deeper root cause analysis that considers systemic factors — but the gains may be smaller than in A4 or A6 because the original prompt is already reasonably well-structured. This experiment serves as a useful calibration point: if even a well-structured prompt shows improvement from pipeline separation, that strengthens the overall thesis.
