---
title: "OpenClaw public docs notes"
source:
  - "https://docs.openclaw.ai/gateway"
  - "https://docs.openclaw.ai/concepts/architecture"
  - "https://docs.openclaw.ai/concepts/multi-agent"
  - "https://docs.openclaw.ai/gateway/heartbeat"
  - "https://docs.openclaw.ai/zh-CN/concepts/soul"
  - "https://docs.openclaw.ai/zh-CN/reference/templates/SOUL"
created: 2026-04-12
description: "Compact notes from public OpenClaw docs, focused on Gateway, assistant identity, SOUL.md, multi-agent routing, and heartbeat."
tags:
  - "openclaw"
  - "docs"
  - "assistant"
  - "gateway"
---

# OpenClaw Public Docs Notes

## Observation Scope

- Product: `OpenClaw`
- Observation date: `2026-04-12`
- Focus:
  - assistant vs gateway 的主语关系
  - `SOUL.md` / identity / continuity
  - multi-agent routing
  - heartbeat / always-on
  - device nodes 与 remote gateway

## Key Public Signals

### 1. 产品叙事已经在努力把主语从 Gateway 切到 assistant

- GitHub README 明确写：
  - `OpenClaw` 是一个 “personal AI assistant”
  - “The Gateway is just the control plane — the product is the assistant”
- 这说明它在产品叙事上并不想把自己定义成聊天桥或纯网关。

### 2. 但实现架构仍然明显以 Gateway 为系统中枢

- Gateway runbook 公开写：
  - one always-on process for routing, control plane, and channel connections
  - single multiplexed port for WebSocket control/RPC、HTTP APIs、Control UI、hooks
- 架构文档进一步写：
  - a single long-lived Gateway owns all messaging surfaces
  - control-plane clients connect over WebSocket
  - nodes 也通过同一个 Gateway WebSocket 连接
- 这说明 assistant 虽然是产品叙事主语，Gateway 仍然是系统实现主语。

### 3. `SOUL.md` 是它人格层和身份层的核心注入点

- `SOUL.md` 指南明确说：
  - `SOUL.md` 是智能体声音所在的地方
  - OpenClaw 会在普通会话中注入它
- `SOUL` 模板进一步强调：
  - “你不是聊天机器人。你正在成为某个人。”
  - “每次会话，你都是全新醒来的。这些文件就是你的记忆。阅读它们。更新它们。它们是你持续存在的方式。”
- 这说明 OpenClaw 很认真地把 continuity 的一部分放在 prompt files 上，而不是只放在 session transcript 上。

### 4. 它对“一个 agent 是什么”已经有清楚定义

- multi-agent 文档明确写：
  - 一个 agent 是 “a fully scoped brain”
  - 它有自己的 workspace
  - 有自己的 `agentDir`
  - 有自己的 session store
- 这很重要，因为它说明 OpenClaw 里的 agent 已经不只是某个单轮聊天对象，而是隔离良好的 workspace + state + sessions 组合体。

### 5. 它支持 multiple agents，但方式仍是“同一 Gateway 下的多个隔离 agent”

- multi-agent 文档公开给出：
  - multiple isolated agents in one running Gateway
  - per-agent workspace
  - per-agent auth profiles
  - per-agent sessions
  - bindings 决定入站消息路由到哪个 agent
- 这意味着它已经比“单助手 + 单会话”更进一步，但默认模型仍然是 gateway 承载多个 agent，而不是一个更高层 agent 自由调度 execution bodies。

### 6. 它已经有明显的 always-on / proactive 语义

- README 里强调 single-user assistant 应该是 local、fast、always-on
- heartbeat 文档说明：
  - 可以按 cadence 周期性跑 heartbeat
  - 默认可以全天运行
  - 可通过 `HEARTBEAT.md` 提供稳定 checklist
  - agent 可以在 heartbeat 中主动执行或维护这类例行检查
- 这说明它不是纯被动聊天工具，而已经把周期性主动行为做进系统。

### 7. 它把设备能力纳入 node 模型，而不是直接等同于 agent

- 架构文档里有 node 概念：
  - macOS / iOS / Android / headless nodes
  - node 通过 Gateway WebSocket 连接
  - node 暴露 `canvas.*`、`camera.*`、`screen.record`、`location.get` 等能力
- README 还明确区分：
  - Gateway host 跑 exec tool 和 channels
  - device nodes 跑 device-local actions
- 这说明它已经在承认 device 只是能力来源，不完全等于 assistant 本体。

## Current Tension

OpenClaw 当前最值得注意的一条张力是：

> 产品叙事在说 assistant 才是产品，本体高于 Gateway；但公开实现架构里，Gateway 仍然是最强的系统中心。

所以如果以后要问它和 `clawhouse` 的差别，关键不是“它有没有人格”或“能不能多端访问”，而是：

- assistant identity 到底有多独立于 gateway / host
- multi-agent 是不是已经接近真正的持续协作对象，还是仍主要是隔离 workspace + sessions
- re-entry 默认入口究竟是聊天 / WebChat / dashboard，还是更高层的主动工作简报

## Related Repo Evidence

- [GitHub repo snapshot: openclaw/openclaw](github-repo-openclaw-openclaw.md)
