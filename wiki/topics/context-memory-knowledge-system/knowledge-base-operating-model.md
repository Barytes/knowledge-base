# 知识库运行模型

## 材料共同指向什么

当这个仓库把“知识编译”和“个人判断蒸馏”视为两条分开的生产线，只在回答时或在稳定桥接页里汇合时，它运行得最好。

从 `llm-wiki` 那里，可以拿到的有效外壳是：

- 原始来源保持不可变
- 被维护的 wiki 负责累积持久综合
- 用 schema 定义 ingest、query、lint 行为

从 `context infrastructure` 那里，可以拿到的关键补充是：

- 个人痕迹也是合法证据
- 稳定判断应被渐进蒸馏，而不是从单一例子里硬猜
- 不同任务应加载不同的上下文切片
- 高噪音个人记录往往需要多层信息提炼，才能沉淀成稳定规则

## 这对本仓库意味着什么

这个仓库应该维持五条边界。

### 1. 来源边界

- 外部证据放进 `raw/external/`
- 个人证据放进 `raw/personal/`

### 2. 派生页面边界

- 面向世界的综合知识与混合分析放进相关 `wiki/topics/` 目录
- 重复出现的判断放进 `wiki/self/`
- 高复用、低噪音的判断框架与 query 入口页放进 `wiki/frameworks/`

### 3. 置信度边界

个人材料应当慢慢上升：

- 先观察，再模式
- 先模式，再公理

一次有启发的对话可以支持一页 topic memo，但不足以直接生成一条高置信度 self axiom。

### 4. 工作流边界

agent 不应每次都临场发明结构，而应遵守明确的 ingest、query、lint 规则，再把耐久结果写回仓库。

### 5. 路由层边界

不是所有耐久 query 都该写进新的 topic 页面。

- 如果结果主要在回答“这类问题以后该先站在哪个框架上看”，应写进 `wiki/frameworks/`
- 如果结果主要在回答“这次结合知识和判断后，具体该怎么做”，应写进最相关的 `wiki/topics/<topic>/`

## 实际含义

- 外部文章通常应先更新最相关的 `wiki/topics/` 页面。
- 个人对话即使也触发了 wiki 结构变化，仍然可以继续作为来源证据保留。
- 混合设计讨论如果主要产出具体结论，很适合写进相关 topic。
- 如果某次讨论主要沉淀的是高复用判断框架、入口页或路由规则，更适合写进 `wiki/frameworks/`。
- 如果未来查询反复暴露某种稳定偏好，这些证据之后就能支持一页 `wiki/self/`。

## 当前用法

关于本地知识库设计的那份比较笔记，最适合被视为混合型个人证据；而它可复用的架构性结论，则应当留在这里，作为 topic 页面并进入维护索引。

## 来源依据

- [本地知识库模式](local-knowledge-base-patterns.md)
- [比较讨论](../../../raw/personal/conversations/比较两份材料的本地知识库方法与理念异同.md)

## 相关页面

- [Harness Engineering（约束壳工程）](../agent-harness-runtime/harness-engineering.md)
- [本地知识库模式](local-knowledge-base-patterns.md)
- [AI 知识系统的产品定义信念](ai-knowledge-systems-product-definition-beliefs.md)
