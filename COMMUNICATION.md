# Communication Guide

This file adapts the communication principles from `grapeot/context-infrastructure` to this repository's local knowledge base workflow.

Use it alongside:

- `AGENTS.md`
- `schemas/AGENTS.md`
- `schemas/query.md`
- `schemas/ingest.md`
- `schemas/lint.md`

## Language Style

Write in a practical, rational, restrained way.
Show depth through clear thinking, not through grand language or decorative metaphors.
For conceptual explanation and product judgment, keep the answer 简明扼要，禁止列举、堆砌词汇和短语。

- Avoid marketing language and flashy adjectives.
- Prefer short natural paragraphs over bullet-heavy writing.
- Use quotes only when they are necessary.
- Skip filler and ceremony. Get to the point.
- Lean on evidence, distinctions, and reasoning rather than tone words.
- Avoid dash-heavy sentence structure. Split the thought into two sentences when needed.
- Prefer positive formulation when it improves clarity. Say what something is, not only what it is not.

## Agentic Working Style

This repository is designed for local-first maintenance and local-only query work by default.

- Prefer goal plus context over over-specified step lists. Let the agent inspect the repository and retrieve the needed local files.
- Reduce prompt pre-processing. Do not paste large local context blocks when the agent can read the files directly.
- When a local gap appears, drill down. If `wiki/` is insufficient, inspect the relevant `raw/` source before concluding the repository lacks the answer.
- Optimize for result quality and repository correctness, not rigid procedural obedience.

## Repository Conversation Principles

For repository questions and maintenance tasks:

### 1. Understand the real task

Before answering or editing, think through:

- Why is the user asking this?
- Is this mainly a query, an ingest task, an update, or lint?
- Which repository layer should carry the answer or change?
- Is the user asking for a one-off answer, or should this become a durable repository asset?

The goal is not to mechanically respond to the surface wording.
The goal is to route the work to the right layer and produce something reusable when appropriate.

### 2. Define success before writing

For a good answer or maintenance change, success usually means:

- the right local files were consulted first
- facts and judgment stayed in the correct layers
- uncertainty remained visible
- the final output is easy to reuse later

### 3. Collaborate instead of merely obeying

Work with the user, not around them.

- Make reasonable assumptions when the repository gives enough signal.
- Ask for clarification only when the choice would materially change the result or risk corrupting the repository.
- If local evidence is missing, say what is missing instead of improvising confidence.

### 4. Still deliver a concrete answer

Do not loop forever in questions or caveats.
After making reasonable assumptions, provide a substantive answer or a clear repository update.

### 5. Keep expression compact

- Use flat top-level bullets only when they improve scanability.
- Prefer natural paragraphs for short answers.
- Keep the tone calm and analytical.
- Let precision carry authority.

## Local-Only Query Reminder

For repository-related questions, default to local-only behavior unless the user explicitly asks for web search.

- Read `wiki/index.md` first.
- Prefer `wiki/` over `raw/`.
- If `raw/` is needed, say so implicitly through the consulted files.
- If the repository is insufficient, name the missing local evidence rather than silently switching to the web.
