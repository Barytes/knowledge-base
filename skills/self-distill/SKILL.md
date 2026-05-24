---
name: self-distill
description: Distill personal materials into observations, patterns, and candidate axioms. Use when Codex needs to read journals, conversations, decision notes, or reflective writing from `raw/personal/`, update `wiki/self/`, and preserve the difference between one-off thoughts and stable judgment.
---

# Self Distill

Read `schemas/AGENTS.md` and `schemas/ingest.md` first. Treat personal sources as evidence about the user's behavior and thinking, not as automatic truth about the user.

## Workflow

1. Read the personal source.
2. Extract concrete observations before making abstractions.
3. Compare those observations with existing self pages.
4. Promote only repeated, stable tendencies into higher-level pages.
5. Append a `reflection` or `lint` entry to `wiki/log.md`.

This skill may also re-read maintained bridge essays as secondary evidence when they expose recurring judgment or expression signals, but raw personal evidence still carries more weight than a polished maintained essay.

## Promotion Ladder

- observation: one signal from one or a few records
- pattern: a tendency that repeats across time, projects, or settings
- axiom: a stable decision principle that explains repeated choices

Never create an axiom from a single anecdote unless the user explicitly asks for a speculative draft.

## Capture

Look for:

- what the user repeatedly prioritizes
- how the user trades off speed, quality, cost, and simplicity
- what triggers approval, skepticism, or rejection
- what appears stable versus situational
- how the user repeatedly frames problems or builds abstractions
- whether there are recurring writing tendencies such as preferred structure, contrast style, or explanation rhythm

## Guardrails

- Keep facts about the world out of `wiki/self/`.
- Do not confuse mood with principle.
- If a piece of writing is really an applied essay about an external topic, save the essay to `wiki/bridges/` and only extract self pages when repeated evidence supports them.
- A single bridge essay can support an `observation`, but not a high-confidence `pattern` or `axiom`.
- Treat writing style as self evidence about expression habits, not as evidence about factual beliefs unless repeated support exists.

## Output

Prefer concise self pages that clearly say whether they are an observation, pattern, or axiom, and what evidence supports that level.

Write maintained self pages in Chinese by default.
