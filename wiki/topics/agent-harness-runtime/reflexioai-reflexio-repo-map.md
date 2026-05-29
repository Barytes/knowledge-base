# ReflexioAI/reflexio 仓库地图

## 摘要

Reflexio 是一个 **AI Agent 自我改进平台**，核心价值是将 Agent 与用户的每一次对话转化为学习机会——自动提取用户偏好（User Profiles）和行为规范（Playbooks），让 Agent 持续改进而无需手动调优。

当前版本 `0.2.9`，采用 FastAPI 后端 + Python SDK + CLI 的架构，支持 SQLite（默认）和 Supabase PostgreSQL 存储。

## 仓库目的

- **公开定位**：AI Agent 自我改进平台——从对话中自动提取用户偏好和行为规范
- **核心价值主张**：
  - 不重复犯错：将用户纠正转化为决策改进
  - 锁定有效策略：持久化成功的策略和工作流
  - 实时纠正：检索个性化和操作信号，无需重新训练
  - 向专家学习：对比 Agent 回复与专家理想回复，自动提取可执行的 playbook
- **主要语言**：Python 3.12+
- **仓库地址**：https://github.com/ReflexioAI/reflexio
- **观察分支**：`main`
- **解析到的 commit**：`7df1a50188a241c6fb7d5ac10803646610639f8a`

## 架构地图

### 顶层目录

```
reflexio/
├── reflexio/              # 主 Python 包
│   ├── client/            # ReflexioClient 实现（轻量级客户端）
│   ├── cli/               # 命令行接口
│   ├── data/              # 数据存储 / fixtures
│   ├── integrations/      # LLM 和外部集成
│   ├── lib/               # 核心库函数（Reflexio 门面）
│   ├── models/            # 数据模型和 API schemas
│   │   └── api_schema/    # API 请求/响应 schemas
│   ├── server/            # FastAPI 后端
│   │   ├── api_endpoints/ # 路由处理器
│   │   ├── services/      # 业务逻辑和存储
│   │   ├── llm/           # LLM provider 集成
│   │   ├── prompt/         # Prompt 模板
│   │   └── site_var/      # 站点配置
│   └── test_support/      # 测试工具
├── docs/                  # Next.js 16 文档前端（ShadCN UI）
├── tests/                 # 测试套件（pytest）
├── scripts/               # 工具脚本（如 reset_db.py）
├── client_dist/           # 轻量级客户端分发包
└── notebooks/             # Jupyter notebooks（示例、快速入门）
```

### 核心架构流程

```
Client (SDK / CLI / Web UI)
  → FastAPI Backend (server/api.py)
    → Reflexio Orchestrator (lib/reflexio_lib.py)
      → GenerationService
        ├─ ProfileGenerationService  → ProfileExtractor(s) → Deduplicator → Storage
        ├─ PlaybookGenerationService → PlaybookExtractor(s) → Deduplicator → Storage
        └─ GroupEvaluationScheduler  → Evaluator(s) → Storage（延迟 10 分钟）
```

### 服务端口与存储

| 服务 | 框架 | 默认端口 | 环境变量 |
|------|------|----------|----------|
| Backend | FastAPI (uvicorn) | 8081 | `BACKEND_PORT` |
| Docs | Next.js 16 | 8082 | `DOCS_PORT` |

存储后端：`--storage sqlite`（默认）或 `--storage supabase`

## 核心洞察：Personal Agent vs Vertical Agent 的分离设计

Reflexio 通过 **两层分离架构** 同时满足两类 Agent 的自进化需求：

| 层级 | 机制 | 适用 Agent 类型 | 存储组织 |
|------|------|-----------------|----------||
| User Profiles | 个人偏好提取 | Personal agent | per-user |
| User Playbooks | 行为规范提取（原始） | Personal agent | per-user |
| Agent Playbooks | 行为规范聚合（泛化） | **Vertical agent** | per-agent_version |

**关键区分**：
- **Profile** 回答"这个用户喜欢什么"
- **User Playbook** 回答"从这个用户身上学到了什么行为规范"
- **Agent Playbook** 回答"这类任务应该怎么做"（跨用户共享）

## 跨用户共享机制

### 数据存储架构

Reflexio 采用**集中式存储**架构（SQLite 或 Supabase PostgreSQL）：

