---
name: repo-practice-query
description: Answer focused engineering-practice questions from a studied repository. Use when Codex should start from an existing repo map or architecture note, revisit only the necessary repository evidence, extract portable patterns, and write durable findings back into the relevant `wiki/topics/` page.
---

# Repo Practice Query

Read these files first:

- `AGENTS.md`
- `schemas/AGENTS.md`
- `schemas/query.md`
- `wiki/topics/agent-harness-runtime/codebases-as-knowledge-sources.md`

Use this skill after a repository has already been mapped, or when a user asks a focused question about a repository's engineering practices.

## Goal

Answer narrow repo questions without re-reading the whole repo every time.

Typical questions:

- how does this repo implement harness engineering
- where are permission gates enforced
- what does this repo use for state handoff between runs
- which practices here are portable to my own project

## Start From The Map

Read in this order:

1. `wiki/index.md`
2. the most relevant maintained repo note in `wiki/topics/`
3. only the anchored raw evidence needed for the question

If no repo map exists yet, either:

- create a minimal one first, or
- hand off to `repo-map-ingest`

Do not jump straight into broad source reading if a maintained map already exists.

## Query Method

Translate the question into mechanisms, not files.

For each mechanism you inspect, answer:

- what the repo does
- why the mechanism exists
- what failure mode it is compensating for
- whether it appears portable or project-specific

Keep these layers separate:

1. observed repo behavior
2. inferred engineering principle
3. recommendation for the user's project

## Preferred Outputs

Choose the write target by stability:

- `wiki/topics/` for descriptive repo facts, cross-repo practice summaries, and “what should we borrow from this repo” style conclusions
- `wiki/self/` only if repeated evidence across projects reveals a stable personal engineering preference

## Good Answer Shape

When useful, structure the answer around:

- what the repo appears to do
- where the evidence lives
- what principle can be extracted
- what remains uncertain

## Guardrails

- Do not restate the repo map if the question is narrower than that.
- Do not treat a single mechanism as a universal best practice.
- Do not promote an implementation detail into a principle without explaining the failure mode it solves.
- If the evidence is thin, say which files or artifacts are still missing.

## Write-Back

If the answer yields a durable clarification, update the maintained repo note and any affected topic pages.

Append a `query` entry to `wiki/log.md` when the result becomes a maintained asset.

Any maintained wiki page written by this skill should default to Chinese.
