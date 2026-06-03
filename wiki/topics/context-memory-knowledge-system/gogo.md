# gogo：本地 llm-wiki 桌面应用

## 项目定位

`gogo` 是一个本地 `llm-wiki` 风格 knowledge-base 的桌面应用原型。

它当前最成立的身份不是“完整公共知识库系统”，而是：

**把本地 markdown 知识库、Pi Agent、示例 knowledge-base、可见机制和最小安全边界收进同一个桌面入口里的作品级原型。**

**GitHub**: https://github.com/Barytes/gogo

**源文件位置**: `raw/personal/writings/gogo-repo-map.md`  
**补充证据**: `raw/external/github-repo-barytes-gogo.md`

## 当前边界

`gogo` 主要承接三件事：

- 浏览和编辑本地 `wiki / raw / inbox`
- 在同一个工作面里和 Pi Agent 对话
- 降低第一次使用 `llm-wiki` 工作流的门槛

它不再承担“课题组公共知识库”的完整主语。公共知识库方向已经独立为 [oh-share-it 公共知识库产品](../research-knowledge-governance/oh-share-it公共知识库产品.md)。

这个拆分很重要。`gogo` 是 app，是入口，是参考实现。`oh-share-it` 才是多人公共知识库、联邦同步、公共池聚合、知识治理和 agent-facing capability layer 的产品主语。

## 当前公开实现

截至 2026-04-28 的公开仓库，`gogo` 已经更明确地收束为本地 `llm-wiki` desktop app prototype，并进入 maintenance mode。

当前直接能力包括：

- 本地应用工作台：`Wiki / Chat` 双主模式
- `wiki / raw / inbox` 浏览与基本编辑
- Pi RPC 主聊天链路
- 多会话管理与历史恢复
- knowledge-base 切换
- `skills / schemas / AGENTS.md` 的发现与编辑入口
- `example-knowledge-base/` 最小样板
- 首次启动 onboarding
- model provider 配置与 Pi 登录路径
- 安全模式、托管 extension、审计日志、inline confirm
- Tauri 桌面壳与安装包分发路径

尚未进入 `gogo` 当前公开主线的能力包括：

- 多用户公共池与自动聚合端
- 面向公共知识库的贡献、晋升与冲突治理
- 独立的公共知识库 MCP / tool surface
- 长期运营型 SaaS 或平台支持链路

这些能力应归入 `oh-share-it`，而不是继续塞回 `gogo`。

## 核心问题

`gogo` 解决的是本地知识工作流里的低摩擦入口问题。

传统 `llm-wiki` 工作流即使理念成立，也有明显门槛：

- 要理解 `raw / wiki / inbox / skills / schemas`
- 要安装和配置 agent
- 要在知识浏览、编辑、对话之间切换
- 要处理模型 provider、session、安全确认等细节

`gogo` 的价值是把这些东西收进一个可下载、可启动、可观察的桌面壳里，让用户第一天就能完成“浏览知识库 + 问 agent + 回到 markdown 资产”的基本闭环。

## AI 协作草稿本方向

当前 Codex 更适合充当知识库的协作 agent，而不是完整的手动工作台。它可以读写本地文件、运行维护脚本、生成页面、做局部编辑和回答 query；但它本身不是一个稳定的 markdown 文件编辑器、看板或长期草稿界面。

因此，如果知识库需要一个“自己可以写东西，同时能和 AI 协作”的草稿本，比较自然的方向不是把所有东西都塞进 Codex，而是在 `gogo` 这类本地入口里补一个轻量工作面：

- `Drafts`：面向人的草稿区，承接临时想法、半成品段落、待整理材料和正在形成的判断。
- `Board`：面向任务状态的低摩擦看板，只追踪少量与知识库维护相关的状态，例如 `inbox`、`drafting`、`review`、`write-back`、`done`。
- `Agent`：面向 AI 协作的对话区，可以把草稿整理进 `raw/`、提升到 `wiki/topics/`，或按规则更新 `wiki/self/` 与 `wiki/frameworks/`。

这个方向的关键不是复制 Notion、Obsidian 或 Linear，而是补上 `llm-wiki` 工作流缺的中间层：人在这里自由写，agent 在这里帮忙整理、引用、迁移和写回，最终资产仍然落回本地 markdown 知识库。

