---
model: GPT-5.2
date: 2026-03-15
experiment: A3
artifact: prompt-architect-analysis
---

# Prompt Architect Analysis — `original/SKILL.md` (`/performance-review`)

## 0) Artifact snapshot (what’s in the prompt)
The skill defines a slash command `/performance-review` with three explicit modes:
- `self-assessment` → produces a self-assessment template
- `manager [employee]` → produces a manager review template
- `calibration` → produces a calibration prep template

It also includes conditional instructions for “If Connectors Available” (~~HRIS, ~~project tracker) and a short “Tips” list about specificity and behavior-based feedback.

This is primarily a **template generator**: it prescribes output headings, tables, and placeholder slots.

## 1) What the prompt is *actually asking for* (cognitive posture)
The dominant posture is **convergent structuring + constrained generation**:
- **Structuring**: Provide pre-shaped containers (sections, tables, rating buckets) that a human can fill.
- **Generation**: Emit the template text and placeholders cleanly in Markdown.

Second-order postures appear depending on mode:
- **Evaluation** is implicitly present in `manager` and `calibration` modes (overall rating, compensation recommendation, rating distribution).
- **Investigation / retrieval** is optionally introduced via connectors (“Pull prior review history…”, “Pull completed work…”).
- **Orchestration** is minimal: the only explicit routing is “If no mode is specified, ask what type of review they need.”

Net: the skill is not asking the model to deeply *discover* truths; it is asking it to **standardize how truths should be recorded and communicated**.

## 2) Where modes interfere (and why)
Overall, this prompt is relatively “clean” for what it is (a template skill). The main risks are not classic investigation/evaluation contamination, but **anchoring and posture drift** created by evaluation language and fixed-slot templates.

### 2.1 Evaluation posture bleeds into generation (within the same artifact)
In the Manager Review template, evaluative decisions are placed as fillable slots alongside narrative structure:
- “### Overall Rating: [Exceeds / Meets / Below Expectations]”
- “### Compensation Recommendation [Promotion / Equity refresh / Adjustment / No change — with justification]”

Mechanism (mode interference): when the prompt frames “rating” and “compensation recommendation” as adjacent template fields, the model is pulled toward an **HR-decision** posture even when the user intent may be “help me structure evidence-based feedback.” This can suppress the exploratory/reflective stance that would surface nuanced behavioral examples, because the model implicitly optimizes for completing the evaluative boxes.

This isn’t “wrong” (performance reviews often include ratings), but it creates a predictable failure mode: **premature convergence**—committing to a rating/disposition before enough evidence or context is elicited.

### 2.2 Connectors introduce investigation, but the skill doesn’t protect it from evaluation anchors
The connectors section proposes pulling historical review/goal data and project contributions:
- “Pull prior review history and goal tracking data”
- “Pull completed work and contributions for the review period”

But the calibration section also provides explicit distribution targets:
- “Company Target ~15-20% / ~60-70% / ~10-15%”

Mechanism: if retrieval is available, the session could mix **investigation (fetch evidence)** with **evaluation (fit into target distribution)**. In mixed contexts, evaluation criteria can become a pre-filter: evidence that doesn’t map cleanly to a rating bucket or distribution narrative may be underweighted or omitted.

### 2.3 Output structure as a convergent “box-filling” engine
The skill heavily specifies the output container (tables, fixed headings). Even where the content should be free-form, the structure encourages completion behavior:
- Self-assessment asks for “top 3–5 accomplishments” plus three numbered “Goals for Next Period.”
- Manager review asks for “2-3 sentence overall assessment.”

Mechanism: fixed slots bias the model toward producing “the right number of things” rather than “the right things.” This is not a mode conflict per se, but it is a structural constraint that can make outputs **competent but predictable**.

## 3) Numeric anchors (explicit + implicit)
This prompt contains multiple anchors that will reliably stabilize output size and shape:
- “top 3-5 accomplishments”
- “2-3 sentence overall assessment”
- “Goals for Next Period: 1…2…3…” (implicit: always three)
- Calibration: company target percentages (“~15-20%”, “~60-70%”, “~10-15%”)

