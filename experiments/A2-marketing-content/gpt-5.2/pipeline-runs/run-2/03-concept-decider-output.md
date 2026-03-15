---
model: GPT-5.2
date: 2026-03-15
experiment: A2
tier: pipeline
run: 2
stage: 03-concept-decider
---

```yaml
MESSAGE_SPINE:
  chosen_angle: "The Catch‑Up Just Happens"
  positioning_statement: "Relay is the timezone-aware narrative layer for distributed engineering teams—turning scattered updates into a living storyline of work so alignment survives overnight without defaulting to catch-up meetings."
  narrative_arc:
    setup: "Distributed teams ship across timezones, but context doesn’t—updates splinter across chat, docs, tickets, and video."
    tension: "When someone’s offline, continuity breaks. The next day starts with ‘what did I miss?’ and another meeting to reconstruct decisions and progress."
    resolution: "Relay keeps a shared, searchable narrative of what changed, why it changed, and what’s next—delivered when you’re online—so the catch-up happens automatically and meetings become optional."
  key_messages:
    - "Continuity beats volume: teams don’t lack updates—they lack a single thread of context across timezones."
    - "Relay turns day-to-day work into a narrative (what/why/next), not a notification storm."
    - "Timezone-aware threads surface the right context when you’re available."
    - "Shared clarity reduces ‘reconstruction’ work and unnecessary sync rituals."
    - "Works alongside your existing tools—Relay is connective tissue, not a forced rip-and-replace."
  proof_points:
    - "Private beta (~8 months) with 200 teams"
    - "Beta-reported average: 35% meeting reduction"
    - "Beta-reported: 73% daily active usage"
    - "Beta-reported: NPS 67"
    - "Customer quote (beta): ‘We stopped having catch-up meetings. The catch-up just... happens.’ (VP Eng, 120-person company)"
    - "Most-loved feature: timezone-aware threads (mentioned in 80% of feedback)"
  objections_and_answers:
    - objection: "Isn’t this just another tool to check?"
      answer: "It’s designed to reduce tool-hopping by turning existing work signals into one storyline of context—so you spend less time hunting and more time shipping."
    - objection: "Will this replace Slack/Notion/Linear/Loom?"
      answer: "No—Relay is meant to complement your stack by preserving continuity across it, without asking you to abandon the tools you already use."
    - objection: "Do I have to write more updates?"
      answer: "The goal is fewer, higher-signal updates: capture what changed, why, and what’s next once—then let the narrative carry it forward for people who were offline."
    - objection: "Those results sound too good—are they guaranteed?"
      answer: "They’re beta-reported averages from early teams, not promises. The reliable outcome is better continuity and less reconstruction—meeting reduction is a common downstream effect."
  voice_and_style:
    tone_adjectives:
      - "direct"
      - "empathetic"
      - "lightly witty"
      - "clear"
    vocabulary_to_use:
      - "catch-up"
      - "continuity"
      - "narrative"
      - "storyline"
      - "context"
      - "timezone-aware"
      - "async-first"
      - "shared clarity"
    vocabulary_to_avoid:
      - "guarantee"
      - "10x"
      - "revolutionary"
      - "disrupt"
      - "replace (as a primary claim)"
      - "AI-first (unless explicitly required elsewhere)"
    do:
      - "Name the pain plainly (reconstructing context, ‘what did I miss?’)."
      - "Use the beta quote as the emotional anchor when appropriate."
      - "Frame metrics as ‘beta-reported’ and ‘average’ with context."
      - "Keep it human—distributed work is social debt, not just process."
    dont:
      - "Promise to eliminate all meetings."
      - "Dunk on other tools; focus on design assumptions and outcomes."
      - "Over-rotate into productivity moralizing."
  calls_to_action:
    primary: "Start a free trial (Free tier up to 5 users)."
    secondary: "Book a demo for your team."
  seo:
    priority: "none"
    primary_keyword: ""
    secondary_keywords: []
    do_not:
      - "Avoid awkward repetition / keyword stuffing"
  channel_plan:
    - channel: "Landing page"
      goal: "Convert interested leaders with a crisp promise + credible proof."
      key_points:
        - "Problem: context expires overnight; teams pay for it with meetings."
        - "Promise: a living narrative of work (what/why/next) across timezones."
        - "How it works (high level): timezone-aware threads + searchable storyline."
        - "Proof: beta quote + beta-reported metrics (with careful framing)."
        - "Reassurance: complements existing tools; no rip-and-replace."
      cta: "Start a free trial (Free tier up to 5 users)."
      compliance_notes:
        - "Frame 35% as beta-reported average; no guarantees."
        - "Avoid ‘replaces Slack/Notion/Linear/Loom’ language."
    - channel: "Email (launch announcement)"
      goal: "Drive warm traffic to the landing page with a memorable hook."
      key_points:
        - "Subject/headline: ‘The catch-up just happens.’"
        - "One-paragraph story: ‘what did I miss?’ → narrative instead of meetings."
        - "Two bullets: continuity + timezone-aware context."
        - "One proof line: beta quote or one metric (not a pile)."
      cta: "Start free trial"
      compliance_notes:
        - "Don’t stack multiple stats; keep claims modest."
    - channel: "LinkedIn post (founder/PM voice)"
      goal: "Earn attention from Eng leaders and start conversations about async continuity."
      key_points:
        - "Observation: catch-up meetings exist because context is fragmented."
        - "Reframe: teams need continuity, not more updates."
        - "What we built: a narrative of work that updates itself across timezones."
        - "Soft proof: beta quote."
      cta: "Try Relay (free tier up to 5 users)"
      compliance_notes:
        - "Avoid ‘meetings are bad’ framing; position as distributed constraint."
    - channel: "Short social (X / Threads)"
      goal: "Deliver the hook + one clear benefit; push to link."
      key_points:
        - "Hook line: ‘We stopped having catch-up meetings. The catch-up just… happens.’"
        - "One benefit: searchable storyline of work across timezones."
        - "One differentiator: narrative > notifications."
      cta: "Start free trial"
      compliance_notes:
        - "Attribute quote as beta customer; don’t imply universal outcome."
```