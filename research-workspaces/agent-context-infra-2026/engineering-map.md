# Agent Context Infra 工程产品 / 开源项目地图草稿

截至日期：2026-05-24

这份草稿把 `agent context infra` 看成一条 context lifecycle，而不是一组互相替代的产品名。它关心的问题是：context 从哪里来、怎么被写入、怎么被取回、何时压缩、如何隔离、谁能治理、如何观察、如何评测。评价标准不是“谁最强”，而是这套系统是否足够 `inspectable`、`correctable`、`scoped`、`testable`、`reusable`。

## 一、总体判断

今天的 agent context infra 大致分成六类：

1. `connector/protocol layer`：MCP、A2A。它们主要解决连接和互操作，不直接解决长期记忆质量。
2. `stateful agent runtime`：OpenAI Agents SDK、LangGraph、Cloudflare Agents、Letta。它们把 agent loop、状态、工具、审批、长任务、消息历史放进运行时。
3. `memory-as-a-service / memory layer`：Mem0、Zep/Graphiti、Mastra。它们把“记忆写入与召回”产品化，重点在跨会话复用、图结构、线程/资源、语义召回。
4. `context database/file-system layer`：OpenViking，以及文件系统式 context、repo skill、`AGENTS.md` 思路。它们把 context 从“检索结果”变成可浏览、可定位、可审计的上下文空间。
5. `coding-agent context workflow`：intentional compaction、subagent context isolation、Research/Plan/Implement、repo skills。它们不是单一产品，而是一组围绕复杂代码库上下文预算的工程纪律。
6. `eval/observability layer`：STATE-Bench、LangSmith、Braintrust、Phoenix 等。它们把 context 系统的成败从“看起来记住了”推进到“任务是否更可靠、路径是否可解释、回归是否可抓住”。

一个有用的分层方式是：

- 协议层负责 `source / retrieve / govern` 的接口边界。
- runtime 层负责 `store / retrieve / compress / isolate / govern / observe` 的执行边界。
- memory 层负责 `store / retrieve / compress`，但治理和评测常依赖外层系统补齐。
- context database / file-system 层负责把 context 做成可检查、可纠正、可分区的工作面。
- coding workflow 层负责在一次任务内压缩事实、意图和执行空间。
- eval/observability 层负责 `observe / evaluate`，并反过来决定哪些 context 写入、保留或修正。

真正的工程分水岭不是有没有 memory，而是：

- 写入路径是否可见：哪些消息、工具调用、文件、任务经验被写进去了。
- 读取路径是否可解释：agent 为什么拿到这些 context，而不是另一些。
- 作用域是否明确：user、thread、project、repo、agent、org、task 的边界是否能分开。
- 压缩是否可纠正：摘要、profile、memory item、skill 是否能审阅、编辑、回滚。
- 评测是否对齐真实任务：不只测“能否找回某事实”，而是测“是否让 agent 更可靠地完成多步任务”。

## 二、Context lifecycle 责任矩阵

| Lifecycle 动作 | 核心问题 | 主要承载层 | 代表系统 | 工程风险 |
|---|---|---|---|---|
| `source` | context 从哪里进入系统 | protocol、runtime、memory、filesystem | MCP servers、A2A messages、Zep `memory.add`、OpenViking resources/session、AGENTS.md | 来源边界不清，混入过时、无权、不可审计信息 |
| `store` | context 如何持久化 | runtime、memory、context database | LangGraph checkpointer/store、Letta DB、Cloudflare Durable Objects、Mem0、Zep graph、OpenViking `viking://` | 写入粒度过粗或过细，后续无法纠错 |
| `retrieve` | agent 如何拿回相关 context | protocol、memory、filesystem、runtime | MCP resources/tools、Zep `memory.get`、LangGraph Store search、OpenViking recursive retrieval | 黑盒召回、只相似不相关、缺少 retrieval trajectory |
| `compress` | 长历史如何降噪降 token | runtime、workflow、context database | OpenAI Responses compaction session、Letta compaction、intentional compaction、OpenViking L0/L1/L2 | 压缩丢失证据，摘要污染长期状态 |
| `isolate` | 不同任务/线程/agent 如何不互相污染 | runtime、workflow、protocol | LangGraph thread state、OpenAI Sessions、Cloudflare Agent instance、subagents、A2A opaque agents | 跨线程泄漏、主上下文被探索噪音污染 |
| `govern` | 谁能读、写、删、调用、审批 | protocol、runtime、filesystem、obs | MCP auth/permissions、A2A security schemes、OpenAI guardrails/HITL、OpenViking namespace policy、AGENTS.md scope | 工具/记忆权限变成旁路，指令优先级不清 |
| `observe` | 能否看见 agent 做了什么 | runtime、obs、context database | LangSmith traces、Phoenix traces、Braintrust logs、OpenViking retrieval trajectory、OpenAI tracing | 只记录 final answer，不记录 context path |
| `evaluate` | context 是否改善任务结果 | eval layer、runtime | STATE-Bench、Braintrust experiments、Phoenix evals、LangSmith datasets/evals、OpenAI eval workflows | 只测 retrieval 命中，不测任务成功和一致性 |

