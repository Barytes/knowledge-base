# Repository AGENTS Guide

This repository is a local knowledge base. For repository-related questions, the default mode is local-first and local-only unless the user explicitly asks for web search.

## Default Behavior

- Read `COMMUNICATION.md` for writing and interaction style.
- Read `wiki/index.md` first.
- Answer from `wiki/` before reading `raw/`.
- Use `raw/` only when the maintained wiki is incomplete.
- Do not browse the web for repository questions unless the user explicitly asks to search online.
- If the local knowledge base is insufficient, say what is missing instead of silently switching to web search.

## Repository Layers

- `raw/`: source evidence
- `wiki/knowledge/`: maintained world knowledge
- `wiki/self/`: maintained personal judgment patterns
- `wiki/frameworks/`: compact judgment frameworks and query routing surfaces
- `wiki/bridges/`: applied analyses that combine the two

## Wiki Language Policy

- All maintained wiki pages under `wiki/` should default to Chinese.
- This includes `wiki/index.md`, `wiki/log.md`, and new or updated pages in `wiki/knowledge/`, `wiki/self/`, `wiki/frameworks/`, and `wiki/bridges/`.
- Keep file paths, repository names, commands, code identifiers, and unavoidable technical terms in their original form when helpful.
- Do not create new English-first wiki pages unless the user explicitly asks for bilingual or English output.

## Query Rules

- Factual repository questions: use `wiki/knowledge/`
- Questions about recurring user preferences or judgment: use `wiki/self/`
- Reusable judgment frameworks, router pages, and compact entry surfaces: use `wiki/frameworks/`
- For design, evaluation, comparison, and decision questions, read `wiki/frameworks/router.md` first, then the most relevant framework page, then the relevant `wiki/knowledge/` and `wiki/bridges/` pages when needed
- Advisory questions: combine the needed layers through `wiki/bridges/` only when a concrete applied analysis is warranted

## Operational Rules

- For maintenance workflows, use `skills/kb-ops/`.
- For local-only question answering, use `skills/kb-query/`.
- For detailed repository policy, read:
  - `COMMUNICATION.md`
  - `schemas/AGENTS.md`
  - `schemas/ingest.md`
  - `schemas/query.md`
  - `schemas/lint.md`