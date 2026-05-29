# AI 产品六层与 L3-L6 能力分层

**来源：** [Superlinear Academy 社区文章：AI 产品的六个层次](../../../raw/external/superlinear-ai-product-six-levels.md)  
**标签：** AI runtime，prompt wrapper，RAG，tool use，workflow，agentic core，AI-native product，能力分层

## 摘要

这篇材料试图澄清一个近两年很常见的误会：会用 `Cursor`、`Claude Code`、`Lovable` 之类工具快速做出 demo，不等于会做 AI system。

它给出两套互相对应的判断尺子：

- 一套看产品：AI 在用户使用时到底参与到什么深度
- 一套看人：能力到底停留在消费模型输出，还是已经上升到能把模型、工具、数据、记忆、权限与评测编排成系统

这页最值得保留的，不是“六层”这个数字本身，而是一个更实用的区分：**判断一个东西是不是 AI 产品，关键不看开发时有没有用 AI，而看用户使用时 AI 是否真的参与 runtime。**

## 最关键的区分：AI-assisted building vs AI runtime

材料把很多表面相似、其实本质不同的东西拆开了。

### AI-assisted building

AI 只在开发阶段帮你写代码、搭页面、补脚本。
用户真正使用产品时，系统内部并没有 AI 持续参与理解、判断、行动。

这类项目可以非常有用，也很适合快速验证想法，但它本质上还是传统软件，只是生产方式变了。

### AI runtime

AI 在产品运行过程中真实承担工作。
它会读取上下文、做判断、调用工具、执行动作、记忆状态，必要时再交还给人。

这个区分很重要，因为很多人会把“80% 代码由 AI 写成”误读成“这是一个 AI 产品”。这篇材料的判断更锋利：

> **决定产品层级的，不是 build-time 用没用 AI，而是 runtime 里 AI 扛没扛责任。**

这和本库已有页面 [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md) 是直接呼应的。那页强调 runtime 与 contract；这篇则先把“什么才算 runtime 里的 AI”划清边界。

## AI 产品的六层

这套分层可以理解成：AI 在系统里的职责逐步加深。

### 1. Prompt Wrapper

最薄的一层。

结构通常是：`用户输入 -> prompt -> LLM -> 输出`。

典型例子包括标题生成器、邮件润色器、文案生成器、简单聊天页。它的价值主要来自模型单轮生成能力，但缺少业务状态、工具动作和可靠性机制。

这里的 AI 更像一个 feature，而不是系统控制层。

### 2. Grounded AI / RAG

第二层开始把模型接到知识与数据上。

系统会检索文档、知识库、数据库或业务规则，再基于检索结果回答。相比 wrapper，它多出的不是“更强 prompt”，而是 grounding 能力。

关键点包括：

- retrieval 与 reranking
- metadata / permission filtering
- source tracking 与 citation
- freshness control
- 降低 hallucination

这时 AI 已经“知道得更多”，但大多数情况下仍然主要是在回答。

### 3. Tool-using AI

第三层的变化是：AI 不只回答，还能动手。

它会判断要不要调用外部工具，并把 API、文件系统、邮件、日历、CRM、Notion 等系统当作执行面。

这层的真正增量不是功能数量，而是模型从“内容生成器”变成“工具入口”。

### 4. LLM Workflow

第四层里，AI 已经被放进一个固定业务流程。

流程的大框架仍由人设计好，LLM 在某些步骤里做分类、抽取、判断、生成，再由程序或人类推进下一步。比如客服退款、合同初审、bug triage、报销审核。

这层的重点不是自主性，而是流程稳定性。它通常对应更现实的企业落地形态。

### 5. Agentic Core

第五层才是更严格意义上的 agent。

它不是沿固定 pipeline 单向推进，而是进入 `plan -> act -> observe -> update state -> continue / stop` 的循环。模型开始控制下一步做什么，而不只是填某个步骤的空。

这一层通常需要：

- planner / reasoner
- tool registry
- memory / state
- evaluator / verifier
- guardrails
- human handoff
- tracing / logs
- stop condition

这里 AI 的角色从“流程中的一环”变成“任务执行控制器”。

### 6. AI-native Product / System

第六层不是单个 agent loop，而是把 agentic core 真正放进产品与组织工作流里。

材料把它收束成三类能力：

- `frictionless interaction`
- `contextual intelligence`
- `proactive intelligence`

也就是：

- 交互要低摩擦，不要求用户每次都从零开一个聊天框
- 系统要有上下文、记忆、权限和数据流
- 系统要能被事件触发，而不只是等用户来问

