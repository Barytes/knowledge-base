---
name: repo-map-ingest
description: Study a code repository as a knowledge-source evidence base. Use when Codex is given a GitHub repository or local codebase and needs to create or update a durable repo map in `wiki/knowledge/`, capturing architecture, key mechanisms, evidence anchors, and follow-up directions without copying raw implementation churn into the wiki.
---

# Repo Map Ingest

NEVER CLONE THE REPO. 

Read these files first:

- `AGENTS.md`
- `schemas/AGENTS.md`
- `schemas/ingest.md`
- `schemas/query.md`
- `wiki/bridges/codebases-as-knowledge-sources.md`
- `skills/repo-map-ingest/references/output-template.md`

Use this skill when the main job is to understand a repository as a source of engineering knowledge.

## Goal

Turn a repository into:

1. a preserved raw evidence snapshot in `raw/external/`
2. a reusable maintained repo map in `wiki/knowledge/`

Do not skip the raw evidence layer for GitHub repos. 

The output should help later queries answer:

- what the repo is trying to do
- how it is structured
- where its important control mechanisms live
- which files or commits should be revisited for deeper study

## Minimum Inputs

Try to freeze these three things before reading widely:

1. which repository
2. which version, branch, release, or observation date
3. which topic or question matters most

If the user gives only a GitHub URL:

1. fetch a compact raw snapshot into `raw/external/`
2. use the README only as the starting map
3. find stronger anchors before writing the maintained repo note

## GitHub URL Mode

When the input is a GitHub URL, the preferred one-shot command is:

```bash
python3 skills/repo-map-ingest/scripts/github_repo_ingest.py <github-url>
```

This creates:

- a compact source snapshot under `raw/external/`
- a maintained repo map draft under `wiki/knowledge/`
- an index entry in `wiki/index.md`
- an ingest entry in `wiki/log.md`

If you only need the raw evidence layer first, you can still run:

```bash
python3 skills/repo-map-ingest/scripts/github_repo_snapshot.py <github-url>
python3 skills/repo-map-ingest/scripts/repo_map_from_snapshot.py <snapshot-path>
```

The snapshot script captures:

- repository metadata
- top-level tree summary
- selected architecture and control files
- evidence anchors for later follow-up

The note-generation step turns that snapshot into a reusable repo map draft with:

- repository purpose
- architecture map
- first-pass mechanism inventory
- evidence anchors
- open questions for deeper study

When using the default repository paths, the one-shot wrapper also refreshes:

- `wiki/index.md`
- `wiki/log.md`

## Network Policy

GitHub access is part of this skill's intended workflow.

- If the user invokes this skill with a GitHub URL, treat that as explicit permission to fetch from that repository.
- Do not ask a separate conversational question before attempting GitHub access.
- If the runtime environment itself requires a network approval prompt, request that approval through the tool directly rather than asking the user to restate the task.

This skill cannot override sandbox or app-level permission systems, but it should treat GitHub fetches as already authorized by user intent.

## Reading Order

Read in this order:

1. root README or docs for stated purpose
2. top-level tree and major directories
3. manifests and environment files
4. CI, lint, test, and repo-rule files
5. agent-control files such as `AGENTS.md`, prompts, skills, planners, eval configs, permission rules, or task specs
6. only then, targeted implementation files

## What To Extract

Build a mechanism inventory rather than a file inventory.

For each important mechanism, capture:

- what it controls
- what failure mode it prevents
- what files implement it
- what tradeoff or cost it introduces

For engineering-practice questions, pay extra attention to:

- state externalization
- planning and coordination
- verification and eval loops
- sandboxing and permission gates
- rollback and reset paths
- CI and repo contracts

## Output Shape

Write or update:

- a raw snapshot in `raw/external/`
- a maintained repo note in `wiki/knowledge/`

Prefer a stable filename such as:

- `<repo-name>-repo-map.md`
- `<repo-name>-engineering-practices.md`

When useful, structure it as:

- summary
- repository purpose
- architecture map
- mechanism inventory
- evidence anchors
- open questions
- related pages

Write the maintained repo map in Chinese by default. Keep repository names, file paths, commands, and necessary technical terms in their original form when useful.

## Evidence Anchors

Always leave behind a compact evidence section for future query work.

Include:

- repo URL or local path
- branch, commit, tag, or observation date when known
- specific file paths worth revisiting
- any especially important PR, issue, ADR, or release note when available

This is the main handoff to `repo-practice-query`.

## Guardrails

- Do not copy large amounts of source code into the wiki.
- Do not store the maintained repo map only in `raw/external/`; raw and maintained layers should both exist.
- Do not confuse README claims with implemented behavior.
- Do not promote project-specific details into general principles too early.
- If the repo has not been read deeply enough, mark open questions instead of smoothing over gaps.

## Write-Back

If the repository introduces durable topic knowledge beyond one repo, also update an existing topic page in `wiki/knowledge/`.

Append an `ingest` or `query` entry to `wiki/log.md` when the repo map becomes a maintained page.
