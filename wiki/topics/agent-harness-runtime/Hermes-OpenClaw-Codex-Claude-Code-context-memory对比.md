# Hermes、OpenClaw、Codex、Claude Code 的 memory 与 context 管理对比

## 摘要

这四个系统都在处理同一个底层问题：模型上下文窗口有限，而 agent 工作又需要跨轮次、跨文件、跨工具、跨设备保留状态。差异不在于“谁有 memory”，而在于它们把 memory 和 context 放在哪一层。

一个粗略判断是：

- `Hermes` 更像显式 `Context Engine`：每轮动态组装 prompt，管理压缩、memory、skills、session search 和 prompt caching。
- `OpenClaw` 更像持续 assistant runtime：用 Gateway、agent workspace、session store、`SOUL.md`、`AGENTS.md`、heartbeat 和 nodes 承接人格连续性与多入口状态。
- `Codex` 更像较克制的 coding harness：以 session、工具调用、patch、权限、trace/replay 和项目上下文文件为核心，长期记忆主要依赖外部文件和工作区资产。
- `Claude Code` 更像厚产品化 harness：把 `CLAUDE.md`、auto memory、session persistence、compaction、checkpoints、permissions、subagents、MCP、skills 和 hooks 都纳入默认工作面。

本文对 `Hermes` 的 context engine 判断仍主要来自 raw conversation；但 skill 的存储、查看与审批边界已经用官方文档补充核对。对 `Codex` 的判断仍偏中等，因为本地材料更多来自对照和路线图，而不是完整官方实现说明。

## 对比表

| 系统 | 主要 context 抽象 | memory 放在哪里 | 长上下文策略 | 关键取舍 |
|---|---|---|---|---|
| `Hermes` | `Context Engine` | 长期 memory、skills、session search、compression summary | token 压力监控后压缩旧历史，稳定 prompt 前缀配合 prompt caching | 上下文调度意识最显式，但本地证据主要来自 raw |
| `OpenClaw` | assistant + Gateway + agent workspace | `SOUL.md` / prompt files、agentDir、workspace、session store、heartbeat checklist | 通过 Gateway 维持多入口 session 和状态，靠文件承接身份与行为边界 | 强调“同一个 assistant”持续存在，但实现仍 gateway-centric |
| `Codex` | terminal-first coding harness / Codex-like session | 项目文件、`AGENTS.md`、session、trace、patch、eval case | 通过 session、compact / resume、工具日志和文件化任务状态管理 | 壳较克制，可观察性和可审计执行更重要 |
| `Claude Code` | 厚 agentic coding harness | `CLAUDE.md`、auto memory、session JSONL、skills、MCP、subagents、hooks | 自动 compaction，先清工具输出，再总结对话；subagents 隔离上下文 | 开箱强，控制机制内建多，但黑箱感更高 |

## Hermes

本地 raw 中对 Hermes 的描述非常接近通用 `Context Engine` 定义。它每轮模型调用前会组装系统提示词、当前会话、工具 schema、已加载 skills、长期 memory、session search 结果和工具结果。

它的核心不是保存所有历史，而是在有限窗口内决定当前最该让模型知道什么。长对话接近阈值时，Hermes 会压缩旧历史，保留目标、约束、决策、待办、工具结果、错误路径和当前状态。

Hermes 还强调插件化：`context_engine.py` / `context_compressor.py` 这类接口可以接管 `on_session_start`、`update_from_response`、`should_compress`、`compress`、`on_session_reset`、`on_session_end` 等生命周期点。它同时会考虑 prompt caching，因此倾向让系统提示词、工具定义和稳定上下文少变，把动态内容放在后面。

所以 Hermes 的特点是：把 context 管理直接做成一个可替换的调度器，而不是把 memory 当成一个附属数据库。

需要补充一个容易被产品表面遮住的事实：Hermes 生成的 skill 并非不可查看。官方文档把 `~/.hermes/skills/` 定义为 agent-created skills 的 source of truth，并提供 `skills_list()` 与 `skill_view()` 查看完整内容。若开启 `skills.write_approval`，agent 对 skill 的 create、edit、patch、delete 会先进入 `~/.hermes/pending/skills/`，用户可以查看 diff 后批准或拒绝。

因此 Hermes 当前更准确的问题不是“没有可见性”，而是这些能力主要分布在文件、CLI、命令和审批机制中。技术上可以检查，不等于普通用户会在主交互里自然意识到 Agent 学会了什么、为何学到、何时开始生效。

## OpenClaw

OpenClaw 的主语不是 coding session，而是 personal assistant。它的 context / memory 主要由几个层共同承接。

第一层是 Gateway。Gateway 是 long-lived、always-on 的本地中枢，负责 channels、sessions、tools、events、WebSocket API、nodes 和 control UI。多入口访问不靠每个聊天窗口自己记忆，而是回到同一个 Gateway。

第二层是 agent workspace。公开 docs 把一个 agent 定义成 workspace、`agentDir`、session store 和 per-agent auth profiles 的组合。这意味着 OpenClaw 的 agent 不是单次聊天实例，而是带隔离状态的 workspace。

第三层是 prompt files，尤其是 `SOUL.md`、`AGENTS.md`、`TOOLS.md`。`SOUL.md` 被放在人格、声音和 continuity 的核心位置。公开 notes 里保留的关键意思是：每次会话虽然是 fresh，但这些文件是它的 memory，agent 应阅读并更新它们。

