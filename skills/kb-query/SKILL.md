---
name: kb-query
description: Answer repository questions from the local knowledge base only. Use when Codex needs to answer questions about this repository's topics, pages, or architecture by reading `wiki/` and `raw/` without automatic web search, and by reporting local gaps explicitly when the repository is insufficient.
---

# KB Query

Read these files first:

- `AGENTS.md`
- `schemas/AGENTS.md`
- `schemas/query.md`

Use this skill for repository-related question answering, not for maintenance.

## Default Invocation

If the user input is only `kb-query` or `$kb-query`, interpret it as:

- answer the current repository question from local materials only

## Default Behavior

Treat repository questions as local-only unless the user explicitly asks for web search.

That means:

1. read `wiki/index.md` first
2. for design, evaluation, comparison, or decision questions, read `wiki/frameworks/router.md` first when available
3. then read the most relevant `wiki/frameworks/` page
4. then read the most relevant `wiki/knowledge/` and `wiki/bridges/` pages
5. read `raw/` only if the wiki is incomplete
6. answer from local material
7. if local material is insufficient, say so explicitly and stop

## Answer Order

When useful, answer in this order:

1. consulted local pages
2. what the local wiki already says
3. what can be inferred from local raw material
4. what remains missing

## Required Opening

Before giving the substantive answer, always list the local repository pages or files actually consulted.

Use a compact opening such as:

- `Consulted local pages:`
- one flat list of the specific `wiki/` or `raw/` files read

If only `wiki/index.md` was read before deciding the repository is insufficient, say that explicitly.

## Guardrails

- Do not browse the web by default.
- Do not silently mix repository material with outside search results.
- If the user asks for latest or external information, clearly mark the answer as going beyond the repository.
- If the question is really a maintenance request, hand off to `kb-ops`.
- Do not omit the consulted-pages opening, even for short answers.

## Write-Back

If a local-only answer produces a durable clarification or synthesis, save it back into the right maintained layer and add a `query` log entry.

Prefer:

- `wiki/frameworks/` for reusable judgment frameworks, router pages, and compact entry surfaces
- `wiki/bridges/` for concrete applied analyses or memos
- `wiki/knowledge/` for factual syntheses

Any maintained wiki page written back by this skill should default to Chinese.
