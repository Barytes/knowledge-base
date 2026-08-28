---
name: kb-ops
description: Perform authorized maintenance for this knowledge base, including ingest, update, lint, and generated-site refresh work.
---

# KB Ops

## Goal

Complete the requested repository maintenance while preserving the ownership, privacy, and evidence boundaries in `AGENTS.md`.

## Contract

- Infer the smallest maintenance scope that satisfies the request: ingest, update, lint, or a combination.
- Use `schemas/ingest.md` and `schemas/lint.md` when their contracts apply.
- Route external evidence, personal evidence, applied analysis, and reusable frameworks to their correct maintained layers.
- Do not modify `notebook/` or expose `life-record/`.
- Prefer reversible, incremental changes and update existing pages over creating duplicates.
- When maintained wiki content changes, update relevant navigation or `wiki/log.md`, regenerate `wiki/site/`, and run proportionate deterministic checks.

## Resources

- `skills/kb-ops/scripts/kb-scripts.sh`: inbox listing, reading, and movement helpers.
- `skills/kb-ops/scripts/kb-ingest.sh`: inbox ingest and site regeneration.
- Task-specific skills may be used as additional contracts when relevant.

For a bare `$kb-ops` invocation, inspect the repository and perform only the smallest safe maintenance justified by the current state. Choose the work order and tools according to actual dependencies.
