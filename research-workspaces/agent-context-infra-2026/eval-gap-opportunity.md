# Agent Context Infra 评测、缺口与机会草稿（截至 2026-05-24）

## 0. 结论先行

截至 2026-05-24，agent memory / context infra 的评测主线正在从“静态 recall”快速转向“经验是否能改变 agent 的后续行为”。这不是一个小的 benchmark 迭代，而是评价对象的变化：过去测的是系统能否从长上下文或外部存储中找到事实；现在开始测 agent 是否能在多会话、多工具、多用户、状态变化和企业流程中，把历史经验组织成可靠的执行能力。

这个变化对 builder 的含义很直接：普通 RAG wrapper 的空间正在被压缩。真正有机会的层，不是再做一个“存进去、搜出来”的记忆接口，而是围绕 `write policy / correction / isolation / replay / observability / cost-latency` 做成可评测、可回放、可迭代的 context runtime。

本地知识库的判断也指向同一处：Harness 架构框架强调 `latent space` 与 `deterministic space` 的边界，AI 系统产品框架强调 runtime 与 contract 才是工程黑洞，研究判断框架强调评测要服务下一步判断，Agent Systems north star 则把 `context / harness / eval / reliability / deployment` 定义成目标履历的核心证据包。因此，agent context infra 的机会不在“更聪明的摘要”，而在“让 agent 的长期上下文生命周期可控、可查、可证伪”。

## 1. 参考范围

### 外部一手来源

