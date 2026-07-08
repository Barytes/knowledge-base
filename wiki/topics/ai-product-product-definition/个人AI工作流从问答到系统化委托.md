# 个人 AI 工作流：从问答到系统化委托

**来源：** 基于 [Superlinear Academy 课程与洞见总索引](superlinear-academy-course-insights-index.md)、[AI User 到 AI Builder 的五个能力差距](AI-User到AI-Builder的五个能力差距.md)、[AI 产品六层与 L3-L6 能力分层](AI%20产品六层与%20L3-L6%20能力分层.md)、[AI Architect Lens](ai-architect-lens.md)、[AI Architect 的 Context Intelligence 镜头](ai-architect-context-intelligence.md)、[AI Architect 的 Proactive Intelligence 镜头](ai-architect-proactive-intelligence.md)、[AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md) 与 [GenAI 的共识边界与任务委托框架](GenAI%20的共识边界与任务委托框架.md) 的应用综合。

## 核心判断

如果现在大部分 AI 使用还停在问答工具，真正要升级的不是“问得更会”，而是把 AI 放进稳定工作流里。

Superlinear 这组材料的共同指向是：`AI User` 到 `AI Builder` 的差距，不主要来自 prompt 技巧，而来自一个人能否持续提供高质量 context、定义验收标准、让 AI 执行后能观察结果、并把有效做法沉淀成下次可复用的资产。

因此，个人工作流的优化目标可以压缩成一句话：

> 把 AI 从临时顾问变成可被委托、可被验收、可复盘、可积累的工作主体。

## 1. 先选可迁移的任务，不要一开始追求全自动

最适合第一批迁移的任务有三个特征：

- 高频出现，每周至少会遇到几次。
- 结果有可判断的好坏，而不是完全依赖灵感。
- 输入材料可以被文件化，例如笔记、草稿、代码、网页、会议记录、聊天记录、需求说明。

适合先迁移的例子：

- 把一批文章压缩成主题索引。
- 把一个模糊想法整理成 `Product Definition Brief`。
- 把调研材料转成对比表、证据表和下一步行动。
- 把项目卡点整理成 debug plan、验收清单和失败分类。
- 把一次好的问答沉淀为 wiki 页面、skill、模板或复盘记录。

不适合作为第一批迁移的任务：

- 价值标准非常模糊的审美判断。
- 高风险外部承诺，例如财务、法律、公开发布前的关键结论。
- 你自己也无法说清“什么叫好”的任务。

这些任务不是不能用 AI，而是不应直接交给 AI 闭环执行。先把判断标准写清楚，再迁移子任务。

## 2. 把聊天框改成文件工作面

问答模式的最大问题，是上下文和结果都太容易消失。更稳定的做法是把 AI 的默认输入输出放到文件里。

最小文件工作面可以只有四类文件：

- `context.md`：这件事的背景、目标、约束、已有材料、不可碰边界。
- `brief.md`：本轮要 AI 完成的任务，写清输出形态和成功标准。
- `result.md`：AI 产出的版本、结论、代码、表格或方案。
- `review.md`：人工验收、失败原因、下一轮要改什么。

这不是形式主义。文件的价值在于：

- AI 可以反复读取同一个稳定上下文。
- 结果可以被后续 agent、脚本或人检查。
- 好的 brief 和 review 可以变成模板或 skill。
- 失败不会只留在聊天记录里，而会变成下次可复用的边界。

这和本知识库的 `raw/ -> wiki/ -> frameworks/self` 分层是一致的：一次任务的原材料、维护结果和可复用规则应该分层沉淀。

## 3. 每次委托都写清四件事

把 AI 当问答工具时，常见句式是“帮我看看这个”。把 AI 当工作流主体时，应该把 prompt 改成 assignment brief。

一个够用的 brief 至少包含：

1. **目标**：这次要产出什么，不只是“分析一下”。
2. **上下文**：AI 必须参考哪些文件、材料、已有判断。
3. **约束**：哪些内容不能改，哪些结论不能越界，哪些风险要标出。
4. **验收标准**：什么样算完成，怎样检查，什么时候需要停下来问人。

这一步对应 Superlinear 里的 `Evaluation First` 与 `Clear Delegation`。真正的升级不在于 prompt 更花，而在于 AI 知道终点在哪里。

## 4. 给 AI 一个可观察的执行循环

从问答升级到工作流，关键不是让 AI “更自主”，而是让它能看到动作后果。

个人工作流里可以先做很轻的 agentic loop：

1. AI 读取 `context.md` 和相关材料。
2. AI 生成 `result.md` 或修改目标文件。
3. AI 运行可用检查，例如 `rg`、测试、链接检查、格式检查、事实表对照。
4. AI 根据检查结果修正。
5. 人只看最终 diff、失败解释和未决问题。

如果没有自动化检查，也可以用人工清单替代：

- 是否引用了指定材料。
- 是否遗漏关键约束。
- 是否把推断说成事实。
- 是否给出可执行下一步。
- 是否把值得复用的部分写回模板或 wiki。

这就是把安全感从“我控制了每一步”转向“我定义了终点和验收方式”。

## 5. 把高频任务沉淀成模板、skill 或仓库规则

