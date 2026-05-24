# Agent Context Infra 调研报告（2026-05-24）

## 摘要

截至 2026-05-24，`agent context infra` 已经不能再被简单理解成 RAG、向量库或“记忆功能”。更准确的定义是：

> agent context infra 是让 agent 在长任务、多轮会话、多工具、多数据源、多用户边界下，能够获得、组织、压缩、隔离、持久化、回写、治理、观察和验证“该知道的东西”的基础设施层。

它的主语是 `context lifecycle`，而不只是 `memory`。Memory 是其中跨轮次保留信息的子系统；更大的问题还包括上下文从哪里来、何时进入模型窗口、如何被压缩、哪些 agent 能看到、写入是否可信、旧记忆何时失效、失败能否回放、质量能否被评测。

研究侧的核心变化是：agent memory research 正在从“存什么、怎么检索”转向 `write-manage-read`、经验抽象、上下文压缩、虚拟化状态、多人记忆与任务级评测。工程侧的核心变化是：协议、stateful runtime、memory layer、context database、coding-agent workflow、eval/observability 正在分化成不同层，而不是由一个“memory API”包打天下。

压缩判断：

> 2026 年 agent context infra 的关键，不是给模型更多上下文，而是把上下文变成可来源化、可存储、可取回、可压缩、可隔离、可治理、可观察、可评测、可复用的工程对象。

## 核心结论

1. **Memory 正在被重新定义成控制问题，而不是存储问题。** 2026 年的 survey 已经把 memory 形式化成 `write-manage-read` loop，并强调写入、管理、读取三处都可能失败。真正危险的不是“没记住”，而是未验证内容被长期固化、旧事实污染新任务、错误反思变成规则。

2. **“更多上下文”不是可靠 agent 的充分解。** 长上下文窗口和 transcript replay 能缓解部分 recall 问题，但也会带来噪音、成本、延迟和 drift。研究里的 `Active Context Compression`、`Agent Cognitive Compressor`、`Contextual Memory Virtualisation` 都在指向同一件事：上下文需要受控压缩、状态承诺和版本化管理。

3. **评测正在从静态 recall 转向任务效果。** LoCoMo、LongMemEval 这类早期 benchmark 仍有价值，但 2026 年更重要的信号来自 STATE-Bench、MemoryAgentBench、GroupMemBench、StructMemEval、LongMemEval-V2、MemGym。它们开始问：memory 是否让 agent 更可靠地完成多步任务、适应环境、处理多人上下文、维护结构、避免重复失败。

4. **工程生态分成六层，不宜混为一谈。** MCP/A2A 是协议连接层；OpenAI Agents SDK、LangGraph、Letta、Cloudflare Agents 是 stateful runtime；Mem0、Zep/Graphiti、Mastra 是 memory layer；OpenViking 和文件系统式 context 是 context database / workbench；coding-agent workflow 是上下文预算管理纪律；STATE-Bench、LangSmith、Braintrust、Phoenix 是 eval/observability 闭环。

5. **Context database / file-system layer 是值得重点跟踪的工程形态。** OpenViking 的 `viking://`、L0/L1/L2、目录递归检索、session commit，以及 `AGENTS.md`、repo skills、local wiki 这类文件式 context，都把上下文从黑盒检索结果变成可浏览、可引用、可 diff、可修正的工作面。

6. **最大缺口在写入、纠错、隔离和回放。** 当前很多系统能 `add/search`，但弱在 memory write policy、contradiction/staleness handling、provenance/correction、多用户/多 agent 隔离、成本延迟控制、真实任务评测和 replay debugger。

7. **最有价值的 builder 机会不在普通 RAG wrapper，而在 eval-first context runtime。** 更具体地说，是 memory eval harness、write/correction layer、group memory namespace、environment experience runbook、memory observability/replay debugger 这几类可评测、可部署、可迭代的系统。

## 范围定义

本文纳入的 `agent context infra` 包括：

- connector / protocol：MCP、A2A、tool/resource registry、SaaS/data connectors。
- runtime state / session：conversation state、task state、checkpoint、resume、compaction。
- memory system：short-term、long-term、episodic、semantic、procedural、shared、multi-user、multimodal。
- retrieval / routing：agentic RAG、hierarchical retrieval、query decomposition、source planning、grounding。
- compression / distillation：summary、task-state compaction、reflection、abstract/overview/full-text 分层、context virtualization。
- isolation / governance：user/project/agent namespace、permission、provenance、memory correction、forgetting、audit。
- evaluation / observability：memory benchmark、retrieval quality、task completion、regression replay、trace、cost、latency。

本文排除：

- 单纯 prompt 技巧，除非它参与系统化 context routing 或 memory policy。
- 普通向量数据库，除非它被设计成 agent-facing context layer。
- 泛 workflow orchestration，除非它管理 context state 或 context lifecycle。
- fine-tuning / continual training，除非它和 external memory/context 明确比较。
- 普通 ETL / data warehouse，除非它服务 agent runtime。

