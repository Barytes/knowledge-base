# Google DeepMind 多智能体安全资金池

这条 2026-06-11 的资金池信号把 agent safety 从单个模型或单个 agent 的行为，推进到多主体系统、协议、runtime、真实沙盒和可回放评测层。

**日期：** 2026-06-12
**标签：** multi-agent safety，agent safety，A2A，Concordia，sandbox evaluation，AI safety funding

## 这条新闻是什么

Cooperative AI Foundation 官网在 2026-06-11 列出一条 `$10m Funding Call Launched with Schmidt Sciences, Google DeepMind, and ARIA`。结合用户提供的 MIT Technology Review 摘要，这个资金池由 Google DeepMind、Schmidt Sciences、英国 ARIA、Cooperative AI Foundation 和 Google.org 共同支持，目标是资助研究者研究大量 AI agent 彼此交互时可能出现的风险。

这不是一般意义上的“AI safety 又拿了一笔钱”。更准确地说，它把安全问题从单个模型或单个 agent 的行为，推进到多主体系统层：

- 很多 agent 会在不同组织、平台、协议和权限环境里互相通信。
- 单个 agent 看起来安全，不代表它进入市场、协议、博弈和委托网络之后仍然安全。
- 风险不只来自一个模型“想坏事”，也来自多个 agent 的错配、反馈环、串谋、竞争和被攻击面放大。

## 已核对来源

