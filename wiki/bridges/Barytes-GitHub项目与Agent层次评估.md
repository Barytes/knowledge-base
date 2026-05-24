# Barytes GitHub 项目与 Agent 履历层次评估

## 评估范围与证据口径

这页只基于**公开可见证据**做判断，**未直接 clone 仓库**。

使用的证据包括：

- GitHub API 可见元数据：`stars`、`release`、最近提交、文件树规模
- `README.md`
- 公开 `docs/` 文档
- `package.json` / `pyproject.toml`
- 公开招聘 JD 抽样：`OpenAI`、`Anthropic`、`Cursor`、`Cohere`、`Sierra`、`Harvey`、`Perplexity`、`Notion`、`Replit`、`Factory`、`Poolside`

评估对象：

- `Barytes/gogo`
- `Barytes/oh-share-it`
- `Barytes/my-little-chating-agent`
- `ICASSP 2026` 论文：`strategic user offloading and service provider pricing in mobile edge computing`
- 教育背景：中山大学软件工程本硕

判断尺子主要来自：

- [AI 产品六层与 L3-L6 能力分层](../knowledge/AI 产品六层与 L3-L6 能力分层.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../knowledge/AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md)
- [职业信号与叙事框架](../frameworks/职业信号与叙事框架.md)
- [Agent 岗位 JD 抽样与能力信号](../knowledge/Agent岗位JD抽样与能力信号.md)

## 压缩结论

先给结论。

你的公开履历已经**不是“街上会搓 Claude Code / RAG 的 L4”**。更准确地说：

- **理解层**：已经进入 **L5 Builder**，并且带有明显的 **L6 产品 / 架构视角**。
- **公开代码证据层**：目前更接近 **L5-**，还没有完全形成一个市场一眼可识别的 **L5 完整证据包**。
- **最强信号**：`context / knowledge / harness / agent-facing system` 这一组方向上的产品定义和系统组织能力。
- **最弱信号**：`eval / reliability / production metrics / real user adoption`。

因此，如果按真实市场来放位：

- 对 **Applied AI Engineer / Agent Platform / Agent Harness / Context System / AI Deployment** 这类岗位，你已经有明显可讲的东西。
- 对 **frontier lab 的核心 RL / post-training / core model / staff-level eval infra** 这类岗位，当前公开证据还不够。

一句话概括：

> 你现在最像的是一个 **早期 L5 的 agent systems builder**，而不是一个普通 vibe coder；但你还没有把这种能力压缩成顶尖公司会立刻识别的“强 L5 作品 + 强 L5 叙事”。

## 表 1：分项目层次评估

| 资产 | 公开证据 | 当前判断 | 为什么不是更低 | 为什么还不是更高 | 下一步最值钱动作 |
|---|---|---|---|---|---|
| `gogo` | `4 stars`，`1 release`，约 `216` 个 tree entries，`82` 个 docs 条目，`68` 个 `app/` 条目，公开文档覆盖 architecture / developer guide / security boundary / session management，桌面壳 + Pi 集成 + knowledge base workflow | **扎实 L5，带 L6 视角** | 它不是单纯 wrapper，也不是单页 demo。已经包含本地知识库工作流、agent 集成、桌面壳、session、skills/schemas、可见边界和比较完整的文档体系。 | 智能核心较多委托给 `Pi`；公开证据里缺少你自己主导的 `eval / regression / reliability loop / real user telemetry`；更像高质量 prototype，而不是被真实使用验证过的长期系统。 | 选它做**旗舰项目**，补 `eval + tracing + failure taxonomy + 真实用户 case study`。 |
| `oh-share-it` | 约 `57` 个 tree entries，`20` 个 docs 条目，`11` 个测试文件，`server + cli + client + tests` 结构完整，README 明确 `share -> layer -> route -> expose to agents`，有 rules / sync / indexes / URI / routing / JSON API | **L5- 实现，L5+ 产品定义** | 它已经超过“知识库想法”阶段，进入了 file-based context layer 的可运行 MVP，并且把多人 context sharing / routing 问题拆得很清楚。 | 还是偏 MVP；公共可见证据里缺少真实团队使用、路由质量评测、冲突治理效果、长期运行数据；更强的是 framing，不是已验证的平台能力。 | 补一个**真实多人试点**，并做 `route quality eval` 与 `context recall / precision` 之类的量化说明。 |
| `my-little-chating-agent` | FastAPI + tools + web search + page reading + 本地 Markdown/FAISS + `Strategic Information Radar`，项目结构简单，几乎无测试与发布信号 | **L4+ / 早期 L5** | 它已经不只是 prompt wrapper，包含 tool use、本地索引、agent loop、scan workflow。 | 结构、测试、可靠性、部署、产品边界、评测都还偏轻；更像 exploration repo，不像长期主项目。 | 不要把它当主叙事，只把它当你进入 agent system 的**早期探索证据**。 |
| `ICASSP 2026` 论文（MEC Stackelberg game） | 顶会接受本身就是硬信号；题目体现建模、优化、策略分析能力 | **强研究补充信号，但不是 agent 主信号** | 它说明你有论文写作、形式化建模、实验 / 推导能力，不是只会“搭个应用”。 | 与 agent runtime / eval / context system 的直接相关性较弱；如果直接摆上去，容易被看成“研究背景不错，但 agent 作品未完全对齐”。 | 把它重写成“系统建模、机制设计、定量分析能力”的补充证据，而不是主叙事。 |
| 中山大学软件工程本硕 | 工科训练完整，软件工程背景和 agent 系统岗位天然兼容 | **稳定基础信号** | 它给了你进入工程型 agent 岗位的可信底座。 | 学历本身不会自动变成高端 agent 岗位信号；决定性仍是作品与叙事。 | 只保留为基础，不要把它当主卖点。 |

