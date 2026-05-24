# gogo 仓库地图（由 `gogo-app` 更新而来，沿用旧文件名 `gogo-repo-map.md`）

**GitHub**: https://github.com/Barytes/gogo  
**观察日期**: 2026-04-28  
**材料类型**: personal project repo map

---

## 一句话理解

当前公开仓库 `gogo` 已经不只是“一个正在收敛中的 app 层实验”，而是一个**可下载、可本地运行、带示例 knowledge-base、内置 Pi Agent、面向 llm-wiki 工作流的桌面应用原型**。

如果说上一版 `gogo-app` 仓库地图强调的是“它从大 gogo 设想里拆出了 app 层”，那么这一版更重要的变化是：

**公开仓库的主语已经彻底变成了一个本地 llm-wiki desktop app，而且它明确以 maintenance mode 的作品形态对外。**

---

## 这次更新最重要的变化

和之前的 `gogo-app` 版本相比，最值得记住的是五点。

### 1. 仓库名与对外表达统一成 `gogo`

现在的公开仓库是：

- `https://github.com/Barytes/gogo`

README 直接把它定义成：

- 自带 `Pi Agent` 的本地 `llm-wiki` 风格知识库桌面应用原型
- 可下载 Windows / macOS 安装包
- 不要求用户额外安装 coding agent 或插件

这说明它的对外表达已经不再主要是“课题组公共知识库系统中的一个 app 层”，而是一个**可以独立被理解和试用的本地知识工作台产品**。

### 2. “开箱即用”从口号变成了真实产品路径

上一版更像是：

- 有 app
- 有桌面化方向
- 有知识库切换
- 有 Pi 对话

而这一版已经补上更完整的第一天路径：

- 首次启动欢迎页
- 模型 provider 配置
- OAuth / API key 两类接入
- 没有现成知识库时自动创建 `example-knowledge-base`
- 有现成 `raw/ + wiki/` 结构时直接接入用户自己的 knowledge-base

也就是说，它不再只是“适合会折腾的人从源码跑起来”，而是在努力把 **llm-wiki 工作流的首次成功闭环** 做成一个普通用户也能进入的体验。

### 3. 安全边界被显式产品化了

这一版最明显的新机制，是把安全问题从“默认相信 agent”前移成了产品界面与运行时机制的一部分。

新增或明确化的东西包括：

- `app/backend/security_service.py`
- 托管生成的 `managed-security.ts`
- 聊天区里的安全模式切换
- `readonly / workspace-write / full-access` 三档模式
- 对 `bash / write / edit` 的 allow / block 审计日志
- 在当前 `tool_call` 上做 inline 安全确认

这很关键。它说明 `gogo` 不只是想把 Pi 嵌进 GUI，而是想把**“本地 agent 可以做到什么、不能做到什么、用户在哪里接管”** 一起做成产品表面的一部分。

### 4. 文档体系从零散说明变成了正式的 docs map

现在 `docs/` 不再只是一些临时设计文档，而是分成：

- `docs/index.md`
- `docs/public/`
- `docs/archive/`

其中：

- `docs/public/` 是当前实现的正式公开文档
- `docs/archive/` 放历史 planning、packaging、deprecated、vendor reference

这意味着仓库已经开始把“当前真实实现”和“历史思考材料”明确分层。对 repo map 来说，这非常重要，因为它降低了“旧文档误导当前判断”的风险。

### 5. 公开边界变得更诚实：maintenance mode

README 现在直接写明：

- 项目处于 `maintenance mode`
- 作为作品项目公开
- 不再积极开发新功能
- 不建议视为生产级软件或长期支持的桌面产品

这不是坏事。相反，这是一种更清晰的边界表达：

**仓库现在优化的是“作为一个完成度足够高的作品与参考实现被理解”，而不是“继续无限扩张产品承诺”。**

---

## 当前仓库到底在做什么

从 `README.md`、`docs/index.md`、`docs/public/architecture.md` 和一组 `design-notes` 看，当前仓库同时成立三种定义。

### 1. 产品层定义

它是一个 **llm-wiki 本地知识库工作台**：

- 浏览 `wiki / raw / inbox`
- 用内置 Pi Agent 聊天
- 上传文件并走 `ingest / query / lint` 工作流
- 编辑知识库里的 `skills / schemas / AGENTS.md`
- 切换模型、思考水平、安全模式与 knowledge-base

