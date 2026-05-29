# Claude Code：较厚的 agentic coding harness

## 摘要

按当前本地资料，Claude Code 不是“给 Claude 加几个工具”的薄壳，而是一套较厚的 agentic harness。它把模型、工具、上下文管理、权限系统、checkpoint、memory、subagents、MCP、hooks 与多界面运行方式整合成一个统一产品面。

如果说 `pi` 的主张是把很多复杂性外置到文件、CLI 和扩展层，那么 Claude Code 更像是在产品核心里直接把这些能力做成默认工作面。

当前可见的核心判断有三条：

- 把 agent loop 显式产品化为 `gather context -> take action -> verify results` 的闭环。
- 把长期协作里的关键控制问题内建进核心，包括 context compaction、session persistence、permissions、checkpoints 与 subagents。
- 接受更厚的系统层和更多内建机制，以换取更强的开箱即用能力，而不是把这些能力主要留给用户自己拼装。

## 证据分层

这页的依据分成两类：

- 高置信度：Anthropic 官方文档 `How Claude Code works`
- 中低置信度：`Claude Code: An analysis` 这篇 didactic 外部分析稿。它明确声明不是源码逆向定稿，而是多模型协作生成的教学性重构，因此更适合拿来补“可能的实现形状”，不适合单独当成事实依据

下面正文会尽量把这两层分开。

## 官方文档明确说了什么

### 1. 它把 agent loop 直接写成产品定义

官方文档把 Claude Code 的核心工作方式定义为三阶段循环：

- gather context
- take action
- verify results

这个循环不是只在“修 bug”时才出现，而是被当成统一的执行框架。问题在于不同任务只会在三阶段之间停留不同时间，而不是切换到不同模式。

这说明 Claude Code 对自己的定位不是聊天工具加工具调用，而是一个围绕验证闭环组织起来的 coding agent harness。

### 2. 工具面比 `pi` 更厚，也更显式分层

官方文档把内建工具分为：

- file operations
- search
- execution
- web
- code intelligence

并明确提到还有：

- subagents
- asking user questions
- 其他 orchestration tools

相比 `pi` 默认只给四个核心工具，Claude Code 的默认面显然更厚，而且把“工具是编排层的一部分”讲得更公开。

### 3. 上下文与持久记忆是核心能力，不是附属功能

官方文档明确把这些都算作 Claude Code 默认能访问的工作面：

- 当前项目与 git state
- `CLAUDE.md`
- auto memory
- 配置好的 MCP、skills、subagents、Chrome 扩展等

这意味着 Claude Code 不是把“项目记忆”当成额外插件，而是把它作为会话起点的一部分。

### 4. session 与 compaction 被深度产品化

官方文档明确说明：

- 会话保存在本地 JSONL 文件中
- 支持 resume 与 fork
- 不同终端可恢复同一 session
- context window 会自动 compaction
- compaction 会先清工具输出，再在必要时总结对话
- subagents 通过独立上下文来减轻主上下文膨胀

这说明 Claude Code 很认真地把“长会话如何不崩”当作核心系统问题，而不是可选增强。

### 5. permissions 与 checkpoints 是安全主轴

官方文档里最明确的两条安全机制是：

- checkpoints：每次编辑前保存文件快照，允许 rewind / undo
- permissions：从默认模式、auto-accept edits、plan mode 到 auto mode 的多档权限控制

这表明 Claude Code 并不接受 `pi` 那种 `YOLO by default` 的哲学，而是把“让用户逐层放权”做成产品内核。

### 6. 它默认把扩展系统当正式一层

官方文档把这些都作为标准扩展面来讲：

- skills
- MCP
- hooks
- subagents

也就是说，Claude Code 的设计不是“尽量没有二级系统”，而是“核心 loop 之外，再叠一层正式支持的可扩展控制面”。

## 从外部分析稿里能谨慎补出的东西