## 表 2：按能力维度看，你现在在哪

| 维度 | 当前层次判断 | 公开证据 | 市场会怎么解读 | 当前缺口 |
|---|---|---|---|---|
| AI 产品分层理解 | **L5+** | 你最强的 repo 都不是“聊天页”，而是在碰 `knowledge base / context / routing / harness` | 说明你知道真正难点不在 build-time，而在 runtime / context / product boundary | 还需把这种理解落成更硬的运行结果和评测结果 |
| 产品定义与架构 framing | **L5+ 到 L6-** | `gogo` 与 `oh-share-it` 的 README / docs 都有明确边界、设计原则、架构层次 | 这对 AI-native startup 很有吸引力，尤其是 agent systems / knowledge systems 团队 | 目前更多体现在文档和原型，而非被市场验证过的系统成果 |
| 工程实现与交付 | **L5-** | `gogo` 已有 release；`oh-share-it` 已有 CLI / API / tests；说明不是只停在 idea | 你不是不能做复杂项目，而是已经能把复杂项目做成一个相对完整的作品 | 缺 production-grade 的长期运行、可维护性和用户反馈证据 |
| agent runtime / harness | **L4.5 到 L5-** | `gogo` 有 Pi 集成，`oh-share-it` 明确不接管 runtime，`my-little-chating-agent` 有 agent loop | 说明你理解 harness / runtime 边界，但真正自己主导的 runtime 证据还不够厚 | 缺自己定义的 `state / eval / tracing / guardrails / handoff` 闭环 |
| eval / reliability | **L4.5** | 公开 repo 里能看到文档化的边界和部分测试，但看不到系统性的 eval 框架、offline replay、judge、regression、线上监测 | 这是你和“顶尖 agent 公司 JD”之间最明显的差距 | 需要一套可运行的 eval / regression / quality dashboard 证据 |
| research signal | **强** | ICASSP 2026 + 软件工程本硕 | 说明你不是纯应用层拼装者，有抽象和研究训练 | 需要把研究能力和 agent 方向更直接地接上 |
| public market signal | **L4.5** | `gogo` 有少量 stars 和 release；其余仓库外部采用信号较弱 | 市场会看到“有东西、会想、会做”，但还不一定立刻归类为顶尖 L5 builder | 缺更强的 adoption / feedback / external endorsement |
| 总体履历 | **早期 L5 Builder，带明显 L6 架构视角** | 三个 repo 方向一致：knowledge / context / harness / agent system | 对不少 AI-native startup 已经可聊 | 离“顶尖公司一眼认出是强 L5 / L6”还差最后一公里的证据打磨 |

## 表 3：按公司类型看当前适配度