### 2. 工作流层定义

它不是抽象的“AI 第二大脑”产品，而是一个对 **llm-wiki workflow** 有明确支持的产品壳。

也就是说它优化的不是“任意知识管理”，而是：

- source 进入 `inbox/`
- 进入 `raw/`
- 蒸馏到 `wiki/`
- 用 agent query
- 再持续 lint 和写回

它甚至把 `example-knowledge-base/` 作为仓库内的一等公民，直接提供了最小工作流样板。

### 3. 交付层定义

它现在是一个 **可安装的桌面应用原型**，但明确停在作品与参考实现边界：

- 已有 Windows / macOS 安装包
- 已有 Tauri 打包链路
- 已有源码运行路径
- 但不承诺长期产品化支持

所以这里最准确的说法不是“一个在开发中的大系统”，而是：

**一个边界相对清楚、完成度不低、但主动停止继续膨胀承诺的本地知识工作台原型。**

---

## 顶层结构

根据 GitHub tree 当前可见结构：

```text
gogo/
├── README.md
├── package.json
├── pyproject.toml
├── app/
│   ├── backend/
│   └── frontend/
├── docs/
├── example-knowledge-base/
├── scripts/
└── src-tauri/
```

相比旧版 `gogo-app`，这里最值得记住的结构变化是：

1. 仓库名统一成了 `gogo`
2. `example-knowledge-base/` 成为顶层正式目录
3. `docs/` 被重构成 `public + archive`
4. `security_service.py` 与安全边界文档进入主线
5. `scripts/` 收敛为更明确的开发/构建脚本

---

## 目录与职责

### `app/backend/`

后端仍然是 FastAPI + Pi RPC 编排层，但现在比上一版更完整地承担这些职责：

- `main.py`：统一 API 入口，串起 settings、wiki/raw/inbox、session、security、diagnostics
- `session_manager.py`：session 生命周期、富历史恢复、流式对话、abort、extension UI response
- `pi_rpc_client.py`：单 reader task 的 Pi RPC 通讯层
- `config.py`：knowledge-base、provider、Pi runtime、app state 配置
- `security_service.py`：安全模式、受信任工作区、危险命令规则、审计日志、托管安全 extension
- `skill_service.py`：skills / schemas / capability 文件发现与编辑
- `wiki_service.py` / `raw_service.py`：本地文件服务
- `desktop_entry.py`：桌面壳后端入口

### `app/frontend/`

前端仍然是 plain HTML / CSS / JS 单页工作台，但现在产品面明显更完整：

- `index.html`：工作台 DOM 骨架
- `assets/workbench.js`：布局切换、设置面板、startup onboarding、diagnostics、provider 配置
- `assets/chat.js`：多会话聊天、流式消息、思考过程、slash、inbox、安全确认、上下文与模型切换
- `assets/wiki.js`：Wiki / Raw / Inbox 浏览与编辑
- `assets/desktop-bridge.js`：前端到 Tauri 的原生能力桥
- `assets/styles.css`：整体布局与视觉系统

### `docs/`

当前文档体系已经是仓库的重要组成，而不只是附属说明。

- `docs/index.md`：当前文档入口地图
- `docs/public/architecture.md`：系统关系与主调用链
- `docs/public/design-principles.md`：产品原则
- `docs/public/knowledge-base-guide.md`：knowledge-base 结构与工作流说明
- `docs/public/design-notes/*`：更深的设计与边界说明
- `docs/archive/*`：历史 planning、packaging、deprecated、vendor snapshot

### `example-knowledge-base/`

这是这一版非常关键的新信号。

它不是 demo 素材而已，而是：

- 产品首次使用路径的一部分
- llm-wiki 工作流的最小可运行样板
- “gogo 服务 knowledge-base，而非反过来绑死知识”的具体证据

### `scripts/`

现在的脚本更收敛：

- `backend-dev.mjs`：桌面开发态启动后端
- `desktop-build.mjs`：桌面打包链路
- `clean.mjs`：清理

这说明仓库已经从“很多实验脚本”转向“围绕当前交付边界保留少数关键脚本”。

### `src-tauri/`

桌面壳仍然是主线之一，但这一版更强调：

- 原生目录选择器
- 本地路径打开
- companion knowledge-base 目录
- packaged runtime 的后端与 Pi 资源注入

这部分已经不只是“把网页包起来”，而是在吸收桌面应用特有的工作流责任。

