---
title: "Scaling Managed Agents: Decoupling the brain from the hands"
source: "https://www.anthropic.com/engineering/managed-agents"
author:
  - Lance Martin
  - Gabe Cemaj
  - Michael Cohen
published: 2026-04-08
created: 2026-05-28
type: source-note
tags:
  - ai-agent
  - managed-agents
  - agent-runtime
  - harness
  - sandbox
  - session-log
---

# Scaling Managed Agents: Decoupling the brain from the hands

这是 Anthropic Engineering 发布的 Claude Managed Agents 架构文章。本文不全文镜像原文，只保存官方链接、本地检索摘要和摄取时提炼的证据点。

官方原文：<https://www.anthropic.com/engineering/managed-agents>

## 本地摘要

文章解释 Anthropic 如何把 Managed Agents 从单容器设计改成以稳定接口为核心的托管 agent runtime。核心动机是：harness 会编码某一代模型的弱点，但模型能力变化很快，旧 harness 补丁可能变成负担。因此平台不应押注某个具体 harness，而应押注能长期稳定的接口。

Anthropic 将 agent virtualize 成三个对象：

- `session`：append-only event log，保存任务全过程。
- `harness`：调用 Claude、调度工具调用、管理上下文的 agent loop。
- `sandbox`：执行代码、编辑文件、访问工具的运行环境。

文章的主要架构变化是把 `brain`、`hands` 和 `session` 解耦：

- `brain` 是 Claude + harness。
- `hands` 是 sandbox、tool、MCP server、外部执行环境等。
- `session` 是独立于二者的 durable log。

这样做以后，sandbox 和 harness 都可以被看作可替换、可失败、可重启的组件。sandbox 通过 `execute(name, input) -> string` 暴露成工具；失败时由 harness 把错误反馈给 Claude，并可通过 `provision({resources})` 重新创建。harness 失败后，也能通过 `wake(sessionId)`、`getSession(id)` 和 `emitEvent(id, event)` 从 session log 恢复。

## 关键证据点

- 早期把 session、harness、sandbox 放在同一个容器里，带来直接文件 syscall、少服务边界等便利，但容器失败会导致 session 丢失，也让 debug 和客户 VPC 接入变困难。
- 官方把这种失败类比为把容器当成需要照顾的 `pet`，而不是可替换的 `cattle`。
- 安全边界的关键，是让凭证不进入 sandbox。Git token 可以在 sandbox 初始化时被用于配置 remote；custom tools 通过 MCP proxy 和外部 vault 获取 OAuth credentials，harness 本身不接触凭证。
- `session` 不是 Claude 的 context window。context window 会被裁剪、压缩和重组；session log 是外部、持久、可查询的事实源。
- `getEvents()` 让 brain 可以按位置切片查询事件流，再由 harness 把需要的片段转成当前模型上下文。
- 解耦之后，许多会话无需等待 sandbox 预热即可开始推理。Anthropic 报告该架构让 p50 TTFT 下降约 60%，p95 下降超过 90%。
- 多个 brain 可以连接多个 hand；hand 可以是容器、MCP server、自定义工具、设备或其他执行环境。

## 原文结构化摄取

### 开篇：harness assumptions 会过期

文章从 Anthropic Engineering Blog 既有主题切入：如何 build effective agents，以及如何为 long-running work 设计 harness。它指出一个共同问题：harness 往往是在补偿 Claude 当前做不到或做不稳的事情，因此会编码某一代模型的能力边界。

原文举了一个具体例子：Claude Sonnet 4.5 在接近上下文上限时会过早收尾。团队曾通过 harness 中的 context reset 处理这个问题。但同一套 harness 用到 Claude Opus 4.5 时，这个行为已经消失，context reset 反而成为无效负担。

因此 Anthropic 的判断是：harness 会持续演化，Managed Agents 不应把平台设计绑定在某个特定 harness 上，而应提供少量足够稳定的接口。文章把这个问题类比为操作系统设计：OS 通过 process、file 等抽象，让上层程序不需要绑定具体硬件；Managed Agents 试图用类似方式，把 agent components virtualize。

