# context-core

Eval-first context infrastructure for agent systems.

## Purpose

`context-core` makes agent context explicit, traceable, and testable.

Instead of treating context as a large prompt blob, it defines a small set of durable objects:

- `Source`: where knowledge comes from
- `ContextUnit`: a reusable chunk of maintained knowledge or evidence
- `ContextBundle`: the context package sent into a task
- `RouteDecision`: why certain context was selected
- `Trace`: what happened during the task
- `EvalCase`: how to replay and score the task
- `WritebackCandidate`: what should become durable knowledge after the task

## Non-Goals

- Not a vector database.
- Not a generic RAG framework.
- Not a full agent runtime.
- Not a chat application.

## V0 Scope

V0 should be small enough to finish quickly:

1. Define the seven core objects.
2. Load `Source` and `ContextUnit` records from markdown or JSON.
3. Route a query to a `ContextBundle` using simple keyword / metadata rules.
4. Emit a `RouteDecision`.
5. Write a JSONL `Trace`.
6. Store an `EvalCase`.
7. Generate a `WritebackCandidate` stub.

## Suggested Tree

```text
context-core/
  README.md
  pyproject.toml
  src/context_core/
    __init__.py
    models.py
    registry.py
    router.py
    bundle.py
    trace.py
    evals.py
    writeback.py
  eval/
    cases/
    reports/
    README.md
  examples/
    research_query.json
    trace.jsonl
  docs/
    design-brief.md
    failure-taxonomy.md
```

## Core Objects

### Source

Represents a durable evidence source.

Required fields:

- `id`
- `kind`
- `uri`
- `title`
- `owner`
- `created_at`
- `updated_at`
- `trust_level`

### ContextUnit

Represents a reusable context block.

Required fields:

- `id`
- `source_id`
- `text`
- `summary`
- `tags`
- `scope`
- `provenance`

### ContextBundle

The actual context package assembled for a task.

Required fields:

- `id`
- `task_id`
- `units`
- `budget`
- `assembly_notes`

### RouteDecision

Explains why this bundle was selected.

Required fields:

- `id`
- `task_id`
- `query`
- `selected_unit_ids`
- `rejected_unit_ids`
- `reason`
- `confidence`

### Trace

Records what happened.

Required fields:

- `id`
- `task_id`
- `context_bundle_id`
- `events`
- `final_output_ref`
- `failure_label`

### EvalCase

Replayable task record.

Required fields:

- `id`
- `task`
- `input`
- `expected_behavior`
- `scoring_rubric`
- `source_refs`

### WritebackCandidate

Possible durable knowledge update.

Required fields:

- `id`
- `trace_id`
- `target_layer`
- `proposed_content`
- `reason`
- `status`

## First Eval Dimensions

1. Grounding: does the answer cite or use the right source?
2. Route relevance: did the router select the right units?
3. Separation: does the answer separate known facts, judgment, and speculation?
4. Usefulness: does the answer give a next action?
5. Writeback quality: is the proposed durable update worth keeping?

## First Demo

Input:

> Should I pursue an AI-native agent systems role in June?

Expected:

- Read career framework pages.
- Build a context bundle from agent JD, career positioning, and project roadmap pages.
- Answer with objective difficulty, subjective fear, and next action.
- Emit trace and writeback candidate.