所有用户数据统一存储在同一后端，**不是每个用户本地存储再同步**。

### 跨用户共享流程

```
User A 对话 → UserPlaybook 提取 → 存入中央 Storage
User B 对话 → UserPlaybook 提取 → 存入中央 Storage
                    ↓
            PlaybookAggregator 获取所有 UserPlaybooks
                    ↓
            Embedding + Clustering 聚类
                    ↓
            LLM 聚合生成 AgentPlaybook
                    ↓
            User C 使用时检索 AgentPlaybook（受益于 A、B 的学习）
```

## Playbook 聚合逻辑详解

### 聚合触发条件

当新 UserPlaybook 数量 >= `reaggregation_trigger_count`（默认 2）时触发聚合。

### 聚合流程

**Step 1: 获取所有 UserPlaybooks**
- 从存储中获取指定 `playbook_name` 和 `agent_version` 的所有 UserPlaybooks
- 包含 trigger 字段的 embedding

**Step 2: Embedding 聚类**
- 提取 embeddings（基于 trigger 字段）
- 计算 cosine distance matrix
- 选择聚类算法：< 50 条用 Agglomerative，>= 50 条用 HDBSCAN
- 过滤小于 `min_cluster_size` 的聚类

**Step 3: 检测聚类变化（增量聚合）**
- 计算 cluster fingerprint（SHA-256 hash of sorted user_playbook_ids）
- 比较当前 fingerprint 与上次存储的 fingerprint
- 只对变化的聚类调用 LLM（跳过未变化的）

**Step 4: LLM 聚合每个聚类**
- 格式化聚类内容（区分单一方向 vs 多方向冲突）
- 调用 LLM 聚合，检查是否与 existing_approved_playbooks 重复
- 输出 AgentPlaybook（包含 trigger/instruction/pitfall）

### 方向分组与冲突处理

当聚类内存在"冲突方向"时，使用 token overlap 分组：
- 按 instruction + pitfall 的相似度分组
- Greedy single-linkage 算法
- 返回按组大小降序排列（largest first）
- LLM 应用 majority-wins 处理冲突

### AgentPlaybook 输出结构

```python
class StructuredPlaybookContent:
    trigger: str | None      # 触发条件
    instruction: str | None  # 应该做什么
    pitfall: str | None      # 应该避免什么
    rationale: str | None    # 推理依据
    blocking_issue: ...      # 阻塞问题（可选）
    content: str             # 自然语言总结
```

### Embedding 聚类 vs LLM 聚合的分工

两步聚类的核心分工不同：

| 步骤 | Embedding 聚类 | LLM 聚合 |
|------|---------------|----------|
| **功能** | **语义分组** | **内容合成** |
| 输入 | UserPlaybooks embeddings | Cluster 内的 UserPlaybooks 内容 |
| 输出 | Cluster ID（哪些条目是一类） | AgentPlaybook（这类事应该怎么做） |
| 技术点 | Cosine distance + HDBSCAN | 结构化输出 + 冲突处理 + 去重 |

**Embedding 聚类解决"哪些条目是一类事"，LLM 聚合解决"这类事应该怎么做"。"

#### LLM 聚合的 5 个作用

**1. 结构化提炼**：将自由文本提炼成 SOP 格式

```
用户原始表达:
- "部署时别用 us-east-1，我们公司规定只能用 us-west-2"
- "上次部署错了区域，出事故了，以后先确认区域再动手"
- "部署前一定要问清楚目标区域"

→ LLM 提炼:
trigger: "执行部署操作时"
instruction: "先确认目标区域再执行"
pitfall: "未确认区域直接部署"
```

**2. 合并相似条目**：不同表达方式但意思相同 → 一个简洁表述

**3. 处理冲突（Majority-wins）**：当 cluster 内存在矛盾建议时，按多数意见输出

```
User A/C/D: "部署用蓝绿部署"（3 人）
User B: "部署用滚动更新"（1 人）

→ LLM 输出: "使用蓝绿部署策略"
```

**4. 去重检查**：与 `existing_approved_playbooks` 比较，避免生成重复，返回 None 表示跳过

**5. 生成可执行指令**：从"用户说的内容"转化为"agent 应该怎么做"

