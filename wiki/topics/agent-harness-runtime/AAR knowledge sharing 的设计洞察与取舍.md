# AAR knowledge sharing 的设计洞察与取舍

## 摘要

`safety-research/automated-w2s-research` 里的 AAR knowledge sharing，不是一个通用知识管理系统，而是为“少量并行研究 agent 在一个 outcome-gradable 实验环境里持续 hill-climb”这个具体场景定制的共享机制。

它最核心的设计不是“做一个更聪明的检索接口”，而是把共享知识变成 agent 的本地工作面：中心 server 负责持久化 findings 与 snapshot 元数据，worker 周期性把 findings 同步到本地目录，再依靠 agent 自己的 `Read / Glob / Grep` 能力去浏览、比较和引用。与此同时，正式 `result` 会自动带上可下载的 workspace snapshot，用来传递可运行状态，而不只是文字经验。

这套设计的优点是简单、可扩展到多 worker、很贴近真实研究流程。它的代价是检索精度主要依赖 agent 自身能力，知识共享更偏广播式，且很大程度上建立在任务本身高度结构化、指标统一、研究方向相对收敛的前提上。

## 先看它服务的具体场景

分析这套 sharing 设计，必须先把场景钉住。它并不是在解决“开放式研究笔记如何长期积累”的问题，而是在解决下面这类问题：

- 同时运行多个 AAR worker
- 每个 worker 在隔离 sandbox 中独立探索
- 所有 worker 面向同一类研究目标：weak-to-strong generalization
- 评估指标相对统一：`PGR`
- 每个 worker 要在 5 天左右的预算内不断试想法、实现、训练、评估、复盘
- 共享的目的不是长期出版，而是**提高并行探索效率，减少重复踩坑，同时保留可复用的高分实现**

这决定了它的 knowledge sharing 首先是一个**研究协作基础设施问题**，而不是一个面向人类读者的知识产品问题。

## 设计洞察

### 1. 把 knowledge sharing 设计成“同步到本地的工作面”，而不是实时检索服务

这是最强的一点。

AAR 并不主要通过一个远程 search API 去查 knowledge。相反，系统会：

1. 把 findings 存在中心 server
2. worker 周期性调用 `/api/findings/all`
3. 把 findings 落到本地 `shared_findings/*.json`
4. 让 agent 直接在本地文件上做 `Read / Glob / Grep`

这背后的设计直觉是：研究工作里的“找相关内容”往往不是一个清晰 query，而更像浏览、对比、联想、回看上下文。远程 keyword search 要求 agent 先知道自己要搜什么，而本地工作面允许它像人类研究者翻资料一样探索。

在这个场景里，这比做一个更花哨的 MCP 检索工具更贴合任务。

### 2. 把共享对象拆成两层：`Finding` 和 `snapshot`

他们没有把所有共享都压成一种对象。

- `Finding` 负责传递：
  - 发现了什么
  - 指标如何
  - 采用了什么配置
  - 属于哪类 finding（`result` / `hypothesis` / `insight` / `error`）
- `snapshot` 负责传递：
  - 当时的 workspace 代码与状态
  - 哪些文件值得回查
  - 如何让其他 worker 真正下载并接着做

这说明他们清楚区分了两种不同共享需求：

- **认知共享**：我学到了什么
- **执行共享**：我具体是怎么做到的

如果只有 finding，没有 snapshot，别的 worker 很难真正继承成果。如果只有 snapshot，没有 finding，别的 worker 又不知道为什么值得下载。两层一起才构成完整 sharing 面。

### 3. 让“什么值得共享”服从实验纪律，而不是完全自由发帖

`share_finding` 并不是完全无门槛的论坛发帖。

最典型的约束是：

- `finding_type="result"` 必须要求至少 5 个随机种子
- 有 metrics 的 `result` 才会自动创建 snapshot，并进入 leaderboard 体系

这说明他们把 knowledge sharing 同时当成一种**实验秩序维护机制**。

在这个场景里，共享不是越多越好，而是要避免：

