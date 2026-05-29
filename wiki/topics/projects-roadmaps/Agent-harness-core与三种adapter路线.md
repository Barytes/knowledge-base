# Agent harness core 与三种 adapter 路线

## 摘要

这页记录一个从 “复刻 Codex” 往外扩展的判断：真正值得做的不是三个彼此独立的 agent harness，而是一个可复用的 `agent-harness-core`，再接三个不同方向的 demo / adapter。

核心结构是：

```text
agent-harness-core
  -> context-eval-adapter
  -> clawhouse-continuity-adapter
  -> companion-desktop-adapter
```

这样既保留 Codex-like harness 的工程硬度，又让项目有自己的独特方向：

- 为 `context-core` / `oh-share-it` 服务的 context infra 测评与改进。
- 为 `clawhouse` 服务的多端同步与任务接续。
- 为个人工作流服务的实时 companion agent。

压缩判断：

> `agent-harness-core` 负责可追踪、可恢复、可评测的 agent runtime；三个 adapter 分别证明它能支撑 context quality、task continuity 和 ambient collaboration。

## 为什么不是三个完全独立的 harness

三个想法看起来不同，但底层需要的机制高度重合：

- session / task state
- tool runtime
- permission / sandbox
- trace / event log
- replay
- evaluator
- patch / action record
- context bridge
- human approval
- failure labeling

如果拆成三个独立项目，很容易重复造底层轮子，最后每个 demo 都只有薄薄一层。更合理的切法是先把共性能力收束到 `agent-harness-core`，再用 adapter 展示不同应用面。

这也更符合 infra 项目的叙事。外部读者看到的不是“做了三个小 agent”，而是“做了一个 harness substrate，并用三个场景证明它的泛化能力”。

## agent-harness-core

`agent-harness-core` 是底座。它不绑定某个具体产品入口，也不直接承诺桌面端、移动端或云端体验。

它应该负责：

| 模块 | 职责 |
|---|---|
| `Session` | 记录 task、message、state、resume、fork、compact |
| `ToolRuntime` | 注册工具、调用工具、记录结果、处理错误 |
| `Permission` | 管理读、写、命令、网络、危险操作的授权 |
| `Trace` | 记录事件流、上下文、工具调用、决策点、最终结果 |
| `Replay` | 基于 trace 或 eval case 重跑任务 |
| `Eval` | 定义 evaluator interface、score record、failure label |
| `Patch` | 让文件修改以 diff / patch 形式进入系统 |
| `ContextBridge` | 对接 `context-core` 的 `ContextBundle`、`RouteDecision`、`EvalCase` |

它的设计原则是 thin core。核心只做运行时和可观察性，不把业务判断写死。具体判断交给 adapter、skills、eval rubric 和 context policy。

## Adapter 1：context-eval-adapter

这个 adapter 服务 `context-core` 与 `oh-share-it`。

核心问题：

> agent 任务失败时，失败到底来自 context 没取到、取错了、打包差、工具执行差，还是模型判断差？

它应该把每次运行显式拆成：

```text
query
  -> RouteDecision
  -> ContextBundle
  -> agent action
  -> answer / patch / writeback
  -> Trace
  -> EvalRecord
  -> FailureLabel
```

最小能力：

- 接入 `context-core` 生成的 `ContextBundle`。
- 记录 route、source、bundle、tool call、answer。
- 对齐 `oh-share-it` 的真实问题集。
- 生成 failure taxonomy：
  - retrieval miss
  - routing mismatch
  - context overload
  - stale context
  - tool failure
  - model judgment failure
  - writeback failure
- 支持 5 到 10 个 replay / regression cases。

这个方向最适合作为第一阶段的 flagship demo，因为它直接支撑当前月度主线。

## Adapter 2：clawhouse-continuity-adapter

这个 adapter 服务 `clawhouse`。

核心问题：

> 一个 agent task 能否从一台设备迁移到另一台设备继续，而不是只同步一段聊天记录？

它关心的是动态上下文：

- 当前 task 是什么。
- agent 做到哪一步。
- 读过哪些文件。
- 改过哪些文件。
- 有哪些 pending approval。
- 当前 plan / todo 是什么。
- 哪些上下文已经被压缩成 working state。
- 哪些 session 可以 resume 或 fork。

最小能力：