### 三个被虚拟化的 agent 组件

原文把 Managed Agents 的核心对象拆成三类：

- `session`：任务中发生过的一切的 append-only log。
- `harness`：调用 Claude、接收 Claude tool calls、再把工具调用路由给相关基础设施的 loop。
- `sandbox`：Claude 可以运行代码、编辑文件的 execution environment。

这三个对象之间通过接口连接。每个对象的实现可以替换，而不会扰动其他对象。Anthropic 说他们对接口形状有明确意见，但不把平台绑定到今天具体运行在接口背后的实现。

### Don’t adopt a pet：单容器设计的问题

Anthropic 最初把 session、harness 和 sandbox 放进同一个 container。这样有短期好处：文件编辑可以直接走 syscall，也不必设计额外服务边界。

但这个结构把 container 变成了不能随便丢弃的单点对象。container 失败会导致 session 丢失；container 无响应时，团队需要想办法救回它。调试也变得困难，因为外部只能看到 WebSocket event stream，很难区分到底是 harness bug、event stream 丢包，还是 container 掉线。若工程师需要进入 container shell 排查，又会碰到用户数据隔离问题。

第二个问题是连接客户 VPC。早期 harness 默认 Claude 处理的所有资源都在同一个 container 里。如果客户希望 Claude 访问自己的 VPC，Anthropic 就要么和客户网络 peer，要么把 harness 跑进客户环境。一个写死在 harness 里的位置假设，变成了接入不同基础设施的障碍。

### Decouple the brain from the hands

文章的解决方式，是把 `brain`、`hands` 和 `session` 分开：

- `brain`：Claude 和 harness。
- `hands`：sandbox 和真正产生动作的工具。
- `session`：独立保存 session events 的 durable log。

解耦后，harness 不再住在 container 里。container 被抽象成普通 tool，接口是 `execute(name, input) -> string`。如果 container 失败，harness 把失败作为 tool-call error 反馈给 Claude；如果 Claude 决定重试，系统可以通过 `provision({resources})` 用标准 recipe 初始化新 container。

harness 自身也可以失败，因为 session log 不在 harness 内部。新 harness 可以通过 `wake(sessionId)` 启动，通过 `getSession(id)` 取回事件日志，并从最后一个事件继续。运行过程中，harness 用 `emitEvent(id, event)` 写入 durable record。

这带来的关键变化是：container 和 harness 都从不能丢的 stateful object，变成可以重启、替换、失败后恢复的组件。

### 安全边界：credentials 不进入 sandbox

单容器设计还有一个安全问题：Claude 生成的不可信代码，与 credentials 处在同一个环境里。如果 prompt injection 诱导 Claude 读取自己的环境变量，攻击者拿到 token 后可以开启新的不受限制 session。

Anthropic 认为单纯缩小 token scope 不够，因为这仍然依赖一个假设：Claude 无法用有限 token 做出危险动作。但 Claude 会越来越聪明，所以结构性修复是让 token 根本不出现在 sandbox 中。

文章给出两种模式：

- 对 Git：在 sandbox initialization 阶段用 repo access token clone 仓库，并把 remote 配好。之后 sandbox 内可以执行 Git push / pull，但 agent 不直接接触 token。
- 对 custom tools：支持 MCP，并把 OAuth tokens 存在外部 secure vault。Claude 通过专门 proxy 调 MCP tools；proxy 接收 session token，再去 vault 找对应 credentials。harness 本身也不知道具体 credentials。

### Session 不是 Claude 的 context window

长任务经常超过 Claude context window。传统处理办法包括 compaction、memory tool、context trimming 等。它们都有价值，但会带来不可逆的保留/丢弃决策。未来 turns 需要哪些 tokens 很难提前判断，compaction 后原始消息如果没有被保存，就只能恢复摘要版本。

Managed Agents 把 session 当成 living outside context window 的 context object。但它不把这个 context object 放在 sandbox 或 REPL 里，而是保存在 durable session log 中。

`getEvents()` 让 brain 可以读取 event stream 的位置切片，例如：

- 从上次停止读取的位置继续。
- 回退到某个事件之前，查看它发生前的上下文。
- 重新读取某个 action 之前的历史。