## 三、六类系统地图

### 1. Connector / protocol layer：MCP 与 A2A

MCP 的定位是把 AI 应用连接到外部系统。官方介绍把 MCP 描述为面向数据源、工具和工作流的开放标准，可让 Claude、ChatGPT 等 AI 应用连接本地文件、数据库、搜索、计算器、专业 prompt 等外部能力。Anthropic 2024-11-25 的发布说明强调，MCP 用统一协议替代碎片化集成，让开发者暴露 MCP server，或让 AI 应用作为 MCP client 连接这些 server。

在 context lifecycle 里，MCP 主要负责：

- `source`：把文件、数据库、SaaS、工具、workflow 暴露给 agent。
- `retrieve`：通过 tools/resources/prompts 让 agent 按需取 context。
- `govern`：通过 server/client、transport、auth、tool schema、权限配置约束访问。
- `observe`：MCP 本身不是 observability 系统，但标准化调用面让 tracing 更容易挂上去。

MCP 不天然负责：

- 长期记忆质量。
- 写入策略。
- 压缩策略。
- 检索结果是否真的足够好。

所以 MCP 更像 context 的“接口层”，不是 memory system。一个 MCP server 可能只暴露 `grep`，也可能暴露一个完整 context database，比如 OpenViking 的 MCP endpoint。

A2A 的定位不同。A2A specification 把它定义为 independent、potentially opaque agent systems 之间的互操作协议，目标包括发现能力、协商 text/file/structured data 等交互模态、管理协作任务，并在不需要访问彼此内部状态、memory 或 tools 的情况下安全交换信息。

在 context lifecycle 里，A2A 主要负责：

- `source`：来自另一个 agent 的 message、artifact、task state。
- `retrieve`：通过 task query、message history、artifact 获取跨 agent context。
- `isolate`：远端 agent 保持 opaque，调用方不直接进入对方内部 memory/tool。
- `govern`：Agent Card、security schemes、认证、授权、task cancellation 等协议对象。

A2A 的价值在于把“另一个 agent”当协作主体，而不是普通 tool。它补的是跨组织、跨框架的 agent-to-agent 边界；MCP 补的是 agent-to-tool/data 边界。两者可以互补：一个 agent 可以用 MCP 调工具，也可以用 A2A 委托另一个 agent。

工程判断：协议层越标准化，越容易复用连接器；但协议标准化不等于 context 正确。真正需要额外设计的是权限、写入策略、retrieval quality、trace 和 eval。

### 2. Stateful agent runtime：OpenAI Agents SDK、LangGraph、Cloudflare Agents、Letta

这一层的共同问题是：agent 不是一次 LLM 调用，而是长流程运行体。它需要保存状态、调用工具、支持中断恢复、协调多个 specialist、管理上下文窗口、提供 guardrails 和 traces。

OpenAI Agents SDK 的官方定位是 code-first agent app：当应用自己拥有 orchestration、tool execution、approvals、state 时使用 SDK。它覆盖 agent definitions、running agents、orchestration/handoffs、guardrails/HITL、results/state、integrations/observability、evaluation。TypeScript Sessions 文档进一步把 session 定义为 SDK 的 persistent memory layer：runner 会取回历史 items、在 run 后持久化新输入与输出，并可接入自定义 Redis/DynamoDB/SQLite 等后端。`OpenAIResponsesCompactionSession` 则把长 history 自动压缩成更短等价 items。

OpenAI Agents SDK 在 lifecycle 中的位置：