| 公司类型 | 当前适配度 | 最合适的叙事 | 当前不匹配点 |
|---|---|---|---|
| AI-native startup：Agent / Context / Knowledge Systems | **高** | 我不是在做 generic chatbot，而是在做 `agent-facing knowledge/context/harness systems` | 需要更强的 eval / adoption 证据，把 repo 从“好原型”推到“可信工作系统” |
| AI Deployment / Forward Deployed / Applied AI | **中高** | 我能理解 workflow、context、tooling、knowledge boundary，也能把模糊问题收束成系统原型 | 缺真实客户 / 用户场景的交付案例 |
| Research Engineer（Applied / Retrieval / Evals / Product-facing） | **中** | 有研究训练，也有 agent system 作品，不是只会论文或只会搭前端 | 缺更硬的 benchmark、实验设计、eval infra 证据 |
| Coding Agent / Agent Harness 平台公司 | **中高** | `gogo` + `oh-share-it` 的主线说明你理解 harness、context surface、agent workbench | 缺更直接的 `agent quality / eval / routing / state` 工程闭环 |
| Frontier lab 的 Applied / Beneficial / Solutions / Architect 角色 | **中** | 你有系统理解，也有研究背景，方向上并不远 | 缺更成熟的 public signal 和更贴近真实部署的案例 |
| Frontier lab 的 core research / RL / post-training / staff infra | **低到中** | 有潜力，但现在不是最优切口 | 公开证据还不支持你直接去打这类最硬 bar |

## 表 4：从现在进到更强 L5 / L6，最值钱的动作

| 动作 | 建议挂靠项目 | 具体交付物 | 它补哪条市场缺口 | 预期提升 |
|---|---|---|---|---|
| 只选一个**旗舰项目** | `gogo` 优先，`oh-share-it` 次之 | 一个你未来 3 个月持续打磨的主仓库，其他项目退到 supporting evidence | 解决叙事分散 | 从“做过几个项目”变成“有一个清晰代表作” |
| 给旗舰补一套 `eval` | `gogo` 或 `oh-share-it` | `eval/` 目录、任务集、judge、回放脚本、regression cases、质量报告 | 解决顶尖 JD 最常出现的 `evaluation / quality / reliability` 缺口 | 从 L5- 往 L5 迈进 |
| 给旗舰补 `tracing / failure taxonomy / guardrails` | `gogo` | session trace、错误分层、失败案例库、权限 / handoff 说明 | 解决“不是 production system”的观感 | 更接近 harness / runtime 岗 |
| 跑一个真实试点 | `oh-share-it` 最合适 | 3-5 个真实用户或一个真实小团队，记录使用前后、典型 query、失败点、修复迭代 | 解决 adoption 和现实约束缺失 | 从原型走向真实系统 |
| 写一篇公开技术长文 | 任选旗舰 | 主题最好是 `context / harness / eval`，不是泛泛而谈，而是把设计取舍和失败过程讲清楚 | 解决“市场只看到你脑中的一部分能力” | 强化职业信号 |
| 明确做一块你自己主导的 runtime / orchestration | `gogo` 或新子模块 | 例如 model routing、state store、long-running task controller、tool execution contract | 解决“关键智能主要委托给上游 agent”问题 | 往 L6 走的核心台阶 |
| 把论文信号接回 agent | 新文章或 README 小节 | 写清你如何把建模、机制设计、定量分析能力迁移到 agent system 的 cost / incentive / routing / evaluation 问题 | 解决 paper 和项目脱节 | 提高 research-engineer 相关性 |

## 现在最该怎么讲自己

最差的讲法是：

> 我做过几个 agent 项目，也会 RAG，也会 Claude Code。

这会把你压回拥挤的 L4 池子。

更强的讲法应该是：

> 我的核心方向不是 generic AI demo，而是 agent systems 里的 `context / knowledge / harness` 问题。公开项目里，我已经分别做过：
> 
> - 本地 `llm-wiki` 工作台与 agent workbench（`gogo`）
> - 面向团队和 coding agent 的 external context layer（`oh-share-it`）
> - 一个更早期的 tool-using / local-indexed agent playground（`my-little-chating-agent`）
> 
> 我现在最想进一步补的是 eval、reliability 和 real-world deployment，把这条线从 prototype 推到 production-grade builder。

这套叙事有三个好处：

1. 它把三个 repo 收束到同一条线上。
2. 它自然对应了当前顶尖 agent 公司最常见的 JD 语言：`context / eval / harness / deployment / reliability`。
3. 它不会把你错误包装成 frontier model researcher，而是更准确地放在你目前最有竞争力的位置上。

## 当前最稳的求职定位

