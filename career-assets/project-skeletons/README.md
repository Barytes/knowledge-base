# Agent Systems Project Skeletons

This folder contains first-pass skeletons for the career signal stack:

1. `context-core`: eval-first context infrastructure.
2. `oh-share-it-eval`: shared research knowledge deployment and evaluation layer.
3. `my-little-agent-loop`: minimal Codex-like harness for trace / replay / eval.

The stack should tell one story:

> I can build agent systems where context is explicit, tool use is traceable, failures are replayable, and quality is evaluated.

## Layering

| Layer | Project | Role |
|---|---|---|
| Context layer | `context-core` | Source registry, route decisions, context bundles, traces, eval cases, writeback candidates |
| Deployment layer | `oh-share-it` | Real research-group context sharing, queries, trials, deployment notes, route-quality eval |
| Runtime layer | `my-little-agent-loop` | Tool use, permission gates, patch editing, trace, replay, evaluator loop |
| Workbench layer | `gogo` | Existing local LLM-wiki workbench and demo entry |

## 2-Week Build Order

1. Create `context-core` repo or folder.
2. Implement schema-only V0: dataclasses / Pydantic models for the seven core objects.
3. Add 5 sample eval cases from your knowledge base.
4. Add `oh-share-it` route-quality eval around those cases.
5. Add `my-little-agent-loop` trace JSONL format and a replay stub.
6. Write one case study using the resulting traces.

## Resume Signal

Target bullet:

> Built an eval-first agent context infrastructure stack: `context-core` for context routing and writeback, `oh-share-it` for real-world shared deployment, and `my-little-agent-loop` as a minimal Codex-like harness for traceable, replayable agent execution.

