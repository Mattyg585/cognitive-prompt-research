# Prompt Architect Analysis: HR Performance Review

## 1. What the Prompt Is Actually Asking For

This prompt operates in three modes — self-assessment, manager review, and calibration — each requiring different types of thinking:

**Self-assessment mode**: Primarily **generation** within a fixed template. The model fills structured slots with placeholder guidance. This is straightforward convergent work — the template IS the output. Minimal cognitive complexity.

**Manager review mode**: The most cognitively complex mode. Requires:
- **Investigation** — understanding the employee's performance from provided data
- **Evaluation** — judging performance against expectations (rating, goal achievement)
- **Synthesis** — compressing observations into a coherent narrative (Performance Summary, Impact and Contributions)
- **Generation** — producing actionable development plans and compensation recommendations
- **Reframing** — translating raw observations into constructive feedback language

**Calibration mode**: Primarily **structuring** and **evaluation** — organising team data, comparing against distribution targets, identifying discussion points. Both convergent, so compatible.

## 2. Where Modes Interfere

### 2.1 Evaluation-First Ordering in Manager Review (Moderate)

The manager review template places `### Overall Rating: [Exceeds / Meets / Below Expectations]` as the FIRST substantive section, before any evidence sections (Key Strengths, Goal Achievement, Impact). This forces the model to commit to a judgment before building the evidentiary case.

**Mechanism**: The rating becomes an anchor. Once "Meets Expectations" is written, every subsequent section is shaped by confirmation bias — strengths are described at the level of "meets," development areas are calibrated to justify "meets, not exceeds." If the rating came after the evidence, the model might discover through investigation that the evidence supports a different rating than the manager initially assumed.

**Severity**: Moderate. In practice, the user typically knows the rating going in. But when the scenario is ambiguous, this ordering suppresses the investigation of evidence that might challenge the pre-committed rating.

### 2.2 Numeric Anchors from Fixed Template Slots (Low-Moderate)

- `"List your top 3-5 accomplishments"` — anchors to 4 accomplishments regardless of actual count
- Manager review has exactly 2 Key Strengths slots (`- [Strength with specific example]` × 2)
- Exactly 2 Areas for Development slots
- `"Goals for Next Period: 1, 2, 3"` — anchors to exactly 3

**Mechanism**: The model will produce exactly the number of items the template suggests, regardless of what the data warrants. An exceptional employee might have 5 strengths worth noting and 1 development area. A struggling employee might have 1 strength and 4 areas. The template forces both to look identical in structure.

**Severity**: Low-moderate. For template generation, fixed slots are common and expected. But they suppress the natural variation that would make reviews more honest and useful.

### 2.3 Rating Distribution Targets as Seeds (Low, Calibration Mode)

The calibration template includes `Company Target` columns: `~15-20%` for Exceeds, `~60-70%` for Meets, `~10-15%` for Below. These are seeds — they tell the model what the distribution SHOULD look like, which anchors the model toward conforming to these targets rather than honestly assessing where the team falls.

**Mechanism**: The model will tend to massage edge cases to fit the target distribution rather than honestly reporting where individuals fall and flagging the distribution discrepancy.

**Severity**: Low. Distribution targets are a real part of calibration processes, so including them is domain-appropriate. The risk is that the model optimises for distribution fit rather than accurate assessment.

### 2.4 Missing Investigation Guidance for Manager Review (Moderate)

The prompt provides detailed output templates but zero guidance on HOW to investigate and synthesise performance data. The Tips section mentions specificity and balance, but there's no lens for how to look at the data — what patterns to attend to, how to weigh different types of evidence, how to handle contradictory signals.

**Mechanism**: Without investigation guidance, the model defaults to template-filling. It maps data to template slots rather than investigating the data to understand the person's performance trajectory. This produces reviews that are structurally correct but lack genuine insight — the "good output hiding great output" pattern.

**Severity**: Moderate. This is the main gap. The prompt treats the review as a template-filling exercise when the manager review mode actually requires genuine investigation and synthesis.

## 3. What to Check For in the Output

