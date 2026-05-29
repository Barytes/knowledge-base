# badlogic/pi-mono 仓库地图

## 摘要

这页是围绕主题“coding agent 架构与工程实践”维护的 `badlogic/pi-mono` 第一版仓库地图。

从根 README、`package.json`、`AGENTS.md` 与几条 GitHub workflow 看，这不是一个松散堆叠的 monorepo，而是围绕 `pi-coding-agent` 这个用户入口组织起来的一整套 agent 基础设施仓库：`pi-ai`、`pi-agent-core`、`pi-tui`、`pi-web-ui`、`pi-mom`、`pi-pods` 都被放进同一个发布与开发约束面里。

当前置信度仍停留在“架构地图”层，而不是“实现已读透”层：它已经足够支撑定向追问，但还不足以裁定每一条工程实践判断。

## 仓库目的

- README 的公开定位是 “Tools for building AI agents and managing LLM deployments.”
- 但根 README 又显式把用户导向 `packages/coding-agent`，说明对外最核心的产品入口仍然是 `pi` 这个 coding agent，而不是一个对称的工具箱集合。
- 观察时默认分支：`main`
- 主要语言：`TypeScript`
- 仓库地址：https://github.com/badlogic/pi-mono
- 从 README 的 package 表与根级脚本看，实际形态更接近“以 coding agent 为中心的分层 monorepo”：底层是 `ai`、`agent`、`tui`，上层是 `coding-agent`，再向外扩到 `mom`、`web-ui` 与 `pods`。

## 架构地图

### 顶层目录

- `.github`
- `.husky`
- `.pi`
- `packages`
- `scripts`

### 顶层文件

- `.gitattributes`
- `.gitignore`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `README.md`
- `biome.json`
- `package-lock.json`
- `package.json`
- `pi-test.sh`
- `test.sh`
- `tsconfig.base.json`
- `tsconfig.json`

### 第一版子系统角色判断

- `packages/ai` 是统一 provider API 层，负责多模型、多 provider 与 tool calling 的底层抽象。
- `packages/agent` 是 agent runtime 层，负责事件流、状态与工具循环。
- `packages/tui` 是终端 UI 基础层，服务于 `coding-agent` 的交互形态。
- `packages/coding-agent` 是对外主入口，把前面三层编排成可用 CLI。
- `packages/mom`、`packages/web-ui`、`packages/pods` 更像侧向扩展，分别把同一套能力投向 Slack、Web UI 和 vLLM pod 管理。
- 根级 `package.json` 的 `build` / `dev` 顺序也侧面说明了这种依赖方向：`tui -> ai -> agent -> coding-agent -> mom -> web-ui -> pods`。

## 机制清单

### 以 monorepo workspace 固化分层依赖与锁步发布

- 根级 `package.json` 用 workspaces 管所有包，并把版本升级、release、publish 与 build 顺序都集中在仓库根部。
- 这控制的是“多包一起演化时的接口漂移”问题，避免 `coding-agent`、`ai`、`agent`、`tui` 各自以不同节奏分裂。
- 代价是耦合更强。哪怕只改 `coding-agent`，发布与检查逻辑也天然带着整仓库视角。

### 用 `AGENTS.md` 把开发约束外化成 agent / contributor contract

- 根级 `AGENTS.md` 不是简单的风格提示，而是具体规定了初次阅读顺序、测试禁令、issue/PR 工作流、changelog 规则、provider 接入步骤与 release 约束。
- 这控制的是 AI 贡献者与人工贡献者在大型 monorepo 中“随意探索、乱跑命令、误改契约”的失败模式。
- 它的代价是贡献门槛更高。外部协作者如果不先接受这套契约，很容易在一开始就偏离仓库预期。

### 把公共入口收束到 `packages/coding-agent`，把其余包留作基础设施层

- 根 README 明确写着 “Looking for the pi coding agent? See `packages/coding-agent`”，而 package 表则把其余组件解释为支撑或扩展能力。
- 这控制的是产品表面的复杂度：用户先看到一个清晰入口，而不是七个并列却难以组合的包。
- 代价是理解路径被分成两层。仓库地图要先看根部 contract，再下钻到 `packages/coding-agent` 及其依赖包，不能只盯单个 package README。

### 用 workflow 门控贡献流量，而不只做 CI 检查

- `.github/workflows/pr-gate.yml`、`approve-contributor.yml`、`oss-weekend-issues.yml`、`openclaw-gate.yml` 说明这个仓库把“谁可以贡献、何时可以贡献、哪些外部输入值得进入维护者注意力”当成正式控制问题。
- 这控制的是维护者注意力被低质量 issue / PR 稀释，以及 open-source inbound 流量在高强度开发时段打断主线工作的失败模式。
- 代价是项目对外会显得更强门控，也更依赖维护者显式批准与社交流程。

## 证据锚点

- Snapshot 来源：[github-repo-badlogic-pi-mono.md](../../../raw/external/github-repo-badlogic-pi-mono.md)
- 仓库：`badlogic/pi-mono`
- 观察分支：`main`
- 解析到的 commit：`3b7448d156aab5af1e21fd9ab45d19e4f10865a8`

- `.github/workflows/approve-contributor.yml`
- `.github/workflows/build-binaries.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/openclaw-gate.yml`
- `.github/workflows/oss-weekend-issues.yml`
- `.github/workflows/pr-gate.yml`
- `AGENTS.md`
- `README.md`
- `package.json`
- `packages/coding-agent/README.md`
- `packages/ai/README.md`
- `packages/agent/README.md`
- `packages/tui/README.md`

## 开放问题

- 如果只关心 `pi` 这个 coding agent，下一轮应先深读 `packages/coding-agent/README.md` 还是先回到 `packages/ai` / `packages/agent` / `packages/tui` 的实现入口？
- 根级 `AGENTS.md` 里哪些规则只是贡献规范，哪些其实已经塑造了产品与测试架构？
- `ci.yml`、`pr-gate.yml`、`oss-weekend-issues.yml` 与 `openclaw-gate.yml` 各自的实际触发频率和维护价值是否对称，还是其中只有少数是真正关键门控？
- `build-binaries.yml` 与 `release` 脚本怎样把 monorepo 的锁步版本约束传递到最终的 `pi-coding-agent` 发布物？

## 来源依据

- [仓库 snapshot](../../../raw/external/github-repo-badlogic-pi-mono.md)
- [pi-mono/packages/coding-agent README](../../../raw/external/pi-mono-coding-agent-readme.md)

## 相关页面

- [Pi coding agent：一种极简且可观察的 coding harness](pi-coding-agent-harness.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
- [代码库作为知识来源](codebases-as-knowledge-sources.md)
