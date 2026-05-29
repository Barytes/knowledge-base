# grapeot/context-infrastructure 仓库地图

## 摘要

这页是围绕主题“仓库架构与工程实践”维护的 `grapeot/context-infrastructure` 第一版仓库地图。

这个仓库把自己呈现为一种给 AI 编码 agent 提供持久上下文的参考实现：个人规则、可复用 skills、记忆分层，以及定时观察或反思任务，都被装进一个以 workspace 为形状的系统里。

当前置信度仍然停留在“架构地图”层，而不是“实现已读透”层：它已经足够支撑定向追问，但还不足以裁定每一条工程实践判断。

## 仓库目的

- 公开定位：一个面向 AI 编码 agent 的上下文与记忆系统，强调持久记忆、个人规则、可复用 skills 与定时观察。
- 观察时默认分支：`main`
- 主要语言：`Python`
- 仓库地址：https://github.com/grapeot/context-infrastructure
- 观察到的定位：它不像一个开箱即用产品，更像一份蓝图，展示一个人的 agent 工作区、记忆系统与周期任务如何拼接在一起。

## 架构地图

### 顶层目录

- `adhoc_jobs`
- `contexts`
- `docs`
- `periodic_jobs`
- `rules`
- `tools`

### 顶层文件

- `.env.example`
- `AGENTS.md`
- `README.md`
- `setup_guide.md`

### 第一版子系统角色判断

- `AGENTS.md` 是会话入口。每次运行在真正开始任务前，都要先经过身份、用户、工作区、沟通与 skill 索引。
- `rules/` 看起来是主要控制层，里面保存 persona 规则、用户约束、workspace 路由、沟通指导、公理与 skill 目录。
- `contexts/` 更像累计观察、报告与日常记录的状态层，而不只是一个临时目录。
- `periodic_jobs/` 像自动化层，尤其是 `ai_heartbeat` 这个任务，会通过重复观察与反思让记忆持续刷新。
- `tools/` 更像次级能力层，用于搜索与报告共享，而不是核心控制平面。

## 机制清单

### Agent 或贡献者控制层

- 仓库通过 `AGENTS.md` 显式规定 agent 的启动顺序，要求每次会话先加载 identity、user、workspace、communication 与 skill 指引。
- 这很可能是在补偿跨会话、跨工具的上下文丢失与任务设置不一致。
- 代价是前置复杂度上升：系统依赖贡献者尊重这套路由契约，而不能把仓库当作平面文件树来用。

### 把 workspace 路由当成控制机制

- 根级说明与 README 都强调 `rules/WORKSPACE.md` 是文件路由表，这意味着“找到正确上下文”本身就被视为系统正确性的一部分。
- 这很可能可以避免昂贵的大范围搜索，并减少 agent 把内容写错记忆面或报告面的概率。
- 代价是维护开销：目录变动会有语义后果，路由表必须持续保持最新。

### 持久记忆加定时刷新

- README 描述了一套三层记忆结构，包含被动的全局规则、主动检索的观察，以及通过周期任务不断累积的观察和反思。
- `periodic_jobs/ai_heartbeat/` 子树是第一版最强的证据，说明这个仓库把记忆维护当成运行闭环，而不只是一次性的 prompt engineering 技巧。
- 代价在于：它的有效性依赖持续、纪律化的数据收集与 cron 式维护，而不是只靠 clone 仓库。

## 证据锚点

- Snapshot 来源：[github-repo-grapeot-context-infrastructure.md](../../../raw/external/github-repo-grapeot-context-infrastructure.md)
- 仓库：`grapeot/context-infrastructure`
- 观察分支：`main`
- 解析到的 commit：`d24b4bbf98ccbdecef7c3a4c40224084457c5640`

- `AGENTS.md`
- `README.md`

## 开放问题

- 围绕当前研究主题，哪些实现文件承载了主要运行路径？
- README 的叙述与代码、CI 真正执行的路径之间，哪里开始出现偏差？
- 这个系统里究竟有多少是可执行自动化，多少只是文档与参考结构？
- `periodic_jobs/ai_heartbeat/` 下到底哪些文件真的会把内容写回 `contexts/memory/OBSERVATIONS.md` 这类记忆面？

## 来源依据

- [仓库 snapshot](../../../raw/external/github-repo-grapeot-context-infrastructure.md)

## 相关页面

- [代码库作为知识来源](../agent-harness-runtime/codebases-as-knowledge-sources.md)
- [Harness Engineering（约束壳工程）](../agent-harness-runtime/harness-engineering.md)
- [本地知识库模式](local-knowledge-base-patterns.md)
- [知识库运行模型](knowledge-base-operating-model.md)
