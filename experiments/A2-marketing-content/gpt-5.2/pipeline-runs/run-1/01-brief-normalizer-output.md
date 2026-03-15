---
model: GPT-5.2
date: 2026-03-15
experiment: A2
tier: pipeline
run: 1
stage: 01-brief-normalizer
---

```yaml
CREATIVE_BRIEF:
  objective: "Announce Relay’s public launch and drive signups for the free trial/free tier."
  product:
    name: "Relay"
    category: "Async-first collaboration workspace for distributed engineering teams"
    description: "A collaborative workspace that combines docs + issue/work tracking + async updates (including short video snippets) built for teams working across multiple timezones."
    key_benefits:
      - "Fewer catch-up meetings and less context loss across timezones"
      - "Clearer decisions and accountability via decision logs"
      - "Less notification fatigue; better deep work protection"
      - "Faster alignment through structured async standups and narrative summaries"
    key_features:
      - "Timezone-aware threads that surface context as a narrative"
      - "Decision logs capturing context, alternatives, and participants"
      - "2-minute video snippets with transcripts + auto-summaries attached to threads"
      - "Async standups that compile into an ongoing team pulse"
      - "Configurable focus windows with batched/summarised notifications"
    differentiators:
      - "Built async-first from the ground up (not retrofitted onto chat)"
      - "Context surfacing + summarisation designed for ‘what happened while you slept’ workflows"
      - "Explicit decision reasoning capture for cross-timezone understanding"
  audience:
    primary: "Engineering managers and tech leads at 50–500 person companies with teams distributed across 3+ timezones"
    pains:
      - "Meeting overload and ‘catch-up’ fatigue"
      - "Notification noise and fragmented context across tools"
      - "Decisions made in one timezone without shared reasoning"
      - "Async updates scattered across docs, tickets, chat, and long recordings"
      - "Difficulty protecting maker time"
    desired_outcomes:
      - "Reduce meetings without losing alignment"
      - "Make progress visible across timezones"
      - "Preserve decision context and rationale"
      - "Improve focus and throughput for makers"
    sophistication_level: "High (experienced technical leaders; expects concrete specifics and credible proof)"
  offer:
    primary_cta: "Start free trial"
    offer_details: "Free tier up to 5 users; Pro is $12/user/month; Enterprise is custom."
  brand:
    voice: "Direct, confident, empathetic; slightly witty when it fits; not corporate and not combative toward competitors."
    do:
      - "Explain like to a smart friend"
      - "Lead with the distributed-team pain and show you understand it"
      - "Use concrete examples of cross-timezone workflows"
      - "Be confident without dunking on other tools"
    dont:
      - "Overhype or make unverifiable performance claims"
      - "Sound like enterprise marketing copy"
      - "Turn it into a competitor takedown"
      - "Force jokes"
  constraints:
    must_include:
      - "Primary keyword: async collaboration platform"
      - "Secondary keywords: distributed teams, timezone collaboration, async-first"
      - "Include beta proof points (DAU, NPS, meeting reduction) if permitted"
      - "Include the beta quote if permitted"
      - "CTA: Start free trial"
      - "Target length ~1200–1500 words"
    must_avoid:
      - "Inventing features, customers, or outcomes not provided"
      - "Unqualified superlatives (e.g., ‘best’, ‘#1’)"
      - "Direct negative comparisons to specific competitors"
    claims_and_proof:
      allowed_claims:
        - "Private beta with 200 teams"
        - "73% daily active usage in beta"
        - "NPS 67 in beta"
        - "Average 35% meeting reduction (self-reported by beta teams)"
        - "Timezone-aware threads cited as most-loved feature in ~80% of feedback"
      required_caveats:
        - "Beta metrics are from private beta and may be self-reported/representative"
        - "Avoid implying guaranteed results for all teams"
  channels_and_assets:
    requested_channels:
      - "Company blog (hero launch post)"
    asset_list:
      - "Launch blog post (~1200–1500 words)"
  seo:
    priority: "high"
    primary_keyword: "async collaboration platform"
    secondary_keywords:
      - "distributed teams"
      - "timezone collaboration"
      - "async-first"
  references:
    links_or_notes:
      - "Company: Threadline (Series A, ~40 employees, founded 2024)"
      - "Competitors/alternatives: Notion, Linear, Slack, Loom, Confluence"
      - "Quote (VP Eng, 120-person company): ‘We stopped having catch-up meetings. The catch-up just... happens.’"
      - "Launch context: public launch after ~8 months private beta"
  assumptions:
    - "The post’s primary goal is signups (not press coverage) since CTA is ‘Start free trial’."
    - "Use ‘free trial’ phrasing while also clarifying there is a free tier (up to 5 users)."
    - "No strict legal review requirements were provided; treat claims cautiously and attribute to beta."
  open_questions:
    - "What is the public launch date/time and does it need to be mentioned explicitly?"
    - "Any preferred product positioning line (e.g., ‘Notion meets Linear meets Loom’) to include or avoid?"
    - "Are there approved brand style guidelines (capitalisation, terminology, tone boundaries)?"
    - "Can we include the beta quote and the specific beta metrics publicly? If yes, any source/footnote format?"
    - "Do we want to include screenshots, diagrams, or a short product video in the post?"
    - "Any required legal disclaimers for metrics (e.g., ‘results may vary’), and any claims we must not make?"
    - "Are there specific signup URLs/UTM parameters to use for the CTA?"
```