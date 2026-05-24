# multica-ai/multica 仓库地图

## 摘要

这页是围绕主题“多设备 agent 访问与运行时工作面”维护的 `multica-ai/multica` 第一版仓库地图。

从 README、`AGENTS.md`、`Makefile` 与 CI 配置看，`multica` 不是单纯给现有 coding agent 加一个远程壳，而是在把 agent 重写成任务系统中的一等协作者：agent 可以像同事一样被分配 issue、自动执行、回报阻塞、更新状态，并把可复用技能沉淀进团队工作流。

就你当前关心的“多设备 agent 访问与运行时工作面”主题看，`multica` 确实和 `clawhouse` 很接近，但它已经往前走了一步。它的中心不是移动端 launcher，而是“面向团队任务流的 managed agents platform”。设备与 runtime 仍然重要，但被放进更大的 board、workspace、issue lifecycle 与 skill compounding 语义里。

当前置信度仍停留在“架构地图”层，而不是“实现已读透”层：它已经足够支撑定向追问，但还不足以裁定每一条工程实践判断。

## 仓库目的

- README 的公开定位是 “The open-source managed agents platform”。
- 它想把 coding agents 变成“真正的队友”，而不是终端里的临时执行器。核心动作不是聊天，而是分配任务、跟踪进度、复用技能。
- `AGENTS.md` 进一步把目标具体化成一套适合 2-10 人 AI-native 团队的任务系统：agent 可以被指派 issue、创建 issue、发表评论、改变状态，并支持本地 daemon 与云端 runtime。
- 观察时默认分支：`main`
- 主要语言：`TypeScript`
- 后端实际还有一套 `Go` 服务与 CLI/runtime 侧实现，所以仓库更准确地说是 `TypeScript + Go` 的双栈系统。
- 仓库地址：https://github.com/multica-ai/multica
- 从 README 的架构图和 `AGENTS.md` 的目录说明看，它的实际产品形态是：`Next.js` 前端 + `Go` 后端 + `PostgreSQL/pgvector` + 本地 daemon/runtime 接入层。

## 架构地图

### 顶层目录

- `.github`
- `apps`
- `docker`
- `docs`
- `e2e`
- `packages`
- `scripts`
- `server`

### 顶层文件

- `.dockerignore`
- `.env.example`
- `.gitattributes`
- `.gitignore`
- `.goreleaser.yml`
- `.npmrc`
- `AGENTS.md`
- `CLAUDE.md`
- `CLI_AND_DAEMON.md`
- `CLI_INSTALL.md`
- `CONTRIBUTING.md`
- `Dockerfile`
- `Dockerfile.web`
- `LICENSE`
- `Makefile`
- `README.md`
- `README.zh-CN.md`
- `SELF_HOSTING.md`
- `SELF_HOSTING_ADVANCED.md`
- `SELF_HOSTING_AI.md`
- `docker-compose.selfhost.yml`
- `docker-compose.yml`
- `package.json`
- `playwright.config.ts`
- `pnpm-lock.yaml`
- `pnpm-workspace.yaml`
- `skills-lock.json`
- `turbo.json`

### 第一版子系统角色判断

- `apps/web` 是主工作台，承接 board、workspace、issues、inbox、skills 与 realtime 这些用户可见工作面。
- `server` 是系统中枢，负责 REST API、认证、issue/comment/agent 等 handler、任务编排、事件广播和 daemon 接入。
- 本地 daemon 不是边缘工具，而是这个系统把“你的机器”接入平台的关键方式。它负责发现本机可用的 CLI agent，并把它们注册成 runtime。
- `pkg/agent` 把 Claude Code、Codex 等 provider 抽象成统一 backend，这说明 `multica` 在努力把不同 agent CLI 压进同一任务执行语义。
- `e2e`、`.github/workflows/ci.yml`、根级 `Makefile` 共同组成跨前后端的验证与运行契约。

### 关键执行流

按 README 与 `AGENTS.md` 当前暴露的信息，这个系统的主路径大致是：

1. 用户在 Web 工作台里创建或分配 issue。
2. issue 可以被分配给 agent，而不只是人类成员。
3. 后端的 task lifecycle 服务把任务编排成 `enqueue -> claim -> start -> complete/fail`。
4. daemon 作为本地 runtime 轮询任务，并按 provider 路由到 Claude Code、Codex、OpenClaw 或 OpenCode。
5. 执行中的消息、状态与结果通过 WebSocket 回推到前端工作台。

这说明它的重心不在单次 prompt，而在“任务系统怎样持续调度 agent 并把状态同步回团队界面”。

## 机制清单

### 把 agent 建模成 issue assignee，而不是聊天对象

- `AGENTS.md` 明确写到 assignee 可以是 member，也可以是 agent，并在数据层使用 `assignee_type + assignee_id`。
- 这控制的是“agent 只能作为工具调用存在”的限制，把 agent 提升成任务系统里的原生参与者。
- 代价是产品语义会更重。系统必须同时处理人类成员和 agent 的身份、状态、权限与 UI 呈现，而不能只做一个轻聊天壳。

### 用 daemon/runtime 机制把分散算力接入统一工作面

