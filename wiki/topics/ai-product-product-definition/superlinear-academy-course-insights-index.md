# Superlinear Academy 课程与洞见总索引

**来源：** [Superlinear Academy 课程与洞见原文归档](../../../raw/external/superlinear-academy-course-insights-2026-06-22/README.md)
**标签：** Superlinear Academy，AI Builder，AI Architect，Agentic AI，Deep News，Knowledge Bank，AI 产品，agent runtime

## 摄取范围

这次摄取覆盖 Superlinear Academy 左侧导航中“课程与洞见”分组下的 7 个空间，共 535 条 lesson / post 原文：

| 空间 | 类型 | 数量 | 主要用途 |
| --- | --- | ---: | --- |
| AI 编程入门 | lesson | 20 | 从 AI user 过渡到能指挥 AI 写代码、处理环境和错误的 builder 入门层。 |
| AI Builders | lesson | 68 | 从生成式 AI 原理、自动化项目、任务委托、评估与开源模型，训练 AI builder 的工程基本功。 |
| AI Architects | lesson | 46 | 从产品定义、context intelligence、proactive intelligence 到 production-grade architecture，训练长期系统设计能力。 |
| 公开课与行业交流 | lesson | 20 | 面向企业、学校和行业交流的公开演讲与案例入口。 |
| Knowledge Bank | post | 163 | 更长的课程化文章、访谈、方法论和 AI 时代工作方式分析。 |
| Deep News | post | 200 | 高频 AI 产业、模型、agent runtime、AI coding、安全与基础设施新闻解释。 |
| Agentic AI 的原理与实践 | lesson | 18 | 从 prompt / command / objective-oriented programming 到 Cursor、工具扩展和 agent 产品形态。 |

原文以 JSONL 形式归档在 `raw/external/superlinear-academy-course-insights-2026-06-22/pages.jsonl`。每条记录保留 `category`、`kind`、`href`、`title`、`headings`、`links`、`text` 和 `textLength`，便于后续用 `rg` 或脚本按主题继续深挖。

## 与 lizheng-open-context 的分工

2026-08-30 的 [lizheng-open-context：来源模型与主题路由](../context-memory-knowledge-system/lizheng-open-context来源模型与主题路由.md) 已作为另一份版本化 raw 快照进入本库。它不是对本归档的替换：

| 查询目标 | 默认来源 |
| --- | --- |
| 立正本人在何时、何处表达过什么；当前 thesis；需要按明确许可公开复用 | `lizheng-open-context` |
| AI Builders / AI Architect / Agentic AI 的 lesson 结构 | 本页对应的 2026-06-22 课程归档 |
| Deep News 的连续产业信号 | 本页对应的 2026-06-22 课程归档 |
| Knowledge Bank 其他作者的正文与当时页面上下文 | 本归档；继续保留原作者归属，不转成立正观点 |
| 嘉宾视频与其他作者的发现信息 | 优先使用新快照元数据，再按权利范围回到原链接或本归档 |

两批材料按规范化 URL 精确比较，有 30 条立正社区帖子 URL、162 条 Knowledge Bank URL 重叠；新快照另有 193 条第一方帖子 URL 不在旧归档中。重叠材料默认用新快照确认作者、日期、时间语义和权利字段，用旧归档补课程位置与 2026-06-22 当时的页面上下文。不要把新快照里 `metadata-only` 的其他作者条目因为本归档有正文，就升级成立正第一方内容。

例如，`AI的大鞭子终于抽回我身上` 在新快照中明确属于 Barytes，且只有元数据；本库的 [AI 鞭子：Accountability、AI 理解与 AI-native 团队](../human-ai-relationship/AI鞭子-accountability与AI-native团队.md) 来自旧归档中的 Barytes 正文。它可以与立正的 [fake work：从内部记分牌到真实结果](../career-positioning-job-search/fake-work-从内部记分牌到真实结果.md) 并置分析，但不能互换作者。

## 这批材料在知识库里的位置

这批材料不应该被理解成单一课程摘要。它更像一组连续更新的 AI builder / architect 训练语料，覆盖三层：

1. **能力训练层**：如何从会聊天、会 vibe coding，进入能定义任务、管理 context、处理失败、设定验收标准的 builder 状态。
2. **产品系统层**：什么才算 AI runtime，什么时候需要 RAG、workflow、agentic core，什么时候应该停在更简单的层级。
3. **产业信号层**：Deep News 持续追踪 Claude Code、Cursor、Vercel、MCP、agent safety、模型推理、本地模型、AI coding 和组织转型，把新事件翻译成工程判断。

