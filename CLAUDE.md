# CLAUDE Guide

This file is the Claude Code companion to this repository's `AGENTS.md`.

It should stay semantically aligned with:

- `AGENTS.md`
- `COMMUNICATION.md`
- `schemas/AGENTS.md`
- `schemas/ingest.md`
- `schemas/query.md`
- `schemas/lint.md`

If this file and `AGENTS.md` ever diverge, treat the schema files as the deeper source of truth and update both entry-point files.

## Repository Purpose

This repository is a local markdown knowledge base with two distinct evidence streams:

1. External materials about the world.
2. Personal materials that reveal recurring judgment patterns.

The goal is to maintain both without collapsing them into one undifferentiated wiki.

## Default Behavior

For repository-related questions, use the local knowledge base as the default evidence anchor. Web search is allowed when it improves freshness, correctness, or completeness.

That means:

- read `wiki/index.md` first
- read `COMMUNICATION.md` for writing and interaction style
- answer from `wiki/` before reading `raw/`
- use `raw/` only when the maintained wiki is incomplete
- use web search as a supplement when it materially improves the answer
- do not produce a purely web-derived answer unless local material is absent and external information is necessary
- when external evidence is used, identify the local contribution, the local gap, and the externally supported claims

## Repository Map

- `raw/external/`: immutable outside sources
- `raw/personal/`: immutable personal records
- `wiki/knowledge/`: maintained world knowledge
- `wiki/self/`: maintained personal judgment pages
- `wiki/bridges/`: analyses combining the two
- `wiki/index.md`: top-level map
- `wiki/log.md`: append-only activity log

## Wiki Language Policy

All maintained pages under `wiki/` should default to Chinese.

This applies to:

- `wiki/index.md`
- `wiki/log.md`
- all new or updated pages in `wiki/knowledge/`
- all new or updated pages in `wiki/self/`
- all new or updated pages in `wiki/bridges/`

Keep file paths, repository names, commands, code identifiers, and unavoidable technical terms in their original form when that improves clarity.

Do not generate English-first wiki pages unless the user explicitly asks for bilingual or English output.

## Primary Duties

The agent has four jobs:

1. Ingest new source material.
2. Update the wiki incrementally.
3. Answer queries using the right layer.
4. Keep the wiki navigable and internally consistent.

## Local Workflow Skills

Use local skills when the task matches:

- `skills/kb-ops/` as the top-level maintenance entry point
- `skills/kb-query/` as the knowledge-base-anchored query entry point
- `skills/research-ingest/` for external-source compilation
- `skills/self-distill/` for personal-source distillation
- `skills/bridge-write/` for mixed analyses and essays

## Layer Boundaries

- Treat files in `raw/` as source evidence.
- Do not rewrite source content in `raw/` unless explicitly asked.
- Put world-facing claims in `wiki/knowledge/`.
- Put recurring user judgment patterns in `wiki/self/`.
- Put mixed analyses in `wiki/bridges/`.

Do not store personal axioms inside `wiki/knowledge/`.
Do not store outside factual summaries inside `wiki/self/`.

## Query Routing

Route questions by type:

- factual or topic questions -> read `wiki/knowledge/` first
- self-modeling questions -> read `wiki/self/` first
- advisory or evaluative questions -> combine `wiki/knowledge/` and `wiki/self/`, then write to `wiki/bridges/` if the result has lasting value

When answering locally from the repository:

- begin by listing the local pages or files actually consulted
- prefer maintained wiki pages over raw materials
- make gaps explicit instead of inventing confidence

## Ingest Rules

When ingesting an external source:

1. Read the source in `raw/external/`.
2. Create or update a relevant page in `wiki/knowledge/`.
3. Link it from existing related pages when appropriate.
4. Append a short note to `wiki/log.md`.

When ingesting a personal source:

1. Read the source in `raw/personal/`.
2. Extract observations before proposing principles.
3. Only promote repeated, stable patterns into higher-level self pages.
4. Append a short note to `wiki/log.md`.

For mixed material:

- preserve the original source in the correct raw folder
- extract world-facing knowledge into `wiki/knowledge/` when durable
- extract recurring judgment into `wiki/self/` only with repeated support
- save integrated interpretation in `wiki/bridges/`

## Stability Standard For Self Pages

Use three levels:

- Observation: one useful signal from one or a few records.
- Pattern: a repeated tendency across time, projects, or contexts.
- Axiom: a stable, high-confidence principle that appears repeatedly and helps explain decisions.

Never create an axiom from a single anecdote.

## Writing Rules

- Prefer updating existing pages over creating duplicate pages.
- Keep pages concise and link-rich.
- Preserve uncertainty instead of smoothing it away.
- Record conflicts instead of silently merging them.

Keep these layers distinct when writing:

- source fact
- inferred pattern
- agent synthesis
- user-specific judgment

## Good Answers Become Assets

If a query produces durable value:

- save factual synthesis under `wiki/knowledge/`, or
- save user-specific analysis under `wiki/bridges/`

Do not let durable work disappear into chat history if it would be useful later.

## Maintenance Checks

During lint or cleanup, check for:

- orphan pages
- duplicate pages
- claims with no visible source basis
- self pages based on weak evidence
- bridge pages that should link back to both knowledge and self pages

## Practical Entry Point

For most operational work in this repository, start by reading:

- `COMMUNICATION.md`
- `schemas/AGENTS.md`
- `schemas/ingest.md`
- `schemas/query.md`
- `schemas/lint.md`

Then use the appropriate local skill or proceed directly if the task is narrow.
