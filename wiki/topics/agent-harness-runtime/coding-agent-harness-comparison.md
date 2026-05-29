# Claude Code、Codex 与 pi 的 harness 对比

## 摘要

从当前本地材料看，`pi`、Claude Code、Codex 都属于 terminal-first 的 coding agent harness。它们共享的基本形状是：给模型一组文件与命令工具、把会话组织成线性消息流、允许读取项目级上下文文件，并围绕长任务构造某种状态保持与交互壳。

但三者的真正分歧不在“是不是 coding agent”，而在 harness 该有多厚。

- `pi` 倾向把核心压到最薄：少量 prompt、极少默认工具、强可观察性、把复杂能力外置到文件、CLI、`tmux` 与 extension system。
- Claude Code 在当前本地材料中的形象更像“更厚的内建 orchestration”：更重的 system prompt、更多内建模式、更多隐藏的辅助流程。
- Codex 在当前本地材料里看起来处于中间位置：同样是 terminal chat harness，但工具面和 UI 路径更接近极简壳，而不像 Claude Code 那样把很多策略直接烤进核心工作流。

需要注意：这页对 `pi` 的判断主要来自本地一手资料；Claude Code 部分现在已经有官方 `How Claude Code works` 作为较强依据，因此相关判断比之前更稳；Codex 部分在当前仓库里仍主要来自侧面对照，因此仍应视为中等置信度画像，而不是完整官方定稿。

## `pi-coding-agent` 是如何实现的

按本地仓库地图与说明，`pi` 不是一个孤立 CLI，而是一套分层实现：

- `pi-ai`：统一多 provider 的 LLM API，负责流式输出、tool calling、reasoning、跨 provider context handoff、token / cost 统计。
- `pi-agent-core`：把模型调用和 tool loop 包成 agent runtime，处理状态、消息队列、附件与 transport。
- `pi-tui`：终端 UI 层，采用保留 scrollback 的 retained-mode + differential rendering 方案，而不是 fullscreen TUI。
- `pi-coding-agent`：最终用户面对的 CLI，负责 session、命令、context files、自定义资源、SDK / RPC 暴露等。

也就是说，它的实现不是“一个 prompt 加四个工具”，而是：

1. 先把 provider 抽象和事件流做成基础设施。
2. 再把 agent loop 做成可复用 runtime。
3. 再把 TUI、session 与 customization 编排成产品层。

这种切法的好处是，`pi` 既能作为 CLI 使用，也能暴露为 SDK 与 RPC runtime，而不必把 UI 和 agent loop 写死在一起。

## `pi` 的结构长什么样

如果只看 `packages/coding-agent` 这一层，它的结构重点不在“功能列表”，而在四个可组合面：

### 1. 会话与上下文面

- session 按工作目录自动保存，底层是带 `id` / `parentId` 的 JSONL tree。
- 支持继续、恢复、fork、tree 导航与 compaction。
- 启动时层级加载 `AGENTS.md` / `CLAUDE.md`，并允许用 `SYSTEM.md` / `APPEND_SYSTEM.md` 覆盖或追加系统提示。

这说明 `pi` 把“长期工作上下文”建模成文件系统和会话树，而不是只靠当下 prompt。

### 2. 极简 agent 面

- 默认 system prompt 很短。
- 默认工具只有 `read`、`write`、`edit`、`bash`。
- 若要限制能力，可退化成只读工具；若要增强能力，则交给扩展系统。

这里的核心判断是：现代模型已经懂得基本 coding workflow，harness 不必把太多执行策略提前固化。

### 3. 终端交互面

- `pi-tui` 走的是“保留终端 scrollback”的路径。
- 用 synchronized output 和 differential rendering 减少闪烁。
- 编辑器、消息流、工具输出和设置 UI 都是围绕原生终端能力搭起来的。

这意味着它优先保留终端自带的滚动、搜索和线性阅读体验，而不是追求更强的全屏 UI 表达。

### 4. 扩展与再编排面

- Prompt templates
- Skills
- Extensions
- Themes
- Pi packages
- SDK
- RPC mode

这层很关键。`pi` 不是没有复杂能力，而是把它们移出核心，做成“你可以自己装、自己写、自己换”的二级层。

## 三者的共同点

基于当前本地材料，`pi`、Claude Code、Codex 至少共享这些形状：

- 都把 coding task 组织成“用户消息 -> tool 调用 -> assistant 回复”的线性会话。
- 都默认运行在 terminal-first 的工作面上，而不是纯 IDE 补全。
- 都依赖项目级上下文文件或类似机制，把 repo-specific 规则注入到会话里。
- 都把文件读写、命令执行之类的能力视为核心工具面。
- 都在处理同一个基本问题：如何让模型在真实代码库里维持上下文、找对文件、执行修改并汇报结果。

所以它们首先不是三种不同物种，而是同一类 harness 在“补偿面”上做出的不同取舍。

## 三者最重要的不同

### 1. 对“核心壳厚度”的判断不同

`pi` 的默认立场是：核心壳应尽量薄，很多能力不应该 baked in。

Claude Code 在当前本地材料里的对照位置则更厚：

- 更长的 system prompt
- 更多内建功能模式
- 更多权限与流程编排
- 更多由 harness 代替用户决定的工作方式

Codex 在本地材料里露出的信号较少，但 `pi` 作者明确把 Codex 的工具定义视为与 `pi` 相近的极简面。这暗示 Codex 至少在“默认工具协议”上，没有走 Claude Code 那种很厚的工具与流程层。