到这一层，AI 不再只是一个功能，而是整个系统的智能层。

## 对应的人类能力分层：L3 到 L6

材料把人的 AI 能力也对应分成四档。

### L3：AI Consumer

核心是聊天与消费输出。

会问问题、会让模型总结翻译解释，但主要依赖模型即时表现。本质上是“把 AI 当顾问”。

### L4：AI Tinkerer / Vibe Coder

核心是 one-off 构建。

能让 AI 帮你做网页、脚本、插件、demo、小工具，但通常还停留在 happy path。系统一遇到权限、异常、维护、多人协作、复杂状态，就容易崩。

本质上是“把 AI 当外包”。

### L5：AI Builder

核心是 reliability 与 iteration。

会把任务拆成可控 workflow，知道如何设计上下文、接入数据、定义结构化输出、加人工确认、做 evaluation、记录失败案例并持续迭代。

本质上是“把 AI 当逻辑引擎”。

### L6：AI Architect

核心是 orchestration 与 integration。

关心的不是某个 prompt 或某个 model，而是整个系统如何长期运行：模型怎么路由，工具如何编排，记忆怎么分层，权限如何收口，何时自动执行，何时交还给人，如何观测与回归测试。

本质上是“把 AI 当系统控制层”。

## 这套框架真正有用的地方

### 1. 它给了一个比“有没有接 LLM API”更好的判断方式

很多项目看上去都叫“AI 产品”，但层级差异其实很大。用这套框架去看，一个项目到底只是 wrapper，还是 grounded tool，还是 workflow，还是已经有 agentic core，会清楚很多。

### 2. 它把“会用 AI”拆成了更现实的成长路径

这套路径不是从“普通工具”升级到“更强工具”，而是：

- 从消费输出
- 到做 one-off 原型
- 到让流程可靠
- 到设计长期运行的系统

这个拆法的价值在于，它把很多模糊的能力焦虑，重新落回可练的工程与产品问题。

### 3. 它解释了真正稀缺的壁垒在哪里

材料的结论很明确：普通 wrapper 会越来越容易，简单 vibe coding 会越来越普及，真正稀缺的是能把 AI 放进真实工作流，并让它稳定、可控、可评估、可迭代、可主动运行的人。

这和 [Harness Engineering（约束壳工程）](../agent-harness-runtime/harness-engineering.md) 那页强调的方向一致。真正难的不是“能不能调到模型”，而是外层控制、验证、权限和协同怎么设计。

## 需要保留的边界

这套六层框架很有用，但也不能机械地读成“层数越深越先进”。

### 不是所有问题都值得上 agent

材料自己也引用了 `Anthropic`、`OpenAI`、`Google Cloud` 的类似判断：如果单轮调用、RAG 或固定 workflow 已经足够，就不该为了“更像 AI”而强行加 agentic 复杂度。

### 很多真实系统会跨层混合

一个产品可能同时包含 RAG、tool use、workflow 和部分 agent loop。六层更像主导结构，而不是严格互斥的 taxonomy。

### 深 runtime 仍然不等于可靠系统

即便已经有工具调用与 loop，如果没有 evals、permission model、observability、human handoff，它仍然可能只是一个更复杂的 demo。

这也是为什么这页最好和 [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md) 一起看。前者告诉你“层级加深意味着什么”，后者告诉你“为什么仅有 runtime 还不够”。

## 与现有知识的关联

这篇材料可以看作几页已有内容之间的一个中间桥：

- 对 [AI Architect Lens](ai-architect-lens.md) 来说，它把“architect 和 builder 的差别”讲得更工程化，不再只停留在问题定义层。
- 对 [AI Architect 的 Context Intelligence 镜头](ai-architect-context-intelligence.md) 来说，它补上了为什么 context、memory、permission 会在更高层级变成系统问题。
- 对 [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md) 来说，它提供了一套更适合给项目或候选人做分层诊断的前置框架。

## 来源依据

- [Superlinear Academy 社区文章：AI 产品的六个层次](../../../raw/external/superlinear-ai-product-six-levels.md)

## 相关页面

- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)
- [AI Architect Lens](ai-architect-lens.md)
- [AI Architect 的 Context Intelligence 镜头](ai-architect-context-intelligence.md)
- [Harness Engineering（约束壳工程）](../agent-harness-runtime/harness-engineering.md)
- [Claude Code、Codex 与 pi 的 harness 对比](../agent-harness-runtime/coding-agent-harness-comparison.md)
