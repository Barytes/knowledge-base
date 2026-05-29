# LuliYanng/Nono-Cowork 仓库地图

## 摘要

这页是 `LuliYanng/Nono-Cowork` 的第一版仓库地图，观察主题是“仓库架构与工程实践”。

`Nono-Cowork` 把自己定位成运行在 VPS 上的 proactive AI coworker：它不只是等用户发 prompt，而是监听邮件、文件同步、定时任务和应用事件，在远端执行工作，再把结果同步回用户本地工作区。它的核心产品判断是“agent 常驻云端，但交付物回到本地文件系统和桌面通知里”。

当前置信度是中等：README、目录树、manifest、关键控制层文件和桌面 API 摘要已经读过，足以建立机制地图；但还没有完整读透所有工具实现、前端状态流和 Composio 细节，因此不应把它提升成完整代码审计结论。

## 仓库目的

- 公开定位：一个 self-hosted AI agent，运行在 VPS 上，通过 Telegram / Feishu / Terminal / Desktop 控制，并通过 Syncthing 把文件结果送回本地工作区。
- 实际架构定位：一个多通道 agent runtime，加上三类自动化入口：Composio trigger、Syncthing file-drop、cron scheduler。
- 阶段声明：README 明确标注 Early Beta，并提示不推荐在 unrestricted shell access 或企业部署场景中直接生产使用。
- 观察分支：`main`
- 解析到的 commit：`c8c4746499033bf81c22cd07c8ad52aabcf97b86`
- 主要语言：`Python`
- 仓库地址：https://github.com/LuliYanng/Nono-Cowork

## 架构地图

### 顶层目录

- `src/`: Python 后端与 agent runtime，包含 agent loop、工具、通道、自动化、Syncthing 集成、通知与持久化。
- `desktop/`: Electron + Vite + React 桌面端，用 FastAPI/SSE 与 VPS 后端交互，并管理 Syncthing 本地侧。
- `docs/`: Desktop、Syncthing、Telegram、Feishu、Composio 等安装说明。
- `developdocs/`: 设计说明，目前关键文件是 `tool-access-control.md`。
- `skills/`: 随仓库分发的 agent skills，包含 `skill-creator` 与 `skill-finder`。

### 后端执行流

`src/main.py` 是统一入口。启动时会恢复日志、注册 session 关闭回调，启动 scheduler、Composio trigger listener、Syncthing watcher、file-drop listener，然后按 `CHANNELS` 环境变量注册 `desktop`、`feishu`、`telegram` 等通道。

普通用户消息会进入 `src/channels/base.py` 或 `src/channels/desktop.py`，再统一走 `src/core/agent_runner.py`。`agent_runner` 负责 per-user lock、session 读取、workspace/sync context 注入、事件回调转发，最后调用 `src/core/agent.py` 的 `agent_loop`。

自动化任务不复用普通对话上下文。`src/automations/composio_triggers.py`、`src/automations/file_drop.py`、`src/automations/scheduler/executor.py` 都倾向创建一次性或独立 agent session，执行后把结果写入 `src/delivery/notifications.py` 的通知层。

### 桌面端表面

`desktop/package.json` 显示桌面端是 Electron + Vite + React 应用，支持 `electron:dev`、`build`、`package`、`lint` 等脚本。`desktop/src/App.tsx` 是大入口，桌面端通过 preload 暴露文件打开、本地 Syncthing 查询、folder 管理、应用配置等能力。

VPS 侧的 `src/channels/desktop.py` 提供 FastAPI API 与 SSE：包括 chat、session、model、notification、workspace、sync、task、trigger、automation 等端点，并用 bearer token middleware 保护非公开接口。

## 机制清单

### Always-on VPS 与 local-first delivery