| 用户原始表达 | LLM 提炼后 |
|-------------|-----------|
| "别用 us-east-1" | "确认目标区域为 us-west-2" |
| "上次忘了问区域" | "部署前询问目标区域" |
| "我讨厌重复问问题" | "记住用户偏好，避免重复确认" |

## 机制清单

### 1. Profile Generation（用户画像生成）

**位置**：`reflexio/server/services/profile/`

**核心组件**：
- `profile_generation_service.py` — Profile 生成服务主逻辑
- `profile_extractor.py` — 从对话中提取用户偏好的提取器
- `profile_deduplicator.py` — 去重机制

**功能**：
- 使用可配置的提取器从对话中提取行为画像
- 支持版本管理（current → pending → archived）
- 多个提取器并行运行，拥有独立的窗口和步长

### 2. Playbook Extraction & Aggregation（行为规范提取与聚合）

**位置**：`reflexio/server/services/playbook/`

**核心组件**：
- `playbook_generation_service.py` — Playbook 生成服务主逻辑
- `playbook_extractor.py` — 从用户行为模式中提取 playbook
- `playbook_aggregator.py` — 聚合相似条目（使用 LLM + 变更检测跳过未变更集群）
- `playbook_deduplicator.py` — 去重机制

**功能**：
- 聚类相似条目并用 LLM 聚合
- 变更检测跳过未变更集群
- 审批工作流：review and approve/reject agent playbooks

### 3. Expert Learning（专家学习）

**机制**：
- 通过 `expert_content` 字段发布专家理想回复
- 自动对比 Agent 回复与专家回复
- 聚焦实质性差异（缺失信息、错误方法、推理差距），忽略风格差异
- 生成可执行的 playbook（trigger/instruction/pitfall SOPs）

### 4. Agent Success Evaluation（Agent 成功评估）

**位置**：`reflexio/server/services/agent_success_evaluation/`

**核心组件**：
- `agent_success_evaluation_service.py` — 评估服务
- `agent_success_evaluator.py` — 评估器实现
- `delayed_group_evaluator.py` — 延迟评估调度器（10 分钟后触发）
- `group_evaluation_runner.py` — 分组评估运行器

**功能**：
- Session 级别评估（最后请求后 10 分钟自动触发）
- Shadow comparison 模式：A/B 测试常规 vs shadow agent 回复
- 工具使用分析检测阻塞问题

### 5. Search & Retrieval（搜索与检索）

**位置**：`reflexio/server/services/unified_search_service.py`

**功能**：
- 混合搜索（向量 + 全文）覆盖 profiles 和 playbooks
- LLM 驱动的查询重写提高召回率
- 并行统一搜索所有实体类型
- **性能指标**：~3,000 行索引数据，p50 57ms / p95 73ms（本地 SQLite，Apple Silicon MacBook）

### 6. Storage Layer（存储层）

**位置**：`reflexio/server/services/storage/`

**架构**：
```
storage/
├── storage_base/         # 抽象基类
├── sqlite_storage/       # SQLite 实现（默认）
└── disk_storage/         # 磁盘存储实现
```

**关键规则**：
- **绝不直接导入存储实现**
- **始终使用** `request_context.storage`（类型：BaseStorage）

### 7. LLM Integration（LLM 集成）

**位置**：`reflexio/server/llm/`

**支持提供商**：
| Provider | 环境变量 | 模型前缀 |
|----------|----------|----------|
| OpenAI | `OPENAI_API_KEY` | (default) |
| Anthropic | `ANTHROPIC_API_KEY` | `anthropic/` |
| Google Gemini | `GEMINI_API_KEY` | `gemini/` |
| OpenRouter | `OPENROUTER_API_KEY` | `openrouter/` |
| MiniMax | `MINIMAX_API_KEY` | `minimax/` |
| Azure OpenAI | via config | `azure/` |

**关键规则**：
- **绝不直接导入 OpenAIClient/ClaudeClient**
- **始终使用** `LiteLLMClient`（通过 LiteLLM 支持多提供商）

### 8. Reflexio Facade（核心门面）

**位置**：`reflexio/lib/reflexio_lib.py`

**设计模式**：使用 Mixin 组合实现统一 API

