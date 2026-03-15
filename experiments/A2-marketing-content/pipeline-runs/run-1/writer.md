# Your Async Culture Isn't Failing. Your Tools Are Still Designed for the Same Room.

It's 7am and you're on a call with London. You've been up since 6:30, re-reading a Slack thread that went sideways overnight, trying to reconstruct who decided what and why before anyone asks you to weigh in. By the time the call ends you have forty minutes before your Singapore team goes offline, so you scramble to leave context — a Loom recording you narrate too fast, a Notion doc you half-finish, a Slack message that says "see the Loom." You know nobody will watch the whole thing. You do it anyway, because the alternative is another sync tomorrow.

You've done the reading. You rolled out async standups. You wrote the Slack etiquette guide, pinned it in every channel, watched people ignore it within a week. You tried "no meeting Wednesdays." It lasted a quarter. And somewhere along the way, you started to suspect that maybe async work is a nice idea that doesn't survive contact with a real team spread across nine hours of timezone difference.

That suspicion is wrong. But the frustration behind it is completely legitimate.

## You were blaming the wrong thing

Async didn't fail your team. Your tools failed async.

Look at what's actually in the stack. Slack was built for real-time conversation. The entire UX — the typing indicators, the green dots, the threading model that buries context three clicks deep — assumes you're there right now. Bolting "do not disturb" onto a synchronous messenger doesn't make it async. It makes it a synchronous messenger you feel guilty about ignoring.

Notion is a document store. A good one. But a document sitting in a folder is not collaboration — it's an artifact. Collaboration is the part where your teammate in Berlin reads your thinking, understands the tradeoffs, and builds on it without scheduling a call. Notion can hold that content. It can't shape it.

And Loom. Loom solved one real problem: it let you show instead of tell. But a twenty-minute recording with no structure is a meeting you can't interrupt. Your teammates watch it at 2x, absorb maybe half, and then message you to clarify the part that mattered — which is, of course, the part you rushed through at minute fourteen.

None of these tools are broken. They're just not designed for the world you actually work in. They were built with one assumption baked into every interaction model, every notification pattern, every collaboration surface: that people overlap. That someone is on the other end right now, or will be soon.

The problem was never the method. It was that nobody built the infrastructure for the method to actually work.

## What async-first looks like when you mean it

We built Relay on a single design constraint: assume nobody is in the same room. Ever. Not sometimes, not during overlap hours, not "except for the weekly all-hands." Never. Every feature exists to answer one question — how does this work when the person who needs it is asleep right now?

Timezone-aware threads restructure conversations based on when you read them. You open a thread in the morning and see what happened while you were offline, laid out as a coherent narrative — not two hundred messages you have to scroll through, mentally filtering what's noise and what changed the direction of a project. The context comes to you shaped for comprehension, not just dumped in chronological order.

Decision logs capture the reasoning, not just the outcome. When your Singapore team wakes up and sees that the API approach changed, they don't just see the new plan. They see what was considered, what was rejected, and why. They can engage with the decision instead of just accepting it. That's the difference between a distributed team and a team that distributes its announcements.

Video updates cap at two minutes. That's not a limitation — it's the whole point. Two minutes forces you to know what you're saying before you hit record. The result auto-transcribes and auto-summarizes, and attaches to the thread it belongs to. No separate tool, no "check the Loom," no hunting for the link someone posted in a channel you muted.

And then there's the feature that tells you to stop using the product. Configurable focus windows batch and summarize your notifications so your deep work stays uninterrupted. The tool actively protects your maker time, because an async platform that creates its own urgency has missed the point entirely.

## What actually happened

We spent eight months in private beta with two hundred teams. Here's what we learned.

73% daily active usage. The industry average for collaboration tools is around 40%. That gap matters more than it looks like it does, because it answers the question every engineering manager asks first: will my team actually use this? Nobody mandated Relay in those beta teams. No one made it a policy. Engineers opened it every morning because it was where the context lived. That's not a metric. That's behavior.

Teams reported 35% fewer meetings on average. Do the math on that for a team of ten: it's roughly a full day of deep work per person, per week, that used to evaporate into "syncing up" and "getting everyone on the same page." A full day, every week, returned to the work your team was hired to do.

The feature mentioned in 80% of user feedback was timezone-aware threads. People don't talk about features they tolerate. They talk about features that fixed something they'd given up on fixing.

And then there's the quote that keeps coming back to us, from a VP of Engineering running a 120-person company across four continents:

"We stopped having catch-up meetings. The catch-up just... happens."

That's it. That's the whole thing. The meeting that existed because the tools couldn't do their job — gone. Not replaced with a different process or a better agenda template. Just gone, because the underlying problem stopped existing.

## Try it

Relay is live, starting today. Free for teams of up to five — no trial period, no feature gates on the free tier. If your team is spread across timezones and you're tired of building async culture on top of tools that were designed for a room, see what happens when the tool agrees with you.

[Try Relay free with your team →]

---

**Meta description:** You've tried everything to make async work. The method was never the problem — your tools still assume everyone's online at the same time. Relay was built for the way distributed teams actually work.
