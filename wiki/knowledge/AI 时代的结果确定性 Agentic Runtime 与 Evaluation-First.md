# AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First

**来源：** [Superlinear Academy 社区文章：从过程确定性到结果确定性：AI 时代的另一种安全感](../../raw/external/superlinear-从过程确定性到结果确定性.md)  
**标签：** agentic runtime，evaluation-first，Claude Code，运行时层，契约层

---

## 核心判断

这篇材料最强的地方，是把“为什么很多 AI demo 很惊艳，但做成产品却很累”拆成了一套清楚的工程结构。

作者的主张可以压缩成一句话：

> **AI 产品开发真正难的，常常不是模型层或协议层，而是运行时层对不确定性的吸收，以及契约层对“什么才算完成”的定义。**

进一步说，Claude Code、Codex、Cursor Agent 这类 general coding agent 的价值，不只是“一个更好用的聊天框”，而是它们正在收敛成一种**可复用的 Agentic Runtime**。开发者可以少写很多“给 AI 擦屁股”的 workflow，把精力从过程控制转向结果定义与验证。

---

## Agent 调用的四层结构

文章把 AI 集成拆成四层：

1. **模型层**：用谁，`Claude` 还是 `GPT`，`Opus` 还是 `Haiku`
2. **协议层**：`Chat Completion API`、`Response API`、`MCP`、`REST`、`JSON Mode`
3. **运行时层**：状态管理、工具调用、文件注入、权限控制、并发、上下文调度
4. **契约层**：成功标准、guardrail、验证逻辑、人工接管条件

这个拆法有一个很实用的效果：它解释了为什么团队嘴上讨论最多的是 API，但工程时间往往死在别处。

因为协议层虽然显眼，真正吞时间的是运行时层。不是业务逻辑复杂，而是 LLM 的 failure pattern 太多：

- 长文偷懒
- 格式漂移
- 中途夹杂错误语言
- 超时中断
- 上下文不一致
- 工具调用不稳定

这些问题不属于“翻译业务”本身，却逼得每个团队都在自己补一层 orchestration。

---

## 运行时层为什么会成为黑洞

文章举的是中翻英自动同步的例子。最开始看起来只是“调个 API 做翻译”，实际落地却要补很多脏活：

- 长文分段
- 断点续传
- 残留中文检测
- 术语统一
- 超时恢复
- 格式校验

关键洞察不是“翻译很难”，而是：

> **AI 输出的不确定性，会把大量工程成本推到运行时层。**

而运行时层最让人难受的地方在于，它和业务价值往往弱相关。无论做翻译、代码生成还是客服 agent，团队都在重复发明类似的补丁系统。

这就是文章后面要引出的转折：如果这层是共性脏活，那么它有没有可能被复用，而不必每个团队自己重做一遍？

---

## Claude Code / Codex 正在变成可复用的 Agentic Runtime

作者的观察是，越来越多模型提供商开始主动兼容 Claude Code 这类 runtime。表面上看，这是“让别家的模型也能在 Claude Code 后面跑”；更深一层看，是：

> **模型提供商开始主动把自己的 failure pattern 适配到某个既有 runtime 的预期行为。**

也就是说，开发者不再亲自面对每个模型的长尾脾气。部分“擦屁股”工作，被生态上移给了 runtime 设计者和模型提供商。

这时 Claude Code / Codex / Cursor Agent 的意义就变了。它们不只是产品，而更像一种正在收敛的基础设施标准：

- 文件作为默认工作面
- 工具调用作为基本闭环
- agentic loop 作为默认运行方式
- 权限、sandbox、allowed tools 作为安全边界

这和单纯“把 LLM 嵌进应用里”是两种非常不同的工程路线。

---

## Agentic loop 的关键，不是更聪明，而是能观察到结果

文章对 agentic loop 的解释很清楚：

- 传统 API 调用：模型只能看到 prompt，然后给你一个结果
- agentic runtime：模型可以执行动作，也能观察动作的后果，再决定下一步

这个差别听上去简单，但它几乎重写了开发体验。

比如让 agent 修改一个文件后，再运行一个 Python 校验脚本：

- 如果脚本报错，错误信息会反馈给 agent
- agent 知道哪里错了
- 它可以自己回去修，再跑一遍

这就是一个最基本的：

**执行 → 观测 → 纠错**

文章特别强调文件的重要性。文件不是随便一种载体，而是让状态变得可见、可持久、可序列化。文件一旦成为默认工作面，很多以前需要外层 orchestration 才能完成的东西，就能直接在 runtime 里闭环。

---

## 只有观测还不够，还要有契约

但 agentic loop 并不自动意味着“结果就对”。

