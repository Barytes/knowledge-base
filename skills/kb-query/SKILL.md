---
name: kb-query
description: Answer repository questions with the local knowledge base as the evidence anchor. Read `wiki/` and `raw/` first, use web search when it materially improves freshness, correctness, or completeness, and keep external evidence distinct from local knowledge.
---

# KB Query

Read these files first:

- `AGENTS.md`
- `schemas/AGENTS.md`
- `schemas/query.md`

Use this skill for repository-related question answering, not for maintenance.

## Default Invocation

If the user input is only `kb-query` or `$kb-query`, interpret it as:

- answer the current repository question from local materials, supplemented by external evidence when useful

## Default Behavior

Treat repository questions as knowledge-base-anchored. Web search is allowed when it materially improves the answer.

That means:

1. read `wiki/index.md` first
2. for design, evaluation, comparison, or decision questions, read `wiki/frameworks/router.md` first when available
3. then read the most relevant `wiki/frameworks/` page
4. then read the most relevant `wiki/topics/` pages
5. read `raw/` only if the wiki is incomplete
6. answer from local material and use web search when freshness, correctness, completeness, or source attribution would materially improve
7. if external evidence is used, keep it distinguishable from the local contribution and name any material local gap
8. do not return a purely web-derived answer unless local material is absent and external information is necessary

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

- Use web search as a supplement, not as a replacement for relevant local knowledge.
- Do not silently mix repository material with outside search results.
- Clearly mark claims supported by external information and explain why external evidence was needed.
- Avoid purely web-derived answers unless the repository has no relevant material and the external information is necessary.
- If the question is really a maintenance request, hand off to `kb-ops`.
- Do not omit the consulted-pages opening, even for short answers.

## Write-Back

If an answer produces a durable clarification or synthesis, save it back into the right maintained layer and add a `query` log entry.

Prefer:

- `wiki/frameworks/` for reusable judgment frameworks, router pages, and compact entry surfaces
- `wiki/topics/` for factual syntheses, concrete applied analyses, memos, and essays

Any maintained wiki page written back by this skill should default to Chinese.
