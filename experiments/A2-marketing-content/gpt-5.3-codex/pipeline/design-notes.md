# Pipeline Design Notes — A2 (GPT-5.3-Codex)

## Why pipeline instead of single prompt only

A2 is a creative + compliance hybrid task. The core interference risk is generation quality being suppressed by in-context evaluation pressure. The pipeline separates:

- Exploration (divergent)
- Narrative commitment (convergent)
- Draft generation (divergent)
- Compliance polish (convergent)

This matches the stance principle: separate when modes interfere, especially investigation/generation mixed with evaluation.

## Why four stages

- Stage 01 prevents premature structure lock-in.
- Stage 02 commits to one narrative strategy so Stage 03 can write decisively.
- Stage 03 is protected from checklist contamination.
- Stage 04 applies SEO and channel constraints after voice is established.

Combining 03 and 04 would recreate the original contamination. Splitting 01 and 02 avoids "explore while deciding" collapse.

## Expected behavioral differences vs baseline

1. Stronger audience-state modeling in openings.
2. Less template repetition across runs.
3. Better proof weighting (not equal feature coverage by default).
4. Cleaner CTA momentum.

## Risks and mitigations

- **Risk:** Stage 02 over-constrains writer creativity.
  - **Mitigation:** Stage 02 defines purpose and beats, not sentence-level copy.
- **Risk:** Stage 04 flattens voice.
  - **Mitigation:** explicit voice-preservation rule and trade-off logging in editorial notes.
- **Risk:** Handoffs become verbose and reintroduce contamination.
  - **Mitigation:** structured, compressed output formats.

## Evaluation focus for A2

Beyond core rubric, prioritize **Voice and Engagement**:
- Does it sound like a real point of view?
- Would a busy engineering manager keep reading?
- Does the post create momentum toward “Start free trial” without generic sales tone?