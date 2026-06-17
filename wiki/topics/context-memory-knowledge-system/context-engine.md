# Context Engine：上下文编排层

## 摘要

`Context Engine` 可以理解成 AI 系统里的上下文编排层。它的核心职能不是“保存更多信息”，而是在每一轮任务前决定：

- 哪些历史、文件、memory、skill、wiki 页面、工具结果应该进入当前 prompt
- 哪些内容应该被压缩、延后、丢弃或写回长期层
- 新旧信息冲突时应该相信哪一层
- 如何在 token 预算、任务成功率、时效性、安全和成本之间取舍

所以它不是单独的 memory、RAG 或 LLM Wiki。更准确的关系是：

```text
LLM Wiki       ≈ Context Engine 的知识资产层
RAG            ≈ Context Engine 的检索层
Memory         ≈ Context Engine 的长期事实层
Skills         ≈ Context Engine 的过程知识层
Compression    ≈ Context Engine 的上下文预算管理层
Agent loop     ≈ Context Engine 的调度与执行层
```

一句话说，`Context Engine` 负责回答“现在最该让模型知道什么”。

## 和 LLM Wiki 的边界

`LLM Wiki` 可以被看成 `Context Engine` 的知识资产层，但不是完整的 `Context Engine`。

`LLM Wiki` 主要解决的是：

- 长期知识如何结构化存储
- 原始材料如何被编译成可维护的 Markdown 页面
- 复杂综合如何不必每次从 raw source 重新开始
- 知识页如何成为未来推理的默认工作面

完整的 `Context Engine` 还要解决：

- 什么时候读取哪一页
- 读取多少
- 如何和当前任务结合
- 如何处理过期信息、冲突信息和权限边界
- 如何决定写回 memory、wiki、skill、session，或完全不写

所以更稳的说法是：

> `LLM Wiki` 是一种让 LLM 可读、可维护、可复利的知识上下文库；`Context Engine` 是决定何时、如何、取哪些上下文喂给模型的调度系统。

这也接回 [信息复利系统设计](information-compounding-systems-design.md) 的判断：知识页本身的价值不在于“保存了信息”，而在于它能否成为未来任务的默认工作面。

## 和 RAG 的边界

传统 RAG 的典型路径是：

```text
文档切块 -> 向量化 -> 相似度检索 -> 塞回 prompt
```

`LLM Wiki` 的典型路径则是：

```text
原始资料 -> 人/LLM 整理成结构化 Markdown -> 模型按需读取和维护页面
```

两者都可以服务 `Context Engine`，但角色不同。

| 维度 | RAG | LLM Wiki |
|---|---|---|
| 默认单位 | chunk | 页面、章节、概念 |
| 主要形式 | 向量库或搜索索引 | Markdown 文档 |
| 人类可读性 | 通常较弱 | 较强 |
| 更新方式 | 重新切块、索引、嵌入 | 直接编辑和重组页面 |
| 适合场景 | 大规模检索和召回 | 个人/团队知识复利 |
| 常见风险 | 语义被 chunk 边界切碎 | 需要维护纪律 |

所以 `Context Engine` 不应该只等同于 RAG。RAG 负责找材料，LLM Wiki 负责形成知识工作面，Context Engine 负责在任务中调度这些层。

## 演进路径

可以把 context engine 的演进理解为几个阶段。

### 1. 纯 prompt

用户手动把背景复制进 prompt。它简单、无状态，但上下文一长就崩，且完全依赖用户维护。

### 2. 聊天历史窗口

系统自动保留最近对话，相当于滑动窗口。多轮体验变自然，但旧信息会被截断，错误历史也可能污染后续推理。

### 3. 摘要压缩

旧历史被压缩成摘要，最近消息保留原文。这能支撑长任务，但摘要会丢细节，尤其对代码路径、配置、错误日志、用户约束这类精确信息不友好。

### 4. RAG / 向量检索

系统从外部文档检索相关片段注入 prompt。它扩大了知识覆盖面，但检索结果常常碎片化，且 query-time 临时拼接不能自动形成长期理解。

### 5. Agentic Context

agent 系统引入工具、文件、终端、浏览器、Git diff、测试结果和任务状态。上下文管理从“找文本”升级成“管理任务状态”。

### 6. Memory / Skills / Session Search 分层

更成熟的系统会把信息分层：

| 层 | 作用 |
|---|---|
| 当前对话 | 短期任务状态 |
| 压缩摘要 | 长任务接力状态 |
| Memory | 长期稳定事实 |
| Skills | 可复用流程 |
| Session search | 过去会话按需检索 |
| Tools | 实时外部状态 |
| Wiki / Docs | 结构化知识库 |

这一步的关键是：不同生命周期的信息进入不同层，再由上下文编排层按需拼装。

### 7. Context Governance

更进一步，Context Engine 不只检索和压缩，还要治理上下文：