- 控制什么：把 agent 的执行位置放在 VPS 上，把最终文件和通知送回用户本地工作区。
- 补偿的失败模式：纯 desktop agent 依赖本机在线，纯 cloud agent 又容易把产物困在云端工作区。
- 证据位置：`README.md` 架构图，`src/main.py`，`src/integrations/syncthing_watcher.py`，`src/core/prompt.py`，`desktop/`。
- 代价：系统边界跨 VPS、Syncthing、本地桌面、IM channel 与第三方 app。部署、权限、同步状态和故障排查都会比单机 agent 更复杂。

### 多通道共享 session

- 控制什么：Desktop、Feishu、Telegram 等入口共享同一个 owner identity 与 session 管理。
- 补偿的失败模式：用户在不同入口触发任务时，agent 状态和交付通道割裂。
- 证据位置：`src/main.py`、`src/channels/base.py`、`src/channels/registry.py`、`src/core/agent_runner.py`、`src/core/session.py`、`src/config.py`。
- 代价：当前设计更像 single-owner runtime。多用户隔离、权限边界和 channel-native identity 的长期模型仍需深读确认。

### Agent loop 的运行护栏

- 控制什么：LLM 调用、tool call 执行、上下文压缩、工具输出 spill、最大轮次与历史修复。
- 补偿的失败模式：长对话上下文爆掉、工具输出撑爆上下文、历史里有未完成 tool call 导致 API 400、agent 无限循环。
- 证据位置：`src/core/agent.py`、`src/context/compressor.py`、`src/context/spill.py`、`src/config.py`。
- 代价：护栏主要是运行时补偿。它提高了可运行性，但不等于强权限安全或任务正确性评估。

### Workspace 与 sync context 注入

- 控制什么：每个 session 绑定到一个 workspace，workspace 再绑定 Syncthing folder；用户最近的同步事件会被注入到 agent 输入里。
- 补偿的失败模式：用户说“刚放进去的文件”时，agent 不知道对应哪个远端路径。
- 证据位置：`src/core/workspace.py`、`src/core/session.py`、`src/core/prompt.py`、`src/core/agent_runner.py`、`src/integrations/syncthing_watcher.py`。
- 代价：正确性依赖 Syncthing 事件、folder 映射和 workspace 记录一致。同步延迟或冲突会直接影响 agent 的上下文质量。

### Syncthing 双端配对与 folder provisioning

- 控制什么：桌面端和 VPS 端分别调用本机 Syncthing REST API，把同一个 `folder_id` 注册到两端，并把对方 device ID 加入共享设备列表。
- 补偿的失败模式：手动配对需要用户复制 device ID、创建 folder、接受分享，容易配置错路径或产生 ghost folder。
- 证据位置：`docs/syncthing_setup.md`、`docs/desktop_setup.md`、`desktop/electron/main.cjs`、`desktop/electron/preload.cjs`、`desktop/src/components/onboarding-dialog.tsx`、`src/channels/desktop.py`、`src/tools/syncthing.py`。
- 代价：自动配对依赖已经可信的 Desktop API token 作为 trust channel。仓库目前刻意不在 `/api/sync/pair` 里自动分享所有 VPS folders，而是要求用户显式创建/选择 workspace folder，避免 ghost-folder propagation 和路径混乱。

### Cross-device sync status

- 控制什么：同步状态不是只看 VPS 本地 folder 是否 idle，而是把 VPS 自己的 `needBytes/needItems` 与已连接 peer 的 `/rest/db/completion` 汇总起来。
- 补偿的失败模式：VPS 认为自己已经 idle，但用户电脑还没下载完，桌面 UI 却显示“已同步”。
- 证据位置：`src/tools/syncthing.py` 的 `get_folder_sync_info()`，`src/channels/desktop.py` 的 `/api/sync/folders` 与 `/api/sync/status`。
- 代价：离线设备会被跳过。这个选择避免用户电脑关机时永远显示 syncing，但也意味着“所有历史设备都已同步”不是当前语义。

### Sync event watcher 与方向建模

