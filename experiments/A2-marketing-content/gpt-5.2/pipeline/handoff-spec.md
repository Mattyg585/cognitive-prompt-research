# A2 Tier 3 Pipeline — Handoff Spec (GPT-5.2)

This document defines the **stage sequence**, the **structured handoff formats**, and what information is allowed to cross each boundary.

> Goal: protect creative divergence (angles/voice) from early template/SEO/evaluation pressure, then converge into channel-ready assets with a clean, coherence-preserving message spine.

## 1) Stage sequence (filenames are canonical)

Run stages **in this exact order**:

1. `01-brief-normalizer`
2. `02-angle-ideator`
3. `03-concept-decider`
4. `04-asset-drafter`
5. `05-copy-optimizer`

Each stage has two prompt files:
- Claude format: `<stage>.md`
- Copilot format: `<stage>.agent.md`

## 2) Shared boundary rules (apply to all handoffs)

- **Pass structured artifacts, not exploratory prose.** Use the specified YAML blocks.
- **Drop**:
  - long reasoning, self-critique, “why this is interesting” narrative
  - alternative paths not chosen (unless explicitly requested as backups)
  - checklists and scoring language *before* the concept is chosen
- **Keep**:
  - factual brief constraints
  - the chosen concept’s compact “message spine”
  - only the minimum necessary context for the next stage

## 3) Handoff contracts

### 01 → 02 : Creative brief (structured)

**Input to 01**: user’s raw brief + any provided brand/product/context.

**Output of 01 (and input to 02)**: `CREATIVE_BRIEF` YAML.

```yaml
CREATIVE_BRIEF:
  objective: ""           # what success looks like (awareness/leads/trial/etc)
  product:
    name: ""
    category: ""
    description: ""       # plain-language
    key_benefits: []       # audience-facing
    key_features: []       # optional
    differentiators: []
  audience:
    primary: ""           # who it is for
    pains: []
    desired_outcomes: []
    sophistication_level: ""  # beginner/experienced/technical/etc
  offer:
    primary_cta: ""       # e.g., book demo / start trial
    offer_details: ""     # pricing/trial/lead magnet if any
  brand:
    voice: ""             # adjectives + short guidance
    do: []
    dont: []
  constraints:
    must_include: []
    must_avoid: []
    claims_and_proof:
      allowed_claims: []
      required_caveats: []
  channels_and_assets:
    requested_channels: []     # e.g., landing page, email, LinkedIn
    asset_list: []             # explicit deliverables if known
  seo:
    priority: "none"       # none/light/important
    primary_keyword: ""     # optional
    secondary_keywords: []
  references:
    links_or_notes: []
  assumptions: []
  open_questions: []
```

### 02 → 03 : Angle set (divergent, unscored)

**Output of 02 (and input to 03)**: `ANGLE_SET` YAML.

```yaml
ANGLE_SET:
  angles:
    - angle_name: ""
      one_line_hook: ""
      core_narrative: ""          # 2–5 sentences
      audience_insight: ""         # what we’re betting is true
      promise: ""                  # what they get
      proof_points: []             # bullets, concrete
      tone: ""                     # how it should feel
      tagline_options: []          # short, punchy
      headline_or_subject_seeds: []# a few starting lines
      cta_direction: ""            # what action we’re moving toward
      risk_notes: []               # credibility, compliance, backlash
  notes:
    gaps_or_questions: []
```

**What must NOT appear**: scores, rankings, “best” labels, SEO placement rules, template slot-filling.

### 03 → 04 : Message spine (coherence carrier)

**Output of 03 (and input to 04)**: `MESSAGE_SPINE` YAML.

```yaml
MESSAGE_SPINE:
  chosen_angle: ""                 # angle_name
  positioning_statement: ""         # 1–2 sentences
  narrative_arc:
    setup: ""                      # current pain/context
    tension: ""                    # why it matters now
    resolution: ""                 # product as enabling path
  key_messages: []                  # audience-facing, benefit-led
  proof_points: []                  # concrete support
  objections_and_answers:            # compact
    - objection: ""
      answer: ""
  voice_and_style:
    tone_adjectives: []
    vocabulary_to_use: []
    vocabulary_to_avoid: []
    do: []
    dont: []
  calls_to_action:
    primary: ""
    secondary: ""                  # optional
  seo:
    priority: "none"               # none/light/important
    primary_keyword: ""
    secondary_keywords: []
    "do_not":
      - "Avoid awkward repetition / keyword stuffing"
  channel_plan:
    - channel: ""                  # e.g., landing_page, email, linkedin
      goal: ""                     # what this asset must achieve
      key_points: []
      cta: ""                      # may differ per channel
      compliance_notes: []
```

**What gets dropped here**: unused angles’ prose, ideation chatter, long evaluations.

### 04 → 05 : Draft assets (full copy)

**Output of 04 (and input to 05)**: `DRAFT_ASSETS` Markdown.

Requirements:
- One clear section per asset.
- Keep channel boundaries explicit.
- No internal commentary inside the copy.

### 05 : Final assets + QA notes

**Output of 05**: `FINAL_ASSETS` Markdown plus:
- `CHANGELOG` (bullet list of meaningful edits)
- `RISK_FLAGS` (only if something conflicts with constraints or needs human confirmation)
