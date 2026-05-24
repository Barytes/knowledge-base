# coding agent 的上下文压缩工作流

**来源：** 演讲转录稿，位置：`raw/external/ai-engineer-harness-engineering-complex-problems.md`

---

## 核心判断

这份材料的真正贡献，不是再说一遍“context engineering 很重要”，而是把它落实成一套适合复杂代码库的工作流。

作者的主张可以压缩成一句话：

> **在 brownfield codebase 里，coding agent 的关键不是一直对话，而是持续压缩上下文，把有限上下文预算留给真正高杠杆的推理与修改。**

这套方法想解决的不是 demo 能不能跑起来，而是三个更真实的问题：

- 怎么减少反复返工出来的 `slop`
- 怎么让 agent 在复杂代码库里做更难的任务
- 怎么在团队里保持对代码演进的共同理解

---

## 一、Greenfield 容易，Brownfield 才是真问题

材料一开头就给出一个很实际的区分：

- 新项目、小 demo、轻量页面，agent 往往表现很好
- 十年老代码库、复杂依赖、跨文件改动，返工和 churn 会明显变多

也就是说，很多“AI 写代码很强”的体验，成立于信息结构比较简单的时候。一旦进入 brownfield 场景，真正稀缺的就不再是生成能力，而是：

- 对代码库结构的定位能力
- 对任务边界的收束能力
- 对上下文窗口的预算管理

---

## 二、上下文窗口不是越用越好，而是会进入 dumb zone

这份材料提出了一个非常实用的工程直觉：

> **上下文不是越多越安全。很多时候，越接近上下文上限，结果反而越差。**

因为 agent 是无状态的，每一步都只能依赖当前对话里留下的 token。上下文里如果混入太多：

- 错误信息
- 过时信息
- 无关文件
- 过长的工具输出
- 重复的人类纠偏对话

模型下一步的选择空间就会被污染。

作者把这称为 `dumb zone`。虽然 40% 只是经验线，不是硬阈值，但这个概念很有价值：**你不该把上下文窗口当仓库，而该把它当工作台。**

---

## 三、Intentional Compaction：把旧上下文压成可复用的工作摘要

材料最核心的方法是 `intentional compaction`。

含义不是简单清空重来，而是先让 agent 把当前上下文压缩成一份结构化 markdown，再用这份摘要启动新的上下文窗口。

好的 compaction 不只是“总结一下我们做了什么”，而要留下：

- 当前到底在解决什么问题
- 相关文件和行号
- 已确认的事实
- 已验证失败的路径
- 下一步应该怎么继续

这样新 agent 启动后，不必重新做一遍定位和理解，而可以直接进入高价值工作。

这和普通聊天式接力的区别在于：**压缩的对象不是聊天内容，而是任务状态。**

---

## 四、Subagent 的意义不是扮演角色，而是隔离上下文

材料对 subagent 有一个非常重要的纠偏：

> subagent 不是为了把 agent 拟人化成“前端”“后端”“QA”，而是为了控制上下文污染。

当父 agent 只需要知道“哪个文件相关、为什么相关”时，就没必要把整个搜索过程都塞进主上下文里。更合理的做法是：

1. 分出一个子上下文去做探索
2. 让它读很多文件、试很多检索路径
3. 最后只把压缩后的结论返回给父上下文

这样父 agent 只保留真正关键的结论，而不是把一长串搜索噪音也带回来。

所以 subagent 的本质不是多角色协作，而是**信息分层回传**。

---

## 五、Research → Plan → Implement，本质上是连续三次压缩

这份材料提出的 `Research / Plan / Implement` 流程，表面上像三段式流程，底层其实是在做三次不同类型的压缩。

### 1. Research：压缩“事实”

目标是弄清楚系统怎么工作、相关文件在哪里、约束条件是什么。

### 2. Plan：压缩“意图”

把 research 和任务目标重写成明确修改步骤，最好带上文件名、代码片段、验证方法。

### 3. Implement：压缩“执行空间”

真正执行时，不再让模型自己临场发明路径，而是在更小的操作空间里按计划推进。

这个流程的关键好处不是形式感，而是它让最贵的人类注意力，集中在 research 和 plan 的审核上。因为一条错误 research 可能毁掉整个实现方向，一条错误 plan 则可能放大成上百行错误代码。

---

## 六、Plan 的另一层作用：维持团队的 mental alignment

材料里一个很好的观察是，AI 时代 code review 的作用正在变化。

过去 review 更多是看代码本身。现在如果 AI 能生成更多代码，那么仅靠 diff 很难让团队保持对系统演化的共同理解。

这时 plan 的作用就不只是给 agent 看，也是给人看：

- 为什么这么改
- 改动顺序是什么
- 做了哪些验证
- 这个改动会如何改变系统

作者把这叫做 `mental alignment`。它不是抽象协作口号，而是团队在高速产出下维持共享理解的必要机制。

---

## 七、不要把思考外包给 AI

这份材料最成熟的地方，是它没有把工作流神化。

作者反复强调：

- 没有完美 prompt
- 不是所有任务都需要完整 research-plan-implement
- 人类仍然要审 research 和 plan
- AI 不能替代思考，只会放大已经做过的思考，或者放大思考缺失

这让整套方法显得更可信。它不是在说“终于找到 silver bullet”，而是在说：

> **通过压缩上下文、分层探索、显式计划和人工审阅，可以把今天模型在复杂代码库里的可用上限往上推。**

---

## 这篇材料的真正增量

相较于泛泛的 context engineering 讨论，这页材料留下了几个很可复用的工程判断：

1. **复杂代码库里的核心资源不是模型能力，而是上下文预算。**
2. **subagent 的本质是上下文隔离，而不是角色扮演。**
3. **research / plan / implement 的本质是事实、意图、执行空间的连续压缩。**
4. **plan 不只服务 agent，也服务团队的共享理解。**

---

## 与现有知识的关联

- [Harness 架构判断框架](../frameworks/Harness架构判断框架.md)：把本文中的上下文预算、subagent 隔离与连续压缩工作流上提为更短的 query 入口。

- [Harness Engineering（约束壳工程）](harness-engineering.md)：那页给出更一般的 harness 视角；本文补上在 coding agent 场景里最实操的一套上下文控制方法。
- [Thin Harness, Fat Skills](thin-harness-fat-skills.md)：这页强调 harness 应该薄、智能应往 skill 层推；本文则展示了 skill/workflow 层如何具体吸收复杂代码库里的上下文成本。
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md)：那页强调 runtime 与 contract；本文更强调 runtime 内部的上下文预算管理与团队协作机制。
- [Pi coding agent：一种极简且可观察的 coding harness](pi-coding-agent-harness.md)：如果要比较不同 coding harness 的默认壳厚度，这页提供了一条“复杂任务需要多少显式压缩工作流”的评价轴。

---

## 来源依据

- `raw/external/ai-engineer-harness-engineering-complex-problems.md`

> 注：原始材料为演讲转录，术语和案例保留一手口语表达的含义，但这里优先提炼可迁移的方法论。
