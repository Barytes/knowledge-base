# Skills

This folder is reserved for task-specific workflows.

Relationship to repository policy and `schemas/`:

- `AGENTS.md` defines repository-wide policy.
- `schemas/` defines task contracts for ingest, query, and lint.
- `skills/` defines situational goals, boundaries, completion conditions, and resources.

Current workflow skills:

- `kb-ops/`: slash-command-like entry point for ingest, update, and lint
- `kb-query/`: repository-grounded question answering with web research when useful
- `repo-map-ingest/`: fetch a compact GitHub or local repo evidence snapshot, auto-generate a maintained repo map note, and refresh index/log entries
- `repo-practice-query/`: answer focused engineering-practice questions from a studied repo
- `research-ingest/`: compile external sources into `wiki/topics/`
- `topic-deep-ingest/`: extract every concrete topic from a material into separate linked wiki pages and verify site search coverage
- `self-distill/`: distill personal records into `wiki/self/`
- `bridge-write/`: combine topic material and `self` into applied analysis under `wiki/topics/`
- `framework-distill/`: lift reusable judgment skeletons from `topics` into `wiki/frameworks/`

Installed external skills:

- `action-coach/`: adapted from `yvonnegladwellstack/yvskills`; helps users clarify a block and identify a self-endorsed next action without a fixed diagnostic script
