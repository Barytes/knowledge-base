# AI Architect Lens

## 摘要

这份课程讲义提出的核心方法，不是先进入代码实现，而是先用产品定义镜头重新拆解一个未来场景，找出真正值得优化的痛点、最关键的上下文，以及能决定架构走向的第一性选择。

它强调：很多看似相同的 AI 产品，真正的差异不在于“能不能做”，而在于“到底在解决哪个更高价值的问题”。

## 核心方法

### 从可能性切换到价值判断

课程把 AI Architect 和普通 builder 的区别定义得很清楚：

- builder 容易直接进入功能描述
- architect 会反问真正要解决的核心问题是什么
- 一旦核心问题变了，产品目标、交互方式、输出格式和技术架构都会跟着变

这意味着最重要的架构决策，往往发生在写第一行代码之前。

### 用产品定义先锁定方向

讲义把第一阶段产物定义为 `Product Definition Brief`，而不是代码或 prompt。

这个 brief 至少需要回答：

- 核心问题是什么
- 用户是谁，关键场景是什么
- 什么是最小但仍然像 magic 的 MVP
- 成功怎么定义，也就是 OKRs 和 acceptance criteria

在这个框架下，prompt 不是魔法咒语，而是 assignment brief；AI 不只是工具，而是一个需要被管理、被委派、被评估的直接下属。

## 三个案例里的共同洞察

### 1. 先找高价值痛点

案例一不是把痛点定义成“忘了电影名”，而是“打断社交魔法的代价太高”。

所以正确优化方向不是更强搜索，而是更低可见度、更低认知负担。

### 2. 不同问题会导向不同产品

案例二强调，同样是耳机里的实时辅助，产品可以是：

- 信息外包系统
- 行为表现教练

二者依赖的能力、数据、评估标准都不同，所以不能把它们混成一个模糊愿景。

### 3. 目标会决定整个系统架构

案例三进一步说明，即使都是“自我反思”，如果目标是：

- 长期模式发现

系统就应优先优化归档、检索、分析与可视化。

如果目标是：

- 当下行为改变

系统就应优先优化低延迟处理与即时反馈闭环。

## Manage-And-Create Workflow

课程提出一套管理 AI 的三步循环：

1. `Evaluation First`
   先定义成功标准，写清楚目标、关键结果和验收条件。
2. `Clear Delegation`
   把 prompt 当 assignment brief，明确目标、背景、约束和输出要求。
3. `Iterative Feedback`
   用预先定义的 OKRs 复盘输出，再把反馈写回下一轮 brief。

这套方法的重点不是“怎么把 prompt 写得更花”，而是把人类的角色从执行者提升为经理与架构师。

## 对 AI 产品设计的启发

这份讲义隐含了几条很强的产品观：

- AI 时代的瓶颈正在从“不会做”转向“不会定义做什么”
- 技术能力变得廉价后，真正稀缺的是问题选择、约束设定和验收标准
- 架构不是先选技术栈，而是先选你到底想优化哪一种价值
- 系统的 shape 主要由目标、场景和反馈闭环决定

## 来源依据

- [AI Architect Product Definition Brief](../../raw/external/ai-architect-product-definition-brief.md)

## 相关页面

- [产品定义判断框架](../frameworks/产品定义判断框架.md)
- [GenAI 的共识边界与任务委托框架](GenAI 的共识边界与任务委托框架.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md)
- [AI Architect 的 Context Intelligence 镜头](ai-architect-context-intelligence.md)
- [AI Architect 的 Proactive Intelligence 镜头](ai-architect-proactive-intelligence.md)
- [AI Architect 的 Advanced Architecture 镜头](ai-architect-advanced-architecture.md)
- [本地知识库模式](local-knowledge-base-patterns.md)
- [grapeot/context-infrastructure 仓库地图](grapeot-context-infrastructure-repo-map.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
