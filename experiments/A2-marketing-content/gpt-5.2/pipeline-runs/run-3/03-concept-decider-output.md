---
model: GPT-5.2
date: 2026-03-15
experiment: A2
tier: pipeline
run: 3
stage: 03-concept-decider
---

```yaml
MESSAGE_SPINE:
  chosen_angle: "The catch-up that happens while you sleep"
  positioning_statement: "Relay by Threadline is the async context layer for distributed engineering teams—turning the last 12 hours of work into a clear, timezone-aware narrative so everyone starts their day oriented without adding another meeting."
  narrative_arc:
    setup: "In multi-timezone teams, momentum gets lost overnight—updates scatter across tools, and each day starts with ‘what did I miss?’"
    tension: "Catch-up becomes a hidden tax: extra meetings, notification walls, and repeated context for the people who weren’t awake."
    resolution: "Relay stitches async work into a structured story—what changed, why it matters, and what decisions were made—so the team can move forward calmly, without forcing sync time."
  key_messages:
    - "Replace the daily ‘what did I miss?’ tax with a calm, structured catch-up."
    - "Async alignment works when context travels: what changed, why it matters, and what’s next."
    - "Timezone-aware narratives keep everyone oriented—without punishing people who were offline."
    - "A narrative, not a notification wall: fewer pings, clearer priorities."
    - "Designed for engineering teams that span 3+ timezones and need durable clarity."
  proof_points:
    - "Private beta: ~200 teams."
    - "Beta metrics: 73% daily active usage; NPS 67."
    - "Most-loved beta feature: timezone-aware threads (80% of feedback mentions)."
    - "Position benefits as reducing catch-up burden (not eliminating meetings universally)."
  objections_and_answers:
    - objection: "We already have Slack + docs + tickets—why another tool?"
      answer: "Relay isn’t another place to post updates; it’s the context layer that turns scattered async activity into a readable narrative (what changed, why it matters, what’s next) so teams spend less time reconnecting the dots."
    - objection: "Will this replace our meetings?"
      answer: "Relay is built to reduce catch-up and recap overhead, not to eliminate meetings across the board. Teams still sync when it matters—just less often for status and context."
    - objection: "Is the summarization accurate enough?"
      answer: "Treat summaries as helpful defaults and keep the underlying threads as the source of truth—Relay’s job is to make context easier to find and follow, not to invent it."
    - objection: "Will people actually use it consistently?"
      answer: "The promise is low-friction orientation: the output is a story people want to read. In beta, teams showed strong engagement (73% daily active usage)."
  voice_and_style:
    tone_adjectives:
      - "empathetic"
      - "crisp"
      - "calm"
      - "engineering-native"
      - "lightly witty (about the ‘catch-up tax’)"
    vocabulary_to_use:
      - "catch-up tax"
      - "context"
      - "narrative"
      - "timezone-aware"
      - "async alignment"
      - "orientation"
      - "what changed / why it matters / what’s next"
    vocabulary_to_avoid:
      - "eliminate meetings"
      - "guaranteed productivity"
      - "magic"
      - "AI will solve"
      - "revolutionary"
    do:
      - "Lead with the pain: lost continuity across timezones."
      - "Be concrete about the artifact: a story of the last 12 hours."
      - "Use metrics with attribution to beta (measured vs self-reported)."
      - "Respect engineer autonomy and offline time."
    dont:
      - "Overpromise outcomes or imply causality beyond what’s stated."
      - "Snark at meetings or other tools; keep it about the problem."
      - "Write long evaluations—keep copy-ready guidance only."
  calls_to_action:
    primary: "Start a free trial"
    secondary: "See how Relay turns the last 12 hours into a narrative"
  seo:
    priority: "none"
    primary_keyword: ""
    secondary_keywords: []
    do_not:
      - "Avoid awkward repetition / keyword stuffing"
  channel_plan:
    - channel: "Landing page"
      goal: "Make the value instantly legible for multi-timezone engineering leads; drive trial."
      key_points:
        - "Headline/hero: end the ‘what did I miss?’ tax with a catch-up that writes itself."
        - "Show the artifact: a timezone-aware story (what changed, why it matters, what’s next)."
        - "Proof: beta traction + favorite feature; caveat where needed."
        - "How it works: threads → narrative; decision context travels."
        - "CTA above the fold + repeated at key sections."
      cta: "Start a free trial"
      compliance_notes:
        - "Avoid implying Relay eliminates meetings universally; position as reducing catch-up burden."
        - "If mentioning meeting reduction outcomes, label as beta self-reported and not guaranteed. Backup angle: Decision-making with receipts."
    - channel: "Email"
      goal: "Hook with a relatable overnight context gap; get clicks to try."
      key_points:
        - "Subject hooks around ‘what did I miss?’ and ‘wake up to context.’"
        - "Short story: last 12 hours → readable narrative."
        - "One proof point + one concrete feature (timezone-aware threads)."
        - "Invite: try it on one project for one week."
      cta: "Start a free trial"
      compliance_notes:
        - "Keep tone lightly witty, never snarky."
        - "Numbers must be precise and attributed to beta."
    - channel: "Social"
      goal: "Earn attention with a sharp insight; drive curiosity and clicks."
      key_points:
        - "Punchy framing: ‘The real cost of distributed teams is the catch-up tax.’"
        - "Before/after: notification wall → narrative."
        - "Simple promise: start your day oriented, without another meeting."
        - "One metric or ‘200 beta teams’ line for credibility."
      cta: "Try Relay free"
      compliance_notes:
        - "Avoid absolute claims; keep benefits framed as ‘reduce’ / ‘make it easier.’"
```