第四层是 heartbeat 和 `HEARTBEAT.md`。这让 assistant 不只是被动响应，还能周期性维护 checklist 或执行例行 upkeep。

所以 OpenClaw 管 context 的方式不是“一个检索器”，而是把身份、workspace、session、prompt files、heartbeat 和设备 nodes 拼成持续 assistant 的状态系统。它的张力是：产品叙事说 assistant 是本体，但实现里 Gateway 仍然是最强中心。

OpenClaw 的实验性 Skill Workshop 已经进一步处理“从工作过程里学习”的治理问题：`/learn` 可以把当前对话或指定来源蒸馏成 skill proposal，但 proposal 与 active `SKILL.md` 分开，只有 inspect、apply 后才会成为生效的 workspace skill。它还保存目标、证据、hash、scanner state 与 rollback metadata。这个设计说明，从轨迹提取 skill 的关键交互对象不应只是最终文件，而应是“候选变更 + 证据 + 激活决策”。

## Codex

本地材料对 Codex 的直接证据比 Claude Code 少，所以这里要保守。

可以确认的是，Codex 更接近 terminal-first coding agent harness。它关心的 context 不是人格连续性，而是一次开发任务能否在真实代码库里可恢复、可审计、可验证地推进。

从本地 `Codex-like agent harness` 路线图看，Codex-like 的最小 context / memory 面包括：

- `Session`：会话、状态、工作目录、resume、fork、compact。
- `Tool Runtime`：文件读取、搜索、patch 编辑、命令执行、外部工具调用。
- `Permission / Sandbox`：读、写、执行、网络、危险命令的权限边界。
- `Plan / Todo`：把长任务拆成可观察状态。
- `Diff / Patch`：所有修改可审计。
- `Trace / Replay`：记录输入、工具调用、上下文、输出和失败标签。
- `Skill System`：把可复用流程和项目规则外置成文件。

这说明 Codex 的 memory 更像“任务状态 + 工作区文件 + 轨迹日志 + 项目规则”，而不是人格化长期 memory。它把可复用上下文更多放进 `AGENTS.md`、repo docs、skills、trace、eval cases 和项目文件，而不是把全部策略内建在聊天历史里。

## Claude Code

Claude Code 的本地资料最完整。它是更厚的 agentic coding harness。

官方材料已经明确它的默认上下文包括当前项目和 git state、`CLAUDE.md`、auto memory、MCP、skills、subagents、Chrome extension 等。session 保存在本地 JSONL 中，支持 resume 和 fork。context window 会自动 compaction：先清理工具输出，必要时再总结对话。subagents 通过独立上下文减轻主上下文膨胀。

它还把 permissions、checkpoints、plan mode、MCP、hooks、skills、subagents 都做成正式控制面。Dynamic Workflows 又进一步把 subagents 推成临时 agent team：动态拆任务、并行 fan out、独立验证、adversarial checking、保存进度并恢复长任务。

所以 Claude Code 的 memory / context 策略是产品化最强的一类：把很多原本需要用户用文件、脚本、tmux、外部流程自己拼的上下文控制机制，直接做进默认 harness。

它的代价也清楚：系统更厚，用户更难完全知道每轮到底注入了什么、压缩了什么、哪些子流程已经发生。

## 核心差异

如果按“context 被放在哪里”来分：

- Hermes：放在可插拔 context engine 生命周期里。
- OpenClaw：放在持续 assistant 的 Gateway / workspace / prompt files / heartbeat 里。
- Codex：放在 coding harness 的 session / trace / patch / repo files / project rules 里。
- Claude Code：放在厚产品化 harness 的内建 memory、compaction、session、permissions、subagents 和扩展面里。

如果按“长期记忆的形态”来分：

- Hermes 更像 memory + session search + compression summary。
- OpenClaw 更像人格文件 + workspace/session store。
- Codex 更像任务轨迹 + 项目文件 + 可复用规则。
- Claude Code 更像 auto memory + `CLAUDE.md` + session JSONL + subagent isolation。

真正的判断点不是谁记得更多，而是谁能把正确上下文在正确时间送进当前任务，并且让写入、压缩、权限、回放和纠错可控。

对于自动学习，还应再加一条：是否能区分 `candidate skill` 与 `active skill`，并让“从哪段轨迹抽出了什么规则、将影响哪些任务、如何撤销”在主交互中可理解。文件可访问只是底线，不是完整的可见性。

## 来源依据

- [Context Engine：上下文编排层](../context-memory-knowledge-system/context-engine.md)
- [Claude Code：较厚的 agentic coding harness](claude-code-harness.md)
- [Claude Code、Codex 与 pi 的 harness 对比](coding-agent-harness-comparison.md)
- [openclaw/openclaw 仓库地图](openclaw-openclaw-repo-map.md)
- [Agent Context Infra 前沿调研（2026-05-25）](../context-memory-knowledge-system/agent-context-infra-2026-05-25.md)
- [Codex-like agent harness 路线图](../projects-roadmaps/Codex-like-agent-harness路线图.md)
- [Hermes context engine raw conversation](../../../raw/personal/conversations/context-engine-ai-infra-2026-06-17.md)
- [Hermes Skills System](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md)
- [Hermes Configuration：skill write approval](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/configuration.md)
- [OpenClaw Skill Workshop](https://docs.openclaw.ai/tools/skill-workshop)
