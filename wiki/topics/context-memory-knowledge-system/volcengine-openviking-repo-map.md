# volcengine/openviking 仓库地图

## 摘要

这页是 `volcengine/openviking` 的第一版仓库地图，观察主题是“面向 AI Agent 的 context database 架构与工程实践”。

`OpenViking` 的核心不是把传统 RAG 包一层 API，而是把 agent 需要的 resources、user memory、agent memory、skills、sessions 统一进 `viking://` 虚拟文件系统。它用类似文件系统的 `ls/tree/read/find/grep` 交互范式，让 agent 先定位目录、读摘要、再按需读全文；同时通过 session commit 把对话、工具使用和任务经验回写成长期记忆。

当前置信度是中等：README、配置文档、session 文档、server 启动层、FastAPI app、storage/native engine loader、Python/Rust CLI、bot README 和 CI/打包脚本已经读过，足够形成机制地图；但 retrieval 具体实现、AGFS/RAGFS 底层、每个 router 的权限语义和 multi-tenant 细节仍需后续定向深读。

## 仓库目的

- 公开定位：面向 AI Agents 的开源 context database，用文件系统范式统一管理 memory、resources 和 skills，支持分层 context delivery 与 self-evolving。
- 实际架构定位：一个 context runtime。底层包含 storage、vector engine、AGFS/RAGFS/native extension；中层是 HTTP server 与 Python SDK；上层是 Rust CLI、server bootstrap、Vikingbot 和多种 agent/channel 集成。
- 主要目标：降低 agent 长任务中的 context 爆炸、检索黑盒、记忆无法迭代、资源/技能/记忆分散管理等问题。
- 观察分支：`main`
- 解析到的 commit：`39b124d037ff7f2f6ecc4cab7560a359468fd641`
- 主要语言：`Python`
- 仓库地址：https://github.com/volcengine/openviking

## 架构地图

### 顶层结构

- `openviking/`: Python 核心包，包含 server、service、storage、metrics、telemetry、console、providers、resources、sessions 等运行时模块。
- `openviking_cli/`: Python CLI 入口与配置、doctor/init/bootstrap 工具。`openviking-server` 从这里进入，`ov/openviking` 则主要转发到 Rust CLI。
- `crates/ov_cli/`: Rust CLI。承载高频交互命令，包括 data、search、chat、admin、observer、TUI 等命令组。
- `bot/`: Vikingbot。基于 Nanobot，给 OpenViking 加 chat channel、agent tools、MCP tools、sandbox、自动 session memory commit 等能力。
- `src/`: native/vector engine 相关源码，与 `setup.py`、CMake、wheel 打包链路配合。
- `docs/`: 概念、配置、quickstart、部署、API 等文档。
- `benchmark/`: 效果评测与对照实验材料。
- `.github/workflows/`: build、lint、test、publish、API test、Docker image、docs deploy 等 CI/CD 工作流。
- `docker/`、`deploy/`、`docker-compose.yml`、`Dockerfile`: 服务化部署和容器入口。

### 主要执行面

`openviking-server` 通过 `openviking/server/bootstrap.py` 启动。它读取 `ov.conf`，初始化全局 config，检测 Ollama，本地启动 Uvicorn；如果启用 bot，会先检查 bot gateway 端口，避免旧进程仍在服务，然后启动 `vikingbot gateway` 子进程。

HTTP 服务由 `openviking/server/app.py` 创建。它在 lifespan 中初始化 `OpenVikingService`、`APIKeyManager`、metrics/tracing/logging、task tracker 和 MCP session manager，然后注册 filesystem、resources、search、sessions、tasks、admin、bot、webdav、observer、metrics 等 router。

CLI 有两层：Python package 暴露 `ov/openviking/openviking-server` 入口；其中 `ov/openviking` 是极薄 Python wrapper，优先处理少量 Python-native 子命令，然后查找开发环境、wheel 内置或 PATH 中的 Rust `ov` 二进制并执行。Rust CLI 负责真正的文件式 context 操作和交互式命令。