```python
class Reflexio(
    InteractionsMixin,
    ProfilesMixin,
    AgentPlaybookMixin,
    UserPlaybookMixin,
    ConfigMixin,
    GenerationMixin,
    OperationsMixin,
    DashboardMixin,
    SearchMixin,
):
    """同步门面，提供所有 Reflexio 操作的统一 API"""
```

### 9. API Endpoints（API 端点）

**位置**：`reflexio/server/api_endpoints/`

| 文件 | 职责 |
|------|------|
| `publisher_api.py` | 发布交互 |
| `retriever_api.py` | 检索 profiles/playbooks |
| `account_api.py` | 账户管理 |

### 10. CLI（命令行接口）

**位置**：`reflexio/cli/`

**核心命令**：
```bash
uv run reflexio services start    # 启动服务
uv run reflexio services stop     # 停止服务
uv run reflexio publish          # 发布对话
uv run reflexio search           # 搜索提取的内容
```

## 测试与质量保证

### 测试框架

- **pytest** + `pytest-xdist`（并行执行 `-n auto`）
- 超时：120 秒/测试
- 覆盖率最低：65%（分支覆盖）
- 测试标记：`unit`、`integration`、`e2e`、`requires_credentials`

### 测试目录结构

```
tests/
├── benchmarks/     # 性能基准测试
├── cli/            # CLI 测试
├── client/         # 客户端测试
├── e2e_tests/      # 端到端测试
├── fixtures/       # 测试 fixtures
├── lib/            # 库测试
├── models/         # 模型测试
├── server/         # 服务端测试
├── test_data/      # 测试数据
└── utils/          # 测试工具
```

### 代码质量工具

**Python**：
- Ruff（lint + format）
- Pyright（类型检查，basic 模式）

**TypeScript/JavaScript**：
- ESLint
- tsc

## 依赖管理

### 运行时依赖

| 类别 | 关键依赖 |
|------|----------|
| Web 框架 | FastAPI, Uvicorn |
| LLM | OpenAI, Anthropic, LiteLLM |
| 存储 | Redis, SQLite (sqlite-vec) |
| 数据处理 | Pydantic, tiktoken, NLTK |
| 聚类 | HDBSCAN |
| CLI | Typer, Rich |

### 开发依赖

- pre-commit, pytest, pytest-asyncio, pytest-xdist
- black, ruff, pyright
- commitizen, semantic-release

## 关键规则与约束

### API 开发

- **绝不直接实例化 `Reflexio()`**
- **始终使用** `get_reflexio()` from `server/cache/`

### Prompts

- **绝不通义硬编码 prompts**
- **始终使用** `request_context.prompt_manager.render_prompt(prompt_id, variables)`

### Config

- `tool_can_use` 位于根 `Config` 级别——共享于 success evaluation 和 playbook extraction

## 证据锚点

- Snapshot 来源：[github-repo-reflexioai-reflexio.md](../../../raw/external/github-repo-reflexioai-reflexio.md)
- 仓库：`ReflexioAI/reflexio`
- 观察分支：`main`
- 解析到的 commit：`7df1a50188a241c6fb7d5ac10803646610639f8a`

### 关键文件

| 路径 | 职责 |
|------|------|
| `CLAUDE.md` | Claude Code 快速参考 |
| `README.md` | 项目概述与快速入门 |
| `developer.md` | 开发指南、项目结构、环境设置 |
| `pyproject.toml` | 依赖配置、测试配置、工具配置 |
| `reflexio/server/OVERVIEW.md` | 服务架构概述 |
| `reflexio/server/services/generation_service.py` | 核心生成服务 |
| `reflexio/lib/reflexio_lib.py` | Reflexio 门面类 |
| `reflexio/server/services/storage/storage_base/_base.py` | 存储抽象基类 |

## 开放问题

- Profile 和 Playbook 的提取 prompt 模板具体是什么？
- 去重算法的具体实现细节？
- Session 评估的 10 分钟延迟是否可配置？
- 聚类算法（HDBSCAN）的参数调优策略？

## 相关页面

- [multica-ai/multica 仓库地图](multica-ai-multica-repo-map.md)
- [badlogic/pi-mono 仓库地图](badlogic-pi-mono-repo-map.md)
- [multica 与 clawhouse 的目标与核心价值差异](multica与clawhouse的目标与核心价值差异.md)