- 把 `Session` 和 `Trace` 序列化成可同步对象。
- 区分静态上下文和动态上下文。
- 支持只读恢复：先能在另一台设备理解当前任务状态。
- 支持最小继续：输入下一条指令后，能接着原 session 生成事件。
- 记录设备、工作目录、git state、agent identity。

这个方向的独特性不是“远程桌面”，而是把 agent 工作状态做成可迁移的对象。

## Adapter 3：companion-desktop-adapter

这个 adapter 服务实时 companion agent。

核心问题：

> agent 能否从一问一答的聊天框，变成一个低打扰、持续伴随、能在关键节点接手的工作伙伴？

它不应该一开始就做成强自动化助手。更合理的第一版是 passive / low-interrupt companion：

- 观察当前任务状态。
- 识别用户可能卡在哪里。
- 在合适时机提出下一步建议。
- 发现风险时提醒。
- 用户授权后执行小任务。
- 把重要发现写回 trace 或 context。

最小能力：

- 读取当前项目状态或前台工作面摘要。
- 维护一个 lightweight working state。
- 生成 low-interrupt suggestion。
- 支持用户 approve / dismiss。
- 记录建议是否有用，进入 eval。

这个方向最有产品想象力，但也最容易膨胀。第一阶段应避免做完整 GUI、全局键盘监听、复杂屏幕理解和强自动执行。它的重点是证明 interaction model，而不是马上做全功能个人助手。

## 三者关系

| 方向 | 主要服务 | 证明什么能力 |
|---|---|---|
| `context-eval-adapter` | `context-core` / `oh-share-it` | context infra 可以被评测、debug、改进 |
| `clawhouse-continuity-adapter` | `clawhouse` | agent task state 可以跨设备迁移和接续 |
| `companion-desktop-adapter` | 个人实时工作流 | agent 可以从 chat 变成低打扰持续协作 |

三者共同指向一个更大的命题：

> 下一代 agent harness 不只是 chat loop，而是围绕 context quality、task continuity 和 ambient collaboration 组织长期工作。

## 推荐推进顺序

第一阶段不应三个 adapter 同时重投入。更稳的顺序是：

1. 先做 `agent-harness-core` 的最小 trace / replay / eval / permission / context bridge。
2. 把 `context-eval-adapter` 做成可跑 demo，直接服务 `context-core` 和 `oh-share-it`。
3. 给 `clawhouse-continuity-adapter` 写设计稿和最小 session sync 原型。
4. 给 `companion-desktop-adapter` 做交互概念和一个 passive suggestion 原型。

也就是说：

- `context-eval-adapter`：本月主力。
- `clawhouse-continuity-adapter`：第二优先级，先验证同步对象模型。
- `companion-desktop-adapter`：保留想象力，先做轻量概念，不抢主线。

## 和 Codex-like 路线的关系

Codex-like 仍然是底层能力参照：

- session
- tool use
- patch
- permission
- trace
- replay
- eval
- skills

但新的路线不止是复刻 Codex。它把 Codex-like 能力重新放进三个更具体的问题里：

- context infra 如何被测评和改进；
- agent 任务如何跨设备连续；
- agent 如何实时伴随用户工作。

因此这条路线可以叫：

> context-native continuity harness

或者更工程化地叫：

> `agent-harness-core` with context-eval, continuity, and companion adapters.

## 简历叙事

可以写成：

> Built an extensible agent harness core with reusable session, tool runtime, permission, trace, replay, and eval primitives, then implemented three adapters for context-infra evaluation, cross-device task continuity, and low-interrupt companion workflows.

中文压缩版：

> 做了一个可扩展的 agent harness core，并用三个 adapter 分别验证 context infra 测评、多端任务接续和实时 companion 协作。

## 相关页面

- [Codex-like agent harness 路线图](Codex-like-agent-harness路线图.md)
- [Agent 系统月度执行计划（2026-05-24）](Agent系统月度执行计划-2026-05-24.md)
- [Clawhouse：多设备 Agent 上下文同步](../agent-harness-runtime/clawhouse-多设备-agent-工作台.md)
- [oh-share-it 公共知识库产品](../research-knowledge-governance/oh-share-it公共知识库产品.md)
- [Context-Core 技术前沿调研报告（2026-05-25）](../context-memory-knowledge-system/context-core-technical-frontier-2026-05-25.md)
- [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md)