它只解决了一半问题：agent 能看到自己做了什么，却还未必知道**什么才算做完**。

这就是契约层的作用。文章把契约层说成成功标准的显式化：

- 什么叫翻译完成
- 什么叫格式正确
- 什么叫没有残留中文
- 什么叫术语统一
- 什么情况下需要人工介入

作者给了一个很好的比喻：

> 像是在给一个有健忘症的实习生交代任务。你必须把验收标准写到只看这次指令，他也能判断自己有没有做完。

这其实就是 evaluation-first 的工程版本：

- 不先想 prompt 多优雅
- 先想成功能不能被验证
- 再把验证条件暴露给 agent

于是 runtime 给 agent 眼睛，contract 给 agent 尺子。两者缺一不可。

---

## 从过程确定性到结果确定性

文章标题里的“结果确定性”，指的是一种和传统编程不同的安全感来源。

### 传统程序员的安全感：过程确定性

过去我们熟悉的是：

- 把结果翻译成逻辑
- 把逻辑写成程序
- 让每个边界条件都由人预先编码

只要过程写对，结果就可靠。

这套心智的成本结构是：

- 代码执行便宜
- 人写流程很贵

所以值得花很多时间设计复用逻辑、覆盖边界、提前编码所有规则。

### Agent 时代的新安全感：结果确定性

现在另一种路径开始可行：

- 不规定每一步怎么走
- 只规定最后什么样算对
- 让 agent 多次尝试、检查、回退、修复

这套心智的前提是：

- intelligence 越来越便宜
- token 可以被用来“挥霍式纠错”
- 很多局部步骤不值得人类再手写成 rigid workflow

于是安全感不再来自“我控制了每一步”，而来自：

> **我定义了终点，也定义了验收方式。至于 agent 走哪条路，只要最终通过验证即可。**

这不是完全抛弃过程，而是把过程控制从人手写规则，部分转移给 runtime + eval 闭环。

---

## 这套方法的边界

文章也没有把它神化，而是保留了两个重要边界。

### 1. 任务必须能较清楚地定义“对”

结果确定性最适合的，是那些可以明确验收的任务：

- 格式对不对
- 文件能不能通过脚本检查
- 是否还残留中文字符
- 测试是否通过

如果任务本身的好坏标准非常模糊，evaluation-first 仍然有帮助，但难度会显著上升。因为问题不再是 runtime 不够强，而是人自己也说不清要什么。

### 2. 安全边界必须认真设计

让 agent 读写文件、跑 Python、执行 bash，本质上是在给它操作权。

这也是 general coding agent 强大的原因，同时也是风险来源。文章建议的方向是：

- 用 `--allowedTools` 收紧工具权限
- 把 agent 约束在指定脚本与目录里
- 配合 sandbox，降低宿主环境风险

也就是说，运行时层被复用了，不代表安全问题消失了；只是安全问题被更明确地集中到权限模型上。

---

## 这篇材料的真正增量

这篇材料和一般“多写点 prompt、多做点 workflow”的经验帖不同。它真正提供了三个可复用判断：

1. **四层结构**：把模型、协议、运行时、契约分开，避免把问题都误归因到 API 或模型。
2. **runtime 视角**：解释 Claude Code 一类工具为什么不是简单“更强聊天”，而是可复用的 agentic runtime。
3. **结果确定性**：把 AI 时代的工程安全感，从“控制过程”转向“定义终点并验证终点”。

这让它不只是翻译场景的 case study，而更像一种通用工程镜头。

---

## 与现有知识的关联

- [Harness Engineering（约束壳工程）](harness-engineering.md)：那页强调外层控制壳的重要性；本文把这层进一步拆成运行时层与契约层。
- [Thin Harness, Fat Skills](thin-harness-fat-skills.md)：那页强调 latent / deterministic 的边界；本文则给出在工程集成中如何把“确定性”落到 eval 与 contract。
- [coding agent 的上下文压缩工作流](coding agent 的上下文压缩工作流.md)：这页更具体讨论复杂代码库里如何通过 compaction、subagent 与 plan 来管理上下文预算。
- [Claude Code：较厚的 agentic coding harness](claude-code-harness.md)：本文提供了一个更偏产品化的解释，说明为什么开发者会把 Claude Code 当作 runtime 复用，而不是只当一个 coding chat。
- [Claude Code、Codex 与 pi 的 harness 对比](coding-agent-harness-comparison.md)：如果要比较不同 coding agent harness 的价值，这篇材料补上了“结果确定性”这条评价轴。
- [AI Architect 的 Advanced Architecture 镜头](ai-architect-advanced-architecture.md)：那页把 evaluation set、multi-model hand-off、fallback 与身份边界放进一套更偏课程化的生产升级路径。
