# oh-share-it 公共知识库产品

## 摘要

`oh-share-it` 是原先被混在 `gogo` 名字下的公共知识库产品方向。

它的核心不是再做一个笔记工具，也不是把本地文件夹简单搬到云上，而是把多人研究中的知识、判断、冲突、贡献和 agent 调用做成一个可治理的公共工作面。

一句话定义：

**`oh-share-it` 是面向课题组和知识密集团队的公共研究知识库，让个人知识在保留边界的前提下进入共享池，并被人和 agent 按场景复用。**

## 为什么从 gogo 拆出来

`gogo` 当前已经收束为本地 `llm-wiki` 桌面应用。继续让它同时代表“本地 app”和“公共知识库产品”，会造成三个混淆：

- app 能力和公共知识治理能力混在一起；
- 本地入口的完成度被误读成公共知识库系统已经实现；
- 微信、MCP、联邦同步等 agent 化想法会反过来冲散 `gogo` 的清晰边界。

因此新的命名边界是：

| 名称 | 负责什么 | 不负责什么 |
|---|---|---|
| `gogo` | 本地 `llm-wiki` 桌面入口 | 多人公共知识库治理 |
| `oh-share-it` | 公共知识库、联邦同步、贡献聚合、agent-facing tools | 桌面 app 的具体 UI 壳 |

`gogo` 可以成为 `oh-share-it` 的客户端或参考实现，但不是 `oh-share-it` 本身。

## 核心问题

`oh-share-it` 主要解决四类问题。

### 1. 知识孤岛

每个研究者都有自己的材料、判断、失败经验和临时结论。问题不在于没有知识，而在于这些知识没有稳定进入团队默认工作面。

### 2. 判断不复利

高价值问答、导师点评、实验失败原因、方法边界和概念区分，经常消失在聊天记录、个人笔记和项目碎片里。

`oh-share-it` 要把这类判断沉淀成可被后人查询、引用、修订和继续追问的公共资产。

### 3. 冲突被错误合并

研究知识不是 SOP。很多冲突观点不应该被 majority-wins 合成一个答案，而应该被保留为 tension。

对认知知识来说，冲突经常就是价值本身。

### 4. Agent 需要可路由上下文

多人知识一旦进入 agent 工作流，就必须回答：

- 哪些知识是公共默认层；
- 哪些知识只属于某个人或某个项目；
- 冲突版本什么时候保留，什么时候合并；
- 当前 query 应该加载哪一层、哪一版、谁的判断。

这也是 `oh-share-it` 和普通 RAG 的关键差异：它不只是“搜到相关片段”，而是管理可复用知识在多人场景里的边界、来源和路由。

## 产品形态

`oh-share-it` 可以被理解成三层系统。

### 1. 文件系统知识资产

每个人仍然有自己的本地知识库：

```text
raw/
wiki/
bridges/
self/
skills/
schemas/
AGENTS.md
```

这层保留 `llm-wiki` 的核心优点：可读、可改、可迁移、可审计。

### 2. 联邦公共知识库

公共层不一定需要中心化推理服务。更稳的初始架构是联邦式：

```text
个人本地知识库
  -> submit / push pending-pool
  -> public repo 做保守聚合
  -> public-pool / tensions / related views
  -> 每个人 pull 回本地
```

这个设计把推理成本分散到个人端，把公共端收束为同步、审计、聚合和页面维护。

### 3. Agent-facing capability layer

OpenViking 的 MCP 设计带来的启发是：公共知识库也可以不是一个“网页产品”，而是一组 agent 可调用能力。

`oh-share-it` 可以暴露为 tool / skill / MCP server：

- `search_public_pool`: 检索公共池中的知识与判断；
- `read_public_page`: 读取公共页或 tension 页；
- `contribute_page`: 把本地页面或问答提交为候选贡献；
- `propose_tension`: 当发现冲突观点时，提出 tension 页；
- `sync_public_pool`: 拉取公共池更新；
- `aggregate_pending`: 对 pending contribution 做保守聚合；
- `list_related_views`: 查找同一主题下的多视角页面；
- `explain_source_basis`: 回答某个判断来自哪些页面与来源。

如果做成 `skill`，重点是教 agent 何时、如何使用公共知识库工作流。  
如果做成 `tool` 或 MCP server，重点是给 agent 一个稳定接口，直接执行检索、写回、同步与聚合。

## 和 agent 的关系