Vikingbot 是 agent-facing 表面。它提供 7 个 OpenViking tools，包括 read、list、search、add_resource、grep、glob、memory_commit，并把 L0/L1/L2 内容访问、session 自动提交、chat channels、MCP servers 和 sandbox/FUSE/OpenCode 等可选能力接到同一个 bot 配置里。

### MCP 交互面

OpenViking server 内置 MCP endpoint，不需要额外启动一个 MCP 进程。`openviking/server/app.py` 在同一个 FastAPI app 上挂载 `/mcp`，支持 `GET`、`POST`、`DELETE`，文档说明它与 REST API 共用同一进程和端口，默认是 `http://<server>:1933/mcp`。

MCP server 本体在 `openviking/server/mcp_endpoint.py`。它使用 `FastMCP("openviking")` 和 streamable HTTP transport，把 OpenViking 的 context 操作暴露成 9 个 MCP tools：`search`、`read`、`list`、`store`、`add_resource`、`grep`、`glob`、`forget`、`health`。

这一层是 thin adapter。每个 MCP tool 都调用已有 `OpenVikingService` 能力，而不是另写一套业务逻辑：`search` 调 `service.search.find`，`read/list/grep/glob/forget` 调 `service.fs.*`，`add_resource` 调 `service.resources.add_resource`，`store` 创建临时 session 并 `commit_async` 触发 memory extraction。

MCP 鉴权复用 REST API 的身份体系。`_IdentityASGIMiddleware` 调用 `resolve_identity`，读取 `X-Api-Key` 或 `Authorization: Bearer ...`，也支持 `X-OpenViking-Account`、`X-OpenViking-User`、`X-OpenViking-Agent`。解析后的 `RequestContext` 通过 contextvar 传给各个 MCP tool，因此 MCP 和 REST 共享 account/user/agent namespace、role 与 namespace policy。

OpenViking 还有反方向的 MCP client 能力。`bot/vikingbot/agent/tools/mcp.py` 让 Vikingbot 连接外部 MCP servers，再把外部工具包装成 `mcp_<server>_<tool>` 形式的 native tools。也就是说：OpenViking server 可以作为 MCP server 给 Claude Code、Codex、Manus、Trae 等客户端用；Vikingbot 也可以作为 MCP client 消费外部工具。

## 机制清单

### `viking://` 虚拟文件系统范式

- 控制什么：把 resources、user memory、agent memory、skills、sessions 统一成可浏览、可定位、可读取的 URI 树。
- 补偿的失败模式：传统 RAG 把 context 打平成 chunks，agent 无法知道信息的层级、来源和相邻上下文，只能依赖黑盒相似度。
- 证据位置：`README.md`、`docs/en/concepts/08-session.md`、`crates/ov_cli/src/main.rs`、`bot/README.md`。
- 代价：系统必须维护目录语义、URI 规范、权限边界、索引一致性和多租户命名空间。它比“单表向量检索”重得多。

### L0/L1/L2 分层 context loading

- 控制什么：写入资源或提交 session 后，生成 `.abstract.md`、`.overview.md` 和可按需读取的原文/详情层。
- 补偿的失败模式：agent 一次性塞入大量原文会浪费 token，也容易引入噪音；只保留短摘要又会丢失需要深读的证据。
- 证据位置：`README.md`、`docs/en/concepts/08-session.md`、`bot/README.md`、Rust CLI 的 `abstract`、`overview`、`read` 命令。
- 代价：摘要质量会成为系统正确性的上游变量。写入成本也更高，因为每个资源和 session 都需要额外加工。

### Directory recursive retrieval

