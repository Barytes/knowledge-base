# Anthropic 与 OpenAI 的 Agent Systems 履历 North Star

## 这页回答什么

这页不回答“现在能不能投”，而是回答一个更上位的问题：

> 如果目标是被 `Anthropic`、`OpenAI` 这类顶尖团队以 `agent systems` 相关岗位认真对待，当前履历最终需要长成什么样。

同时，这页也把当前公开履历与该 `north star` 做一版差距对照，避免只停留在抽象方向感。

## 证据口径

这页只基于本仓库已经整理过的公开材料：

- [Agent 岗位JD抽样与能力信号](Agent岗位JD抽样与能力信号.md)
- [Barytes GitHub项目与Agent层次评估](Barytes-GitHub项目与Agent层次评估.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)

不额外引入新的外部来源。

## 从 JD 倒推出来的 north star

把 `Anthropic`、`OpenAI` 以及相邻公司在 `agent infra / harness / eval / deployment / context` 上的 JD 放在一起看，目标画像不是“最会做 demo 的人”，而是：

> **已经拥有过一个可部署、可评估、可迭代的 agent system 的 builder。**

更展开一点，这个画像通常同时成立六件事：

1. **理解并主导过 `context / harness / runtime` 的关键一段**
2. **做过 `evaluation / regression / quality loop`**
3. **有 `deployment / observability / reliability` 的真实证据**
4. **有真实用户或真实团队使用，而不只是本地原型**
5. **能用失败案例驱动系统改进，而不是只做一次性作品**
6. **对 cost、guardrails、安全边界至少有基本工程意识**

压成一句英文，更接近 JD 语言的是：

> **A builder who has owned a reliable agent system end-to-end: context, execution, evaluation, deployment, and iterative quality improvement.**

## 对 Anthropic 与 OpenAI 的两个偏置

两家公司有明显交集，但也各有偏置。

### Anthropic 更偏什么

更强调：

- `evals`
- `harnesses`
- `context engineering`
- `quality`
- `cost optimization`
- `reward hacking avoidance`
- `research tooling`

因此，Anthropic 版的 `north star` 更像：

> **能做 eval-first、对失败模式敏感、能把 context 与质量闭环接起来的 applied agent systems engineer。**

### OpenAI 更偏什么

更强调：

- `execution environment`
- `deployment`
- `production`
- `experimentation`
- `iteration`
- `reliability`
- `cost`

因此，OpenAI 版的 `north star` 更像：

> **能把 agent 从实验推进到 execution / deployment / reliable iteration 的 systems engineer。**

## 履历 North Star 的六个支柱

如果把目标画像进一步压成“理想履历长相”，最值得围绕的不是更多零散项目，而是下面六个支柱。

### 1. 一个旗舰 agent 系统

不是五个聪明 repo，而是一个足够深、能代表你系统 ownership 的主项目。

### 2. 真实 deployment 与运行证据

哪怕规模不大，也要能证明系统真的跑过，而不是只在本地 `README` 里存在。

### 3. 一套可见的 eval / regression 机制

要能说明你如何定义成功、如何测、如何发现退化、如何根据失败修系统。

### 4. context engineering 的质量收益

不是“我懂 context 很重要”，而是“我改了 retrieval / routing / grounding 之后，质量变好了”。

### 5. 一块明确属于你自己的 runtime ownership

例如 state、tool routing、execution contract、session policy、failure recovery，而不是关键复杂度全部外包给上游框架或模型。

### 6. 真实反馈驱动的迭代记录

顶尖团队更愿意看见“系统如何因为失败而变好”，而不是只看一版设计稿。

## 当前履历 vs north star：总判断

当前公开履历最强的部分是：

- `context / knowledge / harness` 的 framing
- 系统边界和产品主语
- 高质量原型与作品完整度

最弱的部分是：

- `eval / regression / replay`
- `deployment / production evidence`
- `observability / tracing / metrics`
- `real usage / adoption`
- `runtime ownership` 的更硬证据
- 可量化的质量改进

因此，当前更像：

> **很懂 agent systems 问题，并能做出高质量原型的人。**

而离目标画像还差的一层是：

> **把这种理解压缩成“可部署、可评估、可迭代、被真实使用”的系统证据包。**

## 表 1：当前履历 vs north star 差距表

