# 索引

维护层说明见 [README.md](README.md)。

## 知识

- [知识总览](knowledge/README.md)
- [Harness Engineering(约束壳工程)](knowledge/harness-engineering.md): 记录围绕 agent 工作的流程控制、并行协作、独立验证,以及"补偿面会移动"的核心判断。
- [AI 自演化研究 Harness](knowledge/ai-self-evolution-research-harnesses.md): 总结 ASI-Evolve 如何把 AI 研究收束成带检索、门控、分阶段评估与分析回写的闭环。
- [Automated Weak-to-Strong Researcher](knowledge/automated-weak-to-strong-researcher.md): 总结一套自动化 alignment researcher 如何在 weak-to-strong supervision 上并行 hill-climb,并暴露出 reward hacking 与"评测设计比脚手架更关键"的问题。
- [AI 时代大厂打工人的五条路](knowledge/AI 时代大厂打工人的五条路.md): 总结 AI 时代职业发展的核心判断(离开中间层)与五条路径(离模型近、离用户近、经营者视角、组织内转型、小修小补)。
- [AI 焦虑的三种形态与行动解法](knowledge/AI 焦虑的三种形态与行动解法.md): 把常见 AI 焦虑拆成身份、资源与信息三种结构,并给出更偏行动与注意力管理的应对方式。
- [AI 让我们重新开始享受自己的职业](knowledge/AI 让我们重新开始享受自己的职业.md): 把职业拆成机械劳动与判断劳动的 spectrum,主张 AI 的更深影响不是提速,而是把工业化分工挤掉的判断时间还给从业者。
- [AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First](knowledge/AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md): 用模型/协议/运行时/契约四层结构解释 AI 产品开发的真实难点,并把工程安全感从过程控制转向结果验证。
- [AI 产品六层与 L3-L6 能力分层](knowledge/AI 产品六层与 L3-L6 能力分层.md): 用"AI-assisted building vs AI runtime" 的区分,把 AI 应用拆成六层,并把人的能力拆成从 consumer 到 architect 的四档。
- [AI 产业分层地图](knowledge/AI产业分层地图.md): 把 AI 市场理解成"算力/模型/推理训练基础设施/数据与运行时基础设施/通用应用/部门型工作流/垂直行业"的分层结构,并补入截至 2026-04-23 的融资、企业支出与应用格局。
- [AI 产业的付钱地图](knowledge/AI产业的付钱地图.md): 从"谁在为 AI 产业出钱"切入,把平台公司、传统 VC、企业 VC、Growth 资本、国家资本与大企业采购方放进同一张图,解释不同出钱方在看哪些层、为什么出钱。
- [AI 时代的投资与生存法则](knowledge/AI 时代的投资与生存法则.md): 从 Indigo 一场分享里提炼 `taste`、事件/结构/解释三层、`Rewired Index`、Harness 创业机会与中间层挤压等一组宏观判断。
- [Taste：感受良质的能力](knowledge/Taste：感受良质的能力.md): 把 `taste` 从消费偏好改写为对 `quality` 的分辨力,并说明 AI 时代最稀缺的部分正从执行转向质量判断。
- [coding agent 的上下文压缩工作流](knowledge/coding agent 的上下文压缩工作流.md): 总结复杂代码库里围绕上下文预算管理形成的一套 research / plan / implement 工作流。
- [AAR knowledge sharing 的设计洞察与取舍](knowledge/AAR knowledge sharing 的设计洞察与取舍.md): 总结 Automated Weak-to-Strong Researcher 中 knowledge sharing 的场景约束、核心洞察与关键取舍,强调它为何适合并行且可判分的研究环境。
- [AI Architect Lens](knowledge/ai-architect-lens.md): 总结这套课程如何把"先定义高价值问题与 OKRs,再让 AI 实现"的思路变成产品架构方法。
- [GenAI 的共识边界与任务委托框架](knowledge/GenAI 的共识边界与任务委托框架.md): 把大语言模型收束为"压缩共识"的机器,并给出一套判断哪些任务该交给 AI、哪些判断必须留给人的委托框架。
- [AI Architect 的 Context Intelligence 镜头](knowledge/ai-architect-context-intelligence.md): 把这套课程推进到 `Digital Twin` 与个人记忆系统设计,强调 agentic retrieval、访问边界与评测先行。
- [AI Architect 的 Proactive Intelligence 镜头](knowledge/ai-architect-proactive-intelligence.md): 把 AI 从响应式助手推进到围绕长期目标持续观察世界的 proactive agent,强调 `background.md`、`Two-Stage Scan` 与判断质量 OKR。
- [AI Architect 的 Advanced Architecture 镜头](knowledge/ai-architect-advanced-architecture.md): 总结这套课程如何把可跑 MVP 升级成更稳的系统,覆盖 `Context Debugger`、多模型编排、上下文隔离、fallback 与身份认证。
- [AI 知识系统的产品定义信念](knowledge/ai-knowledge-systems-product-definition-beliefs.md): 用 AI Architect Lens 反推 `context-infrastructure` 与 `llm-wiki` 各自真正定义的产品问题。
- [Thin Harness, Fat Skills](knowledge/thin-harness-fat-skills.md): Garry Tan 的 AI agent 架构理念--智能推到 skill 层,执行推到确定性工具层,中间 harness 保持最薄。
- [Claude Code:较厚的 agentic coding harness](knowledge/claude-code-harness.md): 总结 Claude Code 如何把 agent loop、permissions、checkpoints、memory、subagents 与扩展面整合成更厚的默认工作流。
- [Claude Code、Codex 与 pi 的 harness 对比](knowledge/coding-agent-harness-comparison.md): 比较三类 coding agent harness 在默认壳厚度、可观察性、内建功能与外置能力上的不同取舍。
- [本地知识库模式](knowledge/local-knowledge-base-patterns.md): 比较 `llm-wiki` 与 `context infrastructure`,说明它们如何分别承载外部知识与个人判断。
- [Pi coding agent:一种极简且可观察的 coding harness](knowledge/pi-coding-agent-harness.md): 总结 `pi` 如何用极简 prompt、少量工具与强可观察性,反过来质疑 plan mode、MCP、后台 bash 与内建 sub-agent 的必要性。
- [grapeot/context-infrastructure 仓库地图](knowledge/grapeot-context-infrastructure-repo-map.md): 对 `grapeot/context-infrastructure` 的第一版仓库地图,覆盖架构、证据锚点与关键工程机制。
- [Pre-PMF 验证手册](knowledge/pre-pmf-validation-playbook.md): 提炼 AI 初创在 PMF 之前围绕 ICP、关键路径、信号质量、校准与 Go / No-Go 的阶段化验证框架。
- [衰退期的创业环境与技术判断](knowledge/衰退期的创业环境与技术判断.md): 把 downturn 重新解释成风险定价回归商业本质的阶段,并比较 AI、blockchain 与 XR 的技术成熟度判断。
- [科学与技艺双层认知模型](knowledge/science-and-craft-cognitive-model.md): 区分需要理论与框架的方向层工作,以及需要练习与反馈的执行层工作。
- [Auto-Research时代的算力霸权与博士分化](knowledge/Auto-Research时代的算力霸权与博士分化.md): 分析自动化研究如何将科研的决定因素从智力转向算力,并加剧博士路径的内部分化。
- [badlogic/pi-mono 仓库地图](knowledge/badlogic-pi-mono-repo-map.md): `badlogic/pi-mono` 的第一版仓库地图,聚焦主题"coding agent 架构与工程实践"。
- [multica-ai/multica 仓库地图](knowledge/multica-ai-multica-repo-map.md): `multica-ai/multica` 的第一版仓库地图,聚焦主题"多设备 agent 访问与运行时工作面"。
- [openclaw/openclaw 仓库地图](knowledge/openclaw-openclaw-repo-map.md): `openclaw/openclaw` 的第一版仓库地图,聚焦主题"个人 AI assistant、Gateway 与持续身份层"。
- [Agent 时代的人机交互新命题](knowledge/agent时代的人机交互新命题.md): 从两篇文章提炼 agent 时代 HCI 的两个联动变化--人在 loop 中的位置后移,UI 从预制产品变成运行时生成的判断界面。
- [EvoMap:Agent 互联网与集体潜意识](knowledge/EvoMap-Agent 互联网与集体潜意识.md): 总结 EvoMap 平台如何用 GEP-A2A 协议实现 Agent 之间的经验传承,避免重复试错,发布 4 天达到 12 万个 Agent 资产。
- [Agent 复利工作模式](knowledge/agent 复利工作模式.md): 从复利数学题出发,说明 Agent 工作如何通过本地文件、规则文件、迭代积累实现从 30% 到 10 倍的效率提升。
- [Bakery:iOS 端远程开发 APP](knowledge/Bakery-iOS端远程开发APP.md): 让开发者在 iPhone 上实时连接、编写、测试 iOS 应用的工具--核心洞察是 iOS App 的空间性体验无法从代码 diff 中获取。
- [Slock:人机协作平台](knowledge/Slock-人机协作平台.md): humans 和 AI agents 在 channels/DMs 中协作的平台--agents 作为队友而非工具,持久记忆、用户机器执行、always-on。
- [ReflexioAI/reflexio 仓库地图](knowledge/reflexioai-reflexio-repo-map.md): `ReflexioAI/reflexio` 的第一版仓库地图,覆盖架构、证据锚点与关键工程机制。
- [Agentic Design Patterns](knowledge/agentic-design-patterns.md): AI Agent 设计模式实践指南,补充知识库中 Agent 相关主题的实践视角。
- [真本事:从会工作到会赚钱](knowledge/真本事-从会工作到会赚钱.md): 大厂高管转型创业的经验总结--批判优绩主义、个人价值公式(了解市场+打造产品+利用杠杆)、道天地将法职业选择框架、主体思维vs客体思维。与Naval框架高度呼应。
- [增长工程师的职业押注与面试叙事](knowledge/增长工程师的职业押注与面试叙事.md): 从一位 OpenAI 增长工程师的访谈中提炼职业押注、end-to-end ownership 与面试故事组织方式。
- [高级岗位简历的三条写法原则](knowledge/高级岗位简历的三条写法原则.md): 把中高级候选人的简历写法收束成厉害、取舍、align 三条原则。
- [Databricks 的人才态度与双向选择](knowledge/Databricks 的人才态度与双向选择.md): 从一场 Databricks 招聘访谈中提炼高增长公司如何看 fit、risk、reference 与双向选择。
- [Agent 岗位JD抽样与能力信号](knowledge/Agent岗位JD抽样与能力信号.md): 基于 2026-05-13 一轮公开招聘页抽样，整理 OpenAI、Anthropic、Cursor、Cohere、Sierra、Harvey 等公司在 agent / harness / eval / context / deployment 相关岗位上的共同能力要求。
- [Go to Market Multiple Times:把高价值工作与早期产品反复推向市场](knowledge/go-to-market-multiple-times.md): 把多次 go to market 收束成一套可复用工作法,用来放大高价值工作,并验证早期产品与 PMF 假设。
- [gogo:本地 llm-wiki 桌面应用](knowledge/gogo.md): 当前公开仓库 `gogo` 的维护页,明确它是本地 `llm-wiki` 桌面工作台原型,不再承担公共知识库产品主语。
- [Ace the Data Science Interview](knowledge/ace-the-data-science-interview.md): 数据科学面试准备指南,覆盖概率、统计、机器学习、产品感知、行为面试等核心模块。
- [纳瓦尔宝典](knowledge/纳瓦尔宝典.md): Naval Ravikant 多年推特、播客、采访精华合集,深度拆解财富创造(Specific Knowledge + Accountability + Leverage)与幸福本质(和平而非快乐、欲望即不幸福契约)。
- [Naval 的 Mental Models](knowledge/naval-mental-models.md): Naval 列出的十个核心 mental models(Evolution、Inversion、Complexity Theory、Principal-Agent Problem 等)及其使用方式--作为"压缩指针"调用底层经验。
- [概率论入门](knowledge/概率论入门.md): Feller 经典概率论教材,数据科学与机器学习的理论基础。
- [求职范式转变:让工作找到你](knowledge/求职范式转变：让工作找到你.md): 总结 tech 求职从海投转向 profile-market fit、market presence 与 use leverage 的逻辑。
- [线性代数正确入门](knowledge/线性代数正确入门.md): Axler 经典线性代数教材,以抽象向量空间为核心,避开行列式优先的传统路径。
- [如何了解一个人](knowledge/如何了解一个人.md): 戴维·布鲁克斯关于深度人际连接的探索,区分"简历美德"与"悼词美德"。
- [喜欢与擅长的命运飞轮](knowledge/喜欢与擅长的命运飞轮.md): 把"命"重写成成功概率与个人适配参数的问题,强调喜欢=低摩擦、擅长=高回报,两者形成长期放大努力的飞轮。
- [网球的内心游戏](knowledge/网球的内心游戏.md): Gallwey 经典著作,提出 Self 1/Self 2 框架--内心游戏对抗注意力涣散、紧张、自我怀疑,核心是放下评判、信任 Self 2、专注当下。
- [safety-research/automated-w2s-research 仓库地图](knowledge/safety-research-automated-w2s-research-repo-map.md): `safety-research/automated-w2s-research` 的第一版仓库地图,聚焦主题"自动化 alignment research harness 与 weak-to-strong 监督"。
- [alchaincyf/nuwa-skill 仓库地图](knowledge/alchaincyf-nuwa-skill-repo-map.md): `alchaincyf/nuwa-skill` 的第一版仓库地图,覆盖架构、证据锚点与关键工程机制。
- [refactoringhq/tolaria 仓库地图](knowledge/refactoringhq-tolaria-repo-map.md): `refactoringhq/tolaria` 的第一版仓库地图，覆盖架构、证据锚点与关键工程机制。
- [LuliYanng/Nono-Cowork 仓库地图](knowledge/luliyanng-nono-cowork-repo-map.md): `LuliYanng/Nono-Cowork` 的第一版仓库地图，覆盖架构、证据锚点与关键工程机制。
- [volcengine/openviking 仓库地图](knowledge/volcengine-openviking-repo-map.md): `volcengine/openviking` 的第一版仓库地图，聚焦面向 AI Agent 的 context database、`viking://` 虚拟文件系统、L0/L1/L2 分层、session memory 与 server/CLI/bot 运行面。
- [yvonnegladwellstack/yvskills 仓库地图](knowledge/yvonnegladwellstack-yvskills-repo-map.md): `yvonnegladwellstack/yvskills` 的第一版仓库地图，覆盖架构、证据锚点与关键工程机制。

