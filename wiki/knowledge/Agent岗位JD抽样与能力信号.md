# Agent 岗位 JD 抽样与能力信号

**收集时间：** 2026-05-13  
**来源：** 各公司公开招聘页（Ashby / Greenhouse）  
**说明：** 这页是围绕 agent / applied AI / harness / eval / context system 相关岗位做的**人工抽样**，不是全市场统计。它适合用来校准能力要求，不适合拿来推断精确比例。

## 这页回答什么

这页主要回答三个问题：

1. 顶尖和强 AI-native 公司到底在招哪些 agent 相关角色。
2. 这些角色公开写出来的能力要求，重点落在哪些面。
3. “会 Claude Code / RAG” 之外，真正反复出现的高价值信号是什么。

## 抽样方法

本次只看公开可见信息，未 clone 仓库，也未读取私有数据。

抽样覆盖公司：

- `OpenAI`
- `Anthropic`
- `Cursor`
- `Cohere`
- `Sierra`
- `Harvey`
- `Perplexity`
- `Notion`
- `Replit`
- `Factory`
- `Poolside`

筛选原则：

- 只保留与 `agent / applied AI / harness / eval / context / deployment / infrastructure` 明显相关的角色。
- 优先保留最能代表公司真实能力重心的岗位，而不是泛泛的软件工程岗。
- 同一家公司只保留少数代表性角色，避免表格失真地偏向单一公司。

## 表 1：代表性岗位抽样