| 维度 | North Star 目标信号 | 当前公开履历 | 差距判断 | 对顶尖 team 的影响 | 最值钱补法 |
|---|---|---|---|---|---|
| 旗舰项目 | 1 个足够深的主项目，代表 agent systems ownership | `gogo`、`oh-share-it`、`my-little-chating-agent` 都有价值，但主叙事仍偏分散 | 中等差距 | 更像多个聪明原型，而不是一个深系统 owner | 选 1 个旗舰项目，其余降为 supporting evidence |
| 问题主语 | 主语是 `context / harness / runtime / eval`，不是 generic AI app | 这点已经明显成立，尤其在 `gogo` 与 `oh-share-it` | 小差距 | 这是当前最强加分项 | 保持，但进一步落到工程结果 |
| Production deployment | 有真实 deployment，最好是云上或真实环境运行 | 公开证据里很弱 | 大差距 | 会被怀疑只停留在 prototype | 补 Docker、部署链接、运行说明、HTTPS |
| 真实使用 | 有真实用户或团队连续使用 | 当前缺少强公开证据 | 大差距 | 没有真实使用，很多可靠性判断不能成立 | 跑一个小团队或真实试点 |
| Eval 体系 | task set、judge/scorer、offline replay、regression | 当前几乎没有系统性公开证据 | 极大差距 | 这是 Anthropic 风格岗位最关键的门槛之一 | 建 `eval/`、回放、打分、回归机制 |
| Reliability | 能证明系统不只会 happy path | 目前更多是结构和设计，而不是可靠性证据 | 大差距 | 会被看成聪明但不稳 | 增加 retry、fallback、error handling、failure classes |
| Observability | tracing、logs、metrics、dashboard | 当前公开证据弱 | 大差距 | serious system 的基本面不足 | 增加 trace、metrics、日志与故障面板 |
| Runtime ownership | 主导过 state、tool routing、execution contract 或 recovery 的关键一块 | 有边界意识，但 ownership 还不够硬 | 中到大差距 | OpenAI / Cursor / Poolside 一类岗位会特别在意 | 自己做一块：tool router、state machine、session policy 等 |
| Context engineering | 不只是懂 context，而是能把 context 设计转成质量收益 | framing 强，但量化收益不足 | 中等差距 | 会被问“context 改造到底带来什么” | 做 retrieval / routing 改进前后对比 |
| Quality loop | 有“发现失败 → 改系统 → 指标变好”的闭环 | 缺公开闭环证据 | 大差距 | 顶尖 team 很看重这类工作方式信号 | 记录 3–5 轮失败驱动迭代与指标变化 |
| Cost / latency | 有 token、延迟、吞吐意识与优化动作 | 当前公开体现较少 | 中等差距 | OpenAI 风格岗位会更在意 tradeoff | 增加 cost、latency、cache、context budget 优化说明 |
| Guardrails / safety | 有 prompt/tool boundary、权限约束、handoff 逻辑 | 有边界感，但 guardrail 证据不足 | 中等差距 | Anthropic 风格岗位会更敏感 | 增加 allowlist、权限模型、fallback/handoff |
| Research × engineering | 研究训练能自然接回 agent system 工程 | ICASSP 是加分项，但和 agent 主线连接还不够紧 | 中等差距 | 能加分，但不是当前核心卖点 | 重写成 evaluation、机制设计、定量分析能力 |
| Public signal | adoption、文章、公开技术输出、外部背书 | 当前有 repo 和文档，但市场信号还不够强 | 中到大差距 | 顶尖团队不只看 repo，也看世界有没有轻度验证 | 写技术长文、试点案例、公开结果报告 |

## 表 2：按重要性排序的关键缺口

不是所有 gap 都同等重要。

### S 级：不补，很难像 north star

1. `eval / regression / quality loop`
2. `deployment / production evidence`
3. `real usage / user feedback`
4. `observability / tracing`
5. `reliability / failure handling`

### A 级：补上后会明显接近目标画像

1. `runtime ownership`
2. `context engineering` 的量化收益
3. `cost / latency optimization`
4. `guardrails / safety boundary`

### B 级：有用，但不是第一优先级

1. 更强的 public signal
2. 把研究背景更自然接回 agent systems
3. 更强的团队协作信号

## 表 3：Anthropic 视角与 OpenAI 视角下的最大 gap

| 公司 | 已有相对优势 | 最大 gap | 更优先补什么 |
|---|---|---|---|
| Anthropic | context / harness 问题意识、系统边界、对质量问题的天然敏感性 | 缺成体系 `eval-first` 证据 | eval、failure taxonomy、quality loop、guardrails |
| OpenAI | 原型完整度、系统主语较准、research × product × engineering 的潜力 | 缺 execution / deployment / reliability 的系统工程证据 | runtime ownership、deployment、observability、cost / latency |

## 最短路径：从当前履历到 north star

如果只看“最短补强路径”，可以压成下面几步：

1. **只选一个旗舰项目**
   - `gogo` 或 `oh-share-it`
2. **给它补 `eval`**
   - task suite、judge/scorer、回放、回归
3. **给它补 deployment 与 observability**
   - Docker、运行环境、trace、metrics、日志
4. **跑一个真实试点**
   - 一个小团队或 3–5 个真实用户就够
5. **主导一块明确的 runtime ownership**
   - state / tool router / execution contract / failure recovery 四选一先做深
6. **记录失败驱动的迭代历史**
   - 让履历开始像“经营过一个系统”，而不是“做过一个作品”

## 压缩结论

如果把这一页压成一句最有用的话：

> **你当前和 Anthropic / OpenAI agent systems north star 的核心差距，不是你不懂 agent systems，而是你还没有把这种理解变成一套“可部署、可观测、可评测、可迭代、被真实使用”的系统证据包。**

这也意味着方向并没有错。真正该做的，不是换方向，而是沿 `context / harness / eval / reliability` 这条线，把证据补硬。

## 相关页面

- [Agent 岗位JD抽样与能力信号](Agent岗位JD抽样与能力信号.md)
- [Barytes GitHub项目与Agent层次评估](Barytes-GitHub项目与Agent层次评估.md)
- [Agent Systems Engineer职业定位](Agent%20Systems%20Engineer职业定位.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)
