# Context-Core 技术前沿调研报告（2026-05-25）

## 范围说明

本文只讨论 `context layer` / `context-core`，刻意排除通用 agent runtime、MCP/A2A 这类连接协议、OpenAI Agents SDK 这类编排框架、普通 tool orchestration 和泛工作流平台。

这里的 `context-core` 指 agent 系统中负责以下对象的核心层：

- 上下文写入：哪些 episode、状态、偏好、错误、轨迹和经验值得进入长期上下文。
- 上下文状态：哪些信息常驻工作记忆，哪些只在需要时检索，哪些应被版本化。
- 上下文管理：去重、合并、冲突、过期、纠错、压缩、结构化、来源追踪。
- 上下文读取：如何检索、排序、打包、注入，让模型看到“该看到的东西”。
- 上下文文件系统：把 memory、resources、skills、runbooks、sessions 组织成可浏览、可 diff、可审计的工作面。
- 上下文评测：如何证明这些机制真的改善任务表现，而不是只让 demo 看起来更聪明。

压缩判断：

> 2026 年的 context-core 前沿，已经从“外部记忆库”推进到“上下文控制平面”。它的核心问题不是存储容量，而是写入控制、状态承诺、结构化治理、检索归因、环境经验和任务级评测。

## 总览分类

| 类型 | 代表论文 / 项目 | 核心问题 | 主要创新 |
|---|---|---|---|
| 总体理论 | Memory for Autonomous LLM Agents、From Storage to Experience | 如何给 agent memory 建模 | `write-manage-read`、Storage/Reflection/Experience |
| 上下文控制 | ACC、Active Context Compression、CMV、Parallel Context Compaction | 长任务中如何避免上下文膨胀和 drift | 有界状态、主动压缩、DAG snapshot、并行压缩 |
| 写入与治理 | MemRouter、MemMachine、Memori、MemConflict、WorldDB、Portable Agent Memory | 写什么、如何保真、如何冲突治理 | write-side router、ground-truth episodes、semantic triples、conflict diagnostics、write-time reconciliation、Merkle provenance |
| 生成式 / 学习式 memory | Mem-π、Memory-R2、MementoGUI | memory 是否可以学习何时生成、何时写、何时读 | RL guidance、local/global credit assignment、多模态 memory controller |
| 文件式 context | OpenViking、Letta Context Repositories、Claude Managed Agents memory | 如何让上下文成为可操作资产 | context file system、git-backed memory、filesystem memory with audit |
| 产品化 memory layer | Mem0、Zep/Graphiti、Letta memory blocks、Cloudflare Session/context blocks | 如何把 context-core 做成可用组件 | entity scope、temporal KG、self-editing memory、context blocks |
| 评测 | MemoryAgentBench、StructMemEval、GroupMemBench、LongMemEval-V2、MemGym | 如何评估 context-core 是否有效 | incremental memory、结构化记忆、多人记忆、环境经验、memory-isolated score |

## 一、总体理论框架

### 1. Memory for Autonomous LLM Agents