所以它应当接在本库已有的 [AI 产品六层与 L3-L6 能力分层](AI%20产品六层与%20L3-L6%20能力分层.md)、[AI Architect Lens](ai-architect-lens.md)、[AI Architect 的 Context Intelligence 镜头](ai-architect-context-intelligence.md)、[AI Architect 的 Proactive Intelligence 镜头](ai-architect-proactive-intelligence.md)、[AI Architect 的 Advanced Architecture 镜头](ai-architect-advanced-architecture.md) 之后阅读。

如果问题偏运行时、harness 或 coding agent，应转到 [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)、[Claude Code Dynamic Workflows](../agent-harness-runtime/claude-code-dynamic-workflows.md)、[Harness Engineering（约束壳工程）](../agent-harness-runtime/harness-engineering.md) 与 [Thin Harness, Fat Skills](../agent-harness-runtime/thin-harness-fat-skills.md)。

如果问题偏 context / memory / 知识系统，应转到 [Context Engine：上下文编排层](../context-memory-knowledge-system/context-engine.md)、[Agent Context Infra 前沿调研（2026-05-25）](../context-memory-knowledge-system/agent-context-infra-2026-05-25.md) 与 [AI 知识系统的产品定义信念](../context-memory-knowledge-system/ai-knowledge-systems-product-definition-beliefs.md)。

## 课程主线

### 1. 从 User 到 Builder

AI 编程入门和 AI Builders 的共同主线，是把“会用 AI”从聊天能力改写成工程协作能力。

它反复强调的不是语法训练，而是三类更底层的能力：

- **环境亲和力**：能理解文件、命令行、API、开发环境和执行结果，不被底层工作面吓退。
- **报错耐受力**：把红字、异常、失败输出看成可交给 AI 诊断的线索，而不是个人能力失败。
- **逻辑描述力**：把模糊需求拆成 context、components、criteria，把任务交代成可执行 brief。

这条线和本库 [GenAI 的共识边界与任务委托框架](GenAI%20的共识边界与任务委托框架.md) 互补：前者讲能力养成，后者讲哪些任务适合交给 GenAI。

### 2. 从 Builder 到 Architect

AI Architect 课程的核心不是更复杂的代码，而是更早、更硬的问题定义：

- 先写 `Product Definition Brief`，再进入实现。
- 先定义用户、场景、MVP、OKR 和验收标准，再选择技术方案。
- 把 AI 当作需要管理的执行者，而不是一次性 prompt 生成器。
- 把 context、memory、proactive trigger、evaluation、fallback、权限与生产稳定性当作系统设计问题。

这条线解释了为什么本库此前已经单独维护了几页 AI Architect 镜头页：它们不是课程章节摘要，而是可以复用的产品定义镜头。

### 3. Agentic AI 的操作范式

Agentic AI 课程把编程心智从命令式推进到三种模式：

- `Command Oriented Programming`：人明确给出步骤。
- `Prompt Oriented Programming`：人描述目标和上下文，模型补全局部路径。
- `Objective Oriented Programming`：人定义目标、约束和验收，agent 进入行动循环。

这里最值得保留的边界是：agentic 并不等于无约束自主。真正可用的 agent 需要工具入口、规则文件、可观察执行、搜索 / 爬虫能力、权限边界和人类接管点。

## 洞见主题簇

### 1. AI 产品分层与 runtime 判断

Knowledge Bank 中多篇文章共同强化一个判断：一个产品是不是 AI 产品，不看开发时是否用了 AI，而看用户使用时 AI 是否进入 runtime。

这组材料支撑了本库已有的六层框架：

- prompt wrapper
- grounded AI / RAG
- tool-using AI
- LLM workflow
- agentic core
- AI-native product / system

后续查询若问“这个东西算不算 AI 产品”“该做 RAG 还是 agent”“为什么 vibe coding 不等于 AI-native product”，应优先读 [AI 产品六层与 L3-L6 能力分层](AI%20产品六层与%20L3-L6%20能力分层.md)，再回到本页 raw 归档检索具体文章。

### 2. 结果确定性、eval 与 contract

这批材料反复出现 `evaluation`、`contract`、`acceptance criteria`、`runtime` 和 `harness`。它们共同指向一个工程判断：

AI 系统的可靠性不主要来自“模型一次说对”，而来自能否定义终点、观察执行、保存状态、重试、验证和回退。

相关材料可以分成两类：

- 课程层：AI Builders / AI Architect 中关于 task delegation、assessment mechanism、risk management、production-grade architecture 的 lesson。
- 新闻层：Deep News 中围绕 Claude Code dynamic workflow、TDD、agent runtime、CLI、MCP、background activity、security assumption 的连续解释。