---

## 当前最值得记住的几个机制

这里不按文件清单写，而按“它在控制什么”来写。

### 1. 用一个工作台把 llm-wiki 工作流收进来

核心控制的是：

**不要再让用户在 note app 和 coding agent 之间来回切换。**

它现在把这些动作压到同一个表面：

- 看 Wiki
- 看 Raw
- 看 Inbox
- 引用页面
- 上传文件
- 跟 agent 对话
- 触发 ingest
- 编辑 skills / schemas

这比上一版更强，因为它已经不只是“浏览 + 对话”，而是更完整地覆盖了 llm-wiki 的日常闭环。

### 2. 让 knowledge-base 保持独立，而 app 只是入口壳

这条原则在这一版更强了。

证据包括：

- README 明说停止使用 gogo 不会损失知识库内容
- `example-knowledge-base/` 是普通文件夹结构
- skills、schemas、`AGENTS.md` 都暴露给用户直接修改
- 可切换到用户自己的 knowledge-base

这控制的失败模式是：

**产品为了“更顺手”把知识与工作流重新锁回应用本身。**

### 3. 用 app state 和 knowledge-base 分层，避免把运行时污染进知识层

`docs/public/architecture.md` 现在把这层区分讲得很清楚：

- knowledge-base 保存 durable knowledge
- `.gogo/` 保存 app settings、provider profile、session registry、audit logs、generated extensions

这很重要，因为它避免了两种污染：

1. 把产品运行时状态写进用户知识层
2. 把用户可迁移知识绑进 app 私有状态

### 4. Pi RPC 主链路已经收敛成 session-only 编排

当前主聊天路径已经明显收敛到：

- `chat.js`
- `main.py`
- `session_manager.py`
- `pi_rpc_client.py`
- `pi --mode rpc`

而且 `PiRpcClient` 通过：

- 单 reader task
- response future
- event queue

来消除并发读 `stdout` 的问题。

这控制的失败模式是：

**GUI 套一个 agent 后，流式事件、终止、历史恢复和多会话并发全都变得不稳定。**

### 5. Provider 和 Security 都通过托管 extension 外化给 Pi

这一版很漂亮的一点是，没有把“能力配置”全部硬写死在 app 内部，而是继续保持机制可见：

- provider 由 app 托管配置，但生成 `managed-providers.ts`
- security 由 app 托管配置，但生成 `managed-security.ts`
- Pi RPC 启动时通过 `--extension` 注入

这说明 `gogo` 的默认路线依然是：

**应用层编排 + 机制外显**，而不是把一切都黑盒化成“设置生效了，但你不知道系统到底怎么工作的”。

### 6. 安全边界不是后台规则，而是聊天区里的显式工作面

新的安全设计最值得注意的是，它没有把安全只做成静态配置，而是放到了实际聊天工作面里：

- 聊天区可切换安全模式
- 当 `bash / write / edit` 被模式阻断时，直接弹 inline confirm
- 用户可以“允许这一次”或“禁止并告知 Pi”
- 审计日志在 diagnostics 中可见

这控制的失败模式是：

**agent 明明在本地机器上运行，但用户既看不清权限边界，也没有低摩擦的人在环接管点。**

### 7. docs 成了产品边界的一部分

`docs/index.md` 与 `docs/public/*` 的存在，说明这个仓库现在已经把“如何被读懂”本身当成产物的一部分。

这控制的失败模式是：

**仓库已经收敛出不少判断，但只有作者自己知道哪些文档是当前的、哪些是历史残留。**

### 8. maintenance mode 也是一种架构决策

README 里的 maintenance mode 不只是项目状态说明，它实际也在控制一个失败模式：

**作品项目无限背负产品化预期，最后既不能诚实收口，也无法稳定交付。**

现在的边界反而更清楚：

- 这是一个足够完整的参考实现
- 可以安装、运行、阅读、学习
- 但不再承诺继续扩张产品面

---

## 从这版仓库里看到的产品表达

因为这是你的项目材料，所以除了功能和目录结构，更值得记的是它暴露出的产品 taste。

### 1. 仍然从工作摩擦出发

这个项目最根本的出发点仍然不是“我要做一个大平台”，而是：

- Obsidian + Codex 的切换摩擦
- 单屏使用时尤其难受
- 对非技术朋友来说门槛太高

这说明你的产品判断依然优先从**具体摩擦与首次成功路径**开始。