- 控制什么：先用检索定位高相关目录，再在目录内部细化探索，并递归向下收窄范围。
- 补偿的失败模式：单次向量搜索只找“相似片段”，不理解片段所在目录和上下游结构，复杂查询容易缺全局视角。
- 证据位置：`README.md` 的 core concepts 与 `find/search/grep/tree` 命令设计。
- 代价：检索路径变长，系统需要记录和解释 retrieval trajectory。后续要深读具体实现，确认目录递归、语义检索和规则检索如何合流。

### Session commit 与 memory self-iteration

- 控制什么：session 记录 messages、used contexts、used skills 和 tool calls；`commit()` 后先同步归档，再异步总结并抽取长期 memory。
- 补偿的失败模式：agent 每次任务结束后经验消失，用户偏好、工具经验、失败案例无法结构化复用。
- 证据位置：`docs/en/concepts/08-session.md`。
- 代价：memory extraction 引入 LLM 判断、去重、合并、删除冲突等复杂链路。错误记忆会成为长期污染源，所以需要后续关注审计、回滚和可见性。

### Server auth mode 与安全启动门

- 控制什么：server 支持 `dev`、`api_key`、`trusted` 三种认证模式，并在非 localhost 场景阻止不安全配置启动。
- 补偿的失败模式：context database 一旦暴露网络，未经认证的 ROOT 身份或可信 header 模式会变成高风险入口。
- 证据位置：`openviking/server/config.py`、`openviking/server/app.py`。
- 代价：配置复杂度上升。`trusted` 模式要求外部 gateway 真的可信，`api_key` 模式还要处理 key 存储、hashing 与 encryption 的组合语义。

### FastAPI service runtime

- 控制什么：把 context database 服务化，暴露 filesystem、resource、search、session、task、admin、bot、webdav、observer、metrics 等 API。
- 补偿的失败模式：只作为本地库时，多个 agent、CLI、bot、远端 client 难以共享同一份 context runtime。
- 证据位置：`openviking/server/app.py`、`openviking/server/bootstrap.py`、`docs/en/getting-started/03-quickstart-server.md`。
- 代价：长期服务需要处理 auth、CORS、observability、task cleanup、MCP lifespan、shutdown、multi-worker 和部署边界。

### Python package + Rust CLI 双层入口

- 控制什么：Python 包负责发行与配置兼容，Rust CLI 负责高频命令和 TUI 交互。
- 补偿的失败模式：纯 Python CLI 启动慢，纯 Rust CLI 又不容易和 Python wheel、server bootstrap、native extension 打包链路自然合流。
- 证据位置：`openviking_cli/rust_cli.py`、`crates/ov_cli/src/main.rs`、`pyproject.toml`、`.github/workflows/_build.yml`、`setup.py`。
- 代价：构建发布链路明显变重。wheel 需要打包 Rust `ov` 二进制、C++/native vector engine、AGFS/RAGFS 组件，并覆盖 Linux/macOS/Windows 与多 CPU variant。

### Native vector engine loader

- 控制什么：根据平台和 CPU capability 动态选择 `x86_sse3`、`x86_avx2`、`x86_avx512` 或 `native` 后端，也允许用 `OV_ENGINE_VARIANT` 强制指定。
- 补偿的失败模式：向量检索底层性能和平台兼容性难以只靠纯 Python 实现。
- 证据位置：`openviking/storage/vectordb/engine/__init__.py`、`setup.py`、`.github/workflows/_build.yml`。
- 代价：wheel 构建、ABI、Windows DLL 搜索、CPU feature detection 都会成为维护点。仓库用 lazy import 和 missing symbol proxy 降低导入期失败的破坏面。

### Ollama setup 与本地模型 preflight

- 控制什么：启动 server 前检测配置是否使用 Ollama，并在本地场景尝试确保 Ollama 正在运行。
- 补偿的失败模式：本地模型配置看似完成，但 server 启动后 embedding/VLM 调用才失败。
- 证据位置：`openviking_cli/utils/ollama.py`、`openviking/server/bootstrap.py`、`docs/en/guides/01-configuration.md`。
- 代价：它只负责 ensure running，不负责停止服务。这个选择尊重 Ollama 作为共享服务的现实，但也意味着 OpenViking 不完全拥有模型进程生命周期。

