# Knowledge Base

This repository is a lightweight local knowledge base designed for two jobs:

1. Compile external materials into a maintained wiki.
2. Distill personal writings and records into reusable judgment patterns.

Core idea:

- `raw/` stores source materials and is the evidence layer.
- `wiki/` stores LLM-maintained pages and is the working knowledge layer.
- `schemas/` stores the operating rules the agent should follow.
- `skills/` stores task-specific prompts or workflows, including local workflow skills and imported external skills.

Current operating schemas:

- `schemas/AGENTS.md`
- `schemas/ingest.md`
- `schemas/query.md`
- `schemas/lint.md`

Current core workflow skills:

- `skills/kb-ops/`
- `skills/kb-query/`
- `skills/research-ingest/`
- `skills/self-distill/`
- `skills/bridge-write/`
- `skills/framework-distill/`
- `skills/repo-map-ingest/`
- `skills/repo-practice-query/`

For the full list, including installed external skills, see `skills/README.md`.

Start simple. Add material first, then let the structure evolve with use.

## Short Invocations

You do not need to paste the full repository workflow every time.

Use short requests such as:

- `$kb-ops`
- `$kb-query`
- `Use $kb-ops to lint this repository.`
- `Use $kb-ops to ingest everything in inbox/.`
- `Use $kb-ops to update the Harness Engineering topic and any affected bridge pages.`
- `Use $kb-ops to run a full-cycle maintenance pass on this repo.`
- `Use $kb-query to answer from this repository only.`

`$kb-query` should begin by listing the local pages it actually consulted before answering.

Bare invocation behavior:

- `kb-ops` or `$kb-ops` defaults to full repository maintenance
- `kb-query` or `$kb-query` defaults to local-only repository question answering
