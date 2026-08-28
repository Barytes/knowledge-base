# Knowledge Base

This repository is a lightweight local knowledge base designed for two jobs:

1. Compile external materials into a maintained wiki.
2. Distill personal writings and records into reusable judgment patterns.

Core idea:

- `raw/` stores source materials and is the evidence layer.
- `notebook/` stores user-authored draft notes. It may be synced and mirrored into the static site as a separate notebook layer, but it is not an agent-maintained wiki layer.
- `life-record/` stores private local-only records and must not be pushed, published, indexed, or included in site output.
- `wiki/` stores LLM-maintained pages and is the working knowledge layer.
- `schemas/` stores the operating rules the agent should follow.
- `skills/` stores task-specific prompts or workflows, including local workflow skills and imported external skills.

Repository-wide policy lives in `AGENTS.md`. Task contracts live in:

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
- `Use $kb-query to answer with local knowledge and web research when useful.`

Bare invocation behavior:

- `kb-ops` or `$kb-ops` inspects the repository and performs the smallest safe maintenance justified by the current state
- `kb-query` or `$kb-query` uses local knowledge as an evidence anchor and may search the web when useful
