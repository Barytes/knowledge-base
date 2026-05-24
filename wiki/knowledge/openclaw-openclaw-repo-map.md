# openclaw/openclaw 仓库地图

## 摘要

这页是围绕主题"个人 AI assistant、Gateway 与持续身份层"维护的 `openclaw/openclaw` 第一版仓库地图。

从 GitHub README、公开 docs 与顶层结构看,`OpenClaw` 已经明显不是"给现有 coding agent 套一个聊天壳"那么简单。它在产品叙事上明确把主语放在 assistant 本身,而不是 Gateway 本身:README 直接写 "The Gateway is just the control plane - the product is the assistant"。

但从公开架构文档看,它的系统实现主语仍然强烈地是 Gateway。Gateway 是一个 long-lived、always-on 的本地中枢,承接 channels、sessions、control UI、WebSocket API、nodes、heartbeat 与 WebChat。也就是说,OpenClaw 已经在努力把 agent 做成一个有 identity、workspace、memory、multi-agent routing 与主动行为的 personal AI assistant,但它并没有完全摆脱 gateway-centric 的实现结构。

就你当前关心的主题看,`OpenClaw` 最值得注意的不是"能不能通过聊天软件访问",而是它已经认真做了下面这些层:

- assistant 作为产品主语
- `SOUL.md` 作为人格与风格主文件
- multi-agent routing 下的 per-agent workspace / sessions / auth
- always-on heartbeat 与 `HEARTBEAT.md`
- device nodes 作为 assistant 可调用的能力来源

这让它比多数聊天入口型 agent 产品更接近"持续存在的 assistant",但它离"一个高于设备、主动持有工作、以 re-entry inbox 与你协作的 kernel"仍然还有一层差距。

当前置信度仍停留在"架构地图"层,而不是"实现已读透"层:它已经足够支撑定向追问,但还不足以裁定每一条工程实践判断。

## 仓库目的

- README 的公开定位非常直接:`OpenClaw` 是一个 "personal AI assistant you run on your own devices"。
- 它强调 assistant 才是产品本体,而 Gateway 只是 control plane。这和很多以 terminal、bot 或 web shell 为主语的 agent 产品不同。
- README 还把 single-user、local-first、always-on 作为核心感受来卖,而不是把它定义成团队任务系统或纯自动化平台。
- docs 进一步把这条定位拆开成:
  - Gateway 是 one always-on process
  - sessions、channels、tools、events 都经由 Gateway
  - 多个 agent 可以在同一 Gateway 中隔离存在
  - device nodes 作为额外能力接入
- 观察时默认分支:`main`
- 主要语言:`TypeScript`
- 公开文档里还能看到一套围绕 CLI、Gateway、macOS app、iOS/Android nodes、Canvas 与 skills 的完整产品面,而不只是一个 npm CLI。
- 仓库地址:https://github.com/openclaw/openclaw

## 架构地图

### 顶层目录

- `.agents`
- `.github`
- `.pi`
- `.vscode`
- `Swabble`
- `apps`
- `assets`
- `docs`
- `extensions`
- `git-hooks`
- `packages`
- `patches`
- `qa`
- `scripts`
- `skills`
- `src`
- `test`
- `test-fixtures`
- `ui`
- `vendor`

### 顶层文件

