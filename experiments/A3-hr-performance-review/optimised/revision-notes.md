# Revision Notes: HR Performance Review (A3 Optimised)

## Architect finding -> revision mapping

### Finding 1: Evaluation-first ordering in manager review (Moderate)
**What changed:** Moved `### Overall Rating` from the first substantive section to the last section before Compensation Recommendation. The template now flows: Performance Summary, Key Strengths, Areas for Development, Goal Achievement, Impact and Contributions, Development Plan, and only then Overall Rating. Added a bracketed note after the rating slot: "this should feel like a conclusion the evidence leads to, not a premise the evidence was selected to support."

**Why this approach:** When the rating comes first, it becomes an anchor — every subsequent section gets shaped to justify the pre-committed judgment. Moving it to the end lets the model (or the human using the template) build the evidentiary case first and arrive at the rating as a conclusion. The Performance Summary still comes early, but it's framed as synthesis ("synthesise from the evidence, don't just restate the rating") rather than judgment, so it serves as orientation rather than commitment.

### Finding 2: Numeric anchors from fixed template slots (Low-Moderate)
**What changed:**
- Self-assessment accomplishments: "List your top 3-5 accomplishments" replaced with "List key accomplishments from this period — as many as are genuinely significant."
- Self-assessment goals: Removed the numbered "1. [Goal] / 2. [Goal] / 3. [Goal]" template. Replaced with guidance ("as many as are meaningful for the upcoming period") followed by a single example slot.
- Manager review Key Strengths: Removed the two fixed bullet slots. Replaced with "Note what stands out from the evidence — as many or few as the data warrants" followed by a single example slot.
- Manager review Areas for Development: Same treatment — "as many or few as are genuine" with a single example slot.
- Calibration Discussion Points: Removed the numbered "1. / 2." template. Replaced with flexible bullet format and "include as many or few as the team warrants."

**Why this approach:** Fixed slot counts force uniform output regardless of what the data warrants. An exceptional employee might have five strengths and one development area; a struggling employee might have one strength and four areas. The template should accommodate natural variation. Keeping a single example slot shows the format without anchoring the count.

### Finding 3: Rating distribution targets as seeds (Low, calibration)
**What changed:** Removed the `Company Target` column from the Rating Distribution table. Moved the distribution reference below the table as contextual guidance: "Company distributions typically fall in the range of 15-20% Exceeds, 60-70% Meets, 10-15% Below. Note any significant deviation from these ranges for discussion — but don't adjust ratings to fit."

**Why this approach:** The original included target percentages as a column in the data table, which frames them as values the model's output should match. Moving them to a prose note reframes them from "targets to hit" to "reference context for discussion." The added instruction "don't adjust ratings to fit" explicitly counters the tendency to massage edge cases toward the target distribution. The distribution ranges are preserved because they are genuinely part of calibration practice — the change is in how they're presented, not whether they're included.

### Finding 4: Missing investigation guidance for manager mode (Moderate)
**What changed:** Added an investigation block before the manager review template. This block contains five lenses:
- **Trajectory** — trend vs. snapshot
- **Growth patterns** — where they stretch beyond vs. operate within current level
- **Gap between perception and impact** — self-view vs. team experience
- **Next-level readiness** — what the work reveals about readiness
- **Contradictory signals** — where the data tells conflicting stories

The block opens with "Before filling in the template, investigate the performance data. Don't start with a rating or summary — start with the evidence and let the picture emerge." It closes with "Let this investigation shape the review."

**Why this approach:** The original prompt treated the manager review as pure template-filling — map data to slots. But manager reviews require genuine investigation: understanding trajectory, spotting patterns, reconciling contradictions. The lenses guide this investigation without prescribing what the model should find (they're questions, not answers). The explicit instruction to investigate before writing creates a temporal boundary between investigation and template-filling, similar to the phase separation used in A2.

## What to watch for when testing

1. **Rating-evidence alignment.** In the manager review, does the evidence feel like it was discovered through investigation, or does it feel like it was selected to justify the rating? The revision should produce reviews where the evidence section reads as genuinely investigative — including tensions and contradictions — rather than as a case built in support of a predetermined conclusion.

2. **Slot count variation.** Run on two different employee profiles. If both reviews have exactly the same number of strengths and development areas, the anchor removal hasn't fully worked. Healthy: different employees get different numbers of strengths and development areas based on what the evidence warrants.

3. **Investigation depth in manager reviews.** Does the Performance Summary feel like a genuine synthesis or a restated rating? Does the Impact section reveal something that wasn't obvious from the strengths list? These are signals that the investigation guidance is shaping the output.

4. **Calibration distribution.** Does the calibration output land precisely within the target percentages, or does it honestly report the team's distribution and flag the deviation? The revision should produce calibrations that name the deviation rather than hiding it.

5. **Development plan specificity.** Are development plans specific to the employee's actual situation, or are they generic ("improve communication skills")? The investigation lenses should give the model enough understanding of the employee to write genuinely tailored development actions.

## Design rationale

The core move for this prompt is lighter than A2 because the interference is lower. This is mostly convergent template work, and the fixes are calibration adjustments rather than structural reconstruction:

- **Reordering** the manager review template so evidence precedes judgment — the lightest possible intervention that addresses the evaluation-first anchoring.
- **Removing numeric anchors** from template slots — freeing the model to match output volume to evidence, not to slot count.
- **Reframing** distribution targets from table columns (implicit targets) to prose context (explicit reference) — preserving domain-appropriate information while changing its cognitive function.
- **Adding investigation guidance** — the most substantive addition, and the one most likely to produce visible improvement. The original prompt had zero guidance on how to think about performance data; it assumed the user (or model) already knew. The lenses provide structure for investigation without prescribing conclusions.

What's preserved: all three modes, all template sections, the connector guidance, and the tips section. The domain knowledge in the original was solid — the revision changes how the model engages with it, not what it knows.
