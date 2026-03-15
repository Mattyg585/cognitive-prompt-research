---
model: GPT-5.2
date: 2026-03-15
experiment: A2
tier: pipeline
run: 1
stage: 03-concept-decider
---

```yaml
MESSAGE_SPINE:
  chosen_angle: "The Catch-Up Just Happens"
  positioning_statement: "Relay is an async-first collaboration workspace for distributed engineering teams that turns cross-timezone work into a clear, shareable narrative—so you can wake up and know what moved forward without a catch-up meeting."
  narrative_arc:
    setup: "Distributed teams keep shipping across timezones—but context doesn’t travel with the work."
    tension: "People come online to a scrollback of chat, scattered docs, and half-missing decisions, so alignment turns into recurring catch-up meetings."
    resolution: "Relay surfaces a durable narrative of what happened and what needs you next, making handoffs clean and meetings optional—not mandatory."
  key_messages:
    - "Async shouldn’t mean ‘more to read later’—it should mean you come online to clarity."
    - "Relay organizes cross-timezone progress into a narrative: what changed, why it changed, and what’s next."
    - "Reduce context loss so fewer meetings exist just to reconstruct what happened."
    - "Handoffs are a workflow in Relay (threads + decision context), not a hope and a ping."
    - "Start small: one team/project can try Relay on the free tier (up to 5 users)."
  proof_points:
    - "Private beta with 200 teams (early traction signal)."
    - "73% daily active usage in beta."
    - "NPS 67 in beta."
    - "Average 35% meeting reduction (self-reported by beta teams; not guaranteed)."
    - "Customer voice: ‘We stopped having catch-up meetings. The catch-up just... happens.’ (VP Eng, 120-person company)."
  objections_and_answers:
    - objection: "Is this just another chat tool or ‘AI summary’ layer?"
      answer: "No—Relay is built async-first around durable threads and decision context. Summaries help, but the product’s core is structured, navigable narrative that stays attached to the work."
    - objection: "Will this replace Slack/Linear/Notion overnight?"
      answer: "It doesn’t have to. Start with one project/team and use Relay to reduce the seams where context gets lost; expand only if it fits your workflow."
    - objection: "Are auto-summaries accurate enough to trust?"
      answer: "Treat summaries as a fast on-ramp, not a source of truth. Relay keeps the underlying context (thread history, decisions, links) so you can verify quickly when it matters."
    - objection: "Does this feel like surveillance or status theater?"
      answer: "Relay is designed for shared awareness, not micromanagement: focus on what changed/what’s blocked/what needs attention—without requiring everyone to be online at the same time."
  voice_and_style:
    tone_adjectives:
      - "direct"
      - "empathetic"
      - "clear"
      - "slightly witty"
      - "engineering-minded"
    vocabulary_to_use:
      - "handoff"
      - "narrative"
      - "context"
      - "decision reasoning"
      - "signal over noise"
      - "wake up to clarity"
      - "async-first"
      - "cross-timezone"
    vocabulary_to_avoid:
      - "10x"
      - "guaranteed ROI"
      - "magic"
      - "fully automated"
      - "replace everything"
      - "no meetings ever"
    do:
      - "Name the concrete pain: reconstructing ‘what happened’ after you were offline."
      - "Use vivid, believable examples (handoff moments, shift changes, scrollback)."
      - "Keep claims measurable or clearly framed as qualitative; caveat beta/self-reported metrics."
      - "Emphasize ‘optional meetings’ and ‘clean handoffs’ rather than absolutist promises."
    dont:
      - "Don’t frame competitors as villains or call out specific tools negatively."
      - "Don’t imply perfect summaries or guaranteed meeting reduction."
      - "Don’t drift into feature laundry lists—keep it anchored on handoffs and narrative clarity."
  calls_to_action:
    primary: "Start free trial (free tier up to 5 users)."
    secondary: "See a 2-minute walkthrough of the ‘wake up to a narrative’ workflow."
  seo:
    priority: "none"
    primary_keyword: ""
    secondary_keywords: []
    do_not:
      - "Avoid awkward repetition / keyword stuffing"
  channel_plan:
    - channel: "Landing page"
      goal: "Make the promise instantly legible and credible; convert to trial."
      key_points:
        - "Hero: ‘The catch-up just happens.’ + one-sentence explanation (wake up to a narrative)."
        - "Problem section: scrollback, scattered decisions, timezone handoff gaps."
        - "How it works: narrative threads + decision context + what-needs-you-next."
        - "Proof: beta adoption signals; meeting-reduction caveat."
        - "CTA: free tier up to 5 users."
      cta: "Start free trial"
      compliance_notes:
        - "Meeting reduction is self-reported from private beta; avoid guarantee language."
        - "Describe summaries as helpful, not perfect or exhaustive."
        - "Backup angle: Decision Memory (Not Just Decision Logging)."
    - channel: "Launch email"
      goal: "Create recognition (‘this is our pain’) and drive first-session activation."
      key_points:
        - "Open with the moment: coming online after others shipped/decided."
        - "Promise: a narrative of what moved + what needs you next."
        - "One short customer quote + one adoption metric (optional)."
        - "Close with ‘try it with one project this week’ framing."
      cta: "Start free trial (free tier up to 5 users)"
      compliance_notes:
        - "If metrics are included, add ‘private beta’ context and avoid causal claims."
    - channel: "LinkedIn post (founder/PM)"
      goal: "Earn shares via clarity and a differentiated POV on async."
      key_points:
        - "POV: ‘Async shouldn’t mean more messages to read later.’"
        - "Describe the handoff problem (not ‘remote work’ broadly)."
        - "Introduce Relay as ‘wake up to a narrative’ workflow."
        - "Invite teams to try it; keep tone grounded and non-hype."
      cta: "Try Relay (start free trial)"
      compliance_notes:
        - "Avoid competitor mentions; focus on the architecture/outcome."
    - channel: "Short social (X/Bluesky)"
      goal: "Punchy hook + click."
      key_points:
        - "Hook: ‘The catch-up meeting is a symptom.’"
        - "One-line value: ‘Wake up to what changed + what needs you next.’"
        - "CTA + free tier mention."
      cta: "Start free trial"
      compliance_notes:
        - "Keep claims qualitative; no hard % unless clearly caveated."
```