外部分析稿不是官方定稿，但有几点作为“可能的实现风格”仍然有参考价值。

### 1. 它很可能是 streaming-first 的

分析稿反复强调：

- 实时 LLM streaming
- partial JSON parsing
- UI incremental updates
- 工具执行与界面更新并行推进

这和官方文档对 agentic loop、长会话与多工具交互的描述是相容的，因此这点可以作为中等置信度推断。

### 2. 它把控制问题拆得比表面功能更多

分析稿提到的重点不是“有哪些按钮”，而是：

- side-effect-aware tool scheduling
- parallel read-only tools
- serialized writes
- data truncation
- permissions cascade
- 多层 telemetry

即便具体名词未必都准确，这也提示 Claude Code 的实现重点很可能在 orchestration engine，而不只是 prompt engineering。

### 3. prompt 可能比 `pi` 重得多

分析稿强调 verbose prompt、重复强调关键约束、对 BashTool 施加大量安全说明。这个方向和已有本地材料中 `pi` 作者对 Claude Code 的观察是一致的。

因此较稳妥的判断是：Claude Code 确实更依赖较厚的 instruction layer 来约束模型行为。

## 结构上可以怎样理解 Claude Code

按当前本地材料，一个相对稳妥的结构图是：

1. 模型层：Claude model 负责推理与决策
2. 工具层：文件、搜索、执行、web、code intelligence，以及更高阶 orchestration tools
3. 状态层：session JSONL、`CLAUDE.md`、auto memory、git state、context compaction
4. 控制层：permissions、checkpoints、plan mode、subagents、MCP、hooks
5. 界面层：terminal、desktop、IDE、web、remote control、Slack、CI

这个结构的关键，不是每层都新奇，而是 Claude Code 把它们合成了一个统一产品，而不是让用户自己从很多松散组件拼起来。

## 它和 `pi` 最不同的地方

### Claude Code 默认更厚

`pi` 默认只保留最小工具面，然后把很多能力移出核心。Claude Code 则把更多能力直接放进默认产品工作面：

- plan mode
- backgrounded / managed execution
- subagents
- auto memory
- permissions modes
- checkpoints
- MCP / hooks / skills 正式扩展层

### Claude Code 更强调“制度化控制”

如果用 harness engineering 的语言说，Claude Code 更像把很多补偿层直接内建：

- 防上下文膨胀：compaction、subagent isolation
- 防危险执行：permissions modes
- 防错误修改：checkpoints
- 防跨会话信息丢失：memory 与 session persistence

这和 `pi` “默认信任用户自己管理工作流”的思路很不一样。

### 代价是黑箱感和系统厚度上升

从本地材料看，这种路线的代价也很明显：

- 用户更难完整理解系统到底注入了什么
- 版本更新更容易改变行为边界
- 某些高级能力虽然方便，但可观察性较弱
- 产品会更依赖官方定义的默认工作流

## 一个更抽象的判断

Claude Code 的重要性，不只在于它“做了很多功能”，而在于它把 2025 年以后 coding agent 里很多原本分散的工程机制产品化了：

- `CLAUDE.md`
- session persistence
- compaction
- permission modes
- plan mode
- subagents
- extension surfaces

换句话说，它代表的是一种更强 productized orchestration 的路线。

如果 `pi` 代表的是“极简核心 + 用户自编排”，那么 Claude Code 更接近“较厚核心 + 官方默认工作流”。

## 来源依据

- [How Claude Code works](../../../raw/external/claude-code-how-it-works.md)
- [Claude Code: An analysis](../../../raw/external/claude-code-analysis-southbridge.md)
- [Claude Code、Codex 与 pi 的 harness 对比](coding-agent-harness-comparison.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)

## 相关页面

- [Claude Code、Codex 与 pi 的 harness 对比](coding-agent-harness-comparison.md)
- [Pi coding agent：一种极简且可观察的 coding harness](pi-coding-agent-harness.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
