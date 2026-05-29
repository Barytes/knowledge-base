---
name: bridge-write
description: Combine maintained topic pages with the user's recurring judgment patterns to produce applied analysis. Use when Codex needs to write recommendations, essays, project briefs, or evaluations that should reflect both `wiki/topics/` and `wiki/self/`, then save the result under the relevant topic in `wiki/topics/`.
---

# Bridge Write

Read `schemas/AGENTS.md` and `schemas/query.md` first. Use this skill when a task is neither purely factual nor purely self-reflective.

## Workflow

1. Read the relevant page or pages in `wiki/topics/`.
2. Read the relevant page or pages in `wiki/self/`.
3. Separate world evidence from user-specific judgment.
4. Synthesize them into an applied analysis.
5. Save durable outputs in the relevant `wiki/topics/<topic>/` directory, using an `essays/` subdirectory only for finished longform essays.
6. Append a `query` entry to `wiki/log.md` when the result becomes a maintained page.

## Answer Shape

When useful, organize the output into:

- what the materials suggest
- what the user's recurring lens suggests
- what follows from combining the two

## Guardrails

- Do not present personal preference as objective fact.
- Do not hide disagreement between sources and user preferences.
- If the task becomes purely factual, keep the output as a topic page under `wiki/topics/`.
- If the task becomes purely self-modeling, move the output toward `wiki/self/`.
- Remember that finished bridge essays may later be re-read as secondary evidence for `wiki/self/`, especially for recurring framing habits or writing tendencies, so keep the user's lens legible instead of flattening it away.

## Typical Outputs

- applied recommendation
- project brief through the user's lens
- topic essay
- comparative judgment
- decision memo

Prefer outputs that can still be reused later as maintained topic pages.

Write maintained topic pages in Chinese by default.
