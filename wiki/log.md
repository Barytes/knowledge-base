# 日志

把这个文件当成追加式活动日志来用。

## [2026-06-25] query | 外部教育 demo 与 Agent infra 主线边界

更新 [Agent infra 目标一致性判断（2026-06-20）](topics/projects-roadmaps/Agent-infra目标一致性判断-2026-06-20.md)，补入外部教育 demo 的边界判断：若 demo 只承担真实 workload、低并发试点、数据建模、AI workflow、eval、trace 和 failure taxonomy，它可以服务 `Agent Systems Engineer` 主线；若开始承诺生产级后端、万人级扩展、教培运营和完整教育平台责任，则应引入生产级系统经验者，并避免把该项目升级成独立主线。

## [2026-06-24] query | 计划挫败与能力焦虑归因

更新 [产品判断力与能力焦虑的分离观察](self/产品判断力与能力焦虑分离观察.md)，补入“很多计划没有实现时，不要直接归因为能力不行”的判断：顶尖人才密度确实提高复杂项目实现概率，但个人计划失败更常混合方向、执行、反馈、资源、协作密度和失败处理系统等多层问题。页面将“清北 / 斯坦福 / IMO / Cursor”式比较收束为可诊断的能力与资源拆分，而不是总括性的自我否定。

## [2026-06-22] ingest | Superlinear Academy 课程与洞见全量归档

使用已登录的 in-app browser 摄取 Superlinear Academy 左侧导航“课程与洞见”分组下 7 个空间的全部可见内容，共 535 条 lesson / post。原文归档为 `raw/external/superlinear-academy-course-insights-2026-06-22/`，其中 `manifest.json` 保存空间和 URL 清单，`pages.jsonl` 保存逐条原文、标题、链接和正文。新增维护页 [Superlinear Academy 课程与洞见总索引](topics/ai-product-product-definition/superlinear-academy-course-insights-index.md)，把材料收束为 AI Builder / AI Architect / Agentic AI 课程地图、Knowledge Bank 主题簇和 Deep News 趋势雷达，并同步更新 [AI 产品 / 产品定义 / 验证](topics/ai-product-product-definition/index.md)。

## [2026-06-20] query | 失败处理系统与职业路径风险

根据一次围绕“读博还是进入市场”的家庭对话，新增 [失败处理系统与职业路径风险](topics/career-positioning-job-search/失败处理系统与职业路径风险.md)。页面把父亲关于失业、稳定路径和尾部风险的提醒吸收进职业决策框架，同时区分“不接受博士作为唯一解法”和“不忽略市场失败风险”，将“不能靠信念硬扛失败”收束为一个带现金流、外部反馈、资产沉淀、失败分级和转向触发器的最小系统。同步更新 [职业 / 定位 / 求职](topics/career-positioning-job-search/index.md)。

## [2026-06-20] query | Agent infra 目标一致性判断

根据用户对 `founder-skill`、`oh-share-it` 与 agent infra / context infra 主线是否一致的疑问，新增 [Agent infra 目标一致性判断（2026-06-20）](topics/projects-roadmaps/Agent-infra目标一致性判断-2026-06-20.md)。页面把 `context-core` 定为主线核心，`oh-share-it` 定为真实部署和评测面，`my-little-agent-loop` / `agent-harness-core` 定为 runtime ownership 支撑，并把 `founder-skill` 收束为 workload / eval case / human-first workflow 案例，避免膨胀成独立主线。同步更新 [项目 / 路线图 / 执行计划](topics/projects-roadmaps/index.md)。

## [2026-06-17] ingest | Context Engine 与 AI Infra 抗模型吞噬地图

从用户粘贴的概念讨论中摄取 `Context Engine`、`LLM Wiki`、上下文测评和 AI Infra future-proof 判断。源文件归档为 `raw/personal/conversations/context-engine-ai-infra-2026-06-17.md`。新增 [Context Engine：上下文编排层](topics/context-memory-knowledge-system/context-engine.md)，把 Context Engine 和 RAG、memory、LLM Wiki、agent runtime、eval 的边界拆清，并补入最小可行测评方法。新增 [AI Infra 的抗模型吞噬地图](topics/ai-industry-investment/AI-Infra的抗模型吞噬地图.md)，把 AI Infra 分成容易被模型吞掉、需要做深、以及更 future proof 的方向。同步更新相关 topic 索引。

## [2026-06-15] query | 课题组网站低响应启动策略

根据“经验贴 + 成员信息”课题组网站在群里初次发起后响应较少的情境，新增 [课题组网站的低响应启动策略](topics/research-knowledge-governance/课题组网站的低响应启动策略.md)。页面把低响应解释为弱信号而非需求否定，并建议采用发起人样板、私聊小请求、成员信息 opt-in、展示成品后再群发的启动方式。同步更新 [研究知识库 / 公共知识治理](topics/research-knowledge-governance/index.md)。

## [2026-06-12] query | Google DeepMind 多智能体安全资金池

按用户要求在线追踪 Google DeepMind、Schmidt Sciences、ARIA、Cooperative AI Foundation 和 Google.org 的 1000 万美元多智能体安全资助新闻。新增 [Google DeepMind 多智能体安全资金池](topics/agent-harness-runtime/Google-DeepMind多智能体安全资金池.md)，把新闻信号收束为 agent safety 从单 agent 行为扩展到 multi-agent runtime、protocol、真实沙盒、身份权限、可观测性和系统性风险研究的结构变化。同步更新 [Agent / Harness / Runtime](topics/agent-harness-runtime/index.md)。

继续追踪新闻中的 Google 相关工作线、组织和人物网络，新增 [Google 多智能体安全相关工作与组织人物地图](topics/agent-harness-runtime/Google多智能体安全相关工作与组织人物地图.md)。页面把 Google DeepMind 的 AGI safety、A2A、Concordia、SIMA / embodied agents、Evals、AP2 / agentic commerce 与 Schmidt Sciences、ARIA、CAIF、Google.org 的角色分工放到一张图里，并整理 Rohin Shah、James Fox、Lewis Hammond、Thore Graepel、Joel Leibo、Allan Dafoe、Alex Obadia 等关键人物。

## [2026-06-12] ingest | Getting a Seat at the Table as a Data Scientist

从用户提供的 Markdown 剪藏摄取 Yuzheng Sun 的《Getting a Seat at the Table as a Data Scientist》，源文件归档为 `raw/external/Getting a Seat at the Table as a Data Scientist.md`。新增维护入口页 [Data Scientist 的决策桌位置](topics/career-positioning-job-search/Data%20Scientist的决策桌位置.md)，并把材料拆成具体话题页：[数据科学家的三种角色](topics/career-positioning-job-search/数据科学家的三种角色.md)、[分析型 DS 的 AI 替代风险](topics/career-positioning-job-search/分析型DS的AI替代风险.md)、[数据科学家的可信数据与判断](topics/career-positioning-job-search/数据科学家的可信数据与判断.md)、[数据科学家的决策影响力武器](topics/career-positioning-job-search/数据科学家的决策影响力武器.md)。同步更新 [真本事：从会工作到会赚钱](topics/career-positioning-job-search/真本事-从会工作到会赚钱.md)、[AI 让我们重新开始享受自己的职业](topics/career-positioning-job-search/AI%20让我们重新开始享受自己的职业.md) 与 [Go to Market Multiple Times](topics/ai-product-product-definition/go-to-market-multiple-times.md)，把 DS 决策影响力接回已有职业、AI 与产品验证框架。

## [2026-06-05] update | 纳瓦尔 Part II 幸福与哲学话题展开

补齐《纳瓦尔宝典》Part II 的 Happiness、Saving Yourself 和 Philosophy 具体话题页。新增 [幸福是选择](topics/learning-judgment-mental-models/幸福是选择.md)、[幸福需要在场](topics/learning-judgment-mental-models/幸福需要在场.md)、[幸福需要平静](topics/learning-judgment-mental-models/幸福需要平静.md)、[成功不等于幸福](topics/learning-judgment-mental-models/成功不等于幸福.md)、[幸福习惯](topics/learning-judgment-mental-models/幸福习惯.md)、[接受现实](topics/learning-judgment-mental-models/接受现实.md)、[选择成为自己](topics/learning-judgment-mental-models/选择成为自己.md)、[自我照顾与健康](topics/learning-judgment-mental-models/自我照顾与健康.md)、[冥想与心理强度](topics/learning-judgment-mental-models/冥想与心理强度.md)、[构建自己](topics/learning-judgment-mental-models/构建自己.md)、[成长自己](topics/learning-judgment-mental-models/成长自己.md)、[自由自己](topics/learning-judgment-mental-models/自由自己.md)、[人生意义](topics/learning-judgment-mental-models/人生意义.md)、[价值观](topics/learning-judgment-mental-models/价值观.md)、[理性佛教](topics/learning-judgment-mental-models/理性佛教.md) 与 [当下是全部](topics/learning-judgment-mental-models/当下是全部.md)。同步更新 [纳瓦尔与穷查理主题地图](topics/learning-judgment-mental-models/纳瓦尔与穷查理主题地图.md)，使 Naval 全书目录中的主要章节均有对应话题页入口。

## [2026-06-05] update | 纳瓦尔 Part I 具体话题展开

继续把《纳瓦尔宝典》从总览页拆成具体话题页。新增 [纳瓦尔宝典具体话题索引](topics/learning-judgment-mental-models/纳瓦尔宝典具体话题索引.md)，并首批展开 Part I 中的财富与判断主题：[财富如何被创造](topics/learning-judgment-mental-models/财富如何被创造.md)、[长期游戏与长期的人](topics/learning-judgment-mental-models/长期游戏与长期的人.md)、[建立或购买企业股权](topics/learning-judgment-mental-models/建立或购买企业股权.md)、[以判断力获得报酬](topics/learning-judgment-mental-models/以判断力获得报酬.md)、[优先级与专注](topics/learning-judgment-mental-models/优先级与专注.md)、[像玩一样工作](topics/learning-judgment-mental-models/像玩一样工作.md)、[如何获得好运](topics/learning-judgment-mental-models/如何获得好运.md)、[耐心](topics/learning-judgment-mental-models/耐心.md)、[清晰思考](topics/learning-judgment-mental-models/清晰思考.md)、[放下身份看现实](topics/learning-judgment-mental-models/放下身份看现实.md)、[决策技能](topics/learning-judgment-mental-models/决策技能.md) 与 [阅读与经典](topics/learning-judgment-mental-models/阅读与经典.md)。同步更新 [纳瓦尔宝典](topics/learning-judgment-mental-models/纳瓦尔宝典.md) 和 [纳瓦尔与穷查理主题地图](topics/learning-judgment-mental-models/纳瓦尔与穷查理主题地图.md)。

## [2026-06-05] update | 穷查理心理误判二十五项逐页展开

继续扩展《穷查理宝典》的具体模型层。将 Munger 在“The Psychology of Human Misjudgment”中列出的二十五项心理误判全部拆成独立 wiki 页，包括奖励与惩罚超级反应、喜欢/讨厌倾向、避免怀疑、避免不一致、嫉妒、互惠、社会证明、权威误导、废话倾向、尊重理由倾向与 Lollapalooza 心理倾向等。同步更新 [心理误判清单](topics/learning-judgment-mental-models/心理误判清单.md)、[穷查理宝典具体模型索引](topics/learning-judgment-mental-models/穷查理宝典具体模型索引.md) 与 [纳瓦尔与穷查理主题地图](topics/learning-judgment-mental-models/纳瓦尔与穷查理主题地图.md)，让每个具体误判都能从索引页和站点搜索进入。

## [2026-06-05] update | 纳瓦尔与穷查理主题展开

开始把《纳瓦尔宝典》和《穷查理宝典》从单页摘要扩展为可检索、可互链的主题页面组。新增 [纳瓦尔与穷查理主题地图](topics/learning-judgment-mental-models/纳瓦尔与穷查理主题地图.md)，先落地财富、Specific Knowledge、Accountability、杠杆、长期游戏、判断力、逆向、激励、心理误判、幸福和欲望/接受等主题页。

根据“不要只囊括大主题”的反馈，进一步新增 [穷查理宝典具体模型索引](topics/learning-judgment-mental-models/穷查理宝典具体模型索引.md)，并首批展开 [Latticework of Mental Models](topics/learning-judgment-mental-models/Latticework-of-Mental-Models.md)、[Invert, Always Invert](topics/learning-judgment-mental-models/Invert-Always-Invert.md)、[能力圈](topics/learning-judgment-mental-models/能力圈.md)、[激励导致的偏误](topics/learning-judgment-mental-models/激励导致的偏误.md)、[Lollapalooza Effect](topics/learning-judgment-mental-models/Lollapalooza-Effect.md) 与 [检查清单与实践思考](topics/learning-judgment-mental-models/检查清单与实践思考.md)。后续仍需按索引逐项补齐心理误判二十五项、投资与商业判断模型、学习模型和人格伦理话题。

## [2026-06-05] ingest | 穷查理宝典

从用户提供的 PDF 摄取 Charles T. Munger 的 *Poor Charlie's Almanack: The Wit and Wisdom of Charles T. Munger, Expanded Third Edition*，源文件复制归档为 `raw/external/poor-charlies-almanack-2023.pdf`。新增维护页 [穷查理宝典](topics/learning-judgment-mental-models/穷查理宝典.md)，把材料收束为判断力训练入口：多元 mental models、latticework、逆向思考、激励、lollapalooza effect、能力圈、少数重注与心理误判清单。

**新增页面**
- [穷查理宝典](topics/learning-judgment-mental-models/穷查理宝典.md)

**更新页面**
- `wiki/topics/learning-judgment-mental-models/index.md`
- `wiki/topics/learning-judgment-mental-models/naval-mental-models.md`

**源文件新增**
- `raw/external/poor-charlies-almanack-2023.pdf`

## [2026-05-30] ingest | The Founder's Playbook

从用户提供的 PDF 摄取 Claude《The Founder's Playbook: Building an AI-Native Startup》，源文件归档为 `raw/external/the-founders-playbook-2026-05.pdf`，并新增 source note `raw/external/the-founders-playbook-2026-05.md`。新增维护页 [The Founder's Playbook：AI-native startup 的阶段纪律](topics/ai-product-product-definition/the-founders-playbook-ai-native-startup.md)，把材料收束为 AI-native startup 的 Idea / MVP / Launch / Scale 四阶段纪律：AI 压缩执行周期，但 founder 更需要验证、架构、scope、metrics、security 与运营系统化。

