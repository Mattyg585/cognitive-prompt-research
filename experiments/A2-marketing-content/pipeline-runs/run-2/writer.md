# Your Catch-Up Meetings Exist Because Your Tools Failed

It's Monday morning. You open Slack at 7am with coffee and dread in roughly equal measure. Three timezones were awake while you slept. You scroll backwards through channels — engineering, platform, incidents, the thread someone inexplicably started in #random — piecing together what happened, what was decided, and what's now on fire. Forty-five minutes later you have a rough picture. You put it in your own words at the 9am standup so your team doesn't have to do the same archaeology. You've done this every day for two years. You barely notice it anymore.

But here's the thing: that work has a name, even if nobody uses it. You're doing context reconstruction. You're being a human router, turning raw scrollback into something your team can act on. You're not managing — you're translating. And the meeting you run at 9am? It doesn't exist because your team needs to talk. It exists because information doesn't arrive in a usable shape.

Every async tool you've tried solves one piece of this. Notion holds docs but can't tell you what changed overnight. Loom lets someone record an explanation, but you get a forty-minute video and no way to know which four minutes matter. Slack threads capture conversation but present it as a chronological stream — which is exactly the wrong format for someone arriving eight hours late. The integration burden — stitching all of this into a coherent picture — falls on people. Usually you. The engineering manager becomes middleware.

This is why "async-first" has been a lie in practice, even when teams believe in it in principle. The tools are synchronous tools with async features bolted on. They generate information. They don't structure it for the person who wasn't there.

Relay is built around a different assumption: the person reading wasn't there when it happened, and the tool's job is to make that fine.

The core mechanism is timezone-aware threads. When your Taipei team finishes a design discussion at 3am your time, the thread doesn't just sit there waiting for you to scroll back and reconstruct. It restructures itself into a narrative for you — what was discussed, what was decided, what's still open — surfaced when you come online. You don't read the raw conversation unless you want to. The catch-up has already happened before you sit down.

Decision logs work the same way. When someone chooses Postgres over DynamoDB at midnight, the decision captures the alternatives they weighed, the reasoning, and who was involved. Three months later, when a new hire asks "why Postgres?" the answer exists in context, not in someone's memory.

Video updates are capped at two minutes. That constraint is the feature. A two-minute update with an auto-generated transcript and summary, attached to the relevant thread, replaces the hour-long recording that four people meant to watch and nobody did.

"We stopped having catch-up meetings."

That's a VP of Engineering at a 120-person company, eight months into the beta. She paused before finishing the thought.

"The catch-up just... happens."

Relay has been in private beta with 200 teams. The numbers are worth sitting with.

73% daily active usage. The industry average for collaboration tools is around 40%. That gap isn't about feature quality — it's about whether the tool fits into how people already work or whether it creates new work. Tools that get 40% adoption are the ones people use when they have to. Tools that get 73% are the ones people open first.

35% fewer meetings across those 200 teams. Not fewer "unnecessary" meetings — fewer meetings, full stop. The ones that disappeared were the ones that existed only to redistribute context.

NPS of 67. And when asked what they valued most, 80% of beta users named the same feature: timezone-aware threads. Not the video snippets. Not the async standups. The thing that eliminated the morning scroll.

Now picture tomorrow morning.

You open Relay instead. Your Taipei team's overnight work is already structured — you see what moved, what was decided, why, and what needs your input. It took ninety seconds to read. Nobody stayed up late to write a handoff doc. Nobody scheduled a bridge call. The context just arrived, in a shape you can use, because the tool did the work that used to be your job.

Your 9am standup is twelve minutes instead of thirty. Half of what you used to cover out loud is already visible. The meeting is for the things that actually need a conversation — the ambiguous stuff, the human stuff. Everything else already happened.

This isn't a vision for someday. This is what 200 teams have been doing for the past eight months.

Relay's free tier supports up to five users. Enough for your team. Enough to see whether next Monday morning feels different from this one.

Try it for a week. If your catch-up meeting survives, nothing lost. If it doesn't — you just got forty-five minutes back.

---

**Meta description:** Your catch-up meetings exist because context doesn't arrive structured. Relay fixes the morning — 200 beta teams already dropped 35% of their meetings.
