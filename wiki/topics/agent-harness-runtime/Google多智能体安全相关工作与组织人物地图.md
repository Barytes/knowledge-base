# Google 多智能体安全相关工作与组织人物地图

Google 的多智能体安全资助新闻，应放在一张更大的 agent 生态图里看。

**日期：** 2026-06-12
**标签：** Google DeepMind，multi-agent safety，A2A，Concordia，ARIA，Schmidt Sciences，Cooperative AI Foundation，Google.org

## 结论

这不是一条孤立的 funding news。它更像是 Google 对 agent 时代的两手布局：

1. **推动 agent 进入真实生态。** 通过 Gemini、SIMA、Gemini Robotics、Google Antigravity、A2A、agentic commerce 等工作，把 agent 从单次对话推向浏览器、企业流程、机器人、支付和跨组织协作。
2. **提前补多智能体安全层。** 通过 AGI Safety & Alignment、Frontier Safety Framework、Concordia、DeepSearchQA、multi-agent safety funding call 等工作，把风险对象从“单个模型是否安全”推进到“agent population 是否可预测、可观测、可控制”。

核心判断是：Google 看到的 agent 未来不是一个助手，而是一个由很多组织、很多模型、很多工具和很多权限边界组成的生态。因此安全问题也会从 model safety 扩展到 protocol safety、runtime safety、network safety 和 governance。

## Google 相关工作线

### 1. Google DeepMind：AGI safety 与责任治理

Google DeepMind 的责任与安全页面把其安全工作分成治理、研究和影响三块。它内部有 Responsibility and Safety Council，由 COO Lila Ibrahim 和 VP, Responsibility Helen King 共同主持；AGI Safety Council 由联合创始人兼 Chief AGI Scientist Shane Legg 领导，关注未来强 AGI 系统可能带来的极端风险。

Rohin Shah 领导 Google DeepMind 的 AGI Safety & Alignment team。他个人主页说明，这个团队通过 research 和 policy implementation 为更强 AI 系统的出现做准备。Google DeepMind 2025 年的技术 AGI safety paper 也由 Rohin Shah 领衔，核心风险分类包括 misuse、misalignment、mistakes 和 structural risks。其中 structural risks 指多个个人、组织或 AI 系统互动产生的风险，和这次 multi-agent funding call 直接相接。

