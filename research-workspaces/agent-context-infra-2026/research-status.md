# Agent Context Infra 研究现状草稿（截至 2026-05-24）

> 研究侧工作稿。本文只讨论 `agent context infra` 的研究机制，不覆盖完整工程产品地图。公开资料以指定七篇 arXiv 论文为主，并结合本地知识库中关于 harness、上下文预算、信息复利与 context-core 的既有判断。

## 核心结论

1. **agent memory research 正在从“存什么”转向“何时写、怎样管、如何读”。** [Memory for Autonomous LLM Agents](https://arxiv.org/abs/2603.07670) 把 memory 形式化为 `write-manage-read` loop，并用 temporal scope、representational substrate、control policy 三维 taxonomy 统一了很多看似分散的做法。
2. **更大的研究主语不是 memory，而是 context lifecycle。** memory 是跨轮次保留信息的机制子集；context lifecycle 还包括输入获取、路由、压缩、隔离、虚拟化、权限、观测、评测与回写。很多失败并不是“没记住”，而是上下文在运行时被错误地组织、污染、注入或使用。
3. **“更多上下文”不是可靠性的充分解。** [AI Agents Need Memory Control Over More Context](https://arxiv.org/abs/2601.11653) 与 [Active Context Compression](https://arxiv.org/abs/2601.07190) 都指向同一件事：长任务中真正稀缺的是受控的状态承诺和上下文预算，而不是把 transcript 或检索结果越塞越多。
4. **memory 机制的演进可以压成 Storage、Reflection、Experience 三阶段。** [From Storage to Experience](https://arxiv.org/abs/2605.06716) 的价值在于说明，前沿方向已经不只是保存轨迹，而是把多条轨迹抽象成可迁移经验，并让 agent 主动探索和复用经验。
5. **当前最强的机制族大致分成六类：context-resident compression、retrieval-augmented stores、reflective self-improvement、hierarchical/virtual context、policy-learned management、contextual memory virtualization。** 它们解决的失败模式不同，不能用一个“memory system”标签混在一起评估。
6. **评测正在从 fact recall 走向 agentic state 与 experience，但仍很不充分。** STATE-Bench、StructMemEval、GroupMemBench、LongMemEval-V2 等新评测开始覆盖过程合规、结构化记忆、多人记忆和环境经验，但距离可比较、可复现、可解释的统一评测还很远。
7. **研究缺口集中在可验证写入、因果检索、可信反思、学习型遗忘、多人/多源冲突治理和成本-延迟约束。** 这些问题不是简单换向量库或扩大上下文窗口能解决的，更接近 agent runtime 的控制问题。

## 一、范围：memory research 与 context lifecycle research 的区别

本文把 `agent memory research` 定义为：让 LLM agent 在多轮、多会话或长任务中持久保存、组织并选择性调用过去信息的机制研究。它关心的问题包括写入、更新、检索、遗忘、压缩、反思和经验抽象。

但 `agent context infra` 的范围更大。它研究的是 agent 在运行时如何管理“当下应该被模型看到、工具使用、系统保留、后续回写和评测”的全部上下文生命周期。memory 是其中的持久化部分，context lifecycle 还包括：

| 生命周期环节 | 典型问题 | 不等同于 memory 的原因 |
|---|---|---|
| 获取 | 从用户、文件、工具、数据库、浏览器、其他 agent、环境状态中取什么 | 许多上下文只在当前任务有效，不需要长期记忆 |
| 路由 | 哪些材料进入哪个 agent、哪个工具、哪个子任务 | 这是运行时调度问题，不只是存储问题 |
| 压缩 | 把历史、工具输出、探索过程压成任务状态 | 可能完全发生在 session 内，不进入长期 memory |
| 隔离 | planner / executor、主 agent / subagent、用户 A / 用户 B 之间如何隔离上下文 | 主要防止污染和串用，不只是提升 recall |
| 虚拟化 | snapshot、branch、trim、replay、resume 如何被建模 | 更像 OS / VCS 状态管理，而不是单一记忆库 |
| 写回 | 哪些经验、规则、偏好、失败案例值得沉淀 | 属于 memory，但依赖评测和治理 |
| 观测与评测 | 如何判断上下文机制真的改善任务完成、稳定性、成本和用户体验 | 评测对象是整条 context loop，而不只是检索命中 |
| 治理 | provenance、隐私、权限、冲突、过期、删除 | 长期系统必须处理的控制面 |

本地知识库里“默认工作面”的判断可以作为这里的产品化补充：有效的 context infra 不是把所有信息都存下来，而是把未来反复会用到的高价值信号提前提炼成 agent 的默认工作面。换句话说，memory 的目标不是容量，而是让后续工作站在更好的上下文起点上发生。

## 二、主要 taxonomy

### 2.1 Write-manage-read loop

[Memory for Autonomous LLM Agents](https://arxiv.org/abs/2603.07670) 将 agent memory 抽象成与 perception / action 紧密耦合的 `write-manage-read` loop。这个 loop 比“先存后取”的 RAG 图式更适合 agent，因为 agent 的行动会改变环境，环境反馈又会改变后续应该写入什么。

| 阶段 | 核心动作 | 典型机制 | 主要失败模式 |
|---|---|---|---|
| Write | 判断哪些观察、决策、偏好、错误、环境状态值得进入 memory | 规则写入、LLM extraction、事件触发、人工确认、tool trace capture、反思写入 | 噪音写入、未验证内容固化、隐私越界、把临时状态误当长期事实 |
| Manage | 对已写入内容去重、合并、更新、分层、遗忘、加 provenance | 摘要、semantic triples、KG、profile slots、episodic store、时间衰减、conflict resolver | 旧事实覆盖新事实、矛盾未暴露、摘要损失证据、记忆越积越脏 |
| Read | 在任务中选择性召回并组织为可用上下文 | dense / sparse retrieval、hybrid search、query decomposition、rerank、context packing、tool-mediated evidence gathering | 召回不相关、漏掉关键证据、过度注入、证据顺序错误、把 recall 当 reasoning |

这个 loop 的关键不是三个 API，而是三个控制点：写入是否可信，管理是否保留结构与证据，读取是否服务当前 action。

### 2.2 三维 taxonomy：temporal scope、substrate、control policy

| 维度 | 主要取值 | 研究意义 | 典型风险 |
|---|---|---|---|
| Temporal scope | turn-level、session-level、task-level、multi-session、user-longitudinal、group / organization、environment-longitudinal | 决定记忆的生命周期、更新频率和冲突处理方式 | 把短期探索污染长期画像；把长期偏好误用于一次性任务；多人上下文串用 |
| Representational substrate | raw transcript、compressed summary、structured note、semantic triples、knowledge graph、episodic store、profile memory、runbook / skill、DAG snapshot、tool / environment state | 决定 memory 的可检索性、可解释性、可更新性和成本 | 表示过粗导致证据丢失；表示过细导致检索成本高；结构与任务不匹配 |
| Control policy | 固定规则、prompt policy、agent self-management、evaluator-gated、learned controller、人审 / 用户确认、hybrid policy | 决定谁能写、何时写、何时忘、何时读 | 自主写入带来 poisoning；规则过硬错过隐性经验；learned policy 难解释、难迁移 |

这三个维度组合后，可以解释为什么很多系统表面都叫 memory，但实际机制差异很大。例如 Memori 更强调结构化表示和高效检索，[MemMachine](https://arxiv.org/abs/2604.04853) 更强调保留整段 episodic ground truth 并在 retrieval stage 优化；[Contextual Memory Virtualisation](https://arxiv.org/abs/2602.22402) 则把 session state 建成 DAG，并引入 snapshot、branch、trim 这类状态管理原语。

### 2.3 Storage、Reflection、Experience 三阶段

[From Storage to Experience](https://arxiv.org/abs/2605.06716) 给出另一条演进轴：LLM agent memory 从保存轨迹，走向提炼轨迹，再走向跨轨迹经验抽象。

| 阶段 | 定义 | 代表机制 | 解决的问题 | 局限 |
|---|---|---|---|---|
| Storage | 保留 trajectory、对话、工具结果、用户偏好和环境状态 | transcript store、vector DB、episodic memory、profile slots、raw file store | 防止 agent 每次像第一次见到用户或环境 | 容易变成低质量归档；读不出来、读不准、读太多都仍会失败 |
| Reflection | 对轨迹进行总结、提炼、纠错和规则化 | self-reflection、lesson learned、summary consolidation、error analysis、preference extraction | 减少重复犯错，形成可读的中间层 | 反思可能编造因果；错误经验可能被强化；缺少 ground truth 时难验证 |
| Experience | 从多条轨迹中抽象出可迁移策略、环境知识和主动探索计划 | cross-trajectory abstraction、runbook、skills、policy learning、proactive exploration | 让 agent 不只是记住过去，而是拥有“做过类似事”的经验 | 评测和归因很难；经验是否可迁移、何时过期、如何安全探索都未解决 |

这条阶段划分能帮助区分“记忆系统做大了”与“agent 真有经验了”。一个只保存全量 transcript 的系统仍停在 Storage；一个能把多次失败压成可验证 runbook 并在新任务中主动调用的系统，才接近 Experience。

## 三、机制族、失败模式、评测状态与未解问题

### 3.1 Context-resident compression

这类机制把上下文窗口本身当作稀缺工作台，通过摘要、状态块、knowledge block、任务状态 compaction、工具输出裁剪等方式，让 agent 在有限窗口内保留高杠杆信息。

| 代表工作 | 机制要点 | 解决的失败模式 | 评测状态 | 未解问题 |
|---|---|---|---|---|
| [AI Agents Need Memory Control Over More Context](https://arxiv.org/abs/2601.11653) | Agent Cognitive Compressor 用有界内部状态替代 transcript replay，并区分 artifact recall 与 state commitment | 长交互中 constraint focus 丢失、错误累积、memory-induced drift、噪音召回 | 用 agent-judge-driven live evaluation 覆盖 IT operations、cybersecurity、healthcare 场景，报告较低 hallucination 与 drift | agent judge 的可重复性、跨领域泛化、状态承诺的 ground truth、压缩损失如何审计 |
| [Active Context Compression](https://arxiv.org/abs/2601.07190) | Focus agent 自主决定何时把关键学习写入 persistent Knowledge block，并 prune raw history | context bloat、成本上升、延迟增加、历史错误分散注意力 | 在 5 个 SWE-bench Lite context-intensive 实例上测试，报告约 22.7% token reduction 且准确率不降 | 样本很小；是否适用于非 coding 任务；自主压缩何时过度；压缩内容如何被验证 |
| 本地 coding agent 工作流 | Research / Plan / Implement 本质是事实、意图、执行空间的连续压缩 | brownfield codebase 中搜索噪音污染主上下文、重复定位、计划漂移 | 更多是工程经验与局部实践，还缺标准 benchmark | 如何自动判断 compaction 时机；如何评价“任务状态摘要”质量 |

这一类的核心洞察是：上下文窗口不是仓库，而是工作台。它解决的是 session 内注意力与预算问题，不必然形成长期 memory。

### 3.2 Retrieval-augmented stores

这类机制把 memory 外置到向量库、稀疏索引、hybrid search、structured triples、KG、episodic store 或 profile memory 中，再按 query 检索并注入当前上下文。

| 代表工作 | 机制要点 | 解决的失败模式 | 评测状态 | 未解问题 |
|---|---|---|---|---|
| [Memori](https://arxiv.org/abs/2603.19935) | LLM-agnostic API-layer persistent memory，把对话转为 compact semantic triples 和 summaries | 多模型/多会话缺少持久上下文；raw conversation 注入成本高、性能降 | 在 LoCoMo 上报告 81.95% accuracy，且每次 query 约 1,294 tokens，约为 full context 的 5% | LoCoMo 类 benchmark 仍偏 conversation recall；三元组抽取错误如何纠偏；vendor-neutral memory 的权限与 provenance |
| [MemMachine](https://arxiv.org/abs/2604.04853) | 组合 short-term、long-term episodic、profile memory，保留完整 conversational episodes，并做 contextualized retrieval | RAG 在多 session 中退化；抽取式记忆丢失 ground truth；相关证据跨多轮分散 | 在 LoCoMo、LongMemEvalS、HotpotQA-hard、WikiMultiHop 等报告较好 accuracy-efficiency tradeoff；强调 retrieval-stage optimization 比 ingestion-stage 改动更显著 | benchmark 仍难覆盖真实 agent action；episodic ground truth 成本高；检索策略如何随任务类型自适应 |
| KG / temporal KG 路线 | 把实体、关系、时间、事件和用户画像组织成图 | 多事实、多时间、多关系推理；事实更新与冲突追踪 | 评测常落在 QA、multi-hop、temporal recall | 图构建错误、schema 漂移、边权与时效性、可解释但不一定可行动 |

Retrieval-augmented stores 的长处是把上下文窗口外的历史变成可检索资产。它的典型风险是把 memory 退化成 search：召回到了材料，不代表 agent 会正确理解、排序、遵守或行动。

### 3.3 Reflective self-improvement

这类机制让 agent 在任务后或运行中生成 reflection、lesson、rule、preference update、failure analysis，并在后续任务中调用。

| 机制形态 | 解决的失败模式 | 评测状态 | 未解问题 |
|---|---|---|---|
| 单轨迹反思 | 同一类错误反复出现；agent 不会从失败中提炼规则 | 常在 web navigation、coding、game、tool-use 任务中做 before/after 对比 | 反思是否真实因果难判断；容易把偶然成功写成错误规则 |
| 跨轨迹经验抽象 | 多次任务中有相同环境陷阱、API 约束、用户偏好，但系统每次重新发现 | [From Storage to Experience](https://arxiv.org/abs/2605.06716) 把 cross-trajectory abstraction 放在 Experience 前沿；LongMemEval-V2 也开始评测环境 gotchas 与 workflow knowledge | 经验迁移边界不清；经验冲突与过期难管；缺少可回放的因果证据 |
| evaluator-gated reflection | 避免未验证 lesson 被固化 | STATE-Bench 这类任务型评测可部分验证反思是否改善 pass^5、成本与用户体验 | evaluator 本身可能偏；人审成本高；如何把失败归因到 memory 而不是工具或模型 |

Reflective self-improvement 最像“经验”的来源，但也是最危险的写入路径。没有 ground truth、trace 和 evaluator gate 的 reflection，容易把 hallucination 升级成长期规则。

### 3.4 Hierarchical / virtual context

这类机制不只问“存在哪里”，而是把上下文分层、分角色、分窗口或虚拟化，使 agent 在不同抽象层看到不同材料。

| 机制形态 | 代表例子 | 解决的失败模式 | 评测状态 | 未解问题 |
|---|---|---|---|---|
| short-term / long-term 分层 | thread state、long-term namespace、profile memory、episodic memory | 当前任务状态和长期用户画像混在一起 | 多数框架已有工程接口，但研究评测常只看 recall | 层间提升与降级规则不清；什么该从 short-term 晋升到 long-term |
| core / archival 分层 | core memory 常驻，archival memory 检索式进入 | 关键身份/偏好被淹没在长历史中 | 产品系统常用，公开评测有限 | 常驻内容容易过时；用户可控性与隐私边界 |
| planner / executor 隔离 | 高层 planner 保持干净上下文，executor 承担工具噪音 | 执行噪音污染战略判断；subagent 把搜索过程塞满主窗口 | coding agent 与 multi-agent harness 中有强工程信号 | 如何自动决定隔离粒度；子上下文回传摘要是否完整 |
| virtual context / runbook | 把历史经验编译成可调用文件、skill、runbook | 每次任务从 raw history 重新开始 | LongMemEval-V2 的 AgentRunbook-C 说明 coding-agent-style evidence gathering 可提升准确率，但延迟高 | 准确率-延迟 Pareto 仍差；runbook 如何更新、去重、撤销 |

这一类更接近 `context lifecycle research` 而不只是 memory research。它关心的是上下文在运行时的拓扑结构：哪些东西常驻、哪些东西检索、哪些东西隔离、哪些东西只在子任务中存在。

### 3.5 Policy-learned management

这类机制把写入、压缩、检索、遗忘、路由等决策交给 learned policy、agent policy 或 evaluator-guided policy，而不是固定规则。

| 控制点 | 可能学习的策略 | 解决的失败模式 | 评测状态 | 未解问题 |
|---|---|---|---|---|
| 写入 | 何时写、写什么、是否需要确认 | 写入噪音、遗漏关键经验、隐私越界 | 多数仍是 prompt/rule/self-management，严格 learned policy 较少 | reward 设计困难；误写入代价高；需要可解释与可撤销 |
| 压缩 | 何时 compact、保留哪些事实、丢弃哪些 raw trace | context bloat、dumb zone、成本和延迟失控 | Focus 展示 autonomous compression 的早期证据，但样本小 | 压缩质量很难自动评分；错误压缩会隐藏失败证据 |
| 读取 / 路由 | query decomposition、检索深度、direct vs iterative retrieval | 召回不足、过召回、多跳证据分散 | MemMachine 的 Retrieval Agent 展示 direct、parallel decomposition、chain-of-query 路由 | 策略是否可迁移到真实工具环境；成本预算如何纳入 |
| 遗忘 | 何时删除、降权、过期、隔离 | 旧事实污染新任务；敏感信息长期残留 | 当前评测最弱 | “学会忘记”的目标函数和用户权利很难同时满足 |

policy-learned management 是未来方向，但截至 2026-05-24 仍更像研究议程而不是成熟共识。它真正难的地方在于，memory policy 的错误不是单步错误，而会在长期运行中累积。

### 3.6 Contextual memory virtualization

[Contextual Memory Virtualisation](https://arxiv.org/abs/2602.22402) 值得单列，因为它把 agent context 从“内容集合”改写为“版本化状态”。CMV 把 session history 建成 DAG，并提供 snapshot、branch、trim 原语。它的 trimming 目标不是普通摘要，而是结构上尽量无损地移除机械膨胀内容，例如 raw tool outputs、base64 images、metadata。

| 机制 | 解决的失败模式 | 评测状态 | 未解问题 |
|---|---|---|---|
| DAG session state | 单线性会话难复用；并行 session 之间无法共享已积累理解 | 论文在 76 个真实 coding sessions 上做 single-user case study | 需要多人、多仓库、多模型复现；DAG 粒度和 merge 语义仍不成熟 |
| Snapshot / branch | 长任务到达窗口极限后只能 lossy compaction；探索分支难回滚 | 与 coding agent 实践高度相关 | 分支状态如何冲突合并；用户如何理解和控制分支 |
| Structurally lossless trimming | 传统 compaction 丢失用户消息、assistant response 或关键证据 | 报告平均 20% token reduction，mixed tool-use sessions 平均 39% reduction，最高 86% | “结构无损”不等于“语义无损”；工具输出被裁后如何按需恢复 |

CMV 的重要性在于，它把 context infra 往 OS / VCS 类基础设施方向推了一步。这里的研究问题不是“agent 记住了什么”，而是“agent accumulated understanding 如何作为可版本化、可裁剪、可复用的状态存在”。

## 四、评测状态：从 recall 到 agentic memory，但还未闭环

截至 2026-05-24，memory evaluation 正在快速迁移，但仍存在明显断层。

| 评测类型 | 代表 | 测什么 | 价值 | 局限 |
|---|---|---|---|---|
| Conversational recall | LoCoMo、LongMemEval 早期版本 | 用户事实、偏好、多轮对话中的信息召回 | 适合比较检索与压缩成本 | 容易把 memory 简化成 QA；不测 action quality |
| Structured memory | [StructMemEval](https://arxiv.org/abs/2602.11243) | agent 是否能把长期记忆组织成 ledger、todo、tree 等结构 | 开始测“组织记忆”而不只是“记住事实” | 仍是 work in progress；结构提示对结果影响大 |
| Production-like stateful tasks | [STATE-Bench](https://opensource.microsoft.com/blog/2026/05/19/introducing-state-bench-a-benchmark-for-ai-agent-memory/) | 企业场景中的任务完成、pass^5、一致性、效率、用户体验 | 把 memory 价值绑定到 procedure、state mutation 和 user experience | memory 与模型、工具、orchestration 的贡献分离仍难 |
| Group memory | [GroupMemBench](https://arxiv.org/abs/2605.14498) | 多人对话、speaker-grounded belief、term ambiguity、audience adaptation | 暴露单用户 memory 系统在群组场景的结构性缺口 | 合成 pipeline 与真实组织聊天仍有距离；隐私和权限未充分进入评测 |
| Environment experience | [LongMemEval-V2](https://arxiv.org/abs/2605.12493) | web agent 的 interface affordances、state dynamics、workflow、gotchas、premise awareness | 把 memory 推向“有经验的同事” | 高准确方法延迟高；context gathering 与实际闭环行动仍有距离 |

一个关键趋势是，评测对象正在从“是否能取回某个事实”转向“memory 是否改善 agent 的长期行为”。STATE-Bench 明确把 task completion、reliability、efficiency、user experience 放在同一评测框架里；GroupMemBench 则显示，当前领先 memory systems 在多人记忆上会出现明显 collapse，最强系统平均 accuracy 也只有 46.0%，一些维度甚至被 BM25 追平或超过。

但评测仍没有完全解决三个问题：

- **归因问题**：任务变好是 memory 机制带来的，还是模型、prompt、工具、用户模拟器或 orchestration 带来的？
- **长期问题**：许多 benchmark 是一次性离线评测，不能充分模拟 memory 在数周或数月内累积、污染、过期和纠错。
- **治理问题**：隐私、权限、删除、冲突、provenance、多人边界通常还没有成为硬指标。

## 五、失败模式地图

| 失败模式 | 表现 | 更可能需要的机制 | 为什么单纯扩大上下文不够 |
|---|---|---|---|
| Context bloat | token 成本、延迟、推理质量下降 | context-resident compression、CMV trimming、subagent 隔离 | 更多窗口会容纳更多噪音，未必提升注意力 |
| Constraint drift | 长任务中忘记约束、目标或政策 | bounded state、state commitment、runbook、planner/executor 分层 | transcript replay 会带入错误路径和干扰信息 |
| Memory poisoning | 未验证内容、用户误导或模型 hallucination 被长期保存 | write gating、provenance、evaluator-gated reflection、人审 | 扩大上下文会放大 poisoned memory 的影响 |
| Retrieval mismatch | 检索到相关但不够可行动的材料，或漏掉跨轮证据 | contextual retrieval、query routing、episodic ground truth | recall 不是 reasoning；证据结构和排序同样重要 |
| Summary loss | 摘要丢掉关键细节、条件、反例或 provenance | ground-truth-preserving episodic store、structurally lossless trim | 长摘要仍会丢失证据；需要可回溯 raw source |
| Repeated failure | agent 每次重新踩同一坑 | reflection、experience abstraction、runbook / skill | 原始历史太长，agent 未必能抽出可迁移经验 |
| Cross-user contamination | 用户、团队或角色之间的记忆串用 | identity boundary、namespace、group memory model、permission-aware retrieval | 上下文越多，越需要边界，而不是越开放 |
| Stale memory | 旧偏好、旧环境状态、旧 API 规则污染新任务 | temporal scoping、decay、learned forgetting、conflict resolver | 大窗口会同时保留新旧信息，但不自动判断哪个有效 |

## 六、未解问题

1. **可信写入**：哪些信息有资格从 transient context 进入 persistent memory？是否需要 trace、工具证据、用户确认或 evaluator gate？
2. **因果检索**：系统如何知道某条 memory 会真正改善当前 action，而不是只是语义相似？
3. **反思可信度**：agent 生成的 lesson 是否真的解释了失败原因？如何防止错误反思长期污染 policy？
4. **学习型遗忘**：何时删除、降权、隔离、归档或保留矛盾记忆？遗忘既是质量问题，也是隐私和用户权利问题。
5. **结构选择**：何时用 raw episodes，何时用 triples，何时用 KG，何时用 runbook，何时用 DAG state？当前缺少机制选择的明确准则。
6. **多用户和组织记忆**：group memory 需要 speaker-grounded belief、权限、角色、术语歧义和 audience adaptation。单用户 memory 架构不能直接平移。
7. **评测归因**：memory、retrieval、prompt、model、tool、orchestration、user simulator 混在一起时，如何隔离每个组件的贡献？
8. **成本-延迟约束**：越复杂的 memory controller 和 evidence gathering 越可能提升准确率，也越可能让 agent 不适合交互式使用。
9. **context state 的可观察性**：用户和开发者需要看到当前上下文为什么被写入、裁剪、召回或忽略。否则 context infra 会变成新的黑箱。

## 七、对 agent context infra 的研究定位

如果只从 memory 角度看，这个领域像是在比较不同存储和检索策略。但从 agent context infra 角度看，真正的问题更像：

> 在一个长程、状态化、会调用工具、会改变环境、会面对多用户边界的 agent runtime 中，如何把上下文作为一种可治理的运行时资源来管理？

这也是为什么本地知识库里的 harness 判断与这些论文可以接起来：

- context compression 对应上下文预算管理；
- subagent / planner-executor 分层对应上下文隔离；
- write-manage-read loop 对应 memory 的最小控制闭环；
- Storage / Reflection / Experience 对应信息复利从 raw data 到默认工作面的层级迁移；
- CMV 对应 session state 的 OS / VCS 化；
- STATE-Bench 这类评测对应 eval-first context layer，而不是单点 memory demo。

因此，后续主报告如果要讨论 `agent context infra`，建议把 memory 放在更大的四层结构里：

| 层 | 研究主语 | 关键问题 |
|---|---|---|
| Memory layer | 写入、管理、读取长期信息 | 记什么、怎样表示、何时召回、何时遗忘 |
| Context runtime layer | 压缩、路由、隔离、虚拟化、预算 | 当前任务中模型到底该看到什么 |
| Governance layer | provenance、权限、隐私、冲突、可撤销 | 上下文是否可信、合规、可控 |
| Evaluation layer | recall、task success、state mutation、reliability、cost、UX | 机制是否真的让 agent 变好 |

这一区分很重要。一个 memory 系统可以在 recall benchmark 上很好，却在真实 agent workflow 中因为路由、隔离、写入污染或成本延迟失败。反过来，一个 session 内 compression / virtualization 机制未必提供长期 memory，却可能显著提升 agent context lifecycle 的稳定性和经济性。

## 主要来源

- [Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670)
- [From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716)
- [AI Agents Need Memory Control Over More Context](https://arxiv.org/abs/2601.11653)
- [Active Context Compression: Autonomous Memory Management in LLM Agents](https://arxiv.org/abs/2601.07190)
- [Contextual Memory Virtualisation: DAG-Based State Management and Structurally Lossless Trimming for LLM Agents](https://arxiv.org/abs/2602.22402)
- [Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents](https://arxiv.org/abs/2603.19935)
- [MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents](https://arxiv.org/abs/2604.04853)
- [STATE-Bench: A benchmark for AI agent memory](https://opensource.microsoft.com/blog/2026/05/19/introducing-state-bench-a-benchmark-for-ai-agent-memory/)
- [StructMemEval / Evaluating Memory Structure in LLM Agents](https://arxiv.org/abs/2602.11243)
- [GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations](https://arxiv.org/abs/2605.14498)
- [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493)
- 本地知识库：[Harness 架构判断框架](../../wiki/frameworks/Harness架构判断框架.md)、[coding agent 的上下文压缩工作流](../../wiki/knowledge/coding%20agent%20的上下文压缩工作流.md)、[信息复利系统设计](../../wiki/bridges/information-compounding-systems-design.md)、[Agent 系统月度执行计划（2026-05-24）](../../wiki/bridges/Agent系统月度执行计划-2026-05-24.md)

## 本次创建/修改文件

- `/Users/beiyanliu/Desktop/knowledge base/research-workspaces/agent-context-infra-2026/research-status.md`
