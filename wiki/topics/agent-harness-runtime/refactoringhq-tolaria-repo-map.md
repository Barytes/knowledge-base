# refactoringhq/tolaria 仓库地图

## 摘要

这页是围绕主题“仓库架构与工程实践”维护的 `refactoringhq/tolaria` 第一版仓库地图。

从 README 与顶层结构看，这个仓库已经形成清晰的主题定位与控制边界，适合继续按机制而非按文件做定向深读。

当前置信度仍停留在“架构地图”层，而不是“实现已读透”层：它已经足够支撑定向追问，但还不足以裁定每一条工程实践判断。

## 仓库目的

- 公开定位：仓库元数据与 README 表明它有明确主题定位；更精确的中文摘要建议在后续深读时补全。
- 观察时默认分支：`main`
- 主要语言：`TypeScript`
- 仓库地址：https://github.com/refactoringhq/tolaria

## 架构地图

### 顶层目录

- `.claude`
- `.github`
- `.husky`
- `demo-vault-v2`
- `design`
- `docs`
- `e2e`
- `mcp-server`
- `patches`
- `public`
- `scripts`
- `src`
- `src-tauri`
- `tests`

### 顶层文件

- `.codescene-thresholds`
- `.codesceneignore`
- `.codescenerc`
- `.env.example`
- `.githooks-info`
- `.gitignore`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `README.md`
- `SECURITY.md`
- `components.json`
- `eslint.config.js`
- `index.html`
- `package.json`
- `playwright.config.ts`
- `playwright.integration.config.ts`
- `playwright.smoke.config.ts`
- `pnpm-lock.yaml`
- `pnpm-workspace.yaml`
- `trademarks.md`
- `tsconfig.app.json`
- `tsconfig.json`
- `tsconfig.node.json`
- `ui-design.pen`
- `vite.config.ts`

## 机制清单

### 自动化与仓库契约

- 这个仓库通过 GitHub Actions 工作流把质量与交付预期外化出来，而不是只依赖贡献者的非正式自觉。
- 这很可能是在补偿本地开发与合并时质量检查之间的漂移。

### 构建与依赖边界

- Manifest 文件把运行时与打包契约显式放在仓库根部。
- 这能帮助后续阅读者在深入实现文件之前先找到真正的执行边界。

### Agent 或贡献者控制层

- 这个仓库似乎包含显式的指令文件或编辑器规则，用来约束自动化贡献者或人工贡献者的行为方式。
- 这些文件是研究控制逻辑、权限机制与任务塑形方式的强证据点。

### 验证层

- 单独的 `tests/` 目录说明这个仓库把验证当作一级维护子系统。
- 这里最可迁移的问题不只是“测了什么”，而是测试结构如何与 CI 和发布规则相互作用。

### 实现边界

- 单独的 `src/` 目录把实现代码与仓库控制文件清楚分开。
- 这有助于区分运行支架与核心运行时表面。

## 证据锚点

- Snapshot 来源：[github-repo-refactoringhq-tolaria.md](../../../raw/external/github-repo-refactoringhq-tolaria.md)
- 仓库：`refactoringhq/tolaria`
- 观察分支：`main`
- 解析到的 commit：`622977aeb8baece4a132553ddd082b92659a4ce7`

- `.github/workflows/README.md`
- `.github/workflows/auto-update-prs.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/release-stable.yml`
- `.github/workflows/release.yml`
- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `package.json`
- `pnpm-workspace.yaml`

## 开放问题

- 围绕当前研究主题，哪些实现文件承载了主要运行路径？
- README 的叙述与代码、CI 真正执行的路径之间，哪里开始出现偏差？
- 哪些 `src/` 模块定义了杠杆最高的执行路径或架构接缝？
- 哪些 workflow 检查是真正的硬门，哪些只是信息性自动化？

## 来源依据

- [仓库 snapshot](../../../raw/external/github-repo-refactoringhq-tolaria.md)

## 相关页面

- [gogo：本地 llm-wiki 桌面应用](../context-memory-knowledge-system/gogo.md)
- [Naval 财富框架应用于求职困境](../career-positioning-job-search/Naval财富框架应用于求职困境.md)