如果只看当前公开履历，最稳的定位是：

1. **Applied AI Engineer**
2. **Agent / Harness / Context Systems Engineer**
3. **AI Deployment / Forward Deployed Engineer**
4. **偏产品化、偏系统化的 Research Engineer**

暂时不建议把主战场放在：

- 核心 foundation model 训练
- 最硬的 RL / post-training 主线
- 需要多年大规模生产经验的 staff-level infra 岗

这不是因为你不行，而是因为**最优切口不在那里**。

## 表 5：按投递价值分成「当前匹配 / 部分匹配 / 暂不匹配」

这里的标准不是“理论上能不能投”，而是更现实的三档：

- **当前匹配**：现在投递不违和，叙事能自洽，有实际面试概率。
- **部分匹配**：方向对，但 JD 的关键硬证据还缺一块，适合精选投递。
- **暂不匹配**：不是永远不行，而是当前冷投 ROI 很低，不适合作为主战场。

| 档位 | 岗位方向 | 代表公司 / 岗位 | 当前判断 | 主要依据 | 当前缺口 |
|---|---|---|---|---|---|
| 当前匹配 | Startup AI Engineer | `Factory` / `AI Engineer` | 可主投 | 已经证明能做 agentic system prototype，不是纯理论候选人 | 缺真实用户数据与上线反馈 |
| 当前匹配 | Applied AI Engineer – Agentic Workflows | `Cohere` / workflow 类 applied 岗 | 可主投 | workflow、context、knowledge layer 理解对口 | 缺企业交付案例 |
| 当前匹配 | Software Engineer, Agents | `Harvey` / `Software Engineer, Agents` | 可主投 | 能讲 context、tools、retrieval、task system，不是 generic app | 缺 task quality 与 eval 证据 |
| 当前匹配 | Context / Knowledge Systems Engineer | context / knowledge startup | 可主投 | `gogo` + `oh-share-it` 方向高度对口 | 缺 adoption 和 ranking/eval 量化 |
| 当前匹配 | AI Product Engineer（agent workbench / knowledge tools） | AI-native startup | 可主投 | 产品 framing 和系统边界感是明显优势 | 缺 production metrics |
| 当前匹配 | Internal AI Workflow / Research Tools Engineer | 做内部 agent workflow 的团队 | 可主投 | 能把复杂知识流程收束成工具 | 缺组织内真实使用证据 |
| 部分匹配 | Applied AI Engineer, Beneficial Deployments | `Anthropic` | 可精选投 | context / harness / prototyping 语言是对口的 | 缺 partner-facing deployment 证据 |
| 部分匹配 | Forward Deployed Engineer / Applied AI Deployment | `Anthropic` / `OpenAI` / `Cohere` | 可精选投 | 能讲系统、能做 prototype | 缺客户交付与跨职能上线实战 |
| 部分匹配 | Software Engineer, Agent Harness | `Cursor` | 可精选投 | 主线方向很接近 harness | 缺更硬的 runtime ownership |
| 部分匹配 | Software Engineer, Agent Evaluation and Quality | `Cursor` | 可精选投 | 知道 eval 重要性，方向直觉对 | 公开证据里没有成熟 eval infra |
| 部分匹配 | Software Engineer, Agent Architecture / SDK | `Sierra` | 可精选投 | `oh-share-it` / `gogo` 都能讲 agent primitives | 缺 production-grade runtime / SDK 深度 |
| 部分匹配 | Software Engineer, Applied AI / Context Layer | `Perplexity` | 可精选投 | `context / retrieval / knowledge layer` 方向高度相关 | 缺大规模 user-facing AI product 经验 |
| 部分匹配 | Senior Software Engineer, Agent Platform | `Replit` | 可精选投 | agent platform 方向对口 | “Senior” 往往要求更强系统资历 |
| 部分匹配 | Senior Software Engineer, Agent Infrastructure | `Cohere` | 可精选投 | 懂 agent infra 问题域 | 缺 secure execution / auth / state mgmt 硬证据 |
| 部分匹配 | Research Engineer, Codex / coding agents | `OpenAI` | 可精选投 | 有研究信号，也有 agent systems 项目 | research + eval + scale 还不够硬 |
| 部分匹配 | Software Engineer, Agent Infrastructure | `OpenAI` | 可精选投 | 主线方向对口 | 平台复杂度、生产规模证据不足 |
| 暂不匹配 | Model Quality Software Engineer, Claude Code | `Anthropic` | 不宜主投 | 明确偏 Staff 级、eval infra 负责人画像 | 缺大规模 owned systems 证据 |
| 暂不匹配 | Research Engineer, Model Evaluations | `Anthropic` | 不宜主投 | 要求更强评测研究与 live checkpoint 经验 | 缺系统性 eval 研究履历 |
| 暂不匹配 | Research Engineer, Virtual Collaborator (Cowork) | `Anthropic` | 不宜主投 | 更接近 frontier product-facing RL / ML bar | 缺强 ML / RL 主线 |
| 暂不匹配 | Staff+ AI Reliability / Agent Infra / Inference | `OpenAI` / `Anthropic` / `Cohere` | 不宜主投 | 这是多年 production + scale + ownership bar | 当前证据离 staff-level 还远 |

