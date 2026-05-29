# AI 自演化研究 Harness

## 摘要

从本地关于 ASI-Evolve 的来源来看，AI 自演化并不是让一个更聪明的模型端到端决定一切，而是依赖一套 harness，把研究活动收束成一个有边界的闭环：学习、设计、实验、分析。

关键的方法论动作是：真正带来进步的，是围绕模型生成过程工程化整个循环。

- 在提出候选方案前注入相关先验知识
- 在昂贵实验之前先做硬约束校验
- 用分阶段实验而不是一次性判断来评估候选方案
- 同时分析成功与失败，并把经验写回可复用存储

这是一种面向研究的 harness engineering，而不是单纯服务于软件任务执行。

## Harness 在控制什么

### 1. 搜索由检索到的先验知识锚定

ASI-Evolve 会先从人类研究构建结构化认知库，再在每轮中检索相关条目。

- 来源把这描述为避免盲搜的方法。
- 用 harness 的语言看，这不只是“补上下文”，而是在缩小提案空间，让每一轮都从领域相关的约束与模式出发。

### 2. 候选生成在运行前就被门控

设计阶段不会让任意自由输出直接流入完整实验。

来源描述的关键门包括：

- 负责硬约束检查的 static-check agents
- 修复实现错误的 debugging agents
- 过滤重复提案的 novelty checks
- 基于已有强候选做增量修改，而不是每轮全量重写

这里的方法论模式是：先约束，再消耗算力。

### 3. 评估是分阶段且考虑成本的

实验阶段会先用更便宜的早筛，再做完整验证。

- 弱候选会在小规模或部分运行中被提前筛掉
- 只有在定量与定性维度都超过 baseline 的候选，才会继续进入下一阶段

这就是典型的 harness 逻辑：先把通过与失败的边界写清楚，只有当中间证据足够强时，才投入稀缺资源。

### 4. 分析是一级控制组件

本地材料里最强的一点，是专门的 analyzer。

系统不会只保留得分最高的候选，而会：

- 对照 baseline 与历史最优结果
- 识别失败模式
- 提炼可执行的设计经验
- 把结构化洞见重新写回数据库

这使实验从“筛选”变成“学习”。Analyzer 实际上相当于研究版的外部验证器加事故复盘回路。

## 方法论

根据本地来源，AI 自演化背后的 harness engineering 方法大致是这样：

1. 把工作建模成可重复闭环，而不是开放式 agent 会话。
2. 把知识检索、方案生成、实验执行、结果分析拆成明确阶段。
3. 在昂贵实验之前放置廉价筛选与硬约束。
4. 依赖客观环境反馈，而不是信任模型自评。
5. 把失败运行保存成结构化经验，而不只是负分。
6. 除非有证据表明需要大跳跃，否则优先围绕强候选做局部变异。
7. 维护一个不仅保存产物与分数，也保存解释、标签与置信度的记忆底座。

## 为什么重要

这份来源暗示，“AI 自演化”主要不是自主灵感的故事，而是构建研究 harness 的故事。它会：

- 把人类隐性的科研流程拆成机器可执行的阶段
- 把算力转化成大量有边界的试验
- 让失败变得可读且可复用
- 让学习跨轮累积，而不是每次从零开始

在这个视角下，harness 才是真正的研究引擎，模型只是其中一个组件。

## 与 Automated Weak-to-Strong Researcher 的互补

新摄取的 `Automated Weak-to-Strong Researcher` 让这页原先只停留在 ASI-Evolve 的判断，多了一个很不一样的对照点。

两者共同说明的一点是：研究自动化真正有价值的，不是让模型“自己想”，而是给它一个能持续试、持续判分、持续写回经验的闭环。

但两者强调的杠杆并不相同：

- ASI-Evolve 更强调在生成前注入先验知识、分阶段门控实验、保留 analyzer 作为学习器。
- AAR 更强调 outcome-gradable 环境、并行 sandbox、最小 prescriptive scaffold，以及 findings 的共享工作面。

这让“研究 harness”多出一个很关键的补充判断：

- 一旦任务能被可靠判分，瓶颈会迅速转向评测设计与 reward hacking 防护。
- 在研究任务里，厚脚手架未必比薄脚手架更好，关键是外部反馈面是否足够强。
- 多 worker 的价值主要来自维持探索分布，而不是机械复制更多 agent。

## 来源里的限制

- 系统依然依赖人类来定义任务、约束与指标。
- 算力成本仍然是核心瓶颈。
- 即便加入 AAR 之后，这页仍然只覆盖了少数“可判分研究环境”里的自动化研究案例。对于更开放、不可直接判分的问题，还缺少足够本地材料。

## 来源依据

- [ASI-Evolve 来源](../../../raw/external/将无人类容身之地。。AI加速%20AI系统的闭环时代已至：ASI-Evolve实现从模型架构、预训练数据治理、算法设计到跨领域泛化！.md)
- [Automated Weak-to-Strong Researcher PDF](../../../raw/external/Automated Weak-to-Strong Researcher.pdf)
- [Harness Engineering（约束壳工程）](harness-engineering.md)

## 相关页面

- [本地知识库模式](../context-memory-knowledge-system/local-knowledge-base-patterns.md)
- [知识库运行模型](../context-memory-knowledge-system/knowledge-base-operating-model.md)
- [Automated Weak-to-Strong Researcher](automated-weak-to-strong-researcher.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
- [Pi coding agent：一种极简且可观察的 coding harness](pi-coding-agent-harness.md)
