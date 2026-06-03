# Agentic Canvas Workbench：可被 agent 观看的知识画板

## 产品定位

`Agentic Canvas Workbench` 是一个面向个人知识工作流的可视化思考工作面。

它让用户在画板上写写画画、拖拽概念、组织思维导图，同时让 coding agent 能实时读取画板状态，基于当前可见内容总结、追问、建议结构调整，并把稳定结论写回 file-based 知识库。

一句话定义：

**这是一个人类用空间思考、agent 用结构观看、知识库用文件沉淀的协作画板。**

它不应被定义成通用白板，也不应先定义成聊天机器人。更准确的产品主语是：把可视化草稿、agent observation 和本地 markdown 知识资产接到同一个工作面里。

## 核心问题

这个产品解决的不是“没有画图工具”，而是三种工作面断裂：

1. 人在白板上最自然，但白板内容通常不会进入知识库。
2. coding agent 能读文件和代码，但看不见用户正在形成的视觉思路。
3. file-based 知识库可持久、可审计、可迁移，但缺少适合早期发散和关系建模的空间界面。

所以高价值问题是：

> 能否让用户在一个低摩擦视觉工作面里思考，同时让 agent 按规则观察、总结、建议和写回，使画板不只是临时草稿，而成为知识库的前端工作面？

## 用户与场景

第一用户应该是已经在使用 file-based 知识库和 coding agent 的个人 builder / researcher。

关键场景包括：

- 设计一个产品、功能或系统架构；
- 把几条想法组织成思维导图；
- 在 coding agent 实现前，把需求、模块、风险和开放问题画出来；
- 让 agent 根据画板内容生成 brief、todo、wiki 页面或实现计划；
- 把画板中的稳定节点链接到 `wiki/topics/`、`wiki/frameworks/` 或具体文件。

这和 `gogo` 的关系是延展而不是替代。`gogo` 解决本地知识库的浏览、编辑和 agent 对话入口；这个画板方向解决更早一层的视觉草稿与结构形成。

## MVP 定义

最小但仍然像 magic 的版本不需要完整协同白板，也不需要复杂 AI 视觉模型。

第一版只需要四个闭环：

1. **可编辑画板**：支持文本块、自由线条、箭头、简单节点、框选和拖拽。
2. **结构化画板状态**：每个元素都有 id、类型、位置、文本、连接关系和更新时间，而不是只保存为图片。
3. **agent 观察接口**：agent 可以读取当前画板 snapshot，得到结构化 JSON、轻量 markdown 摘要和可选截图。
4. **知识库链接与写回**：画板节点可以链接到本地文件；agent 可以把当前画板总结成 `wiki/topics/` 的草稿或更新建议，但写入前需要用户确认。

第一版的 magic moment 是：

> 用户画了一个混乱的产品思维导图，agent 能立即说出“这里其实有三个产品主语混在一起”，并给出一份可写回知识库的产品定义 brief。

## Agent 应该如何观看画板

agent 不应只看截图。截图适合视觉确认，但不适合作为主要上下文。

更稳的做法是三层上下文：

```text
Canvas JSON
  元素、坐标、连接、层级、选区、更新时间

Canvas Markdown
  按空间邻近、连接关系和用户命名区块压缩成可读摘要

Canvas Screenshot
  用于视觉 sanity check，处理手绘图、布局和空间暗示
```

coding agent 的默认输入应该是前两层。只有当用户手绘内容、布局关系或视觉密度本身重要时，才补截图。

## 与 file-based 知识库的连接

画板不应该成为新的知识孤岛。它应把知识资产继续留在文件系统里。

推荐的本地文件结构是：

```text
boards/
  <board-id>/
    board.json
    board.md
    snapshot.png
    links.json
```

其中：

- `board.json` 是画板真实状态；
- `board.md` 是给人和 agent 快速读取的结构化摘要；
- `snapshot.png` 是视觉备份与调试证据；
- `links.json` 记录画板节点与知识库文件、代码文件、任务、commit 或外部资源的关系。

