---
name: research-ingest
description: Compile external sources into maintained topic knowledge while preserving provenance and repository boundaries.
---

# Research Ingest

## Goal

Turn external material into reusable maintained knowledge rather than a duplicate summary.

## Contract

- Preserve source material in `raw/external/` and treat it as evidence, not an editable draft.
- Update an existing `wiki/topics/` page when it already covers the subject; create a page only for a genuinely new durable topic or comparison.
- Capture the claims, evidence basis, caveats, tensions, and changes the source implies for existing knowledge.
- Keep world-facing claims out of `wiki/self/` and preserve mixed personal judgment as a distinct layer.
- For authorized changes, add useful cross-links, append a concise ingest log entry, and regenerate `wiki/site/`.

Follow `schemas/ingest.md`. Choose the extraction method and page structure appropriate to the source.
