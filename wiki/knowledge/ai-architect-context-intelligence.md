# AI Architect 的 Context Intelligence 镜头

## 摘要

这份课程讲义把 AI 记忆系统重新定义成一个 `Digital Twin` 的产品设计问题，而不是一个“先搭 RAG 再调参数”的实现问题。

它的核心主张是：真正稀缺的不是让模型知道更多公共知识，而是让它理解你的长期个人上下文。为此，最重要的架构决策不是选哪套向量库，而是先决定这个记忆系统究竟服务于哪类问题、允许知道什么、以及检索是否应该只是 agent 工具箱中的一个环节。

## 核心判断

### 记忆系统首先是在做个人上下文移植

讲义把通用 AI 的限制描述成一种“持续失忆”：

- 每次对话都从零开始
- 对公共知识的掌握无法替代对个人上下文的掌握
- 真正高价值的问题，往往都埋在个人笔记、会议纪要、博客、日志这些私有材料里

所以这类系统的目标，不是再教 AI 更多世界知识，而是把“你的世界”移植给它。

### 第一性决策是用途，不是技术栈

在这套镜头里，builder 会把任务描述成“做一个能查笔记的工具”，但 architect 会先问：

- 它主要服务快速事实检索，还是深层模式发现
- 它更像搜索框，还是研究助手
- 它应该读取全部材料，还是需要边界、分区与访问控制

这些问题会直接决定后续的 index 设计、agent prompt、工具编排方式，甚至决定这个系统是否值得被建。

### Static RAG 和 Agentic RAG 是两种不同架构

讲义把两者的分水岭讲得很明确：

- `Static RAG` 把用户原问题直接当查询，把相似文本块塞回 prompt。它是线性的、一次性的流程。
- `Agentic RAG` 则把检索视作 agent 的一个研究工具。agent 可以改写查询、进行多轮探索、在检索后再调用代码分析或外部搜索，最后综合成答案。

对于“项目延期最常见原因”这类需要跨文档聚合、统计和解释的问题，单轮相似度召回并不够。系统需要的不只是 retrieval，而是 retrieval 加 processing 加 synthesis 的闭环。

### 真正关键的是信息架构与边界设计

这份讲义没有把记忆系统想成一个无差别数据池，而是强调：

- 应先定义 `Digital Twin` 应该知道什么
- 也应明确它不该知道什么
- 私密日志、公开博客、工作材料和个人反思未必应放在同一访问面上

因此，访问控制、记忆分区与信任边界不是上线后补的安全项，而是第一批架构决策。

## 为什么课程刻意不教常见 RAG

### 不是否定检索，而是否定一个过渡态实现

讲义批评的不是“从大规模信息里取回稀疏相关知识”这个目标，而是行业里那套常见的朴素实现：

- 简单切块
- embedding 相似度召回
- 把召回结果塞进上下文窗口后直接生成

它认为这种默认范式有三类问题。

### 1. 它在重新发明搜索，而且起点很低

搜索与信息检索本来就是成熟领域，但流行 RAG 往往绕开既有积累，用很基础的切块和相似度搜索重新开始。这让大量优化只是迟到地补课，而不是站在现成能力上继续向前走。

### 2. 它的工作流过静态

在常见 RAG 里，search 只是给 LLM 喂原材料，整个链路无法自我调整。讲义认为这会给智能上限封顶，因为真正的复杂问题需要反复试探、改写问题、交叉验证和多工具配合。

### 3. 它依赖的瓶颈正在快速变化

讲义把 RAG 看成对“上下文窗口不够大、调用太贵”的一类过渡性补丁。随着上下文窗口、成本和推理速度持续变化，围绕旧瓶颈构造一整套复杂系统，未必是长期最稳的下注。

## 更值得学的方向

课程真正强调的是两件事：

- `LLM` 与 search engine 的联合优化，而不是简单串接
- 动态、agentic 的 retrieval workflow，而不是固定两步流水线

也就是说，检索仍然重要，但它更像一套被 agent 主动调用和重组的能力，而不是唯一主流程。

## Build Workflow 的真正重点

这份讲义还把 context intelligence 的实现过程，重新收束回上一模块的 `manage-and-create workflow`。

### 先做评测，再做系统

课程建议先定义一个小型评测集，而不是边做边凭感觉测试。示例 OKR 包括：

- `Hallucination Rate` 小于 10%
- `Needle in a Haystack` 检索精度达到 100%

这个动作的重要性在于，它把“感觉还行”的主观判断改成可重复的质量门槛。

### 先写 assignment brief，再让 AI 实现

课程没有把 prompt 视为咒语，而是把它视为一份任务说明书。真正重要的是：

- 目标是否清楚
- 约束是否明确
- 工具职责是否定义得足够清楚
- agent 是否被明确要求把检索当研究工具而不只是搜索框

### 迭代要先判断故障位于 retrieval 还是 generation

当系统失败时，讲义建议先分辨：

- 是检索没找到对的材料
- 还是材料找到了，但生成阶段误读或幻觉了

只有先分清这一层，后续的改动才知道该落在 chunk size、indexing strategy、tool description，还是 system prompt 上。

## 对本仓库主题的启发

这份来源和当前知识库已有页面之间，有几条很强的连接：

- 它把 `AI Architect Lens` 从一般产品定义推进到“个人记忆系统”的具体架构决策。
- 它和 [本地知识库模式](local-knowledge-base-patterns.md) 一起说明，长期可用的知识系统不该只是 query-time 检索。
- 它和 [AI 知识系统的产品定义信念](ai-knowledge-systems-product-definition-beliefs.md) 形成互证：真正高价值的系统，往往先决定默认工作面与蒸馏目标，再决定检索工具怎么接入。

## 来源依据

- [Context Intelligence: Granting Your AI a Memory](../../raw/external/ai-architect-context-intelligence.md)

## 相关页面

- [AI Architect Lens](ai-architect-lens.md)
- [AI Architect 的 Proactive Intelligence 镜头](ai-architect-proactive-intelligence.md)
- [AI Architect 的 Advanced Architecture 镜头](ai-architect-advanced-architecture.md)
- [AI 知识系统的产品定义信念](ai-knowledge-systems-product-definition-beliefs.md)
- [本地知识库模式](local-knowledge-base-patterns.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