- Cooperative AI Foundation 首页把这次 `$10m Funding Call` 列为 2026-06-11 最新 blog 条目，并列出 Schmidt Sciences、Google DeepMind 和 ARIA。
- Cooperative AI Foundation 的技术报告 [Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143) 把多智能体风险概括为三类 failure modes：miscoordination、conflict、collusion；并提出七类 risk factors：信息不对称、网络效应、选择压力、不稳定动态、承诺与信任、涌现 agency、多智能体安全。
- Google Cloud 在 2025-04-09 发布 [Agent2Agent Protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)，明确目标是让不同供应商、不同框架的 agent 能安全通信、交换信息、协调行动。
- Cooperative AI Foundation 记录了 Google DeepMind 的 [Concordia v2.0](https://www.cooperativeai.com/post/google-deepmind-releases-concordia-library-v2-0)，该库用于生成多 actor 环境、multi-agent simulation、games 和 AI evaluations。
- 2024 年的 safety mapping 论文指出，在 Anthropic、Google DeepMind、OpenAI 的公开安全论文中，`multi-agent safety` 属于论文较少、且公司内部短期激励未必足够覆盖的方向之一。

## 为什么现在发生

这条新闻的背景，是 agent 正在从“单个助手”进入“互联生态”。

单 agent 阶段，安全问题主要是：工具权限、提示注入、越权访问、幻觉执行、任务误解、用户是否能接管。

多 agent 阶段，问题形状会变：

1. **错误会通过交互放大。** 一个 agent 的错误判断、恶意输入或被污染上下文，可能通过消息、任务委托和工具调用传递给其他 agent。
2. **安全边界会从模型输出移动到协议和运行时。** 只做模型安全测试不够，还要测试 agent card、身份、授权、任务生命周期、消息内容、工具副作用、审计日志和恢复机制。
3. **现实系统会出现混合动机。** 企业、个人、市场、攻击者、防御者和平台方的目标并不一致。很多风险不是“所有 agent 都坏”，而是各自局部合理的行为组合成系统性坏结果。
4. **可预测性下降。** 当 agent 会学习、适应、谈判、委托、竞争和执行真实动作时，风险来自动态系统，而不只是单次回答质量。

这解释了 Rohin Shah 这类安全研究者为什么会把注意力放到无人监督 agent、大规模 agent 互相听从指令、以及更真实的沙盒环境上。真正的风险对象不是一个聊天框，而是会跨系统行动的 agent population。

## 风险地图

### 1. 诈骗与社会工程

多 agent 会降低大规模定制化诈骗的边际成本。一个 agent 负责画像，一个 agent 负责话术，一个 agent 负责渠道，一个 agent 负责支付或身份流程，最后形成自动化诈骗流水线。

这里的难点不是单条内容能不能被内容安全模型拦住，而是整个任务图是否被识别出来。单步看起来可能都像正常业务。

### 2. Prompt injection 与跨 agent 污染

agent 互相调用后，提示注入会从“用户骗模型”变成“一个系统污染另一个系统”。如果某个 agent 把网页、邮件、文档、issue、agent card 或工具返回当成可信指令，下游 agent 可能继承被污染的目标。

这要求运行时把 instruction、data、tool output、third-party message 明确分层，而不能把所有文本都混进同一个 prompt。

### 3. 网络攻击与自动化攻防循环

多个 agent 可以分工完成侦察、漏洞分析、payload 生成、横向移动、日志规避和社工。防御侧也会用多个安全 agent 做 triage、red/blue/green agent 协作。

这会让攻防速度提高，但也会让误报、过度自动修复、权限误用和自动化升级链条变得更危险。

### 4. 市场串谋与策略性互动

当 agent 代表商家、广告系统、交易方或采购方行动时，风险不只是“犯错”，还包括 tacit collusion、价格协调、操纵排名、规避规则和相互试探。

这类问题不能只用内容安全或模型 refusal 处理。它需要机制设计、审计、市场规则和可回放的交互记录。

### 5. 协同失败与不稳定反馈环

即使所有 agent 都是“好意”的，也可能因为信息不对称、过度自信、重复委托、互相等待、目标描述不一致、局部优化等原因造成系统级事故。

这和本知识库里的 [Harness Engineering（约束壳工程）](harness-engineering.md) 相接：多 agent 不是简单多开几个 worker，而是需要更强的状态、权限、观测和验证结构。

## 对 agent infra 的含义

这条新闻加强了一个判断：agent 安全的主战场会从“模型有没有安全回答”扩展到 `runtime + protocol + evaluation`。

具体会落到几类工程对象：

- **身份与能力声明：** agent card、capability discovery、供应商身份、权限范围。
- **任务生命周期：** 谁发起任务、谁授权、谁能修改目标、什么时候需要人类确认。
- **消息分层：** 用户指令、系统指令、第三方数据、工具返回、agent-to-agent message 不能混成同一种文本。
- **副作用控制：** 支付、发邮件、改代码、删文件、发交易、调用外部 API 需要不同等级的授权与回滚能力。
- **可观测性：** session log、tool trace、inter-agent message、权限使用记录必须可回放。
- **真实沙盒：** 评测不能停在玩具博弈。需要更接近真实 web、文件系统、支付、企业 SaaS、代码执行和通信平台的 sandbox。

这也解释了为什么 Google 一边推动 A2A 这类互联协议，一边又参与资助 multi-agent safety。互联协议会释放生产力，也会把系统性风险前移成必须研究的问题。

## 对行业的判断

从 AI 产业角度看，这是一条结构层信号，不只是事件层新闻。

它说明下一阶段 agent 竞争不只在“谁的单个 agent 更能干”，还在：

- 谁能提供可信 agent runtime
- 谁能定义跨组织 agent 协议
- 谁能做真实环境评测和审计
- 谁能处理多 agent 权限、身份、合规、责任归属
- 谁能把安全从模型补丁做成平台默认能力

这会强化 agent safety / agent observability / agent runtime / protocol governance 这一带的价值。创业或研究机会不一定在训练更大模型，而是在把 agent 放进真实组织和真实网络之后，补上身份、权限、沙盒、评测、审计和恢复层。

## 需要继续追踪

- 资助项目名单：哪些课题被选中，是否偏理论、仿真、网络安全、市场机制、真实沙盒，还是治理。
- Concordia 与其他 sandbox 的演化：是否成为 multi-agent safety 的事实评测底座之一。
- A2A / MCP / AP2 等协议的安全模型：身份、授权、数据边界、支付授权和责任归属如何落地。
- 企业级 agent 平台是否把 multi-agent trace、policy、eval 和 incident review 做成默认能力。
- 是否出现新的 benchmark：不只是单 agent 任务成功率，而是 agent population 的稳定性、抗污染性、抗串谋性和可恢复性。

## 相关页面

- [Google 多智能体安全相关工作与组织人物地图](Google多智能体安全相关工作与组织人物地图.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)
- [Agent 系统作为 OS 与 Cloud Runtime 问题](agent-runtime-os-cloud-runtime.md)
- [EvoMap：Agent 互联网与集体潜意识](EvoMap-Agent%20互联网与集体潜意识.md)
- [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md)