| 公司 | 代表岗位 | 公开链接 | 角色簇 | 年限要求 | JD 核心信号 | 说明 |
|---|---|---|---|---|---|---|
| OpenAI | Software Engineer, Agent Infrastructure | [link](https://jobs.ashbyhq.com/openai/c1316397-25bb-4add-9e9d-0e3ea8ba929a) | agent infra / runtime | 未显式写出 | training env, deployment, execution, production | 核心不是做 demo，而是做 agent 的训练环境与生产执行平台。 |
| OpenAI | Research Engineer, Codex | [link](https://jobs.ashbyhq.com/openai/793964ae-d40b-45e3-9798-84f4b6da48c5) | coding agent / applied research | 未显式写出 | experimentation, deployment, iteration, reliability, cost | 研究、工程、产品和部署被放在同一条链路里。 |
| Cursor | Software Engineer, Agent Harness | [link](https://jobs.ashbyhq.com/cursor/6e6f5bc2-eb32-40e2-bba9-cfa56479600d) | harness / platform | 未显式写出 | orchestration, tools, guardrails, execution environment | 重点是 agent loop、工具、默认 agent 体验，而不是“会用 Cursor”。 |
| Cursor | Software Engineer, Agent Evaluation and Quality | [link](https://jobs.ashbyhq.com/cursor/2bbe9f02-83a5-4173-98be-9085d1cb5693) | eval / quality | 未显式写出 | curated datasets, offline replay, scorers, regression, dashboards | 说明 eval infra 已经成为独立招聘面。 |
| Cohere | Applied AI Engineer – Agentic Workflows | [link](https://jobs.ashbyhq.com/cohere/1fa01a03-9253-4f62-8f10-0fe368b38cb9) | applied AI / workflow | 未显式写出 | enterprise, workflows, deploy models, customer value | 更偏把 agentic workflow 接入真实企业场景。 |
| Cohere | Senior Software Engineer, Agent Infrastructure | [link](https://jobs.ashbyhq.com/cohere/70664617-84f6-4ee8-a4f6-4037ebfda9db) | infra / platform | 未显式写出 | secure code execution, state management, model routing, auth, long-running workflows | bar 已经来到 runtime、identity、resource management 这一层。 |
| Sierra | Software Engineer, Agent Architecture | [link](https://jobs.ashbyhq.com/Sierra/b3829801-8e0b-4047-8cd8-8a51c87028fd) | agent SDK / runtime | 4+ years | Agent SDK, orchestration engine, runtime, retrieval, grounding, eval | 很典型的 L5-L6 画像：做 agent primitives，不是做 wrapper。 |
| Harvey | Software Engineer, Agents | [link](https://jobs.ashbyhq.com/harvey/0c3ccbfd-25d1-4f66-be9c-e3c680fbe2fc) | vertical applied agent | 2-5 years | context windows, tools, evals, task completion quality | 说明强 PMF 的垂直 AI 公司也在要 builder，不只是要 research。 |
| Perplexity | Member of Technical Staff (Software Engineer, Applied AI) | [link](https://jobs.ashbyhq.com/perplexity/3c656963-876a-458d-bca6-916a42a24c1a) | applied AI / context layer | 5+ years | memory, summarization, retrieval, ranking, evaluation, A/B testing | 直接把 `context layer`、产品实验、完整 AI lifecycle 绑在一起。 |
| Notion | Engineering Manager, Context (Agentic Search) | [link](https://jobs.ashbyhq.com/notion/801ab5f3-ccd7-43dd-96ac-6e59f7ab3b56) | context / search platform | 未显式写出 | search ranking, tool calls, memories, stability, latency, cost | 说明成熟产品公司把 agent 先落在 `context + search + memories` 上。 |
| Replit | Senior Software Engineer, Agent Platform | [link](https://jobs.ashbyhq.com/replit/b82de6f8-aebf-47b8-8bdc-39ea33807975) | agent platform | 5+ years | full-stack systems, backend services, dev experience, agent experience | 角色在 AI team 与 UX / product 之间搭桥，但本质仍是系统工程。 |
| Factory | AI Engineer | [link](https://jobs.ashbyhq.com/factory/2243dab2-62dc-4c64-b4bc-8f7314475607) | AI engineer / startup generalist | 2+ years | deploying agentic systems, stability, scalability, real-world feedback | 是相对可达的样本，但要求仍明显高于“会搓 demo”。 |
| Poolside | Member of Engineering (Agent Harness) | [link](https://jobs.ashbyhq.com/poolside/dd924ed3-329c-4916-9c66-936e3aaf1c74) | harness / orchestration | 未显式写出 | core agent framework, tools, orchestration environment, securely/reliably/at scale | 很清楚地把壁垒定义在 harness 和 scale 上。 |
| Anthropic | Model Quality Software Engineer, Claude Code | [link](https://job-boards.greenhouse.io/anthropic/jobs/5098025008) | eval infra / staff IC | 10+ years | evaluation infrastructure, research tooling, technical direction, scale | 这是很高 bar 的岗位，重点是 eval systems 与 research infra。 |
| Anthropic | Applied AI Engineer, Beneficial Deployments | [link](https://job-boards.greenhouse.io/anthropic/jobs/5068226008) | applied AI / deployment | 4+ years | evals, harnesses, prototyping agents, context engineering, cost optimization | 不是纯 research，而是高水平 applied builder + partner 技术支持。 |
| Anthropic | Research Engineer, Model Evaluations | [link](https://job-boards.greenhouse.io/anthropic/jobs/5198255008) | eval research | 未显式写出 | capabilities metrics, live checkpoints, infra at scale | 把“什么算智能、怎么量化”本身当成岗位主语。 |
| Anthropic | Research Engineer, Virtual Collaborator (Cowork) | [link](https://job-boards.greenhouse.io/anthropic/jobs/4946308008) | product-facing RL / research | 5-8 years ML | RL environments, real organizational data, robust evaluation, reward hacking avoidance | 更接近真正的 frontier applied research bar。 |

## 表 2：从这些 JD 里反复出现什么

这是对上面样本做的一次**粗粒度人工归纳**，不是精确 NLP 统计。

| 反复出现的能力面 | 粗略覆盖度 | 代表词 | 这说明什么 |
|---|---:|---|---|
| `production / deployment / shipping / users` | 17/17 | production, deploy, users, customers | 好公司默认要求你把东西带到真实世界，而不是停在 notebook 或本地 demo。 |
| `eval / quality / regression / measurement` | 14/17 | eval, quality, regression, judge, dashboards | eval 已经不是加分项，而是很多 agent 岗的主战场。 |
| `runtime / orchestration / execution environment / infra` | 14/17 | orchestration, runtime, execution environment, state, platform | 真正的工程黑洞在 runtime，而不是 API 调用本身。 |
| `context / retrieval / memory / ranking` | 8/17 | context, retrieval, memory, ranking, grounding | 很多成熟产品把 agent 能力落在 context layer，而不是纯聊天。 |
| `research × product × engineering` 混合 | 绝大多数 | experiment, iteration, product, scale | 前沿公司很少把 research 和 shipping 完全分开。 |

## 表 3：这些 JD 对能力分层意味着什么

| 层次 | 今天公开市场里的典型状态 | 为什么 |
|---|---|---|
| L4 `vibe coder / one-off builder` | 供给已明显很多 | 会 Claude Code、会接简单 RAG、能做 happy path demo，已经不稀缺。 |
| 早期 L5 `builder` | 是多数强 AI-native startup 真正买单的位置 | 需要把 workflow、tools、context、eval、deployment 组织成一个可用系统。 |
| 强 L5 `reliable builder` | 顶尖 agent 公司反复在招 | 重点是 harness、quality、measurement、runtime、production feedback loop。 |
| L6 `architect / system owner` | 数量少，但在关键团队里非常重要 | 会出现在 `agent harness`、`agent infrastructure`、`context platform`、`applied AI architect` 这类角色里。 |

## 补充来源：miromind 提供的一组更企业化 JD 与薪资整理

除上面的手工抽样外，还补入一份用户提供的二次整理材料：`raw/external/miromind-agent-jd-market-scan-2026-05.md`。

这份材料的价值，不在于它比上面的抽样更“原始”，而在于它补了两类本页前面相对不足的东西：

1. **更传统企业和重行业场景的岗位**，如 `BMO`、`Stellantis`、`Capital One`、`NVIDIA`、`crewAI`、`HERE Technologies`、`Lockheed Martin`。
2. **更明确的层级切分与薪资带**，把 `0–2 年 / 3–5 年 / 6–8 年 / 10+ 年 / 15+ 年` 五档要求拉开。

需要保留一个边界：这份补充材料是**二次整理**，本轮维护没有逐条重新核验所有外链是否仍在线、措辞是否完全未改。因此更适合作为能力要求的补充快照，而不是严格逐字逐句的源头摘要。

## 表 4：miromind 补充样本中的代表角色

| 公司 | 代表岗位 | 角色层级 | 关键要求 | 这对能力判断意味着什么 |
|---|---|---|---|---|
| `BMO` | Agentic AI Developer | 高级（6–8 年） | 6–7 年 AI 软件经验，2 年 agent / multi-agent，企业级 orchestration layer，eval、governance、auditability、logging/tracing/drift detection、Azure AI | 金融企业把 agent 当成带治理与可观测性的企业平台问题，而不是 feature。 |
| `Stellantis` | Agentic AI Developer – Supply Chain | 高级（6–8 年） | 8+ 年软件/AI，3+ 年供应链/运营经验，LLM、Agent 框架、workflow orchestration、APIs、microservices、event-driven、ERP/WMS/TMS | 垂直行业公司要求技术和 domain knowledge 同时成立。 |
| `Intuitive` | Agentic AI Developer | 高级附近 | 补充样本里作为 AI Developer 类角色出现 | 说明 agent 岗正在扩到更多行业，不再只在 frontier lab 和 AI-native startup。 |
| `Synopsys` | Agentic AI Engineer | 高级附近 | 更偏 agentic engineering | 说明 `Agentic AI Engineer` 已经成为正式 title，而不是 informal label。 |
| `Booz Allen` | Agentic AI Machine Learning Engineer | 中高级 | 偏 ML + agentic system | 说明咨询/国防相关组织也在把 agent 作为一类明确工程岗位。 |
| `HERE Technologies` | Senior Backend Software Engineer – AI Agent | 中级（3–5 年） | 后端 API、workflow orchestration、云与生产经验 | 说明 AI Agent 岗并不总是“研究岗”，很多其实是 backend + orchestration 岗。 |
| `crewAI` | AI Deployment Engineer | 中级（3–5 年） | 客户环境、Docker / Kubernetes、分布式系统排障、LLM / Agent 框架 / RAG / vector DB、沟通能力 | 说明 deployment / forward deployed 是 agent 公司的主流人才画像之一。 |
| `Lockheed Martin` | AI Full Stack Engineer – Agentic Systems & Ontology | 中高级 | full stack + agentic systems + ontology | 说明部分企业会把 agent 系统和知识表示 / ontology 绑定。 |
| `Capital One` | Sr. Distinguished AI Engineer (Agentic AI Platform) | 专家（10+ 年） | north star architecture、canonical APIs、RAG pipelines、prompt libraries、多租户策略、starter kits、guardrail 服务、token cost optimization、LLMOps | 真正的专家岗是在定义公司未来几年所有 agent 应用的标准平台。 |
| `NVIDIA` | Principal Engineer – AI Agents and Systems | 顶级（15+ 年） | Windows sandbox、安全、GPU 推理优化、CUDA / TensorRT、OpenClaw、系统级 runtime | 顶级 agent 岗已经延伸到 OS / GPU / self-hosted runtime 这一层。 |

## 表 5：miromind 补充样本给出的五档能力梯度

| 层级 | 经验带 | 更接近的市场要求 | 典型关键词 | 直观含义 |
|---|---:|---|---|---|
| 入门 | 0–2 年 | 能独立做出一个靠谱 agent 应用 | Python、LLM API、至少一个 agent 框架、基础 RAG、README、部署说明 | 不是聊天页，而是能调用工具、有错误处理的小系统。 |
| 中级 | 3–5 年 | 能把一个 agent 系统真正上线并维护 | Docker、Kubernetes、API、workflow orchestration、vector DB、cloud、observability、客户沟通 | 从本地 demo 进入 production / deployment。 |
| 高级 | 6–8 年 | 能设计可复用的 agent 平台 / framework | orchestration layer、eval、governance、auditability、drift detection、domain knowledge | 从单系统 owner 进入平台 owner。 |
| 专家 | 10+ 年 | 能定义公司级 agent 平台北极星架构 | canonical APIs、SDK、CLI、starter kits、guardrails、cost optimization、LLMOps | 不是做应用，而是在规定别人以后怎么做。 |
| 顶级架构 / 系统专家 | 15+ 年 | 能把 agent 做到系统级 + 硬件级 | sandbox、runtime、CUDA、TensorRT、self-hosted agent ecosystem | 把 agent 当 OS / GPU / runtime 问题来做。 |

## 表 6：miromind 补充样本强调的高频硬技能

| 技能簇 | 高频项 | 含义 |
|---|---|---|
| 编程与后端基础 | Python、API、microservices、event-driven、异步/并发 | agent 岗首先仍然是工程岗，不是“prompt operator”。 |
| 云与部署 | Docker、Kubernetes、AWS / Azure / GCP | 真正上线和可维护是中级以上的基本门槛。 |
| Agent 专门能力 | LangChain / LangGraph / Semantic Kernel / AutoGen / CrewAI / OpenClaw，多 Agent、工具路由、state / memory | 企业已经在招聘“会做 agent orchestration”的人，而不只是“会调模型”的人。 |
| 检索与知识层 | RAG、vector DB、chunking、retrieval tuning | 在不少岗位里，agent 与知识层绑定得非常紧。 |
| 评测与可观测性 | eval、trace、drift detection、dashboard、metrics | eval / observability 已经成为生产级 agent 的默认配套。 |
| 治理与安全 | guardrails、prompt firewall、content filtering、audit API、red teaming | 这是 2026 相比早期 agent 热潮的一个明显升级。 |
| 行业知识 | 金融、供应链、制造、运营 | 高薪 agent 岗越来越要求技术和 domain 双重成立。 |

## 新增张力：AI-native startup bar 与传统企业 bar 的差异

把前面的原始抽样和这批补充样本放在一起看，可以看到两种不同但重叠的 bar。

### 1. AI-native startup / frontier 邻近 bar

更强调：

- harness
- runtime
- eval
- context layer
- agent quality
- research × engineering × product 的混合能力

### 2. 传统企业 / 重行业 bar

更强调：

- deployment
- governance
- observability
- compliance
- domain knowledge
- 平台复用能力

这意味着一个重要修正：

> 今天所谓“agent 岗”的市场，并不是单一市场。
> 
> 有一部分公司在买前沿 runtime / harness；另一部分公司在买能把 agent 安全接入企业工作流的人。

## 当前最稳的市场判断

把两轮材料放在一起，可以得出六个更稳的判断：

1. **“会 Claude Code / RAG” 本身确实已经不够。** 这类能力更像进入牌桌的基本动作，不再是高端门槛。
2. **真正高价值的差异点在 eval、reliability、runtime、context、deployment。**
3. **agent 岗位并不都要求 PhD 或最顶 research bar。** 但即使是 2-5 年经验岗位，也往往要求 production 和 system-level thinking。
4. **很多公司招的不是“最会聊 agent 的人”，而是“能把 agent 系统做稳的人”。**
5. **传统企业和重行业场景对治理、安全、审计、可观测性更敏感。** 这类岗位比纯 AI-native 团队更看重合规与 domain knowledge。
6. **高层级 agent 岗已经明显平台化。** 往上走之后，主语会从“单个 agent 应用”变成“orchestration layer / SDK / canonical API / guardrail service / runtime”。

## 适合和哪些页面一起看

- [AI 产品六层与 L3-L6 能力分层](AI 产品六层与 L3-L6 能力分层.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md)
- [求职范式转变：让工作找到你](求职范式转变：让工作找到你.md)
- [高级岗位简历的三条写法原则](高级岗位简历的三条写法原则.md)
- [Barytes GitHub项目与Agent层次评估](../bridges/Barytes-GitHub项目与Agent层次评估.md)

## 备注

- 这些链接和岗位可能会在后续下线或改写，因此这页更适合作为**能力要求快照**，不适合作为长期不变事实。
- 如果以后继续调研，最好补第二轮样本：`Claude Code / coding agent`、`enterprise deployment`、`vertical AI`、`knowledge system` 四个子市场分别抽样。 
