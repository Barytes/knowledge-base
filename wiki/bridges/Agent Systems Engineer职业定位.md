# Agent Systems Engineer 职业定位

## 定位一句话

我想走的不是“用 AI 很快 build 一个 product”的路线，也不是纯粹的 `AI Product Manager` 路线，而是：

**围绕 `agent context / harness / evaluation / reliability`，设计、构建并持续改进可靠 agent 系统的 `Agent Systems Engineer`。**

更具体地说，这个定位关心的是：

- AI 在 runtime 中如何工作，而不是只关心 build-time 如何提速；
- context、knowledge、memory、tool use、workflow、harness 如何被系统性组织；
- agent 如何从 demo 进入更可靠、可评估、可部署的系统；
- evaluation、guardrails、tracing、failure taxonomy、self-improvement loop 如何进入工程闭环。

## 它和常见 `AI Product Manager` / `AI Builder` 的区别

今天很多人说自己在做 AI 产品，实际主语常常是：

- 用 `Cursor` / `Claude Code` / `v0` / `Lovable` 很快做出 demo；
- 用 AI 辅助开发一个产品；
- 做需求、包装、验证、前端和 workflow。

这当然有价值，但门槛在快速下降。

这条定位想走的是更深一层：

| 浅一层 | 深一层 |
|---|---|
| 用 AI build product | 设计 AI product runtime |
| 关注 demo 和功能 | 关注 context、runtime、eval、reliability |
| 把 AI 当开发加速器 | 把 AI 当系统控制层的一部分 |
| 强调原型速度 | 强调系统边界、质量闭环和长期运行 |

所以，这个定位不是“我会用 AI 做产品”，而是：

> **我在做 AI 产品里更难、也更稀缺的那一层：让 agent 系统真正变得可工作、可评估、可演进。**

## 为什么这条线成立

从公开 JD 抽样看，市场真正反复购买的能力，不只是：

- 会调用 LLM API；
- 会接 RAG；
- 会用 `Claude Code` 搓 demo。

更高频出现的是：

- `eval / quality / regression / measurement`
- `runtime / orchestration / execution environment`
- `context / retrieval / memory / ranking`
- `deployment / production / observability`
- `guardrails / auditability / governance`

这说明市场主语已经在从“谁会用 AI 做东西”转向“谁能把 AI 系统做稳”。

因此，这条定位并不是凭空抬高难度，而是在对齐一个真实存在的需求带：

- AI-native startup 在买 `harness / runtime / eval / context layer`；
- 企业和重行业团队在买 `deployment / governance / observability / domain-integrated agent systems`。

## 当前最适合承接这条定位的能力包

这条职业定位最自然对应的能力包是：

1. **context systems**
   - knowledge / context / memory 的组织方式
   - retrieval、routing、grounding、引用边界

2. **agent harness**
   - agent loop
   - tools / prompts / execution environment
   - session / state / orchestration

3. **evaluation 与 reliability**
   - eval dataset
   - judge / scorer
   - regression
   - tracing
   - failure taxonomy
   - guardrails

4. **从 prototype 到系统**
   - 把 demo 推到更稳定、更可部署、更可复用的工程形态

## 当前公开履历和这条定位的关系

现有公开项目已经说明，这条定位不是空想，而是和已有积累相连：

- `gogo`：本地 `llm-wiki` workbench + Pi Agent，说明主语在 `knowledge-base + agent runtime workbench`。
- `oh-share-it`：external context layer，说明主语在 `context sharing / routing`，而不是 generic chatbot。
- `my-little-chating-agent`：tool use + RAG + agent loop，说明已经做过完整的单体 agent 应用原型。

因此，当前最自然的职业叙事不是：

> 我做过几个 AI 项目，也会 RAG，也会 Claude Code。

而是：

> **我的主线不是 generic AI demo，而是 agent systems 里的 `context / knowledge / harness / evaluation` 问题。**

## 需要避免的过度 claim

这条定位成立，不代表现在就该把自己表述成：

- 已经是 production-grade agent 平台 owner；
- 已经是 self-improving agent systems 专家；
- 已经是 staff-level runtime / infra engineer。

更稳的说法是：

> **我已经明确押注 `context / harness / eval / reliability` 这条线，正在把现有作品补成更可靠、更可部署的 agent 系统。**

也就是说：

- `production-grade` 更适合作为正在逼近的目标，而不是已经完全拥有的标签；
- `self-improvement` 更适合作为远期 ambition，而不是当前核心卖点；
- 当前最应该站稳的，是 `Agent Systems Engineer`，而不是更夸张的 “AI Architect / autonomous systems expert”。

## 最适合的岗位画像

这条定位最适合的岗位，不是最泛的 `AI PM`，也不是最硬的 foundation model 训练岗，而是：

1. **Applied AI Engineer**
2. **Agent / Harness / Context Systems Engineer**
3. **AI Deployment / Forward Deployed Engineer**
4. **Research Tools / Knowledge Systems / Workbench Engineer**
5. **偏产品化、偏系统化的 Research Engineer**

这些岗位共同看重的是：

- 对 agent runtime 的理解；
- 对 context / memory / tool use 的判断；
- 对 eval / quality / reliability 的工程意识；
- 把原型推进到系统的能力。

## 对外表达模板

### 一句话版本

> **Agent Systems Engineer，聚焦 `context / harness / evaluation / reliability`，把 agent 从 demo 推向更可靠、可评估的系统。**

### 三句话版本

> 我的主线不是 generic AI demo，而是 agent systems 里的 `context / knowledge / harness` 问题。  
> 我关心 AI 在 runtime 里如何工作，以及 agent 为什么可靠/不可靠。  
> 我想成为能够设计、构建并持续改进可靠 agent 系统的工程师。

### 更保守但稳的版本

> 我正在沿着 `agent context / harness / eval` 这条线发展，目标是成为能设计、构建并持续改进可靠 agent 系统的工程师。

## 下一步最关键的补强方向

这条定位要真正站稳，最需要补的不是更多概念，而是更强的可见证据：

1. 一个旗舰项目
2. 一套 `eval / regression / quality` 机制
3. 更清楚的 `tracing / failure taxonomy / guardrails`
4. 至少一个真实试点或真实使用案例
5. 更直接的 deployment / observability 证据

也就是说，这页定义的是**职业主线**，不是已经完成的终点。

## 当前压缩结论

这条职业定位最核心的区分不是“我也会做 AI 产品”，而是：

> **我想做的是 AI 产品系统层里更深、更稀缺的一段：`context / harness / evaluation / reliability`。**

它和市场需求是对得上的，也和当前公开作品主线是连续的。接下来要做的，不是继续换方向，而是沿这条线把证据补硬。

## 相关页面

- [Agent 岗位JD抽样与能力信号](../knowledge/Agent岗位JD抽样与能力信号.md)
- [Barytes GitHub项目与Agent层次评估](Barytes-GitHub项目与Agent层次评估.md)
- [职业决策与求职策略观察](../self/职业决策与求职策略观察.md)
- [Go to Market 策略](../self/go-to-market-strategy.md)
- [职业信号与叙事框架](../frameworks/职业信号与叙事框架.md)
- [AI 系统产品判断框架](../frameworks/AI系统产品判断框架.md)