- 控制什么：VPS 后端长轮询 Syncthing `/rest/events`，订阅 `RemoteChangeDetected`、`LocalChangeDetected`、`ItemStarted`、`ItemFinished`、`DownloadProgress`、`FolderCompletion`。
- 补偿的失败模式：agent 和 UI 只知道 folder 级状态，不知道具体哪个文件从本地传上来、哪个文件从 VPS 发回去。
- 证据位置：`src/integrations/syncthing_watcher.py`、`desktop/src/components/sync-folder-widget.tsx`。
- 代价：出站方向 VPS -> 用户没有天然 per-file finish 事件，代码用 `FolderCompletion == 100%` 近似把该 folder 的 pending outbound events 标记完成。

### 三类 proactive automation

- 控制什么：时间触发、外部 app 事件触发、本地文件变更触发。
- 补偿的失败模式：传统 agent 只能在用户主动发消息时工作，无法把“事件发生”变成“工作已经先推进”。
- 证据位置：`src/automations/scheduler/engine.py`、`src/automations/scheduler/executor.py`、`src/automations/composio_triggers.py`、`src/automations/file_drop.py`、`src/tools/routines.py`。
- 代价：自动化任务必须自己带完整 prompt、工具权限和交付路径。prompt 不完整或权限过宽时，失败会发生在用户不在场的后台。

### NotificationStore 作为人类审批面

- 控制什么：把 autonomous agent 的结果变成通知卡片，并保留完整 autonomous session 供用户回看或继续处理。
- 补偿的失败模式：后台 agent 完成工作后只发一段文本，用户无法审查过程、交付物和下一步动作。
- 证据位置：`src/delivery/notifications.py`、`src/channels/desktop.py`、`desktop/src/components/notification-card.tsx`、`desktop/src/components/deliverables/`。
- 代价：通知层要同时维护轻量 index 和完整 session。数据迁移、清理、读取性能和跨 channel 一致性会成为维护点。

### Tool registry 与权限预设

- 控制什么：工具通过 `@tool` 注册，带 `read`、`write`、`execute`、`network`、`admin` 等 tags；自动化任务可以选择 `read_only`、`read_write`、`safe`、`full`。
- 补偿的失败模式：自动化 trigger 或 cron 默认拿到完整 shell / 网络 / 外部 API 权限，风险过高。
- 证据位置：`src/tools/registry.py`、`src/tools/command.py`、`src/tools/scheduler.py`、`src/tools/routines.py`、`developdocs/tool-access-control.md`。
- 代价：`developdocs/tool-access-control.md` 明确写着基础文件操作在任何权限设置下都可用。也就是说这里是风险分层，不是严格 sandbox。

### Subagent delegation

- 控制什么：主 agent 可以把复杂任务交给独立 subagent，但实现上是同步阻塞等待结果。
- 补偿的失败模式：复杂任务挤占主上下文，或者需要隔离的大任务污染当前会话。
- 证据位置：`src/tools/delegate.py`、`src/subagent/`。
- 代价：设计注释明确选择 blocking delegation，因为主 agent 通常需要结果才能继续。这降低并发复杂度，但牺牲并行工作能力。

### Desktop API 作为产品控制面

- 控制什么：桌面端不是纯聊天 UI，而是工作区、同步、通知、任务、trigger、automation 的控制面。
- 补偿的失败模式：后台 agent 的状态散落在 CLI、IM、文件夹和服务日志里，用户难以形成可审查的工作面。
- 证据位置：`src/channels/desktop.py` 的 `/api/chat`、`/api/notifications`、`/api/workspaces`、`/api/sync`、`/api/tasks`、`/api/triggers`、`/api/automations` 端点，以及 `desktop/src/App.tsx`。
- 代价：`src/channels/desktop.py` 已经承担很宽的 API surface，后续可能需要拆分路由或服务边界。

## 证据锚点