### 2. 对“可观察性”的优先级不同

`pi` 把 observability 放得很高。它反对：

- 隐藏的上下文注入
- 黑箱 sub-agent
- 不可查询的后台 bash
- 只给结果、不暴露过程的 plan flow

Claude Code 在本地材料中的主要批评点，几乎全部围绕可观察性不足：

- plan mode 背后常有不可见的子流程
- 背景 bash 的状态不够透明
- sub-agent 是“黑箱中的黑箱”
- system prompt 与 tools 会随版本变化，用户不容易稳定控制

Codex 在本地材料中没有被这样集中批评。保守地说，本地证据至少说明它和 `pi` 一样，都更接近“线性终端会话 + 极简工具面”的方向。

### 3. 对“复杂能力该内建还是外置”的判断不同

`pi` 明确把很多常见能力外置：

- plan mode -> `PLAN.md`
- to-dos -> `TODO.md`
- background bash -> `tmux`
- MCP -> CLI + README
- sub-agents -> 用 `bash` 再起一个 `pi`，或扩展实现
- permission gates -> extension 自己做

Claude Code 在本地材料里的相反特点，是它把更多这些能力做成了内建产品功能。

Codex 的本地证据则更偏中间：至少工具面不厚，但本地材料还不够支撑更细的结论。

## 各自独特的设计取舍

### `pi`

独特点：

- 用最小 system prompt 和四工具默认面来押注模型先验能力。
- 用 `pi-ai` 把多 provider、cross-provider handoff、tool result split、partial JSON parsing 这些底层抽象做出来。
- 用 extension / package system 把“更厚的 harness”变成可选层，而不是默认层。

代价：

- 用户必须更主动地管理工作流。
- 默认安全栏杆更弱，`YOLO` 权限模型风险更高。
- 很多“开箱即用”的便利性需要用户自己组装。

### Claude Code

按当前本地材料，独特点主要体现在“更强的产品化 orchestration”：

- 更厚的 prompt 与 tool layer
- 内建 plan mode、background bash、sub-agent 等高级能力
- 更强的权限与运行控制逻辑
- 把 session persistence、memory、context compaction、checkpoints 做成核心系统能力

代价也很明确：

- 用户更难完全知道系统到底注入了什么、看了什么、为什么这样做
- 工作流更依赖官方默认路径
- 版本变化更容易改变 agent 行为

### Codex

当前本地材料里，Codex 最明显的信号有两条：

- 终端交互路径上，它和 Claude Code、`pi` 同属“线性消息流 + 非 fullscreen TUI”的一类。
- 工具定义上，它更接近 `pi` 的极简面，而不是厚重工具层。

因此一个保守判断是：Codex 的独特取舍可能在于，把核心 agent loop 和工具协议做得相对克制，然后把更多复杂性放到其他层，而不是像 Claude Code 那样在默认 harness 里直接展开很多产品机制。

但这部分在当前本地仓库里证据不足，不能进一步说得太满。

## 如果把三者放在同一张图里

可以把它们粗略放在一条轴上：

- 更厚、更强内建 orchestration：Claude Code
- 更薄、更强可观察性与可改造性：`pi`
- 在终端形态与极简工具面上更接近 `pi`，但本地证据还不足以完整画像：Codex

另一条轴则是“内建能力”与“可编排能力”的分配：

- Claude Code：更多能力直接做成产品默认面
- `pi`：默认核心极薄，把能力外移到文件、CLI、`tmux`、extensions、packages
- Codex：从当前本地材料看，至少在工具面上没有走非常厚的默认层

## 一个更抽象的结论

如果用 [Harness Engineering（约束壳工程）](harness-engineering.md) 的语言来看，三者都在给模型加补偿层，但它们对“哪些补偿必须内建”有不同判断。

- Claude Code 更像是把较多补偿直接做进产品。
- `pi` 更像是认为很多补偿应该由用户按需拼装，默认只保留最小壳。
- Codex 在当前本地材料里更像是保留较克制的默认壳，但没有像 `pi` 那样把“反内建哲学”明确写成一整套产品主张。

所以真正的差异，不只是 feature checklist，而是对 “harness 的职责边界” 的不同回答。

## 相关页面

- [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md)
- [AI 系统产品判断框架](../../frameworks/AI系统产品判断框架.md)

## 来源依据

- [Claude Code：较厚的 agentic coding harness](claude-code-harness.md)
- [Pi coding agent：一种极简且可观察的 coding harness](pi-coding-agent-harness.md)
- [badlogic/pi-mono 仓库地图](badlogic-pi-mono-repo-map.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
- [pi-mono/packages/coding-agent README](../../../raw/external/pi-mono-coding-agent-readme.md)
- [What I learned building an opinionated and minimal coding agent](../../../raw/external/pi-coding-agent-retrospective.md)
- [GitHub repo snapshot: badlogic/pi-mono](../../../raw/external/github-repo-badlogic-pi-mono.md)
- [How Claude Code works](../../../raw/external/claude-code-how-it-works.md)
- [Claude Code: An analysis](../../../raw/external/claude-code-analysis-southbridge.md)

## 相关页面

- [Claude Code：较厚的 agentic coding harness](claude-code-harness.md)
- [Pi coding agent：一种极简且可观察的 coding harness](pi-coding-agent-harness.md)
- [badlogic/pi-mono 仓库地图](badlogic-pi-mono-repo-map.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
