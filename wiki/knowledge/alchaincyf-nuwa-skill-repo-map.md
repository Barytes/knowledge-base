# alchaincyf/nuwa-skill 仓库地图

## 摘要

这页是围绕主题“仓库架构与工程实践”维护的 `alchaincyf/nuwa-skill` 第一版增强版仓库地图。

在继续下钻 `references/` 与 `SKILL.md` 之后，这个仓库的真实形态已经更清楚了：它不是一个以 Python 实现为中心的传统工具仓库，而是一个**把“蒸馏某个人的思维方式”外化成 Claude Code skill 协议、方法论文件、模板与示例语料库的 meta-skill 仓库**。

它真正发布的不是一段算法代码，而是一套可复制的 distillation workflow：如何把公开人物的材料拆成多路调研、如何判断某个观点能否升格为“心智模型”、怎样把这些材料组装成可运行的 `SKILL.md`，以及怎样用验证与后置精炼降低“角色扮演味太重、认知框架太浅、过度编造”的风险。

当前置信度已经从“顶层结构图”提高到“方法论与工作流层”，但仍没有逐个 example 或脚本实现细读。因此它足以回答“女娲到底在蒸馏什么、靠什么机制保证质量”，还不足以裁定每个辅助脚本的具体鲁棒性。

## 仓库目的

- README 的公开定位非常明确：不是复制人，而是蒸馏任何人的思维方式，把公开材料提炼成可运行的人物 perspective skill。
- 这个定位通过 `SKILL.md` 被进一步具体化：目标不是捕捉 `WHAT they said`，而是提取 `HOW they think`，也就是一套“认知操作系统”。
- 观察时默认分支：`main`
- 主要语言：`Python`
- 仓库地址：https://github.com/alchaincyf/nuwa-skill

从 README、`SKILL.md` 与 `references/` 看，仓库最核心的产品承诺可以压成三层：

1. **蒸馏对象的重写**：从“同事做什么”转向“强者怎么想”。
2. **输出物的重写**：从静态人物总结转向可运行的 perspective skill。
3. **实现方式的重写**：不是单次 prompt，而是一整条分阶段、可复查、带验证门的 research-to-skill pipeline。

## 架构地图

### 顶层目录

- `assets`
- `examples`
- `references`
- `scripts`

### 顶层文件

- `6-agents-parallel.png`
- `LICENSE`
- `README.md`
- `README_EN.md`
- `README_ES.md`
- `README_JA.md`
- `README_KO.md`
- `SKILL.md`
- `advisory-board.png`
- `cover-distill-minds.png`
- `wechat-qrcode.jpg`
- `x-thread-en.md`

### 第一版子系统角色判断

- `SKILL.md` 不是普通说明文档，而是**女娲本体**：它把入口分流、目录创建、6-agent 调研、提炼、构建、验证、双-agent 精炼都写成可执行的 skill contract。
- `references/extraction-framework.md` 是方法论约束层，回答“什么才算心智模型”“矛盾如何处理”“信息不足时怎么办”。
- `references/skill-template.md` 是产物模板层，把最终人物 skill 的结构标准化成一份骨架。
- `scripts/` 是辅助操作层，用于字幕下载、transcript 清洗、调研摘要合并与质量检查。
- `examples/` 是证据与分发层。它不是装饰性 demo，而是在仓库内部保存完整调研文件与生成结果，用来证明流程不是空谈；同时 README 又把这些 example 对应到各自独立仓库，形成“母 skill 生成子 skill”的分发策略。
- 多语言 `README_*` 与 `assets/` 说明这个仓库同时承担了**方法论发布页**和**技能分发入口**的角色。

### 执行流的第一版理解