## 自我

- [自我总览](self/README.md)
- [职业转型观察](self/career-transition-observation.md): 一条低置信度观察,指出当身份与生计纠缠在一起时,分阶段行动能缓解瘫痪感。
- [工作面摩擦敏感观察](self/工作面摩擦敏感观察.md): 一条中低置信度观察,指出你对同一项知识工作被拆散在多个界面之间的摩擦敏感,并倾向把它们收束到一个更自然的默认工作面。
- [用户自主性优先产品取舍观察](self/用户自主性优先产品取舍观察.md): 一条中低置信度观察,指出当产品需要在"更强接管"与"保留用户自主性"之间取舍时,你倾向优先保留用户的选择权、可替换性和对底层机制的可见性。
- [聚焦优先于通用观察](self/聚焦优先于通用观察.md): 一条中置信度观察,指出在面对"要不要支持更多场景"时,你倾向守住明确边界并做到好用,而不是追求更广覆盖但每个场景都半吊子。
- [抽象框架优先写作观察](self/abstraction-first-writing-observation.md): 一条低置信度观察,指出你在桥接长文中倾向先寻找统一 framing,再回头展开比较与一般化结论。
- [开箱即用洞察优先产品观察](self/开箱即用洞察优先产品观察.md): 一条低置信度观察,指出你在做知识系统产品定义时,倾向优先追求部署第一天就能出现的 insight 与 magic。
- [研究知识系统中的反共识写回观察](self/研究知识系统中的反共识写回观察.md): 一条低置信度观察,指出你在研究知识产品里非常警惕"只会产出共识"的失败模式,并倾向保留高价值问答写回链路来承接反共识判断。
- [产品判断力与能力焦虑分离观察](self/产品判断力与能力焦虑分离观察.md): 一条低置信度观察,指出你容易把"做不出完整系统"和"没有产品判断力"绑定,从而过早否定自己洞察的价值;同一讨论中暴露的纠偏能力本身证明了产品判断力的存在。
- [知识库公开分享的阻力降低观察](self/知识库公开分享的阻力降低观察.md): 一条中置信度观察,指出如果知识库本身就是公开的,分享阻力就消失了--无需额外写博客、无需维护网站,日常积累自动成为作品集。这更接近 oh-share-it 可以扩展的产品方向。
- [自由与当下的观察](self/自由与当下的观察.md): 从两篇随笔提炼的核心洞察--自由=当下、念头=想要=记忆、二维坐标系(Ease vs Alignment)、飞跃到三维观察者视角、与 Self 3 的呼应。
- [物理模型抽象人生问题观察](self/物理模型抽象人生问题观察.md): 一条低置信度观察,指出你在思考人生问题时倾向于引入物理/数学模型作为抽象框架(磁通量、向量分析、余弦相似度)。
- [职业决策与求职策略观察](self/职业决策与求职策略观察.md): 一条中置信度观察,记录不读博选择工作的决策依据,以及求职策略从投简历转向推销自己的转变。
- [公共知识库实践启发他人写作观察](self/公共知识库实践启发他人写作观察.md): 一条中置信度观察,记录本知识库的实践启发鸭哥写成《团队中共享AI Skills的原则与方法》,表明产品判断被领域专家认可。
- [Go to Market 策略](self/go-to-market-strategy.md): 找到高价值工作的策略、历程与迭代记录--资产盘点、兴趣假设、ICP定义、关键路径、展示策略、信号定义。