如果一个任务重复出现三次，就不应该每次重新解释。

可以沉淀成三种层级：

- **模板**：固定输入输出，例如调研 brief、产品定义 brief、复盘表、访谈提纲。
- **skill**：固定工作方法，例如如何读本地知识库、如何做源码审查、如何把文章写回 wiki。
- **规则文件**：稳定偏好和边界，例如 `AGENTS.md`、`COMMUNICATION.md`、项目 README、验收清单。

这一步最容易被低估。AI 工作流真正产生复利，不是因为单次回答更好，而是因为每次成功和失败都会降低下次委托成本。

## 6. 保留人的判断权

Superlinear 的另一条边界同样重要：不是所有东西都该交给 AI。

适合交给 AI 的通常是：

- 总结、改写、翻译、结构化。
- 从给定材料中抽取、比较、归类。
- 生成初稿、检查清单、执行重复步骤。
- 在明确验收标准下尝试、修正、再检查。

应该留在人手里的通常是：

- 要不要做这件事。
- 什么算高质量。
- 哪些风险不能接受。
- 哪个方向值得下注。
- 哪些非共识判断是你的核心价值。

所以个人 AI 工作流不是“把自己外包掉”，而是把机械、共识、可验证的部分交给 AI，让自己更多负责方向、品味、边界和取舍。

## 一个可执行的七天迁移法

第一天：列出最近一周最常让你打开 AI 的 10 个场景，标出其中最高频、最可验收的 1 个。

第二天：为这个场景写一个 `context.md`，只放高信噪比背景和约束。

第三天：写一个 `brief.md` 模板，固定目标、输入、输出格式、验收标准。

第四天：跑一次真实任务，把 AI 输出保存为 `result.md`。

第五天：写 `review.md`，记录哪里好、哪里错、错因属于 context 缺失、指令歧义、验收不清还是模型能力边界。

第六天：把成功的 brief 改成模板，把失败模式写进验收清单。

第七天：决定是否迁移第二个任务。只有第一个任务能稳定复用后，再扩大范围。

## 对你的直接建议

你的知识库已经具备比普通用户更好的起点：本地 `wiki/`、`raw/`、`frameworks/`、`AGENTS.md` 和 repo-local skills 已经构成文件工作面。

所以第一步不需要另起一个复杂个人 AI 系统。更好的起点是选择一个高频工作流，把它从“临时问 AI”改成“有 brief、有 source、有验收、有 write-back”的闭环。

最适合你的三个起手任务是：

1. **调研综合**：给定文章或 corpus，产出主题页、证据表、相关页面和 log。
2. **产品判断**：给定想法，先产出 `Product Definition Brief`，再进入验证或实现。
3. **项目复盘**：给定一次代码 / 写作 / 研究任务，把有效步骤、失败模式和下次规则写回 `wiki/` 或 repo skill。

这三类任务都能积累到你的主线：context、harness、eval、workflow 和可验证执行系统。

## Build copilot 时最该沉淀什么

如果正在 build 一个 copilot，最有复利的沉淀不是“这次项目写了多少代码”，而是下一次 build 能直接复用的工作面。

优先沉淀五类资产：

1. `product-context.md`：用户、场景、核心问题、反例、非目标、必须保留的人类判断权。它让下次不是从“我要做一个 copilot”开始，而是从已经校准过的产品边界开始。
2. `workflow-playbook.md`：从想法到 demo 的实际步骤，包括如何收集材料、如何写 brief、如何让 agent 实现、如何 review、如何决定下一轮。它把一次 build 变成下次 build 的操作手册。
3. `eval-cases/`：真实任务样本、好坏输出对比、失败案例、验收清单。它让 copilot 不只停在“能聊天”，而能被重复验证。
4. `component-contracts/`：capture、context routing、memory/writeback、agent executor、review UI 等模块的输入输出契约。它让下个项目可以换界面、换模型、换框架，但保留底层结构。
5. `failure-log.md`：哪些 prompt 失效、哪些 context 污染结果、哪些自动化让人更累、哪些地方必须人审。失败日志比成功截图更容易复利，因为它会减少下一次同类错误。

对 `Context Copilot` 这类项目，最值得保留的核心不是一个具体 dashboard，而是 `capture -> context state -> routing -> agent use -> review/writeback` 这条链路。每次 build 都应该问：这次有没有让这条链路更清楚、更可测、更容易被下一个项目调用。

## 相关页面

- [Superlinear Academy 课程与洞见总索引](superlinear-academy-course-insights-index.md)
- [AI User 到 AI Builder 的五个能力差距](AI-User到AI-Builder的五个能力差距.md)
- [AI 产品六层与 L3-L6 能力分层](AI%20产品六层与%20L3-L6%20能力分层.md)
- [AI Architect Lens](ai-architect-lens.md)
- [AI Architect 的 Context Intelligence 镜头](ai-architect-context-intelligence.md)
- [AI Architect 的 Proactive Intelligence 镜头](ai-architect-proactive-intelligence.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)
- [GenAI 的共识边界与任务委托框架](GenAI%20的共识边界与任务委托框架.md)
- [知识库运行模型](../context-memory-knowledge-system/knowledge-base-operating-model.md)
