---
name: kb-ops
description: Orchestrate repository maintenance for this knowledge base. Use when Codex needs a slash-command-like entry point to ingest new materials, update maintained pages, run lint cleanup, or perform a full maintenance cycle across `raw/`, `wiki/`, `schemas/`, and `inbox/`.
---

# KB Ops

Read these files first:

- `schemas/AGENTS.md`
- `schemas/ingest.md`
- `schemas/query.md`
- `schemas/lint.md`

Use the local workflow skills as sub-guides when relevant:

- `skills/kb-query/`
- `skills/research-ingest/`
- `skills/topic-deep-ingest/`
- `skills/self-distill/`
- `skills/bridge-write/`
- `skills/framework-distill/`

Do not write to `notebook/`. That directory is a user-owned draft notebook. Maintenance workflows may sync it to git and mirror it into the generated static site, but must not ingest it into maintained wiki pages, lint, normalize, reorganize, move, delete, or otherwise modify its contents.

Treat `life-record/` as private local-only material. Never stage, commit, push, publish, ingest, index, or include it in generated site output.

When this skill creates or updates maintained pages under `wiki/`, write them in Chinese by default. Keep paths, commands, repository names, code identifiers, and necessary technical terms in their original form when useful.

If the user is asking a repository question rather than requesting maintenance, route to `kb-query` instead of doing operational work.

## Local Scripts

For common file operations, use the local shell scripts to avoid token-wasting exploration:

```bash
# List inbox files (simple)
./skills/kb-ops/scripts/kb-scripts.sh list

# Read all inbox files
./skills/kb-ops/scripts/kb-scripts.sh read

# Move inbox files to raw/external
./skills/kb-ops/scripts/kb-scripts.sh move

# List inbox files (detailed with size/lines)
./skills/kb-ops/scripts/kb-ingest.sh list

# Ingest all inbox files to raw/external
./skills/kb-ops/scripts/kb-ingest.sh all

# Ingest single file
./skills/kb-ops/scripts/kb-ingest.sh file <path>

# Regenerate the generated HTML browsing view
./skills/kb-ops/scripts/kb-ingest.sh site
```

## Default Invocation

If the user input is only `kb-ops` or `$kb-ops`, interpret it as:

- run `full-cycle` maintenance for the current repository

That default means:

1. ingest material from `inbox/` when present
2. update affected maintained pages
3. run a light lint pass
4. regenerate `wiki/site/`
5. report what changed and what still needs review

## Command Modes

Interpret the user's request as one of these modes:

- `ingest`: process new source material into the correct wiki layer
- `update`: refresh or extend existing maintained pages
- `lint`: clean the repository and repair structural issues
- `full-cycle`: run ingest, then update affected pages, then lint

If the user does not specify a mode, infer the smallest safe one.
For the bare invocation `kb-ops` or `$kb-ops`, do not ask which mode to use. Use `full-cycle`.

## Ingest Mode

When asked to ingest:

1. Inventory the relevant files or folders.
2. Classify each source as external, personal, or mixed.
3. Move mislocated source files into the correct raw or inbox folder.
4. Compile the material into `wiki/topics/` or `wiki/self/`.
5. Update `wiki/index.md` if the maintained structure changed.
6. Append a short log entry to `wiki/log.md`.
7. 自动重新生成 `wiki/site/`，再报告 ingest 完成。

Use:

- `research-ingest` for external materials
- `self-distill` for personal materials
- `bridge-write` when the result should mix both layers

If a new top-level topic is needed, add its metadata to `wiki/topics/topics.json` before regenerating `wiki/site/`.

## Update Mode

When asked to update:

1. Find the maintained page or topic area involved.
2. Read the relevant wiki pages first.
3. Pull in raw evidence only when the wiki is incomplete or stale.
4. Update existing pages instead of creating duplicates.
5. Write back any durable synthesis.
6. Log meaningful updates in `wiki/log.md`.
7. Regenerate `wiki/site/` when any maintained page or index changed.

Use `bridge-write` when the update should reflect the user's recurring judgment, not just external facts.
Use `framework-distill` when the update should lift reusable judgment skeletons from `wiki/topics/` into `wiki/frameworks/`.

## Lint Mode

When asked to lint:

1. Follow `schemas/lint.md`.
2. Reclassify files that violate the current directory design.
3. Remove obvious clutter such as `.DS_Store`.
4. Check for orphan pages and duplicate pages.
5. Normalize English-first maintained wiki pages into Chinese when needed.
6. Repair links or move uncertain content to `inbox/`.
7. Append a `lint` entry to `wiki/log.md`.
8. Regenerate `wiki/site/` when maintained wiki files changed.

Be conservative. Prefer moving uncertain material to `inbox/` instead of deleting it.

## Full-Cycle Mode

When asked to run a full maintenance cycle:

1. Ingest targeted new materials or the contents of `inbox/`.
2. Update any affected topic, self, or framework pages.
3. Run a light lint pass at the end.
4. Regenerate `wiki/site/`.
5. Return a short summary of what changed and what still needs review.

## Response Style

For operational runs, keep the final report compact:

- what was processed
- what pages were created or updated
- what was moved during lint
- what needs human review

Do not ask the user to restate the repository rules if they are already in this repo.