## 框架

- [框架总览](frameworks/README.md)
- [框架路由入口](frameworks/router.md): `frameworks/` 的默认入口页,先按问题类型把 query 路由到最相关的判断框架,再进入 `knowledge/` 或具体 `bridges/`。
- [让 query 真正调用判断框架](frameworks/让query真正调用判断框架.md): 解释为什么当前 query 容易停留在相关页总结层,并给出从"内容检索器"升级为"框架激活器"的一版最小优化路径。
- [知识系统判断框架](frameworks/知识系统判断框架.md): 收束默认工作面、知识编译 vs 判断蒸馏、`frameworks/` vs `bridges/`、human reuse 等高频判断。
- [研究判断框架](frameworks/研究判断框架.md): 收束 research onboarding、方向筛选、反共识写回、公共层边界与评测重点。
- [AI 系统产品判断框架](frameworks/AI系统产品判断框架.md): 收束 AI-assisted building vs AI runtime、runtime / contract 黑洞、共识任务边界与 agent 复杂度取舍。
- [Harness 架构判断框架](frameworks/Harness架构判断框架.md): 收束补偿面移动、latent vs deterministic、厚壳 vs 薄壳、上下文预算、subagent 的上下文隔离作用与 skill/tool 分工。
- [产品定义判断框架](frameworks/产品定义判断框架.md): 收束高价值问题先行、`Product Definition Brief`、最小但仍然像 magic 的 MVP、用途与边界先于技术栈等产品定义判断。
- [产品验证判断框架](frameworks/产品验证判断框架.md): 收束 `ICP × 场景 × 解决方案`、关键路径、强/弱/噪音信号、多轮 `go to market` 与单变量校准。
- [职业判断框架](frameworks/职业判断框架.md): 收束离开中间层、`profile-market fit`、经营者视角、工资流 vs 资产与选择权等职业判断。
- [职业信号与叙事框架](frameworks/职业信号与叙事框架.md): 收束 `profile-market fit`、简历画像设计、面试故事重写、多信号 hiring 与双向选择。
- [方向与执行判断框架](frameworks/方向与执行判断框架.md): 收束方向层 vs 执行层、`Science` vs `Craft`、何时该继续想、何时该尽快进入反馈回路。
- [AI 产业与投资判断框架](frameworks/AI产业与投资判断框架.md): 收束事件/结构/解释三层、技术分层 vs 付钱分层、`theme` vs `core holding`、`Harness` 创业带与行业哑铃结构。