- `store`：Session、Conversations API、自定义 session backend。
- `retrieve`：每次 run 前把 history prepend 到输入。
- `compress`：Responses compaction session。
- `isolate`：agent、handoff、session、RunState。
- `govern`：guardrails、人类审批、tool approval、sandbox。
- `observe/evaluate`：SDK tracing、OpenAI eval workflow。

LangGraph 更偏状态机/图执行 runtime。LangChain memory 文档把 memory 分成 short-term/thread-scoped 和 long-term/cross-session。短期记忆是 graph state，通过 checkpointer 持久化，可在 step 之间恢复；长期记忆保存在 namespace/key 结构的 Store 中，支持 semantic search 和过滤。它还把 long-term memory 拆成 semantic、episodic、procedural，并明确 memory writing 有 hot path 与 background 两种。

LangGraph 在 lifecycle 中的位置：

- `store`：thread state/checkpointer、Store namespace/key。
- `retrieve`：step 开始读 state，Store search 取 long-term memory。
- `compress`：通过 message trimming、summary、manual forgetting、background memory writer 实现。
- `isolate`：thread、namespace、graph state。
- `govern`：由应用代码、namespace、graph 节点和 LangSmith 配套补齐。
- `observe/evaluate`：LangSmith traces/datasets/evals。

Cloudflare Agents 则把 agent runtime 建在 Durable Objects 上。官方文档说明 `Agent` 是 DurableObject 的 extension，Durable Object 本身是 globally addressable、single-threaded compute instance，带 long-term KV/SQLite storage。Agent layer 提供自动 state persistence、WebSockets、scheduling、RPC、queue、MCP 等。Durable execution 文档中的 `runFiber()` 把任务注册到 SQLite，支持 checkpoint/stash，并在对象被 evict 后恢复。

Cloudflare Agents 在 lifecycle 中的位置：

- `store`：Durable Object storage、SQLite、agent state。
- `retrieve`：同一个 globally addressable agent instance 读取自身状态。
- `compress`：不是核心内建抽象，更多依赖应用层或 memory 组件。
- `isolate`：每个 Durable Object/Agent instance 自带 identity 和单线程顺序执行。
- `govern`：Worker/DO 路由、auth、MCP governance、平台权限。
- `observe`：Cloudflare Agents 文档提供 observability 入口。
- `evaluate`：需要外接 eval harness。

Letta 的核心是 stateful agents。官方文档说 stateful agents 能跨 conversations 维护 memory/context；Letta 把 memories、user messages、reasoning、tool calls 持久化到数据库，即使被 context window evict 也不会丢失。它用 memory blocks 组织可被 agent 工具编辑的 context，并支持 shared memory blocks、messages、runs/steps、conversations、compaction、MCP tools、server tools、Letta Evals。

Letta 在 lifecycle 中的位置：

- `store`：所有 agent state 持久化到 DB。
- `retrieve`：core memory 注入 context window，旧消息可通过 API/retrieval tools 取回。
- `compress`：message compaction/eviction 后仍保留可取回历史。
- `isolate`：agent、conversation、memory block。
- `govern`：server-side tools sandbox、MCP/client/server tools、RBAC。
- `observe/evaluate`：runs/steps 与 Letta Evals。

工程判断：runtime 层的成熟度不只看“能不能跑 agent”，而要看它是否把 state、approval、tool execution、compaction、trace、eval 都放在可被产品工程使用的位置。

### 3. Memory-as-a-service / memory layer：Mem0、Zep/Graphiti、Mastra

这一层把 memory 从 runtime 内部实现拆成独立服务或框架组件。它的核心不是执行 agent loop，而是回答：什么值得记，如何检索，如何跨会话复用，如何避免记忆漂移。

Mem0 自称 universal, self-improving memory layer for LLM applications。Quickstart 展示的基本路径是 `client.add(messages, user_id=...)` 写入，再用 `client.search(query, filters={user_id})` 召回。文档也提到 Mem0 Platform、Open Source、自托管、Integrations、Mem0 MCP、metadata filtering、graph memory、webhooks 等。

Mem0 的 lifecycle 责任：

- `source`：chat messages、应用传入数据、MCP 操作。
- `store`：hosted 或自托管 memory backend。
- `retrieve`：search memories，按 user/filter 召回。
- `compress`：把对话提取成 memory item。
- `govern`：平台 API key、filters、metadata；更复杂的审计要看具体部署。
- `evaluate`：有 memory evaluation 文档入口，但生产级任务评测仍建议外接 STATE-Bench/Braintrust 等。

