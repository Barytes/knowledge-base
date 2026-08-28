# Repository Agent Guide

This repository is a local knowledge base. This file is the canonical source for repository-wide agent policy. Task schemas and skills add task-specific contracts; they should not repeat these rules.

## Authority And Discretion

- `MUST` rules protect data, ownership, evidence, or repository correctness.
- Other guidance is a default, not a required reasoning method or response template.
- Unless a task contract requires an order, the agent may choose how to investigate, reason, use tools, and present the result.
- Examples illustrate possible outputs; they are not mandatory templates.

## Protected Material

- `notebook/` is user-authored draft space. It may be read when relevant and mirrored unchanged to the generated site, but MUST NOT be edited, moved, normalized, linted, reorganized, or ingested into maintained wiki pages.
- `life-record/` is private local-only material. It MUST NOT be staged, committed, pushed, published, ingested, indexed, or included in generated site output.
- `raw/` is source evidence. It MUST NOT be rewritten unless the user explicitly requests it.

## Maintained Layers

- `wiki/topics/`: world-facing knowledge and concrete applied analysis.
- `wiki/self/`: recurring user judgment supported by personal evidence.
- `wiki/frameworks/`: compact reusable judgment frameworks and query routes.
- `contexts/`: low-confidence observations awaiting possible distillation.
- `wiki/site/`: generated browsing view; Markdown remains the source of truth.

Maintained wiki prose defaults to Chinese. Preserve paths, identifiers, commands, repository names, and useful technical terms in their original form.

## Evidence And Query Policy

For repository questions, use relevant maintained wiki material as the default interpretive context. It is an evidence anchor, not an exclusive source.

Web search is allowed whenever it can materially improve freshness, correctness, completeness, verification, or source attribution. When external evidence is used, keep it distinguishable from local material, cite it, and identify any material local gap. If the repository has no relevant material, an externally grounded answer is acceptable.

Use `wiki/topics/` for topic facts, `wiki/self/` for recurring personal judgment, and `wiki/frameworks/router.md` when a reusable decision lens would help. These are routing defaults, not a required reading sequence.

## Change Contract

- Query and review tasks default to read-only. Modify the repository only when the user requests a change or the task is explicitly a maintenance workflow.
- Prefer updating an existing maintained page over creating a duplicate.
- Preserve uncertainty and distinguish source fact, inference, synthesis, and user-specific judgment.
- After changing maintained wiki pages, update relevant navigation or log entries and regenerate `wiki/site/` with `./skills/kb-ops/scripts/kb-ingest.sh site`.

Use `skills/kb-query/` for knowledge-base-anchored questions and `skills/kb-ops/` for maintenance. Task-specific requirements live in `schemas/` and the selected skill.