## 桥接

- [桥接总览](bridges/README.md)
- [知识库运行模型](bridges/knowledge-base-operating-model.md): 这个仓库自己的架构性约束,说明如何把外部知识、个人证据、框架层与混合分析分层保存,又在回答时重新组合。
- [信息复利系统设计框架](bridges/information-compounding-systems-design.md): 从 `llm-wiki` 与 `context-infrastructure` 抽出通用设计准则,进一步讨论如何设计新的信息复利系统。
- [被持续委托的工作主体](bridges/被持续委托的工作主体.md): 分析"同一个被持续委托的工作主体"这个概念的本质、今天的 agent 产品还差在哪,以及 `clawhouse` 可以优先桥接哪些 gap。
- [multica 与 clawhouse 的目标与核心价值差异](bridges/multica与clawhouse的目标与核心价值差异.md): 对照两者真正优化的系统:前者更像团队级 managed agents 平台,后者更像个人多设备场景下的 agent 工作台。
- [Naval财富框架应用于求职困境](bridges/Naval财富框架应用于求职困境.md): 结合Naval的财富原则(出卖时间 vs specific knowledge、Principal-Agent Problem、Hourly Rate本质)分析求职困境--为什么刷简历是Agent路径、如何走"做东西让市场看到你"的Principal路径。
- [传统职业路径与Naval路径的投资模型](bridges/传统职业路径与Naval路径的投资模型.md): 把两条路径形式化成"人力资本折现模型"与"自有资产+选择权模型",澄清它们在投资标的、索取权结构、收益分布与复利机制上的本质差异。
- [自我表达、Specific Knowledge与市场价值之间的桥梁](bridges/自我表达、Specific Knowledge与市场价值之间的桥梁.md): 说明为什么真实表达本身不会自动变成市场价值,并把桥接过程收束成"表达→能力→场景→信号→交易"的链路。
- [Barytes GitHub项目与Agent层次评估](bridges/Barytes-GitHub项目与Agent层次评估.md): 基于公开 GitHub 证据、公开招聘 JD 与本库的 L3-L6 /职业信号框架,评估当前 agent 履历所处层次,补入“当前匹配 / 部分匹配 / 暂不匹配”的投递分层,并给出从早期 L5 走向更强 L5/L6 的补强路径。
- [Anthropic与OpenAI的Agent Systems履历North Star](bridges/Anthropic与OpenAI的Agent Systems履历North Star.md): 从两类顶尖 JD 倒推目标履历画像,并把当前公开履历与 `context / harness / eval / deployment / reliability` 这组 north star 做成差距表。
- [Agent Systems Engineer职业定位](bridges/Agent Systems Engineer职业定位.md): 把“不是用 AI build product,而是围绕 context / harness / evaluation / reliability 做更深一层 agent 系统”的职业主线压成一页对外与对内都可复用的定位说明。
- [Agent 系统求职与项目路线图（2026-05）](bridges/Agent系统求职与项目路线图-2026-05.md): 把 gogo、oh-share-it、my-little-agent-loop、clawhouse、行业学习、求职和博弈论支线收束到同一个 agent systems 证据包路线图。
- [Agent 系统月度执行计划（2026-05-24）](bridges/Agent系统月度执行计划-2026-05-24.md): 将一个月内把 context-core、oh-share-it、my-little-agent-loop 打成简历级旗舰项目的目标拆成四周执行计划,并将 gogo 降级为既有展示入口。
- [Agent Context Infra 调研报告（2026-05-24）](bridges/agent-context-infra-2026-05-24.md): 按研究现状与工程产品/开源项目地图梳理 agent context infra,覆盖 memory 机制、评测迁移、协议/runtime/memory/context database 分层、缺口与 builder 机会。
- [oh-share-it 公共知识库产品](bridges/oh-share-it公共知识库产品.md): 将原先混在 gogo 名字下的公共知识库方向独立出来,定义多人知识治理、联邦同步、公共池聚合与 agent-facing capability layer。
- [课题组公共知识库的产品定义信念](bridges/课题组公共知识库的产品定义信念.md): 把课题组公共知识库明确定位成研究判断基础设施,定义它真正想解决的四个核心问题、五条价值主张与一版 build-oriented OKR。
- [课题组公共知识库的架构风险与分层设计](bridges/课题组公共知识库的架构风险与分层设计.md): 收束公共知识库在多用户治理、上下文窗口、token 成本上的三类核心风险,拆解其共同根因,并给出一版更稳的页面分层、关系模型与仓库架构。
- [课题组公共知识库的联邦架构设计](bridges/课题组公共知识库的联邦架构设计.md): 把部署策略从中心化改为联邦式,每人本地跑完整 RAG + Agent,服务器只做 Git 同步仓,token 成本分散且无需后端服务。
- [什么是公共知识库应该共享的公共知识](bridges/什么是公共知识库应该共享的公共知识.md): 从更本质的问题切入,重新拆解公共知识库中的两类问题:高噪音数据的信号蒸馏,与原始材料的 raw/wiki 关联建模,指出当前架构困难来自两类问题的混合而非单一表示选择。
- [Tolaria 综合分析](bridges/Tolaria 综合分析.md): 把 Tolaria 的产品定位、开源仓库实践、顶层结构、MCP 路线与对 gogo-app 的启发收束成一个总页，作为后续查看 Tolaria 的主入口。
- [公共知识库、Reflexio 与 EvoMap 的对比分析](bridges/公共知识库、Reflexio与EvoMap的对比分析.md): 三方对比分析--认知知识(人可读、保留张力)、操作知识(Agent 执行、解决冲突)、执行知识(百万 Agent、自然选择验证),提炼公共知识库可借鉴的机制。
- [Superlinear 社区 Agent Skill 知识治理信号](bridges/Superlinear社区AgentSkill知识治理信号.md): 从社区求助帖提炼的市场信号--多人协作下的 Agent Skill 知识库更像知识治理问题,而不是单纯的文档整理。
- [团队中共享 AI Skills 的原则与方法](knowledge/superlinear-team-skill-sharing.md): 鸭哥 Context Infrastructure 续篇--共享池+个人INDEX+baseline+heartbeat+review,四部件解决团队skill个性化与积累的矛盾。
- [多人协作知识治理(含 routed context):对外一页纸](bridges/多人协作AgentSkill知识治理-对外一页纸.md): 把"多人共享知识如何分层、保留冲突并在使用时路由"的信号压缩成可外联的一页产品定义信念,并附 2 周 Pre-PMF 冲刺的过线标准与每日最小动作。
- [课题组公共研究知识库的产品化与评测策略](bridges/lab-research-knowledge-base-product-strategy.md): 结合 AI Architect 的 context intelligence 镜头,讨论这套 `raw -> wiki` 架构如何走向课题组公共产品,以及该怎样写第一版评测与 OKR。
- [代码库作为知识来源](bridges/codebases-as-knowledge-sources.md): 说明如何把代码仓库当作证据源来提炼可迁移工程实践,而不是把实现噪音直接灌进 wiki。
- [Clawhouse:多设备 Agent 上下文同步](bridges/clawhouse-多设备-agent-工作台.md): 记录 clawhouse 如何同步和恢复不同设备间的动静态上下文,让人可以在任何设备上继续跟 agent 协作。
- [Go to Yourself 框架](bridges/go-to-yourself-框架.md): 用物理模型（质量通量、余弦相似度）重新审视“向内”与“向外”的策略选择，提出 Go to Yourself 作为比 Go to Market 更优的根本策略。
- [Pulse：有呼吸感的项目工作台](bridges/Pulse-有呼吸感的项目工作台.md): 一个新产品设想——项目作为主语、agent 退到幕后的移动端优先项目工作台，核心意象是项目有呼吸感、对话是树、时间胶囊冻结与解冻、极简美学。

### 桥接长文(essays)

已完成或接近完成的桥接长文,可用于公开发表:

- [从Andrej Karpathy的LLM Wiki和鸭哥的context infrastructure看信息复利系统的设计](bridges/essays/从Andrej Karpathy的LLM Wiki和鸭哥的context infrastructure看信息复利系统的设计.md): 把 `llm-wiki` 与 `context-infrastructure` 放进同一个"信息复利系统"框架,比较它们面对的数据分布、目标函数与蒸馏层次。
- [给自己做了一个 llm-wiki 的入口应用](bridges/essays/给自己做了一个llm-wiki的入口应用.md): 面向公开分享的 gogo app 介绍稿，解释它作为本地 `llm-wiki` 入口的动机、设计原则和反思。
- [课题组公共知识库:让知识产生复利](bridges/essays/课题组公共知识库-博客草稿.md): 基于 oh-share-it 产品设计写的博客草稿--四个核心问题、联邦架构设计、知识复利机制、与 EvoMap / Reflexio 对比。可用于公开发表。

更多见 [bridges/essays/README.md](bridges/essays/README.md)。

## 最近工作

摄取、查询与维护历史见 [log.md](log.md)。
