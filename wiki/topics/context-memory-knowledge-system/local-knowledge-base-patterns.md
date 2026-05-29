# 本地知识库模式

## 摘要

这两份来源材料描述的是两套互补但不相同的系统。

- `llm-wiki` 关注把外部材料编译成一个被维护的 wiki。
- `context infrastructure` 关注把个人行为和判断编译成未来 agent 工作可复用的上下文。

把两者放在一起看，它们指向的不是一个未分层的大记忆池，而是一个分层知识库。

## 模式一：持久化的知识编译

`llm-wiki` 模式把知识库看作用户与原始文档之间的持久中间产物。

它的主要动作是：

- 保持原始来源不可变
- 由 LLM 维护 wiki 层
- 用 schema 定义 ingest、query、lint 行为
- 把高质量查询结果写回 wiki，让理解随时间累积

它强调的是持久的世界知识、综合能力与可导航性。

## 模式二：个人上下文蒸馏

`context infrastructure` 模式把原始个人痕迹当作提炼稳定判断的证据基础。

它的主要动作是：

- 在本地收集丰富的个人痕迹
- 把弱观察与稳定模式分开
- 把重复倾向提炼成更高层的决策原则
- 针对具体任务只加载其中相关的切片

它强调的不是中性的主题覆盖，而是非共识判断、品味与任务特定视角。

## 共同动作

虽然目标不同，两种模式共享几项运行思路。

- 都拒绝把一次性检索当作主流程。
- 都依赖本地文件作为可持久、可检查的状态。
- 都把 LLM 当成维护者，而不只是答题器。
- 都依赖明确的操作规则，确保仓库长期可读。

## 主要差异

### 编译对象是什么

- `llm-wiki` 把外部材料编译成主题知识。
- `context infrastructure` 把个人证据编译成判断模式。

### 什么才算持久页面

- 在 `llm-wiki` 里，持久产物是摘要、概念、实体和比较。
- 在 `context infrastructure` 里，持久产物是观察、模式、公理以及任务相关 skill。

### 它们各自解决什么失败模式

- `llm-wiki` 主要解决的是积累与维护问题。
- `context infrastructure` 主要解决的是输出过于平淡、过于共识化的问题，它通过注入稳定的个人视角来修正这一点。

## 综合结论

最自然的综合方式，是一个分层仓库：

- `raw/external/` 存放外部证据
- `raw/personal/` 存放个人证据
- `wiki/topics/` 按话题存放面向世界的综合知识与应用分析
- `wiki/self/` 存放稳定判断模式
- `wiki/frameworks/` 存放高复用判断框架与 query 入口

这样可以在不把事实与个人判断混成一团的前提下，让两者生活在同一个系统里。

## 来源依据

- [LLM Wiki](../../../raw/external/llm-wiki.md)
- [Context Infrastructure](../../../raw/external/为什么AI只会说正确的废话，以及怎么把它逼出舒适区.md)
- [比较讨论](../../../raw/personal/conversations/比较两份材料的本地知识库方法与理念异同.md)

## 相关页面

- [Harness Engineering（约束壳工程）](../agent-harness-runtime/harness-engineering.md)
- [AI 知识系统的产品定义信念](ai-knowledge-systems-product-definition-beliefs.md)
- [知识库运行模型](knowledge-base-operating-model.md)