Zep 的 Memory API 是更 opinionated 的 high-level memory。官方文档说 `memory.add` 接收 session-specific chat messages，Zep 存储 chat history 并从 messages 构建 user-level knowledge graph；`memory.get` 用 session 最新消息决定用户图中最相关 context，返回 context string、recent chat messages、raw facts。Zep 还提供 Graph API 用于低层 graph add/search/read，自定义 retrieval 和 context string。Graphiti 是 Zep 的开源 temporal graph library，用于构建和更新时间感知知识图谱。

Zep/Graphiti 的 lifecycle 责任：

- `source`：chat history、JSON、unstructured text、business data。
- `store`：temporal knowledge graph，包含 entity nodes、entity edges、episodic nodes。
- `retrieve`：`memory.get` 高层 context string，Graph API 搜索 graph。
- `compress`：从 messages 和 data 中抽取 facts/summaries/graph relationships。
- `govern`：user/session/group graph 边界，fact rating/filter。
- `evaluate`：自身不是 benchmark，适合接入 STATE-Bench 这类 memory-agnostic benchmark。

Mastra 是更宽的 TypeScript agent framework，但其 Memory API 可以放进 memory layer。公开文档索引显示它覆盖 Threads and Resources、Working Memory、Conversation History、Semantic Recall、Memory Processors、storage backends，并有 Evals/Scorers、AI Tracing、Braintrust/Langfuse/LangSmith/OpenTelemetry exporter 等生态接口。

Mastra 的 lifecycle 责任：

- `source`：agent conversation、thread/resource、workflow context。
- `store`：Memory class、thread/resource storage、LibSQL/Postgres/Upstash 等 backend。
- `retrieve`：working memory、semantic recall、conversation history。
- `compress`：memory processors、message/context processors。
- `govern`：应用层资源边界、auth、storage backend。
- `observe/evaluate`：Mastra Cloud observability、AI tracing、scorers/evals/exporters。

工程判断：memory layer 的关键问题是“记忆的产品语义”。单纯 `add/search` 容易变成向量库包装；更强的系统会区分 user/session/group、semantic/episodic/procedural、hot path/background、profile/collection、fact rating、memory processors，并允许人或 eval 纠正。

### 4. Context database / file-system layer：OpenViking 与文件系统式 context

OpenViking 是这一类里最明确的 context database。GitHub README 把它定位为面向 AI Agents 的 open-source Context Database。它认为传统 RAG 的问题包括 fragmented context、context demand surging、flat storage 导致 retrieval 效果差、retrieval chain 不可观察、memory iteration 有限。它的解法是用 file system paradigm 统一管理 memories、resources、skills，提供 L0/L1/L2 tiered context loading、directory recursive retrieval、visualized retrieval trajectory、automatic session management。

本地知识库里已有 `volcengine/openviking 仓库地图`，它对仓库实现做过更深一层拆解：OpenViking 把 resources、user memory、agent memory、skills、sessions 统一进 `viking://` 虚拟文件系统；agent 可用 `ls/tree/read/find/grep` 这类文件式范式先定位目录、读摘要，再按需读全文；session commit 会把对话、工具使用和任务经验回写成长记忆；server 还内置 MCP endpoint，把 context 操作暴露给外部 agent/client。

OpenViking 的 lifecycle 责任：

- `source`：resources、sessions、skills、agent/user memory。
- `store`：context database + `viking://` namespace。
- `retrieve`：目录递归检索、semantic search、grep/glob/read/list。
- `compress`：L0 abstract、L1 overview、L2 原文/详情；session 自动压缩和 memory extraction。
- `isolate`：account/user/agent namespace、session boundary。
- `govern`：server auth mode、API key、trusted mode、namespace policy、MCP identity middleware。
- `observe`：visualized retrieval trajectory、observer/metrics。
- `evaluate`：仓库有 benchmark 目录，但仍需区分 README 级效果宣称与可复现实验。

文件系统式 context 不只指 OpenViking。`AGENTS.md`、repo skills、rules、local wiki、`raw -> wiki` 分层也是同一思想的轻量版本：把 context 变成可读、可 diff、可按目录继承、可被人维护的文件，而不是只存在向量索引或聊天历史里。`agents.md` 项目把 `AGENTS.md` 描述成面向 coding agents 的 README：一个可预测位置，用来提供项目上下文与操作说明；最近的文件对更深层目录生效，从而支持 subproject-specific instructions。