这和 [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md) 是同一条线。

### 3. Context、memory 与 Digital Twin

AI Architect 课程里的 context intelligence 线，把 AI 记忆系统定义成 Digital Twin 产品问题，而不是单纯 RAG 参数问题。

这批 raw 里可以继续追踪几组关键词：

- `context window`
- `memory`
- `digital twin`
- `document as first-class deliverable`
- `personal data`
- `permission`
- `proactive intelligence`

这组材料适合支撑本库后续关于 context infra、knowledge base、agent memory、personal AI 和持续工作面的研究。

### 4. AI 教育与工作方式变化

这批材料里有一条很清楚的教育观：AI 教育不应只交付教程内容，而应帮助学习者建立工程工作面和失败处理能力。

它反对两种误区：

- **找课本**：只看概念和名词，不进入真实任务。
- **抄作业**：依赖 tutorial 复刻，遇到新场景就失效。

更稳定的训练对象是：定义任务、拆解约束、搭环境、读错误、调用工具、保存 context、设定 eval、复盘失败。

这也解释了为什么课程材料常把“学习 AI”说成从 `AI User` 进入 `AI Builder`，而不是掌握更多工具名。

### 5. 产业信号：Deep News 作为连续雷达

Deep News 的价值不在于单条新闻本身，而在于它用相同镜头反复解释事件：

- 模型和推理基础设施如何变化
- AI coding 的工作流如何从盯着改，变成整体委托
- agent safety 为什么从 prompt injection 扩展到权限、runtime、供应链和组织流程
- CLI、MCP、ACP、PTY、Cloudflare、Vercel、OpenAI、Anthropic、Google 等信号怎样指向 agent runtime 的基础设施化
- AI 组织转型为什么不是“更多人会用工具”，而是责任、接口、KPI 和工作流重写

后续如果要做趋势追踪，不宜把 Deep News 每篇都拆成 wiki 页。更好的做法是按主题检索 raw，再把连续多篇压缩进已有 topic 页。

## 推荐检索方式

原文已经保存在 `pages.jsonl`。常用检索可以从这些关键词开始：

```bash
rg -n "Claude Code|dynamic workflow|TDD|harness" raw/external/superlinear-academy-course-insights-2026-06-22/pages.jsonl
rg -n "context|memory|Digital Twin|RAG" raw/external/superlinear-academy-course-insights-2026-06-22/pages.jsonl
rg -n "AI Builder|AI Architect|Product Definition Brief|OKR" raw/external/superlinear-academy-course-insights-2026-06-22/pages.jsonl
rg -n "安全|权限|prompt injection|agentjacking" raw/external/superlinear-academy-course-insights-2026-06-22/pages.jsonl
```

如果要按空间浏览，先读 [raw 归档 README](../../../raw/external/superlinear-academy-course-insights-2026-06-22/README.md)。它保留了 535 条内容的标题、类型和长度。

## 后续写回原则

这批材料已经完整归档，但不应一次性展开成 535 个维护页。后续写回建议遵循：

- **已有主题优先**：能补到 AI 产品分层、agent runtime、context infra、AI 教育、职业与组织转型的，就更新已有页。
- **多篇合并**：至少跨 2-3 篇材料形成稳定主题，再新增维护页。
- **新闻不逐条入 wiki**：Deep News 适合作为趋势证据池，除非某条已经改变本库的框架判断。
- **课程页不逐课摘要**：lesson 的价值在于课程地图和方法论结构，单课只在被具体 query 触发时再抽取。
- **第一方查询先分版本**：涉及立正原话时，保留原书 / 历史帖子与 2026 开放 V1 的真实措辞差异，不用本库综合无声降格或覆盖原表述。

## 相关页面

- [AI 产品六层与 L3-L6 能力分层](AI%20产品六层与%20L3-L6%20能力分层.md)
- [AI Architect Lens](ai-architect-lens.md)
- [AI Architect 的 Context Intelligence 镜头](ai-architect-context-intelligence.md)
- [AI Architect 的 Proactive Intelligence 镜头](ai-architect-proactive-intelligence.md)
- [AI Architect 的 Advanced Architecture 镜头](ai-architect-advanced-architecture.md)
- [GenAI 的共识边界与任务委托框架](GenAI%20的共识边界与任务委托框架.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)
- [Claude Code Dynamic Workflows](../agent-harness-runtime/claude-code-dynamic-workflows.md)
- [Context Engine：上下文编排层](../context-memory-knowledge-system/context-engine.md)
- [lizheng-open-context：来源模型与主题路由](../context-memory-knowledge-system/lizheng-open-context来源模型与主题路由.md)
