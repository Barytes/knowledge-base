# AI Architect 的 Proactive Intelligence 镜头

## 摘要

这份课程讲义把 agent 的下一步，从“会响应”推进到“会持续观察”。

它真正想解决的不是做一个会抓新闻的 bot，而是把你的长期战略意图变成一个可以被系统持续执行的监控任务。也就是说，主动性不是定时运行本身，而是把 intent automation 设计进产品。

## 核心判断

### 主动 agent 的主语，是战略意图而不是单次提问

讲义用两个助理做对比：一个只会等指令，一个会像 chief of staff 一样，基于长期目标主动发来提醒。

因此，系统目标不再只是回答当前问题，而是围绕你的长期目标，持续监控外部世界，并在出现值得注意的新信号时主动上报。

这里最关键的转变是：

- reactive assistant 处理即时请求
- proactive agent 维护长期关注面
- 真正被自动化的不是搜索动作，而是“什么值得我被打断”这个判断过程

### 外部信息是否重要，取决于内部战略上下文

builder 的自然反应通常是：做 scraper、加关键词提醒。

但讲义强调，噪音过滤才是主动系统的核心难点。新闻是否重要，不是由它提到了哪些词决定，而是由它和你的内部战略目标之间的关系决定。

因此第一版系统即使没有复杂内部系统，也至少需要一个明确的战略锚点。课程给出的最小实现是一个 `background.md` 文件，用来写清楚当前真正关心的方向，例如只关心 competitor 在 `video lip-sync` 与 `real-time generation` 上的突破。

这个判断很重要，因为它说明：

- context 不一定要复杂
- 但主动系统不能没有 context
- 没有内部目标约束的 alert system，只会把用户重新淹没在信息流里

### `Two-Stage Scan` 是把“像分析师那样工作”编进架构

讲义不建议用一堆脆弱的 if-else 规则去决定什么重要，而是把人类分析师的工作流抽象成一个两阶段结构：

1. `Broad Scan`
   先做广覆盖扫描，目标是尽可能找出潜在相关候选信号。
2. `Deep Dive`
   再把内部战略上下文和外部候选材料结合起来，对每条候选信息做更精细的战略价值评估。

这里的关键不是“多调一次模型”，而是故意把 coverage 与 precision 分开处理。

- 第一阶段优先不漏掉可能重要的东西
- 第二阶段才判断它是否真的值得进入你的注意力

换句话说，课程把主动性的“智慧”放在流程结构里，而不是寄希望于一次 prompt 就自动得出好判断。

### prompt 不是一次性问题，而是长期 `Mission Brief`

在主动 agent 里，prompt 的角色发生了变化。它不再像聊天那样只是一轮提问，而更像一份长期任务说明书。

这份 brief 需要明确：

- agent 的角色
- 它能看的内部与外部信息源
- 它的工作规则
- 输出格式
- 最终报告的 JSON schema

这和 [AI Architect Lens](ai-architect-lens.md) 中把 prompt 视作 assignment brief 的判断一脉相承，但这里更进一步：因为 agent 会反复运行，所以这份 brief 本身就是长期对齐机制的一部分。

### 主动系统的控制方式，不是盯过程，而是盯判断质量

讲义把 `manage-and-create workflow` 再推进了一步：对于一个自主运行的 agent，你不可能微操每个动作，所以主要控制手段必须前移到 success definition。

课程建议用 OKRs 来约束 agent 的判断质量，例如：

- `Precision`：被标为 `High Importance` 的提醒里，有多少真的和战略目标直接相关
- `Recall`：一段时间内，系统是否漏掉了本应捕获的重要公开信号
- `Actionability`：最终结果是否是前端容易展示、后续容易消费的结构化 JSON

这让主动 agent 的评估从“感觉有点用”变成可复盘的 performance review。

### false positive / false negative 的复盘，才是系统真正变聪明的地方

讲义强调，第一版主动系统判断不准并不等于失败。更重要的是把失败定位清楚：

- 是 `Broad Scan` 阶段关键词或搜索面不对
- 还是 `Deep Dive` 阶段的分析 prompt 不够具体
- 还是背景文件 `background.md` 写得太泛
- 或者系统已经开始需要 memory 来积累历史判断

这和 [AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md) 里的思路一致：先定义评估，再根据失败位置迭代 runtime、context 或 contract。

## 第一版 MVP 应该长什么样

课程给出的起手式非常克制：

- 做一个 `Competitor Radar`
- 前端只有一个 `Start Scan` 按钮
- 点击后手动触发一次 `Two-Stage Scan`
- 读取本地 `background.md`
- 返回一个同时包含 `Broad Scan Report` 与 `Deep Dive Report` 的结构化 JSON

这个设计有两个重要信号。

第一，主动 agent 的第一版不必先解决定时调度、always-on、后台守护这些工程问题。手动触发已经足够验证核心判断环是否成立。

第二，课程故意把“持续主动”拆成可验证的局部能力。先验证系统能不能做对战略价值判断，再考虑把它放进更长时运行环境。

## 对当前知识库主题的启发

这份材料把 AI Architect 系列又向前推了一步：

- [AI Architect Lens](ai-architect-lens.md) 解决“先定义要优化什么价值”
- [AI Architect 的 Context Intelligence 镜头](ai-architect-context-intelligence.md) 解决“怎样把个人上下文交给系统”
- 本页进一步解决“怎样让系统围绕长期目标持续观察世界”

它也和知识库里对 long-lived assistant 的兴趣形成呼应：高价值主动性，不是更频繁地打扰用户，而是更准确地在该打扰时打扰。为此，战略上下文、评测指标和失败复盘，比“是否后台运行”更先构成产品核心。

## 来源依据

- [AI Architect 讲义：Proactive Intelligence](../../../raw/external/ai-architect-proactive-intelligence.md)

## 相关页面

- [AI Architect Lens](ai-architect-lens.md)
- [AI Architect 的 Context Intelligence 镜头](ai-architect-context-intelligence.md)
- [AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)
- [Agent 时代的人机交互新命题](../agent-harness-runtime/agent时代的人机交互新命题.md)
- [被持续委托的工作主体](../agent-harness-runtime/被持续委托的工作主体.md)
