# Knowledge Base Agent Guide

This repository is a local markdown knowledge base with two distinct evidence streams:

1. External materials about the world.
2. Personal materials that reveal the user's recurring judgment patterns.

The agent should help maintain both without collapsing them into one undifferentiated wiki.

Read this file first, then consult the more specific schema for the task:

- `COMMUNICATION.md` for writing and collaboration style
- `schemas/ingest.md` for new materials
- `schemas/query.md` for answering and write-back
- `schemas/lint.md` for cleanup and maintenance

## Repository Map

- `raw/external/`: immutable outside sources
- `raw/personal/`: immutable personal records
- `wiki/topics/`: topic-organized maintained knowledge and applied analysis
- `wiki/self/`: maintained personal judgment pages
- `wiki/frameworks/`: compact judgment frameworks and query routing pages
- `wiki/site/`: generated static HTML browsing view
- `wiki/index.md`: top-level map
- `wiki/log.md`: append-only activity log

## Wiki Language Policy

All maintained pages under `wiki/` should default to Chinese.

This includes:

- `wiki/index.md`
- `wiki/log.md`
- new or updated pages in `wiki/topics/`
- new or updated pages in `wiki/self/`
- new or updated pages in `wiki/frameworks/`

Keep file paths, repository names, commands, code identifiers, and unavoidable technical terms in their original form when helpful.

Do not create English-first wiki pages unless the user explicitly requests bilingual or English output.

## Primary Duties

The agent has four jobs:

1. Ingest new source material.
2. Update the wiki incrementally.
3. Answer queries using the right layer.
4. Keep the wiki navigable and internally consistent.

Use local skills when the task matches:

- `skills/kb-ops/` as the top-level orchestration entry point
- `skills/kb-query/` as the local-only query entry point
- `skills/research-ingest/` for external-source compilation into topic pages
- `skills/self-distill/` for personal-source distillation
- `skills/bridge-write/` for mixed analyses and essays inside `wiki/topics/`
- `skills/framework-distill/` for lifting reusable judgment skeletons from `wiki/topics/` into `wiki/frameworks/`

## Layer Boundaries

- Treat files in `raw/` as source evidence.
- Do not rewrite source content in `raw/` unless explicitly asked.
- Put world-facing claims and mixed applied analysis in the relevant topic under `wiki/topics/`.
- Put recurring user judgment patterns in `wiki/self/`.
- Put reusable judgment frameworks, compact router pages, and high-frequency entry surfaces in `wiki/frameworks/`.

Do not store personal axioms inside `wiki/topics/`.
Do not store outside factual summaries inside `wiki/self/`.
Do not let `wiki/frameworks/` turn into a second topic directory; keep it small and periodically consolidated.

## Query Routing

Route questions by type:

- Factual or topic questions: read `wiki/topics/` first.
- Questions about the user's style, preferences, or recurring judgments: read `wiki/self/` first.
- Design, evaluation, comparison, and decision questions: read `wiki/frameworks/router.md` first, then the most relevant framework page, then pull in `wiki/topics/` as needed.
- Save concrete applied outputs to the relevant `wiki/topics/<topic>/` directory when the result is really an analysis or memo, not merely a reusable router or framework page.

For repository-related questions, default to local-only behavior. Do not browse the web unless the user explicitly requests online search.

## Ingest Rules

When ingesting an external source:

1. Read the source in `raw/external/`.
2. Create or update a relevant page in `wiki/topics/<topic>/`.
3. Link it from existing related pages when appropriate.
4. Append a short note to `wiki/log.md`.

When ingesting a personal source:

1. Read the source in `raw/personal/`.
2. Extract observations before proposing principles.
3. Only promote repeated, stable patterns into higher-level self pages.
4. Append a short note to `wiki/log.md`.

For detailed routing and write targets, follow `schemas/ingest.md`.

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

Use language that distinguishes:

- source fact
- inferred pattern
- agent synthesis
- user-specific judgment

## Good Answers Become Assets

If a query produces durable value:

- save factual synthesis or applied analysis under `wiki/topics/`, or
- save stable user-specific signals under `wiki/self/`, or
- save reusable frameworks and router pages under `wiki/frameworks/`

Do not let durable work disappear into chat history if it would be useful later.

For answer structure and write-back rules, follow `schemas/query.md`.

## Minimum Maintenance

During lint or cleanup, check for:

- orphan pages
- duplicate pages
- claims with no visible source basis
- self pages based on weak evidence
- topic pages that should link back to relevant frameworks or self pages

Use the full maintenance procedure in `schemas/lint.md`.