1. 用户给出明确人物，或只给模糊需求。
2. `SKILL.md` 先走入口分流：直接蒸馏，或先诊断推荐最合适的蒸馏对象/主题。
3. 系统创建一个自包含的 skill 目录，要求所有调研结果都写回 skill 目录内部，而不是散落在外部工作区。
4. 6 个并行 subagent 按信息维度采集资料，并把结果分别写入 `references/research/01-06.md`。
5. 主流程读取 `references/extraction-framework.md`，对候选观点做三重验证，筛出心智模型、决策启发式、表达 DNA、价值观张力与诚实边界。
6. 再读取 `references/skill-template.md`，把提炼结果组装为可运行的目标 `SKILL.md`。
7. Phase 4 用已知问题、边缘问题与 voice test 验证，Phase 5 再做一次双-agent 精炼。
8. 最终产物既可以留在本地 `.claude/skills/` 中，也可以像 README 展示的那样被发布成独立 skill 仓库。

## 机制清单

### 把“蒸馏对象”从行为习惯重写为认知操作系统

- README 与 `SKILL.md` 都反复强调：女娲提炼的不是“这个人说过什么”，而是“这个人如何思考、如何判断、什么绝不会做、哪里有边界”。
- README 明确把输出层拆成五层：表达 DNA、心智模型、决策启发式、反模式/价值底线、诚实边界。
- 这控制的是“人物 skill 退化成语录复读机或角色扮演模仿秀”的失败模式。
- 代价是蒸馏难度显著提高：你不再能靠表层风格和金句堆出一个看起来像的 skill，而必须做跨材料、跨场景的框架归纳。

### 用双入口设计把“想蒸馏谁”也纳入 skill 的工作范围

- `SKILL.md` 的 Phase 0 明确分成两条路径：
  - 直接路径：用户已给出明确人物/主题
  - 诊断路径：用户只有困惑，需要先推荐候选视角
- 这控制的是“用户根本不知道该调用哪个 perspective skill”时的冷启动问题。
- 代价是 skill 不只是生成器，还要承担一定的顾问职责；这让前置判断更主观，也更依赖推荐质量。

### 用 6 路并行 research decomposition 外化信息采集面

- `SKILL.md` 把调研硬拆成六类：著作、长对话、表达 DNA、他者视角、决策记录、时间线。
- 每个 subagent 都被要求把结果写入固定文件，例如 `01-writings.md` 到 `06-timeline.md`。
- 这控制的是“资料混成一锅、事后很难回看哪条判断来自什么证据面”的失败模式。
- 代价是流程更重，也更依赖有足够丰富的公开材料可供 6 个维度并行取证。对冷门人物，这个架构天然会更吃力。

### 用“调研结果必须写回 skill 目录”保证产物自包含

- `SKILL.md` 在 Phase 0.5 里明确要求：所有调研文件必须存在 skill 目录内部的 `references/research/`，不得散落在外部目录。
- 这控制的是“skill 可运行，但其证据与上下文留在作者私有工作区，无法复制或开源分发”的失败模式。
- 它其实是一个很强的 packaging decision：skill 不是 prompt 片段，而是一个可迁移的最小知识包。
- 代价是仓库结构更重，单个 skill 的目录会同时承载 prompt、证据、脚本与来源文件，不像只发一个 `SKILL.md` 那么轻。

### 用信息源优先级与黑名单控制蒸馏噪声

- `SKILL.md` 明确规定信息源优先级：用户提供的一手素材最高，其次是本人著作、长对话、实际决策记录，再到社交媒体、他人评价和二手转述。
- 同时还显式拉黑知乎、微信公众号、百度百科等来源。
- 这控制的是“二手洗稿材料太多，导致蒸馏出的不是人物思维，而是互联网对这个人物的共识幻觉”。
- 代价是调研过程更保守，也更依赖高质量原始材料是否存在；如果人物公开材料本就稀缺，最终 skill 会更常落入“诚实但不完整”的状态。

### 用“三重验证”区分心智模型和随口观点

- `references/extraction-framework.md` 是整个提炼层最关键的机制文件。
- 它要求一个候选观点只有同时通过三重验证，才能升格为心智模型：
  - 跨域复现：至少在两个不同领域出现
  - 有生成力：能推断此人对新问题的可能立场
  - 有排他性：不是所有聪明人都会这样想