harness 可以把取回来的 events 转换成当前 Claude context window 里的材料。转换方式可以包括 prompt cache 优化、context organization、context engineering 等。Anthropic 有意把 recoverable context storage 放在 session，把具体 context management 留给 harness，因为未来模型需要什么 context engineering 还不可预知。

### Many brains：多个 brain 的扩展

解耦 brain 和 hands 后，客户 VPC 接入更容易，因为 harness 不再假设所有资源都在本地 container 旁边。

这也带来性能收益。早期设计下，一个 brain 对应一个 container。每个 session 都要等 container provision、clone repo、启动进程、拉取 pending events，才能开始 inference。这个等待体现在 TTFT，即从接受任务到第一个 response token 出现之间的延迟。

解耦后，container 只有在 brain 真的需要执行环境时，才通过 tool call provision。某些 session 一开始不需要 container，就可以在 orchestration layer 拉到 session log 后直接启动推理。Anthropic 报告这让 p50 TTFT 下降约 60%，p95 下降超过 90%。

### Many hands：多个执行环境

Anthropic 还希望一个 brain 可以连接多个 hand。现实含义是 Claude 要能理解多个执行环境，并决定把工作发往哪里。这比只在单一 shell 中操作更难，所以早期模型可能需要单容器简化问题。

但随着模型能力提升，单容器反而变成限制。一个 container 失败，会让 brain 正在接触的所有 hand 状态都受影响。

解耦后，每个 hand 都是一个 tool。接口仍然可以统一成 name + input 输入，string 输出。这可以覆盖 custom tool、MCP server、Anthropic 自有工具、container、手机，甚至其他特殊执行环境。因为 hand 不和某个 brain 绑定，brain 之间也可以传递 hand。

### 结论：Managed Agents 是 meta-harness

文章最后回到“为未来还没想到的程序设计系统”的问题。OS 的长寿来自它把硬件虚拟化成足够通用的抽象。Managed Agents 试图对 Claude 周边的 harness、sandbox 和其他组件做类似处理。

Anthropic 把 Managed Agents 定义为 `meta-harness`：它不假设未来 Claude 一定需要哪一种具体 harness。Claude Code 可以是优秀 harness，某些 narrow domains 也可能需要 task-specific harness。Managed Agents 的目标是容纳这些不同 harness，并随着 Claude intelligence 的变化继续匹配。

这个 meta-harness 的设计重点是稳定接口：Claude 需要能操作 state，即 session；需要能 perform computation，即 sandbox；还需要能扩展到 many brains 和 many hands。系统应能长期可靠、安全地运行这些接口，但不假设 brain / hand 的数量或位置。

## 对本库已有判断的校准

这篇原文比中文读后感更具体地给出 Anthropic 自己的 engineering decisions。它能校准三条已有判断：

1. **harness 腐化不是抽象担忧，而是 Anthropic 已经遇到的模型升级问题。** Sonnet 4.5 到 Opus 4.5 的 context reset 例子说明，某代模型的补丁可能很快变成下一代模型的负担。
2. **session log 是比 context window 更底层的事实源。** 原文把 `getEvents()` 设计成可 interrogation 的 event stream，而不只是后台日志。
3. **brain / hands 解耦带来的不是架构洁癖，而是安全、恢复、客户环境接入和 TTFT 的直接收益。**

## 对本知识库的价值

这篇文章把 agent runtime 的核心问题从“怎么写更好的 agent loop”推进到“如何为未来还没出现的 harness / sandbox / tool 设计稳定接口”。它与本库已有的 `harness assumptions rot`、`context window is not runtime`、`session log`、`control plane / data plane`、`disposable runtime` 等判断直接对应。

维护页见：

- [Agent 系统作为 OS 与 Cloud Runtime 问题](../../wiki/knowledge/agent-runtime-os-cloud-runtime.md)
- [Harness Engineering（约束壳工程）](../../wiki/knowledge/harness-engineering.md)
- [Agent Context Infra 前沿调研（2026-05-25）](../../wiki/bridges/agent-context-infra-2026-05-25.md)
