# Repository AGENTS Guide

This repository is a local knowledge base. For repository-related questions, the default mode is local-first and local-only unless the user explicitly asks for web search.

## Default Behavior

- Read `COMMUNICATION.md` for writing and interaction style.
- For open-ended collaboration, agent behavior, preference, or judgment questions, also read `wiki/self/agent-collaboration-profile.md`.
- If the question exposes a new agent failure mode or recurring preference signal, record it first as an observation in `contexts/memory/OBSERVATIONS.md`; promote it to `wiki/self/` only when it becomes stable.
- Read `wiki/index.md` first.
- Answer from `wiki/` before reading `raw/`.
- Use `raw/` only when the maintained wiki is incomplete.
- Do not browse the web for repository questions unless the user explicitly asks to search online.
- If the local knowledge base is insufficient, say what is missing instead of silently switching to web search.

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
- For local-only question answering, use `skills/kb-query/`.
- After creating or updating maintained wiki pages, run `./skills/kb-ops/scripts/kb-ingest.sh site` so `wiki/site/` stays in sync automatically.
- For detailed repository policy, read:
  - `COMMUNICATION.md`
  - `schemas/AGENTS.md`
  - `schemas/ingest.md`
  - `schemas/query.md`
  - `schemas/lint.md`
