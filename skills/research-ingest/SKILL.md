---
name: research-ingest
description: Compile external source materials into maintained knowledge pages. Use when Codex needs to ingest articles, papers, reports, book notes, or clipped webpages from `raw/external/` or `inbox/`, update `wiki/knowledge/`, repair links, and record the ingest in the log.
---

# Research Ingest

Read `schemas/AGENTS.md` and `schemas/ingest.md` first. Treat external source files as evidence, not as editable working notes.

## Local Scripts

For common file operations, use the local shell scripts to avoid token-wasting exploration:

```bash
# List inbox files
./skills/kb-ops/scripts/kb-scripts.sh list

# Read all inbox files
./skills/kb-ops/scripts/kb-scripts.sh read

# Move inbox files to raw/external
./skills/kb-ops/scripts/kb-scripts.sh move
```

## Workflow

1. Read the source and identify its topic, claims, and likely destination.
2. Move the source into `raw/external/` if it is still sitting elsewhere in the repository.
3. Update an existing page in `wiki/knowledge/` when one already covers the topic.
4. Create a new page only when the source introduces a genuinely new topic or comparison.
5. Add cross-links to related maintained pages.
6. Append a short `ingest` or `lint` entry to `wiki/log.md`.

## Capture

Capture these elements when they matter:

- what the source is trying to explain
- its main claims or takeaways
- important caveats, tensions, and contradictions
- which existing knowledge pages should change because of it

## Guardrails

- Prefer updating over duplicating.
- Keep world-facing claims in `wiki/knowledge/`, not `wiki/self/`.
- If the source already contains the user's own viewpoint mixed with external material, save the integrated result in `wiki/bridges/` and only extract world knowledge that is durable on its own.
- Write maintained wiki pages in Chinese by default.

## Output

When useful, structure a knowledge page around:

- summary
- key claims
- evidence or source basis
- tensions or open questions
- related pages

Keep the page concise enough that later query work can reuse it quickly.
