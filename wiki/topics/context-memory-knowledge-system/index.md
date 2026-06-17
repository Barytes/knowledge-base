# Context / Memory / 知识系统

围绕 context、memory、本地知识库、信息复利、AI 知识系统与 context infra 的页面。

## 推荐阅读顺序

- [AI 知识系统的产品定义信念](ai-knowledge-systems-product-definition-beliefs.md)
- [Agent Context Infra 前沿调研（2026-05-25）](agent-context-infra-2026-05-25.md)
- [Agent Context Infra 调研报告（2026-05-24）](agent-context-infra-2026-05-24.md)
- [Context Engine：上下文编排层](context-engine.md)
- [Context-Core 技术前沿调研报告（2026-05-25）](context-core-technical-frontier-2026-05-25.md)
- [gogo：本地 llm-wiki 桌面应用](gogo.md)
- [grapeot/context-infrastructure 仓库地图](grapeot-context-infrastructure-repo-map.md)
- [volcengine/openviking 仓库地图](volcengine-openviking-repo-map.md)
- 其余页面可按下面的完整列表继续浏览。

## 页面

- [AI 知识系统的产品定义信念](ai-knowledge-systems-product-definition-beliefs.md): llm-wiki 和 context-infrastructure 的共同点，不在于它们都用了 markdown、schema 或 agent，而在于它们都把“从原始数据里提取高价值信息，并把这些信息变成可持续复利的中间层”当成核心任务。
- [Agent Context Infra 前沿调研（2026-05-25）](agent-context-infra-2026-05-25.md): 截至 2026-05-25，agent context infrastructure 已经从“给 agent 加长期记忆”升级成一条更完整的基础设施主线：
- [Agent Context Infra 调研报告（2026-05-24）](agent-context-infra-2026-05-24.md): 截至 2026-05-24，agent context infra 已经不能再被简单理解成 RAG、向量库或“记忆功能”。更准确的定义是：
- [Context Engine：上下文编排层](context-engine.md): Context Engine 可以理解成 AI 系统里的上下文编排层。它的核心职能不是“保存更多信息”，而是在每一轮任务前决定：
- [Context-Core 技术前沿调研报告（2026-05-25）](context-core-technical-frontier-2026-05-25.md): 本文只讨论 context layer / context-core，刻意排除通用 agent runtime、MCP/A2A 这类连接协议、OpenAI Agents SDK 这类编排框架、普通 tool orchestration 和泛工作流平台。
- [gogo：本地 llm-wiki 桌面应用](gogo.md): gogo 是一个本地 llm-wiki 风格 knowledge-base 的桌面应用原型。
- [grapeot/context-infrastructure 仓库地图](grapeot-context-infrastructure-repo-map.md): 这页是围绕主题“仓库架构与工程实践”维护的 grapeot/context-infrastructure 第一版仓库地图。
- [volcengine/openviking 仓库地图](volcengine-openviking-repo-map.md): 这页是 volcengine/openviking 的第一版仓库地图，观察主题是“面向 AI Agent 的 context database 架构与工程实践”。
- [从Andrej Karpathy的LLM Wiki和鸭哥的context infrastructure看信息复利系统的设计](essays/从Andrej%20Karpathy的LLM%20Wiki和鸭哥的context%20infrastructure看信息复利系统的设计.md): 我最近发现，Andrej Karpathy的llm-wiki 和鸭哥的context-infrastructure 似乎有共同之处。我分析了这两个系统的设计，得到了一些关于如何让数据产生复利的learnings。
- [信息复利系统设计](information-compounding-systems-design.md): 从 llm-wiki 和 context-infrastructure 往上抽象，可以得到一个更一般的洞察：
- [本地知识库模式](local-knowledge-base-patterns.md): 这两份来源材料描述的是两套互补但不相同的系统。
- [知识库运行模型](knowledge-base-operating-model.md): 当这个仓库把“知识编译”和“个人判断蒸馏”视为两条分开的生产线，只在回答时或在稳定桥接页里汇合时，它运行得最好。
- [给自己做了一个 llm-wiki 的入口应用](essays/给自己做了一个llm-wiki的入口应用.md): 我在用 llm-wiki 作为自己的第二大脑。但是一个痛点是，我需要同时打开 Obsidian 和 Codex，在两个工具之间来回切换。并且我只有一个屏幕，来回切换就超级麻烦。我又懒得给obsidian装插件，现有的插件又需要配置（如acp）。

## 相关框架

- [知识系统判断框架](../../frameworks/知识系统判断框架.md)
- [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md)

## 相关自我页面

- [工作面摩擦敏感观察](../../self/工作面摩擦敏感观察.md)
- [研究知识系统中的反共识写回观察](../../self/研究知识系统中的反共识写回观察.md)

## 返回

- [话题总览](../index.md)
- [Wiki 首页](../../index.md)