- Snapshot 来源：[github-repo-luliyanng-nono-cowork.md](../../../raw/external/github-repo-luliyanng-nono-cowork.md)
- 仓库：`LuliYanng/Nono-Cowork`
- 观察分支：`main`
- 解析到的 commit：`c8c4746499033bf81c22cd07c8ad52aabcf97b86`
- README 与 manifest：`README.md`、`README_zh-CN.md`、`pyproject.toml`、`nono-cowork.service`、`desktop/package.json`
- 后端入口与核心：`src/main.py`、`src/core/agent.py`、`src/core/agent_runner.py`、`src/core/session.py`、`src/core/workspace.py`、`src/core/prompt.py`
- 通道与桌面 API：`src/channels/base.py`、`src/channels/desktop.py`、`src/channels/registry.py`
- 自动化：`src/automations/composio_triggers.py`、`src/automations/file_drop.py`、`src/automations/scheduler/engine.py`、`src/automations/scheduler/executor.py`
- 通知与交付：`src/delivery/notifications.py`、`desktop/src/components/notification-card.tsx`、`desktop/src/components/deliverables/`
- 工具与权限：`src/tools/registry.py`、`src/tools/command.py`、`src/tools/delegate.py`、`src/tools/routines.py`、`developdocs/tool-access-control.md`
- 同步集成：`src/integrations/syncthing_watcher.py`、`desktop/electron/vendor/syncthing/README.md`
- 同步底层机制：`docs/syncthing_setup.md`、`docs/desktop_setup.md`、`desktop/electron/main.cjs`、`desktop/electron/preload.cjs`、`desktop/src/components/onboarding-dialog.tsx`、`desktop/src/components/sync-folder-widget.tsx`、`desktop/src/hooks/use-sync-status.ts`、`src/tools/syncthing.py`

## 开放问题

- `src/channels/desktop.py` 的 API surface 是否已经过宽，后续是否需要按 session、sync、automation、notification 拆分。
- `tool_access` 的实际风险边界有多强。尤其是文件写入工具始终可用，而 README 又提醒 unrestricted shell access 不适合生产。
- Composio trigger、file-drop、cron 三类 autonomous session 的失败恢复、重试、幂等和去重策略是否足够。
- 多设备共享同一个 workspace folder 时，workspace 删除语义需要重设。当前 `delete_workspace` 注释明确写着 single-device assumption，如果多个客户端共享同一 folder，这个 endpoint 会变成 global nuke。
- 多设备场景下的冲突治理仍需深读。`syncthing_watcher.py` 能识别 `.sync-conflict-` 文件，但 repo map 尚未确认 UI 和 agent policy 如何处理冲突。
- 桌面端承载一部分本地安全与路径边界：它只暴露本地 Syncthing、文件打开、folder picker、配置存储等 IPC，而不是把任意本地 shell 暴露给 VPS。
- 当前没有在 snapshot 中看到 `.github/workflows/` 或顶层 `tests/`。质量门禁和回归测试状况需要后续确认。

## 可迁移判断

`Nono-Cowork` 最值得学习的不是某个工具函数，而是它把“proactive agent”拆成了四个稳定表面：事件入口、独立执行 session、通知审批面、本地文件交付。这个拆法比“让 agent 常驻聊天窗口”更接近真实工作流。

同时，这个仓库也显示出 proactive agent 的主要工程负担：权限、同步状态、后台任务可审查性、失败恢复和 UI 控制面都会迅速变成一等问题。它适合作为 `Clawhouse`、多人协作 agent 工作台、local-first agent runtime 等主题的对照样本。

## 来源依据

- [仓库 snapshot](../../../raw/external/github-repo-luliyanng-nono-cowork.md)

## 相关页面

- [代码库作为知识来源](codebases-as-knowledge-sources.md)
- [Clawhouse:多设备 Agent 上下文同步](clawhouse-多设备-agent-工作台.md)
- [被持续委托的工作主体](被持续委托的工作主体.md)
- [Agent 时代的人机交互新命题](agent时代的人机交互新命题.md)
- [Slock:人机协作平台](Slock-人机协作平台.md)
