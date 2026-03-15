---
model: GPT-5.2
date: 2026-03-15
experiment: A2
tier: pipeline
run: 3
stage: 01-brief-normalizer
---

```yaml
CREATIVE_BRIEF:
  objective: "Announce Relay’s public launch and drive sign-ups (Start free trial) via a launch blog post that anchors launch-week sharing."
  product:
    name: "Relay"
    category: "Async-first collaboration workspace for distributed engineering teams"
    description: "A collaborative workspace for distributed engineering teams (Notion + Linear + Loom-style capabilities) designed for teams working across multiple timezones."
    key_benefits:
      - "Fewer meetings via async updates and decision context"
      - "Reduced notification overload while keeping everyone aligned"
      - "Shared understanding across timezones (context preserved, not lost)"
      - "More protected deep work time for makers"
    key_features:
      - "Timezone-aware threads (narrative catch-up based on when you’re online)"
      - "Decision logs (context, alternatives, participants)"
      - "2-minute video snippets with transcripts + auto-summaries"
      - "Async standups compiled into a team pulse"
      - "Focus windows with batched/summarised notifications"
    differentiators:
      - "Built async-first from the ground up for multi-timezone teams"
      - "Catch-up presented as structured narrative rather than a notification wall"
      - "Decision-making context captured by default, not as extra work"
  audience:
    primary: "Engineering managers and tech leads at 50–500 person companies with teams distributed across 3+ timezones."
    pains:
      - "Meeting fatigue and constant ‘catch-up’ calls"
      - "Notification overload and fragmented context across tools"
      - "Decisions made in one timezone without context for others"
      - "Long recordings nobody watches; knowledge trapped in sync conversations"
      - "Interrupted deep work from always-on chat"
    desired_outcomes:
      - "Clear async alignment without daily scheduling pain"
      - "Decisions that are understandable later (and across timezones)"
      - "Lower meeting load while staying coordinated"
      - "More predictable focus time and less context switching"
    sophistication_level: "High (experienced with modern collaboration tools and tradeoffs)."
  offer:
    primary_cta: "Start free trial"
    offer_details: "Pricing: Free tier (up to 5 users), Pro ($12/user/month), Enterprise (custom)."
  brand:
    voice: "Direct, confident-but-not-arrogant, empathetic to distributed-team pain; lightly witty when it fits (never forced)."
    do:
      - "Write like explaining to a smart friend"
      - "Lead with empathy for meeting fatigue + notification overload"
      - "Be specific about product mechanics (how it works)"
      - "Use proof points plainly and accurately"
    dont:
      - "Sound corporate or boardroom-y"
      - "Dunk on competitors (Slack/Notion/Linear/etc.)"
      - "Overpromise or imply universal results"
      - "Force jokes or snark"
  constraints:
    must_include:
      - "Product name (Relay) and company name (Threadline)"
      - "Public launch after 8 months of private beta with ~200 teams"
      - "What makes it different (timezone-aware threads, decision logs, video snippets w/ transcripts, async standups, focus windows)"
      - "Relevant beta proof points (DAU 73%, NPS 67, ~35% meeting reduction reported)"
      - "Primary CTA: Start free trial"
      - "Primary SEO keyword: async collaboration platform"
    must_avoid:
      - "Competitor bashing or direct comparisons framed as insults"
      - "Unverifiable claims (e.g., guaranteed meeting reductions)"
      - "Inaccurate stats or invented customer names/logos"
    claims_and_proof:
      allowed_claims:
        - "Private beta: ~200 teams"
        - "73% daily active usage (as measured during beta)"
        - "NPS of 67"
        - "Average meeting reduction of ~35% (reported by beta teams)"
        - "Most-loved feature: timezone-aware threads (80% of feedback mentions)"
        - "Representative quote from beta VP Eng provided in brief"
      required_caveats:
        - "Clearly label figures as beta results and/or self-reported where applicable"
        - "Avoid implying results are typical or guaranteed"
  channels_and_assets:
    requested_channels:
      - "Company blog (hero launch post)"
    asset_list:
      - "Launch announcement blog post (~1200–1500 words)"
      - "Optional: pull-quote snippet(s) suitable for social sharing (derived from post)"
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
      - "Competitors mentioned: Notion, Linear, Slack, Loom, Confluence (positioning: none built async-first from the ground up)"
      - "Beta user quote: \"We stopped having catch-up meetings. The catch-up just... happens.\" (VP Eng, 120-person company)"
  assumptions:
    - "‘Start free trial’ routes to a sign-up flow that at minimum enables the Free tier (up to 5 users)."
    - "The post should be written for engineering leadership readers (not general consumers) and can use light product/process terminology."
  open_questions:
    - "Exact public launch date/timezone and any launch event details?"
    - "Preferred URL for CTA (product page / signup link) and tracking parameters?"
    - "Should pricing be included in the post body, or linked only?"
    - "Any legal/brand guidelines for claims, testimonials, or NPS usage?"
    - "Any customer logos or case studies approved for mention beyond the provided quote?"
    - "Preferred narrative angle: ‘meeting reduction’ vs ‘async narrative catch-up’ vs ‘protect maker time’ as the lead?"
```
