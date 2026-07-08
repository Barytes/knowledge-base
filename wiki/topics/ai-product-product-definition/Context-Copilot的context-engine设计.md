# Context Copilot 的 context engine 设计

## 摘要

如果 `Context Copilot` 的愿景是让 AI 在写作、产品定义、研究判断和构建过程中持续理解用户，而不是每次从零开始，那么它的 `context engine` 不应被设计成一个泛 memory/RAG 系统。

它更应该是：

> 一个把用户正在形成的理解、判断边界、材料来源、失败纠正和当前工作状态，持续整理成可被 agent 调用的上下文工作面的系统。

它的核心任务不是“记住更多”，而是让下一次协作少一点误解、少一点重复铺垫、少一点 AI slop，多一点自然接话、保真延续和可验证写回。

## 产品边界

`Context Copilot` 最容易失败的方向，是把自己做成总结器、dashboard、个人知识库搜索框或“自动给建议”的 wrapper。

更好的边界是：它不替用户做最终判断，也不把用户压进固定字段；它负责维护一个能服务当前任务的 context state，让主 agent 在合适时刻知道：

- 用户现在真正想推进什么
- 哪些 framing 已经被否定
- 哪些材料是来源，哪些是用户自己的理解
- 哪些判断还只是观察，哪些已经稳定
- 这次输出应该接在哪条思路后面
- 什么东西不该再被 AI 重复建议

所以它的主产品场景不是“我问，它答”，而是“我持续想、写、做，它帮我带着上下文继续”。

## 核心对象

第一版不要先做复杂图数据库。先把 context engine 的对象定义清楚。

`Source`：原始材料。包括笔记、对话、网页、代码、会议记录、草稿。它只负责证据和回查。

`Working Context`：当前工作状态。包括目标、材料、约束、最近决策、否定过的方向、当前卡点。它是任务内默认工作面。

`Understanding State`：用户对某个 idea 的当前理解。它不是偏好画像，而是一个正在演化的解释结构，包含核心表达、反规格说明、张力和未决问题。

`Memory Candidate`：可能值得长期保存的观察。默认低置信，不直接变成规则。

`Pattern / Rule / Skill`：经过多次验证后才能进入稳定层。这里才是长期复利层。

`Context Packet`：每次 agent 工作前生成的上下文包。它不是全量记忆，而是这次任务真正需要的材料组合。

`Review / Writeback`：任务结束后的人工或半自动审查。决定哪些内容丢弃、保留、降级、升级或写回。

## 读路径

读路径应服务“自然接上用户当前理解”，而不是机械召回相似文本。

合理流程是：

```text
task intent
-> identify active thread
-> load working context
-> retrieve supporting sources
-> include rejected framings
-> assemble context packet
-> run main agent
```

这里最重要的是 `active thread`。例如用户问 `context-copilot`，系统不应只召回所有带 context 的材料，而要识别这是同一条产品探索线：反感 AI slop、反感固定字段、重视 writing 场景、重视 context continuity，而不是泛泛 dashboard。

因此检索要分两层：

- 结构化路由：先判断主题、产品线、任务类型、用户意图。
- 语义检索：再找具体材料、相邻页面、旧对话、失败样本。

如果只做向量相似度，系统会很容易把所有叫 `context` 的东西混在一起。

## 写路径

写路径必须慢，尤其是关于用户偏好和产品直觉的写入。

建议分成四级：

```text
capture -> observation -> pattern candidate -> stable rule / skill
```

`capture` 自动记录任务过程、引用材料、输出、用户纠正。

`observation` 提炼单次有效信号，例如“用户反感把 context-copilot 压成周报式字段”。

`pattern candidate` 需要跨多次任务重复出现，才进入候选稳定层。

`stable rule / skill` 只有在确实能改善后续协作时才写入默认工作面。

这条门禁很关键。`Context Copilot` 的最大风险不是忘记用户，而是过早把一次表达固化成粗暴画像，然后以后每次都用错误规则打断用户。

## 运行时结构

第一版应采用 `thin runtime + file-based working layer + agentic routing`。

```text
Capture Layer
  收集来源、对话、草稿、代码、任务结果

Context Store
  raw sources
  working contexts
  understanding states
  observations
  skills / rules
  eval cases

Router
  判断任务类型、active thread、可见范围、需要读取的层

Context Assembler
  生成 context packet，控制 token、顺序、来源和排除项

Main Agent
  写作、分析、构建、复盘

Review / Writeback
  人审或半自动决定是否写回、升级、废弃、纠错

Trace / Eval
  记录读了什么、漏了什么、上下文是否帮助任务
```

runtime 不要太厚。真正的判断应尽量沉淀到文件、skills、框架和 eval cases。这样用户和 agent 都能检查系统为什么这样接话。

## 最小 MVP

最小版本不要做全量个人记忆，也不要接所有 app。

更锋利的 MVP 是围绕一个高频场景：

> 用户围绕一个产品想法连续写作、讨论、反驳、修正，系统能在下一次对话或写作时自动带回正确的理解状态。

最小文件结构可以是：

```text
context-copilot/
  sources/
  threads/
    context-copilot.md
  observations/
  packets/
  eval-cases/
  writeback-log.md
```

第一版只需要四个动作：

1. `capture`：把一段对话或草稿挂到某条 thread。
2. `distill`：提炼 active understanding、rejected framings、open questions。
3. `assemble`：为下一次写作或 agent 任务生成 context packet。
4. `review`：用户确认哪些理解保留、哪些删掉、哪些写成规则。

只要这条链能稳定减少“AI 又误解我了”的次数，就比做一个漂亮 dashboard 更接近愿景。

## 评测方式

不要先测“召回了多少记忆”。应该测：

- 是否接住用户当前 framing
- 是否避免重复已经被否定的建议
- 是否区分来源材料和用户自己的判断
- 是否减少用户重复解释的次数
- 是否让写作或产品定义更快进入有效状态
- 是否有错误写回、过度概括、隐私越界

可以做 10 个真实 episode。每个 episode 标注：

- `must_include`：这次必须带回的上下文
- `must_not_include`：过期、错误、被否定或越权的上下文
- `stance`：这次 agent 应该采用的接话姿态
- `failure_mode`：如果失败，属于漏召回、误召回、压缩失真、过度建议，还是写回污染

这比通用 memory benchmark 更能验证 `Context Copilot` 是否真的成立。

## 推荐设计取向

推荐先走“写作/产品探索 context continuity”路线，而不是“全能个人 memory”路线。

原因很简单：`Context Copilot` 的独特价值不在于知道用户生日、项目列表或日程，而在于能保存并带回那些正在形成、还没有固定成知识页或任务表的理解状态。

这也是它和普通知识库、RAG、dashboard 的区别：它维护的不是事实集合，而是“用户正在怎样理解这件事”。

## 相关页面

- [个人 AI 工作流：从问答到系统化委托](个人AI工作流从问答到系统化委托.md)
- [AI 产品反向筛选经验：避免 wrapper 与 slop](AI产品反向筛选经验-避免wrapper与slop.md)
- [AI Architect 的 Context Intelligence 镜头](ai-architect-context-intelligence.md)
- [Context Engine：上下文编排层](../context-memory-knowledge-system/context-engine.md)
- [长期 file-based context engine 设计](../context-memory-knowledge-system/file-based-context-engine-design.md)
- [产品探索保真优先观察](../../self/产品探索保真优先观察.md)