这类文件系统式 context 的 lifecycle 责任：

- `source`：人维护的规则、经验、命令、架构说明、测试策略。
- `store`：repo 文件、skills 目录、local wiki、context docs。
- `retrieve`：agent 启动时读取，或 resolver/skill 按需加载。
- `compress`：把反复出现的经验压成规则、skill、index、framework。
- `isolate`：目录作用域、workspace、project、skill trigger。
- `govern`：git review、code review、owner、instructions precedence。
- `observe/evaluate`：通过任务结果、review、CI、agent trace 反馈修正。

工程判断：context database 与文件系统式 context 的共同优势是 inspectability。它们让 context 不再只是“模型记得什么”，而是变成可浏览、可引用、可编辑、可回滚的资产。代价是系统必须维护目录语义、命名空间、写入纪律和权限边界。

### 5. Coding-agent context workflow：压缩、隔离、三段式工作流、repo skills

这一类不是单个产品，而是今天复杂代码库里最有用的一组操作系统。

本地页 `coding agent 的上下文压缩工作流` 已经把核心讲得很清楚：brownfield codebase 里的关键不是一直对话，而是持续压缩上下文，把有限上下文预算留给高杠杆推理与修改。它把 context window 当工作台，而不是仓库。

核心模式有四个。

第一，`intentional compaction`。它不是“总结聊天”，而是把当前任务状态压成结构化 markdown，保留目标、相关文件、已确认事实、失败路径、下一步。它解决的是长对话进入 `dumb zone` 后的上下文污染。

第二，subagent context isolation。subagent 最重要的作用往往不是角色扮演，而是让探索噪音留在子上下文里。父上下文只接收压缩后的结论，比如“哪些文件相关、为什么相关、下一步看哪里”。

第三，`Research -> Plan -> Implement`。这不是形式感，而是三次压缩：

- Research 压缩事实：系统怎么工作，相关文件在哪里，约束是什么。
- Plan 压缩意图：要改什么，顺序是什么，如何验证。
- Implement 压缩执行空间：按已审过的计划在较小空间里行动。

第四，repo skills。`Thin Harness, Fat Skills` 的本地页把 skill files 看成可复用程序：Markdown 里写流程、判断、触发条件、参数。它们和 repo rules、`AGENTS.md`、local scripts 一起构成 agent 可以按需加载的 procedural context。好的 skill 不是把所有知识塞进主 prompt，而是让 resolver 在正确时刻加载正确上下文。

这类 workflow 的 lifecycle 责任：

- `source`：代码库、工具输出、错误日志、review 反馈、人类判断。
- `store`：research notes、plans、skills、AGENTS.md、summary files。
- `retrieve`：按任务阶段、skill trigger、目录规则读取。
- `compress`：intentional compaction、plan、facts summary。
- `isolate`：subagents、worktrees、task files、separate sessions。
- `govern`：human review of research/plan、CI、permissions、sandbox。
- `observe/evaluate`：diff、tests、review、trace、postmortem、skill improvement。

工程判断：coding-agent context workflow 是最接近“可操作工程纪律”的部分。它不假设底层 memory 足够聪明，而是把上下文预算、探索噪音、任务边界、人类审阅点显式化。

### 6. Eval / observability layer：STATE-Bench、LangSmith、Braintrust、Phoenix

这一层回答的问题是：context infra 到底有没有让 agent 做得更好。

STATE-Bench 是截至 2026-05-24 最值得纳入的 memory-specific eval 信号。Microsoft Open Source 2026-05-19 发布的介绍把它定义为 open-source、memory-agnostic benchmark，用来衡量 agents 是否能在 realistic enterprise tasks 上“with experience” 改善表现。它不是只测 50 轮前的名字能否找回，而是测 customer support、travel、shopping 三个域的 450 个任务，覆盖 policy compliance、information synthesis、多步程序。指标包括 task completion rate、pass^5 reliability、agent efficiency、user experience score。它提供 tasks、environment、tools、user simulator、scoring，并支持 bring your own memory。

STATE-Bench 的关键贡献是把 memory eval 从“retrieval works”推进到“procedure/state/user experience 是否改善”。这正好补上 memory layer 常见的自我证明不足。