从边界上看，草稿本应优先服务个人知识工作流，不应重新扩张成公共知识库产品。多人协作、公共池、贡献治理和同步机制仍应归入 `oh-share-it`，而不是作为草稿本的第一阶段目标。

## 设计原则

这版仓库中最稳定的设计原则有六条。

1. **gogo 服务于本地 llm-wiki knowledge-base**  
   知识不应被锁进 app。停止使用 `gogo` 不应损失知识层内容。

2. **统一 Wiki + Agent 工作面**  
   浏览、编辑、引用、对话应尽量放在一个表面里。

3. **聚焦 llm-wiki，而不是泛化成通用知识管理器**  
   保持边界清晰，比扩大场景更重要。

4. **用户是知识库的第一拥有者**  
   路径、结构、skills、schemas、`AGENTS.md` 都应尽量可见、可改、可迁移。

5. **不过度黑盒化 Agent 机制**  
   让 provider、thinking level、slash、diagnostics、安全边界保持可理解。

6. **开箱即用**  
   让第一次成功闭环更容易发生。

## 与 oh-share-it 的关系

`gogo` 和 `oh-share-it` 的关系可以这样拆：

| 名称 | 主语 | 主要问题 |
|---|---|---|
| `gogo` | 本地桌面应用 | 让个人更顺手地使用 `llm-wiki` 和本地 agent |
| `oh-share-it` | 公共知识库产品 | 让多人知识、判断、冲突和贡献形成可治理的公共工作面 |

`gogo` 可以成为 `oh-share-it` 的一个客户端或本地入口，但不应该再被描述为公共知识库产品本身。

这也解释了为什么“把 gogo 接到微信”这类想法需要拆开看：

- 如果是在控制本地知识库 app，那属于 `gogo` 的入口扩展；
- 如果是在给任何 agent 暴露公共知识库查询、贡献、同步、聚合能力，那属于 `oh-share-it` 的 tool / MCP / skill surface。

## 核心文档

当前最值得回看的文档是：

| 文档 | 作用 |
|------|------|
| `README.md` | 当前最直接的产品主语与公开边界 |
| `docs/index.md` | 当前文档总入口 |
| `docs/public/architecture.md` | 系统结构、调用链与 ownership split |
| `docs/public/design-principles.md` | 产品原则与边界 |
| `docs/public/knowledge-base-guide.md` | `llm-wiki` knowledge-base 的结构与工作流 |
| `docs/public/design-notes/agent-architecture.md` | Pi RPC 与后端编排收敛 |
| `docs/public/design-notes/frontend-workbench-elements.md` | 工作台与设置面板的真实产品面 |
| `docs/public/design-notes/pi-security-boundary.md` | 最小安全边界 |
| `docs/public/design-notes/session-management.md` | session 主链路与富历史恢复 |
| `docs/public/design-notes/slash-command-scope.md` | 为什么 slash 命令优先服务 knowledge-base 能力 |

历史上的 `product-definition-belief.md`、`release-target-and-boundaries.md`、`gogo-app-architecture.md` 仍有参考价值，但现在更多属于 `docs/archive/` 范围。

## 与现有知识的关联

- [oh-share-it 公共知识库产品](../research-knowledge-governance/oh-share-it公共知识库产品.md)
- [Pi coding agent:一种极简且可观察的 coding harness](../agent-harness-runtime/pi-coding-agent-harness.md)
- [本地知识库模式](local-knowledge-base-patterns.md)
- [AI 知识系统的产品定义信念](ai-knowledge-systems-product-definition-beliefs.md)
- [Claude Code、Codex 与 pi 的 harness 对比](../agent-harness-runtime/coding-agent-harness-comparison.md)
- [Tolaria 综合分析](../agent-harness-runtime/Tolaria%20综合分析.md)

## 当前压缩结论

`gogo` 是本地 `llm-wiki` 桌面应用。它的价值是把知识浏览、agent 对话、可见规则层和本地安全边界做成一个低摩擦入口。

公共知识库、联邦架构和 agent-facing 知识能力层不再叫 `gogo`，统一归入 `oh-share-it`。