## 表 6：最适合投的 20 个岗位方向

按实际投递价值排序。前 1-8 适合作为主投方向，9-16 适合作为精选投递，17-20 暂缓。

| 排名 | 岗位方向 | 当前判断 | 备注 |
|---:|---|---|---|
| 1 | Startup AI Engineer | 当前匹配 | 适合把作品能力直接转成岗位语言 |
| 2 | Applied AI Engineer – Agentic Workflows | 当前匹配 | 对接 workflow / context / enterprise AI |
| 3 | Software Engineer, Agents（vertical AI） | 当前匹配 | 适合 Harvey 一类垂直 agent 公司 |
| 4 | Context / Knowledge Systems Engineer | 当前匹配 | 最能利用 `gogo` + `oh-share-it` 的独特性 |
| 5 | AI Product Engineer（agent workbench / knowledge tools） | 当前匹配 | 利用产品定义与系统组织能力 |
| 6 | Internal AI Workflow Engineer | 当前匹配 | 适合知识工作流、内部工具、研究工具类团队 |
| 7 | Research Tools / AI Workbench Engineer | 当前匹配 | 贴近本地知识库与 workbench 方向 |
| 8 | AI-native startup Founding / Early Engineer（knowledge/agent niche） | 当前匹配偏谨慎 | 更吃方向感与作品集 |
| 9 | Applied AI Engineer, Beneficial Deployments | 部分匹配 | 适合定制投递 |
| 10 | Forward Deployed Engineer, Applied AI | 部分匹配 | 需要补交付叙事 |
| 11 | Software Engineer, Agent Harness | 部分匹配 | 需要补 runtime / harness 证据 |
| 12 | Software Engineer, Agent Evaluation and Quality | 部分匹配 | 需要补 eval 体系 |
| 13 | Software Engineer, Agent Architecture / SDK | 部分匹配 | 需要补 platform / SDK 深度 |
| 14 | Software Engineer, Applied AI / Context Layer | 部分匹配 | 需要补大规模产品面 |
| 15 | Senior Software Engineer, Agent Platform | 部分匹配 | senior 信号偏弱 |
| 16 | Agent Infrastructure Engineer | 部分匹配 | 要求更强系统工程实绩 |
| 17 | Research Engineer, Codex / coding agents | 部分匹配偏低 | 可投，但不应当主战场 |
| 18 | Model Quality Software Engineer, Claude Code | 暂不匹配 | staff-level eval infra bar |
| 19 | Research Engineer, Model Evaluations | 暂不匹配 | 更偏 frontier eval research |
| 20 | Frontier virtual collaborator / product-facing RL research | 暂不匹配 | 当前不该消耗主火力 |

## 补充来源：miromind 对当前履历的一次外部评估

另一个外部材料 `raw/external/miromind-profile-evaluation-barytes-2026-05.md` 给出了一版更保守的定位：

> **高配初级（Entry-level 上沿）到 Early Mid 的过渡阶段。**

它的核心理由是：

- `oh-share-it`、`gogo`、`my-little-chating-agent` 都明显超过“只会调 API 的 demo”；
- 但公开证据里仍然缺少：
  - 云端生产部署；
  - 容器化与 K8s；
  - metrics / tracing / dashboard；
  - 真实业务环境下运行一段时间的证明；
  - 更典型的 SRE / 运维 / 故障排查证据。

这份外部评估和本页原有判断并不完全相同，但有明显重合：