LangSmith 是 LangChain/LangGraph 生态里的 traces/evals/monitoring 层。LangChain 文档说 LangChain agents 自动支持 LangSmith tracing；traces 会记录从用户输入到最终响应的每一步，包括 tool calls、model interactions、decision points。它适合观察 graph runtime 的 step-level behavior，并把 production traces 转成 datasets/evals。

Braintrust 更偏评测与生产闭环。官方 docs 把 systematic evaluation 描述成从 playground iteration、experiment snapshot、CI/CD eval、production online scoring、feedback into datasets 的完整循环。它明确支持 multi-step agent、retrieval pipeline、custom workflow 作为 task，scorers 可以是 code-based 或 LLM-as-judge。

Phoenix 是 open-source AI observability/evaluation 平台。官方 docs 说 Phoenix 用 traces 帮你看 run 中到底发生了什么，用 eval tests 标记失败和回归，用 production examples 迭代 prompts，并基于 OpenTelemetry/OpenInference instrumentation。它的优势是开放协议和本地/自托管友好，适合把 model calls、retrieval、tool use、custom logic 串成分布式 trace。

工程判断：observability 不等于 evaluation。trace 告诉你 context path 是什么；eval 告诉你这个 path 是否产生了更可靠的结果。好的 agent context infra 需要二者闭环：从 trace 找 failure mode，从 eval 判断改动是否改善，再把经验写回 memory、skill、rule 或 dataset。

## 四、系统比较表

