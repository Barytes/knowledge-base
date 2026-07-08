# Claude Code Dynamic Workflows

**来源：** [Introducing dynamic workflows in Claude Code](../../../raw/external/claude-code-dynamic-workflows.md)  
**标签：** Claude Code，dynamic workflows，subagents，coding agent，harness

---

## 核心判断

Dynamic Workflows 把 Claude Code 的 subagent 能力从“用户或 harness 分发子任务”推进到“Claude 动态生成临时 orchestration workflow”。

它的关键不只是并行运行更多 agents，而是把一组长任务控制动作产品化：

- 动态拆分任务
- 并行 fan out
- 独立角度探索
- 结果验证
- adversarial checking
- 中断恢复
- 最终收敛成单一协调答案

这说明 Claude Code 的厚壳路线继续加深：复杂工程任务的编排不再主要交给用户在外部用脚本、`tmux` 或手工计划管理，而是被做进 Claude Code 自身。

---

## 这项功能是什么

Claude 官方将 Dynamic Workflows 定位为 Claude Code 的 research preview。用户可以直接要求 Claude 创建 workflow，也可以开启 `ultracode` 设置，让 Claude 在 `xhigh` effort 下自行判断何时启用 workflow。

可用入口包括：

- Claude Code CLI
- Desktop
- VS Code extension
- Claude API
- Amazon Bedrock
- Vertex AI
- Microsoft Foundry

Max、Team、Enterprise 可用；Enterprise 默认关闭，需 admin 开启。官方也明确提示，这类 workflow 会比典型 Claude Code session 消耗更多 tokens。

---

## 适合什么任务

官方给出的典型场景都指向同一类问题：任务空间很大、可并行拆分、需要独立验证，单个 agent 线性执行容易漏。

- 全代码库 bug hunt
- profiler-guided optimization audit
- security audit
- 大规模 framework migration
- API deprecation migration
- language port
- 高风险方案 review

这些任务过去往往需要人类先写 plan，再分派给多个 agent 或多轮 session。Dynamic Workflows 的产品信号是：Claude Code 开始把这套分派和复核流程变成默认能力。

---

## Bun rewrite 例子说明了什么

原文用 Bun 从 Zig 到 Rust 的 rewrite 作为规模示例：

- 使用者是 Jarred Sumner。
- 目标是把 Bun 从 Zig port 到 Rust。
- 结果达到已有测试套件 99.8% 通过。
- 产出约 750,000 行 Rust。
- 从 first commit 到 merge 大约 11 天。
- workflow 分别处理 Rust lifetime mapping、逐文件行为等价 port、build / test fix loop，以及后续不必要数据复制清理。
- 每个文件有并行 agents 处理，并配有两个 reviewers。
- 官方同时注明该 port 当时尚未进入生产。

这个例子的重要性不在“自动写了很多代码”，而在于它展示了一种新的 coding-agent workload：大规模迁移被拆成可并行、可复核、可循环修复的工作流。

---

## 工作机制

从原文看，Dynamic Workflows 的机制可以压缩成四步：

1. **计划**：Claude 根据用户 prompt 动态规划任务。
2. **拆分与分发**：任务被拆成 subtasks，并 fan out 给并行 subagents。
3. **检查与反驳**：结果先被独立检查，部分 agents 从反方向尝试推翻已有结论。
4. **收敛**：workflow 多轮迭代，直到产出一个协调后的答案。

它还强调 long-running 支持：任务可以持续数小时到数天，进度会保存；如果被中断，可以从中断点继续。coordination 发生在 conversation 外部，因此主对话不需要承载完整编排状态。

---

## 对 Claude Code harness 画像的增量

这篇文章更新了 [Claude Code：较厚的 agentic coding harness](claude-code-harness.md) 的判断。

原先 Claude Code 已经体现出厚壳特征：

- session persistence
- context compaction
- permissions
- checkpoints
- subagents
- MCP / hooks / skills

Dynamic Workflows 进一步把“多个 subagents 如何协作”也产品化。它不只是提供 subagent primitive，而是提供一个由 Claude 动态生成的 workflow layer。

所以 Claude Code 的厚度可以再加一层：

1. 普通 agent loop
2. plan / permissions / checkpoints
3. subagent isolation
4. dynamic workflow orchestration

这让 Claude Code 更接近“官方内建 agent team harness”，而不只是“单 agent + 子任务工具”。

---

## 和 Harness 判断框架的关系

这篇材料给 [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md) 补了一个新判断：

> subagent 不只是在隔离上下文，也可以成为动态生成工作流中的并行执行单元。

但这也会带来新的张力：

- 开箱即用能力更强，但 token 成本显著上升。
- 任务覆盖面更大，但过程可观察性更重要。
- 独立验证更强，但不能替代人工 review 与真实测试门禁。
- 官方默认 workflow 更有吸引力，但用户对编排细节的控制会更少。

## 不要把上百个 agent 当成先进性指标

Dynamic Workflows 里“数十到数百个 subagents”的意义，不是给个人使用者设定一个先进性门槛，而是说明某些任务空间已经可以被工程化拆分、并行探索和交叉验证。

真正该问的是：这个任务是否大到值得并行，是否能拆成独立子问题，是否有测试、评分、review 或真实验收门禁，是否能把子 agent 的探索噪音压缩回主上下文。如果这些条件不存在，开更多 agent 只会增加 token 成本、管理成本和复核负担。

所以生产力提升不来自 agent 数量本身，而来自可积累的工作面、清楚的上下文、稳定的质量标准、可验证的执行闭环，以及把人类判断留在成功标准和风险边界上。

---

## 相关页面

- [Claude Code：较厚的 agentic coding harness](claude-code-harness.md)
- [Claude Code、Codex 与 pi 的 harness 对比](coding-agent-harness-comparison.md)
- [Harness Engineering（约束壳工程）](harness-engineering.md)
- [coding agent 的上下文压缩工作流](coding%20agent%20的上下文压缩工作流.md)
- [Agent 系统作为 OS 与 Cloud Runtime 问题](agent-runtime-os-cloud-runtime.md)
