# safety-research/automated-w2s-research 仓库地图

## 摘要

这页是围绕主题“自动化 alignment research harness 与 weak-to-strong 监督”维护的 `safety-research/automated-w2s-research` 第一版仓库地图。

从 README、`pyproject.toml` 与顶层结构看，这个仓库并不是一个泛用 agent 框架，而是一套为 weak-to-strong research 定制的研究操作环境：它把数据集、baseline、自动化研究者、评测 API、Web dashboard、Docker / RunPod 执行面收束在同一个 repo 里。

当前置信度仍停留在“架构地图 + 机制初判”层，而不是“关键实现已逐文件读透”层。但它已经足够回答一个更重要的问题：这个项目真正想优化的，不只是模型训练，而是**让自动化研究在一个可判分、可隔离、可并行、可共享发现的环境里持续 hill-climb**。

## 仓库目的

- README 的显式定位是：发布一个 automated weak-to-strong research sandbox，附带数据集、baseline 与 baseline automated researcher。
- 从仓库结构看，它实际承载了两层东西：
  - 一层是 weak-to-strong supervision 的实验环境与 baseline 实现。
  - 另一层是一个面向研究任务的 agent harness：提出想法、实现、训练、通过 server API 拿回 `PGR`、共享 findings、横向比较结果。
- 观察时默认分支：`main`
- 主要语言：`Python`
- 仓库地址：https://github.com/safety-research/automated-w2s-research

## 架构地图

### 顶层目录

- `.claude`
- `.github`
- `scripts`
- `w2s_research`

### 顶层文件

- `.dockerignore`
- `.gitignore`
- `.gitmodules`
- `Dockerfile`
- `Idea.md`
- `README.md`
- `cache_results.tar.gz`
- `labeled_data.tar.gz`
- `entrypoint.sh`
- `pyproject.toml`
- `run.py`
- `run.sh`
- `uv.lock`

### 第一版子系统角色判断

- `run.py` 是统一入口。README 明确把 baseline 运行、server 启动与 agent 工作流都收束到这个入口下。
- `w2s_research/core/` 是共享训练层，承载训练、评测、数据加载、配置与推理工具。
- `w2s_research/ideas/` 是实验插件层。每个方法以目录形式存在，并通过 `TEMPLATE` 降低新 idea 的接入成本。
- `w2s_research/research_loop/` 是自动化研究层，包含 agent loop、prompt 与 MCP tools。
- `w2s_research/web_ui/backend/` 是 orchestration surface：实验管理、leaderboard、findings forum、评测 API 都经由这里暴露。
- `w2s_research/infrastructure/` 是执行与部署层，把本地 Docker、RunPod 与 S3 artifact 流程接起来。

### 执行流的第一版理解

1. 人或 agent 通过 `run.py` / dashboard 启动实验。
2. 训练与推理由 `core/` 提供统一能力。
3. 具体方法从 `ideas/` 中选取或新建。
4. AAR 在 `research_loop/` 中提出想法、调用工具、提交预测。
5. `web_ui/backend/` 持有实验队列、评测 API、结果面板与 findings forum。
6. 如果需要隔离或扩容，则通过 Docker / RunPod 执行，并借助 S3 交换数据、结果与共享 artifacts。

## 机制清单

### 用“隐藏标签 + 远程评测 API”把开放研究任务改写成 outcome-gradable 环境

- README 明确说明，agent 在 sandbox 内只看到去标签后的 `data/`，真实标签保留在 server 侧，通过 evaluation API 返回 `PGR`。
- 这个机制控制的是“研究 agent 既要能自主试验，又不能直接读取 ground truth”的失败模式。
- 它让 weak-to-strong research 从开放式讨论变成一个可以 hill-climb 的外部反馈环境。
- 代价是，一旦 API 反馈足够稳定，系统就必须面对 reward hacking 与 test-set gaming。

### 用 `ideas/` 目录和 `TEMPLATE` 把研究方法做成可插拔实验单元

- README 把“创建自己的 idea”设计成复制 `w2s_research/ideas/TEMPLATE`、实现 `run.py`、返回 metrics 的流程。
- 这控制的是“每次尝试新方法都要重搭训练管线”的重复劳动，也让人工 baseline 与 agent 提案落在同一接口上。
- 代价是所有方法天然被压进同一 `RunConfig` 与 shared training stack 里，探索空间会被这套接口边界塑形。

