---
name: framework-distill
description: Distill reusable judgment frameworks from maintained `wiki/topics/` pages into compact pages under `wiki/frameworks/`. Use when Codex needs to lift repeated distinctions, routing surfaces, or decision skeletons upward without mixing in `wiki/self/` or turning `frameworks/` into a second topic layer.
---

# Framework Distill

Read these files first:

- `schemas/AGENTS.md`
- `schemas/query.md`
- `schemas/lint.md`
- `wiki/frameworks/README.md`
- `wiki/frameworks/router.md`

Use this skill when the task is to compress existing maintained material into reusable framework pages, not to answer a one-off question or write a concrete memo.

## Default Invocation

If the user input is only `framework-distill` or `$framework-distill`, interpret it as:

- scan recent or user-named `wiki/topics/` pages
- identify the best candidate reusable judgments
- update or create the smallest necessary page under `wiki/frameworks/`
- refresh router/index links when needed
- run a light link check on touched files

## What Counts As A Framework

A page belongs in `wiki/frameworks/` when it mainly answers:

- 以后这类问题该先站在哪个框架上看
- 哪几个区分、张力、诊断问题最值得先问
- 哪些 `topics/` 页面常该一起调用

A page does **not** belong in `wiki/frameworks/` when it mainly answers:

- 这次具体该怎么做
- 这个项目、公司、案例的结论是什么
- 你的个人判断倾向是什么

## Required Boundaries

- Distill from `wiki/topics/` only.
- Do not pull `wiki/self/` into `frameworks/`.
- Do not turn `frameworks/` into a second topic directory.
- Prefer compact framework pages over long summary pages.
- Prefer updating an existing framework over spawning a near-duplicate.

## Workflow

1. Read `wiki/frameworks/router.md` and the most relevant existing framework pages first.
2. Read the candidate `wiki/topics/` pages.
3. Extract the reusable layer only:
   - recurring distinctions
   - routing questions
   - decision skeletons
   - common tensions
   - recommended reading order
4. Decide one of three actions:
   - update an existing framework page
   - create one new compact framework page
   - keep the source page in place and add only a short framework summary that links back
5. Link the new or updated framework page back to its main source pages.
6. Update `wiki/frameworks/router.md`, `wiki/frameworks/README.md`, and `wiki/index.md` when the new framework changes routing.
7. Append a short `维护` or `query` log entry to `wiki/log.md`.
8. Run a light link check on touched files.

## Distillation Heuristics

Prefer promoting material when at least one of these is true:

- the same distinction will likely be reused across many future questions
- the source page already contains a strong named framework or decision skeleton
- the page helps route future design, evaluation, comparison, or decision queries
- later queries would otherwise need to re-read a long page to recover the same top-level lens

Prefer leaving material in `topics/` when:

- it is mainly source summary or factual exposition
- it is mainly a case memo or concrete recommendation
- the “framework” is really just a restatement of one page’s conclusion
- the signal is too narrow, too time-sensitive, or too weak to deserve a new entry surface

## Recommended Shape For A Framework Page

When useful, organize the page as:

- what this framework is for
- what to ask first
- core judgments
- common tensions
- recommended reading order
- when to enter a concrete topic page
- related pages

Keep it short. Link outward instead of re-expanding the full source material.

## Guardrails

- Do not copy whole sections from source pages into `frameworks/`.
- Do not add personal-lens language sourced only from `wiki/self/`.
- Do not create a framework page that could be replaced by one bullet in an existing framework.
- If two candidate framework pages are adjacent, merge them unless the split is clearly reusable.
- Write maintained pages in Chinese by default.

## Typical Inputs

- “把这几页知识抽成框架”
- “从 `knowledge/` 里找适合上升到 `frameworks/` 的页面”
- “给 query 增加一个新的判断入口”
- “把这页长文里的可复用判断压成 framework”

## Typical Outputs

- one new compact framework page
- an update to an existing framework page
- router/index/readme link refresh
- a short maintenance log entry