重要来源：
- [Responsibility & Safety - Google DeepMind](https://deepmind.google/responsibility-and-safety/)
- [Rohin Shah 个人主页](https://rohinshah.com/)
- [An Approach to Technical AGI Safety and Security](https://arxiv.org/abs/2504.01849)

### 2. Multi-agent safety funding call：把问题从模型推进到 agent population

这次 2026-06-11 的 funding call 由 Cooperative AI Foundation、Schmidt Sciences、Google DeepMind、ARIA 共同宣布，并得到 Google.org 支持，金额最高 1000 万美元。

funding call 的关键设定是：未来会有大量由不同组织构建的 AI agents，在数字环境中互相通信、谈判和交易。现在多数 safety evaluation 仍然把模型孤立评测，但多智能体系统会出现突然的集体行为、能力跃迁、经济活动异常和安全挑战。

资助方向分四类：

- **Sandboxes and testbeds：** 构建真实、可复现的多智能体评测环境，例如虚拟市场、模拟生态、多组织工作流。
- **The science of agent networks：** 研究 agent population 的安全相关性质、集体能力如何涌现、网络如何失败或变得不稳定。
- **Strengthening agent infrastructure：** 压测 identity、reputation、commitment 等跨平台 agent interaction 协议。
- **Oversight and control：** 监测已部署 agent population，并缓解大规模集体伤害。

Cooperative AI Foundation 首页显示，申请截止日期是 2026-08-09 23:59 AoE。

重要来源：
- [Investing in multi-agent AI safety research](https://deepmind.google/blog/investing-in-multi-agent-ai-safety-research/)
- [Cooperative AI Foundation](https://www.cooperativeai.com/)
- [Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143)

### 3. A2A：Google Cloud 推的 agent-to-agent 互联协议

Agent2Agent Protocol（A2A）是 Google Cloud 在 2025-04-09 发布的开放协议，目标是让不同供应商、不同框架中的 agents 能彼此通信、交换信息并协调行动。

A2A 的关键机制包括：

- agent 用 `Agent Card` 声明能力，供其他 agent 发现。
- 任务对象有生命周期，支持长任务状态同步。
- agent 之间可以传递消息、context、artifact 和用户指令。
- 协议强调认证、授权和企业级安全。

这条线是 multi-agent safety 的直接前提。没有 A2A 这类互联协议，多智能体安全更像研究命题；一旦协议进入企业应用，安全问题就变成工程基础设施问题。

重要来源：
- [Announcing the Agent2Agent Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)

### 4. Concordia：多 actor 模拟与评测底座

Concordia 是 Google DeepMind 开源的 generative social simulation 库。它用类似桌面角色扮演游戏的模式，把环境交给 Game Master，把参与者建模为可配置的 entities，用来构造多 actor 环境。

Concordia 的意义是：multi-agent safety 不能只靠经典 Prisoner's Dilemma 或玩具仿真。它需要能快速搭建场景、配置 actor、记录互动、复现实验，并支持 AI safety、ethics、economics、social science 和真实服务模拟。

Google DeepMind 与 Cooperative AI Foundation 的关系在这里也很明显：CAIF 记录了 Concordia v2.0 的发布，并曾围绕 Concordia Contest 做社区活动。

重要来源：
- [google-deepmind/concordia](https://github.com/google-deepmind/concordia)
- [Multi-Actor Generative Artificial Intelligence as a Game Engine](https://arxiv.org/abs/2507.08892)
- [Google DeepMind Releases Concordia Library v2.0](https://www.cooperativeai.com/post/google-deepmind-releases-concordia-library-v2-0)

### 5. SIMA / Gemini Robotics / embodied agents：从虚拟世界走向行动能力

SIMA 2 是 Google DeepMind 的虚拟 3D 世界 agent。它把 Gemini 的推理能力嵌入到能看屏幕、理解目标、执行动作、与用户对话并逐步改进的 agent 中。

这条线和 multi-agent safety 的关系不是“多 agent”本身，而是说明 Google 正在让 agent 从语言输出走向行动。只要 agent 能在虚拟世界、网页、机器人或真实工具中行动，它就需要更强的权限、观测、评测和接管机制。

Google DeepMind 的 models 页面也把 Genie、Gemini Robotics、SIMA 2、Gemini 等放在同一条 “World models & embodied AI / intelligent agents” 线上。

重要来源：
- [SIMA 2: An Agent that Plays, Reasons, and Learns With You in Virtual 3D Worlds](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)
- [About Google DeepMind](https://deepmind.google/about/)

### 6. Evals：从事实性到 agent 长链任务评测

Google DeepMind 的 evals 页面包含 SimpleQA Verified、FACTS、DeepSearchQA 等评测。DeepSearchQA 是一个 900 prompt 的 agent benchmark，用于评估 agent 在复杂、多步骤信息搜索任务中的能力，强调 long-horizon planning 和 context retention。

这说明 Google 的 eval 线已经不只评估模型知道什么，也在评估 agent 能否制定复杂搜索计划、长程保持上下文并完成可验证任务。

重要来源：
- [Evals - Google DeepMind](https://deepmind.google/research/evals/)

### 7. AP2 / agentic commerce：当 agent 开始交易，安全问题变成责任问题

Agent Payments Protocol（AP2）不在这条新闻里，但和 multi-agent safety 高度相关。它处理 agent 代用户购买、支付、授权和责任归属。公开报道显示，AP2 通过 cryptographically signed mandates 试图证明用户授权、真实意图和交易责任。

这条线说明 Google 不是只做 agent 间“聊天协议”，而是在推进 agent 进入交易场景。只要 agent 能交易，multi-agent safety 就必须处理身份、授权、欺诈、prompt injection、重放攻击和责任归属。

重要来源：
- [Axios: Google's new plan to build trust in AI agents as personal shoppers](https://www.axios.com/2025/09/16/google-ai-agents-ecommerce-online-shopping)
- [Whispers of Wealth: Red-Teaming Google's Agent Payments Protocol via Prompt Injection](https://arxiv.org/abs/2601.22569)

## 新闻中的组织

### Google DeepMind

Google DeepMind 是 Alphabet/Google 的前沿 AI 研究与产品实验室，由 DeepMind 与 Google Brain 合并而来。它的公开使命是负责任地构建 AI，使其造福人类。与这条新闻相关的角色是：

- 模型和 agent 能力供给方：Gemini、SIMA、Gemini Robotics、AlphaEvolve 等。
- 安全研究方：AGI Safety & Alignment、Frontier Safety Framework、technical AGI safety paper。
- 评测和沙盒方：Evals、DeepSearchQA、Concordia。
- 议程发起方：multi-agent safety funding call。

重要人物：

- **Demis Hassabis：** Google DeepMind 联合创始人兼 CEO。
- **Shane Legg：** 联合创始人、Chief AGI Scientist，领导 AGI Safety Council。
- **Rohin Shah：** AGI Safety & Alignment team lead，这次新闻里的核心发声者之一。
- **Anca Dragan、Allan Dafoe、Dave Orr：** 据 AGI Safety & Alignment 公开社区说明，他们与 Rohin Shah 一起构成该团队领导层，Shane Legg 是 executive sponsor。
- **Lila Ibrahim、Helen King：** Google DeepMind Responsibility and Safety Council 的共同主持者。
- **Joel Leibo、Edward Hughes、Thore Graepel、Raphael Köster、Manon Revel、Alexander Sasha Vezhnevets：** 与 cooperative AI、多智能体学习、Concordia、multi-agent simulation 或 CAIF 网络有直接交集的 Google DeepMind 研究者。

### Google.org

Google.org 是 Google 的公益/慈善部门。它的定位是把 Google 的资金、项目和技术资源提供给全球组织，帮助推进公共利益方向。它在这次 funding call 里是 supporting party，更像公益资金与社会影响力资源入口，而不是技术主导方。

Google.org 当前公开 focus 包括 Knowledge, Skills & Learning、Scientific Progress 和 Stronger Communities。multi-agent safety 可归入 Scientific Progress 与 safer digital world 的交叉地带。

### Schmidt Sciences

Schmidt Sciences 是 Eric Schmidt 和 Wendy Schmidt 创立的科学慈善组织，支持非常规科学与技术研究。它在这次新闻里的作用是资助和组织独立研究网络。

它有两条与这次 funding call 直接相关的项目线：

- **Science of Trustworthy AI：** 支持 AI 安全基础科学，强调成熟、决策相关的 eval、对 frontier AI 风险的理解、预测和控制。
- **AI Agents：** 支持多 agent 通信与协调研究，目标是观察和测量 inter-agent communication、coordination、protocol stability 和 agent social dynamics。

重要人物：

- **Eric Schmidt、Wendy Schmidt：** 创始人。
- **Stuart Feldman：** President。
- **Mark Greaves：** Vice President，也是 Science of Trustworthy AI advisory board 成员之一。
- **James Fox：** Senior Science Associate，AI & Advanced Computing。新闻摘要里提到他强调研究者需要把 agent 放入更真实的沙盒环境。
- **Mike Belinsky：** Director, AI & Advanced Computing。

### ARIA

ARIA 是英国 Advanced Research and Invention Agency，属于英国政府支持的 moonshot research agency。它在这条新闻里的相关项目是 Scaling Trust，位于 Trust Everything, Everywhere opportunity space。

Scaling Trust 近 5000 万英镑，目标是让 AI agents 能在不可信、高风险、对抗性环境里安全协调、谈判和验证。项目分三条线：

- **Arena：** 开放竞赛平台，测试 AI 系统在数字和物理世界中的多智能体协调能力。
- **Tooling：** 开源协调基础设施。
- **Fundamental research：** 从经验测试走向理论驱动保证，设计新的安全 primitives。

重要人物：

- **Alex Obadia：** Programme Director，曾共同创立 Flashbots，对加密、MEV、分布式系统和信任基础设施有背景。
- **Sarath Murugan：** Programme Specialist。
- **Nicola Greco：** External Technical Advisor，密码学研究与投资背景。
- **Edith-Clare Hall：** Frontier Specialist。

### Cooperative AI Foundation

Cooperative AI Foundation（CAIF）是一个慈善组织，获得 Macroscopic Ventures 1500 万美元慈善承诺支持。它的使命是支持能提升 advanced AI cooperative intelligence 的研究。

它关心的不是“让 AI 更会合作”这么简单，而是 differential progress：希望支持能增加社会福利的合作能力，而不是同样会强化欺骗、操纵、胁迫或压制其他主体的 dual-use capability。

CAIF 是这条 funding call 的自然组织节点，因为它此前已经：

- 发布或参与 [Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143)。
- 做 grants、PhD fellowship、seminar、workshop 和 Concordia 相关活动。
- 形成了包含 Google DeepMind、学术界、治理界和合作 AI 研究者的网络。

重要人物：

- **Lewis Hammond：** Research Director，Multi-Agent Risks 报告核心作者之一。
- **Cecilia Elena Tilli：** Associate Director (Research and Grants)。
- **Chandler Smith：** Research Analyst/Engineer，参与 Concordia 相关材料。
- **Allan Dafoe：** CAIF trustee，Google DeepMind Senior Staff Research Scientist，Centre for the Governance of AI President。
- **Gillian Hadfield：** CAIF trustee，Johns Hopkins 政府、政策与计算机科学方向教授。
- **Thore Graepel：** CAIF trustee，Google DeepMind Distinguished Research Scientist，UCL Chair of Machine Learning，多智能体学习重要研究者。
- **Jesse Clifton：** CAIF trustee，Macroscopic Ventures Grantmaking Officer。
- **Audrey Tang：** CAIF trustee，Taiwan Cyber Ambassador。
- **Joel Leibo、Edward Hughes、Natasha Jaques、Vincent Conitzer、Jakob Foerster、Kate Larson、Noam Brown：** CAIF advisors 或相关合作网络中的关键研究者。

## 新闻中的关键个人

### Rohin Shah

Rohin Shah 是 Google DeepMind AGI Safety & Alignment team lead。研究主题包括 amplified oversight、interpretability、deployment monitoring、dangerous capability evaluations。他在这条新闻中的角色是把 multi-agent safety 解释成产业实验室眼下可能不优先、但外部学术界适合提前研究的问题。

他的更大背景是：从 Berkeley CHAI 到 Alignment Newsletter，再到 Google DeepMind AGI Safety & Alignment。他代表的是 Google DeepMind 内部“前沿模型安全 + alignment + policy implementation”的主线。

### James Fox

James Fox 是 Schmidt Sciences AI & Advanced Computing 的 Senior Science Associate。新闻摘要中他强调研究者需要在更真实的沙盒环境中观察 agent 大规模互动会做什么。这个观点和 Schmidt Sciences 的 AI Agents 项目目标完全一致：构建开放平台，让研究者设计 realistic challenges，测试 multi-agent systems 在复杂、高压环境中如何协作和失效。

### Lewis Hammond

Lewis Hammond 是 CAIF Research Director，也是 Multi-Agent Risks from Advanced AI 的核心作者之一。他代表的是把 multi-agent risk 系统化、taxonomy 化的研究线。

### Thore Graepel

Thore Graepel 是 Google DeepMind Distinguished Research Scientist、UCL Chair of Machine Learning、CAIF trustee。CAIF 表示他是 cooperative AI 领域早期重要论文作者之一，也长期发表 multi-agent learning 相关工作。新闻里若要追踪 Google 与 CAIF 的人员交叉，他是关键节点。

### Joel Leibo

Joel Leibo 是 Google DeepMind 研究者、CAIF advisor，也是 Cooperative AI 早期重要人物之一。他参与了 Concordia 和 multi-agent / social-cognitive capacities 相关工作，是从 DeepMind 多智能体研究传统连接到当前 CAIF 网络的重要人物。

### Allan Dafoe

Allan Dafoe 是 Google DeepMind Senior Staff Research Scientist，也是 CAIF trustee 和 Centre for the Governance of AI President。他连接的是 AI governance、cooperation、frontier AI 风险和机构设计这条线。

### Alex Obadia

Alex Obadia 是 ARIA Scaling Trust 的 Programme Director。他的背景来自 Flashbots 和加密信任基础设施。放在这条新闻里看，他代表的不是传统 AI safety，而是“多主体在对抗环境中如何建立可信协调机制”的工程与机制设计路线。

## 这张网络的真实分工

| 节点 | 主要角色 | 贡献方式 | 目标 |
| --- | --- | --- | --- |
| Google DeepMind | 前沿模型、agent、评测、安全研究实验室 | 发布 funding call、提供研究议程、推进 Concordia / eval / AGI safety | 让更强 agent 和 AGI 系统安全、可控、可部署 |
| Google Cloud | 企业 agent 互联协议推动者 | A2A、企业伙伴生态 | 让不同供应商 agent 能跨系统协作 |
| Google.org | 公益资源与资金支持 | funding、programs、technical expertise | 把 Google 资源用于社会影响 |
| Schmidt Sciences | 科学慈善资助方 | Trustworthy AI、AI Agents、学术/非营利项目资助 | 支持公共品性质的 AI safety science |
| ARIA | UK moonshot agency | Scaling Trust、Arena、Tooling、Fundamental research | 建立 cyber-physical multi-agent coordination 的信任基础设施 |
| CAIF | cooperative AI 研究网络与资助组织 | grants、报告、seminars、fellowships、Concordia 社区 | 推进 advanced AI 的 cooperative intelligence，并控制 dual-use 风险 |

## 对后续追踪的建议

后续不应只追“谁拿到钱”。更重要的是追四类产物：

1. **真实沙盒。** 是否出现标准化的 virtual marketplace、multi-organisation workflow、adversarial arena、agent population simulation。
2. **协议安全。** A2A、AP2、MCP、UCP 是否补出身份、授权、信誉、承诺、审计、回滚和责任归属。
3. **评测指标。** 是否从单 agent 成功率，转向 population-level volatility、collusion resistance、prompt contamination propagation、network failure mode。
4. **治理接口。** 学术研究能否转成企业 agent platform 的默认能力，例如 trace、policy、incident review、human takeover 和 deployment monitoring。

这条新闻的真正价值，是把一个很抽象的问题具体化了：agent 时代的安全边界不再停在模型内部，而会落在 agent 之间的协议、运行时、身份系统、真实沙盒和治理机制上。

## 相关页面

- [Google DeepMind 多智能体安全资金池](Google-DeepMind多智能体安全资金池.md)
- [Agent 系统作为 OS 与 Cloud Runtime 问题](agent-runtime-os-cloud-runtime.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)
- [EvoMap：Agent 互联网与集体潜意识](EvoMap-Agent%20互联网与集体潜意识.md)