- 只过 1 重则降级为决策启发式，0 重则丢弃。
- 这控制的是“把一时观点误判为稳定框架”的失败模式。
- 代价是产出会变少，也会更偏向抽象度高、复现率强的人物；某些靠直觉或特定语境驱动的人，可能更难被漂亮地蒸馏。

### 把矛盾当作人格深度，而不是数据脏点

- `references/extraction-framework.md` 明确提出三种矛盾：时间性矛盾、领域性矛盾、本质性张力。
- 处理原则不是调和，而是保留并标注：早期与近期、不同场景的不同规则、价值观之间的内在拉扯。
- 这控制的是“为了让人物 skill 看起来一致，就把复杂人格压平成平滑品牌”的失败模式。
- 代价是最终 skill 可能不够整齐、不够爽快，甚至会让用户觉得“这个人怎么前后不一”。但这恰恰更接近真实人物。

### 用诚实边界把“会什么”和“不会什么”一起产品化

- README 和 `SKILL.md` 都把诚实边界放在显眼位置：无法捕捉直觉、无法覆盖调研时间点之后的变化、公开表达不等于真实想法。
- `SKILL.md` 甚至规定信息不足时的处理：标注推测、降低置信度、并列呈现矛盾、尊重沉默。
- 这控制的是“人物 skill 因为风格太强而被误用为万能顾问”的失败模式。
- 代价是产品魅力会下降一点，因为最迷人的幻觉通常来自“它好像真的是那个人”。女娲选择牺牲一部分魔法感，换更可信的使用边界。

### 用 Agentic Protocol 让生成出来的 skill 不只“像”，还“会做事”

- `SKILL.md` 在 Phase 3 里最有意思的机制，不是普通的模板填充，而是要求为目标人物自动生成一段“回答工作流（Agentic Protocol）”。
- 这段 protocol 要求：
  - 先判断问题是否需要事实研究
  - 如需要，先做 [人物名] 式研究
  - 研究维度必须从蒸馏出的心智模型反推，而不是套通用搜索模板
- 这控制的是“最终人物 skill 只有语气，没有研究动作”的失败模式，也是在避免模型遇到具体事实题时只靠预训练记忆硬编。
- 代价是模板变得更复杂，且生成质量取决于 Phase 2 的模型提炼是否真的抓住了这个人的分析偏好。

### 用多重检查点和后置精炼把大 workflow 拆成可纠偏的阶段

- `SKILL.md` 在 Phase 1.5 和 Phase 2.5 都设置了 review checkpoint，要求在调研完成和提炼完成后先暂停展示摘要，让用户确认再继续。
- Phase 4 再做三种验证：
  - 已知测试
  - 边缘测试
  - 风格测试
- Phase 5 还会并行启动两个 agent 做后置精炼，其中一个借用了 `darwin-skill` 的评估思想。
- 这控制的是“前面方向错了，却一路写完整个 SKILL.md 才发现返工”的失败模式。
- 代价是整个流程明显更厚、更慢，也更像研究 harness，而不是一句 prompt 即时生成。

### 用 examples 把方法论变成可审计证据，而不只停在宣称层

- README 不只是说“我们蒸馏了很多人”，还明确把 `examples/` 作为透明调研档案展示出来。
- 从 `examples/steve-jobs-perspective/` 的树看，example 里确实包含最终 `SKILL.md`、完整的 `references/research/01-06.md`，以及 demo conversation。
- 这控制的是“仓库只给方法论口号，却不给足够证据让人判断流程是否真的跑通”的失败模式。
- 代价是仓库更像出版物 + 证据库的混合体，维护成本高于一个只发布 skill contract 的极简仓库。

## 蒸馏理念与方法论总结

### 蒸馏理念