Why it matters (per framework): these anchors can cause the model to converge on midpoints (e.g., 4 accomplishments) regardless of what the user’s actual data supports. The calibration target numbers are especially strong anchors because they imply an externally validated distribution.

Health signal to look for: **natural variation**. If every run produces the same counts and similar density regardless of context richness, the anchors are dominating.

## 4) Seeds vs lenses
The skill is mostly **seeds** (prescribed headings, rating buckets, table columns), with a small amount of **lenses** in the Tips (“Be specific”, “Focus on behaviors…”).

Because this is a template-generator skill, seeding is partly appropriate: the *goal* is consistent structure.

Risk: when users want help *thinking* (what evidence matters, what themes exist, what to say delicately), the seeded template can constrain the model into **format-completion** rather than sensemaking. The tips are not integrated as lenses that guide what to ask the user or how to reason; they sit after the templates as general advice.

## 5) What to check for in outputs (diagnostics)
When this skill is used, look for these contamination/anchoring signatures:

1. **Uniform counts**: always 3 goals, always ~4 accomplishments, always ~2 development areas—even when the user provides very sparse or very rich input.
2. **Premature rating**: the output confidently populates “Overall Rating”/“Compensation Recommendation” without first requesting evidence, context, or the org’s rating rubric.
3. **Template compliance over substance**: lots of filled headings with generic filler (“Strong communicator”, “Improve prioritization”) rather than behavioral examples.
4. **Distribution gravity** (calibration): recommendations drift toward the provided company target percentages even when the team composition or performance distribution described by the user would imply otherwise.
5. **Connector hallucination**: the model implies it “pulled” HRIS/project data when none is actually available (a runtime/tooling mismatch risk created by conditional connector language).

## 6) What to do about it (interventions; not a rewrite)
These are prompt-structure interventions to consider (prompt-level, not pipeline reconstruction), keyed to the mechanisms above:

- **Add a scope boundary before evaluative fields**: make explicit that the template should not be populated with ratings/comp changes unless the user provides (a) evidence and (b) the org’s rubric. This reduces premature convergence from evaluation posture.

- **Convert fixed-count slots into optional slots** (or at least allow “0–N”): remove the implicit requirement to always produce three goals / 3–5 accomplishments. This restores natural variation and reduces anchoring.

- **Move from seed-only templates to seed + lens prompts**: embed a small set of lens questions *upstream* of the template (e.g., ask for role/level expectations, key projects, feedback snippets). This keeps the generation posture but adds light orchestration and sensemaking.

- **Treat calibration targets as adjustable context, not default truth**: explicitly frame distribution targets as “reference constraints” rather than “aim here,” to avoid anchor-driven convergence.

- **Add a connector boundary**: if connectors are unavailable, explicitly instruct the model to ask the user for the missing data rather than implying retrieval occurred.

Trade-off note (per framework): tightening boundaries and removing numeric anchors improves depth and honesty, but reduces “instant template completion” convenience.

## 7) Composition signature (runtime composition / skill interaction)
Because this file is itself a skill intended to be loaded into an interactive agent environment, the key composition question is: what mode does it inject into the session?

- **Skill `/performance-review` (this file)**: Structuring + Generation, with embedded Evaluation (rating/compensation/distribution) and optional Investigation (connector-based retrieval).

Potential incompatibilities when combined with other skills or a base agent:
- If the base agent/session is in **investigation** mode (open-ended exploration) and this skill is loaded, the embedded **evaluation** elements (“Overall Rating”, distribution targets) can pull the session toward judgment and box-filling.
- If another loaded skill is explicitly **evaluative/compliance-like**, combining it with the calibration distribution targets can compound anchoring effects.

Benign combinations:
- With skills that add **formatting** or **note-taking**, this skill stays primarily generative/structuring.

## 8) Handoff
Analysis complete. Ready to hand off to the `prompt-writer` agent to implement prompt-level changes (if desired) while preserving the skill’s intended templating function.
