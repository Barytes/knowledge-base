# Agent Context Infra 来源清单（2026-05-24）

这份清单服务于 `wiki/bridges/agent-context-infra-2026-05-24.md`。它不是全量 bibliography，而是一组能支撑“研究现状 + 工程产品/开源项目地图”的 dated source set。

优先级含义：

- `must-read`：主报告直接依赖。
- `skim`：用于校准分类或补充例子。
- `optional`：后续深挖时再读。

来源类型：

- `primary`：论文、官方文档、官方博客、GitHub 仓库、项目自述。
- `secondary`：媒体、社区讨论、第三方总结。

## 研究论文

| 优先级 | 来源 | 日期 | 类型 | 证据性质 | 为什么重要 |
|---|---|---:|---|---|---|
| must-read | [Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670) | 2026-03 | primary | survey | 把 agent memory 形式化为 write-manage-read loop，并给出 temporal scope、representational substrate、control policy 三维 taxonomy。 |
| must-read | [From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716) | 2026-05 | primary | survey | 把 memory 演进压成 Storage、Reflection、Experience 三阶段，适合判断研究范式从“存储”向“经验抽象”移动。 |
| must-read | [AI Agents Need Memory Control Over More Context](https://arxiv.org/abs/2601.11653) | 2026-01 | primary | mechanism + eval | 代表“更多上下文不是答案，控制写入和状态承诺更关键”的研究线。 |
| must-read | [Active Context Compression: Autonomous Memory Management in LLM Agents](https://arxiv.org/abs/2601.07190) | 2026-01 | primary | mechanism | 代表 agent 自主决定何时压缩、写入 persistent knowledge、裁剪历史的方向。 |
| must-read | [Contextual Memory Virtualisation: DAG-Based State Management and Structurally Lossless Trimming for LLM Agents](https://arxiv.org/abs/2602.22402) | 2026-02 | primary | mechanism | 用 OS virtual memory 类比 session history，提出 snapshot、branch、trim 等上下文状态管理原语。 |
| skim | [Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents](https://arxiv.org/abs/2603.19935) | 2026-03 | primary | system paper | 代表 API 层 persistent memory 的产品化/框架化尝试。 |
| skim | [MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents](https://arxiv.org/abs/2604.04853) | 2026-04 | primary | mechanism + benchmark | 强调 ground-truth preserving、retrieval-stage optimization、query routing。 |
| skim | [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) | 2025-01 | primary | system paper | 工程系统 Zep/Graphiti 的论文化依据，强调 temporal knowledge graph。 |

## Benchmark 与评测来源

| 优先级 | 来源 | 日期 | 类型 | 证据性质 | 为什么重要 |
|---|---|---:|---|---|---|
| must-read | [STATE-Bench: A benchmark for AI agent memory](https://opensource.microsoft.com/blog/2026/05/19/introducing-state-bench-a-benchmark-for-ai-agent-memory/) | 2026-05 | primary | benchmark + official blog | 从“记住事实”推进到企业任务、状态变更、过程合规、用户体验和多次运行稳定性。 |
| must-read | [MemoryAgentBench](https://openreview.net/pdf?id=DT7JyQC3MR) | 2026-04 | primary | benchmark | ICLR 2026 paper，强调 incremental multi-turn interactions 中评估 memory agent。 |
| must-read | [GroupMemBench](https://arxiv.org/abs/2605.14498) | 2026-05 | primary | benchmark | 把 memory 从双人对话推到多人/群组场景，暴露 speaker-grounded belief tracking、term ambiguity 等缺口。 |
| must-read | [StructMemEval](https://arxiv.org/abs/2602.11243) | 2026-02 | primary | benchmark | 评测 agent 能否把长期记忆组织成有用结构，而不是只做事实 recall。 |
| skim | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) | 2026-05 | primary | benchmark | 把 long-term memory 目标转向“成为有经验的同事”。 |
| skim | [MemGym](https://arxiv.org/abs/2605.20833) | 2026-05 | primary | benchmark/environment | 试图统一 memory reasoning interface 与 long-horizon memory environment。 |
| optional | [LoCoMo and PerLTQA overview](https://www.emergentmind.com/topics/locomo-and-perltqa) | 2026 | secondary | benchmark overview | 常被 memory 产品引用，但需要谨慎对待 LLM judge 和数据质量问题。 |
| optional | [LongMemEval overview](https://www.emergentmind.com/topics/longmemeval-benchmark) | 2026 | secondary | benchmark overview | 社区主流 conversational memory benchmark 的背景说明。 |

## 工程系统、产品与开源项目

| 优先级 | 来源 | 日期 | 类型 | 证据性质 | 为什么重要 |
|---|---|---:|---|---|---|
| must-read | [Model Context Protocol docs](https://modelcontextprotocol.io/docs/getting-started/intro) | 2026 snapshot | primary | official docs | 标准化 agent/app 与外部 data source、tools、workflow 的连接。 |
| must-read | [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) | 2024-11 | primary | official blog | MCP 的原始定位：打通 data silos，让 AI assistant 连接实际系统。 |
| must-read | [A2A Protocol Specification](https://google-a2a.github.io/A2A/specification/) | 2026 snapshot | primary | official spec | agent-to-agent 互操作协议，覆盖 discovery、task lifecycle、context exchange、artifacts。 |
| must-read | [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) | 2026 snapshot | primary | official docs | 把 agent runtime 明确到 orchestration、tool execution、state、approvals、observability、evaluation。 |
| must-read | [OpenAI Agents SDK Sessions](https://openai.github.io/openai-agents-js/guides/sessions/) | 2026 snapshot | primary | official SDK docs | session memory、compaction、storage strategy 的工程接口。 |
| must-read | [LangGraph memory docs](https://docs.langchain.com/oss/python/concepts/memory) | 2026 snapshot | primary | official docs | 把 short-term thread state、long-term namespace store、semantic/episodic/procedural memory、hot path/background writes 做成工程术语。 |
| must-read | [Letta stateful agents docs](https://docs.letta.com/guides/core-concepts/stateful-agents) | 2026 snapshot | primary | official docs | 状态化 agent、core memory、archival memory、agent 自编辑 memory 的代表系统。 |
| must-read | [Mem0 docs](https://docs.mem0.ai/introduction) | 2026 snapshot | primary | official docs | memory-as-a-service / open-source self-hosted memory layer 代表。 |
| must-read | [Zep Memory docs](https://help.getzep.com/v2/memory) | 2026 snapshot | primary | official docs | temporal knowledge graph memory、chat history + graph 的代表系统。 |
| must-read | [Graphiti docs](https://help.getzep.com/graphiti/getting-started/welcome) | 2026 snapshot | primary | official docs | 实时 temporal KG、MCP server、hybrid search 的开源工程形态。 |
| must-read | [OpenViking site](https://www.openviking.ai/) | 2026 snapshot | primary | official site | 把 memory、resources、skills 统一为 file-system-like context database。 |
| must-read | [OpenViking GitHub](https://github.com/volcengine/OpenViking) | 2026 snapshot | primary | GitHub repo | 开源 context database 的代码与文档依据。 |
| skim | [Cloudflare Agents memory docs](https://developers.cloudflare.com/agents/concepts/memory/) | 2026-05 | primary | official docs | Session API、conversation history、context blocks、skills/loadable context 的运行时实现。 |
| skim | [Mastra Observational Memory](https://mastra.ai/research/observational-memory) | 2026-02 | primary-ish | company research blog | 代表不显式写 memory，而把 observation 注入 context 的 memory 产品思路。 |

## 市场、岗位与产业信号

| 优先级 | 来源 | 日期 | 类型 | 证据性质 | 为什么重要 |
|---|---|---:|---|---|---|
| must-read | [Agent 岗位 JD 抽样与能力信号](../../wiki/knowledge/Agent岗位JD抽样与能力信号.md) | 2026-05-13 | local synthesis | local primary synthesis | 已整理 OpenAI、Anthropic、Cursor、Cohere、Sierra、Harvey、Notion 等岗位，显示 context / runtime / eval / deployment 正在成为招聘主语。 |
| must-read | [Anthropic 与 OpenAI 的 Agent Systems 履历 North Star](../../wiki/bridges/Anthropic与OpenAI的Agent%20Systems履历North%20Star.md) | 2026-05 | local synthesis | local bridge | 将岗位信号压成 agent systems builder 的 north star：context、execution、evaluation、deployment、quality loop。 |
| skim | [AI 产业与投资判断框架](../../wiki/frameworks/AI产业与投资判断框架.md) | local | local framework | local framework | 判断 context infra 是否是补偿层、控制点、还是容易被模型进步吞掉的中间层。 |
| optional | [TechRadar: Zendesk adopts MCP](https://www.techradar.com/pro/zendesk-becomes-the-latest-to-adopt-mcp-to-futureproof-customers-in-the-ai-first-era) | 2026-05 | secondary | industry news | 可作为 MCP 企业采用的事件层信号，不作为核心证据。 |

## 证据比例检查

本清单核心证据中，研究论文、官方文档、官方博客、GitHub 仓库和本地已核验 JD synthesis 占主体。媒体与社区讨论只作为环境噪音和弱信号，不用于支撑关键结论。