| System | Category | Context abstraction | Write path | Read path | Governance | Eval story | Maturity |
|---|---|---|---|---|---|---|---|
| MCP | connector/protocol | server 暴露的 tools/resources/prompts | server 实现写操作或只读资源 | client 调用 tool/resource | transport/auth/tool schema/permissions，依赖实现 | 本身无 eval，需外接 trace/eval | 标准生态成熟度高，但质量依赖具体 server |
| A2A | connector/protocol | Agent Card、Task、Message、Part、Artifact | agent 间 message/task/artifact 交换 | task query、message history、artifact | security schemes、auth、authorization、task cancellation | 本身无 eval，适合评测跨 agent delegation | 标准化中，适合企业 agent 互操作 |
| OpenAI Agents SDK | stateful runtime | Agent、Run、Session、RunState、tool/handoff/guardrail | Session 持久化 inputs/outputs，自定义 backend | run 前自动取历史，handoff/tool 读上下文 | guardrails、HITL、approvals、sandbox、MCP | tracing + OpenAI eval workflows | 成熟产品路径，适合 code-first runtime |
| OpenAI Responses Compaction Session | runtime compression | compacted conversation items | run 后触发 `responses.compact`，清空并重写 session | 下轮读取压缩后 items | trigger hook、storage backend、developer policy | 可通过 trace/eval 比较压缩前后效果 | 新但工程语义清晰 |
| LangGraph | stateful runtime | graph state、thread checkpoint、Store namespace/key | graph step 更新 state，Store 写 long-term memory | step 读 state，Store search | namespace、application logic、LangSmith | LangSmith datasets/evals | 开源生态成熟，适合图式流程和可恢复状态 |
| Cloudflare Agents | stateful runtime | Durable Object-backed Agent instance | `setState`、SQLite/KV、fiber checkpoint | 同一 globally addressable Agent 读取状态 | Workers/DO auth、routing、MCP governance | 需外接 eval；平台提供 observability | 平台级 runtime 成熟，agent 抽象仍在演进 |
| Letta | stateful runtime | stateful agent、memory blocks、messages、runs/steps | messages/tool calls/reasoning/memory 写入 DB | core memory 注入，旧消息通过 API/tool 取回 | tool sandbox、MCP/client/server tools、RBAC | Letta Evals | stateful agent 语义强，适合 memory-first runtime |
| Mem0 | memory layer | memory items per user/filter | `client.add(messages, user_id)`、MCP/tool 写入 | `client.search(query, filters)` | API key、metadata filters、hosted/self-host boundary | memory eval 入口，建议外接 task benchmark | 产品化程度高，抽象简洁 |
| Zep | memory layer | user/session/group temporal graph context | `memory.add` chat messages，Graph API 加 data | `memory.get` context string，Graph API search | user/session/group graph、fact rating/filter | 需外接 STATE-Bench/Braintrust 等 | 高层 API 成熟，graph 语义强 |
| Graphiti | memory/graph layer | temporal knowledge graph | episodes、text/JSON、entity/edge 更新 | hybrid semantic/keyword/graph search | 由应用/部署控制 | 需外接 eval | 开源组件，适合自建 graph memory |
| Mastra Memory | memory/runtime component | thread、resource、working memory、semantic recall | agent/workflow 写 memory/thread | working memory、conversation history、semantic recall | storage backend、resource/thread boundary | Mastra scorers/evals + exporters | JS agent 框架内成熟，纯 memory SaaS 属性较弱 |
| OpenViking | context database/filesystem | `viking://` virtual filesystem，resources/memory/skills/sessions | add_resource、store/session commit、memory extraction | ls/tree/read/find/grep/search，directory recursive retrieval | account/user/agent namespace、API key、auth mode、MCP identity | benchmark 目录 + 可外接 eval；需验证可复现性 | 新兴但设计完整，inspectability 强 |
| 文件系统式 context | context filesystem | docs、rules、skills、index、raw/wiki、plans | 人或 agent 写 Markdown/JSON/代码旁文档 | agent 启动/按需读取，resolver/skill 加载 | git、review、目录作用域、owner | tests/review/trace 间接验证 | 低技术风险，高维护纪律要求 |
| AGENTS.md | repo context workflow | repo/目录级 agent instruction file | 人维护规则、命令、边界 | coding agent 读取最近/上层 AGENTS.md | precedence、directory scope、code review | 需任务级 benchmark 或 review 验证 | 实用成熟，效果取决于具体性和加载可靠性 |
| Repo skills | coding workflow | procedural markdown capability | 经验复盘后 codify 成 skill | trigger/resolver 按需加载 | review、版本控制、触发条件 | 通过任务复用率、失败率、review 质量验证 | 对 coding agents 高杠杆，标准化仍分散 |
| Intentional compaction | coding workflow | task-state summary | 当前上下文压成结构化状态 | 新 session 从 summary 恢复 | 人审 compaction，文件可 diff | 通过接力成功率、返工率验证 | 方法成熟，产品化程度低 |
| Subagent context isolation | coding workflow | child context result summary | 子上下文探索，回传压缩结论 | 父上下文只读结论 | task boundary、tool permission、worktree | 比较主上下文污染/成功率 | 已成 coding agent 实操核心 |
| STATE-Bench | eval layer | memory-agnostic enterprise task benchmark | 运行 agent/memory 后产生 logs/results | scorer 读 final state、conversation、tool actions | benchmark task/schema/scorer | task completion、pass^5、efficiency、UX | 新发布但方向很对，值得作为 memory eval anchor |
| LangSmith | observability/eval | trace、run、dataset、experiment | auto trace LangChain/LangGraph agent | UI/API 查 execution steps | project、metadata、API key | traces + datasets/evals/monitoring | LangChain 生态成熟 |
| Braintrust | observability/eval | logs、experiments、datasets、scorers | instrumentation/production logs/eval runs | dashboards、experiments、online scoring | org/project access、CI gates | offline eval、CI、online scoring、feedback loop | 生产 eval 工作流强 |
| Phoenix | observability/eval | OpenTelemetry/OpenInference traces、evals、datasets | app sends traces/eval results | trace viewer、experiments、eval UI | self-host/cloud、RBAC/API keys/data retention | deterministic/LLM evals, trace scoring | 开源观测层成熟，适合可迁移 instrumentation |

## 五、横向取舍

### Inspectable：能不能看见 context path

最强的是文件系统式 context、OpenViking、LangSmith/Phoenix 这类 trace/context trajectory 明确的系统。最弱的是只暴露 `add/search` 的 memory API，如果它没有展示为什么写入、为什么召回、为什么压缩，就很难纠错。

### Correctable：能不能改错

文件、skills、AGENTS.md、LangGraph Store、Letta memory blocks、OpenViking `viking://` 理论上都比较可纠正。纯黑盒 memory service 如果只返回 memory item 而不暴露抽取依据、合并逻辑、删除机制，就容易积累长期污染。

### Scoped：边界是否清楚

A2A 的 opaque-agent 设计、Cloudflare Durable Object 的 per-agent instance、LangGraph thread/namespace、Zep user/session/group graph、OpenViking account/user/agent namespace 都在解决 scoped context。AGENTS.md 的目录作用域是轻量但很有效的版本。

### Testable：能不能证明更好