### 用三种执行模式在“调试速度、隔离强度、并行规模”之间切换

- README 显式区分 Local、Local Docker、RunPod 三种模式。
- 这控制的是研究任务里常见的三难：
  - 本地调试需要快
  - 正式实验需要隔离，避免直接看到 `labeled_data`
  - 大规模并行需要云端调度与 artifact 同步
- 代价是系统复杂度显著上升。仓库不只是一个训练 repo，还必须同时维护容器镜像、云执行与存储路径。

### 用 dashboard 把实验管理、评测、排行榜与 findings forum 收束到同一工作面

- `run.py server --port 8000` 启动的 Flask server 不只是一个薄 API，而是整个研究 harness 的控制台。
- 它控制的是多 agent 运行时最容易散掉的几个面：谁在跑、结果如何、哪些发现值得共享、哪个想法暂时领先。
- 代价是 repo 的核心逻辑不再只在训练代码里，还分散到 Web / server orchestration 层。

### 用“隔离 sandbox + 共享 findings / codebase snapshot”平衡独立探索与交叉授粉

- README 说明 AAR 在隔离环境中工作，但 findings 与 codebase snapshot 会在 worker 之间同步。
- 这控制的是两种相反失败模式：
  - 完全隔离会让每个 agent 重复踩坑
  - 完全共享会让探索过快收敛到少数路径
- 这个设计对齐论文里“维持探索分布”的目标。它的代价是共享面本身也可能成为信息污染或过早收敛的来源。

### 用统一依赖栈把训练、agent、server 与云执行压进同一个可复现实验环境

- `pyproject.toml` 把 ML 训练、Claude Agent SDK、Flask、RunPod、S3、tracking 工具放在同一个 Python 项目里。
- 这控制的是“研究代码、agent 代码、部署代码分裂导致环境不一致”的失败模式。
- 代价是依赖很重，环境构建和冲突管理本身就成为工程问题；`uv` override 也说明这里已经开始补偿生态冲突。

## 证据锚点

- Snapshot 来源：[github-repo-safety-research-automated-w2s-research.md](../../../raw/external/github-repo-safety-research-automated-w2s-research.md)
- 仓库：`safety-research/automated-w2s-research`
- 观察分支：`main`
- 解析到的 commit：`79a0562fa1a2c246048ed7c009f3684907987b05`

值得回查的关键文件与路径：

- `README.md`
- `run.py`
- `Idea.md`
- `pyproject.toml`
- `Dockerfile`
- `w2s_research/core/train.py`
- `w2s_research/core/eval.py`
- `w2s_research/core/config.py`
- `w2s_research/ideas/TEMPLATE/run.py`
- `w2s_research/research_loop/agent.py`
- `w2s_research/research_loop/prompt.jinja2`
- `w2s_research/research_loop/tools/`
- `w2s_research/web_ui/backend/`
- `w2s_research/infrastructure/runpod.py`
- `w2s_research/infrastructure/execute_autonomous.py`
- `.github/workflows/docker-image.yml`

## 开放问题

- `research_loop/agent.py` 里的 agent autonomy 到底有多厚？它更像一个自由探索 loop，还是一个被 tool contract 强约束的研究 worker？
- findings forum 与 codebase snapshot 的共享频率、触发条件与检索方式具体如何实现？这会直接影响“探索分布 vs 熵坍缩”的平衡。
- server 侧如何防止 evaluation API 被策略性 probing？论文已暴露 reward hacking，但 repo 中的防护边界需要更细读。
- `web_ui/backend/` 到底只是 orchestration glue，还是已经承载了研究状态机与任务队列等更厚控制逻辑？
- Local / Docker / RunPod 三种模式在代码里是否共用同一实验契约，还是已经开始出现分叉实现？

## 来源依据

- [仓库 snapshot](../../../raw/external/github-repo-safety-research-automated-w2s-research.md)
- [Automated Weak-to-Strong Researcher](automated-weak-to-strong-researcher.md)

## 相关页面

- [Automated Weak-to-Strong Researcher](automated-weak-to-strong-researcher.md)
- [AI 自演化研究 Harness](ai-self-evolution-research-harnesses.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
- [代码库作为知识来源](codebases-as-knowledge-sources.md)
