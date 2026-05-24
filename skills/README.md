# Skills

This folder is reserved for task-specific workflows.

Difference from `schemas/`:

- `schemas/` defines stable global rules for the whole repository.
- `skills/` defines situational instructions for specific jobs such as research, writing, coding, or reflection.

Current workflow skills:

- `kb-ops/`: slash-command-like entry point for ingest, update, and lint
- `kb-query/`: local-only question answering from the repository knowledge base
- `repo-map-ingest/`: fetch a compact GitHub or local repo evidence snapshot, auto-generate a maintained repo map note, and refresh index/log entries
- `repo-practice-query/`: answer focused engineering-practice questions from a studied repo
- `research-ingest/`: compile external sources into `wiki/knowledge/`
- `self-distill/`: distill personal records into `wiki/self/`
- `bridge-write/`: combine `knowledge` and `self` into applied analysis
- `framework-distill/`: lift reusable judgment skeletons from `knowledge` and `bridges` into `wiki/frameworks/`

Installed external skills:

- `action-coach/`: imported from `yvonnegladwellstack/yvskills`; a dialogue-first action coaching skill for users who want to act but feel stuck
