# my-little-agent-loop

Minimal Codex-like agent harness for traceable tool use and eval-driven replay.

## Purpose

This project should prove runtime ownership.

It should not become another chatbot. It should show that agent behavior can be:

- permissioned
- traced
- replayed
- evaluated
- connected to explicit context bundles

## V0 Loop

```text
task
  -> load ContextBundle
  -> plan
  -> call tools
  -> produce patch or result
  -> emit JSONL trace
  -> replay
  -> evaluate
```

## Suggested Tree

```text
my-little-agent-loop/
  README.md
  pyproject.toml
  src/agent_loop/
    __init__.py
    session.py
    tools.py
    permissions.py
    patcher.py
    trace.py
    replay.py
    evaluator.py
  traces/
    examples/
  eval/
    cases/
    reports/
  docs/
    design-brief.md
    permission-model.md
    trace-schema.md
```

## V0 Features

1. Session object with task, working directory, context bundle, and status.
2. Tool call wrapper that records input, output, duration, and error.
3. Permission modes:
   - `read-only`
   - `edit-with-approval`
   - `command-with-approval`
   - `trusted-local`
4. Patch-based file editing.
5. JSONL trace.
6. Replay runner for fixed tasks.
7. Evaluator stub with human score fields.

## Trace Event Types

- `task.created`
- `context.loaded`
- `plan.updated`
- `tool.called`
- `tool.completed`
- `patch.proposed`
- `patch.applied`
- `command.requested`
- `command.completed`
- `failure.labeled`
- `task.completed`
- `eval.scored`

## First Demo Tasks

1. Read a small markdown knowledge base and answer a grounded question.
2. Apply a tiny patch to a README and emit the diff.
3. Replay the same task with a fixed context bundle.
4. Label whether failure came from context routing, tool execution, or model judgment.

## Resume Bullet Draft

Built a minimal Codex-like agent harness for traceable tool use, permission-gated execution, patch-based editing, replayable sessions, and evaluator stubs, designed to connect agent runtime behavior with explicit context bundles and regression cases.