### 2. 用户对象比上一版更明确地走向“非技术用户也能试”

上一版更多是“把自己的工作流做顺”；这一版则更明确多了一层：

- 不想要求别人先装 coding agent
- 不想要求别人先配一堆环境
- 想让人通过 installer 和 welcome flow 先跑起来

这使得“开箱即用”不再只是偏好，而是产品核心约束。

### 3. 依然优先保留用户对底层机制的可见性

虽然产品面对的人群更广了，但并没有因此彻底把底层机制藏掉。相反，仍然暴露：

- skills / schemas
- model provider
- thinking level
- context window
- diagnostics
- security mode

这说明你的偏好不是“消费级 = 完全不可见”，而是：

**让复杂性被驯化，但不把关键边界藏起来。**

### 4. 明确接受“作品项目”的边界，而不是继续假装会无限长大

maintenance mode 其实也是一种取舍表达。

它说明你愿意让项目停在：

- 已经能展示判断
- 已经能展示手艺
- 已经足以成为参考实现

而不是为了迎合“正式产品”叙事继续拉长不必要的承诺链条。

---

## 当前仓库与“大 gogo 设想”的关系

现在最需要避免的误读是：

- 当前公开仓库 `gogo` ≠ 那个完整的“课题组公共知识库系统”已经被完整实现

更准确的理解是：

### 当前主语

当前主语是：

**一个本地 llm-wiki desktop app 原型。**

### 更大设想仍然存在，但不再是当前公开仓库的默认读法

围绕：

- 公共知识聚合
- 多人协作写回
- 联邦同步
- `gogo-client / gogo-server`

这些更大的系统设想，今天更多沉淀在：

- `docs/archive/planning/`
- 本知识库里的 `wiki/bridges/` 页面

而不是当前 README 的第一主语。

换句话说：

**仓库现在公开表达的是“可用的本地工作台”，更大的公共知识库愿景则退回到历史规划与本地分析层。**

这比上一版更进一步地完成了收口。

---

## 当前值得回看的证据锚点

### GitHub 仓库

- `https://github.com/Barytes/gogo`

### 顶层产品表达

- `README.md`
- `package.json`
- `pyproject.toml`
- `src-tauri/tauri.conf.json`

### 当前正式文档入口

- `docs/index.md`
- `docs/public/architecture.md`
- `docs/public/design-principles.md`
- `docs/public/knowledge-base-guide.md`
- `docs/public/concepts.md`
- `docs/public/developer-guide.md`

### 关键设计说明

- `docs/public/design-notes/agent-architecture.md`
- `docs/public/design-notes/frontend-workbench-elements.md`
- `docs/public/design-notes/session-management.md`
- `docs/public/design-notes/pi-security-boundary.md`
- `docs/public/design-notes/slash-command-scope.md`

### 后端关键机制

- `app/backend/main.py`
- `app/backend/session_manager.py`
- `app/backend/pi_rpc_client.py`
- `app/backend/security_service.py`
- `app/backend/skill_service.py`
- `app/backend/config.py`

### 前端关键机制

- `app/frontend/index.html`
- `app/frontend/assets/workbench.js`
- `app/frontend/assets/chat.js`
- `app/frontend/assets/wiki.js`
- `app/frontend/assets/desktop-bridge.js`

### 桌面与打包

- `src-tauri/src/main.rs`
- `scripts/backend-dev.mjs`
- `scripts/desktop-build.mjs`

### 工作流样板

- `example-knowledge-base/`

---

## 这一版 repo map 的临时结论

如果只压成一句话：

**`gogo` 现在最像一个“把本地 llm-wiki 工作流、Pi Agent、knowledge-base 结构、桌面安装路径和最小安全边界一起收进同一个产品壳里的作品级桌面应用原型”。**

相比上一版，这一版更清楚的不是“它还能长成什么”，而是：

- 它今天已经是什么
- 它明确不再承诺什么
- 它把哪些边界真正做成了产品

而从你的表达看，仓库里反复出现的个人取向仍然是：

- 从具体工作摩擦出发
- 强调首次成功闭环
- 尊重用户对知识库的拥有权
- 暴露关键机制而不是全黑盒
- 守住 llm-wiki 边界，不泛化成通用知识管理器
- 愿意在合适的时候停止扩张承诺

这些都比“它用了哪些技术”更值得保留下来。