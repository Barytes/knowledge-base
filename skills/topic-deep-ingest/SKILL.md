---
name: topic-deep-ingest
description: Build a complete, linked, searchable topic surface from a substantial source rather than producing only a summary.
---

# Topic Deep Ingest

## Goal

Represent every reusable concept, mechanism, named distinction, checklist, practice, failure mode, or recurring claim from the source in the maintained knowledge base.

## Coverage Contract

- Preserve the source and identify the concrete topic set before declaring completion.
- Map each concrete topic to a suitable existing page or a justified new page; broad chapter pages are not substitutes for missing reusable concepts.
- Route pages according to `AGENTS.md` and `schemas/ingest.md`. Do not modify `notebook/` or source PDFs.
- Provide navigation from the material overview or topic index and meaningful links among related maintained pages.
- Paraphrase copyrighted material rather than copying long passages, and preserve source anchors needed for later verification.
- Regenerate `wiki/site/` and verify that representative titles or keywords reach the intended pages through the search index.
- Run applicable repository and link checks and report any residual coverage gap.

## Resources

- `skills/topic-deep-ingest/scripts/topic_coverage_audit.py`
- `scripts/test_kb_workflow.py`
- `skills/kb-ops/scripts/kb-ingest.sh site`

The agent may choose how to inspect the material, group concepts, structure pages, and verify coverage. Completion is governed by coverage and verification, not a fixed sequence or template.