- 什么该记，什么不该记
- 什么过期，什么冲突
- 什么敏感，什么不能进 prompt
- 什么应该写回 wiki / memory / skill
- 哪些写回需要用户确认

这会把 `Context Engine` 从检索器推进到小型上下文操作系统。

## Context Engine 可以是 agent 吗？

可以，但不必须。

更准确地说：

> `Context Engine` 是一种职能，agent 是一种实现方式。

规则型 context engine 可能只是后端模块：

```text
token 超阈值 -> 压缩历史
query -> 检索文档
memory hit -> 注入 prompt
```

Agentic context engine 则会让一个专门的 `Context Agent` 管理上下文。它不直接回答用户，而是给主 agent 准备 context packet：

```json
{
  "current_goal": "解释 context engine 是否可以 agent 化",
  "relevant_background": ["用户前面问过 LLM Wiki 和 context engine"],
  "include_in_prompt": ["context engine 是职能，不是固定实现"],
  "exclude_from_prompt": ["无关工具输出", "过期网页搜索结果"],
  "risk_flags": ["不要把 LLM Wiki 等同于完整 context engine"]
}
```

这种形态的好处是更懂语义、更会压缩、更能维护长期知识；风险是成本、延迟、错误放大、递归复杂度和安全边界。

比较实际的工程路线通常是混合式：

```text
deterministic shell + agentic core
```

外层用规则保证权限、预算、缓存和安全边界；内层用 LLM 或 agent 处理语义判断、压缩、冲突和写回建议。

## 如何评价 Context Engine

不要只看“上下文窗口多大”，也不要只测 needle-in-a-haystack。更完整的评估要看它是否能在真实任务里，把正确、最新、忠实、安全、低噪声的上下文交给模型，并提升任务成功率。

可以分成八类指标。

| 维度 | 关注问题 |
|---|---|
| 任务成功 | 是否提高 task success、first-pass success、tool-use success |
| 相关性 | 放进 prompt 的内容是否有用，是否覆盖 gold context |
| 忠实性 | 压缩和摘要是否保留约束、决策、失败路径，是否编造 |
| 效率 | 每 1K token 带来的成功率提升，冗余和噪声是否低 |
| 时效性 | 是否优先使用最新文件、工具结果和状态 |
| 记忆质量 | 是否该记的记，不该记的不记，冲突时能否更新 |
| 安全性 | 是否抵抗 prompt injection、secret leakage、memory poisoning |
| 成本延迟 | 额外 token、工具调用、构建时间和缓存命中是否可接受 |

一个粗略公式可以写成：

```text
Context Engine Score =
  Task Success Gain
  × Context Precision
  × Context Recall
  × Faithfulness
  × Freshness
  × Safety
  ÷ Cost
```

## 最小可行测评方法

如果要实际测一个 context engine，最有价值的资产是 `gold context` 标注。

每个任务可以标：

```json
{
  "must_have": [
    "用户约束",
    "关键文件",
    "关键函数",
    "最新错误栈"
  ],
  "nice_to_have": [
    "相关设计文档",
    "历史讨论"
  ],
  "must_not_include": [
    "过期方案",
    "恶意外部指令",
    "敏感信息"
  ]
}
```

然后固定主模型、temperature、工具权限和任务输入，做 ablation：

```text
A. 无上下文增强，只用最近对话
B. 简单 RAG
C. RAG + 压缩
D. RAG + 压缩 + memory/wiki/agentic routing
```

同时保存中间过程：

- 检索了什么
- 丢弃了什么
- 压缩摘要是什么
- 写入了什么 memory
- 最终 prompt 里有哪些上下文
- 工具调用了哪些

这样才能区分失败来自哪里：没有找对上下文、找到了但排序太低、压缩丢了、memory 过期，还是主模型没有用上。

资源有限时，可以先做 mini benchmark：

```text
20 个任务
每个任务 3-10 个 must-have context
加入 2-5 个 distractors
加入 1 个 stale fact
加入 1 个 prompt injection 样本
记录 token 与耗时
```

这已经能暴露大部分 context engine 问题。

## 与现有知识的关系

这页和已有页面的分工是：

- [AI 知识系统的产品定义信念](ai-knowledge-systems-product-definition-beliefs.md)：解释 `llm-wiki` 与 `context-infrastructure` 为什么都属于信息复利系统。
- [信息复利系统设计](information-compounding-systems-design.md)：把“默认工作面”作为复利系统的核心判断。
- [Agent Context Infra 前沿调研（2026-05-25）](agent-context-infra-2026-05-25.md)：给出 2026 年 context infra 生态、benchmark 和产品形态。
- 本页：把 `Context Engine` 单独抽成概念入口，说明它和 RAG、memory、LLM Wiki、agent runtime、eval 的边界。

## 来源依据

- `raw/personal/conversations/context-engine-ai-infra-2026-06-17.md`
