# The Founder's Playbook：AI-native startup 的阶段纪律

**来源：** [The Founder's Playbook: Building an AI-Native Startup](../../../raw/external/the-founders-playbook-2026-05.md)  
**标签：** AI-native startup，founder，Pre-PMF，MVP，Launch，Scale

---

## 核心判断

这份 playbook 的真正增量，不是“Claude 能帮创业者做哪些事”，而是把 AI-native startup 的 founder 工作重新压缩成一句话：

> **AI 改变的是路径速度和组织形态，不是 founder 的判断责任。**

AI 让 research、coding 和 workflow automation 都变得便宜，早期公司可以用极少 headcount 达到过去需要完整团队才能做到的产品和运营能力。但这也带来一个新风险：build 太容易，founder 更容易在证据不足时提前进入执行、扩张和自动化。

所以这份材料和本库已有 [Pre-PMF 验证手册](pre-pmf-validation-playbook.md) 的关系很清楚：Pre-PMF 手册强调验证路径，这份 playbook 强调当 AI 把执行摩擦拿掉后，验证纪律更不能被跳过。

---

## Founder 角色如何变化

材料把 founder role 从 individual contributor 改写成 orchestrator：

- 非技术 founder 可以用 agentic coding 把专业领域知识变成生产软件。
- 技术 founder 可以用 AI 补齐 GTM、财务、文档、运营和战略分析。
- 小团队可以用 AI 在 research、coding、workflow automation 三个面上像更大组织一样运行。

但材料也提醒，这不是 autopilot。founder 的注意力只是上移了：

- 选择要解决什么问题
- 设计证据路径
- 编排 AI agents、tools 和少量团队成员
- 判断什么时候继续、什么时候停、什么时候转向

---

## 四阶段框架

### 1. Idea Stage：先验证问题，再让 Claude Code 写代码

Idea stage 的退出条件是 problem-solution fit。founder 要先确认：

- 问题真实、具体、频繁。
- 有明确人群正在受这个问题影响。
- 当前替代方案不足。
- 方案解决的是验证后暴露出来的真实问题，而不是最初脑补的问题。

这阶段最危险的 AI-native 误区是把 prototype 当验证。Claude Code 可以很快做出看起来像产品的东西，但 prototype 只应该是 customer discovery 的道具。真正证据仍然来自目标用户对问题和方案的真实反应。

材料还强调 confirmation bias 的升级：如果 founder 让 AI 为自己的想法找支持证据，AI 会很快构造一套看似扎实的论证。正确用法是让 AI 做 adversarial research、premortem、竞争分析和 disconfirming evidence search。

### 2. MVP Stage：速度不是唯一变量

MVP stage 不是纯 construction phase，而是从 problem evidence 转向 solution evidence。退出条件是出现早期 PMF 证据：真实用户愿意使用、回来、付费或推荐。

这阶段的新增风险有四个：

- **agentic technical debt**：AI 每轮 session 都能继续写代码，但如果没有 specs、architecture constraints 和 `CLAUDE.md`，结构会慢慢漂移。
- **false PMF**：早期热度、朋友支持、投资人介绍用户、HN spike 等都可能是假阳性。
- **zero-friction scope creep**：功能变得太便宜，每个新功能都显得合理，产品边界反而消失。
- **insecure by inexperience**：AI 生成 functional code，不自动生成 secure code。

它给出的最有用动作是：

- 写 architecture context，再打开 Claude Code。
- 写 scope document，并明确什么用户证据才允许加功能。
- 上线前做 security review。
- 第一批用户到来前定义 activation、retention、Day 7 / Day 30、false positive。
- 用 Sean Ellis test、effort test 和多轮行为数据判断 PMF。

### 3. Launch Stage：从产品成立转向业务可重复

Launch stage 的目标是证明业务可以增长，而不是只证明产品有人喜欢。退出条件包括：

- 增长来自可解释渠道，并有 CAC、LTV、payback period 等单位经济模型。
- 产品能承受 production workload。
- 运营系统不再依赖 founder 亲自处理每个 support、triage、planning 和 reporting。

这阶段的关键变化是 founder 不能继续做所有事情。材料建议先 audit founder 的全部 recurring tasks 和 decisions，再分成：

- 可以完全自动化
- 需要人但不一定需要 founder
- 必须由 founder 判断

这和本库的产品验证框架互补：当 PMF 初步出现后，问题从“这条路径是否成立”转向“这条成立路径能否被系统化、合规化、重复化”。

### 4. Scale Stage：把 domain expertise、data 和 workflow 变成 moat

Scale stage 的目标是公司在 founder 不直接运行 day-to-day operations 时仍能系统增长。材料把退出状态压成三类：

- sustainable profitability
- IPO-readiness
- acquisition

Scale stage 的护城河不只是产品功能，而来自：

- founder domain expertise 被写进产品上下文、skills、playbooks 和 edge-case tests
- 用户行为数据形成反馈飞轮
- workflow integrations 带来 switching cost
- support、compliance、SLA、documentation 和 observability 支撑 enterprise trust

这点对 AI-native startup 很关键：通用 AI 能快速复制浅层功能，但很难复制长期积累的垂直场景知识、用户行为 fingerprint 和工作流嵌入深度。

---

## 对本库框架的增量

这份 playbook 给 [产品验证判断框架](../../frameworks/产品验证判断框架.md) 补了一个 AI-native 版本的警告：

> 当 build 变得极快，验证纪律反而更重要。

过去很多 founder 不验证，是因为急着做；现在是不验证也能立刻做出来。这个变化让旧问题更危险：

- 还没验证 problem-solution fit，就已经有 prototype。
- 还没定义 scope，就已经有十几个功能。
- 还没定义 metrics，就已经有一波 launch traffic。
- 还没定义 architecture，就已经有一套能跑但不可解释的 codebase。

所以 AI-native startup 的默认操作顺序应该更强调：

1. 先写假设。
2. 先写边界。
3. 先写验证指标。
4. 先写架构约束。
5. 再让 agentic coding 放大执行。

---

## 和相关页面的关系

- [Pre-PMF 验证手册](pre-pmf-validation-playbook.md)：提供更一般的验证纪律；本文补充 AI-native startup 中 build 摩擦消失后的新风险。
- [Go to Market Multiple Times](go-to-market-multiple-times.md)：强调反复推出高价值工作；本文把 go-to-market 放进 Idea / MVP / Launch / Scale 的阶段框架。
- [AI 产品六层与 L3-L6 能力分层](AI%20产品六层与%20L3-L6%20能力分层.md)：本文说明 founder 如何用 AI 工具跨越 build-time 与 runtime 能力，但也提醒不能把能 build 误当成产品成立。
- [产品验证判断框架](../../frameworks/产品验证判断框架.md)：本文可作为该框架在 AI-native startup 场景里的应用补充。