### Vikingbot 作为 agent 工作面

- 控制什么：把 OpenViking 的 context 操作变成 agent tools，并接入 chat channels、MCP servers、sandbox、FUSE、OpenCode 等能力。
- 补偿的失败模式：context database 如果只暴露 API/CLI，agent 仍需要额外 glue code 才能把记忆、资源、技能和外部工具编排进日常对话。
- 证据位置：`bot/README.md`、`pyproject.toml`。
- 代价：bot 层会把身份、channel 权限、工具 allowlist、MCP server 连接、sandbox 隔离和 memory commit 混在一起。它提升可用性，也扩大治理面。

### MCP endpoint 作为标准 agent 接口

- 控制什么：把 OpenViking 的 context database 能力通过标准 MCP streamable HTTP 暴露给外部 agent/client。
- 补偿的失败模式：如果只有 REST API/CLI，每个 agent runtime 都要自己写 adapter；MCP 让 Claude Code、Codex、Manus、Trae 等 MCP client 可以用同一套 tool schema 访问 OpenViking。
- 证据位置：`openviking/server/mcp_endpoint.py`、`openviking/server/app.py`、`docs/en/guides/06-mcp-integration.md`、`tests/server/test_mcp_endpoint.py`。
- 代价：MCP 是更宽的暴露面，尤其是 `store`、`add_resource`、`forget` 这类写操作。它必须复用 REST API 的 auth、account/user/agent identity 与 namespace policy，否则会变成绕过权限边界的旁路。

### MCP-to-skill 与外部工具接入

- 控制什么：一方面把 OpenViking 暴露给外部 MCP clients；另一方面让 Vikingbot 消费外部 MCP servers，并把 MCP tool definition 转成 OpenViking skill 形态。
- 补偿的失败模式：agent 工具生态如果只存在于某个运行时里，难以沉淀和复用；把 MCP tool 转成 skill 可以把“可调用工具”变成“可描述、可检索、可治理的能力资产”。
- 证据位置：`bot/vikingbot/agent/tools/mcp.py`、`openviking/core/mcp_converter.py`。
- 代价：MCP tool schema 到 OpenAI/tool schema/skill markdown 的转换会丢失一部分语义。Vikingbot 代码只规范化 nullable schema，说明这里更偏实用接入，而不是完整语义建模。

### CI/CD 与多平台发行

- 控制什么：通过 GitHub Actions 构建 sdist、wheel、Rust CLI、Docker image、docs、API tests、CodeQL、lint 与 publish。
- 补偿的失败模式：Python + Rust + C++ native extension + Docker + docs 的多语言仓库很容易出现“本地能跑、发行不可用”的漂移。
- 证据位置：`.github/workflows/_build.yml`、`_test_lite.yml`、`_test_full.yml`、`api_test.yml`、`api_test_effect.yml`、`_publish.yml`、`build-docker-image.yml`。
- 代价：CI 本身复杂，且 snapshot 显示不少工作流里有平台分支、临时跳过、测试忽略列表和构建清理逻辑。后续要区分哪些是硬质量门，哪些只是发布辅助。

## 证据锚点