STATE-Bench 是目前 memory layer 最直接的 testable anchor。Braintrust、LangSmith、Phoenix 提供 eval/trace infrastructure，但具体 benchmark 仍要团队定义。对 coding agent workflow，最实用的 eval 往往是 brownfield tasks 的 pass rate、返工率、测试通过率、review 发现率、上下文接力成功率。

### Reusable：context 能不能复利

Repo skills、AGENTS.md、OpenViking skills/session memory、LangGraph procedural memory、Letta shared memory blocks 都在把一次经验转成可复用能力。关键是不要把所有东西写成长 prompt，而要做 resolver：何时加载哪份 context。

## 六、对工程产品地图的结论

1. MCP/A2A 是连接层，不是答案层。它们能降低集成成本，但不能替代 memory quality、context governance 和 eval。
2. Stateful runtime 正在把“agent loop”产品化。OpenAI Agents SDK、LangGraph、Cloudflare Agents、Letta 的共同方向是让状态、工具、审批、compaction、observability 成为一等对象。
3. Memory layer 的竞争点不应只看召回速度，而要看写入语义、作用域、纠错、事实评级、图结构、热路径/后台路径，以及能否在 STATE-Bench 这类任务评测中带来可靠性提升。
4. Context database/file-system layer 是 inspectability 最强的方向。OpenViking 的 `viking://`、L0/L1/L2、目录递归检索、session commit 值得重点跟踪，因为它把 context 从向量 chunk 提升成可浏览的工作空间。
5. Coding-agent context workflow 仍然是短期最高 ROI 的部分。intentional compaction、subagent isolation、Research/Plan/Implement、repo skills 不依赖某个 vendor，能立刻减少 brownfield 任务中的上下文污染。
6. Eval/observability 是所有层的闭环。没有 trace，context path 不可解释；没有 eval，memory 是否有用不可证明；没有 write-back，评测发现不会变成系统改进。

如果要把这张地图压成一句话：

> Agent context infra 的核心不是“给模型更多上下文”，而是把上下文变成可来源化、可存储、可取回、可压缩、可隔离、可治理、可观察、可评测、可复用的工程对象。

## 参考链接

- [MCP introduction](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [A2A specification](https://google-a2a.github.io/A2A/specification/)
- [OpenAI Agents SDK guide](https://developers.openai.com/api/docs/guides/agents)
- [OpenAI Agents SDK Sessions](https://openai.github.io/openai-agents-js/guides/sessions/)
- [LangChain/LangGraph memory overview](https://docs.langchain.com/oss/python/concepts/memory)
- [Letta stateful agents](https://docs.letta.com/guides/core-concepts/stateful-agents)
- [Mem0 introduction](https://docs.mem0.ai/introduction)
- [Mem0 quickstart](https://docs.mem0.ai/platform/quickstart)
- [Zep memory](https://help.getzep.com/v2/memory)
- [Zep graph overview](https://help.getzep.com/v2/understanding-the-graph)
- [Graphiti welcome](https://help.getzep.com/graphiti/getting-started/welcome)
- [Mastra Memory reference](https://mastra.ai/reference/memory/Memory)
- [Cloudflare Agents: Agent class internals](https://developers.cloudflare.com/agents/concepts/agent-class/)
- [Cloudflare Agents: Durable execution](https://developers.cloudflare.com/agents/api-reference/durable-execution/)
- [OpenViking website](https://www.openviking.ai/)
- [volcengine/OpenViking GitHub](https://github.com/volcengine/OpenViking)
- [STATE-Bench announcement](https://opensource.microsoft.com/blog/2026/05/19/introducing-state-bench-a-benchmark-for-ai-agent-memory/)
- [LangSmith observability docs](https://docs.langchain.com/oss/python/langchain/observability)
- [Braintrust evaluation docs](https://www.braintrust.dev/docs/evaluate)
- [Phoenix docs](https://arize.com/docs/phoenix)
- [AGENTS.md project](https://agents.md/)

## 本地参考页

- `wiki/frameworks/router.md`
- `wiki/frameworks/Harness架构判断框架.md`
- `wiki/frameworks/AI系统产品判断框架.md`
- `wiki/knowledge/coding agent 的上下文压缩工作流.md`
- `wiki/knowledge/volcengine-openviking-repo-map.md`
- `wiki/knowledge/ai-architect-context-intelligence.md`
- `wiki/knowledge/thin-harness-fat-skills.md`
- `wiki/knowledge/harness-engineering.md`