- 单次偶然高分被误当成可靠进展
- worker 因低质量结果而被噪音带偏
- 论坛沦为没有筛选的随手日志

所以它不是一个中立知识库，而是一个带研究纪律的 sharing 系统。

### 4. 中心 server 主要负责持久化、索引与协调，不直接替 agent 做认知工作

这个系统里的 server 很重要，但它不是“中央大脑”。

server 负责：

- 存储 `Finding`
- 暴露 `/api/findings/all`、`/api/findings/share`、`/api/snapshots/*`
- 提供 leaderboard
- 记录 snapshot 元数据

但真正的检索、比较、引用，仍主要发生在 agent 的本地工作面中。这意味着它在架构上更像：

- **薄协调层**
- **厚本地工作面**

这很适合他们的并行研究场景，因为每个 worker 都需要保持较强自治性，而不是不断回到中心服务请求“下一步该看什么”。

### 5. 结构化的不是正文本身，而是 sharing envelope

他们的 `Finding` 结构看起来很强 schema，但真正结构化得最厉害的，其实是正文外面的 envelope：

- `finding_type`
- `idea_uid`
- `run_id`
- `dataset`
- `weak_model`
- `strong_model`
- `pgr`
- `num_seeds`
- `commit_id`
- `files_snapshot`

而 `content/summary` 仍然是自由文本。

这说明他们的目标不是把研究表达强行模板化，而是让系统知道：这条内容处在什么实验上下文里、能不能进 leaderboard、有没有对应 snapshot、值不值得其他 worker 消费。

这对高度结构化实验环境非常有效。

## 关键取舍

### 1. 选择“全量拉取 + 本地 JSON 文件”，而不是增量同步或复杂检索

这是一个非常务实的取舍。

优点：

- 实现简单
- 调试容易
- worker 端几乎不需要复杂状态
- 本地文件天然兼容 Claude 的通用 file tools

代价：

- `/api/findings/all` 是广播式、全量式，不够精细
- findings 多了以后会变吵
- 去重主要依赖本地文件名和 `id`
- 没有真正的增量订阅或路由机制

但在他们的具体场景里，这个代价是可接受的。因为并行 worker 数并不大，运行时间虽长，但知识共享的总规模仍处在“几百条 findings 以内依然可管理”的区间。

### 2. 选择“依赖 agent 自己检索”，而不是给专门 retrieval tool

这带来两个效果。

优点：

- agent 可以更自由地浏览和联想
- 避免 retrieval API 把问题空间压窄成关键词匹配
- 更接近真实研究者的文档工作流

代价：

- 检索质量更依赖 agent 本身是否会读、会搜、会比较
- 共享内容多了以后，agent 可能漏看重要 findings
- 没有显式的 reranker、召回、去噪机制

这个取舍成立的前提是：作者相信当前模型在文件工作面上的 agentic 浏览能力，已经足以胜过窄接口检索。这是一个很具体、也很场景化的工程判断。

### 3. 选择“workspace snapshot”这种粗粒度复用，而不是 patch / diff 级复用

`snapshot` 直接上传整个 workspace 的压缩包。

优点：

- 最简单可靠
- 复用时不需要还原复杂依赖关系
- 别的 worker 下载下来就能看完整上下文
- 非常适合研究中“这个思路到底怎么实现的”这种问题

代价：

- 粒度很粗，体积更大
- 容易把与核心思路无关的上下文一并带过去
- 复用更像“参考一整套工作区”，而不是“继承一小段精炼改动”

但对研究任务来说，这个粗粒度反而有优势。因为 research idea 的可迁移部分，常常不只是几行 patch，而是代码、配置、缓存假设、日志解读一起构成的工作上下文。

### 4. 选择强实验 schema，而不是开放式知识模型

`Finding` 的字段设计之所以这么结构化，是因为它面对的是：

- 单一问题域
- 统一指标体系
- 明确的实验配置
- 需要 leaderboard 排序

优点：

- 可比较性强
- 可以自动排序、筛选、展示结果
- 方便约束 result 的质量门槛

代价：