**新增页面**
- [The Founder's Playbook：AI-native startup 的阶段纪律](topics/ai-product-product-definition/the-founders-playbook-ai-native-startup.md)

**更新页面**
- `wiki/topics/ai-product-product-definition/index.md`

## [2026-06-30] ingest | 摄取 dogfooding 做产品方法论来源

继续检索并保存 dogfooding / eating your own dog food 相关产品方法论材料，覆盖 Joel Spolsky、Graphite、GitLab Customer 0、GitLab R&D dogfooding、IBM Cloud、智能家居研究和 Codex agentic AI 相关案例。新增主题页将 dogfooding 定义为产品验证链条中的内部真实使用层，重点区分真实任务验证、低频关键路径、基础设施可靠性验证，以及它不能替代外部用户研究的边界。

**新增原始材料**
- `raw/external/dogfooding-product-sources/`

**新增页面**
- `wiki/topics/ai-product-product-definition/Dogfooding作为产品验证机制.md`

**更新页面**
- `wiki/topics/ai-product-product-definition/index.md`
- `wiki/frameworks/产品验证判断框架.md`

## [2026-06-30] query | 补充陈子深项目 dogfooding 与市场调研顺序判断

围绕陈子深 AI 教育项目当前找方向的问题，补充一条产品验证判断：不应在“先做给自己用的完整 dogfooding 产品”和“先做泛市场调研”之间二选一，而应先做内部诊断工作台，用它产出一道题的错因诊断样本，再立刻拿给小样本真实老师和学生验证。核心边界是：dogfooding 验证任务路径和样本生产能力，外部验证才判断学生 aha moment、老师教学动作改变和需求强度。

**更新页面**
- `wiki/topics/ai-product-product-definition/陈子深AI教育项目notebook-idea整理.md`
- `wiki/topics/ai-product-product-definition/pre-pmf-validation-playbook.md`
- `wiki/frameworks/产品验证判断框架.md`

**源文件新增**
- `raw/external/the-founders-playbook-2026-05.pdf`
- `raw/external/the-founders-playbook-2026-05.md`

## [2026-05-29] ingest | Claude Code Dynamic Workflows

按用户提供链接摄取 Claude 官方博客《Introducing dynamic workflows in Claude Code》。新增 `raw/external/claude-code-dynamic-workflows.md` source note 与维护页 [Claude Code Dynamic Workflows](topics/agent-harness-runtime/claude-code-dynamic-workflows.md)，把 dynamic workflows 收束为 Claude Code 的内建多 subagent workflow layer：动态规划、并行 fan out、独立验证、adversarial checking、长任务恢复与更高 token 成本。

**新增页面**
- [Claude Code Dynamic Workflows](topics/agent-harness-runtime/claude-code-dynamic-workflows.md)

**更新页面**
- `wiki/topics/agent-harness-runtime/claude-code-harness.md`
- `wiki/topics/agent-harness-runtime/index.md`
- `wiki/frameworks/Harness架构判断框架.md`

**源文件新增**
- `raw/external/claude-code-dynamic-workflows.md`

## [2026-05-28] ingest | Agent 系统作为 OS 与 Cloud Runtime 问题

从 `inbox/` 摄取外部文章《Agent 系统正在重新走一遍 OS 和 Cloud Runtime 的老路》，移入 `raw/external/`，并新增知识页。页面把材料收束为 agent runtime 的系统工程视角：`context window` 不是 runtime，append-only session log 类似 event sourcing，brain / hands 对应 control plane / data plane，sandbox 趋向 disposable runtime，稳定接口比具体实现更重要。

随后按用户要求联网搜索并摄取 Anthropic Engineering 官方原文《Scaling Managed Agents: Decoupling the brain from the hands》。新增一个 `raw/external/` source note，并更新知识页，把官方 Managed Agents 的 `session / harness / sandbox` 三对象、`execute / provision / wake / getEvents` 接口、凭证隔离、TTFT 改善和 `meta-harness` 判断补入同一页。随后将 source note 扩成原文结构化摄取版，按原文章节覆盖论证与工程细节，但不全文镜像受版权保护的原文。

**新增页面**
- [Agent 系统作为 OS 与 Cloud Runtime 问题](topics/agent-harness-runtime/agent-runtime-os-cloud-runtime.md)

**更新页面**
- `wiki/index.md`
- `wiki/knowledge/AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md`
- `wiki/knowledge/harness-engineering.md`
- `wiki/frameworks/Harness架构判断框架.md`

**源文件移至**
- `raw/external/agent-runtime-os-cloud-runtime.md`
- `raw/external/anthropic-scaling-managed-agents.md`

## [2026-05-26] query | Agent harness core 与三种 adapter 路线

根据用户关于“也许做三个 agent harness”的 brainstorming，新增一页 bridge，将想法收束为 `agent-harness-core` 加三个 demo / adapter：`context-eval-adapter`、`clawhouse-continuity-adapter`、`companion-desktop-adapter`。页面明确三者共享 session、tool runtime、permission、trace、replay、eval、patch 和 context bridge，区别在于分别证明 context quality、task continuity 和 ambient collaboration。

**新增页面**
- [Agent harness core 与三种 adapter 路线](topics/projects-roadmaps/Agent-harness-core与三种adapter路线.md)

**更新页面**
- `wiki/index.md`
- `wiki/bridges/Codex-like-agent-harness路线图.md`
- `wiki/bridges/Agent系统月度执行计划-2026-05-24.md`

## [2026-05-26] query | Codex-like agent harness 路线图

根据用户提出的“把 `my-little-agent-loop` 做成 Codex-like agent harness”的想法，新增一页 bridge。页面将 Codex-like 压缩为可实现的 harness 能力组合：session、tool runtime、permission / sandbox、plan / todo、patch、trace / replay、eval harness 和 skill system，并明确它本月仍作为 `context-core` 与 `oh-share-it` 的支撑项，而不是新的旗舰主线。

**新增页面**
- [Codex-like agent harness 路线图](topics/projects-roadmaps/Codex-like-agent-harness路线图.md)

**更新页面**
- `wiki/index.md`
- `wiki/bridges/Agent系统月度执行计划-2026-05-24.md`

## [2026-05-25] query | Agent Context Infra 前沿调研

基于既有 `Agent Context Infra 调研报告（2026-05-24）`、相关 framework 页和外部前沿资料，新增一篇 2026-05-25 版桥接调研页。新版把主线从“agent memory / RAG”进一步收束为 `context lifecycle layer`，补入 Anthropic Managed Agents filesystem memory、STATE-Bench、MemGym、LongMemEval-V2、GroupMemBench、Cloudflare Session/context blocks、OpenViking context file system 等信号，并形成缺口地图、机会地图和 2-4 周研究产物路线。

**新增页面**
- `wiki/bridges/agent-context-infra-2026-05-25.md`

**更新页面**
- `wiki/index.md`
- `wiki/log.md`

## [2026-05-25] query | Context-Core 技术前沿机制级调研

按用户要求重新收窄到 context layer / context-core，不再讨论 MCP、OpenAI SDK 等连接或通用 runtime 层。逐一浏览前沿论文和项目源页后，新增机制级技术报告，按技术判断、工作机制、技术创新、重点难点和未来方向解读 memory/context-control/context-file-system/context-eval/context-governance 相关工作。报告补入 MemRouter、MemConflict、Mem-π、Memory-R2、MementoGUI、Parallel Context Compaction、WorldDB、Letta Context Repositories 等新近信号，并将 `context-core` 收束为 episode store、working state、write gate、structured memory、governance、context filesystem、experience layer 和 eval/replay 八层架构。

**新增页面**
- `wiki/bridges/context-core-technical-frontier-2026-05-25.md`

**更新页面**
- `wiki/index.md`
- `wiki/log.md`

## [2026-05-24] 查询/写回 | Agent 系统月度执行计划

将“一个月内把 `gogo`、`oh-share-it`、`my-little-agent-loop` 打造成可以写进简历的生产级旗舰项目”的目标拆成四周执行计划。计划以 `oh-share-it` 真实试点与 eval 为主体，`gogo` 作为 workbench / portfolio 入口，`my-little-agent-loop` 补 trace / replay / evaluator loop 的 runtime ownership，同时保留行业研究、求职外联和博弈论低维结构支线。

随后按用户澄清更新计划：新增 `context-core` 作为本月核心主线，弱化 `gogo`，明确 `gogo` 不再主动改动，只作为已有 workbench / demo / portfolio 入口。

**新增页面**
- [Agent 系统月度执行计划（2026-05-24）](topics/projects-roadmaps/Agent系统月度执行计划-2026-05-24.md)

**更新页面**
- `wiki/index.md`

## [2026-05-23] 查询/写回 | Agent 系统求职与项目路线图

围绕“论文结束后如何重新整理项目、行业学习、求职和博弈论研究支线”做本地知识库查询与综合。结论是继续以 `Agent Systems Engineer` 为主线，把 `gogo / oh-share-it` 打成可部署、可评测、被真实使用的 agent context infra 旗舰证据包，用 `my-little-agent-loop` 补 runtime ownership，把 `clawhouse` 放在低成本探索轨，同时让行业学习和求职围绕同一画像外化。

**新增页面**
- [Agent 系统求职与项目路线图（2026-05）](topics/projects-roadmaps/Agent系统求职与项目路线图-2026-05.md)

**更新页面**
- `wiki/index.md`

## [2026-05-15] 查询/写回 | Anthropic / OpenAI Agent Systems 履历 North Star

基于已经整理好的 `Anthropic`、`OpenAI` 及相邻 agent systems JD 抽样，以及已有的 GitHub 履历评估，新增一页 bridge，把“顶尖 agent systems 团队到底想看到什么样的履历画像”压成一版 north star，并加入当前公开履历与该目标画像的差距表。

**新增页面**
- [Anthropic与OpenAI的Agent Systems履历North Star](topics/career-positioning-job-search/Anthropic与OpenAI的Agent%20Systems履历North%20Star.md): 从 JD 倒推 `context / harness / runtime / eval / deployment / reliability` 目标画像,并把当前履历与该 north star 的差距按重要性排序。

**更新页面**
- `wiki/index.md`

## [2026-05-13] 查询/写回 | Agent Systems Engineer 职业定位

基于当前对 agent 市场需求、公开 JD 抽样、已有项目主线与用户自我澄清，把“不是用 AI build product，而是围绕 context / harness / evaluation / reliability 做更深一层 agent 系统”的方向压成一页职业定位 bridge。

**新增页面**
- [Agent Systems Engineer职业定位](topics/career-positioning-job-search/Agent%20Systems%20Engineer职业定位.md): 定义这条职业主线与 `AI Product Manager` / generic AI builder 的区别、市场需求基础、适配岗位与对外表达模板。

**更新页面**
- `wiki/index.md`

## [2026-05-13] 查询/写回 | GitHub 项目与 Agent 履历层次评估

基于公开 GitHub API 元数据、README、公开 docs、manifest，以及公开招聘 JD 抽样，对 `Barytes/gogo`、`Barytes/oh-share-it`、`Barytes/my-little-chating-agent`、`ICASSP 2026` 论文与教育背景做了一次不 clone 仓库的层次评估，并写回一页 bridge。随后又补入“当前匹配 / 部分匹配 / 暂不匹配”的投递分层与 20 个优先岗位方向。

同日，再把一份用户提供的 `miromind` 二次整理材料摄取到 `raw/external/miromind-agent-jd-market-scan-2026-05.md`，并更新 [Agent 岗位JD抽样与能力信号](topics/career-positioning-job-search/Agent岗位JD抽样与能力信号.md)，补充传统企业 / 重行业场景岗位、五档经验梯度、薪资带、治理与安全要求，以及 AI-native startup bar 与 enterprise bar 的差异。

随后又把另一份 `miromind` 对用户 GitHub / 论文 / 教育背景的二次评估摄取到 `raw/external/miromind-profile-evaluation-barytes-2026-05.md`，并更新 [Barytes GitHub项目与Agent层次评估](topics/career-positioning-job-search/Barytes-GitHub项目与Agent层次评估.md)，补入一版更保守的外部定位（Entry 上沿 → Early Mid）及其与本页原判断的对照。

**新增页面**
- [Barytes GitHub项目与Agent层次评估](topics/career-positioning-job-search/Barytes-GitHub项目与Agent层次评估.md): 用 L3-L6、runtime / eval /职业信号三组尺子评估当前公开履历,补入投递分层与 20 个岗位方向,并给出从早期 L5 走向更强 L5/L6 的补强动作。
- [Agent 岗位JD抽样与能力信号](topics/career-positioning-job-search/Agent岗位JD抽样与能力信号.md): 把本轮公开招聘页抽样整理成可复用表格,并补入 miromind 提供的企业化 JD 梯度、薪资带与治理 / 安全 / domain 要求。

**更新页面**
- `wiki/index.md`
- `wiki/bridges/Barytes-GitHub项目与Agent层次评估.md`
- `wiki/knowledge/Agent岗位JD抽样与能力信号.md`

**源文件新增**
- `raw/external/miromind-agent-jd-market-scan-2026-05.md`
- `raw/external/miromind-profile-evaluation-barytes-2026-05.md`

## [2026-05-01] 摄取 | 给华为高管表哥的自我介绍

从 `inbox/` 摄取一份个人写作，移入 `raw/personal/writings/`，并提炼两条 self observation：求职策略的具体展开、投简历恐惧的心理卡点。

**新增页面**
- [投简历恐惧观察](self/投简历恐惧观察.md)：非标准履历对简历投放机制的心理卡点

**更新页面**
- [职业决策与求职策略观察](self/职业决策与求职策略观察.md)：补充不读博的增量理由、具体求职策略、AI Agent成果
- `wiki/self/README.md`

**源文件移至**
- `raw/personal/writings/给华为表哥的自我介绍.md`

## [2026-05-01] 摄取 | inbox 文章《团队中共享AI Skills的原则与方法》

从 `inbox/` 摄取鸭哥 Superlinear Academy 的续篇，移入 `raw/external/`，并新增一页知识页，保留其中关于共享池+个人INDEX+baseline+heartbeat+review四部件、skill是prompt不是code、以及Context Infra作为岗位的判断。

**新增页面**
- [团队中共享AI Skills的原则与方法](topics/research-knowledge-governance/superlinear-team-skill-sharing.md)

**更新页面**
- [Superlinear 社区 Agent Skill 知识治理信号](topics/research-knowledge-governance/Superlinear社区AgentSkill知识治理信号.md): 补入对鸭哥系统性回答的引用
- `wiki/index.md`

**源文件移至**
- `raw/external/superlinear-team-skill-sharing.md`

## [2026-05-01] 反思 | 公共知识库实践启发鸭哥写作

用户确认这篇文章是鸭哥受到本知识库的公共知识库实践启发后写的。本知识库的 `raw → wiki` 分层、联邦架构、知识治理思考为他提供了实际问题样本。

这表明用户的产品判断与实践已经足够成熟，可以启发同领域专家的系统性写作。

**新增页面**
- [公共知识库实践启发他人写作观察](self/公共知识库实践启发他人写作观察.md): 一条中置信度 self observation

**更新页面**
- [团队中共享AI Skills的原则与方法](topics/research-knowledge-governance/superlinear-team-skill-sharing.md): 补入背景说明
- `wiki/self/README.md`
- `wiki/index.md`

## [2026-04-30] 摄取 | inbox 文章《Taste不是品味，是感受quality的能力》

从 `inbox/` 摄取一篇 Superlinear 社区文章，移入 `raw/external/`，并新增一页知识页，保留其中关于 `taste`、`quality`、动态 / 静态良质，以及 AI 时代为什么更需要质量判断的一组解释。

**新增页面**
- [Taste：感受良质的能力](topics/learning-judgment-mental-models/Taste：感受良质的能力.md)

**更新页面**
- `wiki/index.md`

**源文件移至**
- `raw/external/Taste不是品味，是感受quality的能力.md`

## [2026-04-30] 摄取 | inbox 讲义《Proactive Intelligence》《Advanced Architecture》

从 `inbox/` 摄取两份 AI Architect 课程讲义，移入 `raw/external/`，并新增两页知识页，补上从产品定义与记忆系统继续推进到主动情报与生产级架构的后续模块。

**新增页面**
- [AI Architect 的 Proactive Intelligence 镜头](topics/ai-product-product-definition/ai-architect-proactive-intelligence.md)
- [AI Architect 的 Advanced Architecture 镜头](topics/ai-product-product-definition/ai-architect-advanced-architecture.md)

**更新页面**
- `wiki/knowledge/ai-architect-lens.md`
- `wiki/knowledge/ai-architect-context-intelligence.md`
- `wiki/knowledge/AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md`
- `wiki/index.md`

**源文件移至**
- `raw/external/ai-architect-proactive-intelligence.md`
- `raw/external/ai-architect-advanced-architecture.md`

## [2026-04-29] lint | 修复 wiki 链接与孤页

执行轻量 lint，重点检查非历史日志页的 Markdown 链接、孤页、重复标题、English-first 维护页、`raw/` 顶层误放文件、`.DS_Store` 和 gogo / oh-share-it 命名残留。

**修复内容**
- 将 `wiki/bridges/essays/给自己做了一个llm-wiki的入口应用.md` 收录进 `wiki/bridges/essays/README.md` 和 `wiki/index.md`
- 修复该页中的 `Pi agent` 链接和 `Github Release` 链接
- 将 `wiki/bridges/README.md` 中指向 essays README 的绝对路径改为相对路径
- 给 `wiki/bridges/essays/给自己做了一个llm-wiki的入口应用.md` 补上一级标题

**检查结果**
- 非 `wiki/log.md` 页面坏链：`0`
- 维护 wiki 孤页：`0`
- 重复一级标题：`0`
- English-first 维护页疑似项：`0`
- `raw/` 顶层误放文件：`0`
- `.DS_Store`：`0`

## [2026-04-29] lint | 拆分 gogo 与 oh-share-it 产品主语

按当前命名边界清理维护页：`gogo` 只保留为本地 `llm-wiki` 桌面应用，原先混在 `gogo` 名字下的公共知识库、联邦架构、agent-facing tool / MCP 方向统一改名为 `oh-share-it`。

**新增页面**
- `wiki/knowledge/gogo.md`
- `wiki/bridges/oh-share-it公共知识库产品.md`

**移除混淆页面**
- `wiki/knowledge/gogo-课题组公共知识库产品.md`
- `wiki/bridges/gogo作为agent能力层.md`

**更新内容**
- 修复 `wiki/index.md`、相关 self observation、Tolaria 页面与 Superlinear 知识治理页中的旧链接和旧主语
- 将公共知识库博客草稿中的产品名从 `gogo` 调整为 `oh-share-it`
- 保留 `wiki/log.md` 里的旧记录作为历史，不回改历史日志

## [2026-04-28] 摄取 | 更新 `Barytes/gogo` 并重写 gogo 仓库地图

按“禁止直接克隆仓库”的约束,通过 GitHub API 与 raw 文件抓取 `https://github.com/Barytes/gogo` 的公开信息,新增一份紧凑 snapshot,并据此更新现有 gogo 仓库地图与知识页。

**新增页面**
- `raw/external/github-repo-barytes-gogo.md`

**更新页面**
- `raw/personal/writings/gogo-repo-map.md`
- `wiki/knowledge/gogo-课题组公共知识库产品.md`
- `wiki/index.md`

**本轮关键信号**
- 公开仓库已统一为 `gogo`,主语更明确地收束为本地 `llm-wiki` 桌面工作台原型
- `example-knowledge-base/`、首次启动 onboarding、provider 配置与 installer 路径进入公开主线
- `security_service.py`、安全模式与 inline confirm 说明安全边界已被产品化
- `docs/public/` 与 `docs/archive/` 的分层说明文档体系已成熟
- README 明确进入 `maintenance mode`,公开边界更诚实

## [2026-04-28] lint | 清理遗留坏链

执行补充 lint,处理上一轮后仍残留的一组坏链。

**修复内容**
- 从 `wiki/index.md` 移除缺失页面 `bridges/essays/从零搭建Agent网页应用踩过的坑.md` 的入口
- 从 `wiki/bridges/essays/README.md` 移除同一失效条目
- 从 `wiki/knowledge/refactoringhq-tolaria-repo-map.md` 的相关页面中移除该坏链引用

**检查结果**
- `wiki/` 中非 `log.md` 页面坏链: `0`
- `wiki/` 中孤立页: `0`
- 无 `.DS_Store`

## [2026-04-28] lint | 清理失效链接与错放源文件

执行一轮轻量 lint,主要做了以下修复:

**重分类**
- 将 `raw/projects/gogo-repo-map.md` 移到 `raw/personal/writings/gogo-repo-map.md`
- 同步更新相关维护页中的源文件引用

**清理内容**
- 删除根目录、`raw/`、`raw/external/`、`wiki/`、`wiki/knowledge/` 下的 `.DS_Store`

**修复链接与索引**
- 修复多处指向 `AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First`、`AI产业分层地图`、`求职范式转变：让工作找到你` 的历史路径漂移
- 从 `wiki/index.md`、`wiki/bridges/` 与 `wiki/bridges/essays/README.md` 中移除或改写失效页面引用
- 给 `wiki/index.md` 补回对 `wiki/README.md` 的入口,消除孤立页

**保留说明**
- `wiki/log.md` 中的历史坏链按 schema 保留,未改写
- 未重建已缺失的旧页面,仅把现存维护页的引用收敛到仍然存在的页面

## [2026-04-28] 摄取 | inbox 文章《AI 产品的六个层次》

从 `inbox/` 摄取一篇 Superlinear Academy 文章,移入 `raw/external/`,并新增一页知识页,保留其中关于 `AI-assisted building vs AI runtime`、AI 产品六层与 L3-L6 能力分层的判断。

**新增页面**
- [AI 产品六层与 L3-L6 能力分层](topics/ai-product-product-definition/AI%20产品六层与%20L3-L6%20能力分层.md)

**更新页面**
- `wiki/index.md`

**源文件移至**
- `raw/external/superlinear-ai-product-six-levels.md`

## [2026-04-23] lint | 仓库清理

执行 lint pass,修复以下问题:

**清理内容**
- 删除空文件 `bridges/agent产品让用户看到什么,以及clawhouse还能补什么.md`(0字节,错误位置)

**修复孤立页面**
- `wiki/self/工作面摩擦敏感观察.md` → 添加到 index.md
- `wiki/self/用户自主性优先产品取舍观察.md` → 添加到 index.md
- `wiki/self/聚焦优先于通用观察.md` → 添加到 index.md
- `wiki/bridges/Pulse-有呼吸感的项目工作台.md` → 添加到 index.md

**检查结果**
- 无 `.DS_Store` 文件
- 无源文件直接置于 `raw/` 根目录(仅有 README.md 说明文件)
- wiki 下所有页面均已链接至 index 或各目录 README
- wiki 下页面均为中文为主(英文名页面内容亦为中文)

## [2026-04-23] 摄取 | 从 gogo-app 产品边界讨论提炼 self observation

从关于 `gogo-app` 产品边界的两轮对话中,提炼一条新的 self observation:聚焦优先于通用。

**新增页面**
- [聚焦优先于通用观察](self/聚焦优先于通用观察.md):面对"要不要支持更多场景"时,倾向守住明确边界并做到好用,而不是追求更广覆盖但每个场景都半吊子

**更新页面**
- `wiki/self/README.md`:更新观察列表索引

**来源**
- 两轮产品边界讨论:gogo-app 是否要支持 ACP / 更多 agent;gogo-app 是否要支持任意目录
- 关键共鸣句:"在自己选定的那类工作区里,真的很好用"

**判断收束**
- 支持更多 agent 不是 `gogo-app` 核心价值(后续可选增强)
- 支持任意目录会显著扩大 scope 且不一定增强核心价值
- `llm-wiki` 模式是让知识产生复利的工作流约束,不是包袱
- **结论:守住结构化 knowledge workspace 边界,先收口,先发布,先验证**

## [2026-04-23] 更新 | 从零搭建Agent网页应用踩过的坑

将本次对话中的产品边界抉择添加到 `bridges/essays/从零搭建Agent网页应用踩过的坑.md`,新增三个"产品边界坑"章节。

**新增章节**
- 坑八:看到新协议就想重构 -- 产品边界诱惑(ACP / agent 可替换抉择)
- 坑九:看到用户门槛就想泛化 -- llm-wiki 模式要不要保留(任意目录抉择)
- 坑十:聚焦 vs 通用 -- 产品边界焦虑的本质(聚焦优先于通用)

**更新内容**
- 坑总结分为两类:技术实现坑 + 产品边界坑
- 相关阅读添加对 `聚焦优先于通用观察` 的链接

**核心教训**
- 不是做完所有功能,不是适配所有场景,而是在自己认定的那个价值点上,做到真的好用

## [2026-04-22] 摄取 | inbox 三篇求职与 PMF 材料

从 `inbox/` 摄取三篇外部材料,移入 `raw/external/`。新增一页知识页,更新三页已有知识页,并同步更新 `wiki/index.md`。

**新增页面**
- [Go to Market Multiple Times:把高价值工作与早期产品反复推向市场](topics/ai-product-product-definition/go-to-market-multiple-times.md)

**更新页面**
- [求职范式转变:让工作找到你](knowledge/求职范式转变:让工作找到你.md)
- [Pre-PMF 验证手册](topics/ai-product-product-definition/pre-pmf-validation-playbook.md)
- [增长工程师的职业押注与面试叙事](topics/career-positioning-job-search/增长工程师的职业押注与面试叙事.md)
- `wiki/index.md`

**源文件移至**
- `raw/external/新时代的招聘现实和应对方法-熊力访谈-上.md`
- `raw/external/获取product market fit的三个步骤.md`
- `raw/external/高价值工作如何发挥最大效果-Go to market multiple times.md`


## [2026-04-22] 摄取 | Databricks 招聘访谈

从 `inbox/` 摄取一份 Databricks 招聘相关访谈转录,移入 `raw/external/`,并新增一页知识页,保留其中关于双向选择、风险适配与多信号 hiring 的结构判断。

**新增页面**
- [Databricks 的人才态度与双向选择](topics/career-positioning-job-search/Databricks%20的人才态度与双向选择.md)

**源文件移至**
- `raw/external/databricks-hiring-attitude-and-bidirectional-selection.md`


## [2026-04-22] 摄取 | inbox 五篇新材料

从 `inbox/` 摄取五篇新材料,统一移入 `raw/external/`,并新增五页知识页,同时给几页旧页面补回相关链接。

**新增页面**
- [AI 焦虑的三种形态与行动解法](topics/career-positioning-job-search/AI%20焦虑的三种形态与行动解法.md)
- [增长工程师的职业押注与面试叙事](topics/career-positioning-job-search/增长工程师的职业押注与面试叙事.md)
- [coding agent 的上下文压缩工作流](topics/agent-harness-runtime/coding%20agent%20的上下文压缩工作流.md)
- [衰退期的创业环境与技术判断](topics/ai-industry-investment/衰退期的创业环境与技术判断.md)
- [高级岗位简历的三条写法原则](topics/career-positioning-job-search/高级岗位简历的三条写法原则.md)

**源文件移至**
- `raw/external/superlinear-ai-anxiety-three-forms.md`
- `raw/external/openai-growth-engineer-career-bets.md`
- `raw/external/ai-engineer-harness-engineering-complex-problems.md`
- `raw/external/downturn-generative-ai-prediction.md`
- `raw/external/resume-three-principles.md`

**补回链接的旧页面**
- `wiki/knowledge/harness-engineering.md`
- `wiki/knowledge/求职范式转变:让工作找到你.md`
- `wiki/knowledge/AI 让我们重新开始享受自己的职业.md`
- `wiki/knowledge/AI 时代大厂打工人的五条路.md`

## [2026-04-22] Lint | 轻量清理与补链

完成一轮轻量 lint。

**操作**
- 删除 `.DS_Store`:根目录、`raw/`
- 给以下页面补回相关链接:
  - `wiki/knowledge/thin-harness-fat-skills.md`
  - `wiki/knowledge/AI 时代的结果确定性:Agentic Runtime 与 Evaluation-First.md`
  - `wiki/knowledge/真本事-从会工作到会赚钱.md`
- 复查本轮新增页面与索引链接,未发现新的坏链

## [2026-04-22] Lint | 修复历史坏链

继续做了一轮历史链接修复,清掉 `wiki/` 中除 `log.md` 历史记录外的坏链。

**修复页面**
- `wiki/self/职业决策与求职策略观察.md`
- `wiki/bridges/clawhouse-多设备-agent-工作台.md`
- `wiki/bridges/information-compounding-systems-design.md`
- `wiki/bridges/mechanism-design-research-compounding-system.md`
- `wiki/bridges/公共知识库、Reflexio与EvoMap的对比分析.md`
- `wiki/bridges/课题组公共知识库的联邦架构设计.md`
- `wiki/bridges/essays/课题组公共知识库-博客草稿.md`
- `wiki/knowledge/EvoMap-Agent 互联网与集体潜意识.md`

**结果**
- `wiki/` 中非 `log.md` 页面坏链复查结果:`0`

## [2026-04-22] 更新 | 补强"增长工程师的职业押注与面试叙事"具体例子

根据后续复读原始访谈,把这页从偏抽象总结改成带具体经历的版本,补入:

- `AVOS` 与 YouTube 创始团队的早期创业经历
- `Uber China growth` 中的 incentive、anti-fraud、微信分发与中美组织差异
- `CloudKitchens / City Storage Systems` 的城市基础设施 vision
- 两次面 `OpenAI` 的具体复盘:第一次没过、第二次主要靠把近期项目故事讲清楚而通过

已更新页面:
- `wiki/knowledge/增长工程师的职业押注与面试叙事.md`

## [2026-04-22] 更新 | 为三篇新知识页补反向链接

对刚摄取的三页新知识页做一轮轻量 update,把它们反向挂到更相关的旧页面中,方便后续从旧主题页导航过去。

**更新页面**
- `wiki/knowledge/AI 让我们重新开始享受自己的职业.md`
- `wiki/knowledge/AI 时代大厂打工人的五条路.md`
- `wiki/knowledge/thin-harness-fat-skills.md`
- `wiki/knowledge/harness-engineering.md`
- `wiki/knowledge/求职范式转变:让工作找到你.md`
- `wiki/knowledge/真本事-从会工作到会赚钱.md`
- `wiki/knowledge/ai-architect-lens.md`

## [2026-04-22] 摄取 | Superlinear Academy 三篇新材料

从 `inbox/` 摄取三篇 Superlinear Academy 相关文章,统一移入 `raw/external/`,并新增三页知识页。

**新增页面**
- [GenAI 的共识边界与任务委托框架](topics/ai-product-product-definition/GenAI%20的共识边界与任务委托框架.md)
- [AI 时代的结果确定性:Agentic Runtime 与 Evaluation-First](knowledge/AI%20时代的结果确定性:Agentic%20Runtime%20与%20Evaluation-First.md)
- [喜欢与擅长的命运飞轮](topics/learning-judgment-mental-models/喜欢与擅长的命运飞轮.md)

**源文件移至**
- `raw/external/ai-builders-module-6-become-future-proof.md`
- `raw/external/superlinear-从过程确定性到结果确定性.md`
- `raw/external/superlinear-喜欢与擅长的命运飞轮.md`


## [2026-04-18] 反思 | 从 gogo-app 提炼新的 self observations

基于这轮把 `gogo-app` 当作项目材料的摄取,新增两条较保守的 observation,用来承接之前关于"自我表达如何走向 specific knowledge"的问题。

**新增观察**
- [用户自主性优先产品取舍观察](self/用户自主性优先产品取舍观察.md)
- [工作面摩擦敏感观察](self/工作面摩擦敏感观察.md)

**它们提供的增量证据**
- 不再只是抽象地说"给用户自由",而是落到 knowledge-base 可切换、skill/schema 可编辑、app 与 server/client 解耦、Pi 机制显式暴露等具体取舍
- 不再只是抽象地说"喜欢做架构判断",而是落到对 `Obsidian + coding agent` 分裂工作面的不满,以及把浏览 + 对话收束成统一工作台的具体设计

## [2026-04-18] 更新 | gogo-app 仓库地图与产品边界

把 `https://github.com/Barytes/gogo-app` 当作你的项目材料重新摄取,并更新现有 `raw/projects/gogo-repo-map.md`。

**这次更新的关键点**
- 不再把当前仓库混同为整个"大 gogo"系统,而是明确它当前收敛成 `gogo-app`:一个本地 knowledge-base 工作台应用
- 补入当前对外发布边界:正式目标是 Windows / macOS 桌面版,Web 版主要用于开发与验证
- 补入当前关键机制:`Wiki / Chat` 双主模式、knowledge-base 切换、skills / schemas 暴露与编辑、Pi 能力显式带到 GUI、Tauri 桌面壳
- 把你后续补充的 5 条设计取舍也纳入 repo map,作为项目材料中的第一手产品判断证据

**已更新页面**
- `raw/projects/gogo-repo-map.md`
- [gogo:课题组公共知识库产品](knowledge/gogo-课题组公共知识库产品.md)

## [2026-04-17] 反思 | 技术定义 vs 业务口径的区分

澄清一个重要区分:字段的技术定义是确定的,但业务口径是多样的。

**核心判断**
- 技术定义:`user_id = INT PRIMARY KEY`(schema 层面,确定)
- 业务口径:"统计用户数"时用 JOIN 哪张表(使用层面,多样)
- Joey Wu 场景的冲突发生在业务口径层面,不是技术定义层面
- 认知知识定锚的是业务口径,不是技术定义

已更新页面:
- [Superlinear 社区 Agent Skill 知识治理信号](topics/research-knowledge-governance/Superlinear社区AgentSkill知识治理信号.md)

## [2026-04-17] 反思 | 操作知识需要认知知识的定锚

## [2026-04-17] 反思 | 三层图:private / shared / routed context

把前面讨论的三层知识结构记录下来,作为对 gap 的更具体描述。

**三层定义**
- private context:不强制共享的个人知识,高噪声、场景依赖、可能冲突
- shared context:团队公认的默认知识,低噪声、可复用、可聚合
- routed context:决策层,决定"这个场景用谁的知识、如何处理冲突"

**关键判断**
- Reflexio 有 private + shared,但缺 routed
- gogo 目前也缺 routed
- routed context 正是这个 gap 的核心补齐点

**对 gogo 的启发**
- private:个人 wiki(本地)
- shared:public-pool(服务器)
- routed:需要设计--路由策略、冲突处理、场景判定

已更新页面:
- [Superlinear 社区 Agent Skill 知识治理信号](topics/research-knowledge-governance/Superlinear社区AgentSkill知识治理信号.md)

## [2026-04-17] 反思 | Superlinear 求助帖里的知识治理信号

从 Joey Wu 在 Superlinear 社区发出的求助帖和你的回复里,提炼出一个更一般的市场信号:多人协作中的 Agent Skill 知识库,核心不是"存更多内容",而是基础共识、个人定制、冲突治理与按人/按场景路由。

**初步判断**
- 这更像 shared base + personal overlay 的知识治理问题,不是传统 FAQ 或文档系统问题。
- 和 Reflexio 的差异在于:这里不一定要把知识压成单一执行答案,而是要保留局部差异,并在需要时选择性使用。
- 对 gogo 的启发是:公共知识库可以继续往"团队知识基础设施"推进,而不只是一个可检索仓库。

**补充判断**
- Reflexio 没有直接丢掉 user specific knowledge,而是把它保留在 per-user 层,再把可泛化部分提炼到共享层。
- 如果有东西能 address 这个 gap,它更像是 context 层的知识治理基础设施,而不是单纯更强的模型。

**待验证**
- 是否有更多团队在用 YAML / Notion / docs / playbooks 管理 Agent knowledge 时,遇到类似的扩张后失真问题。
- 是否存在明确的 ICP:人数增长后,知识冲突开始影响 agent 输出质量的团队。

新增页面:
- [Superlinear 社区 Agent Skill 知识治理信号](topics/research-knowledge-governance/Superlinear社区AgentSkill知识治理信号.md)

## [2026-04-16] 摄取 | Slock 人机协作平台

从 inbox 摄取 Slock.ai 产品介绍。

**产品定位**
- humans 和 AI agents 在 channels/DMs 中协作--agents 作为队友而非工具
- 核心主张:"The future of work isn't humans using AI tools. It's humans and AI agents collaborating."

**核心特性**
- Agents That Remember:持久记忆,跨 session 持续存在
- One Conversation:channels/DMs 中 humans 和 agents 平等
- Your Machines, Your Agents:daemon 在用户自己的机器上执行
- Always on:idle 时 hibernate,需要时 wake with full context

**与现有产品对比**
- 与 multica 相似(team managed agents、daemon 接入),但 Slock 以 channel/DM 为中心而非 issue/task
- 与 OpenClaw 相似(persistent memory、always-on),但 Slock 是 team 平台而非 single-user assistant
- 与 clawhouse 有关联(daemon 执行、context restore),但 Slock 是实时协作而非异步同步

新增页面:
- [Slock:人机协作平台](topics/agent-harness-runtime/Slock-人机协作平台.md)

源文件移至:
- `raw/external/slock-ai-product-intro.md`

## [2026-04-16] 更新 | Bakery 产品描述

基于新的官方描述,更新 Bakery 知识页面。

**核心定位更新**
- Bakery 把 iPhone 变成 Mac 上 Claude Code 的远程控制器
- 与 clawhouse 核心目标高度重叠:离开桌面后如何继续使用 agent

**已 address 的 clawhouse 痛点**
- ✅ 移动端接回原 agent 工作
- ✅ 实时代码可见性
- ✅ iOS 模拟器画面实时串流

**clawhouse 可能的独特价值收束**
- 通用性(不限 iOS、不限 Claude Code)
- 异步性(不依赖实时在线)
- 双向性(任意设备互连)

## [2026-04-16] 摄取 | Bakery iOS 远程开发 APP

从 inbox 摄取 Superlinear Academy 社区分享的项目介绍。

**产品定位**
- iOS 应用,让开发者在 iPhone 上实时连接、编写、测试 iOS 应用
- 核心洞察:iOS App 是空间性的--手势、转场、触觉反馈、滚动物理效果无法从代码 diff 中获取
- 完整开发循环:在手机上写代码、编译、预览、测试

**技术机制**
- iOS 模拟器画面串流到 iPhone
- 手机变成控制器,减少与 Mac 端开发体验的差异
- 结合 Asc CLI 自动发布到 AppStore

**与知识库其他主题的关联**
- 与 Clawhouse 方向相关:多设备场景下的 agent 访问与连续性
- 体现了实时反馈循环在开发工具中的价值

新增页面:
- [Bakery:iOS 端远程开发 APP](topics/agent-harness-runtime/Bakery-iOS端远程开发APP.md)

源文件移至:
- `raw/external/bakery-ios-远程开发APP.md`

## [2026-04-16] Lint | 仓库清理

运行 lint 检查。

**检查结果**
- 所有 wiki/knowledge/、wiki/self/、wiki/bridges/ 页面均为中文标题,无需语言规范化
- 无孤儿页面(所有页面均可从索引链路到达)
- 无重复页面
- essays 目录下 gogo-app-产品介绍与核心卖点.md 通过 essays/README.md 链接,可从 wiki/index.md → bridges/README.md → essays/README.md 到达

**清理操作**
- 删除 .DS_Store 文件(3个:根目录、inbox/、wiki/)

**新增页面**
- [Go to Market 策略](self/go-to-market-strategy.md):找到高价值工作的策略、历程与迭代记录
- wiki/self/README.md 已更新,添加了新页面链接

## [2026-04-15] 摄取 | 职业决策与求职策略观察

从与Fang Zhang老师的回访回复中提取self observation。

**核心判断**
1. 不读博的决策依据:评价体系单一、身心健康考量、面对心魔、自由探索的幻想破除
2. 求职策略转变:从投简历转向推销自己、给人解决问题
3. 项目实践的自信来源:能驾驭复杂开发、与AI协作、价值洞察与技术取舍

**待解决的卡点**
- 不清楚怎么了解市场:知道重要但不清晰具体怎么做

**与既有框架呼应**
与Naval财富框架高度呼应:找工作是Agent路径、真正好机会不在招聘网站、做东西让市场看到你。

新增页面:
- [职业决策与求职策略观察](self/职业决策与求职策略观察.md)

源文件位置:
- `raw/personal/conversations/2026-04-15-fang-zhang-followup.md`

## [2026-04-15] 摄取 | Go to Yourself 框架

从 inbox 摄取两篇个人随笔,将物理模型映射到人生策略问题。

**随笔内容**
1. **质量通量模型**:$\Phi = B \cdot S \cdot \cos \theta$ 映射到"质量-数量-一致性"
2. **余弦相似度模型**:$ec{V}_{Self}$ 与 $ec{V}_{Market}$ 的向量分析

**核心框架**
- Go to Yourself vs Go to Market 的策略对比
- 三种结果:Go to Market(平庸)、浅层 Go to Yourself(自嗨)、深层 Go to Yourself(最优解)
- 卡尔·罗杰斯洞察:"最个人的就是最普遍的"
- 引力扭曲动态模型:理解市场 + 极致制造自我 → 让市场偏转

**与现有知识对照**
- 真本事:"了解市场 + 打造产品 + 利用杠杆" → Go to Yourself 强调先校准自我
- Pre-PMF:"从 ICP 出发" → Go to Yourself 强调先有极致产品
- Naval:Prepared luck + 判断力 → 呼应"深耕识别机会"

**提取的 self observation**
- 倾向用物理/数学模型抽象人生问题(磁通量、向量分析、余弦相似度)

新增页面:
- [Go to Yourself 框架](topics/learning-judgment-mental-models/go-to-yourself-框架.md)
- [物理模型抽象人生问题观察](self/物理模型抽象人生问题观察.md)

源文件移至:
- `raw/personal/writings/Go to Yourself:提升你的"质量通量" 2c74a089a3c18080afc9fbb6eb5f8454.md`
- `raw/personal/writings/Go to Yourself和Go to Market的余弦相似度模型 2d74a089a3c180f2bdf5d3a5ce4a4138.md`

## [2026-04-15] 反思 | 知识库公开分享的阻力降低观察

建议格式:

- `## [YYYY-MM-DD] 摄取 | 标题`
- `## [YYYY-MM-DD] 反思 | 标题`
- `## [YYYY-MM-DD] 查询 | 标题`
- `## [YYYY-MM-DD] 整理 | 标题`
- `## [YYYY-MM-DD] 更新 | 标题`

**核心洞察**:如果知识库本身就是公开的,分享阻力就消失了。
- 无需额外写博客 → 直接用知识库内容
- 无需维护网站 → gogo 本身就是网站
- 无需额外动作公开 → 一个简单步骤同步

**产品判断**:gogo 可以扩展为"个人公开知识库 host",降低分享阻力,boost 用户分享动力。

**验证方式**:你自己先用 gogo host 公开知识库,观察是否确实 boost 了你的分享动力。

新增页面:
- [知识库公开分享的阻力降低观察](self/知识库公开分享的阻力降低观察.md)

## [2026-04-15] 反思 | 自由与当下的观察

摄取两篇个人随笔,提炼核心洞察到 self。

**随笔内容**
1. **自由即当下**:重构圣多纳释放法六步骤为新三步骤,核心等式:自由=当下,念头=想要=记忆
2. **自由的两个侧面**:构建二维坐标系(Ease vs Alignment),四个象限分析,飞跃到三维观察者视角

**与 Self 3 的呼应**
- Gallwey:意识觉察自身 → 随笔:三维观察者视角
- Gallwey:真诚渴望放下结果 → 随笔:允许一切,不把解决问题当自由的先决条件
- Gallwey:灯塔一直在 → 随笔:当下一直在
- Gallwey:Self 1 = 念头/评判 → 随笔:念头 = 想要 = 记忆
- Gallwey:Self 3 = 真实不变的内在自我 → 随笔:当下 = 自由 = 真实

**核心判断**
- 自由不发生在二维平面,飞跃时刻才是自由
- 不必须解决问题才能自由--允许问题存在,同时保持临在
- 当下的 Ease 本身就是对终点的 Alignment--坐标系最终收束为一条轴
- 诚实看见自己在哪,然后允许--从允许开始就已经赢了

新增页面:
- [自由与当下的观察](self/自由与当下的观察.md)

源文件位置:
- `raw/personal/writings/自由即当下-一个更容易实践的释放步骤.md`
- `raw/personal/writings/自由的两个侧面.md`

## [2026-04-15] 摄取 | 网球的内心游戏

从 inbox 摄取《The Inner Game of Tennis》(W. Timothy Gallwey, 1974)。

**核心框架**
- Self 1(告诉者)vs Self 2(执行者):两者的关系决定能否把知识转化为行动
- 核心问题:"不是我不知道该怎么做,是我做不到我知道的事"
- 心流状态:"playing out of his mind"--Self 1 安静,Self 2 自由行动
- 放下评判:评判触发思考过程 → 身体紧张 → 表现下降
- Self 3:内在自我--潜能的终极来源

**关键洞察**
- 图像比语言好,示范比讲解好,过多指令比没有更糟
- 让 Self 1 被占用(观察球的缝线),Self 2 就能自然执行
- "trying too hard":努力过度导致紧张和肌肉冲突
- 心流破坏法:问对手"你今天怎么做得这么好?"--95% 心流立刻结束
- 内心游戏的目标不是赢得外部比赛,而是发现内在自我

新增页面:
- [网球的内心游戏](topics/learning-judgment-mental-models/网球的内心游戏.md)

源文件位置:
- `raw/external/the-inner-game-of-tennis.pdf`
- `raw/external/the-inner-game-of-tennis.txt`

## [2026-04-15] 摄取 | Thin Harness, Fat Skills

从 inbox 摄取 Garry Tan 的原文和 Superlinear Academy 的中文解读。

**核心内容**
- 五个概念:Skill Files(参数化 markdown 程序)、Thin Harness(只做四件事的薄壳)、Resolvers(上下文路由表)、Latent vs Deterministic(智能与信任的分界线)、Diarization(多源交叉的结构化画像)
- 三层架构:Fat Skills → Thin Harness → Application Layer
- 实战案例:Startup School 6000 founder 的 enrichment、matching、学习循环
- 与 grapeot/context-infrastructure 的对应:skills 目录、三级缓存、axiom 路由

**判断**
- 10x-100x 差距来自架构,不是模型参数
- Skill file = 方法调用,接受参数,同一流程不同能力
- Harness 薪水:200 行指针文档 vs 20,000 行知识
- Diarization 做不到:SQL 做不到,RAG 做不到,模型必须读完整档案

新增页面:
- [Thin Harness, Fat Skills](topics/agent-harness-runtime/thin-harness-fat-skills.md)

源文件位置:
- `raw/external/garry-tan-thin-harness-fat-skills.md`(原文)
- `raw/external/superlinear-thin-harness-fat-skills-解读.md`(解读)

## [2026-04-14] 准备 | 向 Reflexio 开发者提问的问题草稿

准备向 Reflexio 团队请教聚合机制的设计取舍。

**我的背景**:正在做课题组公共知识库产品--每个组员有个人知识库,需要聚合成公共知识库。与 Reflexio 有相似(跨主体知识聚合)也有不同(认知知识 vs 操作知识、人类研究者 vs Agent)。

**核心问题**:
1. 两步聚合的设计理由--为什么 Embedding 聚类 + LLM 聚合?有没有考虑过其他方案?
2. trigger 字段做 Embedding 的考量
3. Cluster fingerprint 增量聚合的实践经验
4. Majority-wins 冲突处理的设计直觉--有没有考虑保留冲突的场景?
5. 用户权重的影响(expert vs novice)
6. 核心设计直觉和踩过的坑

新增页面:
- [向 Reflexio 开发者提问(润色版)](self/向Reflexio开发者提问-润色版.md)

## [2026-04-14] 设计 | gogo-app 个人主页发布功能

基于"知识库公开分享的阻力降低观察",设计了在 gogo-app 中增加"发布知识库作为个人主页"的功能。

**方案**:静态生成 + GitHub Pages
- 公开层配置:`publish-config.yaml` 定义哪些目录公开
- 静态渲染:Markdown → HTML
- 部署:git push 到 GitHub Pages
- 个人主页:简洁风格,按目录组织(knowledge/bridges/log)

**新增模块**
- `publish_service.py`:读取配置、筛选公开层
- `static_renderer.py`:渲染静态 HTML
- `deployer.py`:部署到 GitHub Pages
- `publish.js`:发布按钮 UI

**实现路线图**
- Phase 1:基础发布能力
- Phase 2:GitHub Pages 部署
- Phase 3:个人主页模板优化
- Phase 4:高级功能(选择性公开 UI、定时发布)

新增页面:
- [gogo-app 个人主页发布功能设计](bridges/gogo-app个人主页发布功能设计.md)

## [2026-04-14] 创作 | 课题组公共知识库博客草稿

基于gogo产品设计,起草了一篇可用于公开发表的博客文章。

**核心内容**
- 四个核心问题:找方向难、孤岛状态、无复利、无公共工作面
- 核心洞察:"默认工作面产生复利"
- 联邦架构设计:推理是个人消费,同步是公共产品
- 知识复利机制:前人页面继续写、冲突即知识、检索优先级
- 与现有方案的对比

**可发表状态**:文章结构完整、逻辑清晰、语言通俗,可直接用于即刻/博客/公众号发表。

**位置**:已移至 `bridges/essays/课题组公共知识库-博客草稿.md`

新增页面:
- [课题组公共知识库:让知识产生复利](topics/research-knowledge-governance/essays/课题组公共知识库-博客草稿.md)

## [2026-04-14] 摄取 | gogo 项目(自己 build 的知识库产品)

从 GitHub clone 了用户自己的项目 https://github.com/Barytes/gogo,这是一个 agentic knowledge base 产品。

**核心洞察(最有价值,可以直接分享)**
- 识别四个核心问题:找方向难、孤岛状态、无复利、无公共工作面
- 联邦架构判断:推理是个人消费,同步是公共产品
- 知识复利机制:前人页面继续写、冲突即知识、检索优先级

**与 Hermes agent 方向一致**
- Hermes agent = "把 llm wiki 内置在 agent 里面"
- gogo 的产品定义 = "让问答中形成的洞察沉淀回知识库"
- 再次验证了用户对"知识库 + agent 包装"方向的直觉判断

**可以公开分享的内容**
- 层次一(现在就可以):product-definition-belief.md、联邦架构设计、项目分层设计
- 层次二(选择性分享):agent 架构判断、build 过程中的问题解决
- 层次三(做完再分享):产品功能演示

新增页面:
- [gogo:课题组公共知识库产品](knowledge/gogo-课题组公共知识库产品.md)

源文件位置:
- `raw/projects/gogo/`

## [2026-04-14] 摄取 | 真本事:从会工作到会赚钱

从 inbox 摄取两篇长文,来自《真本事:从会工作到会赚钱》一书。作者背景:康奈尔经济学博士、亚马逊/Meta/腾讯数据科学高管,现为 Statsig 布道师(该公司被 OpenAI 以11亿美元收购)。

**核心框架**
- 批判优绩主义:"好学生→好工作→赚大钱"是死胡同,公司与个人目标天然冲突
- 主体思维 vs 客体思维:对自己负责 vs 等外界满足自己
- 个人价值公式:个人价值 = 了解市场 + 打造产品 + 利用杠杆
- 道、天、地、将、法:职业选择的五个层次框架
- 杠杆在职场中的应用:风险与收益不完全对称、高杠杆情境
- 人力资本 vs 金融资本:年轻人最大资产是自己

**与 Naval 的呼应**
- Principal-Agent Problem:公司与个人目标冲突
- 个人价值由市场需求决定:与 Naval 同义
- 杠杆放大回报:Naval 分类更细化
- 保护本金、避免重大亏损:与 Naval 同义

新增页面:
- [真本事:从会工作到会赚钱](topics/career-positioning-job-search/真本事-从会工作到会赚钱.md)

源文件移至:
- `raw/external/真本事-从会工作到会赚钱-上篇.md`
- `raw/external/真本事-从会工作到会赚钱-下篇.md`

## [2026-04-14] 桥接 | Naval 财富框架应用于求职困境

围绕"临近毕业想找AI agent工作但不确定路径"的困境,从Naval宝典中提炼应用框架:

**核心判断**
- 找工作本质是"renting out your time" → Agent路径 → 低杠杆
- 真正好的机会不会在招聘网站上 → "The best jobs are neither decreed nor degreed"
- 陷阱:总有人给你一份"刚好够好"的工作 → 让你无法真正发展

**替代路径**
- Be a maker who makes something interesting → 做东西 + 公开展示 = 让机会来找你
- Hourly Rate的本质:跳过"别人希望你做的事",只剩下"自己真正想做的事"
- 你已有的知识库积累 = specific knowledge的雏形 = 需要变成可被看到的形式

**关键洞察**
- Principal-Agent Problem应用于求职:招聘网站的岗位让你变成Agent
- 你的直觉判断(觉得boss直聘不对胃口)本身就是判断力 → 需要相信并用它指导行动

新增页面:
- [Naval财富框架应用于求职困境](topics/career-positioning-job-search/Naval财富框架应用于求职困境.md)

## [2026-04-14] 摄取 | Naval 的 Mental Models

从《纳瓦尔宝典》"Building Judgment" 章节深度摄取 Naval 的 mental models 体系。

**核心概念**
- 大脑是 "memory prediction machine"
- Mental models 是比"过去发生→未来发生"更高级的预测方式
- Mental models = "压缩指针",需要底层经验支撑,否则只是语录

**十个 Mental Models 清单**
1. Evolution - 解释社会现象(性别选择、竞争)
2. Inversion - 通过排除错误来找正确
3. Complexity Theory - 知识和预测的根本局限
4. Microeconomics - 供需、博弈论
5. Principal-Agent Problem - Naval 认为"最重要的问题"
6. Compound Interest - 智力领域的复利
7. Basic Math - 算术、概率、统计
8. Black Swans - 尾部事件
9. Calculus - 理解变化率原理
10. Falsifiability - 可证伪性是科学的标准

**两个决策 Heuristic**
- "If you can't decide, the answer is no"
- "Run uphill" - 选择短期痛苦的那条路

**Naval 的使用方式**
- Tweets 作为 maxims/指针
- 决策时调用原则而非依赖具体事件
- 通过阅读经典建立高质量基础

新增页面:
- [Naval 的 Mental Models](topics/learning-judgment-mental-models/naval-mental-models.md)

更新页面:
- [纳瓦尔宝典](topics/learning-judgment-mental-models/纳瓦尔宝典.md) - 待深入学习中标记 mental models 已完成

## [2026-04-14] 摄取 | 纳瓦尔宝典深度摄取

从 PDF 提取文本并深度摄取《纳瓦尔宝典》。核心内容包括:

**Part I: Wealth**
- Wealth vs Money vs Status 的本质区分
- Productize Yourself 框架:Specific Knowledge + Accountability + Leverage
- 三种杠杆类型:Labor(最难)> Capital(需许可)> Code & Media(无需许可)
- 四种运气:Blind luck > Hustle luck > Prepared luck > Unique character luck
- 复利不只适用于资本,也适用于知识和关系
- 财富游戏是正和游戏,地位游戏是零和游戏

**Part II: Happiness**
- Happiness is peace at rest/motion
- 幸福是技能而非天赋,前提是相信它可以习得
- Desire is a contract to be unhappy until you get what you want
- 人生是单人游戏,嫉妒无意义
- 接受现实:改变/接受/离开,三选一
- 健康优先级高于幸福、家人、工作

**核心张力**
- 努力(苦干)vs 判断力(方向)
- 和平 vs 目的
- 欲望的两面性:外部欲望破坏幸福,内部欲望可以保留

更新页面:
- [纳瓦尔宝典](topics/learning-judgment-mental-models/纳瓦尔宝典.md)(从薄摘要扩展为 5500+ 字深度摄取)

## [2026-04-13] 摄取 | Agent 复利工作模式讲义

将一份关于"复利"的讲义材料 ingest 到知识库。核心内容:

1. **复利原理** - 1.03^200 = 1.02^200 × 7,3% 周增长率累积 4 年比 2% 相差 7 倍
2. **电机 vs 蒸汽机类比** - 把电机当蒸汽机用只拿 30% 提升,重新设计工作方式可获几十倍提升
3. **Agent 复利三维度** - 本地文件(持久记忆)+ 规则文件(质量标准)+ 迭代(越来越快)
4. **两个实战案例** - 腾讯游戏培训项目、PPT 四次迭代

核心洞察:这不是「用 AI」,是在「训练 AI」。Agent 的价值不是第一次做得多好,是每一次都在变好。

新增页面:
- [Agent 复利工作模式](topics/agent-harness-runtime/agent%20复利工作模式.md)

## [2026-04-13] 更新 | 课题组公共知识库联邦架构设计

讨论并记录了联邦式架构设计:每人本地跑完整 LLM Wiki + Agent,服务器只做 Git 同步仓。相比中心化架构,token 成本分散给个人,导师无需承担推理开销,同时保留"打破孤岛"和"知识复利"的核心价值。

新增页面:
- [课题组公共知识库的联邦架构设计](topics/research-knowledge-governance/课题组公共知识库的联邦架构设计.md)

## [2026-04-13] 更新 | 联邦架构简化设计

进一步简化联邦架构设计,核心变化:

1. **public-pool 只存 wiki,不存 raw** - 原始材料永远留在个人本地
2. **默认贡献** - wiki 页面默认公开,无需手动标记
3. **Agent 语义聚合** - git merge 无法处理语义关联和认知冲突,改用 Agent 自动聚合
4. **无需人工 review** - 降低摩擦,保守自动聚合:
   - 相似主题 → 都保留,互加链接
   - 冲突判断 → 创建 tension 页面
   - 互补内容 → 自动添加 cross-link

关键判断:EvoMap 解决 how 问题(可执行 Capsule),联邦知识库解决 what/why 问题(理解框架),知识类型不同决定了聚合策略不同。

## [2026-04-13] 摄取 | EvoMap 与 Agent 互联网

从 inbox 摄取两篇关于 EvoMap 的材料:
- 张昊阳 24 天从零搭建 EvoMap 平台的完整历程
- GEP-A2A 协议如何实现 Agent 之间的经验传承

新增页面:
- [EvoMap:Agent 互联网与集体潜意识](topics/agent-harness-runtime/EvoMap-Agent%20互联网与集体潜意识.md)

## [2026-04-12] 整理 | Lint 与 inbox 摄取

执行 lint 检查,清理 `raw/` 下的 `.DS_Store`,并将 inbox 中的职业发展文章移到 `raw/external/`,创建维护页 `AI 时代大厂打工人的五条路.md`,更新索引。

## [2026-04-06] 整理 | 初始化 schema 与本地 skills

建立了专用的摄取、查询与整理 schema,加入了三套本地工作流 skill,并把仓库整理到适合结构化维护的状态。

## [2026-04-06] 整理 | 重分类外部资料并清理仓库杂物

把误放在 `raw/` 根下的外部材料移到 `raw/external/`,清除了 `.DS_Store` 杂物,并检查了当前 wiki 根页面的基本链接覆盖。

## [2026-04-06] 更新 | 增加 kb-ops 编排 skill

增加了仓库本地的编排 skill,让短指令可以直接触发摄取、更新、整理或完整维护流程,而不必每次重写完整提示。

## [2026-04-06] 更新 | 将裸调用 kb-ops 设为完整流程

把 `kb-ops` 与 `$kb-ops` 定义成这个仓库的默认完整维护入口。

## [2026-04-06] 摄取 | Harness Engineering 概览

把新的 Harness Engineering 来源从 `inbox/to-ingest/` 移到 `raw/external/`,并创建了总结其控制层与补偿面框架的维护页。

## [2026-04-06] 查询 | 本地知识库运行模型

从一场比较 `llm-wiki` 与 `context infrastructure` 的讨论中提炼出可复用结论,并分别写回中性的比较页与面向本仓库的桥接页。

## [2026-04-06] 整理 | 重分类收件箱条目并刷新索引

把一份混合比较笔记移到 `raw/personal/conversations/`,更新了 `wiki/index.md`,并为新维护页补回入链。

## [2026-04-06] 查询 | 代码库作为知识来源

回答了代码仓库该如何进入知识库的问题:把代码库当作证据源处理,并写回一页关于如何提炼工程实践而不把实现噪音直接抄进 wiki 的桥接页。

## [2026-04-06] 更新 | 增加仓库研究 skills

新增 `repo-map-ingest` 用于首次仓库建图,新增 `repo-practice-query` 用于聚焦式后续提炼,并把推荐的双-skill 流程补进"代码库作为知识来源"页面。

## [2026-04-06] 更新 | 完成 GitHub 仓库地图摄取流程

为 `repo-map-ingest` 增加了 GitHub snapshot 脚本、repo map 输出模板,并明确要求先把紧凑证据保存到 `raw/external/`,再把维护过的仓库地图写入 `wiki/knowledge/`。

## [2026-04-06] 更新 | 支持从 snapshot 自动生成仓库地图

增加了从 snapshot 生成笔记的脚本和一站式 GitHub 摄取封装,因此 `repo-map-ingest` 现在可以自动产出原始 repo snapshot 与初始维护稿。

## [2026-04-06] 更新 | 自动刷新 repo 摄取后的索引与日志

扩展了一站式 GitHub repo 摄取封装,使其在生成原始 snapshot 与维护后的 repo map 之后,也能更新 `wiki/index.md` 并向 `wiki/log.md` 追加摄取记录。

## [2026-04-06] 更新 | 更智能的仓库地图相关页面匹配

升级了 repo map 生成逻辑,让相关页面可以从 `wiki/index.md` 与现有页面标题中推断,再按 topic 与机制重合度筛选,而不再依赖单一硬编码关键词。

## [2026-04-06] 更新 | 增加根级 AGENTS 与本地查询模式

新增了根级 `AGENTS.md`,将仓库问题的默认查询模式收紧为本地优先且本地限定,并增加 `kb-query` skill 来回答不自动联网的仓库问题。

## [2026-04-06] 更新 | 强制 kb-query 先列出已查页面

调整了本地限定查询规则,要求仓库回答在正文前先列出实际查阅过的本地页面。

## [2026-04-06] 摄取 | ASI-Evolve 研究 Harness

把新的 ASI-Evolve 来源从 `inbox/to-ingest/` 移到 `raw/external/`,创建了关于 AI 自演化研究 harness 的维护页,并从既有 Harness Engineering 页面与索引建立了链接。

## [2026-04-06] 摄取 | grapeot/context-infrastructure 仓库地图

把 GitHub 上的紧凑仓库 snapshot 抓取到 `raw/external/github-repo-grapeot-context-infrastructure.md`,并围绕主题"仓库架构与工程实践"生成了初始维护页 `wiki/knowledge/grapeot-context-infrastructure-repo-map.md`。

## [2026-04-06] 摄取 | Pre-PMF 验证手册

把 Pre-PMF 手册及其分章节源文件从 `inbox/to-ingest/` 移到 `raw/external/`,随后创建了围绕 ICP 优先验证、关键路径设计、信号质量、校准与 Go / No-Go 判断的维护页。

## [2026-04-06] 摄取 | 科学与技艺双层认知模型

把关于 Science/Craft 双层认知模型的外部笔记移到 `raw/external/`,并创建了区分方向层理论与执行层实践的维护页。

## [2026-04-06] 反思 | 职业转型观察

把一份 coaching 往来 PDF 移到 `raw/personal/conversations/`,并提炼出一条低置信度观察:在职业与身份不确定性下,分阶段行动有助于缓解瘫痪。

## [2026-04-06] 更新 | 增加 Claude Code 兼容指南

新增了根级 `CLAUDE.md`,让 Claude Code 也能遵循与 `AGENTS.md` 一致的本地限定查询、分层边界、摄取规则与维护预期。

## [2026-04-06] 更新 | 增加仓库沟通指南

把 `grapeot/context-infrastructure` 里的沟通原则适配成根级 `COMMUNICATION.md`,并接入 `AGENTS.md`、`schemas/AGENTS.md` 与 `CLAUDE.md`,让仓库会话可以共享一套写作与协作风格。

## [2026-04-06] 更新 | wiki 全面中文化并固化中文写作规范

把 `wiki/` 下现有维护页、索引与日志统一改成中文,同时把"以后所有维护态 wiki 页面默认用中文写"写进 `AGENTS.md`、`CLAUDE.md`、schemas、skills 与 repo-map 生成脚本。

## [2026-04-06] 更新 | 明确 lint 中文化职责与 query 回写标准

为 `schemas/lint.md` 增加了"把英文维护页自动规范成中文"的清理规则,并把 `schemas/query.md` 中 `useful again` 的判断标准细化成可执行的回写启发式。

## [2026-04-06] 更新 | 细化 query 回写的复用与洞察标准

把 `schemas/query.md` 中的回写判断进一步收敛成四条明确标准,并补充了一条规则:如果当前对话本身产出了足够好的洞察、新发现或可复用区分,也应写回 wiki。

## [2026-04-06] 更新 | 显式支持从桥接长文反向蒸馏 self

把 `wiki/bridges/essays/` 明确纳入 `wiki/self/` 的二级证据源:允许从桥接长文中提取 observations,尤其是 framing、抽象习惯与写作风格,但要求跨多篇或结合 `raw/personal/` 证据后,才能升级为 pattern。

## [2026-04-07] 反思 | 从桥接长文提炼抽象框架优先写作观察

第一次按新规则从 `wiki/bridges/essays/` 反向蒸馏 `wiki/self/`,新增一页 observation,记录在桥接长文中暴露出来的抽象框架优先写作与问题 framing 倾向。

## [2026-04-07] 摄取 | MoE2 边缘 LLM 协同推理

把 `MOE2.pdf` 从 `inbox/to-ingest/` 移到 `raw/external/`,并创建了一页知识稿,总结它如何把异构边缘 LLM 的协同推理拆成两层 expert selection、预算约束和离散单调优化问题。

## [2026-04-06] 摄取 | AI Architect Lens 与知识系统产品定义

把一份用户提供的 AI architect 课程讲义保存到 `raw/external/ai-architect-product-definition-brief.md`,随后创建了 `AI Architect Lens` 维护页,并新增一页用该镜头反推 `context-infrastructure` 与 `llm-wiki` 的产品定义信念。

## [2026-04-06] 更新 | 重写知识系统产品定义信念页

根据一份新的用户分析大纲,完整重写了 `AI 知识系统的产品定义信念`,把比较主线改为"共同的信息复利逻辑、不同的数据分布、不同的目标函数与不同的蒸馏层次",并补充修正了对 agentic workflow、online learning 类比和多层去噪架构的判断。

## [2026-04-06] 查询 | 从知识编译到人格蒸馏

基于既有比较页与新的分析主线,写成一篇桥接长文,论证 `llm-wiki` 与 `context-infrastructure` 作为两类"信息复利系统"的共同母题,以及它们在数据分布、目标函数、agent workflow 与蒸馏层次上的根本差异。

## [2026-04-06] 查询 | 信息复利系统设计框架

从 `llm-wiki` 与 `context-infrastructure` 的比较继续向上抽象,新增一页通用设计框架,讨论信息复利系统的设计准则、关键因素、通用模板,并构造了两个新的系统例子:`Decision Ledger` 与 `Personal Failure Compiler`。

## [2026-04-06] 更新 | 以默认工作面重写信息复利系统页

把 `信息复利系统设计框架` 从"设计准则清单"重写为围绕单一洞察展开的分析:信息复利设计的关键,是把未来会反复用到的信号提前提炼成默认工作面。同时把例子替换成两个更远离知识库与个人上下文的系统:`Customer Objection Surface` 与 `Operational Early-Warning Surface`。

## [2026-04-06] 查询 | 机制设计研究的信息复利系统

围绕边缘计算与网络经济学研究中的机制设计痛点,新增一页专门分析:为什么理论推导不应继续充当第一道筛选器,以及如何把"什么值得证明"的研究判断提炼成一个新的默认工作面。

## [2026-04-06] 更新 | 同步长文新标题并补充 TL;DR

把桥接长文的相关引用标题统一更新为《从Andrej Karpathy的LLM Wiki和鸭哥的context infrastructure看信息复利系统的设计》,并在正文开头补上一个简短 `TL;DR`。

## [2026-04-06] 更新 | 用研究场景替换信息复利系统页示例

把 `信息复利系统设计` 中原先两个较通用的例子替换成一个更贴近当前研究工作的简短段落,改为说明边缘计算与网络经济学机制设计里,如何把"什么值得证明"的判断提炼成默认工作面。

## [2026-04-08] 摄取 | AI Architect Context Intelligence

把一份用户提供的 context intelligence 课程讲义保存到 `raw/external/ai-architect-context-intelligence.md`,新增 `AI Architect 的 Context Intelligence 镜头` 维护页,并把它接入 `AI Architect Lens` 与知识索引。

## [2026-04-09] 查询 | 课题组公共研究知识库的产品化与评测策略

围绕把当前 `raw -> wiki` 架构产品化为课题组公共知识库的设想,新增一页 bridge,解释为什么系统应从知识编译扩展到研究判断蒸馏,并给出适合研究场景的第一版评测与 OKR 框架。

## [2026-04-09] 反思 | 课题组公共研究知识库产品化讨论

把一段关于课题组公共研究知识库架构、bootstrap、反共识写回与 MVP 取舍的对话保存到 `raw/personal/conversations/课题组公共研究知识库产品化讨论.md`,并提炼出两条低置信度 self observation:一条关于"开箱即用洞察优先"的产品偏好,另一条关于研究系统必须承接反共识判断写回的设计警觉。

## [2026-04-09] 摄取 | 课题组公共知识库的产品定义信念

把一份新的用户产品定义稿保存到 `raw/personal/writings/课题组公共知识库产品定义信念.md`,新增 bridge 页 `课题组公共知识库的产品定义信念`,并把它接入既有的公共研究知识库策略页与索引。

## [2026-04-09] 查询 | 课题组公共知识库 MVP 架构

基于刚形成的 product definition belief,新增一页专门收敛 MVP 架构,明确第一版应使用 `raw / knowledge / insights` 三层可见结构,并保留轻量隐含 maps 与 query write-back 闭环。

## [2026-04-09] 更新 | 把公共知识库 MVP 架构重写成软件产品架构

根据新的用户澄清,把 `课题组公共知识库MVP架构` 从"知识库目录与 agent harness 形状"重写成"真实软件产品架构",明确前端工作台、后端 API、异步任务、AI 编译层、存储分层和写回提案机制。

## [2026-04-09] 整理 | 收拢 inbox 为单一待处理目录

移除了 `inbox/to-ingest/` 与 `inbox/to-review/` 两个子目录,把相关 README、schema 与 skill 说明统一改成只使用 `inbox/` 作为待处理材料入口。

## [2026-04-10] 摄取 | Pi coding agent 极简 harness

把两份与 `pi` 相关的新来源从 `inbox/` 移到 `raw/external/`,新增一页知识稿,总结它如何用极简 prompt、四工具工作面与强可观察性来重写 coding agent harness 的边界。

## [2026-04-10] 摄取 | badlogic/pi-mono 仓库地图

把紧凑的 GitHub 仓库 snapshot 抓取到 `raw/external/github-repo-badlogic-pi-mono.md`,并围绕主题"coding agent 架构与工程实践"在 `wiki/knowledge/badlogic-pi-mono-repo-map.md` 生成了初始维护页。

## [2026-04-10] 查询 | Claude Code、Codex 与 pi 的 harness 对比

基于已有 `pi` 主题页、`pi-mono` 仓库地图和两份原始来源,新增一页比较稿,收束三类 coding agent harness 在默认壳厚度、可观察性与"内建还是外置"策略上的主要差异。

## [2026-04-10] 摄取 | Claude Code harness

把两份 Claude Code 新来源从 `inbox/` 移到 `raw/external/`,新增一页知识稿,区分官方工作机制说明与外部分析稿的置信度,并补强既有的 harness 对比页。

## [2026-04-11] 查询 | 课题组公共知识库的架构风险与分层设计

围绕把 `llm-wiki` 推进成公共知识库时出现的三类担心,新增一页桥接稿,拆解多用户治理、上下文窗口与 token 成本问题的共同根因,并收束成一版更稳的页面分层、关系模型与推荐仓库架构。

## [2026-04-12] 摄取 | Clawhouse 多设备 Agent 工作台

把一份新的个人项目设想保存到 `raw/personal/writings/clawhouse-项目设想.md`,新增 bridge 页 `Clawhouse:多设备 Agent 的统一入口与运行时工作台`,收束其核心问题、运行时上下文洞察、现成方案缺口与三组产品 OKR,并接入索引。

## [2026-04-12] 摄取 | multica-ai/multica 仓库地图

把紧凑的 GitHub 仓库 snapshot 抓取到 `raw/external/github-repo-multica-ai-multica.md`,并围绕主题"多设备 agent 访问与运行时工作面"在 `wiki/knowledge/multica-ai-multica-repo-map.md` 生成了初始维护页。

## [2026-04-12] 查询 | multica 与 clawhouse 的目标差异

基于现有 `Clawhouse` bridge 页与 `multica` 仓库地图,新增一页对照分析,收束两者在第一性目标与核心价值上的差异:前者优先解决个人多设备场景下的 agent 连续性与可观察性,后者优先把 agent 纳入团队任务系统。

## [2026-04-12] 查询 | clawhouse 相对 multica 的独特价值

在既有对照页基础上,进一步补充一轮分析,区分 `multica` 已经 address 的任务层可见性,与 `clawhouse` 可能主打的运行时现场可见性、移动端 re-entry 和项目级 dashboard 价值。

## [2026-04-12] 查询 | clawhouse 原始动机校正

根据新的用户澄清,回调 `clawhouse` 的产品定义优先级:其第一性动机不是黑盒治理,而是"希望在任何地方都能访问我的 agent";可观察性与 dashboard 被重写成服务这个主目标的条件,而不是更高一层目标。

## [2026-04-12] 更新 | 重写 clawhouse 产品定义信念

把 `Clawhouse` 维护页从"多设备 agent 工作台 + 黑盒问题"重写成一版更聚焦的产品定义信念:核心不再是 observability 本身,而是让 agent 变成一种可随身访问、可重新接回的持续存在。

## [2026-04-12] 查询 | clawhouse 定义中的有效点与风险

围绕重写后的 `clawhouse` 产品定义信念,新增一页批判性分析,区分其中哪些判断已经直击本质,哪些仍带有 wishful thinking,哪些只是实现偏好或可有可无的包装。

## [2026-04-12] 查询 | 被持续委托的工作主体

围绕"同一个被我持续委托的工作主体"这一新洞察,新增一页桥接分析,拆解其本质、今天的 coding agent 与 agent 产品距离这一概念还有哪些 gap,以及 `clawhouse` 可以优先桥接哪些对象层、委托层与接回语义层的问题。

## [2026-04-12] 更新 | 以"持续在岗的同事"重写 clawhouse

根据新的"人类同事协作"类比,进一步重写 `Clawhouse` 维护页,把主线从"可随身访问的对象"推进成"有稳定人格、持续关系、ongoing assignments 与可接回协作的持续在岗同事"。

## [2026-04-12] 更新 | 校正 clawhouse 中 agent 与 assignment 的边界

根据新的用户反馈,进一步重写 `Clawhouse` 维护页,明确区分 `agent`、`assignment`、`session`、`runtime` 与 `device`:agent 不等于某个 runtime,也不等于某一项工作;更准确的主线是"持续协作对象"而不是"工作本身"。

## [2026-04-12] 更新 | 重写"被持续委托的工作主体"

根据新的用户反馈,重写这页概念分析,保留其对象层洞察,但明确校正旧版里"agent 与某项工作绑定过紧"的问题,把主线改成:agent 是可以持续持有多项 assignment、并被用户持续协作与持续接回的对象。

## [2026-04-12] 查询 | clawhouse 最小但仍有 magic 的 MVP 架构

围绕当前 `clawhouse` 的产品定义信念,新增一页架构分析,对比聊天桥接型、设备中心型、轻控制平面型与完整 orchestration 型四种路径,并推荐以 `light control plane + per-device node + structured re-entry artifact + mobile-first launcher` 作为最稳的 MVP 方案。

## [2026-04-12] 更新 | 以 Agent Kernel 重写 clawhouse MVP 架构

根据新的用户反馈,推翻上一版过于设备锚定的 MVP 架构,改用 `Agent Kernel + Executors + Re-entry Inbox` 作为新的主语,把 magic 的来源从"移动端看到设备和状态"改成"移动端重新见到那个持续在岗、主动给你工作简报的 agent"。

## [2026-04-12] 摄取 | openclaw/openclaw 仓库地图

把紧凑的 GitHub 仓库 snapshot 抓取到 `raw/external/github-repo-openclaw-openclaw.md`,并围绕主题"个人 AI assistant、Gateway 与持续身份层"在 `wiki/knowledge/openclaw-openclaw-repo-map.md` 生成了初始维护页。

## [2026-04-12] 更新 | 补强 openclaw 的公开文档信号

补充整理 `OpenClaw` 官方 docs 中关于 Gateway、`SOUL.md`、multi-agent routing、heartbeat 与 device nodes 的公开信息,新增 `raw/external/openclaw-public-docs-notes.md`,并据此把 `openclaw/openclaw` 仓库地图从薄摘要补强成可用于后续和 `clawhouse` 对照的维护页。

## [2026-04-12] 查询 | agent 产品让用户看到什么,以及 clawhouse 还能补什么

围绕"用户在使用 agent 时到底想看到什么"这一核心问题,新增一页桥接分析,对比 terminal-first coding agent、`OpenClaw` 与 `multica` 各自暴露的默认对象,并把 `clawhouse` 最可能的剩余价值收束到 `work commitment visibility` 这一层。

## [2026-04-12] 反思 | Clawhouse 产品质疑与能力焦虑

把一段关于 `clawhouse` 产品存在意义的深度质疑对话保存到 `raw/personal/conversations/2026-04-12-clawhouse-codex-产品质疑与能力焦虑.md`,并更新 `Clawhouse` bridge 页。核心判断包括:

- `Termius + tmux` 已经解决了"可见"和"可控"两件最硬的事,是 clawhouse 必须打赢的 baseline
- clawhouse 作为"另起炉灶的完整产品",存在意义已经明显变弱
- 建议把 clawhouse 从"产品定义"降级为"一组关于 agent 默认工作面的未解问题集"
- 区分"做不出完整系统"(正常)和"没有产品判断力"(不成立)

同时校正了之前对 `OpenClaw` 和 `multica` 的用户视角分析:之前把"系统内部对象"误当成了"用户默认看到什么"。

## [2026-04-13] 更新 | Clawhouse 新方向:先做自己能用的小工具

更新 `Clawhouse` bridge 页,加入新方向:**与其纠结做一个"完整产品",不如先做一个自己能用的、解决具体问题的小工具**。

核心转变:
- 从"要做成通用产品"转向"先做自己能用的小工具"
- 具体目标:解决用手机、iPad 也可以继续跟 agent 工作的问题
- 最小可行路径:只服务你自己、只解决一个具体场景、用最简单的方式实现

同步了更清晰的背景描述:多设备(实验室台式机、宿舍游戏本、MacBook air、腾讯云 vps)上的 agent 无法在移动端访问,聊天软件方式会导致黑盒问题。

## [2026-04-13] 思考 | 移动端 agent 交互界面的中间态可能性

在 `Clawhouse` 页面新增"移动端交互界面的核心冲突"分析:
- 聊天窗口方案(OpenClaw):阅读友好但黑盒、控制力弱
- 终端方案(Termius+tmux):完全掌控但移动端体验差

尝试抽象 coding agent 交互界面的本质要素(输出/反馈、过程可见性、控制能力、上下文),探索中间态的可能性:在"足够信息量"和"友好移动端呈现"之间取得平衡。

## [2026-04-13] 思考 | 本质要素拆解与工作面抽象

新增对交互界面本质要素的进一步拆解:
- 输入:对话框
- 输出:文本流
- 控制能力:小弹窗 + slash 命令(可改进为类似 app 的交互)
- 上下文:最难的问题,移动端更难呈现

**核心洞察:** clawhouse 只在移动端使用,不是替代电脑工作流。

**更深层的抽象:**
- 人类默认的工作面是"项目",不是工具
- 就像用微信时想的是聊天内容,而不是用哪个设备打开
- 需要一个封装层把设备、coding agent 的摩擦封装起来
- 但目前完全不知道怎么做

## [2026-04-13] 思考 | 两层同步方案

提出更可行的方案,放弃"完全透明",改为分两层同步:

**静态上下文**(已有方案):代码状态、文章状态 - GitHub / iCloud 等

**动态上下文**(需要解决):聊天记录、对话进度 - 例如"当前聊到哪了、agent 知道什么"

**具体场景:** 出门拿手机 iPad 想继续当前对话,需要知道聊了什么、聊到哪了。

这比完全透明弱很多,但更可行:不需要迁移 agent 内存,不需要同步执行命令,只需要同步"对话历史"和"已知信息"。

## [2026-04-13] 思考 | 同步对话历史 JSON 的具体方案

提出非常务实的实现思路:直接同步 coding agent 导出的对话历史 JSON 文件。

**现状:** Codex 保存在 `.codex/` 目录,pi 和 Claude Code 可能也有类似机制。

**方案:** 把 JSON 同步到共享存储(GitHub、iCloud),移动端读取恢复上下文。

**优点:** 不需要改造 agent,利用现有文件同步,实现简单。

**待解决问题:** 不同 agent JSON 格式不同、并发处理、大文件增量同步。

## [2026-04-13] 查询 | Pi Agent 对话存储方式调研

调研 `pi` agent 的对话存储机制:

**格式:** JSONL 文件(JSON Lines),树状结构
**位置:** `~/.pi/agent/sessions/`,按 working directory 组织
**特点:** 每个 entry 有 `id` 和 `parentId`,支持分支(branching)
**命令:** `/tree` 导航历史,`/export` 导出 HTML,`/fork` 创建分支

相比 Codex 的 JSON 格式,Pi 的 JSONL 更便于增量追加和读取,树状结构天然支持复杂的分支管理。

## [2026-04-13] 反思 | OpenClaw 设计策略的批判性观察

指出 OpenClaw 的设计策略:**通过人格化"欺骗"用户把 agent 当人来对待,从而锁定用户在单一设备/入口,避免处理多设备同步的复杂性**。

**核心洞察:** OpenClaw 用**人格锁定**解决上下文问题,而不是用同步机制。用户因为情感连接而愿意一直用同一台设备,上下文自然堆积在那里。

这是与 Clawhouse 设想(用同步机制解决上下文问题)完全不同的路径。

## [2026-04-13] 反思 | 人格化与同步的互补性

提出关键问题:"Why not both?"

**核心洞察:** OpenClaw 的人格化(表现层)和 clawhouse 的同步(基础设施层)不是对立的,而是互补的。

如果 clawhouse 能解决上下文同步,它实际上**增强**了人格化的可信度--"它真的记得我们之前聊过什么"。

人格化是表现,同步是基础设施。做好同步,让人格化更真实、更可信。

## [2026-04-14] 摄取 | ReflexioAI/reflexio 仓库地图

把紧凑的 GitHub 仓库 snapshot 抓取到 `raw/external/github-repo-reflexioai-reflexio.md`,并围绕主题"仓库架构与工程实践"在 `wiki/knowledge/reflexioai-reflexio-repo-map.md` 生成了初始维护页。

### [2026-04-14] 更新 | ReflexioAI/reflexio 仓库地图详细版

深入阅读仓库核心文件(developer.md、server/OVERVIEW.md、generation_service.py、reflexio_lib.py、profile/playbook generation service 等),大幅扩展 repo map 内容:

- 补充完整目录结构和架构流程图
- 详细记录 Profile Generation、Playbook Extraction、Agent Success Evaluation、Search & Retrieval 等核心机制
- 添加 LLM 集成、Storage Layer、Reflexio Facade 等架构细节
- 记录测试与质量保证机制
- 补充关键规则与约束(API 开发、Prompts、Config)
- 扩展 raw snapshot 文件,添加更多核心代码文件内容

### [2026-04-14] 更新 | Reflexio 跨用户共享与聚合逻辑

开发者分享了 Personal Agent vs Vertical Agent 的区分视角,补充关键洞察:

- **核心设计**:三层分离架构(User Profiles / User Playbooks / Agent Playbooks)
- **跨用户共享机制**:集中式存储(SQLite/Supabase),所有用户数据统一存储
- **聚合逻辑详解**:
  - Embedding 聚类(Agglomerative < 50条 / HDBSCAN >= 50条)
  - Cluster fingerprint 增量检测(SHA-256 hash)
  - LLM 聚合:方向分组 + majority-wins 冲突处理
  - AgentPlaybook 输出结构(trigger/instruction/pitfall)
- **关键洞察**:Profile 回答"用户喜欢什么",AgentPlaybook 回答"这类任务应该怎么做"

### [2026-04-14] 撰写 | 公共知识库、Reflexio 与 EvoMap 的三方对比分析

扩展原有二元对比,加入 EvoMap 形成三方对比:

**三系统本质差异**:
- 公共知识库:认知知识(人消费),保留张力(思考价值),课题组规模
- Reflexio:操作知识(Agent 执行),解决冲突(Majority-wins),单 Agent 多用户
- EvoMap:执行知识(Agent 继承),自然选择验证,百万 Agent 网络

**三层知识谱系**:认知 → 操作 → 执行(抽象度递降)

**因果链条**:消费主体 → 冲突哲学 → 验证方式 → 架构设计

**可借鉴机制**:
- 从 Reflexio:增量聚合、两步聚合、结构化输出、动态触发、版本追踪
- 从 EvoMap:Reputation、环境上下文、进化日志、蜂群协作

**不应照搬**:Majority-wins、自然选择验证、Credits 激励、实时协议、Env Fingerprint

### [2026-04-14] 更新 | 补充操作知识 vs 执行知识的本质区别

在对比分析文档中新增"操作知识 vs 执行知识的本质区别"章节:

**7 个关键差异**:
1. 来源不同:用户告诉 Agent(操作) vs Agent 自己试错发现(执行)
2. 抽象度不同:行为规范(操作) vs 具体方案(执行)
3. 可执行性不同:需理解后执行(操作) vs 可直接执行(执行)

## [2026-04-18] 摄取 | 求职范式转变:让工作找到你

从 inbox 摄取 Superlinear Academy 社区的求职经验分享。

**核心观点**:对中高级 corporate 岗位(Data Scientist, ML Engineer, AI Engineer)来说,找工作的逻辑已经变成--不是你在找工作,而是工作在找你。

**市场现实**
- ATS 系统失效:申请量 2021→2025 涨 239%,海投成功率仅 1%-2%
- 隐藏职位市场:约 70% 职位不公开 posted
- AI 冲击:entry level 需求减少,senior 职位占比上升

**核心策略**
1. LinkedIn 作为 landing page,突出 PMF (profile-market fit)
2. 简历与具体岗位对齐,准备多版
3. 面试作为市场调研,多面获取反馈
4. 用好 recruiter 渠道,保持边界
5. 提前准备:reference、documentation 在职时就开始维护

新增页面:
- [求职范式转变:让工作找到你](knowledge/求职范式转变:让工作找到你.md)

源文件移至:
- `raw/external/superlinear-job-search-paradigm-shift.md`
4. 环境依赖不同:低(操作) vs 高(执行)--解释 EvoMap 需要 Env Fingerprint
5. 验证方式不同:用户纠正验证(操作) vs Agent 执行验证(执行)--解释 EvoMap 需要自然选择
6. 失败容忍度不同:高(操作) vs 低(执行)--解释 EvoMap 需要严格验证
7. 架构设计因果链条:操作知识 → Majority-wins;执行知识 → Protocol + Reputation + Credits

**实际案例对比**:Reflexio 提取"部署前确认区域"(用户纠正);EvoMap 封装"pip install pandas==1.3.0"(Agent 试错)

## [2026-04-14] 摄取 | inbox 书籍材料

将 inbox 中的 6 本书籍 PDF/EPUB 移动到 `raw/external/`,并创建知识页面:

- **Agentic Design Patterns** (Antonio Gullí, 2025): AI Agent 设计模式实践指南
- **Ace the Data Science Interview** (Nick Singh & Kevin Huo, 2021): 数据科学面试准备指南,201 道真实面试题
- **An Introduction to Probability Theory and Its Applications** (William Feller): 经典概率论教材
- **The Almanack of Naval Ravikant** (Eric Jorgenson): Naval 关于财富、幸福、学习的智慧合集
- **Linear Algebra Done Right** (Sheldon Axler): 经典线性代数教材
- **如何了解一个人** (戴维·布鲁克斯, 2025): 关于深度人际连接的探索

新增页面:
- [Agentic Design Patterns](topics/agent-harness-runtime/agentic-design-patterns.md)
- [Ace the Data Science Interview](topics/learning-judgment-mental-models/ace-the-data-science-interview.md)
- [Naval Ravikant 智慧年鉴](knowledge/naval智慧年鉴.md)
- [概率论入门](topics/learning-judgment-mental-models/概率论入门.md)
- [线性代数正确入门](topics/learning-judgment-mental-models/线性代数正确入门.md)
- [如何了解一个人](topics/learning-judgment-mental-models/如何了解一个人.md)

### [2026-04-14] 更新 | Embedding 聚类 vs LLM 聚合的分工

补充两步聚类的核心分工说明:

- **Embedding 聚类**:语义分组(哪些条目是一类事)
- **LLM 聚合**:内容合成(这类事应该怎么做)

LLM 聚合的 5 个作用:
1. 结构化提炼(自由文本 → SOP 格式)
2. 合并相似条目(不同表达 → 一个简洁表述)
3. 处理冲突(Majority-wins)
4. 去重检查(与 existing_approved_playbooks 比较)
5. 生成可执行指令(用户说的 → agent 应该做的)

## [2026-04-18] 摄取 | AI 让我们重新开始享受自己的职业

从 inbox 摄取 Superlinear Academy 社区文章。

**核心判断**
- 任何职业都处在"机械执行 / 判断"的 spectrum 上
- 工业化分工会持续把岗位日常推向机械端,因为更易标准化、管理与验收
- AI 的更深影响不是让人做更多机械活,而是压缩机械部分,让职业重新回到判断
- 对初级从业者,成长关键不主要来自手工执行,而来自对真实结果的追问、回溯与取舍
- 但对外科、木工、厨师等依赖手感积累的职业,这个逻辑不完全成立

新增页面:
- [AI 让我们重新开始享受自己的职业](topics/career-positioning-job-search/AI%20让我们重新开始享受自己的职业.md)

源文件移至:
- `raw/external/superlinear-ai-让我们重新开始享受自己的职业.md`

顺手整理:
- 补回 [求职范式转变:让工作找到你](knowledge/求职范式转变:让工作找到你.md) 在 `wiki/index.md` 中的缺失入口
- 删除 `inbox/.DS_Store`

## [2026-04-21] 摄取 | safety-research/automated-w2s-research 仓库地图

把紧凑的 GitHub 仓库 snapshot 抓取到 `raw/external/github-repo-safety-research-automated-w2s-research.md`,并围绕主题"自动化 alignment research harness 与 weak-to-strong 监督"在 `wiki/knowledge/safety-research-automated-w2s-research-repo-map.md` 生成了初始维护页。

## [2026-04-21] 摄取 | inbox 外部材料

从 `inbox/` 摄取 3 份外部材料,并移动到 `raw/external/`:

- `Automated Weak-to-Strong Researcher.pdf`
- `对 Human in the Loop 的新理解.md`
- `那些说UI会消失的人,把人机交互理解错了一半.md`

新增页面:

- [Automated Weak-to-Strong Researcher](topics/agent-harness-runtime/automated-weak-to-strong-researcher.md)
- [Agent 时代的人机交互新命题](topics/agent-harness-runtime/agent时代的人机交互新命题.md)

同步更新:

- [AI 自演化研究 Harness](topics/agent-harness-runtime/ai-self-evolution-research-harnesses.md):补入 AAR 作为 outcome-gradable research harness 的对照案例
- [wiki/index.md](index.md):补入新知识页入口

## [2026-04-21] 查询 | AAR knowledge sharing 的设计洞察与取舍

围绕 `safety-research/automated-w2s-research` 的 findings sync、`share_finding`、snapshot 与本地文件工作面,整理了一页可复用总结:

- [AAR knowledge sharing 的设计洞察与取舍](topics/agent-harness-runtime/AAR%20knowledge%20sharing%20的设计洞察与取舍.md)

核心收获:这套 sharing 更像"同步到本地的 agent 工作面 + 可下载的 workspace snapshot",而不是一个更强的在线检索系统;其结构化程度与取舍都高度依赖 weak-to-strong 研究任务本身的统一指标与并行探索场景。

## [2026-04-22] 摄取 | alchaincyf/nuwa-skill 仓库地图

把紧凑的 GitHub 仓库 snapshot 抓取到 `raw/external/github-repo-alchaincyf-nuwa-skill.md`,并围绕主题"仓库架构与工程实践"在 `wiki/knowledge/alchaincyf-nuwa-skill-repo-map.md` 生成了初始维护页。

## [2026-04-22] 查询 | alchaincyf/nuwa-skill 蒸馏理念与方法论补充

继续下钻 `alchaincyf/nuwa-skill` 的 `SKILL.md`、`references/extraction-framework.md` 与 `references/skill-template.md`,把 repo map 从顶层结构图扩展到方法论与 workflow 层。

更新页面:
- [alchaincyf/nuwa-skill 仓库地图](topics/agent-harness-runtime/alchaincyf-nuwa-skill-repo-map.md)

补充重点:
- 明确其核心定位是"蒸馏认知操作系统",不是语录模仿
- 补入双入口分流、6 路并行 research、三重验证、矛盾保留、诚实边界、Agentic Protocol、Phase 4/5 质量验证与精炼机制
- 说明 `references/`、`examples/` 与 `scripts/` 在整条 distillation workflow 中各自扮演的角色

## [2026-04-22] 查询 | 公共知识库的联邦底座与蒸馏共享层

围绕"联邦方向"与"只共享蒸馏结果"两种公共知识库方向,整理出一条更稳的判断:

- [什么是公共知识库应该共享的公共知识](topics/research-knowledge-governance/什么是公共知识库应该共享的公共知识.md)(原题:公共知识库的联邦底座与蒸馏共享层)

核心结论:两者不应被当成同一层面的二选一。联邦更适合作为部署与治理底座;蒸馏共享更适合作为公共工作面的默认内容协议。如果必须压成一句话,就是"系统部署上做联邦,公共工作面上做蒸馏共享"。

## [2026-04-23] 查询 | AI 产业分层地图(2026)

围绕"与其先枚举公司,不如先建立 AI 产业分层地图"的问题,新增一页知识页:

- [AI 产业分层地图(2026)](knowledge/AI产业分层地图(2026).md)

本次写回把 AI 市场压成一张更适合方向判断的结构图,而不是公司清单。核心判断包括:

- AI 更像分层堆栈,而不是线性上下游
- VC 的钱最集中在底层,尤其是 frontier labs 与 compute
- 企业预算更快流向上层,尤其是 coding、copilot 与 vertical ROI 场景
- 中间层如 runtime、eval、observability、agent orchestration 仍在早期,结构尚未完全定型

同时更新:
- `wiki/index.md`

## [2026-04-23] 查询 | AI 产业的付钱地图(2026)

围绕"AI 产业链条上每个环节的钱从哪来、VC 到底是什么、给钱的人是否也应该进入产业地图"的问题,新增一页知识页:

- [AI 产业的付钱地图(2026)](knowledge/AI产业的付钱地图(2026).md)

本次写回把 AI 产业中的出钱方压成六类:

- 超大平台 / 云 / 芯片公司
- 传统独立 VC
- 企业 VC / 战略投资部门
- Growth Equity / Crossover / 晚期资本
- 主权基金 / 政府资金 / 国家开发资本
- 大企业采购方 / 运营型战略买家

并明确区分:

- 经营性的钱:客户为当前结果付的钱
- 融资性的钱:资本为未来可能性付的钱

同时更新:
- `wiki/index.md`

## [2026-04-22] 维护 | 重写"公共知识库的联邦底座与蒸馏共享层"

根据新一轮分析,重写了页面:
- [什么是公共知识库应该共享的公共知识](topics/research-knowledge-governance/什么是公共知识库应该共享的公共知识.md)(原题:公共知识库的联邦底座与蒸馏共享层)

本次修改去掉了"公共层只共享蒸馏信号"的武断结论,改为明确区分两类问题:
- 从高噪音数据中提取稳定信号的蒸馏问题
- 对原始材料进行索引、关联与可回查建模的 raw/wiki 问题

并指出公共知识库的架构困难来自同时处理这两类问题的混合体,而不是单纯的共享协议选择。

## [2026-04-22] 维护 | 页面更名为"什么是公共知识库应该共享的公共知识"

将页面
- `bridges/公共知识库的联邦底座与蒸馏共享层.md`
更名为
- [`bridges/什么是公共知识库应该共享的公共知识.md`](topics/research-knowledge-governance/什么是公共知识库应该共享的公共知识.md)

同时调整页面标题与 `wiki/index.md` 中的主题描述,使其从"联邦底座与蒸馏共享层的搭配问题"转向更本质的问题:公共知识库到底应该共享什么样的公共知识。

## [2026-04-22] 维护 | 补充"什么是公共知识库应该共享的公共知识"页面

根据后续两轮讨论,补充页面:
- [什么是公共知识库应该共享的公共知识](topics/research-knowledge-governance/什么是公共知识库应该共享的公共知识.md)

新增要点:
- `raw/wiki` 可能比"蒸馏信号层"更本质,因为真正高价值的 signal 最终会长成高权重 wiki 节点
- signal distillation 可被理解为 wiki 内部的 page creation / promotion / compression / graph reweighting 机制
- 架构上不必过早维护大量 handcrafted page type,可改为"自由 wiki + 最小关系骨架 + 使用轨迹/权重后验识别高价值公共知识"

## [2026-04-22] 维护 | 简化"什么是公共知识库应该共享的公共知识"中的高价值节点判定

继续更新页面:
- [什么是公共知识库应该共享的公共知识](topics/research-knowledge-governance/什么是公共知识库应该共享的公共知识.md)

本次修改进一步简化了"高价值节点"的判定逻辑:
- 不再强调复杂的多指标权重机制
- 不再主张额外增加独立压缩层
- 改为突出一个更简洁的判断:wiki 本身已经承担压缩功能,而"有复用"可能就是高价值公共知识最核心的判定信号

新增表述可压缩为一句话:`wiki 负责压缩,复用负责筛选。`

## [2026-04-22] 维护 | 将"复用"的主语从 agent 修正为人

继续更新页面:
- [什么是公共知识库应该共享的公共知识](topics/research-knowledge-governance/什么是公共知识库应该共享的公共知识.md)

本次修改补入一个关键修正:
- "复用"不应优先理解为 agent reuse,而应优先理解为 human reuse
- 公共知识更应由"人是否反复把某页带回后续工作流"来判定,而不是由 agent 在内部回答链中是否常调用来判定
- 这使高价值公共知识的识别更贴近产品目标,也允许更简洁的机制设计

## [2026-04-24] 摄取 | refactoringhq/tolaria 仓库地图

把紧凑的 GitHub 仓库 snapshot 抔取到 `raw/external/github-repo-refactoringhq-tolaria.md`，并围绕主题"仓库架构与工程实践"在 `wiki/knowledge/refactoringhq-tolaria-repo-map.md` 生成了初始维护页。

## [2026-04-24] 分析 | Tolaria MCP vs gogo-app 内置 runtime

对比两种 Agent 与知识库关系设计方案，写成 `bridges/Tolaria MCP vs gogo-app 内置 runtime.md`。

核心差异：
- Tolaria MCP：知识库是外部资源，Agent 是外部 CLI 工具，MCP 是开放接口
- gogo-app 内置 runtime：知识库浏览与 agent 对话在同一产品壳内，Agent 是内置能力

设计哲学差异：
- Agent 是工具还是工作面的一部分？
- 知识库主语是文件系统还是协作工作面？
- 用户要管理几个工具？
- 扩展性靠开放协议还是内置 runtime 抽象？

结论：不是"谁赢"的问题，而是"为谁设计"的问题——power-user 选 MCP，普通用户选内置 runtime。

## [2026-04-24] 分析 | Tolaria 各目录作用详解

详解 Tolaria 根目录下 14 个目录的作用，写入 `bridges/Tolaria 各目录作用详解.md`。

核心发现：
1. **.claude/** — Claude Code 配置，slash 命令定义任务工作流
2. **.github/** — CI/CD workflows（ci.yml、release.yml、release-stable.yml、auto-update-prs.yml）
3. **.husky/** — Git hooks：pre-commit（快速门控）、pre-push（完整检查，增量优化）
4. **demo-vault-v2/** — QA fixture，4 个测试场景（搜索、关系、导航、附件）
5. **design/** — ~50 个 Penpot 设计文件，任务级设计 → 合并到 ui-design.pen
6. **docs/** — 文档四层：ARCHITECTURE/ABSTRACTIONS/GETTING-STARTED/VISION + 78 个 ADR
7. **e2e/** — ~26 个 Playwright E2E 测试
8. **mcp-server/** — MCP 服务器，14 个工具，WebSocket 桥接
9. **patches/** — 编辑器依赖 patch（blocknote、tiptap、prosemirror-tables）
10. **public/** — 静态资源（favicon）
11. **scripts/** — 构建/发布/生成脚本
12. **src/** — React 前端（~98 组件、~87 hooks、~48 utils）
13. **src-tauri/** — Rust 后端（vault/、frontmatter/、git/、ai_agents.rs）
14. **tests/** — Playwright smoke + regression 测试

## [2026-04-24] 维护 | 合并 Tolaria 相关 wiki 页面

将分散的 Tolaria 分析页收束为一个总页：`bridges/Tolaria 综合分析.md`。

合并内容主要来自：
- `bridges/Tolaria MCP vs gogo-app 内置 runtime.md`
- `bridges/Tolaria 优秀开源仓库实践分析.md`
- `bridges/Tolaria 根目录文件作用速查.md`
- `bridges/Tolaria 各目录作用详解.md`

处理方式：
- 新建 `Tolaria 综合分析` 作为 Tolaria 的主入口
- `wiki/index.md` 改为优先链接总页
- 原页面暂时保留，避免丢失展开细节

## [2026-04-24] 维护 | 删除已合并的 Tolaria 旧页面

删除 4 个已被 `bridges/Tolaria 综合分析.md` 吸收的旧页面：
- `bridges/Tolaria MCP vs gogo-app 内置 runtime.md`
- `bridges/Tolaria 优秀开源仓库实践分析.md`
- `bridges/Tolaria 根目录文件作用速查.md`
- `bridges/Tolaria 各目录作用详解.md`

同时修正 `Tolaria 综合分析` 的来源依据，去掉对已删除页面的链接。

## [2026-04-24] 分析 | Tolaria 优秀开源仓库实践

深入学习 Tolaria 的文档体系、项目架构、开源实践，写成 `bridges/Tolaria 优秀开源仓库实践分析.md`。

核心发现：
1. **文档四层结构** — README（门面）、核心文档（架构/抽象/入门/愿景）、ADR（78 个决策记录）、CONTRIBUTING/SECURITY
2. **项目架构清晰** — 前端按职责分（components/hooks/utils）、后端按领域分（commands/vault/frontmatter/git）
3. **开源实践可复制** — AGENTS.md 给 AI 的指南、CI 门控（覆盖率 + CodeScene）、分层测试、贡献者体验
4. **设计哲学可迁移** — Convention over Configuration、Filesystem as Source of Truth、AI-Native by Design

gogo-app 可立即开始的行动：
- 写 VISION.md
- 开始写 ADR
- 完善 CONTRIBUTING.md 和 AGENTS.md
- 加 CI 门控
- 录 Loom 视频
- 创建 demo knowledge-base

## [2026-04-29] 摄取 | LuliYanng/Nono-Cowork 仓库地图

把紧凑的 GitHub 仓库 snapshot 抓取到 `raw/external/github-repo-luliyanng-nono-cowork.md`，并围绕主题“仓库架构与工程实践”在 `wiki/knowledge/luliyanng-nono-cowork-repo-map.md` 生成了初始维护页。

## [2026-04-29] 摄取 | 扩充 Nono-Cowork 机制地图

在不克隆仓库的前提下，通过 GitHub API 定向读取目录树与关键实现锚点，扩充 `raw/external/github-repo-luliyanng-nono-cowork.md` 的 follow-up evidence，并把 `wiki/knowledge/luliyanng-nono-cowork-repo-map.md` 从初始骨架补成机制地图。

## [2026-04-29] 查询 | Nono-Cowork 同步底层机制

定向读取 Nono-Cowork 的 Syncthing 文档、Electron 本地桥接、VPS `/api/sync/*` 端点、`SyncthingClient` 与 event watcher，把双端配对、folder provisioning、cross-device status 和多设备开放问题补入 `wiki/knowledge/luliyanng-nono-cowork-repo-map.md`。

## [2026-04-29] 摄取 | volcengine/openviking 仓库地图

把紧凑的 GitHub 仓库 snapshot 抓取到 `raw/external/github-repo-volcengine-openviking.md`，并围绕主题“仓库架构与工程实践”在 `wiki/knowledge/volcengine-openviking-repo-map.md` 生成了初始维护页。

## [2026-04-29] 摄取 | 扩充 OpenViking 机制地图

在不克隆仓库的前提下，通过 GitHub contents API 定向读取 OpenViking 的 server、session、storage/native engine、CLI、Ollama preflight、Vikingbot 与配置文档锚点，扩充 `raw/external/github-repo-volcengine-openviking.md` 的 follow-up evidence，并把 `wiki/knowledge/volcengine-openviking-repo-map.md` 从目录骨架补成围绕 `viking://` 虚拟文件系统、L0/L1/L2 分层、session memory、server runtime、Rust CLI 与 bot 工作面的机制地图。

## [2026-04-29] 查询 | OpenViking MCP 设计

定向读取 `openviking/server/mcp_endpoint.py`、`openviking/server/app.py`、`openviking/server/auth.py`、MCP 集成文档、Vikingbot MCP client 与 MCP endpoint 测试，确认 OpenViking 的 `/mcp` 是同进程 streamable HTTP endpoint，复用 REST API 的 auth/identity/namespace policy，暴露 9 个 context tools，并把结果补入 `wiki/knowledge/volcengine-openviking-repo-map.md` 与 raw follow-up evidence。

## [2026-04-29] 分析 | gogo 作为 Agent 能力层

把从 OpenViking MCP / tool 设计引出的产品启示写入 `wiki/bridges/gogo作为agent能力层.md`：公共知识库联邦架构可以进一步做成 skill / tool system，`gogo` 也可以拆成 `gogo-core`、`gogo-tools`、`gogo-mcp`、`gogo-agent`、`gogo-app`，其中微信等聊天入口应作为外层 adapter，而不是产品主语本身。

## [2026-04-29] 摄取 | inbox 文章《AI时代的投资与生存法则》

从 `inbox/` 摄取一篇 Superlinear 社区活动笔记，移入 `raw/external/`，并新增一页知识页，保留其中关于 `taste`、事件 / 结构 / 解释三层、`Rewired Index`、`software + labor -> model + compute`、Harness 创业机会与中间层挤压的一组判断。

**新增页面**
- [AI 时代的投资与生存法则](topics/ai-industry-investment/AI%20时代的投资与生存法则.md)

**更新页面**
- `wiki/index.md`

**源文件移至**
- `raw/external/AI时代的投资与生存法则.md`

## [2026-04-29] 查询 | 让 query 真正调用判断框架

围绕“为什么 wiki 里已有判断框架，但 query 仍不够深”这个问题，综合 `信息复利系统设计`、`知识库运行模型`、`AI 知识系统的产品定义信念` 与多条 self observation，新增一页 bridge，收束出一版优化方向：把 query 从“相关内容检索器”升级成“框架激活器”，并补上框架入口页、反共识沉淀与 query write-back 的闭环。

**新增页面**
- [让 query 真正调用判断框架](bridges/%E8%AE%A9query%E7%9C%9F%E6%AD%A3%E8%B0%83%E7%94%A8%E5%88%A4%E6%96%AD%E6%A1%86%E6%9E%B6.md)

**更新页面**
- `wiki/index.md`

## [2026-04-29] 维护 | 增加 `wiki/frameworks/` 最小实现

为降低 `wiki/bridges/` 的噪音并给 query 提供更稳定的默认工作面，新增与 `knowledge / self / bridges` 同级的 `wiki/frameworks/`。

**新增页面**
- `wiki/frameworks/README.md`

**迁移页面**
- `wiki/bridges/让query真正调用判断框架.md` → `wiki/frameworks/让query真正调用判断框架.md`

**更新页面**
- `AGENTS.md`
- `schemas/AGENTS.md`
- `schemas/query.md`
- `skills/kb-query/SKILL.md`
- `wiki/README.md`
- `wiki/index.md`
- `wiki/bridges/README.md`
- `wiki/bridges/knowledge-base-operating-model.md`

## [2026-04-29] 维护 | 增加 framework router 并整理高价值判断

为让 query 先站在更小、更硬的框架层上工作，在 `wiki/frameworks/` 下新增一页 router，并从 `knowledge/` 与 `bridges/` 中提炼几组高频判断，压成简短 framework 页；只在会破坏原页完整性时保留原页不动、改为摘要加链接。

**新增页面**
- `wiki/frameworks/router.md`
- `wiki/frameworks/知识系统判断框架.md`
- `wiki/frameworks/研究判断框架.md`
- `wiki/frameworks/AI系统产品判断框架.md`
- `wiki/frameworks/职业判断框架.md`

**更新页面**
- `AGENTS.md`
- `schemas/AGENTS.md`
- `schemas/query.md`
- `skills/kb-query/SKILL.md`
- `wiki/frameworks/README.md`
- `wiki/index.md`

## [2026-04-29] lint | 校对 framework 路由与入口链接

完成一轮轻量 lint，重点检查 `wiki/frameworks/` 的入口关系、迁移后旧路径残留，以及 `wiki/index.md` 新增 framework 条目的本地链接写法。

**处理内容**
- 把 `wiki/index.md` 中新增的 framework 链接改成直写文件名，避免本轮新增条目继续沿用 percent-encoded 本地路径
- 确认 `wiki/frameworks/` 页面都有来自 `index.md`、`README.md` 或 `router.md` 的入口
- 确认非 `log.md` 页面中不再残留指向 `wiki/bridges/让query真正调用判断框架.md` 的旧链接

**说明**
- 仓库中仍存在一批历史遗留的 percent-encoded 本地链接与早期坏链，本轮未做全库修复，只处理了本次 framework 改动直接涉及的入口与迁移关系

## [2026-04-29] 维护 | 为 framework router 补入配套 self 路由

继续收紧 `frameworks/` 作为默认工作面的入口作用。为 `router.md` 的四类问题都补入常配套读取的 `self/` 页面，并把同样的 self 配对写回各 framework 页；同时把 query 规则改成在进入 framework 后优先补读对应 self lens，而不是把 `self/` 当成完全后置的可选层。

**更新页面**
- `AGENTS.md`
- `schemas/AGENTS.md`
- `schemas/query.md`
- `skills/kb-query/SKILL.md`
- `wiki/frameworks/router.md`
- `wiki/frameworks/知识系统判断框架.md`
- `wiki/frameworks/研究判断框架.md`
- `wiki/frameworks/AI系统产品判断框架.md`
- `wiki/frameworks/职业判断框架.md`

## [2026-04-29] 维护 | 从 frameworks 中移除 self 路由

根据后续边界判断，`frameworks/` 不应混入 `self/` 内容，而应专注沉淀从 `knowledge/` 与 `bridges/` 中提取出来的可复用框架。因此撤回上一轮加入的 self 配套路由，并同步把 query 规则改回“router -> framework -> knowledge/bridges”的主路径。

**更新页面**
- `AGENTS.md`
- `schemas/AGENTS.md`
- `schemas/query.md`
- `skills/kb-query/SKILL.md`
- `wiki/frameworks/router.md`
- `wiki/frameworks/知识系统判断框架.md`
- `wiki/frameworks/研究判断框架.md`
- `wiki/frameworks/AI系统产品判断框架.md`
- `wiki/frameworks/职业判断框架.md`

## [2026-04-29] 维护 | 从 AI 宏观材料中抽出产业与投资框架

继续把 `knowledge/` 与 `bridges/` 中高复用、非个人判断层的分析骨架上提到 `frameworks/`。这轮主要把《AI 时代的投资与生存法则》中的三层信号过滤、`theme` vs `core holding`、`Harness` 创业带、行业哑铃结构等判断，连同 `AI 产业分层地图`、`AI 产业的付钱地图`、`衰退期的创业环境与技术判断` 里的结构镜头，压成一页新的产业与投资框架，并把它接入 router。

同时继续清理 `frameworks/` 中残留的个人判断层引用，保持该层只由 `knowledge/` 与 `bridges/` 支撑。

**新增页面**
- `wiki/frameworks/AI产业与投资判断框架.md`

**更新页面**
- `wiki/frameworks/README.md`
- `wiki/frameworks/router.md`
- `wiki/frameworks/研究判断框架.md`
- `wiki/frameworks/让query真正调用判断框架.md`
- `wiki/index.md`
- `wiki/knowledge/AI 时代的投资与生存法则.md`

## [2026-04-29] 维护 | 从 knowledge 中继续抽取产品定义与验证框架

继续按 `knowledge -> frameworks` 的方向上提高复用判断。这轮主要从 `AI Architect Lens`、`AI Architect 的 Context Intelligence 镜头`、`Pre-PMF 验证手册` 与 `Go to Market Multiple Times` 中抽出两类适合反复调用的框架：一类回答“到底在定义什么产品”，另一类回答“当前这条验证路径到底有没有开始成立”。

**新增页面**
- `wiki/frameworks/产品定义判断框架.md`
- `wiki/frameworks/产品验证判断框架.md`

**更新页面**
- `wiki/frameworks/README.md`
- `wiki/frameworks/router.md`
- `wiki/frameworks/AI系统产品判断框架.md`
- `wiki/index.md`
- `wiki/knowledge/ai-architect-lens.md`
- `wiki/knowledge/pre-pmf-validation-playbook.md`
- `wiki/knowledge/go-to-market-multiple-times.md`

## [2026-04-29] 维护 | 从 knowledge 中继续抽取职业信号与方向-执行框架

继续从 `knowledge/` 中上提适合反复调用的判断骨架。这轮主要把求职、简历、面试、reference、reputation 与双向选择相关判断压成一页职业信号框架；同时把 `Science / Craft` 的二层区分上提成一页方向与执行框架，用来诊断“该继续想还是先做”“这到底是方向错了还是执行不够”。

**新增页面**
- `wiki/frameworks/职业信号与叙事框架.md`
- `wiki/frameworks/方向与执行判断框架.md`

**更新页面**
- `wiki/frameworks/README.md`
- `wiki/frameworks/router.md`
- `wiki/frameworks/职业判断框架.md`
- `wiki/frameworks/产品定义判断框架.md`
- `wiki/frameworks/产品验证判断框架.md`
- `wiki/index.md`
- `wiki/knowledge/求职范式转变：让工作找到你.md`
- `wiki/knowledge/高级岗位简历的三条写法原则.md`
- `wiki/knowledge/增长工程师的职业押注与面试叙事.md`
- `wiki/knowledge/Databricks 的人才态度与双向选择.md`
- `wiki/knowledge/science-and-craft-cognitive-model.md`

## [2026-04-29] 维护 | 继续用 framework-distill 抽取 Harness 架构框架

按 `framework-distill` 的默认流程，继续扫描近期 `knowledge/` 页面，并从 harness 相关材料中上提一页新的框架入口。新页把 `Harness Engineering`、`Thin Harness, Fat Skills`、coding agent 上下文压缩工作流，以及 Claude Code / Codex / pi 的对比，压成一套更短的 harness 架构判断骨架，用来回答壳厚度、补偿面、subagent、上下文预算与 skill/tool 分工等问题。

**新增页面**
- `wiki/frameworks/Harness架构判断框架.md`

**更新页面**
- `wiki/frameworks/README.md`
- `wiki/frameworks/router.md`
- `wiki/frameworks/AI系统产品判断框架.md`
- `wiki/index.md`
- `wiki/knowledge/harness-engineering.md`
- `wiki/knowledge/thin-harness-fat-skills.md`
- `wiki/knowledge/coding agent 的上下文压缩工作流.md`
- `wiki/knowledge/coding-agent-harness-comparison.md`

## [2026-04-29] lint | 修复本地坏链并复核入口关系

执行一轮保守 lint，重点处理 maintained wiki 中由 percent-encoding、旧文件名和已删除页面遗留造成的本地坏链，同时检查孤儿页、重复命名和明显杂物。

**处理内容**
- 修复 `wiki/index.md` 中一批指向 `knowledge/` 与 `bridges/essays/` 的 percent-encoded 本地链接
- 从 `wiki/index.md` 移除一条已不存在的 `self/` 页面入口：`向 Reflexio 开发者提问(润色版)`
- 修复 `wiki/bridges/`、`wiki/knowledge/` 与 `wiki/self/` 中多处指向本地 `raw/`、`bridges/`、`essays/` 页面时仍沿用 percent-encoded 路径的问题
- 修复 `clawhouse` / `multica` 相关页面之间的旧文件名引用
- 修复 `Harness Engineering`、`Pre-PMF`、`Automated Weak-to-Strong Researcher`、`agent 时代的人机交互新命题` 等页的源文件链接写法
- 复核 `wiki/knowledge/`、`wiki/self/`、`wiki/bridges/`、`wiki/frameworks/`，未发现新的孤儿页
- 未发现 `.DS_Store` 或 `Thumbs.db` 等显式杂物

**说明**
- `wiki/log.md` 仍保留历史记录中的旧坏链与旧路径，不在本轮修复范围内
- 目前 maintained wiki（除 `log.md` 外）的本地内部链接检查已通过

## [2026-04-29] 维护 | 增加 framework-distill skill

把“从 `wiki/knowledge/` 与 `wiki/bridges/` 抽取可复用判断框架到 `wiki/frameworks/`”这类工作单独收束成一个 task-specific skill，避免每次都在聊天里临时重述边界。这个 skill 明确要求只上提非个人判断层的高复用骨架，并同步约束 router、README、index 与轻量 link check 的收尾动作。

**新增页面**
- `skills/framework-distill/SKILL.md`

**更新页面**
- `skills/README.md`
- `skills/kb-ops/SKILL.md`
- `schemas/AGENTS.md`

## [2026-05-01] 摄取 | yvonnegladwellstack/yvskills 仓库地图

把紧凑的 GitHub 仓库 snapshot 抓取到 `raw/external/github-repo-yvonnegladwellstack-yvskills.md`，并围绕主题“仓库架构与工程实践”在 `wiki/knowledge/yvonnegladwellstack-yvskills-repo-map.md` 生成了初始维护页。

## [2026-05-01] 维护 | 安装 `yvskills` 的 `action-coach`

继续下钻 `action-coach/SKILL.md` 与 `action-coach/gemini-gem-prompt.md`，把 `action-coach` 安装到本地 `skills/`，并补存一份源 skill 到 `raw/external/`。同时把 `yvskills` 仓库地图从 README 级初稿增强为基于 `SKILL.md` 的机制页，并收敛 `README.md` 与 `skills/README.md` 对 skills 列表的说明。

**新增文件**
- `skills/action-coach/SKILL.md`
- `skills/action-coach/gemini-gem-prompt.md`
- `raw/external/yvskills-action-coach-SKILL.md`

**更新页面**
- `wiki/knowledge/yvonnegladwellstack-yvskills-repo-map.md`
- `skills/README.md`
- `README.md`

## [2026-05-29] lint | 按话题重组 wiki 并生成静态网页

将原 `wiki/knowledge/` 与 `wiki/bridges/` 的维护页合并迁移到 `wiki/topics/`，按话题建立索引；保留 `wiki/self/` 与 `wiki/frameworks/` 作为独立层级。同时生成 `wiki/site/` 静态网页入口，用于从网页视角浏览话题层、自我层与框架层。

**新增结构**
- `wiki/topics/`
- `wiki/site/`

**说明**
- Markdown 仍是维护源，HTML 是可重新生成的浏览视图。
- 历史维护记录中的旧路径不主动重写。

## [2026-05-31] query | 补充 AI 协作草稿本方向

围绕“Codex 是否适合承担看板、文件编辑器、AI 协作草稿本”这一问题，更新 `gogo` 维护页。新增结论是：Codex 更适合作为本地知识库的协作 agent，而不是主编辑器或看板；如果要降低知识库的工作面摩擦，草稿本应更自然地成为 `gogo` 这类本地入口的轻量工作面，承接 `Drafts / Board / Agent` 三类功能，并最终写回本地 markdown 知识库。

**更新页面**
- `wiki/topics/context-memory-knowledge-system/gogo.md`

## [2026-05-31] 维护 | 增加用户专属草稿本目录

新增 `drafts/` 作为用户自己的草稿本目录。该目录不是 agent 维护层，agent 只能在用户明确相关时读取，不得写入、摄取、lint、整理、移动或删除其中内容。同步更新根 `AGENTS.md`、`schemas/AGENTS.md` 与 `skills/kb-ops/SKILL.md`，避免后续维护流程误碰草稿本。

**新增目录**
- `drafts/`

**新增规则**
- `drafts/AGENTS.md`

**更新页面**
- `AGENTS.md`
- `schemas/AGENTS.md`
- `skills/kb-ops/SKILL.md`

## [2026-05-31] 维护 | 草稿本目录改名为 notebook

按用户要求，将用户专属草稿本目录从 `drafts/` 改名为 `notebook/`。只读边界保持不变：agent 只能在用户明确相关时读取，不得写入、摄取、lint、整理、移动或删除其中内容。同步更新根规则、schema 和 `kb-ops` skill 中的路径引用。

**重命名**
- `drafts/` -> `notebook/`

**更新页面**
- `AGENTS.md`
- `schemas/AGENTS.md`
- `skills/kb-ops/SKILL.md`
- `notebook/AGENTS.md`

## [2026-06-01] query | 郑元杰创业想法与 AI 基础设施取舍评估

围绕 `life-record/郑元杰-创业想法.md` 与 `life-record/陈子深- AI教育产品定义.md`，新增一页应用分析。分析区分郑元杰提出的可商品化垂直机会，与用户提出的长期 AI 基础设施 / 知识系统积累方向，并建议先用真实付费验证窄场景，再把 AI 框架作为内部交付系统沉淀。随后补充“无聊但能收钱”的判断：付费信号不等于 PMF，更不等于 founder-market fit；这类场景更适合作为短期市场训练和现金流实验，而不是自动成为长期主线。进一步补充“拒绝 promising 但无聊机会”的判断：正确的不是拒绝市场，而是拒绝把低兴趣、低资产沉淀的现金流机会误当成事业。最后补充现实选择结论：不建议加入陈子深 / 郑元杰项目作为共同创业主线，主时间应投入 agent infra 项目、履历证据包与求职市场验证。

**新增页面**
- `wiki/topics/ai-product-product-definition/郑元杰创业想法评估.md`

## [2026-06-01] query | 空窗期、RA 与 Agent Systems 求职主线取舍

围绕毕业后去处选择，更新 `Agent系统求职与项目路线图-2026-05.md`。新增判断：空窗期不是第一风险，profile-market fit 未完成才是第一风险；不建议为了填补空窗而进入低相关研究助理岗位或不感兴趣创业项目。更合理的做法是把这段时间组织成 `Agent Systems Engineer profile-market fit sprint`，用旗舰项目、eval、真实试点、case study、portfolio 和定向外联把空窗转化成可解释资产。随后补充“先投还是先做项目”的判断：不应大规模投递弱画像，也不应闭门等项目完成；应先做最小可投递画像，再用少量高定向投递和外联校准，同时继续补项目证据。

**更新页面**
- `wiki/topics/projects-roadmaps/Agent系统求职与项目路线图-2026-05.md`

## [2026-06-02] query | Agentic Canvas Workbench 产品定义

围绕“可写写画画做思维导图、coding agent 可实时观看并总结建议、并链接 file-based 知识库”的设想，新增一页产品定义。核心结论是：这个方向不应被定义成通用白板或聊天机器人，而应定义成“人类用空间思考、agent 用结构观看、知识库用文件沉淀”的协作工作面。第一版应优先验证结构化画板状态能否成为 agent-facing context surface，并打通画板摘要、节点链接、本地文件写回和用户确认。

**新增页面**
- `wiki/topics/projects-roadmaps/Agentic-canvas-workbench.md`

## [2026-06-03] query | AI 鞭子、Accountability 与 AI-native 团队

围绕“AI 何时成为助理，何时成为上级追加要求的鞭子”这一观察，新增一页应用分析。核心结论是：AI 是否解放人，不取决于模型能力本身，而取决于工作关系中判断权、责任、成本和验证标准是否被正确分配。页面进一步区分非 AI-native 团队中的“AI 许愿机式加码”，以及 AI-native 团队中“执行速度领先于判断速度”的隐性鞭子风险。

随后补充 accountability 主轴：AI-native 团队和非 AI-native 团队的本质区别不是工具使用频率，而是组织是否把目标定义权、价值判断权、路径选择权、停止权和结果解释权给到真正做事的人。

后续重排文章结构，按陌生读者的理解顺序改为：常见场景、AI 鞭子定义、accountability 定义、AI 理解、两条件叠加、团队差异、论文实验场景和判断清单。

随后将页面从 `agent-harness-runtime` 迁移到新话题 `human-ai-relationship`。该话题用于承接人和 AI 的关系、协作方式、组织权责、工作心智与 AI 介入后的人类处境观察，避免稀释 `Agent / Harness / Runtime` 的 agent harness 边界。

随后将文章开头改为第一人称论文实验场景，并补充从卡尔·罗杰斯人本主义视角看 accountability-first AI-native 团队的展望。

**新增页面**
- `wiki/topics/human-ai-relationship/AI鞭子-accountability与AI-native团队.md`

## [2026-06-05] ingest | 补齐《穷查理宝典》投资与商业判断模型

围绕《穷查理宝典》中投资不是价格预测、而是企业所有权和商业判断这一主线，新增一组具体模型页。重点把安全边际、机会成本、少数重注、耐心等待、好生意、护城河、定价权、保险浮存金等从大主题拆成可检索、可互链、可复用的独立页面。

**新增页面**
- `wiki/topics/learning-judgment-mental-models/股票是企业所有权.md`
- `wiki/topics/learning-judgment-mental-models/企业分析而非市场预测.md`
- `wiki/topics/learning-judgment-mental-models/好生意.md`
- `wiki/topics/learning-judgment-mental-models/公平价格买伟大企业.md`
- `wiki/topics/learning-judgment-mental-models/内在价值.md`
- `wiki/topics/learning-judgment-mental-models/安全边际.md`
- `wiki/topics/learning-judgment-mental-models/机会成本.md`
- `wiki/topics/learning-judgment-mental-models/少数重注.md`
- `wiki/topics/learning-judgment-mental-models/耐心等待与果断行动.md`
- `wiki/topics/learning-judgment-mental-models/持久竞争优势.md`
- `wiki/topics/learning-judgment-mental-models/护城河.md`
- `wiki/topics/learning-judgment-mental-models/定价权.md`
- `wiki/topics/learning-judgment-mental-models/保险浮存金.md`

**更新页面**
- `wiki/topics/learning-judgment-mental-models/穷查理宝典.md`
- `wiki/topics/learning-judgment-mental-models/穷查理宝典具体模型索引.md`
- `wiki/topics/learning-judgment-mental-models/纳瓦尔与穷查理主题地图.md`

## [2026-06-28] ingest | 摄取 AI 时代人才筛选与学习潜力判断

保存 Superlinear Academy 社区文章《正确的学习方法比大家想象中稀缺很多，那我们如何筛选人才？》到 `raw/external/`，并将其压缩为职业/人才筛选主题页。核心增量是把早期候选人判断从“当前存量”扩展到“遇到正确方法后的学习斜率”，包括从不会到会的真实经历、现场机制理解、follow-up 小任务和高质量学习场。

**新增页面**
- `wiki/topics/career-positioning-job-search/AI时代人才筛选与学习潜力判断.md`

**更新页面**
- `wiki/topics/career-positioning-job-search/index.md`
- `wiki/frameworks/职业信号与叙事框架.md`

## [2026-06-28] ingest | 摄取 AI 时代面试与作品化简历信号

保存 Superlinear Academy 社区文章《别用昨天的方法准备今天的面试：AI 时代最好的简历，是做出来的》到 `raw/external/`，并新增职业/求职主题页。核心增量是：AI 让口头叙事、简历包装和项目描述更容易生成，因而候选人更需要用 GitHub、真实项目、`CLAUDE.md`、`AGENTS.md`、skills、公开复盘等可检查材料证明自己真的具备 AI 时代的动手能力。

**新增页面**
- `wiki/topics/career-positioning-job-search/AI时代最好的简历是做出来的.md`

**更新页面**
- `wiki/topics/career-positioning-job-search/index.md`
- `wiki/frameworks/职业信号与叙事框架.md`

## [2026-06-05] 维护 | 新增具体话题深度摄取 skill

将《纳瓦尔宝典》和《穷查理宝典》深度 ingest 的方法沉淀为仓库内 skill。新 skill 面向“给定材料，抽取每个具体话题，逐项建立 wiki 页面，并构造页面和知识库之间关联”的工作流，要求先做候选话题清单，再建页面、更新索引和主题地图，最后重新生成 site 并验证搜索索引。

**新增 skill**
- `skills/topic-deep-ingest/SKILL.md`
- `skills/topic-deep-ingest/agents/openai.yaml`
- `skills/topic-deep-ingest/scripts/topic_coverage_audit.py`

**更新页面**
- `skills/README.md`
- `skills/kb-ops/SKILL.md`

## [2026-06-05] ingest | 补齐跨书数学、经济学与受托判断主题

补齐主题地图中剩余的跨书缺口：数学、概率与期望值；学院经济学的优点与缺陷；受托资金与机构投资。随后将主题地图的“待补齐主题页”改为覆盖状态，后续维护重点转为补充案例与复用记录。

**新增页面**
- `wiki/topics/learning-judgment-mental-models/数学概率与期望值.md`
- `wiki/topics/learning-judgment-mental-models/学院经济学的优点与缺陷.md`
- `wiki/topics/learning-judgment-mental-models/受托资金与机构投资.md`

**更新页面**
- `wiki/topics/learning-judgment-mental-models/穷查理宝典.md`
- `wiki/topics/learning-judgment-mental-models/穷查理宝典具体模型索引.md`
- `wiki/topics/learning-judgment-mental-models/纳瓦尔与穷查理主题地图.md`
- `wiki/topics/learning-judgment-mental-models/index.md`

## [2026-06-05] ingest | 补齐《穷查理宝典》学习与人格伦理模型

继续把《穷查理宝典》从大主题拆成具体话题页。新增学习与思考模型，包括基础普世智慧、多学科大思想、数字敏感性、主动摧毁最爱的想法、避免意识形态和持续阅读；新增人格伦理模型，包括声誉、可信任、配得的成功、避免嫉妒与怨恨、可靠和独立思考。

**新增页面**
- `wiki/topics/learning-judgment-mental-models/基础普世智慧.md`
- `wiki/topics/learning-judgment-mental-models/多学科大思想.md`
- `wiki/topics/learning-judgment-mental-models/数字敏感性.md`
- `wiki/topics/learning-judgment-mental-models/主动摧毁最爱的想法.md`
- `wiki/topics/learning-judgment-mental-models/避免意识形态.md`
- `wiki/topics/learning-judgment-mental-models/持续阅读.md`
- `wiki/topics/learning-judgment-mental-models/声誉.md`
- `wiki/topics/learning-judgment-mental-models/可信任.md`
- `wiki/topics/learning-judgment-mental-models/配得的成功.md`
- `wiki/topics/learning-judgment-mental-models/避免嫉妒与怨恨.md`
- `wiki/topics/learning-judgment-mental-models/可靠.md`
- `wiki/topics/learning-judgment-mental-models/独立思考.md`

**更新页面**
- `wiki/topics/learning-judgment-mental-models/穷查理宝典.md`
- `wiki/topics/learning-judgment-mental-models/穷查理宝典具体模型索引.md`
- `wiki/topics/learning-judgment-mental-models/纳瓦尔与穷查理主题地图.md`
## [2026-06-30] query | 整理陈子深 AI 教育项目 notebook idea

从 `notebook/陈子深- AI教育产品想法.md` 和 `notebook/一道题.md` 中整理陈子深 AI 教育项目相关草稿，只保留 notebook 层来源，不混入 `life-record/` 访谈层。新增主题页将方向收束为认知原因级诊断、解题 copilot、`一道题` MVP、未解问题和个人参与边界。

**新增页面**
- `wiki/topics/ai-product-product-definition/陈子深AI教育项目notebook-idea整理.md`

**更新页面**
- `wiki/topics/ai-product-product-definition/index.md`

## [2026-06-30] ingest | 摄取 Codex 与 AI 产品工作形态访谈

保存微信文章《砍掉PM、全员做Builder？OpenAI Codex主管：人人皆可做产品就是“毒鸡汤”，别总觉得别的岗位只是在摸鱼！》到 `raw/external/`，并整理为 AI 产品定义主题页。核心增量是：当 AI 让实现和原型成本下降后，产品工作的稀缺点转向品味、策展、系统嵌入、媒介选择和模型能力时机判断，而不是简单取消 PM / 设计 / 工程角色。

**新增原始材料**
- `raw/external/wechat-openai-codex-product-taste-csdn.html`
- `raw/external/wechat-openai-codex-product-taste-csdn.txt`

**新增页面**
- `wiki/topics/ai-product-product-definition/Codex与AI产品工作的实现廉价化.md`

**更新页面**
- `wiki/topics/ai-product-product-definition/index.md`

## [2026-06-30] ingest | 摄取 AI User 到 AI Builder 五条差距文章束

保存 Superlinear Academy 两篇关于 AI User / AI Builder 差距的 Markdown clipping，并整理为 AI 产品定义主题页。核心增量是：AI 使用能力差距不主要来自 prompt 技巧，而来自 context、验收标准、质量诊断、Agentic Loop、经验沉淀和个人/团队基础设施。

**新增原始材料**
- `raw/external/superlinear-ai-user-builder-five-gaps/`

**新增页面**
- `wiki/topics/ai-product-product-definition/AI-User到AI-Builder的五个能力差距.md`

**更新页面**
- `wiki/topics/ai-product-product-definition/index.md`

## [2026-07-01] ingest | 摄取后台守护进程式 Agent 形态材料

保存 Superlinear Academy clipping《AI Agent 的下一个形态：从聊天窗口到后台守护进程》到 `raw/external/`，并新增主题页把材料整理为 `chat window -> agentic tool -> background agent -> consumer ambient agent` 的产品形态迁移。核心增量是：当前 personal agent 实验应从“低入口摩擦”进一步压缩为“持续存在的 personal context daemon / 持续情境理解层”，重点验证 agent 是否能在用户不显式 call 的情况下持续同步事件流、更新 context state，并在相关场景主动 resurfacing。

**新增原始材料**
- `raw/external/AI Agent的下一个形态-从聊天窗口到后台守护进程.md`

**新增页面**
- `wiki/topics/agent-harness-runtime/后台守护进程式Agent与持续情境理解.md`

## [2026-07-01] query | Superlinear 视角下的个人 AI 工作流迁移

根据用户关于“现在大部分还是拿 AI 作为问答工具”的提问，综合 Superlinear Academy 课程索引、AI User / AI Builder 差距、AI 产品六层、AI Architect、Context Intelligence、Proactive Intelligence、Agentic Runtime / Evaluation-First 与 GenAI 任务委托边界，新增一页应用分析。核心增量是：个人 AI 工作流优化不应停留在 prompt 技巧，而应从 `context.md`、`brief.md`、`result.md`、`review.md` 这样的文件工作面开始，把高频任务迁移成有上下文、验收、执行循环和 write-back 的系统化委托。

**新增页面**
- `wiki/topics/ai-product-product-definition/个人AI工作流从问答到系统化委托.md`

## [2026-07-01] query | AI 泡沫破裂后的死亡名单与留存层

根据用户把 2000 年互联网泡沫迁移到当前 AI 周期的追问，综合 AI 产业分层、付钱地图、AI Infra 抗模型吞噬、AI 时代投资与生存法则、衰退期技术判断和 AI 产品 runtime 分层，新增主题页。核心增量是：会破的是把 AI 当估值叙事、融资故事和薄包装能力的公司；会留下的是算力、模型、inference、eval、security、context / memory governance、agent runtime、workflow harness 和高 ROI 垂直应用这些真实系统层。

**新增页面**
- `wiki/topics/ai-industry-investment/AI泡沫破裂后的死亡名单与留存层.md`

**更新页面**
- `wiki/topics/ai-industry-investment/index.md`

## [2026-07-01] query | 修正 AI 泡沫判断中的前沿公司图谱

根据用户指出“2026 年前沿公司已经很少是 prompt wrapper / 普通 chatbot builder / 简单 RAG wrapper”的反馈，追加外部调研并修正页面。新增判断是：当前主战场已经迁移到 coding agent、企业 work AI、customer support agent、vertical workflow、consumer/prosumer AI 和推理/评测基础设施；真正的死亡风险不再是“是不是 wrapper”，而是复杂 agent / workflow 公司能否兑现可靠性、权限治理、可验证 ROI、服务交付毛利、默认工作面和分发控制。

**更新页面**
- `wiki/topics/ai-industry-investment/AI泡沫破裂后的死亡名单与留存层.md`

## [2026-07-01] query | AI 泡沫破裂后留下来的用户需求

根据用户追问“AI 泡沫破裂后留下来的用户需求有哪些”，在既有 AI 泡沫页面中补充用户需求层。核心增量是：泡沫后留下来的不是“我要 AI 产品”，而是把任务做完、降低专业服务成本、安全执行、携带上下文、操作软件和数据、更快创造数字作品、信息过载中的判断辅助、陪伴表达与身份建构、降低 AI 使用成本和风险、重新组织人类工作这十类长期需求。

**更新页面**
- `wiki/topics/ai-industry-investment/AI泡沫破裂后的死亡名单与留存层.md`

## [2026-07-01] query | 用 2000 年互联网泡沫事实压测 AI 用户需求判断

根据用户要求用 2000 年互联网泡沫事实反向 pressure test 既有 claim，在 AI 泡沫页面中新增压测小节。核心修正是：需求存在只是必要条件，不是公司、产品形态或估值穿越周期的充分条件；`Pets.com`、`Webvan`、门户、个人主页和光纤建设等案例都说明，真实需求可能留下，但错误时机、错误资本结构、错误履约模型和缺少分发入口会让公司死亡。压测后将十类 AI 用户需求重分为终端强需求、基础设施型需求、消费与表达型需求、组织转型型需求。

**更新页面**
- `wiki/topics/ai-industry-investment/AI泡沫破裂后的死亡名单与留存层.md`

## [2026-07-01] query | 深哥 AI 教育项目的泡沫穿越标准

根据用户追问“这些对深哥和我的创业项目有什么启发”，把 AI 泡沫穿越标准迁移到陈子深 AI 教育项目。核心判断是：不要把项目定义成泛泛 AI 教育、AI tutor、拍照搜题、题库或学生聊天 app；更可能穿越泡沫的主线是把好老师对学生“为什么不会”的隐性判断产品化，并让诊断改变下一步教学动作。新增取舍包括优先诊断闭环、老师校准面、可评测样本和真实分发路径；如果 `3-5` 个学生与 `2-3` 个老师的小样本不能证明 L5-L7 诊断价值，就应停在 workload / demo / 学习资产层，而不是升级为长期共同创业主线。

**更新页面**
- `wiki/topics/ai-product-product-definition/陈子深AI教育项目notebook-idea整理.md`

## [2026-07-01] query | 标注陈子深 AI 教育方向已停止推进

根据用户纠正“我们已经不再做 AI 教育项目了”，更新陈子深 AI 教育项目整理页的当前状态。新增页面顶部状态说明：该方向不再作为当前创业项目推进，本文仅保留为历史想法整理、产品定义复盘和 AI workflow / eval / diagnostic harness 案例。同步把此前“泡沫穿越标准”小节改为历史复盘语气，避免后续继续把该方向当成正在推进的创业项目。

**更新页面**
- `wiki/topics/ai-product-product-definition/陈子深AI教育项目notebook-idea整理.md`
