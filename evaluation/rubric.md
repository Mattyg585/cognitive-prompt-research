# Evaluation Rubric

## Purpose

Score AI prompt outputs to compare baseline (original prompt) vs optimised versions. Designed for blind evaluation — the evaluator should not know which version produced which output.

## Dimensions

### 1. Depth (1-5)

| Score | Description |
|-------|-------------|
| 1 | Surface-level, obvious findings only. Restates what's visible without analysis. |
| 2 | Covers some expected ground but misses layers. |
| 3 | Covers expected ground competently. Finds what a knowledgeable person would expect. |
| 4 | Goes beyond the expected. Follows threads, connects non-obvious dots. |
| 5 | Surprising insights. Finds things that reframe how you think about the input. |

### 2. Specificity (1-5)

| Score | Description |
|-------|-------------|
| 1 | Generic. Could apply to any input of the same type. |
| 2 | Some grounding in the specific input but mostly templated. |
| 3 | Grounded in the actual input. References specific elements. |
| 4 | Precise references. Actionable recommendations tied to specific details. |
| 5 | Deeply specific. Every observation is traceable to evidence in the input. |

### 3. Natural Variation (1-5)

*Score this across multiple runs of the same version, not on a single output.*

| Score | Description |
|-------|-------------|
| 1 | Identical structure and count across all runs regardless of input complexity. |
| 2 | Minor wording variation but same structure and findings. |
| 3 | Some variation in findings count and emphasis. |
| 4 | Output structure and depth visibly respond to input complexity. |
| 5 | Simple inputs get concise output; complex inputs get deep output. Natural stopping points. |

### 4. Completeness (1-5)

| Score | Description |
|-------|-------------|
| 1 | Misses obvious, important things. |
| 2 | Covers some areas but has notable gaps. |
| 3 | Covers major points adequately. |
| 4 | Comprehensive without padding. Everything present earns its place. |
| 5 | Comprehensive AND appropriately weighted. More depth where it matters most. |

### 5. Audience Awareness (1-5)

| Score | Description |
|-------|-------------|
| 1 | Wrong register. Reads like it was written for a different audience. |
| 2 | Acceptable but generic tone. |
| 3 | Appropriate register for the target audience. |
| 4 | Tailored. Anticipates what this audience cares about. |
| 5 | Models the audience's perspective. Understands not just what they need but how they'll receive it. |

## Scoring Protocol

### For single-run comparison
1. Read Output A and Output B without knowing which is baseline/optimised
2. Score each independently on dimensions 1, 2, 4, 5
3. Note which output you'd prefer to receive if you were the target audience
4. Provide 2-3 sentences of reasoning per dimension

### For multi-run comparison
1. Read all runs of Version A, then all runs of Version B
2. Score dimension 3 (Natural Variation) for each version
3. Score dimensions 1, 2, 4, 5 using the median-quality run from each version
4. Note the range of quality within each version

### Overall assessment
After scoring all dimensions:
- Which version would you trust more for real work?
- What does the better version do that the other doesn't?
- Is the difference meaningful or marginal?

## Domain-specific additions

For some experiments, add domain-specific scoring:

| Domain | Additional dimension |
|--------|---------------------|
| Legal | **Risk identification accuracy**: Did it find the genuinely risky clauses? |
| Security | **Vulnerability detection**: Did it find real issues, not just noise? |
| Creative writing | **Voice and engagement**: Does it read well? Would you keep reading? |
| HR | **Bias and fairness**: Does the output avoid problematic assumptions? |
| Code | **Correctness**: Does the generated code actually work? |