- README 和 `AGENTS.md` 都强调本地 daemon。daemon 会自动发现本机 PATH 上可用的 `claude`、`codex`、`openclaw`、`opencode`，并把这台机器注册成 runtime。
- 这控制的是“设备很多，但每台机器到底能跑什么 agent、能不能接任务”这一类分布式执行问题。
- 代价是系统必须维护 daemon 生命周期、runtime 注册、provider 路由和本地 CLI 兼容性，复杂度明显高于单机 agent UI。

### 用 task lifecycle 服务把 agent 执行收束成可观测状态机

- `internal/service/task.go` 被 `AGENTS.md` 点名为任务编排中心，负责 `enqueue -> claim -> start -> complete/fail`，并自动同步 issue 状态、广播 WebSocket 事件。
- 这控制的是 agent 执行过程“不知道现在到哪一步了”的黑盒问题，把运行状态变成 board 可消费的事件流。
- 代价是系统会更偏 orchestration platform，而不是简单的远程访问层。

### 用 WebSocket 把运行时进度持续推回前端

- `AGENTS.md` 里前端专门有 `features/realtime/`，后端有 `internal/realtime/` hub，并在 README 里把 “real-time progress streaming” 当成核心特性。
- 这控制的是 agent 任务只在后台悄悄完成、用户只能靠轮询或总结文本得知进展的失败模式。
- 代价是前后端都要围绕长连接、事件同步和乐观更新设计，架构会更像协作软件而不是单页控制台。

### 用 workspace isolation 承接团队级协作，而不只面向单用户多设备

- `AGENTS.md` 明确写出 multi-workspace、`workspace_id` 过滤、membership checks 和 `X-Workspace-ID` header。
- 这控制的是 agent、issue、skills 和设置在多团队环境里的混线问题。
- 代价是它的第一性问题已不再只是“我怎么连回我那台机器”，而是“一个团队怎样共享 agent、任务与技能资产”。

### 用 skills 作为团队复利层，而不只做单次任务执行

- README 把 “Reusable Skills” 列为核心特性，强调 solutions 会沉淀成 reusable skills。
- 这控制的是每次 agent 完成任务后能力不留痕、团队只能重复提示的失败模式。
- 代价是平台要额外承担 skill 的存储、发现、治理和版本兼容问题。

### 用自托管与一键安装降低接入门槛

- README 提供了 CLI 安装、`multica setup`、`multica setup --local` 和 self-host 路径；`Makefile` 则把 `setup`、`start`、`selfhost`、`daemon` 等路径收束成脚本入口。
- 这控制的是“平台很强，但部署太重，导致 runtime 无法真正分散接入”的落地阻力。
- 代价是运维面会扩张，需要兼顾本地运行、Docker、自托管和 CLI 配置体验。

### 用 AI contributor contract 固化仓库内协作边界

- 根级 `AGENTS.md` 与 `CLAUDE.md` 不只是普通贡献指南，而是把前后端目录边界、状态管理约束、测试路径、命名方式和完成标准显式写出来。
- 这控制的是多 agent / 多贡献者同时修改时的漂移，尤其是当仓库本身就在为 agent 设计时，更需要把协作契约文本化。
- 代价是贡献门槛更高，新贡献者必须先接受这套 repo contract。

## 证据锚点

- Snapshot 来源：[github-repo-multica-ai-multica.md](../../raw/external/github-repo-multica-ai-multica.md)
- 仓库：`multica-ai/multica`
- 观察分支：`main`
- 解析到的 commit：`9ed80120e091bb50a7838a0fd0009ef384f5fb19`

- `.github/workflows/ci.yml`
- `.github/workflows/release.yml`
- `AGENTS.md`
- `CLAUDE.md`
- `Dockerfile`
- `Makefile`
- `README.md`
- `docker-compose.yml`
- `package.json`
- `pnpm-workspace.yaml`
- `turbo.json`

## 开放问题

- daemon 与 cloud runtime 在代码里到底是对称抽象，还是本地 daemon 仍然是主路径、cloud 只是延伸能力？
- `pkg/agent` 当前到底统一到了哪一层：只是 CLI 启动接口一致，还是连消息流、能力探测与错误恢复都已抽象一致？
- skills 在实现里是“任务模板库”“沉淀出的能力包”，还是更接近组织级 SOP 载体？README 的产品语言很强，但还需要更深代码证据。
- WebSocket 目前已经能覆盖哪些执行中事件，哪些状态仍然依赖补偿性轮询或最终刷新？
- 相比 [Clawhouse：多设备 Agent 的统一入口与运行时工作台](../bridges/clawhouse-多设备-agent-工作台.md)，`multica` 的移动端与项目级 dashboard 是否足够强，还是它更偏桌面/团队协作面？

## 来源依据

- [仓库 snapshot](../../raw/external/github-repo-multica-ai-multica.md)

## 相关页面

- [Clawhouse：多设备 Agent 的统一入口与运行时工作台](../bridges/clawhouse-多设备-agent-工作台.md)
- [badlogic/pi-mono 仓库地图](badlogic-pi-mono-repo-map.md)
- [Claude Code、Codex 与 pi 的 harness 对比](coding-agent-harness-comparison.md)
- [Claude Code：较厚的 agentic coding harness](claude-code-harness.md)
- [Pi coding agent：一种极简且可观察的 coding harness](pi-coding-agent-harness.md)