来源：[arXiv:2603.07670](https://arxiv.org/abs/2603.07670)

**技术判断**

这篇 survey 的价值不是列举很多 memory 方法，而是把 agent memory 从“存储组件”重新定义为与 perception / action 耦合的控制循环。它提出的 `write-manage-read` loop 是当前 context-core 最好的总框架。

**工作机制**

它把每一步 agent 交互看成：agent 基于当前输入、目标和 memory read 产生 action；环境返回 observation / reward；memory update 函数再决定如何写入、管理和读取。这个定义把 memory 从被动数据库变成 agent belief state 的外部化版本。

三维 taxonomy：

- Temporal scope：turn、session、multi-session、user-longitudinal、group、environment。
- Representational substrate：raw transcript、summary、semantic triples、knowledge graph、profile memory、procedural memory、runbook。
- Control policy：规则、prompt policy、agent self-management、evaluator-gated、learned controller、human-confirmed。

**技术创新**

1. 把 write / manage / read 拆成三个可评测控制点。
2. 把 context-resident compression、retrieval stores、reflection、hierarchical virtual context、policy-learned management 放进同一个机制族地图。
3. 明确指出工程难点包括 write-path filtering、contradiction handling、latency budgets、privacy governance。

**重点难点**

- `manage` 是最弱环节。很多系统能写和读，但不会合并、过期、纠错。
- memory 和 action 是耦合的。agent 的行为会改变环境，环境变化又会改变应该写入什么。
- evaluation 不能只测 recall。必须测 memory 对行动质量的影响。

**未来方向**

最值得继续做的是 learned memory controller、causally grounded retrieval、trustworthy reflection、learned forgetting、multimodal embodied memory。对 context-core builder 来说，这篇给出的不是具体实现，而是系统分层语言。

### 2. From Storage to Experience

来源：[arXiv:2605.06716](https://arxiv.org/abs/2605.06716)

**技术判断**

这篇 survey 的核心贡献是把 agent memory 的演进从“存储更多历史”推进到“抽象可迁移经验”。它对 context-core 的启发是：长期上下文的终点不是 archive，而是 experience。

**工作机制**

它把 memory 机制分成三阶段：

| 阶段 | 对象 | 机制 | 技术含义 |
|---|---|---|---|
| Storage | trajectory preservation | 保存 observation-action traces | 解决无状态问题，但容易变成低质量归档 |
| Reflection | trajectory refinement | 对轨迹做 critique、summary、lesson | 提升密度，但可能错误归因 |
| Experience | trajectory abstraction | cross-trajectory abstraction、proactive exploration | 形成可迁移策略和环境经验 |

**技术创新**

它把“经验”定义为高于 episodic memory 的层：不是记住某一次发生了什么，而是从多次交互中提炼“下次遇到类似环境该怎么做”。

**重点难点**

- Reflection 很容易产生伪因果。agent 会把偶然成功写成规则。
- Experience 的迁移边界很难判断。一个 repo / UI / 组织流程中的经验，在另一个环境可能有害。
- 评测难。经验是否有效，必须放进后续任务里看 first-try success、重复错误率和探索步数。

**未来方向**

下一代 context-core 应该有 `episode -> reflection -> runbook -> skill` 的链路，并保留源 episode 以便回溯。只做 conversation memory 的系统会停在 Storage。

## 二、上下文控制与压缩

### 3. Agent Cognitive Compressor（ACC）

来源：[AI Agents Need Memory Control Over More Context](https://arxiv.org/abs/2601.11653)

**技术判断**

ACC 的核心判断很明确：agent 失控不是因为上下文不够多，而是因为 context replay 和 retrieval memory 会带来无界增长、噪音召回和 memory poisoning。它主张用一个有界、schema-constrained 的 cognitive state 替代 transcript replay。

**工作机制**

ACC 维护一个 compressed cognitive state（CCS）。每轮交互后，它用当前输入、旧 CCS 和经过资格过滤的 recall set 生成新 CCS。关键在于区分：

- artifact recall：可以读取外部材料，但不一定承诺进长期状态。
- state commitment：只有被压缩器确认的内容才能进入下一轮常驻认知状态。

**技术创新**

1. 把 memory 从“越来越长的历史”改成“有界状态承诺”。
2. 把未验证 recall 与持久状态分开，降低错误信息固化。
3. 用 live evaluation 测 memory-driven anomalies，而不是只测最终答案。

**重点难点**

- CCS 的 schema 如何设计是系统成败关键。太粗会丢约束，太细会退化成小数据库。
- 压缩器本身可能把错误归纳进状态。
- 对复杂代码 / 多工具任务，状态中哪些字段应常驻仍需 domain-specific 设计。

**未来方向**

ACC 适合成为 context-core 的 `working state` 层，而不是完整 memory layer。它未来应和 provenance、episode store、replay debugger 结合，让每个状态字段都能追溯来源和验证结果。

### 4. Active Context Compression

来源：[arXiv:2601.07190](https://arxiv.org/abs/2601.07190)

**技术判断**

Active Context Compression 代表“agent 自主管理上下文预算”的方向。它不满足于外部定时总结，而是让 agent 在运行中判断何时压缩、写入 persistent knowledge、裁剪历史。

**工作机制**

系统把长期对话和工具结果拆成可被压缩的段落，并让 controller 根据任务状态触发 compression。压缩产物不只是 summary，而是可在后续步骤稳定注入的 persistent knowledge block。

**技术创新**

- 把 compression 变成 agentic action。
- 从“被动防止超窗”转向“主动维护上下文质量”。
- 关注压缩后对 task state 和 constraint focus 的保留。

**重点难点**

- 何时压缩比怎么压缩更难。过早压缩会丢局部细节，过晚压缩会污染工作台。
- 压缩产物需要可验证。否则 summary drift 会变成新的长期污染。
- 通用压缩 prompt 很难适配不同 domain 的完成标准。

**未来方向**

最有前途的方向是 domain-aware compression policy：coding、GUI、research、customer support 应该有不同的状态槽和压缩模板。

### 5. Contextual Memory Virtualisation（CMV）

来源：[arXiv:2602.22402](https://arxiv.org/abs/2602.22402)

**技术判断**

CMV 的贡献是把 session history 当成可版本化状态，而不是线性聊天记录。它用 OS virtual memory / Git 的类比，为 context-core 引入 snapshot、branch、trim 三个原语。

**工作机制**

CMV 把 session history 建模为 DAG。节点可以 snapshot，新的会话可以从某个 snapshot branch 出来。trim 算法保留用户消息和 assistant response，同时删除机械噪音，如 raw tool outputs、base64 images、metadata。

**技术创新**

1. conversation state 版本化。
2. branch 允许并行探索不同方案。
3. structurally lossless trimming 关注“保留对话语义，删除机械负载”。

**重点难点**

- CMV 更像状态管理工具，不负责判断哪些经验该沉淀为长期 memory。
- 对 tool-heavy 任务有价值，但对需要事实抽取和冲突治理的长期 assistant 不够。
- DAG snapshot 的可读性、命名和合并策略会影响实际可用性。

**未来方向**

CMV 适合和 context repository / runbook memory 结合：snapshot 管任务状态，runbook 管跨任务经验，episode store 管证据。

### 6. Parallel Context Compaction

来源：[arXiv:2605.23296](https://arxiv.org/abs/2605.23296)

**技术判断**

这篇论文切中一个工程痛点：LLM-based summarization 不仅有损，而且会阻塞 agent 推理数十秒；同时 summary 长度不可控，导致保留知识在不同 run 之间波动。

**工作机制**

它提出 parallel compaction：把上下文划分成多个 block 并行压缩，让 operator 能更细粒度控制每个 block 的 summary volume 和 prompt。评测覆盖 HotpotQA 和 LoCoMo，并比较不同规模、不同架构模型。

**技术创新**

- 将 compaction 从单个同步阻塞调用，改成可并行、可配额、可分块的服务。
- 强调 summary volume 的可预测性。
- 让不同上下文块使用不同 prompt，避免“一把 summary prompt 走天下”。

**重点难点**

- 分块边界很难。错误切分会破坏跨块依赖。
- 并行摘要之间可能互相矛盾或重复。
- block-level summary 还需要全局 reconciler，否则会丢整体任务状态。

**未来方向**

适合服务端 agent serving 场景。未来应加入 provenance-preserving summary、cross-block consistency check、summary diff 和 replay eval。

## 三、写入、保真与治理

### 7. MemRouter

来源：[arXiv:2605.00356](https://arxiv.org/abs/2605.00356)

**技术判断**

MemRouter 的关键判断是：长期 memory 的瓶颈在 write side。当前很多系统每轮都用 autoregressive LLM 判断是否写入，成本高、延迟高、还和 answer backbone 耦合。MemRouter 把 memory admission 学成轻量分类问题。

**工作机制**

每个 turn 连同 recent context 被编码成 embedding，再通过 frozen LLM backbone 投影，训练轻量 classification heads 判断是否应存储。它只训练约 12M 参数，并保持 retrieval pipeline、answer prompt、QA backbone 不变做 matched-harness 比较。

**技术创新**

- 把 memory admission 从 LLM decoding 换成 embedding routing。
- 解耦 write-side policy 和 answer generation。
- 显著降低 memory-management latency，搜索结果显示 p50 从 970ms 降到 58ms。

**重点难点**

- 训练数据决定写入标准。不同 domain 的“值得记住”差异很大。
- 二分类过粗，实际需要 memory type、scope、TTL、confidence。
- 它解决写不写，但不直接解决怎么合并、纠错和冲突。

**未来方向**

MemRouter 很适合变成 context-core 的 write gate 第一层：先低成本 admission，再由更重的治理层决定 type / scope / provenance / expiry。

### 8. MemMachine

来源：[arXiv:2604.04853](https://arxiv.org/abs/2604.04853)

**技术判断**

MemMachine 站在 preservation-first 一侧。它反对在写入时用 LLM 摘要或抽取事实，因为这会丢 ground truth。它选择保存完整 conversational episodes，把重活放到 retrieval stage。

**工作机制**

它整合 short-term、long-term episodic、profile memory。核心是保存原始 episode，并在检索时做 contextualized retrieval：命中 nucleus turn 后，扩展相邻上下文以恢复对话语义。论文报告在 LoCoMo 达到 0.9169，在 LongMemEvalS 达到 93.0%，且 retrieval-stage optimization 的收益大于 ingestion-stage chunking。

**技术创新**

1. 延迟抽取：写入时保真，读取时解释。
2. context expansion：检索命中点周围的 turns，而不是孤立 chunk。
3. 通过 retrieval depth、context formatting、search prompt、query bias correction 提升效果。

**重点难点**

- 读路径变重。每次查询都要更聪明地解释原始 episode。
- 原始 episode 存储带来隐私和治理压力。
- 如果没有冲突建模，保真只会保留所有矛盾，不会告诉 agent 哪个现在有效。

**未来方向**

MemMachine 适合高问责场景，如医疗、合规、研究助理。未来要和 conflict-aware ranking、provenance audit、selective disclosure 结合。

### 9. Memori

来源：[arXiv:2603.19935](https://arxiv.org/abs/2603.19935)

**技术判断**

Memori 站在 structured-compression 一侧。它认为 memory 是 data structuring problem，而不是长上下文问题。它把非结构化 dialogue 转成 compact semantic triples 和 conversation summaries。

**工作机制**

Advanced Augmentation pipeline 将 dialogue 编译成 semantic triples 与 summary，查询时用这些结构化表示做更精确的 retrieval 和 prompt augmentation。论文报告 LoCoMo 81.95% accuracy，并且每 query 只用约 1,294 tokens，约为 full context 的 5%。

**技术创新**

- 用 semantic triples 提升 compactness 和可检索性。
- 显著降低 token 成本。
- LLM-agnostic API layer，避免 vendor lock-in。

**重点难点**

- 写入时抽取会丢失上下文细节。
- triples 对关系事实有效，但对过程经验、环境 gotchas、风格偏好不一定足够。
- correction 和 contradiction 需要额外管理层。

**未来方向**

Memori 的路线适合把事实型 memory 编译成结构化中间层。它未来需要和原始 episode backpointer 结合，避免 semantic triple 成为不可追溯的“二手事实”。

### 10. MemConflict

来源：[arXiv:2605.20926](https://arxiv.org/abs/2605.20926)

**技术判断**

MemConflict 把 context-core 的治理问题说清楚了：memory 是否有效不是全局属性，而是 query-conditioned fitness-for-use。某条 memory 对一个 query 有效，对另一个 query 可能过期、错误或条件不适用。

**工作机制**

它构造结构化用户画像和跨月多 session 历史，引入三类冲突：

- Dynamic conflict：用户状态随时间变化，旧值被新值 supersede。
- Static conflict：不变事实被后续错误提及干扰。
- Conditional conflict：多个事实都正确，但只有满足 query condition 的事实适用。

评测分黑盒 final answer 和白盒 supporting-memory retrieval / ranking。指标包括 Answer Accuracy、Support Evidence Hit@K、Support Rank Score 等。

**技术创新**

- 把冲突类型形式化。
- 区分“答对了”和“检索/排序对了”。
- 能诊断 retrieval failure 与 utilization failure。

**重点难点**

- 目前主要是 benchmark，不是解决方案。
- simulated profile 和真实企业历史之间仍有 gap。
- 对多人 / 权限 / source authority 的冲突还可扩展。

**未来方向**

MemConflict 应成为 memory governance 的标准回归测试。真正的 context-core 应内建 dynamic/static/conditional conflict tests，而不是只做 recall benchmark。

### 11. WorldDB

来源：[arXiv:2604.18478](https://arxiv.org/abs/2604.18478)

**技术判断**

WorldDB 是目前最激进的 write-time governance 方案之一。它认为 flat vector store 和普通 temporal KG 都不够，因为它们没有递归结构、内容地址不变性和边语义行为。

**工作机制**

WorldDB 把每个 node 定义为一个 `world`：内部可包含子图、本体 scope、composed embedding 和 bitemporal validity。节点 content-addressed 且 immutable，任何修改都会产生新 hash 并向祖先传播。边不是被动标签，而是 write-time programs，带 `on_insert`、`on_delete`、`on_query_rewrite` handler。

典型边行为：

- supersession：关闭旧事实 validity。
- contradiction：保留双方并显式标记冲突。
- same_as：提出 merge proposal。

**技术创新**

1. 递归 world node，突破 flat graph。
2. Merkle-style audit trail。
3. write-time reconciliation，禁止 raw append path。
4. BM25、HNSW、graph traversal 三路 hybrid retrieval。

**重点难点**

- 工程复杂度很高。ontology、edge programs、hash propagation、query planning 都是维护点。
- 论文结果需要独立复现，尤其是 LongMemEval-s 上的高分。
- 对 open-ended conversational memory，ontology scope 如何自动生成和演进仍不清楚。

**未来方向**

WorldDB 的方向很像“memory database 变成有语义约束的数据库”。未来如果要做 enterprise context-core，write-time reconciliation 会比 read-time rerank 更关键。

### 12. Portable Agent Memory

来源：[arXiv:2605.11032](https://arxiv.org/abs/2605.11032)

**技术判断**

Portable Agent Memory 关注 memory portability 和 provenance。它提出：agent 积累的 episodic、semantic、procedural、working state 和 identity preferences 不应锁死在某个 vendor runtime 中。

**工作机制**

它定义五组件 memory model，使用 content-addressable entries 和 Merkle-DAG provenance graph，支持 capability-based access control、selective scoped disclosure、injection-resistant rehydration，以及 JSON-first / CBOR optional serialization。

**技术创新**

- 把 memory 当成可验证、可转移资产。
- 用 Merkle-DAG 提供 tamper-evidence。
- 引入 rehydration protocol，处理跨模型注入时的 prompt injection 风险。

**重点难点**

- 协议本身不保证 memory quality。
- 不同 agent 对同一 memory entry 的语义解释可能不同。
- selective disclosure 与上下文完整性存在张力：不给足背景可能误用，给太多又泄露。

**未来方向**

适合成为 context export / import / migration 层。对个人长期 agent 来说，memory portability 会越来越重要。

## 四、学习式与生成式 context-core

### 13. Mem-π

来源：[arXiv:2605.21463](https://arxiv.org/abs/2605.21463)

**技术判断**

Mem-π 挑战了“memory 必须是检索外部条目”的默认假设。它把 memory 重新定义成按需生成的 task guidance：由独立 memory model 根据当前 agent context 决定何时生成、生成什么。

**工作机制**

Mem-π 使用一个独立语言或视觉语言模型作为 memory policy。它 conditioned on 当前 agent context，联合决定：

- 是否生成 guidance。
- 生成什么 guidance。

训练采用 decision-content decoupled RL，让模型学会在无帮助时 abstain，有帮助时输出简短有效指导。

**技术创新**

- memory as generated guidance，而不是 retrieved entry。
- decision 和 content 解耦训练。
- 可用于 web navigation、terminal tool use、text-based embodied interaction。

**重点难点**

- guidance 不是可审计事实，可能产生幻觉或不可追溯建议。
- 需要 RL 训练数据和任务 reward。
- 对高问责 memory，不如保真型 / provenance 型系统稳。

**未来方向**

Mem-π 更像 procedural memory / strategy hint generator。未来可与 episode store 结合，让 generated guidance 必须附带源 episode 或 confidence。

### 14. Memory-R2

来源：[arXiv:2605.21768](https://arxiv.org/abs/2605.21768)

**技术判断**

Memory-R2 关注训练 memory-augmented agents 的 credit assignment 难题。它指出：memory 会把过去 action 变成未来 environment 的一部分，所以不同 rollouts 一旦写了不同 memory，就不再处于同一个中间状态，传统 GRPO 式比较不公平。

**工作机制**

核心算法 LoGo-GRPO 结合：

- Global objective：保留端到端 long-horizon reward。
- Local rerollouts：从同一个 intermediate memory state 出发，比较不同 memory operation 的结果。

同时用共享参数 co-learning 训练 fact extractor 和 memory manager，并通过 8 -> 16 -> 32 sessions 的 progressive curriculum 稳定长 horizon 训练。

**技术创新**

- 把 memory operation 的 credit assignment 明确成训练问题。
- 局部 rerollout 解决不同 memory states 不可比的问题。
- 同时优化 memory formation 和 memory evolution。

**重点难点**

- 训练成本高。
- reward 设计决定 memory 学到什么。
- local rerollout 的 intermediate state capture 和恢复在真实系统里很重。

**未来方向**

Memory-R2 指向 context-core 的长期方向：write/manage policy 不只靠 prompt，而应可训练、可评估、可归因。

### 15. MementoGUI

来源：[arXiv:2605.18652](https://arxiv.org/abs/2605.18652)

**技术判断**

MementoGUI 把 context-core 推进到多模态 GUI agent。它指出：GUI agent 的长期任务不能只靠 raw screenshot replay，也不能只靠 text summary，因为局部视觉证据会丢。

**工作机制**

MementoGUI 引入 MementoCore，一个学习式 online memory controller。它有两类 memory：

- Working memory：保存任务相关 interface events，包括文本摘要和 ROI-level visual evidence。
- Episodic memory：保存可复用历史轨迹，通过 learned relevance selection 检索。

MementoCore 模块化为 step processing、memory compression、episodic writing、episodic selection 等 operator，可插入 GUI agent backbone 而无需微调 backbone。

**技术创新**

- 多模态 memory 不再只存文字。
- ROI-level evidence 保留未来决策需要的局部视觉线索。
- 把长 GUI 控制建模成 online memory-control problem。

**重点难点**

- 视觉 evidence 的存储和检索成本高。
- ROI selection 错误会造成不可恢复的信息损失。
- GUI 状态变化快，episode reuse 的适用性需要严格判断。

**未来方向**

对 computer-use agent，未来 context-core 必须支持 multimodal episodic memory。文本 runbook 不够，必须能保留 UI region、视觉状态和动作轨迹。

## 五、文件式 context 与 context database

### 16. OpenViking

来源：[OpenViking docs](https://openviking.ai/docs)、[OpenViking GitHub](https://github.com/volcengine/OpenViking)

**技术判断**

OpenViking 最重要的判断是：agent context 不应该只是平面 chunk store，而应该是可浏览、可定位、可回写的 context file system。它把 memory、resources、skills、sessions 统一进 `viking://` 虚拟文件系统。

**工作机制**

核心路径：

- `viking://resources`：项目文档、代码库、网页等资源。
- `viking://user`：用户偏好、习惯、长期记忆。
- `viking://agent`：agent skills、instructions、task memories。
- `viking://session`：运行中的会话、使用过的 context、工具轨迹。

Agent 可通过 `ls/tree/read/find/grep/search` 等文件式操作定位上下文。资源和 session 可生成 L0/L1/L2 分层摘要：abstract、overview、full detail。session commit 后异步抽取长期 memory。

**技术创新**

1. context database，而不是 vector database。
2. 文件系统范式让 agent 先导航，再检索，再深读。
3. session memory self-iteration，把任务轨迹回写为可复用 context。
4. retrieval trajectory 可观察，有助于 debugging。

**重点难点**

- 目录语义维护成本高。
- L0/L1/L2 摘要质量成为上游依赖。
- session commit 的 memory extraction 可能写入错误经验。
- 多用户 / 多 agent namespace 和权限边界复杂。

**未来方向**

OpenViking 的方向适合作为 context-core 的工作面。未来最关键不是再加检索算法，而是 write policy、correction log、memory diff、failure replay 和 namespace isolation。

### 17. Letta Context Repositories / MemFS

来源：[Letta Context Repositories](https://www.letta.com/blog/context-repositories)、[Letta Code Memory docs](https://docs.letta.com/letta-code/memory/)

**技术判断**

Letta Context Repositories 把 memory 从 API block 进一步推到 git-backed filesystem。它的核心洞察是：coding agent 已经会用本地文件、bash、git、subagents；因此 memory 应该变成 agent 可用这些工具直接管理的 repo。

**工作机制**

MemFS / context repository 是一个 git-backed markdown filesystem，克隆到本地 `~/.letta/agents/<agent-id>/memory`。文件树和 frontmatter description 作为 progressive disclosure 的导航面。`system/` 目录中的文件始终完整注入 system prompt，其他文件只暴露树和描述，按需读取。

它还支持：

- sleep-time reflection subagents。
- memory initialization。
- memory defragmentation。
- git worktree 并发处理历史轨迹。
- commit message 记录 memory 变化。

**技术创新**

1. git 作为 memory versioning / conflict resolution layer。
2. progressive disclosure 由目录结构和 frontmatter 承担。
3. memory swarm：多个 subagents 并发处理不同历史切片，再合并到主 memory。
4. agent 可直接重构自己的 memory hierarchy。

**重点难点**

- agent 自编辑 memory 可能重构出坏层级。
- git conflict 解决并不等于语义冲突解决。
- `system/` pinned context 如果膨胀，会损害 prompt caching 和注意力。
- sleep-time reflection 仍可能生成错误经验。

**未来方向**

Context repositories 很适合成为 coding-agent context-core 的主形态。下一步应加 memory lint、semantic diff、source episode backpointer、eval-driven defragmentation。

### 18. Claude Managed Agents Memory

来源：[Built-in memory for Claude Managed Agents](https://claude.com/blog/claude-managed-agents-memory)

**技术判断**

这套系统的 context 层判断非常清楚：memory 应该挂载到 filesystem，因为 agent 已经擅长用 bash 和 code execution 处理文件。相比黑盒 memory API，文件式 memory 更可导出、可审计、可管理。

**工作机制**

Memory 以 files 形式保存。开发者可以通过 API 管理、导出、回滚和 redaction。它支持 scoped permissions 和 audit logs。stores 可跨 agent 共享，也可按 org / user / agent 设置不同读写权限。

**技术创新**

- filesystem-based memory 进入生产级 managed agents。
- scoped store 解决不同 agent / user / workspace 的可见性问题。
- audit log 记录哪个 agent、哪个 session 写入了 memory。
- rollback / redaction 将 memory 变成可治理对象。

**重点难点**

- 官方没有完全公开 memory extraction / consolidation 的内部算法。
- 文件式 memory 质量依赖 agent 自己组织文件的能力。
- 多 agent 并发写同一 store 仍有语义冲突风险。

**未来方向**

它证明 filesystem memory 是主流供应商认可的方向。未来值得跟踪 memory consolidation、dreaming、scoped store policy、memory audit UI、cross-agent memory sharing。

## 六、产品化 memory / context layer

### 19. Mem0

来源：[Mem0 Entity-Scoped Memory docs](https://docs.mem0.ai/platform/features/entity-scoped-memory)、[Mem0 CLI docs](https://docs.mem0.ai/platform/cli)

**技术判断**

Mem0 的价值在于把长期 memory 产品化为简单可接入的 API / CLI。它更像 memory-as-a-service，而不是完整 context-core。

**工作机制**

Mem0 支持按 user、agent、app、session / run scope 写入和查询。CLI 支持 add、search、list、update、delete，输出 agent-friendly JSON。entity-scoped memory 用 identifier 和 metadata filters 防止不同用户、agent、app 的记忆混合。

**技术创新**

- entity-scoped memory 是生产系统必须项。
- CLI 面向 agent programmatic consumption。
- 简化 add/search/update/delete lifecycle。

**重点难点**

- 抽象过简单时容易停在 `add/search` API。
- 需要外部 write policy、conflict handling、eval harness。
- memory quality 和 task success 之间的闭环不由 Mem0 本身保证。

**未来方向**

Mem0 应向 write-side policy、memory provenance、conflict-aware retrieval、task-level eval 发展。否则会被更完整的 context-core 吸收为底层 store。

### 20. Zep / Graphiti

来源：[Zep docs](https://help.getzep.com/docs)、[Zep Facts](https://help.getzep.com/v2/facts)、[Graphiti docs](https://help.getzep.com/graphiti/getting-started/welcome)、[Zep paper](https://arxiv.org/abs/2501.13956)

**技术判断**

Zep / Graphiti 是 temporal knowledge graph 路线的代表。它的强项是把 memory 从 chunk recall 升级成实体、关系、事实、有效时间和失效时间。

**工作机制**

Zep 从 chat history 和 business data 构建 user-level 或 group-level knowledge graph。entities 是节点，facts / relationships 是边。新事实会动态更新图；事实 invalidation 会记录 valid / invalid 时间。`memory.get()` 返回面向 prompt 的 context string，`graph.search()` 返回更底层的 nodes / edges。Fact ratings 支持按 use case 过滤低价值 facts。

**技术创新**

- temporal KG 比普通 vector memory 更适合变化事实。
- user graph 与 group graph 区分，接近多人 context 需求。
- fact invalidation 和 fact rating 是治理面雏形。
- Graphiti 支持实时增量更新与 hybrid search。

**重点难点**

- entity resolution 是硬问题。名字、别名、隐含指代、跨 session 身份合并都可能错。
- KG extraction 仍依赖 LLM，存在抽取错误和 schema drift。
- context string 生成仍是黑盒压缩点。

**未来方向**

Graphiti 的下一个关键是 conflict-aware graph ranking、provenance-first fact display、group memory isolation tests、schema evolution。

### 21. Letta memory blocks / context hierarchy

来源：[Letta Stateful Agents](https://docs.letta.com/guides/agents/memory/)、[Letta Context Hierarchy](https://docs.letta.com/guides/agents/context-hierarchy/)、[Letta Core Concepts](https://docs.letta.com/core-concepts)

**技术判断**

Letta 的核心不是普通 memory API，而是让 agent 拥有 self-editing memory。它把 memory blocks 放进上下文窗口，把 archival memory 放到外部检索层，并让 agent 通过工具主动编辑自己的记忆。

**工作机制**

Letta agent 包含 system prompt、memory blocks、messages、tools。Memory blocks 是可编辑字符串，可 attach / detach 到 agent，也可 shared across agents。所有 messages、tool calls、reasoning、memory 都持久化。Context hierarchy 区分：

- memory block：小而重要，常驻上下文。
- file：可读取片段和搜索。
- archival memory：大规模外部存储，可按需查询。

**技术创新**

- self-editing memory。
- core memory / archival memory 分层。
- shared blocks 支持多个 agent 共享 context。
- out-of-context messages 仍可通过 API / tools 取回。

**重点难点**

- agent 自己编辑 memory 可能写入错、删错、泛化错。
- 常驻 blocks 容易膨胀。
- shared blocks 会引入多 agent 污染。

**未来方向**

Letta 的方向应与 MemFS 结合：blocks 处理强常驻 identity / constraints，context repository 处理大规模可版本化经验。

### 22. Cloudflare Session / context blocks

来源：[Cloudflare Sessions docs](https://developers.cloudflare.com/agents/api-reference/sessions/)、[Cloudflare Agent Memory blog](https://blog.cloudflare.com/introducing-agent-memory/)

**技术判断**

Cloudflare 的 context-block 设计值得看，因为它把 session memory 做成持久、树状、可压缩、可搜索的上下文块体系。本文不讨论其 agent SDK，只看 context 机制。

**工作机制**

Session 提供 tree-structured messages、context blocks、compaction、full-text search。context block 有 label、description、content、tokens、maxTokens、writable、isSkill、isSearchable 等属性。系统可生成 `set_context`、`load_context`、`unload_context`、`search_context` 等操作。Compaction 保护 head / tail，把中间消息总结成 overlay，原始消息仍保存在 SQLite。

**技术创新**

- context blocks 把常驻上下文显式化。
- compaction 是 non-destructive overlay，而不是替换原文。
- FTS5 支持 session search。
- writable / searchable / loadable 区分不同上下文行为。

**重点难点**

- context block 仍需要写入治理。
- compaction overlay 的正确性需要验证。
- block 粒度、maxTokens 和加载策略需要 domain tuning。

**未来方向**

它适合作为轻量 context-core primitive：block、search、compaction、overlay。未来应补 provenance、conflict-aware block update 和 replay eval。

## 七、Context 评测前沿

### 23. MemoryAgentBench

来源：[arXiv:2507.05257](https://arxiv.org/abs/2507.05257)、[GitHub](https://github.com/HUST-AI-HYZ/MemoryAgentBench)

**技术判断**

MemoryAgentBench 的价值是把 memory 评测从静态长上下文 QA 改成 incremental multi-turn interaction。它更接近真实 agent：信息不是一次性给全，而是随着多轮交互逐步积累。

**工作机制**

它评测四类能力：

- Accurate Retrieval。
- Test-Time Learning。
- Long-Range Understanding。
- Selective Forgetting / Conflict Resolution。

它重构既有数据集，并新增 EventQA、FactConsolidation，把长文本拆成 chunks 逐轮喂给 memory agent，再多次 query。

**技术创新**

- 评测 memory accumulation，而不是一次性 reading。
- 同一个长历史对应多问题，提高评测效率。
- 同时比较 long-context agents、RAG agents、agentic memory methods。

**重点难点**

- 仍偏对话 / QA，不完全覆盖工具执行和环境状态。
- selective forgetting 仍是当前系统短板。
- 如果没有白盒 trace，难定位写入失败还是检索失败。

**未来方向**

MemoryAgentBench 适合做 context-core 的第一层 sanity check，但需要与 MemConflict、LongMemEval-V2、MemGym 组合。

### 24. StructMemEval

来源：[arXiv:2602.11243](https://arxiv.org/abs/2602.11243)

**技术判断**

StructMemEval 补上了 memory evaluation 的一个盲点：系统不只要记得事实，还要知道该把长期记忆组织成什么结构。

**工作机制**

它测试 agent 是否能形成 ledger、todo、tree 等结构化 memory。已有总结显示，简单 RAG 在组织任务上失败，而 memory agents 在被明确提示结构时表现更好；但模型并不会总是主动识别合适结构。

**技术创新**

- 从 recall 转向 organization。
- 把 memory structure 本身作为评测对象。
- 暴露“模型需要结构提示”的现实。

**重点难点**

- benchmark 的结构类型有限。
- 真实工作中的结构常混合 ledger、decision log、runbook、state machine。
- 结构正确不代表下游任务成功。

**未来方向**

context-core 应提供 task-specific memory schemas，而不是让模型临场发明结构。

### 25. GroupMemBench

来源：[arXiv:2605.14498](https://arxiv.org/abs/2605.14498)

**技术判断**

GroupMemBench 证明多人 memory 不是多个单人 memory 的拼接。当前领先 memory systems 在 group memory 上 collapse，说明 ingestion 抹平了 speaker、audience、belief 和术语差异。

**工作机制**

它用 graph-grounded synthesis pipeline 生成多人对话，控制 reply structure、persona、target audience。查询绑定具体 asker，覆盖六类：multi-hop reasoning、knowledge update、term ambiguity、user-implicit reasoning、temporal reasoning、abstention。

**技术创新**

- 评测 speaker-grounded belief tracking。
- 评测 audience-adapted language。
- 评测 group dynamics，而非 dyadic memory。

**重点难点**

- 当前 strongest system 只有 46.0% average accuracy。
- knowledge update 和 term ambiguity 特别弱。
- BM25 能匹配或超过多数 memory systems，说明复杂 ingestion 可能擦掉关键信号。

**未来方向**

多人 context-core 必须显式建模 user / group / channel / workspace / audience namespace。否则团队 agent 会持续泄漏、串用和误归因。

### 26. LongMemEval-V2

来源：[arXiv:2605.12493](https://arxiv.org/abs/2605.12493)、[Project page](https://xiaowu0162.github.io/longmemeval-v2/)

**技术判断**

LongMemEval-V2 是从 user memory 转向 environment experience memory 的关键信号。它问的不是 agent 是否记得用户事实，而是能否像“有经验的同事”一样懂一个 web environment。

**工作机制**

它包含 451 个 manually curated questions，覆盖五类能力：

- static state recall。
- dynamic state tracking。
- workflow knowledge。
- environment gotchas。
- premise awareness。

历史轨迹最高达 500 trajectories / 115M tokens。评测采用 context gathering formulation：memory system 消费历史轨迹，返回 compact evidence 给下游 QA。

两个重要 baseline：

- AgentRunbook-R：RAG memory，分 raw state observations、events、strategy notes。
- AgentRunbook-C：把 trajectories 存成文件，并调用 coding agent 在 sandbox 中 gather evidence。

**技术创新**

- 直接评测环境经验。
- 引入 accuracy-latency frontier，项目页使用 LAFS Gain 衡量在不同延迟预算下的可达准确率。
- 证明文件 + coding-agent evidence gathering 能超越普通 RAG，但成本高。

**重点难点**

- 451 个问题的覆盖和偏差需要更强验证。
- coding-agent 方法延迟高。
- context gathering 仍和 downstream QA 分离，不能完全代表端到端执行。

**未来方向**

这应成为 context-core 的 north star：把 episode traces 编译成可检索、可验证、低延迟的 environment runbook。

### 27. MemGym

来源：[arXiv:2605.20833](https://arxiv.org/abs/2605.20833)

**技术判断**

MemGym 认为现有 memory benchmarks 太偏 personalized chat，无法迁移到 coding、web navigation、deep research、computer use。它把 memory evaluation 推向 agentic regimes。

**工作机制**

MemGym 统一五个 evaluation tracks，覆盖四类 agentic regimes：

- tool-use dialogue。
- multi-turn deep research search。
- coding。
- computer use。

它报告 memory-isolated scores，试图区分 memory 策略和 reasoning / retrieval / tool-use 能力。为 coding 环境训练 MemRM，用 lightweight reward model 快速评价 compression quality，避免完整 Docker rollout 成本。

**技术创新**

- 把 memory benchmark 放进真实 agent gyms。
- memory-isolated score 是重要方向。
- 用 reward model 降低长 horizon coding memory 评测成本。

**重点难点**

- memory-isolated 仍难完全解耦，因为 memory、retrieval、reasoning 会互相影响。
- reward model 可能学习 benchmark 偏差。
- 多 regime 评测成本很高。

**未来方向**

MemGym 适合成为 context-core 的综合压力测试。未来应加入 write trace、retrieval trace、compression trace，才能做根因诊断。

## 八、横向技术判断

### 1. 两条主路线：保真优先 vs 抽象优先

| 路线 | 代表 | 优势 | 风险 |
|---|---|---|---|
| 保真优先 | MemMachine、CMV、Claude filesystem memory、Letta MemFS | 可追溯、可审计、少丢证据 | 读路径重，噪音多，冲突需治理 |
| 抽象优先 | Memori、ACC、Active Context Compression、Mem-π | 低 token、快、任务状态清晰 | summary drift、伪因果、不可追溯 |

真正稳的 context-core 不会二选一，而是分层：

- raw episode 保真。
- working state 有界。
- semantic memory 结构化。
- runbook / skills 抽象经验。
- 每个抽象层保留 source backpointer。

### 2. 写侧正在超过读侧成为核心战场

过去 context infra 主要问“怎么搜得准”。现在更关键的是：

- 该不该写。
- 写成什么类型。
- 写给谁看。
- 什么时候过期。
- 与旧记忆冲突时谁赢。
- 用户纠正后哪些下游 memory 受影响。

MemRouter、WorldDB、MemConflict、Memory-R2 都说明，write / manage path 已经是前沿主线。

### 3. 文件系统范式正在变成主流工程形态

OpenViking、Letta Context Repositories、Claude Managed Agents memory 都选择 filesystem-like memory。这不是怀旧，而是因为文件系统天然提供：

- hierarchy。
- progressive disclosure。
- diff。
- versioning。
- audit。
- human readability。
- agent-friendly operations。

这对 context-core 很重要：上下文不是 query result，而是可维护资产。

### 4. 环境经验比用户画像更接近 agent systems 的核心价值

用户画像 memory 很直观，但对高价值 agent systems，真正稀缺的是：

- repo 结构和历史坑。
- UI affordance 和状态动态。
- 工具失败模式。
- workflow invariant。
- 人工纠正后的操作策略。
- 多次任务后形成的 runbook。

LongMemEval-V2、MemGym、MementoGUI 都在把评测从 persona memory 推向 environment experience。

### 5. 多人上下文必须显式建模命名空间和 audience

GroupMemBench 显示，如果系统不显式记录 speaker、asker、audience、channel、group、permission，检索得越多反而越容易串用。团队 agent 的 memory 不能只按 semantic similarity 检索。

### 6. 评测必须从 outcome-only 转向 trace-aware

只看最终答案会掩盖四类错误：

- 写入没写对，但模型猜对了。
- 检索没检到，但上下文中有暗示。
- 检索对了，但模型没用好。
- 压缩把关键约束写错了。

未来 context-core eval 必须包含 write log、retrieval set、context assembly、memory diff、state assertions 和 replay。

## 九、Context-Core 的建议架构

结合以上论文和项目，比较稳的 context-core 可以分成八层：

| 层 | 责任 | 对应前沿 |
|---|---|---|
| Raw episode store | 保留原始轨迹、对话、工具结果、截图 / ROI | MemMachine、CMV、MementoGUI |
| Working state | 有界任务状态、当前约束、open items | ACC、Cloudflare context blocks |
| Write gate | 判断哪些信息进入长期上下文 | MemRouter、Memory-R2 |
| Structured memory | semantic triples、temporal KG、profile facts | Memori、Zep/Graphiti |
| Governance layer | conflict、staleness、supersession、provenance、audit | MemConflict、WorldDB、Portable Agent Memory |
| Context filesystem | resources / memory / skills / sessions 的可浏览工作面 | OpenViking、Letta MemFS、Claude filesystem memory |
| Experience layer | runbooks、procedural memory、skills、environment gotchas | From Storage to Experience、LongMemEval-V2 |
| Eval / replay | 任务级回放、trace、failure taxonomy、memory-isolated score | MemoryAgentBench、StructMemEval、GroupMemBench、MemGym |

这套架构的关键是：不要让 summary 成为唯一真实来源。保真层、抽象层、治理层和评测层要同时存在。

## 十、未来发展方向

### 1. 从 memory API 到 context operating layer

未来 context-core 不会只是 `add/search/delete`，而会像一个小型操作系统：

- memory admission。
- state commit。
- snapshot / branch / trim。
- versioning / rollback。
- namespace / permission。
- garbage collection / defragmentation。
- background consolidation。
- replay / trace / eval。

### 2. 从相似度检索到 query-conditioned validity

检索结果不应只按 semantic relevance 排序，还应按：

- temporal validity。
- source authority。
- speaker / audience fit。
- condition applicability。
- correction status。
- confidence。
- privacy scope。

### 3. 从单人 memory 到 group / workspace memory

团队 agent 的 context-core 必须一开始就有 namespace：

- personal memory。
- channel memory。
- project memory。
- organization memory。
- agent-private memory。
- shared procedural memory。

并且每条 memory 都要知道“谁说的、谁知道、谁能看、对谁成立”。

### 4. 从 textual memory 到 multimodal memory

GUI / computer-use agent 会迫使 memory 保存：

- screenshots。
- ROI crops。
- UI state。
- coordinate/action traces。
- visual affordance。
- failure frames。

纯文本 summary 会丢掉大量未来决策所需证据。

### 5. 从 sleep-time summary 到 sleep-time verification

背景反思不能只做总结，还要做：

- source checking。
- contradiction detection。
- duplicate merge。
- stale memory pruning。
- runbook validation。
- eval episode generation。

也就是说，sleep-time compute 的核心应从“整理记忆”升级为“验证和治理记忆”。

### 6. 从 benchmark score 到 context-debugger

未来 builder 真正需要的是 memory observability：

- 这条 memory 从哪个 episode 来。
- 什么时候被谁写入。
- 后来是否被修正。
- 当前 query 为什么召回它。
- 它如何进入 prompt。
- final answer 是否真的使用了它。
- 如果删掉它，任务是否仍成功。

这会把 context-core 从功能层推进到可靠性工程层。

## 十一、对 `context-core` 项目的直接启发

如果要把这轮调研落到一个可展示的 `context-core` 项目，最小但有说服力的方向不是再做一个 memory wrapper，而是做：

1. **Episode-first context store**：保留原始 episode 和工具轨迹，抽象层全部带 source backpointer。
2. **Write gate + memory type**：每次写入必须带 type、scope、confidence、source、expiry、supersedes。
3. **Context filesystem**：用目录承载 resources、memories、runbooks、skills、sessions，支持 progressive disclosure。
4. **Conflict-aware retrieval**：至少支持 dynamic / static / conditional conflict 三类诊断。
5. **Runbook experience layer**：从多次 task trace 中提炼 environment gotchas 和 workflow invariants。
6. **Trace-aware eval harness**：每个 episode 可 replay，输出 write / retrieve / assemble / answer 四段 trace。

最小验证集：

- 30-50 个真实或半真实 episode。
- no-memory / naive RAG / structured context / context-core 四组对比。
- 指标包括 task success、pass^k、cost、latency、wrong write rate、stale recall rate、support evidence hit@k、repeated failure rate。

## 来源清单

### 论文与 benchmark

- [Memory for Autonomous LLM Agents](https://arxiv.org/abs/2603.07670)
- [From Storage to Experience](https://arxiv.org/abs/2605.06716)
- [AI Agents Need Memory Control Over More Context](https://arxiv.org/abs/2601.11653)
- [Active Context Compression](https://arxiv.org/abs/2601.07190)
- [Contextual Memory Virtualisation](https://arxiv.org/abs/2602.22402)
- [Parallel Context Compaction](https://arxiv.org/abs/2605.23296)
- [MemRouter](https://arxiv.org/abs/2605.00356)
- [MemMachine](https://arxiv.org/abs/2604.04853)
- [Memori](https://arxiv.org/abs/2603.19935)
- [MemConflict](https://arxiv.org/abs/2605.20926)
- [WorldDB](https://arxiv.org/abs/2604.18478)
- [Portable Agent Memory](https://arxiv.org/abs/2605.11032)
- [Mem-π](https://arxiv.org/abs/2605.21463)
- [Memory-R2](https://arxiv.org/abs/2605.21768)
- [MementoGUI](https://arxiv.org/abs/2605.18652)
- [MemoryAgentBench](https://arxiv.org/abs/2507.05257)
- [StructMemEval](https://arxiv.org/abs/2602.11243)
- [GroupMemBench](https://arxiv.org/abs/2605.14498)
- [LongMemEval-V2](https://arxiv.org/abs/2605.12493)
- [LongMemEval-V2 project page](https://xiaowu0162.github.io/longmemeval-v2/)
- [MemGym](https://arxiv.org/abs/2605.20833)

### 项目与产品文档

- [OpenViking docs](https://openviking.ai/docs)
- [OpenViking GitHub](https://github.com/volcengine/OpenViking)
- [Letta Context Repositories](https://www.letta.com/blog/context-repositories)
- [Letta Code Memory docs](https://docs.letta.com/letta-code/memory/)
- [Letta Stateful Agents](https://docs.letta.com/guides/agents/memory/)
- [Letta Context Hierarchy](https://docs.letta.com/guides/agents/context-hierarchy/)
- [Letta Context Constitution](https://www.letta.com/blog/context-constitution)
- [Claude Managed Agents Memory](https://claude.com/blog/claude-managed-agents-memory)
- [Mem0 Entity-Scoped Memory](https://docs.mem0.ai/platform/features/entity-scoped-memory)
- [Mem0 CLI](https://docs.mem0.ai/platform/cli)
- [Zep docs](https://help.getzep.com/docs)
- [Zep fact ratings](https://help.getzep.com/v2/facts)
- [Graphiti docs](https://help.getzep.com/graphiti/getting-started/welcome)
- [Zep paper](https://arxiv.org/abs/2501.13956)
- [Cloudflare Sessions](https://developers.cloudflare.com/agents/api-reference/sessions/)
- [Cloudflare Agent Memory](https://blog.cloudflare.com/introducing-agent-memory/)

### 本地知识库

- [Agent Context Infra 前沿调研（2026-05-25）](agent-context-infra-2026-05-25.md)
- [Agent Context Infra 调研报告（2026-05-24）](agent-context-infra-2026-05-24.md)
- [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md)
- [AI 系统产品判断框架](../../frameworks/AI系统产品判断框架.md)
- [volcengine/openviking 仓库地图](volcengine-openviking-repo-map.md)
