---
title: "Introducing dynamic workflows in Claude Code"
source: "https://claude.com/blog/introducing-dynamic-workflows-in-claude-code"
published: 2026-05-28
created: 2026-05-29
type: source-note
product: Claude Code
category: Product announcements
tags:
  - claude-code
  - dynamic-workflows
  - subagents
  - coding-agent
  - harness
---

# Introducing dynamic workflows in Claude Code

这是 Claude 官方博客发布的 Claude Code Dynamic Workflows 产品公告。本文不全文镜像原文，只保存官方链接、本地摘要和摄取时提炼的证据点。

官方原文：<https://claude.com/blog/introducing-dynamic-workflows-in-claude-code>

## 本地摘要

Dynamic Workflows 是 Claude Code 的 research preview 功能。它让 Claude 在单个 session 中动态生成 orchestration scripts，并行运行数十到数百个 subagents，再在结果交给用户前做检查和整合。

这项能力面向单个 agent 一次 pass 难以完成的工程任务，例如全代码库 bug hunt、大规模迁移、安全审计、性能优化和高风险方案 review。它的核心不是多开几个 agent，而是把“规划、并行探索、独立验证、反驳、收敛、恢复”做成 Claude Code 的内建 workflow 层。

## 可用性与入口

- 发布时间：2026-05-28。
- 形态：research preview。
- 可用入口：Claude Code CLI、Desktop、VS Code extension、Claude API、Amazon Bedrock、Vertex AI、Microsoft Foundry。
- 计划：Max、Team、Enterprise 可用；Enterprise 需要 admin enabled。
- Max / Team / API 默认开启；Enterprise 发布时默认关闭，由 admin 开启。
- 推荐使用方式：开启 auto mode。
- 启动方式：
  - 直接要求 Claude 创建 dynamic workflow。
  - 开启 Claude Code 专用设置 `ultracode`。它把 effort level 设为 `xhigh`，并让 Claude 自动决定何时使用 workflow。
- 成本提示：dynamic workflows 会比典型 Claude Code session 消耗明显更多 tokens。
- 安全/治理提示：第一次触发 workflow 时，Claude Code 会展示将要执行的内容并请求确认；组织 admin 可通过 managed settings 禁用。

## 典型使用场景

- 全代码库 bug hunt。
- profiler-guided optimization audit。
- security audit。
- 大规模 framework swap。
- API deprecation migration。
- language port。
- 高风险工作中的独立复核与 adversarial review。

这些场景共同点是：任务空间大、可并行拆分、需要独立验证，而且单个 agent 线性探索容易遗漏。

## Bun rewrite 例子

原文给出的强例子是 Bun 从 Zig 到 Rust 的 rewrite：

- Jarred Sumner 使用 dynamic workflows 将 Bun 从 Zig port 到 Rust。
- 迁移后已有测试套件通过率达到 99.8%。
- 产出约 750,000 行 Rust。
- 从 first commit 到 merge 大约 11 天。
- 一个 workflow 为 Zig codebase 中每个 struct field 映射合适的 Rust lifetime。
- 另一个 workflow 将每个 `.zig` 文件行为等价地 port 成 `.rs` 文件。
- 过程中有数百个 agents 并行处理，并对每个文件设置两个 reviewers。
- 后续 fix loop 驱动 build 与 test suite，直到两者通过。
- port 之后，一个 overnight workflow 处理不必要的数据复制，并为人工最终 review 打开 PR。
- 原文同时说明该 Rust port 当时尚未进入生产。

## 工作机制

Dynamic workflow 启动后，Claude 会根据用户 prompt 动态规划，将任务拆成 subtasks，并把工作 fan out 给并行 subagents。结果不会直接拼回最终答案，而是先经过检查。

原文强调三类机制：

1. **独立角度**：agents 从不同方向处理同一问题，降低单一路径偏差。
2. **反驳与验证**：其他 agents 尝试推翻已有发现或结果。
3. **迭代收敛**：workflow 持续迭代，直到答案收敛。

Dynamic workflows 面向可以持续数小时到数天的 long-running work。进度会在运行中保存，中断后可以从中断点继续，而不是从头开始。原文还强调 coordination 发生在 conversation 外部，因此任务很大时，计划也能保持在轨道上。

## 本地判断

这篇文章说明 Claude Code 的 harness 厚度又往前推进了一层：

- 原来的 subagent 更像独立上下文和任务分发工具。
- Dynamic Workflows 把 subagents 组织成 Claude 自己生成的临时工作流。
- 工作流不只并行执行，还内建独立验证、adversarial checking 和 long-running recovery。

因此它补上的不是一个普通按钮，而是“从 single agent 到 dynamic agent team”的中间层。它也进一步强化了 Claude Code 和极简 harness 的差异：复杂性被做进产品默认能力，而不是留给用户用 `tmux`、脚本和手工任务分解外部拼装。

## 边界与风险

- token usage 会显著上升。
- workflow 越自主，用户越需要可观察性来理解哪些 subagents 做了什么、如何验证、为什么收敛。
- 对高风险代码修改，内建 adversarial checking 有价值，但不能替代最终人工 review、测试与部署门禁。
- 这类功能会进一步强化 Claude Code 官方默认 workflow 的吸引力，也会让行为更依赖 Anthropic 对 orchestration 的产品判断。

## 相关维护页

- [Claude Code Dynamic Workflows](../../wiki/topics/agent-harness-runtime/claude-code-dynamic-workflows.md)
- [Claude Code：较厚的 agentic coding harness](../../wiki/topics/agent-harness-runtime/claude-code-harness.md)
- [Harness 架构判断框架](../../wiki/frameworks/Harness架构判断框架.md)