- 它把重点压在**工程落地证据不足**；
- 它更愿意用传统招聘市场语言，把你放在 `Junior → Early Mid` 之间；
- 它比本页原先的 “早期 L5 / L5-” 说法更保守，因为它更看重 production deployment 这条证据链。

## 表 7：本页判断与 miromind 判断的对照

| 维度 | 本页原判断 | miromind 补充判断 | 可并存的解释 |
|---|---|---|---|
| 对普通 L4 demo 选手的相对位置 | 明显更高 | 明显更高 | 二者一致。都认为你不是“只会 Claude Code / RAG”的候选人。 |
| 分层主标签 | 早期 L5 / L5- | Entry 上沿 → Early Mid | 分歧主要来自是否把 `产品 / 架构 / 系统定义能力` 也计入层级，而不只看 production 运维证据。 |
| 最强项 | `context / knowledge / harness` 的 framing 与作品完整度 | 架构清晰、子系统边界、完整 Agent 应用能力 | 二者基本一致。 |
| 最大短板 | eval / reliability / adoption / runtime ownership | deployment / containerization / observability / real business usage | 其实是同一组问题的不同表述：缺少更硬的生产级证据。 |
| 对 `gogo` 的看法 | 扎实 L5，带 L6 视角，但更像高质量 prototype | 高质量个人作品 / prototype，不足以证明长期稳定运营 | 二者都承认 `gogo` 强在 framing 与完整度，弱在生产级验证。 |
| 对 `oh-share-it` 的看法 | L5- 实现，L5+ 产品定义 | 系统设计和代码完整度超出典型 Junior，但未到公司级平台线 | 这两种说法本质接近，只是命名体系不同。 |
| 对 `my-little-chating-agent` 的看法 | L4+ / 早期 L5 | 完全满足 Entry-level，且实现干净，但未到可维护中级线 | 二者都把它看成 strong entry artifact，而不是中级代表作。 |

## 更冷一点的招聘方视角

如果站在招聘方角度，你当前最像的是：

- 一个**方向判断明显优于普通候选人**的人；
- 一个**已经做出高质量原型**的人；
- 但还不是一个能只凭履历就被稳定归类为“强 L5 builder”的人。

招聘方看到你，通常会同时产生两种判断：

### 会被认可的部分

- 不是浅层 `Claude Code + RAG` 选手；
- 有 `context / knowledge / harness` 这一条清晰主线；
- 有系统感、文档感和边界感；
- 不是只会“搭个页面”，而是能把项目做到完整作品形态。

### 会被怀疑的部分

- 这些系统到底有多少真实使用；
- 质量怎么评估，可靠性怎么证明；
- runtime / orchestration 到底有多少是你自己主导；
- 能不能在团队环境里持续把系统做稳，而不只是做出聪明原型；
- deployment、observability、线上稳定性这些工程环节到底补到了什么程度。

更压缩的结论是：

> 当前公开履历已经足够让很多 AI-native startup 愿意“聊一聊”，但还不足以让顶尖 agent 团队只看材料就默认你是稳妥的核心 builder。

## 最终判断

如果把人的 L3-L6 分层和市场可见证据分开看：

- **你的内在能力结构**：已经明显超过 L4，进入 **L5 Builder**，并带有很强的 L6 架构直觉。
- **你的公开履历证据**：当前最合理的判断是 **早期 L5 / L5-**。
- **离更强 L5 的最后一公里**：不是再做一个新项目，而是把现有主线项目补上 `eval / reliability / real use / sharper narrative`。
- **离 L6 的关键台阶**：不是概念更大，而是你亲自主导更多 `runtime / orchestration / contract / long-running execution`。

一句话结尾：

> 你现在最需要的，不是证明自己“也会 agent”，而是把自己已经明显存在的 `context / harness / knowledge systems builder` 能力，压缩成顶尖公司一眼能识别的 L5 证据包。

## 相关页面

- [gogo：本地 llm-wiki 桌面应用](../knowledge/gogo.md)
- [Agent 岗位 JD 抽样与能力信号](../knowledge/Agent岗位JD抽样与能力信号.md)
- [oh-share-it 公共知识库产品](oh-share-it公共知识库产品.md)
- [职业信号与叙事框架](../frameworks/职业信号与叙事框架.md)
- [AI 系统产品判断框架](../frameworks/AI系统产品判断框架.md)
- [职业决策与求职策略观察](../self/职业决策与求职策略观察.md)
- [Go to Market 策略](../self/go-to-market-strategy.md)
