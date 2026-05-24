# Harness 架构判断框架

这页服务于 agent harness、coding agent、tool use、上下文控制、默认壳厚度、可观察性与工作流编排这类问题。

它不回答某个产品到底好不好，而是先回答：这套 harness 到底在补偿什么，厚度该放在哪里，以及哪些复杂性应该内建、哪些应该外置。

## 先看什么

遇到 harness 问题时，优先先问七件事：

1. 当前主要失败在模型本身，还是在外层控制壳
2. 这套系统在补偿模型的哪类弱点
3. 智能步骤和确定性步骤有没有被放在正确的一边
4. 复杂性是被做进默认壳，还是被外置到 skills、文件、CLI 与工作流里
5. subagent 在这里是角色分工，还是上下文隔离
6. 系统优先追求的是开箱即用，还是可观察性与可改造性
7. 随着模型变强，哪些补偿面会从杠杆变成负担

## 核心判断

### 1. agent 的很多进步来自 harness，不只来自模型

长流程、跨步骤、跨文件任务里，真正让 agent 不漂移、不误判完成、不协同坍塌的，往往是模型外侧那层控制壳，而不只是权重升级。

主要依据：
- [Harness Engineering（约束壳工程）](../knowledge/harness-engineering.md)
- [Claude Code：较厚的 agentic coding harness](../knowledge/claude-code-harness.md)
- [Pi coding agent：一种极简且可观察的 coding harness](../knowledge/pi-coding-agent-harness.md)

### 2. Harness 首先是在补偿模型弱点，而且补偿面会移动

- 上下文保持不够稳，就会出现 compaction、reset、状态外化
- 不擅长定义完成标准，就会出现 contract、gating、plan
- 不擅长可靠自评，就会出现独立验证与 evaluator

所以重点不是“壳越厚越好”，而是持续追踪：哪些补偿仍然必要，哪些已经开始变成负担。

主要依据：
- [Harness Engineering（约束壳工程）](../knowledge/harness-engineering.md)
- [Thin Harness, Fat Skills](../knowledge/thin-harness-fat-skills.md)

### 3. 先分清 latent space 和 deterministic space

最常见的系统错误，是把该交给确定性工具的事塞进模型判断，或者把该留给模型综合判断的事硬做成死流程。

- latent space 负责阅读、解释、判断、综合
- deterministic space 负责查询、编译、执行、验证、约束

最好的 harness 不是让模型接管一切，而是对这条边界保持冷酷。

主要依据：
- [Thin Harness, Fat Skills](../knowledge/thin-harness-fat-skills.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../knowledge/AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md)

### 4. 壳厚度的核心张力，是开箱即用能力 vs 可观察性与可改造性

较厚的 harness 倾向内建：

- plan mode
- memory
- compaction
- permissions
- checkpoints
- subagents
- 扩展面

较薄的 harness 倾向只保留最小工具面，把复杂性外置到：

- skills
- 文件
- CLI
- `tmux`
- packages / extensions

厚壳的好处是默认能力更强。薄壳的好处是更透明、更容易理解系统到底做了什么。

主要依据：
- [Claude Code：较厚的 agentic coding harness](../knowledge/claude-code-harness.md)
- [Pi coding agent：一种极简且可观察的 coding harness](../knowledge/pi-coding-agent-harness.md)
- [Claude Code、Codex 与 pi 的 harness 对比](../knowledge/coding-agent-harness-comparison.md)

### 5. subagent 的本质常常是上下文隔离，不是拟人分工

在复杂代码库里，subagent 最重要的作用往往不是扮演“前端”“后端”“QA”，而是把探索噪音留在子上下文里，只把压缩后的结论回传给主上下文。

这时它真正解决的是上下文污染，而不是角色感。

主要依据：
- [coding agent 的上下文压缩工作流](../knowledge/coding agent 的上下文压缩工作流.md)
- [Thin Harness, Fat Skills](../knowledge/thin-harness-fat-skills.md)

### 6. 复杂代码库里的核心资源是上下文预算，不是上下文总量

上下文不是越多越安全。很多时候，越接近上限，结果反而越差。真正关键的是：

- 旧上下文能否被压成任务状态
- facts / plan / execution space 能否分层压缩
- 主上下文里保留的是高杠杆信息，还是大量搜索噪音

主要依据：
- [coding agent 的上下文压缩工作流](../knowledge/coding agent 的上下文压缩工作流.md)
- [Harness Engineering（约束壳工程）](../knowledge/harness-engineering.md)

### 7. 智能应尽量推到 skills，执行应尽量压到确定性工具

当系统把判断流程写进 skills，把查询、执行、验证压进窄而快的工具层时，模型升级会自动放大整套系统，而确定性层仍保持可靠。

这比把大量智能混进厚重 God-tools 或把每个动作都塞进巨大 prompt 更容易复利。

主要依据：
- [Thin Harness, Fat Skills](../knowledge/thin-harness-fat-skills.md)
- [Pi coding agent：一种极简且可观察的 coding harness](../knowledge/pi-coding-agent-harness.md)

## 常见张力

- 模型升级 vs 壳层补偿
- 厚壳默认能力 vs 薄壳可观察性
- latent 判断 vs deterministic 执行
- 内建 orchestration vs 外置编排
- subagent 角色化 vs 上下文隔离
- 更多上下文 vs 更干净的工作台

## 推荐阅读顺序

1. [Harness Engineering（约束壳工程）](../knowledge/harness-engineering.md)
2. [Thin Harness, Fat Skills](../knowledge/thin-harness-fat-skills.md)
3. [coding agent 的上下文压缩工作流](../knowledge/coding agent 的上下文压缩工作流.md)
4. [Claude Code、Codex 与 pi 的 harness 对比](../knowledge/coding-agent-harness-comparison.md)
5. 如涉及具体产品取舍，再补读 [Claude Code：较厚的 agentic coding harness](../knowledge/claude-code-harness.md) 与 [Pi coding agent：一种极简且可观察的 coding harness](../knowledge/pi-coding-agent-harness.md)

## 什么时候进入 bridge

如果问题已经具体到某个 harness 方案、某个 repo、某个产品路线、某次工具取舍或某个团队工作流，再进入相应 `bridges/` 页面。

## 相关页面

- [框架路由入口](router.md)
- [AI 系统产品判断框架](AI系统产品判断框架.md)
- [知识系统判断框架](知识系统判断框架.md)