`oh-share-it` 不应该先被做成“一个聊天机器人”。更稳的顺序是先把公共知识库能力拆成 tools，再接各种入口。

推荐分层：

```text
oh-share-it-core
  文件系统知识资产 + 公共池规范 + schemas + skills

oh-share-it-tools
  query / ingest / writeback / contribute / sync / aggregate / lint

oh-share-it-mcp
  把 oh-share-it-tools 暴露给任意 MCP client

oh-share-it-agent
  默认 agent，连接微信 / 飞书 / Telegram / 桌面聊天入口

gogo
  可选的人类本地桌面入口
```

微信、飞书、桌面聊天框都只是 channel。核心产品能力应放在 tools 和公共知识库协议里。

这能避免 channel 牵着产品走，也能保留一个重要原则：知识库仍然是用户和团队拥有的文件系统资产，app、agent、bot 都只是入口。

## 与 RAG 和 file-based context 管理的不同

`oh-share-it` 可以用 RAG，也可以保留 file-based context，但它的产品问题比二者更高一层。

| 方案 | 主要解决 | 主要不足 |
|---|---|---|
| 直接 file-based context | 文件可读、可编辑、可由 agent 调用 | 缺少多人贡献、冲突治理和使用路由 |
| 普通 RAG | 在大材料集合中找相关片段 | 容易只做检索，不处理判断沉淀和公共层维护 |
| `oh-share-it` | 多人知识如何进入公共工作面，并被人和 agent 按边界复用 | 需要定义贡献、聚合、冲突、权限和评测机制 |

所以 `oh-share-it` 的目标不是替代文件系统或 RAG，而是把它们放进一个更明确的知识治理流程里。

## 最小可验证版本

第一版不需要做完整平台。可以先验证一个问题：

> 外部 agent 调用 `oh-share-it-tools`，是否比直接用文件系统工具更稳定地完成公共知识库查询、贡献、写回和维护？

最小版本可以包含：

- `search`: 按 `wiki/index.md`、维护页和全文检索查相关页面；
- `read`: 读取并压缩一个页面或一组页面；
- `query`: 按 `schemas/query.md` 生成回答；
- `contribute`: 把本地页面、问答或判断提交为候选贡献；
- `writeback`: 把高价值问答写回合适层；
- `sync`: 同步公共池；
- `lint`: 做轻量结构检查、孤页检查和索引修复。

后续再增加 `aggregate_pending`、`propose_tension`、`list_related_views` 和 `explain_source_basis`。

## 风险与边界

`oh-share-it` 的主要风险不是技术不够炫，而是边界过早膨胀。

- 如果先做 bot，容易被微信、飞书等 channel 的限制牵走。
- 如果先做中心化平台，容易过早承担账号、权限、成本和运营复杂度。
- 如果只做 RAG，容易把公共知识库降级成搜索框。
- 如果过早自动聚合，容易把真正有价值的冲突抹平。
- 如果写操作没有确认和审计，知识资产会被黑盒 agent 污染。

因此初期应优先验证：公共知识库 tool surface 能否让 agent 更稳定地查询、贡献、写回和维护，而不是先追求完整平台形态。

## 相关页面

- [gogo：本地 llm-wiki 桌面应用](../context-memory-knowledge-system/gogo.md)
- [课题组公共知识库的产品定义信念](课题组公共知识库的产品定义信念.md)
- [课题组公共知识库的联邦架构设计](课题组公共知识库的联邦架构设计.md)
- [课题组公共知识库的架构风险与分层设计](课题组公共知识库的架构风险与分层设计.md)
- [什么是公共知识库应该共享的公共知识](什么是公共知识库应该共享的公共知识.md)
- [公共知识库、Reflexio 与 EvoMap 的对比分析](公共知识库、Reflexio与EvoMap的对比分析.md)
- [Superlinear 社区 Agent Skill 知识治理信号](Superlinear社区AgentSkill知识治理信号.md)
- [volcengine/openviking 仓库地图](../context-memory-knowledge-system/volcengine-openviking-repo-map.md)

## 当前压缩结论

`oh-share-it` 是公共知识库产品。它继承原先公共知识库愿景里的多人知识治理、联邦架构和 agent-facing capability layer，但不再和 `gogo` 桌面 app 混用同一个名字。

`gogo` 负责让个人使用本地 `llm-wiki` 更顺手。`oh-share-it` 负责让多人知识进入公共工作面，并能被 agent 稳定、透明、可审计地调用。