- 更依赖任务域
- 不适合承接开放式、多主题、长时间跨度的研究笔记
- 对“模糊但重要”的洞察不够友好

所以不能把这套 schema 直接提升成通用知识库范式。它首先是一个**实验研究系统的数据结构**。

### 5. 选择共享促进交叉授粉，但接受一定程度的探索收敛风险

他们想解决的是 parallel AAR 完全隔离导致的重复劳动，所以引入 findings 与 snapshot 共享。

优点：

- worker 能更快知道哪些方向不值得继续
- 高价值结果能被快速复用
- 可以减少平行重复实验

代价：

- 共享本身会推动 worker 向少数 promising 方向收敛
- 可能增加 herd behavior
- 如果共享面过强，反而会损失探索多样性

所以他们一边共享，一边又通过“给不同 worker 不同 research direction”来对冲 entropy collapse。这说明 knowledge sharing 不是孤立设计，而是和整个并行探索策略绑在一起的。

## 为什么这些取舍在这个场景下成立

把上面的设计放回具体环境里看，会更清楚。

这套 sharing 成立，依赖几个前提：

1. **研究问题相对集中**
   所有 worker 都在 weak-to-strong 这个总问题下工作，彼此 findings 的可复用性本来就高。

2. **评估指标统一**
   `PGR` 提供了很强的共享排序依据，所以系统能较自然地区分 result 和非 result。

3. **共享对象规模可控**
   worker 数量和 findings 数量都没有大到必须上复杂检索基础设施。

4. **agent 已经具备基本文件浏览能力**
   否则“同步到本地再靠 agent 自搜”就会退化成噪音堆。

5. **目标是研究效率，不是知识出版**
   所以他们优先优化 cross-pollination，而不是长期可读性、冲突保留或人类读者体验。

## 不应过度泛化的地方

如果把这套设计借到别的系统里，有几处必须小心。

### 1. 它不天然适合开放式研究知识库

公共知识库往往面对：

- 更异构的来源
- 更模糊的结论边界
- 没有统一指标
- 多主题并存
- 冲突需要被保留而不是被压平

这些都和 AAR 的实验场景不同。

### 2. 它的结构化程度来自任务本身，而不是抽象上的“更先进”

AAR 的 schema 不是普适真理，而是 weak-to-strong 实验环境给出来的自然结果。

### 3. 它优化的是“并行研究 worker 的复用效率”

而不是“长期知识沉淀的张力保留”。如果直接照搬到公共知识库，可能会过度偏向 result、排序和收敛，而牺牲探索期的模糊信号。

## 压缩成一句话

AAR knowledge sharing 的核心洞察是：**在高度结构化、可判分的自动化研究环境里，最有效的共享方式未必是更强的在线检索，而是把共享知识同步成 agent 的本地工作面，并把“认知发现”和“可运行状态”分层保存。**

它的核心取舍是：用简单广播、自由本地检索和粗粒度 snapshot，换取足够好的 cross-pollination 速度；并接受这套机制更依赖统一任务、统一指标与较小共享规模的现实约束。

## 来源依据

- [safety-research/automated-w2s-research 仓库地图](safety-research-automated-w2s-research-repo-map.md)
- [Automated Weak-to-Strong Researcher](automated-weak-to-strong-researcher.md)
- `w2s_research/research_loop/agent.py`
- `w2s_research/research_loop/prompt.jinja2`
- `w2s_research/research_loop/tools/findings_sync.py`
- `w2s_research/research_loop/tools/server_api_tools.py`
- `w2s_research/research_loop/tools/prior_work_tools.py`
- `w2s_research/web_ui/backend/app.py`
- `w2s_research/web_ui/backend/models.py`
- `w2s_research/infrastructure/s3_utils.py`

## 相关页面

- [Automated Weak-to-Strong Researcher](automated-weak-to-strong-researcher.md)
- [AI 自演化研究 Harness](ai-self-evolution-research-harnesses.md)
- [safety-research/automated-w2s-research 仓库地图](safety-research-automated-w2s-research-repo-map.md)
- [代码库作为知识来源](codebases-as-knowledge-sources.md)