从 `README.md`、`SKILL.md` 与 `references/` 交叉看，女娲的蒸馏理念大致可以压成五句：

1. **蒸馏的对象是思维框架，不是语录。**
2. **好的人物 skill 是一套可运行的认知操作系统，而不是人格 cosplay。**
3. **独特性来自排他性的心智模型与未被抹平的内在张力。**
4. **可靠性来自诚实边界，而不是全知幻觉。**
5. **真正有价值的最终产物，是让用户“用另一个人的眼睛看自己的问题”。**

### 方法论主线

它的方法论不是“多搜一些资料”这么简单，而是一个明确的 research-to-distillation pipeline：

- **输入重写**：人物名或模糊需求都可以成为入口
- **证据分解**：把信息源拆到 6 个研究维度
- **证据写回**：每个维度都必须落文件
- **框架筛选**：三重验证把候选论点分层
- **人格保真**：矛盾不被抹平，边界必须明写
- **模板组装**：用 `skill-template.md` 固化最终输出结构
- **行为化输出**：为目标人物生成 Agentic Protocol，让 skill 具备研究与回答流程
- **验证与精炼**：用已知问题、未知问题和风格测试做门控，再做一轮结构优化

从 repo 角度看，这个仓库最值得研究的，不是“怎么写一个 skill prompt”，而是**如何把一种主观且容易失真的蒸馏任务，外化成多阶段、带证据文件、带验证门和后置精炼的 workflow**。

## 证据锚点

- Snapshot 来源：[github-repo-alchaincyf-nuwa-skill.md](../../raw/external/github-repo-alchaincyf-nuwa-skill.md)
- 仓库：`alchaincyf/nuwa-skill`
- 观察分支：`main`
- 解析到的 commit：`25bb2dec3befb43611911f2dee2adb725da43a56`

值得回查的关键文件与路径：

- `README.md`
- `SKILL.md`
- `references/extraction-framework.md`
- `references/skill-template.md`
- `scripts/download_subtitles.sh`
- `scripts/srt_to_transcript.py`
- `scripts/merge_research.py`
- `scripts/quality_check.py`
- `examples/steve-jobs-perspective/SKILL.md`
- `examples/steve-jobs-perspective/references/research/01-writings.md`
- `examples/steve-jobs-perspective/references/research/02-conversations.md`
- `examples/steve-jobs-perspective/references/research/03-expression-dna.md`
- `examples/steve-jobs-perspective/references/research/04-external-views.md`
- `examples/steve-jobs-perspective/references/research/05-decisions.md`
- `examples/steve-jobs-perspective/references/research/06-timeline.md`
- `examples/steve-jobs-perspective/references/demo-conversation-2026-04-05.md`

## 开放问题

- `scripts/quality_check.py` 里的 6 项或更多检查，到底只是格式 lint，还是已经能对“像不像这个人”做更强结构化判断？
- `scripts/merge_research.py` 与 examples 里的 research 文件，是否真的形成了稳定的 research artifact contract，还是主要仍依赖主 skill 的文本约束？
- README 里“40+ primary sources”“6 agents parallel”的宣称，是否在所有 example 中都被一致落实，还是不同人物间差异很大？
- 主题 skill 与人物 skill 虽然在方法论上被区分开了，但模板复用到什么程度、什么时候会失真，仍需要进一步回读 `examples/x-mastery-mentor/` 才能判断。
- 这套 workflow 高度依赖公开材料丰富度。对缺乏长文、长访谈或系统著作的人物，它还能否稳定产出有区分度的 skill？

## 来源依据

- [仓库 snapshot](../../raw/external/github-repo-alchaincyf-nuwa-skill.md)

## 相关页面

- [代码库作为知识来源](../bridges/codebases-as-knowledge-sources.md)
- [Agent 复利工作模式](agent 复利工作模式.md)
- [公共知识库、Reflexio 与 EvoMap 的对比分析](../bridges/公共知识库、Reflexio与EvoMap的对比分析.md)