- `.codex`
- `.detect-secrets.cfg`
- `.dockerignore`
- `.env.example`
- `.gitattributes`
- `.gitignore`
- `.jscpd.json`
- `.mailmap`
- `.markdownlint-cli2.jsonc`
- `.npmignore`
- `.npmrc`
- `.oxfmtrc.jsonc`
- `.oxlintrc.json`
- `.pre-commit-config.yaml`
- `.prettierignore`
- `.secrets.baseline`
- `.shellcheckrc`
- `.swiftformat`
- `.swiftlint.yml`
- `AGENTS.md`
- `CHANGELOG.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `Dockerfile`
- `Dockerfile.sandbox`
- `Dockerfile.sandbox-browser`
- `Dockerfile.sandbox-common`
- `INCIDENT_RESPONSE.md`
- `LICENSE`
- `Makefile`
- `README.md`
- `SECURITY.md`
- `VISION.md`
- `appcast.xml`
- `docker-compose.yml`
- `docker-setup.sh`
- `docs.acp.md`
- `dream-diary-preview-v2.html`
- `dream-diary-preview-v3.html`
- `fix2.py`
- `fly.private.toml`
- `fly.toml`
- `knip.config.ts`
- `openclaw.mjs`
- `openclaw.podman.env`
- `package.json`
- `pnpm-lock.yaml`
- `pnpm-workspace.yaml`
- `pyproject.toml`
- `render.yaml`
- `setup-podman.sh`
- `tsconfig.json`
- `tsconfig.oxlint.json`
- `tsconfig.plugin-sdk.dts.json`
- `tsdown.config.ts`
- `vitest.config.ts`
- `zizmor.yml`

### 第一版子系统角色判断

- `Gateway` 是系统中枢。公开 docs 明确写它是 single long-lived process,负责 routing、control plane、channel connections、WS API、HTTP surfaces 和 heartbeat。
- `assistant` 是产品叙事主语。README 一再强调产品不是 gateway,而是 assistant。
- `agents` 在实现上已经是清晰对象。公开 multi-agent 文档把一个 agent 定义成 workspace + `agentDir` + sessions + auth 的隔离组合,而不只是聊天实例。
- `SOUL.md`、`AGENTS.md`、`TOOLS.md` 这类 prompt files 是它人格层、操作边界层与行为层的关键构件。
- `nodes` 是设备能力接入层。macOS / iOS / Android / headless nodes 通过 Gateway WebSocket 暴露本地能力,而不是直接等于 assistant 本体。
- `WebChat`、Control UI、Canvas、companion apps 说明它并不把聊天软件入口当成唯一交互面。

## 机制清单

### 用 "assistant 是产品,Gateway 是 control plane" 重写系统主语

- README 的这句定位非常关键:
  - "The Gateway is just the control plane - the product is the assistant."
- 这控制的是很多多渠道 agent 产品容易滑向"其实只是一个 bot hub"的失败模式。
- 代价是它必须同时维护两层叙事:
  - 面向用户时,assistant 才是产品本体
  - 面向实现时,Gateway 仍然是最强系统中枢
- 这也是 OpenClaw 当前最值得注意的结构性张力。

### 用 Gateway 作为 always-on 本地中枢承接 channels、sessions、tools 与 UI

- 公开 gateway runbook 明确写:
  - one always-on process for routing, control plane, and channel connections
  - single multiplexed port for WS control/RPC、HTTP APIs、Control UI 和 hooks
- 架构文档也明确写:
  - a single long-lived Gateway owns all messaging surfaces
  - clients 与 nodes 都连到同一个 WS server
- 这控制的是渠道碎片化、状态不一致和多入口漂移的问题。
- 代价是 Gateway 成为实现里的真正中心对象,assistant 的高层抽象仍要通过它落地。

### 用 `SOUL.md` 把人格层做成一等 prompt file

- docs 明确把 `SOUL.md` 写成"智能体声音所在的地方",并说明普通会话中会注入它。
- `SOUL` 模板进一步把 continuity 讲得很明确:
  - 每次会话都是 fresh
  - 这些文件是你的 memory
  - 阅读它们、更新它们,它们是你持续存在的方式
- 这控制的是 agent 风格漂移、人格不稳定和"每次都像新壳"的问题。
- 代价是人格连续性强依赖 prompt files 的维护质量,而不是更深的 persistent runtime abstraction。

### 用 multi-agent routing 把一个 Gateway 扩展成多个隔离 agent

- multi-agent 文档把 "one agent" 定义成:
  - workspace
  - `agentDir`
  - session store
  - per-agent auth profiles
- 绑定规则决定 inbound channels/accounts/peers 路由到哪个 agent。
- 这控制的是多个 persona、多账户、多工作区之间的串线问题。
- 代价是它当前更像"同一 Gateway 下多个隔离 brains",而不是"一个更高层 assistant 自由调度多个 execution bodies"。

### 用 heartbeat 和 `HEARTBEAT.md` 把 assistant 做成主动存在

- README 强调 always-on。
- heartbeat docs 则把这层能力具体化成:
  - 周期性 heartbeat
  - 默认可以全天运行
  - `HEARTBEAT.md` 作为稳定 checklist
  - agent 可在 heartbeat 中主动维护这份 checklist
- 这控制的是 assistant 完全被动、只有你来问才会响应的失败模式。
- 代价是主动性更多表现为周期性 upkeep,而不一定已经等于高层的持续工作简报。

### 用 nodes 把设备能力纳入 assistant,而不直接等同于 assistant

- 架构文档中 nodes 通过 Gateway WebSocket 暴露能力。
- README 也清楚区分:
  - Gateway host 运行 exec 和 channel 连接
  - device nodes 运行 device-local actions
- 这控制的是"assistant 必须完全绑定某一个 host 才能工作"的限制。
- 代价是设备能力仍然通过 Gateway 和 node protocol 被组织,而不是由一个更抽象的 agent kernel 自然调度。

### 用 Web surfaces、Canvas 和 companion apps 扩展默认交互面

- README 已不只卖消息入口,还强调:
  - WebChat
  - Control UI
  - live Canvas
  - macOS app
  - iOS / Android nodes
- 这控制的是"助手只能存在于聊天软件里"的单一入口问题。
- 代价是交互面增多之后,真正的默认入口到底是聊天、控制面板还是别的高层工作面,会变得更值得继续追问。

### 用仓库契约与 CI 外化复杂系统的协作边界

- 顶层有 `AGENTS.md`、`CLAUDE.md`、大量 workflows、release 流程与安全文件。
- 这控制的是大仓库、多入口、多平台、多贡献者下的漂移。
- 代价是系统工程面明显比单一 CLI agent 厚得多。

## 证据锚点

- Snapshot 来源:[github-repo-openclaw-openclaw.md](../../raw/external/github-repo-openclaw-openclaw.md)
- Docs 摘要:[openclaw-public-docs-notes.md](../../raw/external/openclaw-public-docs-notes.md)
- 仓库:`openclaw/openclaw`
- 观察分支:`main`
- 解析到的 commit:`f2c7cec8de2c7c5867f126b93fec3349c5cbe385`

- `.github/workflows/auto-response.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/control-ui-locale-refresh.yml`
- `.github/workflows/docker-release.yml`
- `.github/workflows/docs-sync-publish.yml`
- `.github/workflows/docs-translate-trigger-release.yml`
- `.github/workflows/install-smoke.yml`
- `.github/workflows/labeler.yml`
- `.github/workflows/macos-release.yml`
- `.github/workflows/openclaw-npm-release.yml`
- `.github/workflows/plugin-clawhub-release.yml`
- `AGENTS.md`
- `CLAUDE.md`
- `Dockerfile`
- `Makefile`
- `README.md`
- `docker-compose.yml`
- `package.json`
- `pnpm-workspace.yaml`
- `pyproject.toml`

## 开放问题

- assistant 的 identity 到底在多大程度上独立于 Gateway/host,而不只是依靠 workspace + prompt files + sessions 拼起来?
- multi-agent routing 更接近"多个隔离 brains",还是已经接近更高层的长期协作对象?
- heartbeat 当前更多是 upkeep / cron 语义,还是已经在走向真正的 proactive work briefing?
- 默认入口在产品上究竟是什么:聊天、WebChat、Control UI、Canvas,还是别的更高层工作面?

## 来源依据

- [仓库 snapshot](../../raw/external/github-repo-openclaw-openclaw.md)
- [公开 docs 摘要](../../raw/external/openclaw-public-docs-notes.md)

## 相关页面

- [multica-ai/multica 仓库地图](multica-ai-multica-repo-map.md)
- [Clawhouse:多设备 Agent 上下文同步](../bridges/clawhouse-多设备-agent-工作台.md)
