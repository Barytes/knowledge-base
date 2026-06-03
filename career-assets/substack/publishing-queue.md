# Substack Publishing Queue

Goal: turn existing essays and project notes into public market signals for the same profile:

> Agent Systems Engineer focused on context infrastructure, agent harnesses, evaluation, and reliable knowledge workflows.

This is not a generic blog. Each post should prove one part of the same career image.

## Publishing Principles

1. Lead with a concrete problem, not a grand AI claim.
2. Show the system boundary: what humans decide, what agents do, where context lives, and how failure is detected.
3. Make every post point back to one of the projects: `gogo`, `oh-share-it`, `context-core`, or `my-little-agent-loop`.
4. Prefer clear diagrams, short examples, and failure cases over abstract manifestos.
5. End with a specific artifact: repo link, design note, eval case, trace screenshot, or roadmap.

## Queue

### 1. Building an Eval-First Context Layer for Research Agents

Status: draft from `wiki/bridges/Agent系统月度执行计划-2026-05-24.md` and context-core notes.

Purpose: flagship career signal.

Proves:
- you understand context as infrastructure, not prompt stuffing
- you know eval / trace / failure taxonomy matter
- you can connect a research-group use case to agent systems engineering

Suggested structure:
1. The problem: research agents fail because context is invisible and untested.
2. The wrong default: bigger prompts, more RAG, more chat UI.
3. The context-core model: `Source`, `ContextUnit`, `ContextBundle`, `RouteDecision`, `Trace`, `EvalCase`, `WritebackCandidate`.
4. Eval dimensions: grounding, route relevance, known / judgment / speculation separation, next-step usefulness.
5. One example query from a research knowledge base.
6. What this enables for `oh-share-it` and `my-little-agent-loop`.

CTA:
- Link to `context-core` repo once skeleton exists.
- Link to `oh-share-it` as the deployment scenario.

### 2. From Local LLM-Wiki to Agent Workbench

Status: existing essay draft at `wiki/bridges/essays/给自己做了一个llm-wiki的入口应用.md`.

Purpose: explain `gogo` without overselling it.

Proves:
- you can build usable knowledge workbenches
- you care about local-first files, visibility, and user-owned context
- you understand why agent UX is more than a chat box

Suggested title options:
- "I Built a Local LLM-Wiki Workbench"
- "Why Agent Workbenches Should Start from Files"
- "From Markdown Knowledge Bases to Agent Workbenches"

Needed edits before publishing:
- Add one screenshot or diagram.
- Add a short "What I would build next" section that points to `context-core`.
- Keep `gogo` as the workbench/client, not the full public knowledge-base product.

### 3. Public Research Knowledge Bases Should Preserve Tension

Status: existing essay draft at `wiki/bridges/essays/课题组公共知识库-博客草稿.md`.

Purpose: position `oh-share-it` as a knowledge governance product, not just shared notes.

Proves:
- you understand research knowledge is not only retrieval
- you can reason about conflict, provenance, writeback, and team workflows
- you can define a product from a real research-lab pain point

Suggested title options:
- "Public Research Knowledge Bases Should Preserve Tension"
- "A Shared Knowledge Base Is Not a Shared Folder"
- "How Research Groups Can Make Knowledge Compound"

Needed edits before publishing:
- Open with a concrete research-group onboarding or idea-screening scenario.
- Compress the EvoMap / Reflexio comparison.
- Add the role of `oh-share-it` and the current MVP boundary.

### 4. A Minimal Codex-like Agent Harness

Status: draft from `wiki/bridges/Codex-like-agent-harness路线图.md`.

Purpose: prove runtime / harness ownership.

Proves:
- you understand agent harnesses as traceable systems
- you can separate model intelligence from deterministic tooling
- you can talk about permissions, patches, replay, and eval

Suggested structure:
1. What "Codex-like" means here.
2. Why this is not another chat agent.
3. The minimal loop: task -> context bundle -> tool calls -> patch/result -> trace -> replay -> eval.
4. Thin harness, fat skills.
5. How this connects to `context-core`.

Needed before publishing:
- Build V0 or at least create the repo skeleton.
- Include a sample JSONL trace.

### 5. The Career Frame: Agent Systems Engineer

Status: from `wiki/bridges/Agent Systems Engineer职业定位.md`.

Purpose: make the profile legible to people who may hire or refer you.

Proves:
- you are not a generic AI builder
- your projects form a coherent direction
- you know the limits of your current evidence

Suggested title options:
- "I Want to Work on Agent Systems, Not AI Demos"
- "From AI Demos to Reliable Agent Systems"
- "The Role I Am Looking For: Agent Systems Engineer"

Suggested structure:
1. The shallow version: using AI to build products.
2. The deeper version: building AI product runtime.
3. The four surfaces: context, harness, eval, reliability.
4. My current projects.
5. What I am looking for.

## Minimal Posting Schedule

If time is tight, publish in this order:

1. From Local LLM-Wiki to Agent Workbench
2. Public Research Knowledge Bases Should Preserve Tension
3. Building an Eval-First Context Layer for Research Agents
4. A Minimal Codex-like Agent Harness
5. The Career Frame: Agent Systems Engineer

This order starts from existing material, then moves toward the harder flagship stack.

## Bio Draft

Agent systems builder focused on context infrastructure, agent harnesses, and evaluation-first reliability. I build local-first knowledge workbenches and shared context layers that help agents and humans work from the same durable knowledge base.

## About Page Draft

I write about agent systems beyond demos: context infrastructure, knowledge workflows, agent harnesses, evaluation, and reliability.

My current work centers on a small stack:

- `gogo`: a local LLM-wiki desktop workbench.
- `oh-share-it`: a shared context layer for research knowledge bases.
- `context-core`: an eval-first context routing and trace layer.
- `my-little-agent-loop`: a minimal Codex-like harness for traceable, replayable tool use.

The common question behind these projects is simple:

> How do we make agents work from visible, durable, evaluable context instead of fragile chat history?
