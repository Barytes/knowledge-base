# Codex-like agent harness 路线图

## 摘要

这个想法的核心不是“复制一个 Codex”，而是把 Codex 暴露出来的 agent harness 能力压缩成 `my-little-agent-loop` 可以实现、可以评测、可以服务 `context-core` 和 `oh-share-it` 的内核。

更准确的定位是：

> `my-little-agent-loop` 是一个最小 Codex-like agent harness，用来提供可追踪 tool use、可恢复 session、patch-based editing、permissioned execution、trace / replay / evaluator loop，以及和 `context-core` 对齐的上下文质量闭环。

它仍然是支撑项，不应抢走本月两个旗舰项目的位置。旗舰项目仍是：

- `context-core`：agent context infra 的核心层。
- `oh-share-it`：真实部署、协作与评测场景。

`my-little-agent-loop` 的价值，是证明自己不仅会“用 agent”，也能拥有 agent runtime / harness 的工程主权。

## 什么叫 Codex-like

这里的 `Codex-like` 指一组 agent harness 能力，而不是某个完整产品形态。

最小能力包括：

1. `Session`：会话、状态、工作目录、resume / fork / compact 的基本模型。
2. `Tool Runtime`：文件读取、搜索、patch 编辑、命令执行、浏览器或外部工具调用的统一事件流。
3. `Permission / Sandbox`：读、写、执行、网络、危险命令的权限边界。
4. `Plan / Todo`：把长任务拆成可观察的执行状态，而不是只靠模型隐式记忆。
5. `Diff / Patch`：所有文件修改都走可审计 patch，而不是黑箱写文件。
6. `Trace / Replay`：记录 agent 的输入、工具调用、上下文、输出、失败标签，并支持重跑固定任务。
7. `Eval Harness`：把 replay 结果接到评分、人工评审或 regression case。
8. `Skill System`：把可复用流程、判断标准和项目规则外置成可加载文件。

后续再考虑：

- subagents：主要用于上下文隔离，而不是角色扮演。
- worktrees：让长任务在隔离工作区里运行。
- cloud / remote task runner：把本地 harness 推到远程异步执行。
- PR review bot：把 harness 放进真实代码审查链路。
- automations：定时运行 eval、整理 issue、扫描失败。
- GUI / browser / computer use：作为可选工具层，而不是第一阶段核心。

## 为什么值得做

这个方向和当前职业主线高度一致。

`context-core` 证明你理解 context lifecycle、routing、bundle、trace、eval 和 writeback。`oh-share-it` 证明这套 context layer 可以进入多人协作和真实部署。`my-little-agent-loop` 如果做成 Codex-like harness，则补上第三块关键证据：你能控制 agent runtime 本身。

这比单纯做一个聊天机器人或 RAG demo 强很多。它展示的是：

- 能把模型能力放进受控 runtime。
- 能区分 latent 判断和 deterministic 工具执行。
- 能让 agent 行为可追踪、可回放、可评测。
- 能把上下文基础设施接入真实 agent loop，而不是停留在静态知识库。

对 `Agent Systems Engineer` 叙事来说，这是一条很硬的信号。

## 设计原则

### 1. 先做可观察内核，不做大而全产品

第一阶段不追求覆盖 Codex 的桌面端、云端、IDE、GitHub、自动化和视觉能力。先把最小闭环做实：

```
task -> context bundle -> tool calls -> patch/result -> trace -> replay -> eval
```

这条链路跑通，才有资格继续扩展。

### 2. Thin harness, fat skills

内核保持薄，只做事件循环、工具协议、权限、状态、trace 和 replay。

复杂判断尽量放到 skills、项目规则、eval rubric 和 `context-core` 的路由策略里。这样模型升级时，latent 判断会自然受益，而 deterministic 执行层仍然稳定。

### 3. Context native

这个 harness 不应把 context 当成 prompt 附件，而应把 `context-core` 当作一等公民：

- 每次任务都显式生成 `ContextBundle`。
- 每次 route 都记录 `RouteDecision`。
- 每次回答都能追溯 source。
- 每次失败都能回写成 `EvalCase` 或 `WritebackCandidate`。

这样 `my-little-agent-loop` 才会和 `context-core` 互相增强，而不是变成另一个孤立 agent 项目。

### 4. Eval-first

每个功能都要能落到一个可回放任务上。

优先做 5 到 10 个固定 regression tasks，而不是堆新功能。任务可以来自：

- `oh-share-it` 的真实查询。
- `context-core` 的路由失败。
- 小型代码修改任务。
- 文档整理或知识库写回任务。

### 5. 权限边界先于自动化

如果要让 agent 真正改文件、跑命令、部署服务，permission model 必须前置。

最小权限层可以先分成：

- `read-only`
- `edit-with-approval`
- `command-with-approval`
- `trusted-local`