## 一、研究现状

### 1. Memory 的新基本模型：write-manage-read

[Memory for Autonomous LLM Agents](https://arxiv.org/abs/2603.07670) 将 agent memory 抽象为与 perception/action 耦合的 `write-manage-read` loop。这个模型比传统“存进去、搜出来”的 RAG 图式更适合 agent，因为 agent 的行动会改变环境，环境反馈又会改变后续该写入什么。

| 阶段 | 核心动作 | 典型机制 | 主要失败模式 |
|---|---|---|---|
| Write | 判断哪些观察、偏好、错误、工具结果、环境状态值得进入 memory | LLM extraction、事件触发、人类确认、tool trace capture、反思写入 | 噪音写入、未验证内容固化、隐私越界、临时状态长期化 |
| Manage | 对已写入内容去重、合并、更新、分层、遗忘、加 provenance | summary、semantic triples、KG、profile slots、episodic store、时间衰减、conflict resolver | 旧事实覆盖新事实、矛盾被抹平、摘要丢证据、记忆越积越脏 |
| Read | 在任务中选择性召回并组织成可用上下文 | dense/sparse retrieval、hybrid search、query decomposition、rerank、context packing | 召回不相关、漏关键证据、过度注入、证据顺序错误、把 recall 当 reasoning |

这条 loop 的意义是把 memory 拆成三个可评测控制点。只做 read-path retrieval 的系统，无法解决长期 agent 最容易出错的写入和治理问题。

### 2. 三维 taxonomy：时间、表示、控制

同一篇 survey 还可以被压成三维 taxonomy：

| 维度 | 主要取值 | 研究意义 | 典型风险 |
|---|---|---|---|
| Temporal scope | turn、session、task、multi-session、user-longitudinal、group / organization、environment-longitudinal | 决定记忆生命周期、更新频率和冲突处理 | 把短期探索污染长期画像；把长期偏好误用于一次性任务；多人上下文串用 |
| Representational substrate | raw transcript、compressed summary、structured note、semantic triples、knowledge graph、episodic store、profile memory、runbook、DAG snapshot、tool/environment state | 决定可检索性、可解释性、可更新性和成本 | 表示过粗丢证据；表示过细检索成本高；结构与任务不匹配 |
| Control policy | 固定规则、prompt policy、agent self-management、evaluator-gated、learned controller、人审 / 用户确认、hybrid policy | 决定谁能写、何时写、何时忘、何时读 | 自主写入带来 poisoning；规则过硬错过隐性经验；learned policy 难解释 |

这解释了为什么很多产品都叫 memory，但实际不是一类系统。Mem0 更像 memory-as-a-service；Zep/Graphiti 更强调 temporal knowledge graph；Letta 更强调 stateful agent 与 self-editing memory；OpenViking 则更像 context database。

### 3. Storage -> Reflection -> Experience

[From Storage to Experience](https://arxiv.org/abs/2605.06716) 给出另一条演进轴：LLM agent memory 从保存轨迹，走向提炼轨迹，再走向跨轨迹经验抽象。

| 阶段 | 定义 | 代表机制 | 解决的问题 | 局限 |
|---|---|---|---|---|
| Storage | 保留 trajectory、对话、工具结果、用户偏好和环境状态 | transcript store、vector DB、episodic memory、profile slots、raw file store | 防止 agent 每次像第一次见到用户或环境 | 容易变成低质量归档；读不出来、读不准、读太多仍会失败 |
| Reflection | 对轨迹进行总结、提炼、纠错和规则化 | lesson learned、summary consolidation、error analysis、preference extraction | 减少重复犯错，形成可读中间层 | 反思可能编造因果；错误经验可能被强化 |
| Experience | 从多条轨迹中抽象可迁移策略、环境知识和主动探索计划 | cross-trajectory abstraction、runbook、skills、policy learning、proactive exploration | 让 agent 不只是记住过去，而是拥有“做过类似事”的经验 | 评测和归因很难；经验何时可迁移、何时过期仍未解决 |

这条轴对工程判断很有用：一个保存全量 transcript 的系统仍停在 Storage；一个能把多次失败压成可验证 runbook 并在新任务中主动调用的系统，才接近 Experience。

### 4. 主要机制族

| 机制族 | 核心想法 | 解决的失败模式 | 代表来源 | 成熟度 |
|---|---|---|---|---|
| Context-resident compression | 把长历史、工具输出、探索过程压成常驻任务状态或 knowledge block | context bloat、dumb zone、成本/延迟、constraint drift | [AI Agents Need Memory Control Over More Context](https://arxiv.org/abs/2601.11653)、[Active Context Compression](https://arxiv.org/abs/2601.07190) | 可工程化，但评测样本仍偏小 |
| Retrieval-augmented stores | 把 memory 外置到向量、稀疏索引、KG、episodic store、profile memory | 跨会话缺上下文、历史证据分散、用户偏好丢失 | [Memori](https://arxiv.org/abs/2603.19935)、[MemMachine](https://arxiv.org/abs/2604.04853)、Zep/Graphiti | 工程成熟度高，但容易退化成 search |
| Reflective self-improvement | agent 在任务后或运行中生成 lesson、rule、failure analysis | 重复失败、不能从经验中学习 | Reflexion 系列、Storage->Experience survey | 有潜力，但可信度与因果验证弱 |
| Hierarchical / virtual context | 把 context 分层、分角色、分窗口、分抽象层 | 常驻信息被淹没、planner 被执行噪音污染、session 太长 | Letta core/archival memory、OpenViking L0/L1/L2、本地 Research/Plan/Implement | 工程上很有用，标准评测不足 |
| Policy-learned management | 用 agent policy / evaluator / learned controller 决定写入、压缩、读取、遗忘 | 静态规则无法适应任务差异 | ACC、Focus、retrieval agent、learned memory manager | 更像前沿方向，解释性与安全性不足 |
| Contextual memory virtualization | 把 session history 当成可 snapshot、branch、trim 的 DAG 状态 | 长任务无法复用、分支探索无法回滚、compaction lossy | [Contextual Memory Virtualisation](https://arxiv.org/abs/2602.22402) | 对 coding agent 很有启发，但仍需更多复现 |

### 5. Memory research 与 context lifecycle research 的边界

本文不把 memory 等同于 context infra。更准确地说：

| 生命周期环节 | 典型问题 | 为什么不只是 memory |
|---|---|---|
| 获取 | 从用户、文件、工具、数据库、浏览器、其他 agent、环境状态中取什么 | 很多上下文只在当前任务有效，不应长期保存 |
| 路由 | 哪些材料进入哪个 agent、哪个工具、哪个子任务 | 这是运行时调度问题，不是存储问题 |
| 压缩 | 把历史、工具输出、探索过程压成任务状态 | 可能只发生在 session 内，不进入长期 memory |
| 隔离 | planner/executor、主 agent/subagent、用户 A/用户 B 之间如何隔离 | 主要防污染和泄漏，不只是提高 recall |
| 虚拟化 | snapshot、branch、trim、replay、resume 如何建模 | 更像 OS/VCS 状态管理 |
| 写回 | 哪些经验、规则、偏好、失败案例值得沉淀 | 属于 memory，但依赖评测和治理 |
| 观测与评测 | 如何判断上下文机制真的改善任务完成、稳定性、成本和用户体验 | 评测对象是整条 context loop |
| 治理 | provenance、隐私、权限、冲突、过期、删除 | 长期系统必须处理的控制面 |

## 二、评测现状

### 1. Benchmark 演进

| 阶段 | 典型问题 | 代表 benchmark | 测到什么 | 没测到什么 |
|---|---|---|---|---|
| 静态长上下文 QA | “事实藏在很长文本里，模型能不能找出来？” | LongBench、needle-in-a-haystack | 长上下文读取、局部检索、基本多跳 | 记忆如何写入、更新、删除；agent 是否因此做得更好 |
| 长对话 / 多会话 recall | “跨很多 session 的用户事实能不能被召回？” | LoCoMo、LongMemEval | single-hop、多跳、时间、知识更新、abstention | 多用户边界、企业工具状态、真实任务后果、成本和可靠性 |
| incremental multi-turn memory | “agent 能不能逐步吸收信息，并在后续任务中使用？” | [MemoryAgentBench](https://openreview.net/pdf?id=DT7JyQC3MR) | accurate retrieval、test-time learning、long-range understanding、selective forgetting | 企业级 state mutation、多人协作语境、runtime observability |
| stateful task / enterprise workflow | “记忆是否让 agent 在真实流程中更可靠？” | [STATE-Bench](https://opensource.microsoft.com/blog/2026/05/19/introducing-state-bench-a-benchmark-for-ai-agent-memory/) | procedure following、stateful tools、pass^5、成本、用户体验 | memory write policy 本身是否正确；跨组织、多角色隔离 |
| multi-party group memory | “多人频道里，agent 能不能知道谁相信什么、对谁该怎么说？” | [GroupMemBench](https://arxiv.org/abs/2605.14498) | group dynamics、speaker-grounded beliefs、audience adaptation | 工具执行、权限边界、真实企业数据治理 |
| memory structure | “agent 能不能把历史组织成 ledger、tree、todo、state machine？” | [StructMemEval](https://arxiv.org/abs/2602.11243) | 长期记忆是否被组织成有用结构 | 结构如何审计、纠错、迁移到生产工作流 |
| environment experience memory | “agent 能不能像老同事一样记住环境 affordance、workflow、坑和状态动态？” | [LongMemEval-V2](https://arxiv.org/abs/2605.12493)、[MemGym](https://arxiv.org/abs/2605.20833) | web/coding/research/computer use 中的经验压缩与复用 | 大规模线上回放、成本、延迟、真实用户反馈闭环 |

### 2. 几个关键 benchmark 的含义

**STATE-Bench** 的重要性在于，它把 memory 放进企业任务，而不是只测 50 轮前的名字能否找回。它覆盖 customer support、travel、shopping 三个域，任务强调 procedure、stateful tools 和 user experience。指标包括 task completion、pass^5、efficiency、user experience。它直接服务生产问题：memory 是否减少重复失败模式，是否提高流程一致性。

**MemoryAgentBench** 把 memory agent 能力拆成准确检索、test-time learning、long-range understanding、selective forgetting。它比 LoCoMo / LongMemEval 更接近“agent 运行时逐步学到东西”的问题，但仍偏 memory 能力隔离测试。

**GroupMemBench** 把问题推向多人协作。它显示，很多 memory ingestion 会抹平群聊结构、说话者、术语差异和 audience 关系。它报告领先系统在 group memory 上明显 collapse，这对团队 agent、Slack/Discord/Teams agent 很关键。

**StructMemEval** 关注 agent 是否能把长期记忆组织成 ledger、todo、tree 等结构。它提醒我们：好的 memory 不只是 recall，而是能被组织成任务需要的结构。

**LongMemEval-V2 / MemGym** 把 memory 推向环境经验。尤其是 coding、browser、internal tools agent，真正有价值的不是“用户喜欢什么”，而是这个 repo、这个 UI、这个工作流有哪些历史坑、状态动态和成功路径。

### 3. LoCoMo / LongMemEval 的边界

LoCoMo 和 LongMemEval 是重要起点，但不能作为 2026 年 agent context infra 的唯一 north star。

| 局限 | 具体表现 | 对机会判断的影响 |
|---|---|---|
| 偏 recall / QA | 多数问题仍是历史事实召回 | 容易高估普通 RAG |
| 用户模型偏单人 | 多是 user-agent dyad | 测不到 speaker isolation、权限和 group memory |
| 缺少真实状态改变 | 答错通常只是 QA 错 | 测不到 enterprise agent 的实际失败成本 |
| 写入策略覆盖不足 | 更关注给定历史后的读取 | 生产最危险错误常发生在写入和更新 |
| stale / contradiction 诊断不细 | 有 knowledge update，但少有完整 correction provenance | 难评估长期污染、纠错和审计 |
| 可被长上下文暴力缓解 | 大窗口下 dump more context 有竞争力 | 区分不了好 memory 与上下文预算够大 |
| 缺少 observability / replay | 多数只看最终答案 | builder 无法据此修系统 |

## 三、工程产品 / 开源项目地图

### 1. 六类系统

| 类别 | 代表系统 | 它在 context lifecycle 中主要负责什么 | 不是它主要解决什么 |
|---|---|---|---|
| Connector / protocol layer | [MCP](https://modelcontextprotocol.io/docs/getting-started/intro)、[A2A](https://google-a2a.github.io/A2A/specification/) | source、retrieve、govern 的接口边界；AI app 与工具/数据/其他 agent 的互操作 | 不直接保证 memory 质量、写入策略、检索正确性 |
| Stateful agent runtime | [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents)、[OpenAI Sessions](https://openai.github.io/openai-agents-js/guides/sessions/)、[LangGraph memory](https://docs.langchain.com/oss/python/concepts/memory)、[Letta](https://docs.letta.com/guides/core-concepts/stateful-agents)、[Cloudflare Agents](https://developers.cloudflare.com/agents/concepts/memory/) | session、state、tool execution、checkpoint、handoff、compaction、guardrail、trace | 不一定提供最强 memory policy 或 domain-specific retrieval |
| Memory layer / MaaS | [Mem0](https://docs.mem0.ai/introduction)、[Zep](https://help.getzep.com/v2/memory)、[Graphiti](https://help.getzep.com/graphiti/getting-started/welcome)、Mastra memory | long-term memory、user/session graph、semantic/episodic/procedural memory、search | 如果没有治理和 eval，容易变成 `add/search` API |
| Context database / file-system layer | [OpenViking](https://www.openviking.ai/)、[OpenViking GitHub](https://github.com/volcengine/OpenViking)、`AGENTS.md`、repo skills、local wiki | 可浏览上下文空间、目录层级、L0/L1/L2、session commit、skills/resources/memory 统一管理 | 系统较重，需要维护目录语义、权限、索引一致性 |
| Coding-agent context workflow | intentional compaction、subagent isolation、Research/Plan/Implement、repo skills | 任务内压缩、隔离探索噪音、保持主上下文干净、把经验写成 procedural context | 不是独立产品；依赖团队纪律和工具支持 |
| Eval / observability layer | STATE-Bench、LangSmith、Braintrust、Phoenix、OpenTelemetry/OpenInference | traces、episode replay、datasets、scorers、regression、cost/latency/UX | observability 不等于自动修复，eval 仍需 domain task design |

### 2. MCP 与 A2A：连接层，不是答案层

MCP 官方定义是让 AI 应用连接外部系统的开放标准，覆盖本地文件、数据库、工具和 workflow。Anthropic 的发布说明也强调，MCP 的目标是替代碎片化集成，让 AI assistant 连接真实数据系统。

在 context infra 中，MCP 的位置是：

- 暴露 data source、tool、workflow。
- 降低 agent/client 与外部系统集成成本。
- 为权限、schema、调用路径提供标准面。

但 MCP 不天然解决长期记忆质量。一个 MCP server 可以只是 `grep`，也可以背后接完整 context database。协议给的是连接能力，不是 context policy。

A2A 的主语则是 agent-to-agent。它让独立、甚至 opaque 的 agent 系统发现彼此能力、交换 context、管理 shared task 和 artifact。它和 MCP 的区别可以压成：

- MCP：agent 连接工具和数据。
- A2A：agent 连接另一个 agent。

两者会共同构成 agent context 外部边界，但都需要上层 runtime、memory、governance、eval 才能变成可靠系统。

### 3. Stateful runtime：agent loop 产品化

OpenAI Agents SDK、LangGraph、Letta、Cloudflare Agents 的共同趋势，是把 agent 从单次 LLM call 变成有状态运行体。

| 系统 | Context abstraction | Write path | Read path | Governance / eval |
|---|---|---|---|---|
| OpenAI Agents SDK | Agent、Run、Session、RunState、handoff、tool、guardrail | Session 持久化 inputs/outputs，自定义 backend；Responses compaction | run 前自动取历史，handoff/tool 读 context | guardrails、HITL、approvals、sandbox、tracing、eval workflows |
| LangGraph | graph state、thread checkpoint、Store namespace/key | graph step 更新 state，Store 写 long-term memory | step 读 state，Store search | namespace、application logic、LangSmith |
| Letta | stateful agent、memory blocks、messages、runs/steps | messages、tool calls、reasoning、memory 写入 DB | core memory 注入，旧消息通过 API/tool 取回 | tool sandbox、RBAC、Letta Evals |
| Cloudflare Agents | Durable Object-backed Agent instance、Session memory | SQLite/KV、agent state、conversation tree、context blocks | 同一 Agent instance 读取状态，conversation search，context blocks 注入 | Workers/DO 权限、MCP、平台 observability |

这一层的工程成熟度不只看“能不能跑 agent”，而要看 state、approval、tool execution、compaction、trace、eval 是否成为一等对象。

### 4. Memory layer：从 add/search 到 memory semantics

Mem0、Zep/Graphiti、Mastra 这类系统把 memory 做成可复用组件。

Mem0 的典型抽象是 universal memory layer：应用把 messages 加入 memory，再按 user/filter 搜索。它的价值是简化接入和跨框架复用；风险是如果只停留在 `add/search`，会弱在 provenance、correction、write policy 和 eval。

Zep/Graphiti 的差异点是 temporal knowledge graph。Zep 通过 `memory.add` 接收 session chat history，构建 user-level graph；`memory.get` 根据最新消息返回相关 context。Graphiti 作为开源 temporal graph framework，强调实时增量更新、历史关系、hybrid search。

Mastra memory 更像 agent framework 内部的 memory component，覆盖 thread/resource、working memory、semantic recall、memory processors、storage backends，并接入 eval/tracing 生态。

判断：memory layer 的竞争点不应只看召回速度，而要看写入语义、作用域、纠错、事实评级、图结构、hot path/background 写入，以及能否在任务级 benchmark 中带来可靠性提升。

### 5. Context database / file-system layer：从 chunk 到工作面

OpenViking 是这一类最明确的样本。它把 memory、resources、skills、sessions 统一进 `viking://` 虚拟文件系统，让 agent 通过 `ls/tree/read/find/grep/search` 等文件式范式定位上下文。它还强调 L0/L1/L2 分层 context loading、directory recursive retrieval、session commit、retrieval trajectory 可观察。

本地已维护的 [volcengine/openviking 仓库地图](../knowledge/volcengine-openviking-repo-map.md) 进一步说明，OpenViking 的重要性不在“又一个向量库”，而在它把 context 从黑盒相似片段升级成可浏览、可定位、可回写的 context runtime。

轻量文件系统式 context 也很重要：

- `AGENTS.md`：面向 coding agents 的 repo/目录级说明。
- repo skills：把可复用流程写成触发式 procedural context。
- local wiki / raw-wiki 分层：把一次性材料编译成长期可导航中间层。
- plans / research notes / compaction files：把任务状态显式化。

这类系统的优势是 inspectability 和 correctability。缺点是需要维护纪律、目录语义、命名空间和权限。

### 6. Coding-agent context workflow：短期最高 ROI

复杂代码库中的 agent context 管理，已经形成一组很实用的工作流：

- intentional compaction：把聊天历史压成任务状态，而不是随便总结。
- subagent context isolation：让探索噪音留在子上下文，只把结论回传。
- Research -> Plan -> Implement：事实、意图、执行空间的连续压缩。
- repo skills / rules：把反复有效的程序性经验写成可加载能力。

这类 workflow 不依赖单个 vendor，却能立刻改善 brownfield codebase 上的 agent 表现。本地 [coding agent 的上下文压缩工作流](../knowledge/coding%20agent%20的上下文压缩工作流.md) 已经把这条线总结得很清楚：上下文窗口不是仓库，而是工作台。

### 7. 工程系统比较表

| System | Category | Context abstraction | Write path | Read path | Governance | Eval story | Maturity |
|---|---|---|---|---|---|---|---|
| MCP | connector/protocol | tools/resources/prompts | server 实现写操作或只读资源 | client 调用 tool/resource | auth、tool schema、permissions，依赖实现 | 本身无 eval | 标准生态成熟，质量依赖具体 server |
| A2A | connector/protocol | Agent Card、Task、Message、Artifact | agent 间 message/task/artifact | task query、message history、artifact | security schemes、auth、task lifecycle | 本身无 eval | 标准化中，适合企业 agent 互操作 |
| OpenAI Agents SDK | stateful runtime | Agent、Run、Session、RunState | Session 持久化 inputs/outputs | run 前取历史、handoff/tool 使用 | guardrails、HITL、approvals、sandbox | tracing + eval workflows | 产品路径成熟 |
| LangGraph | stateful runtime | graph state、checkpoint、Store | graph step 和 Store 写入 | step 读 state，Store search | namespace、application logic | LangSmith datasets/evals | 开源生态成熟 |
| Letta | stateful runtime | memory blocks、messages、runs/steps | state 写入 DB | core memory 注入，旧消息检索 | sandbox、MCP、RBAC | Letta Evals | stateful agent 语义强 |
| Mem0 | memory layer | memory items per user/filter | `add(messages, user_id)` | `search(query, filters)` | API key、metadata filters | 需外接 task benchmark | 产品化高，抽象简洁 |
| Zep/Graphiti | memory/graph layer | temporal knowledge graph | chat/data -> graph | context string / graph search | user/session/group graph | 需外接 eval | graph 语义强 |
| OpenViking | context database | `viking://` filesystem | resource/session/memory/skill 写入 | ls/read/find/grep/search | namespace、API key、MCP identity | benchmark + 外接 eval | 新兴但设计完整 |
| AGENTS.md / repo skills | file-system context | repo docs、rules、skills | 人或 agent 写文件 | agent 按目录/trigger 读取 | git、review、目录作用域 | tests/review 间接验证 | 轻量、ROI 高 |
| STATE-Bench | eval layer | enterprise task benchmark | 运行 agent 产生 logs/results | scorer 读 final state / conversation / tool actions | benchmark schema/scorer | task completion、pass^5、cost、UX | 新但方向很对 |
| LangSmith / Braintrust / Phoenix | observability/eval | trace、dataset、experiment、scorer | instrumentation / production logs | trace viewer、eval dashboard | project/org access | offline/online eval、regression | 生产闭环逐渐成熟 |

## 四、缺口地图

| 缺口 | 当前覆盖 | 生产失败模式 | 机会含义 |
|---|---|---|---|
| Memory write policy | 弱到中。MemoryAgentBench 有增量输入，StructMemEval 暴露组织问题，但大多不直接测写入决策 | agent 把临时事实写成长期偏好；把错误工具结果写成经验；把一次性异常泛化成规则 | 需要可配置、可评测的 write gate、memory type、TTL、confidence、human correction |
| Stale / contradiction handling | 中。LongMemEval 有 knowledge update，MemoryAgentBench 有 selective forgetting | 旧政策、旧偏好、旧环境状态长期污染 | 需要 contradiction detector、supersession graph、staleness score、delete/archive/override 机制 |
| Provenance / correction | 弱。多数 benchmark 只看答案，不强制解释 memory 从何而来 | 用户纠正后，系统不知道哪个记忆被修、哪些结论受影响 | 需要 memory provenance、correction log、反向索引、影响范围分析 |
| Multi-agent / multi-user isolation | GroupMemBench 开始覆盖，但权限、租户、agent namespace 不足 | A 用户偏好泄露给 B；团队共识被写进个人记忆；agent 之间污染策略 | 需要 user/group/agent/workspace namespace 和 isolation tests |
| Cost / latency | STATE-Bench、LongMemEval-V2、MemGym 开始关注 | memory system 准确但太慢；context gathering 成本高到不可上线 | 需要 accuracy-latency-cost Pareto eval、缓存、分层摘要、预算感知 retrieval |
| Eval realism | STATE-Bench 和 MemGym 推进明显，但许多 benchmark 仍 synthetic/offline | benchmark 过了，真实企业流程仍失败 | 需要真实工具 sandbox、可变用户模拟器、state assertions、human handoff case |
| Observability / replay | 普遍弱。许多系统只看最终答案 | 只知道 pass rate 降，不知道错在写入、检索、压缩、工具还是 judge | 需要 memory trace、episode replay、diff、scorer breakdown、failure taxonomy |

缺口压缩成一句话：

> 2026 年以后，memory infra 的难点不在“有没有一个向量库”，而在“长期上下文进入系统后，谁决定它变成什么状态、对谁可见、何时失效、如何纠正、如何证明它真的改善任务表现”。

## 五、机会地图

### 机会 A：Agent Memory Eval Harness

| 字段 | 内容 |
|---|---|
| Target user | 正在做 coding agent、browser agent、customer support agent、internal workflow agent 的 builder |
| Painful failure mode | 加了 memory 后 demo 更聪明，但线上任务完成率、pass^k、成本和用户体验没有稳定改善；失败后不知道该修 prompt、retrieval、memory 写入还是工具流程 |
| Minimum viable artifact | 一个 `eval/` harness：episode replay、stateful tool sandbox、memory on/off A/B、pass@1 / pass^5、cost / latency、memory trace、failure class 标注 |
| First eval | 选 30-50 个真实或半真实 workflow episode，跑 no-memory、RAG-memory、structured-memory 三组，对比 task success、pass^5、tool call waste、retrieval tokens、UX judge |
| 为什么不是普通 RAG wrapper | 主语不是 retrieval，而是 memory 是否改善 agent runtime 行为 |

### 机会 B：Memory Write Policy 与 Correction Layer

| 字段 | 内容 |
|---|---|
| Target user | 已经有长期 memory 的个人 assistant、团队 assistant、agent app |
| Painful failure mode | agent 乱写长期记忆；用户纠正后旧记忆仍污染后续任务 |
| Minimum viable artifact | memory mutation layer：每条写入带 type、scope、confidence、source episode、expiry、supersedes、correction status；提供 create/update/archive/override policy |
| First eval | 构造 100 条 episode stream，包含偏好变化、政策变化、用户纠正、矛盾事实。测 stale recall rate、wrong persistence rate、correction success、unwanted write rate |
| 为什么不是普通 RAG wrapper | 它解决 corpus 如何从 agent 运行中生成、变更、失效和被纠正，是写侧和治理侧问题 |

### 机会 C：Group Memory Namespace 与 Isolation Harness

| 字段 | 内容 |
|---|---|
| Target user | Slack / Discord / Teams / Linear / Notion / GitHub 等多人协作环境中的 agent builder |
| Painful failure mode | agent 混淆“谁说的、谁知道、谁允许、谁应该看到”；团队讨论和个人记忆互相污染 |
| Minimum viable artifact | group memory runtime：user / group / workspace / agent namespace，speaker-grounded facts，audience policy，channel-level memory，visibility resolver，leakage test suite |
| First eval | 复刻 GroupMemBench 六类 query，再加权限泄露题和纠错题。测 speaker attribution、audience adaptation、forbidden context leakage、abstention correctness |
| 为什么不是普通 RAG wrapper | 多人 memory 先问“这个 asker 能不能看、这个事实属于谁、对哪个 audience 成立” |

### 机会 D：Environment Experience Runbook

| 字段 | 内容 |
|---|---|
| Target user | browser / coding / internal tools agent 的 builder |
| Painful failure mode | agent 每次都像新人一样重新探索 UI、API、仓库、测试环境和隐藏坑；同一个 workflow 反复失败 |
| Minimum viable artifact | runbook memory system：把 episode trace 自动压成 environment affordance、workflow steps、gotchas、state invariants、tool recipes，并能按任务检索和回放证据 |
| First eval | 选一个真实 repo 或 web app，录制 50-100 条任务轨迹。测 first-try success、重复错误率、探索步数、runbook retrieval precision、延迟 |
| 为什么不是普通 RAG wrapper | 它从执行轨迹中提取可复用经验，核心对象是 workflow knowledge、state dynamics 和 recurring failure modes |

### 机会 E：Memory Observability / Replay Debugger

| 字段 | 内容 |
|---|---|
| Target user | 已经上线 agent 或准备上线的 infra/platform builder、AI product engineer、forward deployed engineer |
| Painful failure mode | 用户报告“agent 记错了”或“重复犯错”，团队只能看最终对话，无法知道是哪次写入、哪次 retrieval、哪次压缩导致问题 |
| Minimum viable artifact | trace viewer：展示 episode timeline、memory writes、retrieval set、context assembly、tool calls、state diff、judge result；支持 replay with patch 和 memory diff |
| First eval | 对 20 个已知失败 episode 做 root-cause annotation，测 debugger 是否减少定位时间、提高修复准确率，并把修复后 episode 纳入 regression |
| 为什么不是普通 RAG wrapper | 它观察的是 memory 生命周期和 agent episode 的因果链，目标是可靠性工程 |

## 六、对本地项目与职业主线的含义

本地 [Harness 架构判断框架](../frameworks/Harness架构判断框架.md) 已经有一个关键判断：agent 的很多进步来自外层控制壳，而不是模型本身。Context infra 正是这个控制壳里正在变成独立主语的一层。

与本地 [AI 系统产品判断框架](../frameworks/AI系统产品判断框架.md) 对齐后，可以得到一个更清楚的定位：

> agent context infra 不是“AI memory API”，而是 agent runtime 的 context lifecycle layer，负责历史经验的写入、组织、隔离、调度、纠错、回放和评测。

这也对个人项目路线有直接启发：

1. `gogo / oh-share-it` 适合承载 context database / local wiki / routed context 的证据。
2. `my-little-agent-loop` 适合承载 runtime ownership，比如 session policy、tool routing、trace/replay、evaluator loop。
3. 如果要做简历级旗舰项目，优先补 `eval / replay / observability / write policy`，而不是再扩一个普通 RAG 功能。
4. 最短证据包不是“功能很多”，而是有一组真实或半真实 episode，能展示 context 改造前后 task success、pass^k、cost、latency、failure class 的变化。

这和 [Anthropic 与 OpenAI 的 Agent Systems 履历 North Star](Anthropic与OpenAI的Agent%20Systems履历North%20Star.md) 也一致：目标画像不是“做过几个聪明 demo”，而是拥有过可部署、可评估、可迭代、可观测的 agent system。

## 七、建议的最小研究产物路线

如果把这次调研转成 2-4 周的可展示项目，建议这样收束：

| 周期 | 产物 | 成功标准 |
|---|---|---|
| 第 1 周 | 选一个 domain，收集 30-50 个 episode，定义 failure taxonomy 和 baseline | 能跑 no-memory / naive RAG / structured memory 三组 |
| 第 2 周 | 加 memory trace、write log、retrieval log、state assertions、pass^k 和 cost | 每个失败 episode 能定位到至少一个 failure class |
| 第 3 周 | 实现一个明确 runtime ownership 模块，例如 write policy 或 namespace isolation | 至少一个关键指标显著改善，而不是只换模型 |
| 第 4 周 | 写公开报告：benchmark、失败案例、修复、指标变化、残余缺口 | 能被看成 agent systems 证据包，而不是 demo README |

这个路线最符合 `context / harness / eval / reliability` 主线。它也能把今天的调研自然转成作品集资产。

## 来源依据

### 研究与 benchmark

- [Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670)
- [From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716)
- [AI Agents Need Memory Control Over More Context](https://arxiv.org/abs/2601.11653)
- [Active Context Compression: Autonomous Memory Management in LLM Agents](https://arxiv.org/abs/2601.07190)
- [Contextual Memory Virtualisation](https://arxiv.org/abs/2602.22402)
- [Memori](https://arxiv.org/abs/2603.19935)
- [MemMachine](https://arxiv.org/abs/2604.04853)
- [STATE-Bench](https://opensource.microsoft.com/blog/2026/05/19/introducing-state-bench-a-benchmark-for-ai-agent-memory/)
- [MemoryAgentBench](https://openreview.net/pdf?id=DT7JyQC3MR)
- [GroupMemBench](https://arxiv.org/abs/2605.14498)
- [StructMemEval](https://arxiv.org/abs/2602.11243)
- [LongMemEval-V2](https://arxiv.org/abs/2605.12493)
- [MemGym](https://arxiv.org/abs/2605.20833)

### 工程系统

- [MCP docs](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [A2A Protocol Specification](https://google-a2a.github.io/A2A/specification/)
- [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents)
- [OpenAI Agents SDK Sessions](https://openai.github.io/openai-agents-js/guides/sessions/)
- [LangGraph memory docs](https://docs.langchain.com/oss/python/concepts/memory)
- [Letta stateful agents](https://docs.letta.com/guides/core-concepts/stateful-agents)
- [Cloudflare Agents memory](https://developers.cloudflare.com/agents/concepts/memory/)
- [Mem0 docs](https://docs.mem0.ai/introduction)
- [Zep Memory docs](https://help.getzep.com/v2/memory)
- [Graphiti docs](https://help.getzep.com/graphiti/getting-started/welcome)
- [OpenViking](https://www.openviking.ai/)
- [OpenViking GitHub](https://github.com/volcengine/OpenViking)

### 本地知识库

- [Agent Context Infra 来源清单](../../raw/external/agent-context-infra-source-list-2026-05-24.md)
- [Harness 架构判断框架](../frameworks/Harness架构判断框架.md)
- [AI 系统产品判断框架](../frameworks/AI系统产品判断框架.md)
- [研究判断框架](../frameworks/研究判断框架.md)
- [coding agent 的上下文压缩工作流](../knowledge/coding%20agent%20的上下文压缩工作流.md)
- [volcengine/openviking 仓库地图](../knowledge/volcengine-openviking-repo-map.md)
- [Agent 岗位 JD 抽样与能力信号](../knowledge/Agent岗位JD抽样与能力信号.md)
- [Anthropic 与 OpenAI 的 Agent Systems 履历 North Star](Anthropic与OpenAI的Agent%20Systems履历North%20Star.md)