| 来源 | 时间截面 | 本文使用方式 |
|---|---:|---|
| [Microsoft: Introducing STATE-Bench](https://opensource.microsoft.com/blog/2026/05/19/introducing-state-bench-a-benchmark-for-ai-agent-memory/) | 2026-05-19 | 作为 enterprise workflow / stateful task memory eval 的代表 |
| [MemoryAgentBench, ICLR 2026, OpenReview PDF](https://openreview.net/pdf?id=DT7JyQC3MR) | ICLR 2026 | 作为 incremental multi-turn memory competencies 的代表 |
| [GroupMemBench](https://arxiv.org/abs/2605.14498) | 2026-05-14, v2 2026-05-16 | 作为 multi-party group memory 的代表 |
| [StructMemEval](https://arxiv.org/abs/2602.11243) | 2026-02-11 | 作为 memory structure / organized memory 的代表 |
| [LongMemEval-V2](https://arxiv.org/abs/2605.12493) | 2026-05-12 | 作为 environment-specific experience memory 的代表 |
| [MemGym](https://arxiv.org/abs/2605.20833) | 2026-05-20 | 作为 long-horizon agentic memory environment 的代表 |
| [LoCoMo](https://arxiv.org/abs/2402.17753) | 2024-02-27 | 作为早期 long conversational memory benchmark 的代表 |
| [LongMemEval](https://openreview.net/pdf?id=wIonk5yTDq) | ICLR 2025/2026 相关 | 作为 multi-session personalized assistant memory 的代表 |

### 本地判断来源

| 本地页 | 本文调用的判断 |
|---|---|
| [Harness 架构判断框架](../../wiki/frameworks/Harness架构判断框架.md) | harness 是对模型弱点的补偿；关键是把智能判断和确定性执行放在正确边界 |
| [AI 系统产品判断框架](../../wiki/frameworks/AI系统产品判断框架.md) | AI 产品难点常在 runtime、state、tool calling、验收契约和人工接管 |
| [研究判断框架](../../wiki/frameworks/研究判断框架.md) | 研究系统评测不应只问“答得像不像百科”，而应问“是否帮助判断下一步” |
| [Anthropic 与 OpenAI 的 Agent Systems 履历 North Star](../../wiki/bridges/Anthropic与OpenAI的Agent%20Systems履历North%20Star.md) | 顶尖 agent systems 画像是能 end-to-end 拥有 context、execution、evaluation、deployment、reliability 的 builder |

## 2. Benchmark 演进：从 recall 到经验驱动的 agent runtime

| 阶段 | 典型问题 | 代表 benchmark | 测到什么 | 没测到什么 |
|---|---|---|---|---|
| 静态长上下文 QA | “事实藏在很长文本里，模型能不能找出来？” | LongBench、needle-in-a-haystack 一类 | 长上下文读取、局部检索、基本多跳 | 记忆如何写入、更新、删除；agent 是否因此做得更好 |
| 长对话 / 多会话 recall | “跨很多 session 的用户事实能不能被召回？” | LoCoMo、LongMemEval | single-hop、多跳、时间、知识更新、abstention | 多用户边界、企业工具状态、真实任务后果、成本和可靠性 |
| incremental multi-turn memory | “agent 能不能逐步吸收信息，并在后续任务中使用？” | MemoryAgentBench | accurate retrieval、test-time learning、long-range understanding、selective forgetting | 企业级 state mutation、多人协作语境、runtime observability |
| stateful task / enterprise workflow | “记忆是否让 agent 在真实流程中更可靠？” | STATE-Bench | procedure following、stateful tools、pass^5、成本、用户体验 | memory write policy 本身是否正确；跨组织、多角色隔离 |
| multi-party group memory | “在多人频道里，agent 能不能知道谁相信什么、对谁该怎么说？” | GroupMemBench | group dynamics、speaker-grounded beliefs、audience adaptation | 工具执行、权限边界、真实企业数据治理 |
| memory structure | “agent 能不能把历史组织成 ledger、tree、todo、state machine？” | StructMemEval | 结构化长期记忆是否真的被建立和维护 | 结构如何审计、纠错、迁移到生产工作流 |
| environment experience memory | “agent 能不能像老同事一样记住环境 affordance、workflow、坑和状态动态？” | LongMemEval-V2、MemGym | web / coding / research / computer use 中的经验压缩与复用 | 大规模线上回放、成本、延迟、真实用户反馈闭环 |

这条演进线说明，memory eval 的中心正在从 `read` 迁到完整生命周期：`write -> organize -> retrieve -> apply -> update / forget -> explain / replay`。如果只测 retrieval，就会天然高估简单 RAG 的价值；如果测 stateful workflow、multi-party group memory 和 structure，很多“看起来高级”的 memory system 会暴露出写入策略、组织策略和纠错策略的缺口。

## 3. 重点 benchmark 速览

### 3.1 STATE-Bench

[STATE-Bench](https://opensource.microsoft.com/blog/2026/05/19/introducing-state-bench-a-benchmark-for-ai-agent-memory/) 的关键推进，是把 memory 从“是否能找到旧事实”放进 enterprise workflow 里测。它覆盖 customer support、travel、shopping 三个域，共 450 个任务。每个任务有预填充数据库、工具、用户模拟器和 deterministic state assertions。

它的任务有三类特征：

| 特征 | 含义 | 为什么重要 |
|---|---|---|
| Procedural | agent 要按领域流程执行，例如查 booking、校验 eligibility、检查 policy、计算 fee、确认再执行 | 企业 agent 常失败在漏步骤，不是单纯忘事实 |
| Stateful | agent 的工具调用会改变环境状态，例如退款、订单、账户、预订 | 错误不只是回答不好，而是造成真实系统清理成本 |
| User experience | 除了结果，还评估交互质量、用户负担、consent 等 | memory 不能只提高任务完成率，也要降低用户协作成本 |

STATE-Bench 的指标也明显比传统 QA 更接近生产：

| 指标 | 评测含义 |
|---|---|
| task completion rate | 最终状态或过程是否正确 |
| pass^5 | 同一任务跑 5 次是否全部成功，捕捉可靠性而非偶然成功 |
| efficiency | turn、无用 tool call、input / output / retrieval token 成本 |
| user experience score | 用户是否省力、是否被充分告知、是否在关键动作前确认 |

它最重要的信号是：即使用强模型和完整工具，无记忆 baseline 也很难稳定完成一半以上任务；travel 域 pass^5 只有约 30%。这说明 production memory 的目标不应只是“记得更多”，而应是“减少重复失败模式，提高流程一致性”。

### 3.2 MemoryAgentBench

[MemoryAgentBench](https://openreview.net/pdf?id=DT7JyQC3MR) 把 memory agent 的能力拆成四个核心项：

| 能力 | 含义 | 对 context infra 的启发 |
|---|---|---|
| Accurate Retrieval | 从历史中抽取正确片段 | 这是底线，不是终点 |
| Test-Time Learning | 从部署期交互中学会新规则或行为 | memory 要承载经验，而不是只承载事实 |
| Long-Range Understanding | 跨超长历史整合全局信息 | 需要压缩、索引和抽象层，而不是无限塞上下文 |
| Selective Forgetting | 面对矛盾信息时修订、覆盖或删除旧记忆 | stale / contradiction handling 是核心能力，不是清理脚本 |

它的贡献是把很多静态 long-context 数据转成增量多轮输入，模拟 agent 逐步积累信息的过程。它比 LoCoMo / LongMemEval 更接近“agent 运行时逐渐学到东西”的问题，但仍更偏 memory 能力隔离测试，而不是完整企业任务后果。因此它适合做 memory mechanism benchmark，不足以单独回答“我的 agent product 是否生产可用”。

### 3.3 GroupMemBench

[GroupMemBench](https://arxiv.org/abs/2605.14498) 的价值在于指出：真实部署不是单用户和 agent 的二元关系，而是 group、channel、team 中多人和 agent 共同说话。它测三类过去被忽略的能力：

| 能力 | 失败模式 |
|---|---|
| group dynamics | agent 把群聊当作很多一对一对话拼接，丢掉 reply structure 和关系结构 |
| speaker-grounded belief tracking | agent 不知道“谁知道什么、谁相信什么、谁更新了什么” |
| audience-adapted language | agent 不能根据提问者、角色和语境调整术语与表达 |

它的问题类型包括 multi-hop reasoning、knowledge update、term ambiguity、user-implicit reasoning、temporal reasoning、abstention。结果很尖锐：最强系统平均准确率只有 46.0%，knowledge update 只有 27.1%，term ambiguity 只有 37.7%，简单 BM25 还可以匹配或超过许多 agent memory system。

这个结果对产品机会很重要：很多 memory ingestion 会把群聊的结构、说话者、词汇差异磨平。只要 memory store 把信息扁平化成匿名 chunks，多用户 agent 就会天然污染。

### 3.4 StructMemEval

[StructMemEval](https://arxiv.org/abs/2602.11243) 的核心问题是：如果任务需要 tree、ledger、todo list、state tracking 这样的结构，memory agent 能不能自己把长期记忆组织成正确形状。

它的设置刻意避免把失败归因混到 coding、planning 或工具能力里，而是选择“只要组织对就简单，不组织就很难”的任务。论文报告了 73 个 scenario、544 个 evaluation questions，并提供 optional memory organization hint 来诊断错误来源。

重要发现是：简单 retrieval 在小规模任务上可以工作，但任务超过 retrieval budget 或需要状态转移时迅速失效；memory agents 如果被提示如何组织 memory，会显著更可靠；但没有提示时，现代 LLM 不一定会主动识别正确结构。这说明 context infra 不能只提供 storage / search，还需要提供 structure policy 或 structure discovery harness。

### 3.5 LongMemEval-V2

[LongMemEval-V2](https://arxiv.org/abs/2605.12493) 把长期记忆定义成“让 agent 成为 customized environment 里的 experienced colleague”。它不再只问用户历史，而是问 web agent 是否记得界面 affordance、state dynamics、workflow 和 recurring failure modes。

它包含 451 个 manually curated questions，覆盖五类能力：

| 能力 | 例子 |
|---|---|
| static state recall | 某个环境中的固定对象、字段、页面结构 |
| dynamic state tracking | 状态随操作或时间如何变化 |
| workflow knowledge | 完成任务的常见步骤和依赖 |
| environment gotchas | 历史中踩过的坑、非显然限制 |
| premise awareness | 问题前提是否在环境历史中成立 |

它的 history trajectories 可到 500 trajectories / 115M tokens。评测采用 context gathering：memory system 消费历史轨迹，返回 compact evidence，再用于问答。AgentRunbook-C 用文件存轨迹，并让 coding agent 在增强 sandbox 中搜证，达到 72.5% 平均准确率，高于最强 RAG baseline 的 48.5% 和 off-the-shelf coding agent baseline 的 69.3%，但代价是高延迟。

这个 benchmark 暴露的机会是：agent context 不只是 chat memory，而是“环境经验库”。它更接近 coding agent、browser agent、internal tools agent 的真实需求。

### 3.6 MemGym

[MemGym](https://arxiv.org/abs/2605.20833) 进一步把 memory 放进 long-horizon agentic environments，覆盖四类 agentic regimes：

| Regime | Track |
|---|---|
| tool-use dialogue | tau2-bench |
| deep research | MEMGYM-DR |
| coding | SWE-Gym、MEMGYM-CODEQA |
| computer use | WebArena-Infinity |

它的关键主张是报告 memory-isolated scores，尽量把 memory 表现和 reasoning、retrieval、tool-use ability 解耦。为让 coding 环境评测成本可承受，它还训练了轻量 reward model MemRM，用来快速评分 compression quality，替代完整 Docker rollout。

MemGym 的方向对 builder 很实用：生产里的 memory 评测必须知道失败到底来自 memory、reasoning、tool、环境还是 scorer。没有隔离，eval 会变成“整体成功率变差了，但不知道该修哪层”。

## 4. LoCoMo / LongMemEval 的价值与局限

LoCoMo 和 LongMemEval 是这一轮 memory benchmark 的重要起点。它们把问题从短对话推进到多 session、长历史、时间和知识更新。

[LoCoMo](https://arxiv.org/abs/2402.17753) 构造了平均 300 turns、9K tokens、最多 35 sessions 的长对话，包含 QA、event summarization、multi-modal dialogue generation。[LongMemEval](https://openreview.net/pdf?id=wIonk5yTDq) 则提供 500 个高质量问题，覆盖 information extraction、multi-session reasoning、temporal reasoning、knowledge updates、abstention，并提供约 115K tokens 与约 1.5M tokens 两个设置。

但到 2026-05-24，它们的局限已经很清楚：

| 局限 | 具体表现 | 为什么影响机会判断 |
|---|---|---|
| 仍偏 recall / QA | 主要问历史里有没有事实、是否能跨 session 找到证据 | 容易让普通 RAG 看起来足够好 |
| 用户模型偏单人 | 多数是 user-agent dyad，而非多人频道和组织环境 | 无法测 speaker isolation、权限和 group memory |
| 缺少真实状态改变 | 答错通常是 QA 错，不会改变数据库或业务状态 | 无法测 enterprise agent 的真实失败成本 |
| 对 memory write policy 覆盖不足 | 更关注给定历史后的读取，不充分测何时写、写什么、如何合并 | 生产中最危险的错误常发生在写入和更新 |
| 对 stale / contradiction 的诊断不够细 | 有知识更新题，但少有完整 correction provenance 和回滚链路 | 很难评估长期污染、纠错和审计 |
| 可被长上下文或 top-k 暴力缓解 | 上下文窗口变大后，dump more context 会在部分题上竞争力很强 | benchmark 区分不了“好 memory”与“上下文预算够大” |
| 缺少 observability / replay | 多数只看最终答案，不看 retrieval trajectory、memory mutation 和执行轨迹 | builder 无法据此修系统 |

因此，LoCoMo / LongMemEval 仍适合作为回归集和历史对照，但不能作为 2026 年 agent context infra 的唯一 north star。新的评测需要把 memory 写入、结构、状态、多人边界、执行后果和成本都纳入。

## 5. 缺口地图

| 缺口 | 当前 benchmark 覆盖 | 生产失败模式 | 机会含义 |
|---|---|---|---|
| memory write policy | 弱到中。MemoryAgentBench 有增量输入，StructMemEval 间接暴露组织问题，但大多不直接测写入决策 | agent 把临时事实写成长期偏好；把错误工具结果写成经验；把一次性异常泛化成规则 | 需要可配置、可评测的 write gate、memory type、TTL、confidence、human correction |
| stale / contradiction handling | 中。MemoryAgentBench 有 selective forgetting；LongMemEval 有 knowledge update；但 production 纠错链路不足 | 旧政策、旧偏好、旧环境状态长期污染后续任务 | 需要 contradiction detector、supersession graph、staleness score、delete / archive / override 机制 |
| provenance / correction | 弱。多数 benchmark 只看答案，不强制解释 memory 从何而来、何时被改 | 用户纠正后，系统不知道哪个记忆被修、哪些下游结论受影响 | 需要 memory provenance、correction log、反向索引、影响范围分析 |
| multi-agent / multi-user isolation | GroupMemBench 开始覆盖，但工具权限、组织租户和 agent namespace 仍不足 | A 用户偏好泄露给 B；team channel 的共识被写进个人记忆；agent 之间互相污染策略 | 需要 user / group / agent / workspace 四层 namespace 和可测隔离 |
| cost / latency | STATE-Bench、LongMemEval-V2、MemGym 开始显式关注，但还不够标准化 | memory system 准确但太慢；context gathering 成本高到不可上线 | 需要 accuracy-latency-cost Pareto eval，缓存、分层摘要、预算感知 retrieval |
| eval realism | STATE-Bench 和 MemGym 推进明显，但多数 benchmark 仍是 synthetic 或离线 | benchmark 过了，真实企业流程仍失败 | 需要真实工具 sandbox、可变用户模拟器、state assertions、human handoff case |
| observability / replay | 普遍弱。MemGym 有解耦意识，STATE-Bench 有 orchestrator，但 builder 可调试面仍不足 | 只知道 pass rate 降了，不知道错在写入、检索、压缩、工具还是 judge | 需要 memory trace、episode replay、diff、scorer breakdown、failure taxonomy |

缺口地图压缩成一句话：2026 年以后，memory infra 的难点不在“有没有一个向量库”，而在“长期上下文进入系统后，谁决定它变成什么状态、对谁可见、何时失效、如何纠正、如何证明它真的改善任务表现”。

## 6. 机会地图：面向 builder 的 4 个方向

### 机会 A：Agent Memory Eval Harness

| 字段 | 内容 |
|---|---|
| Target user | 正在做 agent 产品或平台的 builder，尤其是 coding agent、browser agent、customer support agent、internal workflow agent 团队 |
| Painful failure mode | 加了 memory 后 demo 看起来更聪明，但线上任务完成率、pass^k、成本和用户体验没有稳定改善；失败后不知道该修 prompt、retrieval、memory 写入还是工具流程 |
| Minimum viable artifact | 一个 `eval/` harness：支持 episode replay、stateful tool sandbox、memory on/off A/B、pass@1 / pass^5、cost / latency、memory trace、failure class 标注 |
| First eval | 选 30-50 个真实或半真实 workflow episode，跑 no-memory、RAG-memory、structured-memory 三组，对比 task success、pass^5、tool call waste、retrieval tokens、UX judge |
| 为什么不是普通 RAG wrapper | 它的主语不是 retrieval，而是“memory 是否改善 agent runtime 行为”。RAG wrapper 只负责取证；eval harness 负责定义成功、复现失败、隔离变量和驱动系统迭代 |

这个方向最贴近本地 Agent Systems north star。它把 `eval / regression / replay` 从简历缺口变成产品能力，也符合 Harness 架构框架里“独立 evaluator 与 deterministic scorer”应外置成可靠控制面的判断。

### 机会 B：Memory Write Policy 与 Correction Layer

| 字段 | 内容 |
|---|---|
| Target user | 已经有长期 memory 的 agent app、个人 assistant、团队 assistant、knowledge worker agent |
| Painful failure mode | agent 乱写长期记忆，误把临时上下文、错误结论、旧偏好、用户玩笑写成稳定事实；用户纠正后系统表面道歉，但旧记忆仍在后续污染 |
| Minimum viable artifact | 一个 memory mutation layer：每条写入带 type、scope、confidence、source episode、expiry、supersedes、correction status；提供 create/update/archive/override policy 和人类确认阈值 |
| First eval | 构造 100 条 episode stream，包含偏好变化、政策变化、用户纠正、互相矛盾事实。测 stale recall rate、wrong persistence rate、correction success、unwanted write rate |
| 为什么不是普通 RAG wrapper | 普通 RAG 假设 corpus 已经存在且相对正确。这里解决的是 corpus 如何从 agent 运行中生成、变更、失效和被纠正，是 memory 写侧和治理侧问题 |

这个方向对应 MemoryAgentBench 的 selective forgetting、LongMemEval 的 knowledge update、GroupMemBench 的 speaker-grounded update，也补上多数 benchmark 不充分测的生产风险。

### 机会 C：Group Memory Namespace 与 Isolation Harness

| 字段 | 内容 |
|---|---|
| Target user | Slack / Discord / Teams / Linear / Notion / GitHub 等多人协作环境中的 agent builder |
| Painful failure mode | agent 在多人频道中混淆“谁说的、谁知道、谁允许、谁应该看到”；把团队讨论写入个人记忆，或把个人偏好错误广播到群体上下文 |
| Minimum viable artifact | 一个 group memory runtime：`user / group / workspace / agent` namespace，speaker-grounded facts，audience policy，channel-level memory，per-query visibility resolver，leakage test suite |
| First eval | 复刻 GroupMemBench 的六类 query，再加权限泄露题和纠错题。指标包括 speaker attribution accuracy、audience adaptation、forbidden context leakage、abstention correctness |
| 为什么不是普通 RAG wrapper | RAG wrapper 通常只问“哪些 chunk 相关”。多人 memory 要先问“这个 asker 能不能看、这个事实属于谁、这句话对哪个 audience 成立、是否需要 abstain” |

这个方向和本地研究判断框架中的 group memory、公共知识治理非常接近。它的壁垒不是 embedding，而是 context boundary、permission 和 provenance。

### 机会 D：Environment Experience Runbook

| 字段 | 内容 |
|---|---|
| Target user | browser / coding / internal tools agent 的 builder，尤其是需要 agent 长期操作同一复杂环境的团队 |
| Painful failure mode | agent 每次都像新人一样重新探索 UI、API、仓库、测试环境和隐藏坑；同一个 workflow 反复失败，历史成功路径不能迁移到新任务 |
| Minimum viable artifact | 一个 runbook memory system：把 episode trace 自动压成 environment affordance、workflow steps、gotchas、state invariants、tool recipes，并能按任务检索和回放证据 |
| First eval | 选一个真实 repo 或 web app，录制 50-100 条任务轨迹。测 agent 在新任务上的 first-try success、重复错误率、探索步数、runbook retrieval precision、延迟 |
| 为什么不是普通 RAG wrapper | 它不是检索文档，而是从执行轨迹中提取可复用经验。核心对象是 workflow knowledge、state dynamics 和 recurring failure modes，接近 LongMemEval-V2 的 experienced colleague 定义 |

这个方向天然连接 Harness 架构中的 context budget 和 deterministic execution。runbook 既是 memory，也是 harness 的一部分：它告诉 agent 如何更少试错、更稳定地走流程。

### 机会 E：Memory Observability / Replay Debugger

| 字段 | 内容 |
|---|---|
| Target user | 已经上线 agent 或准备上线的 infra / platform builder、AI product engineer、forward deployed engineer |
| Painful failure mode | 用户报告“agent 记错了”或“重复犯错”，团队只能看最终对话，无法知道是哪次写入、哪次 retrieval、哪次压缩或哪条旧记忆导致问题 |
| Minimum viable artifact | 一个 trace viewer：展示 episode timeline、memory writes、retrieval set、context assembly、tool calls、state diff、judge result；支持 replay with patch 和 memory diff |
| First eval | 对 20 个已知失败 episode 做 root-cause annotation，测 debugger 是否能减少定位时间、提高修复准确率，并把修复后 episode 纳入 regression |
| 为什么不是普通 RAG wrapper | RAG wrapper 的可观察性通常停在 retrieval hits。这里观察的是 memory 生命周期和 agent episode 的因果链，目标是可靠性工程，不是检索接口 |

这个方向对应本地 north star 中最弱但最关键的 `observability / tracing / metrics` 缺口。它也能服务其他四个机会，成为 context infra 的底层调试面。

## 7. 与本地知识库判断的连接

### 7.1 Harness 架构

本地 Harness 架构框架的关键判断是：agent 的很多进步来自外层控制壳，而不是模型本身；更重要的是分清 `latent space` 和 `deterministic space`。

这对 agent memory eval 的含义是：

| Harness 判断 | 对 memory infra 的转译 |
|---|---|
| 补偿面会移动 | 今天需要 memory write gate、replay、scorer；未来模型更强后，可能部分组织能力内化，但 provenance 和 isolation 仍是系统责任 |
| latent vs deterministic | 是否该写入、如何综合矛盾，部分需要模型判断；权限、版本、TTL、state assertion、成本统计必须 deterministic |
| subagent 常是上下文隔离 | memory / eval worker 的价值不只是分工，而是把探索噪音隔离，只把高价值状态回传 |
| 上下文预算不是越多越好 | LongMemEval-V2 和 MemGym 都说明，关键是 compact evidence 和 memory-isolated score，不是无限塞历史 |

### 7.2 AI 系统产品

AI 系统产品框架强调：真正的工程黑洞常在 runtime 与契约层。Memory benchmarks 的演进正好验证这一点。LoCoMo / LongMemEval 更像问“模型能不能从历史中回答”；STATE-Bench、LongMemEval-V2、MemGym 开始问“runtime 中的 context 是否让任务结果更可靠”。

因此，产品定义上应避免把 agent context infra 说成“AI memory API”。更准确的主语是：

> agent runtime 的 context lifecycle layer，负责历史经验的写入、组织、隔离、调度、纠错、回放和评测。

### 7.3 研究判断

研究判断框架提醒：研究系统的评测应围绕“是否帮助判断下一步”，而不是只追求像百科一样答题。对应到 agent context infra，好的 benchmark 不只是排行榜，而应该帮助 builder 定位下一步该修什么。

这意味着第一版自建 eval 不必追求覆盖所有论文能力。更有价值的是把失败分成可行动类别：

| Failure class | 下一步动作 |
|---|---|
| missed write | 调 write policy 和 salience detector |
| bad merge | 调 contradiction / supersession |
| wrong scope | 调 namespace / permission |
| retrieval miss | 调 index / query / reranker |
| context overload | 调 compression / budget |
| stale application | 调 freshness / expiry / correction |
| tool-state mismatch | 调 state assertion / environment model |

### 7.4 Agent Systems north star

本地 north star 说，目标画像不是“最会做 demo 的人”，而是拥有过一个可部署、可评估、可迭代的 agent system 的 builder。对应本报告，最短路径不是再做一个 memory demo，而是做一个有证据链的 context system：

1. 有真实或半真实 episode dataset。
2. 有 memory on/off 和不同策略的回归评测。
3. 有 trace / replay / scorer breakdown。
4. 有 failure taxonomy。
5. 有 cost / latency / reliability 指标。
6. 有至少一块明确 runtime ownership，比如 write policy、namespace isolation、environment runbook 或 observability debugger。

## 8. 建议的最小研究产物路线

如果以 2-4 周为周期，建议把产物收束成一个小而硬的公开 repo 或 workspace：

| 周期 | 产物 | 成功标准 |
|---|---|---|
| 第 1 周 | 选一个 domain，收集 30-50 个 episode，定义 failure taxonomy 和 baseline | 能跑 no-memory / naive RAG / structured memory 三组 |
| 第 2 周 | 加 memory trace、write log、retrieval log、state assertions、pass^k 和 cost | 每个失败 episode 能定位到至少一个 failure class |
| 第 3 周 | 实现一个明确 runtime ownership 模块，例如 write policy 或 namespace isolation | 至少一个关键指标显著改善，而不是只换模型 |
| 第 4 周 | 写公开报告：benchmark、失败案例、修复、指标变化、残余缺口 | 能被看成 agent systems 证据包，而不是 demo README |

这条路线最适合连接本地知识库已有主线：`context / harness / eval / reliability`。它也能把当前研究调研自然转成履历资产。

## 9. 总结

2026 年的 agent memory benchmark 已经不再满足于“记住用户喜欢什么”。STATE-Bench 把 memory 放进企业状态任务；MemoryAgentBench 把 memory 拆成增量学习、长程理解和选择性遗忘；GroupMemBench 暴露多人记忆的崩塌；StructMemEval 指出结构组织能力缺失；LongMemEval-V2 和 MemGym 把长期记忆推向 web、coding、research、computer use 的环境经验。

这些 benchmark 共同指向一个机会：agent context infra 的下一层壁垒，是把 memory 从被动存储升级为可评测的 runtime control surface。真正值钱的 builder 方向，不是“再包一个 RAG”，而是让 agent 的上下文生命周期有 policy、有边界、有纠错、有回放、有指标，并且能证明它降低了真实任务中的失败率。
