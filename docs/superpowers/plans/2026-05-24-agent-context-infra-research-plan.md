# Agent Context Infra Research Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a dated 2026-05-24 map of agent context infrastructure across research status and engineering/product/open-source systems.

**Architecture:** Treat context infra as an agent runtime lifecycle problem: source, store, retrieve, compress, isolate, govern, observe, and evaluate context. The final output should separate research mechanisms from engineering systems, then reconnect them through a gap map and opportunity map.

**Tech Stack:** Local knowledge base (`wiki/`, `raw/`), web research with primary sources where possible, arXiv/OpenReview papers, official docs, GitHub repositories, company docs/blogs, spreadsheet-style comparison tables in Markdown.

---

## Research Scope

This plan uses the working definition from 2026-05-24:

Agent context infra is the infrastructure layer that lets an agent obtain, organize, compress, isolate, persist, write back, govern, and evaluate the context it needs across long tasks, sessions, tools, users, and data sources.

Include:

- Connectors and protocols: MCP, A2A, tool/resource registries, SaaS/data connectors.
- Runtime state and sessions: conversation state, task state, checkpoints, resume, compaction.
- Memory systems: short-term, long-term, episodic, semantic, procedural, shared, multi-user, multimodal.
- Retrieval and routing: agentic RAG, hierarchical retrieval, query decomposition, source planning, grounding.
- Compression and distillation: summaries, task-state compaction, reflection, context virtualization.
- Isolation and governance: user/project/agent namespaces, permissions, provenance, memory correction, forgetting, audit.
- Evaluation and observability: memory benchmarks, retrieval quality, task completion, regression, trace, cost, latency.

Exclude:

- Pure prompt tips without persistent context lifecycle.
- Plain vector databases unless used as agent-facing context or memory infrastructure.
- Generic workflow orchestration unless it manages context state.
- Fine-tuning unless it is explicitly compared with external memory/context.
- Ordinary enterprise data pipelines not designed for agent runtime use.

## Output Package

- `wiki/bridges/agent-context-infra-2026-05-24.md`: final Chinese research memo.
- `raw/external/agent-context-infra-source-list-2026-05-24.md`: source bibliography and notes.
- Optional `wiki/knowledge/agent-context-infra-market-map.md`: durable map if the memo becomes reusable.

## Key Questions

1. What does research in early 2026 consider the hard parts of agent memory and context management?
2. Which mechanisms are converging: compression, retrieval stores, reflection, hierarchical memory, learned management, context virtualization?
3. Which evaluations are credible, and what do they actually measure: recall, decision quality, task success, consistency, state mutation, or user experience?
4. Which engineering systems are becoming real product categories: protocol, memory layer, context database, stateful runtime, eval/observability, coding-agent context layer?
5. Where is the gap between research benchmarks and production systems?
6. What opportunities remain for a builder focused on agent context / harness / eval / reliability?

## Source Buckets

### Research Sources

Seed sources:

- `Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers` (`arXiv:2603.07670`).
- `From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms` (`arXiv:2605.06716`).
- `AI Agents Need Memory Control Over More Context` (`arXiv:2601.11653`).
- `Active Context Compression: Autonomous Memory Management in LLM Agents` (`arXiv:2601.07190`).
- `Contextual Memory Virtualisation` (`arXiv:2602.22402`).
- `Memori` (`arXiv:2603.19935`).
- `MemMachine` (`arXiv:2604.04853`).
- `MemoryAgentBench`, `GroupMemBench`, `STATE-Bench`, `LongMemEval`, `LoCoMo`, `PerLTQA`, `StructMemEval`.
- ICLR 2026 workshops: `Memory for LLM-Based Agentic Systems`, `Lifelong Agent`, `Agents in the Wild`.

### Engineering/Product/Open-Source Sources

Protocol and standards:

- MCP official docs and Anthropic launch post.
- A2A protocol specification.
- OpenAI Agents SDK sessions/context docs.
- Cloudflare Agents memory docs.

Memory and stateful agent systems:

- Letta / MemGPT.
- Mem0.
- Zep / Graphiti.
- LangGraph memory.
- LlamaIndex memory and agentic retrieval.
- Microsoft AutoGen / Agent Framework memory materials.
- Mastra memory.

Context database and file-system approaches:

- OpenViking.
- Project-level context engines or MCP memory servers with explicit hierarchy, provenance, or context pack design.
- Coding-agent context patterns: AGENTS.md, repo skills, compaction workflows, subagent isolation.

Eval and observability:

- STATE-Bench.
- Cursor/Anthropic/OpenAI-style eval, replay, trace, quality-loop docs where public.
- Open-source tracing stacks used in agent systems: LangSmith, Braintrust, Arize/Phoenix, OpenTelemetry-based traces.

## Task 1: Build Source Inventory

