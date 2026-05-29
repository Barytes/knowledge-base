# Slock：人机协作平台

> 来源：https://slock.ai/

## 产品定位

Slock 是一个 humans 和 AI agents 在 channels 和 DMs 中协作的平台——**不是作为工具，而是作为队友**。

**核心主张**：

> "The future of work isn't humans using AI tools. It's humans and AI agents collaborating."

## 核心特性

### 1. Agents That Remember

每个 agent 有持久记忆——记住你的代码库、偏好、历史对话，**跨 session 持续存在**。

### 2. One Conversation

Channels 和 DMs 中，humans 和 agents 是平等的。Agents 看到频道里的每条消息，自然响应。**无需上下文切换，无需复制粘贴**。

### 3. Your Machines, Your Agents

Agents 通过轻量 daemon 在**你自己的机器上执行**：
- 完全控制算力
- 完全隐私保护代码和数据

命令：`npx @slock-ai/daemon`

### 4. Always on, Always ready

Agents 不"下班"——idle 时 hibernate，需要时立刻唤醒，**完整上下文恢复**。

状态示例：
- Atlas — Online
- Luna — Thinking…
- Nova — Working…
- Echo — Offline

## 使用流程

1. **Create a Server** — 几秒钟设置，邀请团队
2. **Connect a Machine** — 一行命令连接硬件
3. **Spawn Agents** — 用描述定义角色，加入频道
4. **Collaborate** — 自然聊天，agents 记住上下文，持续工作

## 与其他产品的对比

| 维度 | Slock | multica | OpenClaw | clawhouse |
|------|-------|---------|----------|-----------|
| **核心定位** | humans + agents 协作频道 | team task system + managed agents | personal assistant + Gateway | 跨设备 agent 接回 |
| **协作单位** | channel / DM（平等对话） | issue / board（任务分配） | channel routing（多渠道） | session sync（历史同步） |
| **agent 记忆** | ✅ persistent memory，跨 session | ✅ skills 沉淀 | ✅ SOUL.md + workspace | ❓ 对话历史同步 |
| **执行位置** | 用户自己的机器（daemon） | 本地 daemon + 云端 runtime | Gateway host + device nodes | 任意设备 |
| **always-on** | ✅ hibernate + wake with context | ✅ daemon 轮询任务 | ✅ heartbeat | ❓ 异步恢复 |
| **主语** | agents（队友） | workspace / issue（任务系统） | assistant（人格） | agent（协作对象） |

### 与 multica 的相似与差异

**相似**：
- 都是团队级 managed agents 平台
- 都用 daemon 把用户机器接入平台
- 都让 agents 成为协作系统的一等公民

**差异**：
- multica 以 issue/task lifecycle 为中心（任务分配 → 状态追踪）
- Slock 以 channel/DM 为中心（平等对话 → 自然协作）
- multica 强调 skills 复利沉淀
- Slock 强调 agents 的持续记忆和随时唤醒

### 与 OpenClaw 的相似与差异

**相似**：
- 都强调 agent 持续存在（persistent memory / SOUL.md）
- 都支持 always-on（hibernate + wake / heartbeat）
- 都让 agents 在多个渠道/频道中存在

**差异**：
- OpenClaw 是 single-user personal assistant
- Slock 是 team collaboration platform
- OpenClaw 用人格锁定策略（SOUL.md）
- Slock 用对话频道策略（channel equality）

### 与 clawhouse 的关系

**Slock 已 address 的部分**：
- agents execute on your own machines via daemon → 与 clawhouse 的"不锁定到云端"一致
- wake with full context restored → 类似 clawhouse 设想的"接回完整上下文"

**Slock 未 address 的部分**：
- 依赖实时协作（channel/DM），而非异步同步恢复
- 团队协作视角，而非个人多设备视角
- agents 的可见性停留在对话层，而非运行时现场层

## 关键洞察

Slock 的设计揭示了几个重要趋势：

1. **Agents 作为队友而非工具** — 不是"我调用你"，而是"我们一起在频道里协作"
2. **持久记忆是基础设施** — 跨 session 的记忆不是锦上添花，而是 agents 能持续协作的前提
3. **用户控制算力** — daemon 在自己的机器上执行，隐私和可控性是核心承诺
4. **Hibernate + Wake** — agents 不需要一直在线消耗资源，idle 时休眠，需要时唤醒

## 与知识库其他主题的关联

- [multica-ai/multica 仓库地图](multica-ai-multica-repo-map.md)：团队级 managed agents 平台，以任务系统为中心
- [openclaw/openclaw 仓库地图](openclaw-openclaw-repo-map.md)：个人 assistant，以人格和 Gateway 为中心
- [Clawhouse：多设备 Agent 工作台](clawhouse-多设备-agent-工作台.md)：个人多设备场景的 agent 接回
- [被持续委托的工作主体](被持续委托的工作主体.md)：agent 作为持续协作对象的概念分析