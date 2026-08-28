---
name: repo-map-ingest
description: Study a code repository as evidence and create a durable repo map with architecture, mechanisms, version anchors, and open questions.
---

# Repo Map Ingest

## Goal

Create both a preserved source snapshot in `raw/external/` and a reusable maintained repo map under the relevant `wiki/topics/` area.

## Contract

- Identify the repository, observed version or date, and the question or topic being studied.
- Use README and documentation as claims about intent, not proof of implemented behavior.
- Describe important mechanisms by what they control, the failure mode they address, their implementation anchors, and their cost or tradeoff.
- Preserve compact evidence anchors: repository URL or local path, version, relevant files, and notable issues, PRs, ADRs, or releases when available.
- Do not copy large amounts of source code or claim deeper implementation knowledge than the evidence supports.
- Prefer a compact remote snapshot. Clone only when the user requests it or when a snapshot cannot answer the authorized task.
- For authorized maintained changes, follow `schemas/ingest.md`, update relevant navigation and log entries, and regenerate the site.

## Resources

- `skills/repo-map-ingest/scripts/github_repo_ingest.py`
- `skills/repo-map-ingest/scripts/github_repo_snapshot.py`
- `skills/repo-map-ingest/scripts/repo_map_from_snapshot.py`
- `skills/repo-map-ingest/references/output-template.md`
- `wiki/topics/agent-harness-runtime/codebases-as-knowledge-sources.md`

The agent may choose the reading order, tools, and map structure needed for the repository and question.