- **Rating-evidence alignment**: Does the evidence section feel like it was written to justify the rating, or does it feel like honest investigation that happens to support the rating? If the former, evaluation-first ordering is anchoring.
- **Uniform slot counts**: Does every review have exactly 2 strengths and 2 development areas regardless of the employee? If so, template slots are anchoring.
- **Calibration distribution conformity**: Does the calibration output magically land within the target percentages? If so, the distribution targets are acting as seeds.
- **Surface-level development plans**: Are development plans generic ("improve communication skills") or specific to the actual person? Generic plans suggest template-filling rather than investigation.
- **Performance summary depth**: Does the 2-3 sentence summary feel like a genuine synthesis or a restatement of the rating? Synthesis requires the model to have actually investigated — if it reads like "Jordan meets expectations because [list of things]," that's template-filling, not synthesis.

## 4. What to Do About It

### Tier 2 — Prompt-Level Optimisation

1. **Reorder the manager review template**: Move Overall Rating to the END, after all evidence sections. Let the model investigate and synthesise before committing to a judgment.
2. **Remove fixed slot counts**: Replace `2 × Key Strengths` with guidance like "Key strengths — note what stands out from the evidence, as many or few as the data warrants." Same for Development Areas.
3. **Reframe distribution targets**: Change from "Company Target: ~15-20%" to a note like "Company distributions typically fall in these ranges — note any significant deviation for discussion" to prevent optimisation toward the target.
4. **Add investigation guidance for manager mode**: Before the template, add a lens like: "Before writing, consider: What's the trajectory? Where is growth accelerating or plateauing? What does this person's work reveal about their next level readiness? Where is the gap between their self-perception and the team's experience of them?"
5. **Remove "3-5 accomplishments"**: Replace with "List key accomplishments — as many as are genuinely significant."

### Tier 3 — Pipeline Reconstruction

Pipeline reconstruction adds value primarily for the **manager review mode**. Self-assessment and calibration are well-served by Tier 2 fixes.

**Pipeline for Manager Review mode:**

**Agent 1 — Performance Investigator** (Investigation + light Structuring)
- Receives: employee data, performance observations, goals
- Does: investigates the performance data with lenses — trajectory, growth patterns, gap between potential and current level, team impact patterns
- Produces: structured findings (observations, evidence, patterns) — NOT ratings or judgments
- Why separate: investigation without evaluation criteria in context allows the model to notice patterns it might otherwise filter out

**Agent 2 — Review Writer** (Synthesis + Evaluation + Generation)
- Receives: structured findings from Agent 1
- Does: synthesises findings into the review template, assigns rating based on evidence, writes development plan
- Produces: the final review document
- Why separate: evaluation and synthesis are compatible (both convergent); receiving pre-investigated findings means the synthesis works from rich material rather than doing shallow template-filling

**Handoff**: Agent 1 → structured findings (bullets, not prose) → Agent 2. The structured format strips the investigative cognitive mode so Agent 2 gets clean input for synthesis.

## 5. Composition Signature

Single-prompt skill with three independent modes. No pairwise composition conflicts between modes (they don't run simultaneously). Within each mode:
- **Self-assessment**: Generation (clean)
- **Manager review**: Investigation + Evaluation + Synthesis + Generation (moderate interference — evaluation-first ordering is the main issue)
- **Calibration**: Structuring + Evaluation (compatible — both convergent)

## 6. Overall Assessment

**Severity: Low-to-moderate.** This is a calibration case. The prompt is largely doing convergent template generation, which is the type of work where fixed structure is least harmful. The interference is real but bounded:

- The manager review mode has genuine investigation + evaluation mixing, but it's mitigated by the sequential template structure
- Numeric anchors exist but are common in this domain
- The biggest miss is investigation guidance — the prompt treats all modes as template-filling when the manager review mode actually needs genuine performance investigation

**Expected experimental outcome**: Tier 2 should show incremental improvement (reordering, removing anchors). Tier 3 may show moderate improvement in the manager review mode specifically, but the gains may be smaller than in experiments with stronger mode interference (A4, A6).
