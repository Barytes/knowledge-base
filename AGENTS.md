# Repository AGENTS Guide

This repository is a local knowledge base. For repository-related questions, use the maintained knowledge base as the default evidence anchor. Web search is allowed when it improves freshness, correctness, or completeness.

## Default Behavior

- Read `COMMUNICATION.md` for writing and interaction style.
- For conceptual explanation and product judgment, answer 简明扼要，禁止列举、堆砌词汇和短语。
- For open-ended collaboration, agent behavior, preference, or judgment questions, also read `wiki/self/agent-collaboration-profile.md`.
- If the question exposes a new agent failure mode or recurring preference signal, record it first as an observation in `contexts/memory/OBSERVATIONS.md`; promote it to `wiki/self/` only when it becomes stable.
- Read `wiki/index.md` first.
- Answer from `wiki/` before reading `raw/`.
- Use `raw/` only when the maintained wiki is incomplete.
- Prefer an answer that combines relevant local knowledge with any necessary external evidence. Do not return a purely web-derived answer unless the local knowledge base has no relevant material and external information is necessary to answer well.
- When web search is used, state what the local knowledge base contributed, identify any local gap, and clearly distinguish external evidence from local material.

## Repository Layers

- `notebook/`: user-owned draft notebook; agents may read it and may include it in git sync and the generated website view, but must not rewrite, move, delete, lint, normalize, reorganize, or convert it into maintained wiki pages
- `life-record/`: private life records; never stage, commit, push, publish, ingest, index, or include in generated site output
- `raw/`: source evidence
- `contexts/`: low-confidence working memory and observation logs for future distillation; not a substitute for maintained `wiki/self/` pages
- `wiki/topics/`: topic-organized maintained knowledge and applied analysis
- `wiki/self/`: maintained personal judgment patterns
- `wiki/frameworks/`: compact judgment frameworks and query routing surfaces
- `wiki/site/`: generated static HTML browsing view

## Wiki Language Policy

- All maintained wiki pages under `wiki/` should default to Chinese.
- This includes `wiki/index.md`, `wiki/log.md`, and new or updated pages in `wiki/topics/`, `wiki/self/`, and `wiki/frameworks/`.
- Keep file paths, repository names, commands, code identifiers, and unavoidable technical terms in their original form when helpful.
- Do not create new English-first wiki pages unless the user explicitly asks for bilingual or English output.

## Query Rules

- Factual repository questions: use `wiki/topics/`
- Questions about recurring user preferences or judgment: use `wiki/self/`
- Reusable judgment frameworks, router pages, and compact entry surfaces: use `wiki/frameworks/`
- For design, evaluation, comparison, and decision questions, read `wiki/frameworks/router.md` first, then the most relevant framework page, then the relevant `wiki/topics/` pages when needed
- Advisory questions: write durable applied analysis back to the most relevant topic under `wiki/topics/`

## Operational Rules

- Treat `notebook/` as user-owned working space. It may be synced as source files and mirrored into the generated website under a separate notebook navigation entry, but do not rewrite, move, delete, lint, normalize, reorganize, or ingest it into maintained wiki pages.
- Treat `life-record/` as private local-only material. Never stage, commit, push, publish, ingest, index, or include it in generated site output.
- For maintenance workflows, use `skills/kb-ops/`.
- For knowledge-base-anchored question answering, use `skills/kb-query/`.
- After creating or updating maintained wiki pages, run `./skills/kb-ops/scripts/kb-ingest.sh site` so `wiki/site/` stays in sync automatically.
- For detailed repository policy, read:
  - `COMMUNICATION.md`
  - `schemas/AGENTS.md`
  - `schemas/ingest.md`
  - `schemas/query.md`
  - `schemas/lint.md`