这不是为了形式安全，而是为了让 harness 的行为能被解释、能被复盘。

## 分阶段路线

### V0：可追踪本地 agent loop

目标：先做一个透明、可保存、可复盘的本地 loop。

最小交付：

- message log
- tool call log
- file read / search tool
- patch apply tool
- command runner
- permission gate
- JSONL trace
- README 解释架构边界

过线标准：能完成 3 到 5 个小型代码或知识库任务，并留下完整 trace。

### V1：和 context-core 对齐

目标：让 harness 成为 context infra 的运行面。

最小交付：

- 接入 `ContextBundle`
- trace 中记录 `RouteDecision`
- replay runner 支持固定 `EvalCase`
- evaluator 生成人工评分入口或 score stub
- 5 到 10 个 regression cases

过线标准：能用 `context-core` 输出的上下文执行任务，并知道失败来自 retrieval、routing、context packaging、tool execution 还是 model judgment。

### V2：Codex-like 开发者体验

目标：把它从脚本变成可用的 coding agent harness。

可选交付：

- resume / fork session
- plan / todo state
- patch preview
- skill loader
- subagent isolation
- worktree support
- compact / summary policy

过线标准：可以连续处理一个 1 到 2 小时的真实开发任务，过程中上下文、修改、命令和判断都有记录。

### V3：产品化与外部信号

目标：把它变成简历和公开展示能看懂的系统。

可选交付：

- GitHub PR review bot
- scheduled eval automation
- remote task runner
- small web trace viewer
- integration with `oh-share-it`
- case study

过线标准：外部读者能在 10 分钟内明白它和普通 agent demo 的差异：它不是“会聊天”，而是一个可评测、可恢复、可审计的 agent runtime。

## 本月最小切法

本月不建议直接冲完整 Codex-like 产品。最合理的切法是：

1. `my-little-agent-loop` 只做 `trace + replay + evaluator loop`。
2. trace schema 对齐 `context-core` 的 `Trace` / `EvalCase`。
3. replay cases 来自 `oh-share-it` 和 `context-core`。
4. README 用 Codex-like harness 叙事包装，但不承诺桌面端、云端、IDE 这类大产品能力。

本月可以写进简历的表达是：

> Built a minimal Codex-like agent harness for traceable tool use, resumable task execution, patch-based editing, and eval-driven replay, powering an eval-first context infrastructure stack.

## 不该做什么

- 不要第一阶段就做完整 UI。
- 不要把所有 Codex 功能都做成路线承诺。
- 不要脱离 `context-core` 和 `oh-share-it` 单独做一个玩具 agent。
- 不要用复杂 agent orchestration 掩盖没有 eval 的事实。
- 不要把 permission、trace、replay 当成后期再补的附属功能。

## 和其他项目的关系

| 项目 | 关系 |
|---|---|
| `context-core` | 提供 context routing、bundle、trace、eval schema，是 harness 的上下文基础设施 |
| `oh-share-it` | 提供真实任务、真实用户问题、部署和协作场景 |
| `my-little-agent-loop` | 提供 Codex-like agent runtime，把 context 和 tool execution 接成可回放闭环 |
| `gogo` | 保留为既有 workbench / demo，不承担本路线主要开发 |
| `clawhouse` | 未来可接入 remote / multi-device session，但不是本月主线 |

## 简历叙事

可以收束成三层：

1. Context layer：`context-core` 负责知识来源、路由、上下文包、trace 和 writeback。
2. Deployment layer：`oh-share-it` 把 context layer 放进课题组共享知识场景。
3. Runtime layer：`my-little-agent-loop` 提供 Codex-like harness，让 agent 行为可追踪、可恢复、可评测。

一句话版本：

> Built an eval-first agent context infrastructure stack: `context-core` for context routing and writeback, `oh-share-it` for real-world shared deployment, and `my-little-agent-loop` as a minimal Codex-like harness for traceable, replayable agent execution.

## 相关页面

- [Agent harness core 与三种 adapter 路线](Agent-harness-core与三种adapter路线.md)
- [Agent 系统月度执行计划（2026-05-24）](Agent系统月度执行计划-2026-05-24.md)
- [Agent 系统求职与项目路线图（2026-05）](Agent系统求职与项目路线图-2026-05.md)
- [Agent Systems Engineer 职业定位](../career-positioning-job-search/Agent%20Systems%20Engineer职业定位.md)
- [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md)
- [Claude Code、Codex 与 pi 的 harness 对比](../agent-harness-runtime/coding-agent-harness-comparison.md)
- [Thin Harness, Fat Skills](../agent-harness-runtime/thin-harness-fat-skills.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)

## 来源依据

- 本次对话中关于 Codex 功能清单的整理。
- 本地 `codex --help` 显示的 CLI 命令面。
- 本知识库已有 harness、context infra、职业叙事和月度计划页面。