**Files:**
- Create: `raw/external/agent-context-infra-source-list-2026-05-24.md`

- [ ] Step 1: Create the source list with four sections: research papers, benchmarks, engineering systems, market/JD signals.
- [ ] Step 2: For each source, record title, URL, date, type, why it matters, and whether it is primary or secondary.
- [ ] Step 3: Mark each source as `must-read`, `skim`, or `optional`.
- [ ] Step 4: Keep at least 70% of the evidence from primary sources: papers, official docs, GitHub repos, official blogs.

## Task 2: Research Status Map

**Files:**
- Create: `wiki/bridges/agent-context-infra-2026-05-24.md`

- [ ] Step 1: Read survey papers first and extract the shared taxonomy.
- [ ] Step 2: Build a table with columns: mechanism, core idea, solved failure mode, representative papers, evaluation status, open problems.
- [ ] Step 3: Separate memory mechanisms from context lifecycle mechanisms. Do not let memory swallow the whole category.
- [ ] Step 4: Summarize research maturity in three bands:
  - mature enough to engineer now
  - promising but benchmark-bound
  - early or speculative
- [ ] Step 5: Add a section on evaluation shift: from static recall to multi-session task performance and stateful enterprise scenarios.

## Task 3: Engineering/Product/Open-Source Map

**Files:**
- Modify: `wiki/bridges/agent-context-infra-2026-05-24.md`

- [ ] Step 1: Group systems into six families:
  - connector/protocol layer
  - stateful agent runtime
  - memory-as-a-service
  - context database/file-system layer
  - coding-agent context workflow
  - eval/observability layer
- [ ] Step 2: For each family, write what it owns in the context lifecycle.
- [ ] Step 3: Create a comparison table with columns: system, category, context abstraction, write path, read path, governance, eval story, maturity.
- [ ] Step 4: Avoid ranking by hype. Rank by whether the system makes context inspectable, correctable, scoped, testable, and reusable.

## Task 4: Gap Map

**Files:**
- Modify: `wiki/bridges/agent-context-infra-2026-05-24.md`

- [ ] Step 1: Compare research mechanisms against shipped systems.
- [ ] Step 2: Identify gaps in:
  - memory write policy
  - contradiction and stale context handling
  - provenance and correction
  - multi-agent/multi-user isolation
  - cost and latency
  - eval realism
  - observability and replay
- [ ] Step 3: Write a short judgment for each gap: research ahead, engineering ahead, or both immature.

## Task 5: Opportunity Map

**Files:**
- Modify: `wiki/bridges/agent-context-infra-2026-05-24.md`

- [ ] Step 1: Connect findings to the local framework pages:
  - `wiki/frameworks/Harness架构判断框架.md`
  - `wiki/frameworks/AI系统产品判断框架.md`
  - `wiki/frameworks/研究判断框架.md`
  - `wiki/bridges/Anthropic与OpenAI的Agent Systems履历North Star.md`
- [ ] Step 2: Identify 3-5 practical builder opportunities.
- [ ] Step 3: For each opportunity, state:
  - target user
  - painful failure mode
  - minimum viable artifact
  - first eval
  - why it is not just another RAG wrapper
- [ ] Step 4: Highlight which opportunities best match agent context / harness / eval / reliability positioning.

## Task 6: Final Memo Polish

**Files:**
- Modify: `wiki/bridges/agent-context-infra-2026-05-24.md`

- [ ] Step 1: Add a dated executive summary.
- [ ] Step 2: Add a `核心结论` section with 5-7 claims.
- [ ] Step 3: Add a `研究现状` section.
- [ ] Step 4: Add a `工程产品/开源项目地图` section.
- [ ] Step 5: Add a `缺口与机会` section.
- [ ] Step 6: Add `来源依据` with primary sources first.
- [ ] Step 7: Check that all maintained wiki prose is Chinese.

## Quality Bar

The final memo succeeds if it:

- Defines context infra more precisely than generic RAG or memory.
- Separates research claims from engineering adoption.
- Uses dated evidence and states uncertainty.
- Names the evaluation problem, not just architectures.
- Produces an opportunity map useful for project and career decisions.
- Can be reused as a durable wiki bridge page.

## Suggested Timeline

- Day 1: source inventory and research taxonomy.
- Day 2: benchmark and evaluation map.
- Day 3: engineering/product/open-source system map.
- Day 4: gap map and opportunity map.
- Day 5: final memo and wiki integration.

## Self-Review

- Spec coverage: The plan covers both requested axes: research status and engineering/product/open-source map.
- Placeholder scan: No `TBD` or unspecified source class remains.
- Scope check: The scope is broad but research-only. It is decomposed by evidence type and output section rather than implementation subsystem.
- Risk: The plan depends on rapidly changing product docs and GitHub repos. The final memo must preserve the exact date, 2026-05-24, and avoid timeless claims where the evidence is only a snapshot.