- Snapshot 来源：[github-repo-volcengine-openviking.md](../../../raw/external/github-repo-volcengine-openviking.md)
- 仓库：`volcengine/openviking`
- 观察分支：`main`
- 解析到的 commit：`39b124d037ff7f2f6ecc4cab7560a359468fd641`
- README 与文档：`README.md`、`docs/en/guides/01-configuration.md`、`docs/en/concepts/08-session.md`、`docs/en/getting-started/03-quickstart-server.md`
- Server：`openviking/server/bootstrap.py`、`openviking/server/app.py`、`openviking/server/config.py`
- Storage/native：`openviking/storage/__init__.py`、`openviking/storage/vectordb/engine/__init__.py`、`setup.py`
- CLI：`openviking_cli/rust_cli.py`、`openviking_cli/server_bootstrap.py`、`openviking_cli/utils/config/config_loader.py`、`openviking_cli/utils/ollama.py`、`crates/ov_cli/src/main.rs`
- Bot：`bot/README.md`、`pyproject.toml` 的 `bot*` optional dependencies
- MCP：`openviking/server/mcp_endpoint.py`、`docs/en/guides/06-mcp-integration.md`、`docs/zh/guides/06-mcp-integration.md`、`bot/vikingbot/agent/tools/mcp.py`、`openviking/core/mcp_converter.py`、`tests/server/test_mcp_endpoint.py`
- CI/CD：`.github/workflows/_build.yml`、`.github/workflows/_lint.yml`、`.github/workflows/_test_lite.yml`、`.github/workflows/_test_full.yml`、`.github/workflows/api_test.yml`、`.github/workflows/api_test_effect.yml`、`.github/workflows/_publish.yml`

## 开放问题

- AGFS/RAGFS 的真实数据模型、事务语义、锁策略和失败恢复还没有深读。
- `filesystem_router`、`resources_router`、`search_router`、`sessions_router` 的具体 API 权限边界需要定向确认。
- Directory recursive retrieval 的实现细节还停留在 README 级别，需要补读 search/service/storage 代码。
- multi-tenant 下 account/user/agent_id 如何映射到 `viking://agent/{agent_id}/user/{user_id}/...` 仍需读 identity、namespace policy 与 API key manager。
- memory extraction 的 dedup/merge/delete 决策如何审计和回滚，是后续判断它能否承载长期 self-evolving 的关键。
- MCP endpoint 文档写 9 个 tools，而 `app.py` 注释仍写“5 tools”，应是旧注释；`tests/server/test_mcp_endpoint.py` 里 `list_dir` 导入与当前 endpoint 中 `ls` 函数名也有命名漂移迹象，需确认 CI 中的真实状态。
- Bot 层外部 MCP tools、sandbox、channel identity 与 OpenViking account/user 的映射关系还需要继续看。
- README 中 OpenClaw + OpenViking 的效果数据值得保留为产品论证线索，但还不能当作已复现实验结论。

## 可迁移判断

`OpenViking` 最值得学习的是把 agent context 从“检索接口”升级成“可浏览的上下文文件系统”。它让 agent 不只问“哪些 chunk 相似”，而是先知道自己处在哪个 context namespace、哪个目录、哪一层摘要，以及是否需要继续深读。

这和本知识库的 `raw -> wiki` 分层有天然呼应：两者都把原文、摘要、索引、使用路径分开，只是 `OpenViking` 更偏 runtime 和 agent tool surface，而本仓库更偏人可维护的知识资产。后续可以把它作为 [AI Architect 的 Context Intelligence 镜头](../ai-product-product-definition/ai-architect-context-intelligence.md)、[AI 知识系统的产品定义信念](ai-knowledge-systems-product-definition-beliefs.md)、[本地知识库模式](local-knowledge-base-patterns.md) 的重要对照样本。

## 来源依据

- [仓库 snapshot](../../../raw/external/github-repo-volcengine-openviking.md)

## 相关页面

- [AI Architect 的 Context Intelligence 镜头](../ai-product-product-definition/ai-architect-context-intelligence.md)
- [AI 知识系统的产品定义信念](ai-knowledge-systems-product-definition-beliefs.md)
- [本地知识库模式](local-knowledge-base-patterns.md)
- [代码库作为知识来源](../agent-harness-runtime/codebases-as-knowledge-sources.md)
- [openclaw/openclaw 仓库地图](../agent-harness-runtime/openclaw-openclaw-repo-map.md)
