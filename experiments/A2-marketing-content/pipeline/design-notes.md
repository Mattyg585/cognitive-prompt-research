# Pipeline Design Notes

## Why a pipeline

The architect identified five interference patterns in the original prompt, all stemming from one structural problem: **generation + evaluation + template-filling in a single context**. The evaluation posture dominates because it's more convergent and concrete than the generative intent, suppressing voice, creative structure, and reader engagement.

A Tier 2 revision (scope boundaries within a single prompt) can reduce this interference by sequencing understand → write → polish phases. But scope boundaries are unreliable for fundamental mode conflicts — the evaluation criteria are still in the context during generation, even if the prompt says "ignore them for now." The model has to actively suppress patterns it's already activated.

A pipeline with clean contexts eliminates this entirely. The writer never sees evaluation criteria. The explorer never sees templates. Each agent works in a context that only contains what supports its cognitive posture.

## Why four agents (not three, not five)

**Why not three?** The architect's analysis suggested four stages. I considered combining Brief Explorer + Content Architect into a single "Strategist" agent. But investigation and synthesis are different postures — investigation follows threads openly, synthesis commits to a narrative. Combining them risks premature narrative commitment: the agent starts building a story before it's finished exploring. Keeping them separate means the explorer can follow surprising threads without worrying about whether they fit a structure yet.

**Why not five?** I considered splitting the Editor into "SEO Specialist" and "Voice Editor." But evaluation + evaluation is a compatible combination — both are convergent, criteria-referenced work. Splitting them adds orchestration overhead without resolving any mode interference. The editor can check SEO placement and then verify voice preservation in the same pass. The key protection is already in place: the editor explicitly prioritizes voice preservation over SEO compliance when they conflict.

## The rhythm

```
Brief Explorer → Content Architect → Writer → Editor
  (diverge)       (converge)         (diverge)  (converge)
```

This is the compression-expansion rhythm that the cognitive stance reference identifies as the healthiest pipeline pattern:

1. **Diverge**: Explore the brief openly, follow threads, surface what's interesting
2. **Converge**: Compress into a plan — commit to an angle, structure, voice
3. **Diverge**: Write with full creative freedom, invest in voice and flow
4. **Converge**: Polish for SEO, formatting, channel compliance

Each convergent stage chunks material for the next divergent stage. The explorer's observations are chunked into a strategic brief. The architect's decisions are chunked into a content plan. The writer's draft is the material the editor refines. No stage needs to hold everything — each works with what's been compressed for it.

No n-2 repetition costs — each cognitive mode appears exactly once. No mode is abandoned and then returned to.

## Handoff design rationale

### Explorer → Architect
The explorer produces structured observations, not exploratory prose. This is compression built into the output format — the structured brief strips the exploratory cognitive mode. The architect receives observations it can reason over without being pulled into continued exploration.

### Architect → Writer
The architect produces a content plan with clear decisions. This is already convergent output, so it carries minimal mode contamination. The writer also receives the original product brief — for raw data access (quotes, stats, details), not for strategic direction. The brief is source material.

### Writer → Editor
The draft crosses as-is — the writer's prose IS the product. The editor also receives the SEO requirements extracted from the original brief, but passed as a separate structured list, not embedded in the draft's context. This means the editor can check requirements against the draft without the requirements having been present during writing.

**Critical design choice**: the SEO requirements go to the editor, not to the writer. This is the structural separation the original prompt lacked. The writer's context is free of evaluation criteria. The editor's context is free of generative pressure.

## What the original prompt contributed

The domain knowledge in the original prompt isn't wrong — channel awareness, SEO fundamentals, CTA principles, and platform-specific guidance are all valuable. The pipeline redistributes this knowledge:

- **Channel and audience insight** → Brief Explorer (as things to notice, not checklists)
- **Structure and narrative craft** → Content Architect (as decisions to make, not templates to fill)
- **Voice and engagement** → Writer (as generative principles, not evaluation criteria)
- **SEO, formatting, readability** → Editor (as polish criteria, where they belong)

The same knowledge, in the right context, at the right time.

## What to watch for when testing

1. **Explorer output**: Does it surface genuine insights about the product and audience, or does it produce generic observations? The explorer should find things that are specific to this brief — not boilerplate "the audience wants solutions to their problems."

2. **Architect decisions**: Does it commit to a specific angle, or hedge between several? The plan should feel decisive. If it reads like "you could do X or Y," the architect isn't converging.

3. **Writer voice**: This is the primary test. Does the blog post read like someone who understands and is excited about this product? Or does it read like competent marketing copy? The writer's context has no evaluation criteria — if the output is still generic, something else is anchoring it (possibly training data priors for "blog post" format).

4. **Editor preservation**: Does the edited version still sound like the writer wrote it? Or has the SEO integration flattened the voice? The editor prompt explicitly prioritizes voice, but the tension is real — check whether the final piece retains the energy of the draft.

5. **Cross-tier comparison**: The key experiment question is whether the pipeline produces qualitatively different output from the Tier 2 prompt (which uses scope boundaries in a single context). The Tier 2 version should improve over baseline. The pipeline should show whether clean context separation produces a further leap — particularly in voice, creative structure, and reader engagement.