与当前知识库的写回关系可以这样定义：

| 画板内容 | 写回目标 |
|---|---|
| 产品、项目、架构分析 | `wiki/topics/projects-roadmaps/` 或相关 topic |
| 高复用判断镜头 | `wiki/frameworks/` |
| 反复出现的个人取舍偏好 | `wiki/self/`，但只作为 observation 起步 |
| 临时想法与半成品 | 用户草稿空间，不自动晋升 |

写回要遵守本仓库已有规则：先 wiki，必要时 raw，维护页用中文，用户草稿空间不被 agent 自动整理。

## 推荐架构

第一版可以走本地优先架构：

```text
frontend canvas
  React + tldraw / Excalidraw-like editor

canvas store
  local file adapter
  board.json / board.md / snapshot.png / links.json

agent bridge
  expose tools:
    read_canvas_snapshot
    summarize_canvas
    link_canvas_node
    propose_wiki_writeback
    export_canvas_brief

knowledge-base adapter
  read wiki/index.md
  route writeback by schemas/query.md
  run kb-ingest.sh site after confirmed wiki updates
```

如果目标是快速验证，不建议先做多人实时同步。先把单人本地工作面、agent 可观察状态和知识库写回打通，价值会更清楚。

## 实现建议

第一阶段应优先使用成熟画布库，而不是手写白板引擎。

可选路线：

- `tldraw`：更适合结构化 shape、协作画板、可扩展 editor API。
- `Excalidraw`：更适合手绘感和轻量图示，但结构化语义需要额外适配。
- 自研 canvas：除非有强交互实验需求，否则第一阶段不推荐。

MVP 推荐 `tldraw + 本地文件 adapter + agent tools`。原因是产品风险主要在“画板是否能成为 agent-facing context surface”，不是画布渲染技术本身。

技术上可以先做五个能力：

1. 保存和恢复 board；
2. 把 shape graph 转成 markdown brief；
3. 允许节点链接本地文件路径；
4. 暴露一个 MCP 或本地 HTTP tool surface 给 agent；
5. 写回知识库前弹出 diff / confirm。

## 风险与边界

最大风险是过早做成一个“大而全的 AI 白板”。

更稳的边界是：

- 不先和 Miro、FigJam、Obsidian Canvas 正面竞争；
- 不把所有图形都交给视觉模型理解；
- 不默认自动改知识库；
- 不把画板变成新的封闭数据库；
- 不在第一版承担多人权限、云同步和公共知识治理。

它第一版只验证一个问题：

> 结构化画板作为 agent-facing context surface，是否能显著降低从发散思考到知识库写回、产品定义和 coding plan 的摩擦？

## 成功标准

短期成功可以用几个行为信号判断：

- 用户愿意先在画板上组织想法，而不是直接开聊天；
- agent 能基于画板准确总结当前问题结构；
- agent 的建议能指出混乱关系、缺口或产品主语混用；
- 用户愿意把 agent 生成的 brief 写回 wiki；
- 写回后的 wiki 页面在后续 query 中被再次引用。

如果这些成立，这个方向就不是“多一个画图工具”，而是本地知识系统的一个新默认工作面。

## 相关页面

- [gogo：本地 llm-wiki 桌面应用](../context-memory-knowledge-system/gogo.md)
- [本地知识库模式](../context-memory-knowledge-system/local-knowledge-base-patterns.md)
- [AI 知识系统的产品定义信念](../context-memory-knowledge-system/ai-knowledge-systems-product-definition-beliefs.md)
- [AI Architect Lens](../ai-product-product-definition/ai-architect-lens.md)
- [AI Architect 的 Context Intelligence 镜头](../ai-product-product-definition/ai-architect-context-intelligence.md)
- [产品定义判断框架](../../frameworks/产品定义判断框架.md)
- [知识系统判断框架](../../frameworks/知识系统判断框架.md)
- [工作面摩擦敏感观察](../../self/工作面摩擦敏感观察.md)
- [用户自主性优先产品取舍观察](../../self/用户自主性优先产品取舍观察.md)
