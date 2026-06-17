# AI Infra 的抗模型吞噬地图

## 摘要

AI Infra 可以粗略理解为：让 AI 应用、agent、模型训练/推理、数据闭环、评测、安全治理稳定运行的一整套基础设施。

但不是所有 AI Infra 都同样抗周期。一个简单判断是：

> 模型会持续吞掉“纯认知层”的 infra，但很难吞掉和真实世界绑定的状态、权限、成本、执行、安全、评测和治理。

也就是说，越只是帮助模型“更会说话”，越容易被 foundation model、平台 API 或开源库商品化；越接近真实系统边界，越可能 future proof。

## AI Infra 包含哪些层

可以按下面这张层次图理解：

```text
应用 / Agent 层
↑
Context / Memory / Workflow 层
↑
模型调用 / 推理服务层
↑
模型训练 / 微调 / 对齐层
↑
数据 / 向量 / 知识层
↑
评测 / 观测 / 安全层
↑
算力 / 调度 / 存储 / 网络底座
```

更具体地拆，可以包括：

| 方向 | 核心问题 |
|---|---|
| Compute / GPU Infra | 如何让 GPU 不空转，如何调度、隔离、恢复和扩缩容 |
| Training Infra | 如何管理训练数据、分布式训练、checkpoint、实验和模型注册 |
| Inference Infra | 如何降低每 token 成本、延迟和线上服务不稳定性 |
| Model Gateway / LLMOps | 如何做 provider routing、fallback、限流、成本、日志和策略 |
| Data Infra for AI | 如何摄取、清洗、索引、追踪、授权和更新数据 |
| RAG / Knowledge Infra | 如何检索、引用、grounding、处理 stale docs 和文档权限 |
| Context / Memory Infra | 模型该知道什么、什么时候知道、知道多少、是否可信 |
| Agent Infra | 如何安全执行工具、浏览器、终端、长任务、审批和回滚 |
| Eval Infra | 如何做离线/在线评测、回归、LLM-as-judge、人工抽检和 agent trajectory eval |
| Observability / Tracing | 如何知道模型看到了什么、为什么调用工具、哪里失败 |
| Safety / Governance | 如何做 PII、secret、prompt injection、权限、审计和合规 |
| Developer Tooling | 如何做 prompt / context debugger、eval dashboard、replay 和本地 sandbox |

这张图的重点不是列名词，而是把 AI Infra 从“模型外面的工具”改看成一组真实系统边界。

## 容易被模型吞掉的方向

“被模型吞掉”指的是：原来需要外部工具、框架或 prompt trick 做的事情，随着模型能力和模型 API 提升，逐渐被模型原生能力或平台能力吸收。

容易被吞掉的方向通常有这些特征：

```text
纯文本变换
无强状态
无强权限
无强可靠性要求
没有深度系统集成
核心价值靠 prompt trick 维持
```

### 简单 Prompt Engineering 工具

例如 prompt 模板库、prompt 改写器、prompt marketplace、简单 chain prompt。模型会越来越会理解意图，平台也会把常见 prompting 模式产品化。

剩下更有价值的部分不是模板本身，而是 prompt versioning、eval、deployment 和 observability。

### 简单 Chain / Workflow Wrapper

如果一个框架只是：

```text
LLMChain(prompt1) -> LLMChain(prompt2) -> JSON
```

它很容易被模型原生 structured output、function calling 或更强的单次推理吃掉。

### 简单 RAG Wrapper

纯粹做：

```text
chunk -> embedding -> vector search -> stuff prompt
```

会越来越商品化。原因是 embedding、长上下文、file search、数据库原生向量检索和 agentic file reading 都会持续压缩这层价值。

但企业级 RAG 不会完全被吞，因为它涉及权限、更新、审计、评测、数据治理和来源追踪。

### 简单 Output Parser

过去很多库的价值是把 LLM 输出修成 JSON。随着 structured outputs、function calling、JSON mode 变强，这层会被压缩。

更有价值的是 schema migration、validation、repair audit、contract testing 和 downstream integration。

### 普通 Chatbot Builder

“上传文档生成客服机器人”如果没有行业数据、业务工作流和系统集成，壁垒会很低，容易被 OpenAI、Anthropic、Google、Microsoft 或企业 SaaS 内置能力吸收。

### 简单 Agent Framework

只提供 `tools + planner + executor`，但没有 sandbox、权限、状态、debug、eval、deployment 的 agent framework，容易变成 demo 框架。模型会越来越会自己 plan、call tools 和修正错误。

## 更 future proof 的方向

更抗模型能力提升的 AI Infra 通常有这些特征：

```text
靠近真实系统边界
靠近数据 / 权限 / 状态
强工程复杂度
强企业集成
强可靠性要求
强成本优化
强治理需求
跨模型 / 跨供应商
```

### 1. Compute / Inference Optimization

推理需求越大，成本和延迟越重要。GPU 调度、KV cache、batching、routing、quantization、multi-tenant serving、edge/on-prem inference 都不会因为模型变强而消失。

企业会持续问：

```text
能不能便宜 50%
能不能快 2 倍
能不能稳定承载峰值
```

所以推理 infra 和 GPU optimization 很抗周期。

### 2. Eval Infra

模型越强，越需要评测。因为 prompt、context、模型版本、工具和 agent 行为都会引入 regression。

Eval 会越来越像 AI 系统里的 CI/CD。真正有壁垒的是 task set、scorer、replay、regression、failure taxonomy 和 human review workflow，而不是单次 LLM-as-judge。

### 3. Observability / Debugging

AI 系统失败时，问题通常不是简单 crash，而是：

```text
模型错了？
上下文错了？
检索错了？
工具错了？
memory 污染？
权限没给？
prompt injection？
```

因此 tracing、context inspection、agent trajectory debugging、failure replay 会越来越重要。

### 4. Context / Memory Governance

这不只是“长期记忆”，而是管理信息生命周期：

- 什么该记
- 什么不该记
- 什么过期
- 什么冲突
- 什么敏感
- 什么进入当前 prompt
- 什么进入 LLM Wiki
- 什么进入 skill
- 什么需要用户确认

这层很难被模型完全吞掉，因为它涉及状态管理、权限、审计、用户信任和长期一致性。模型可以参与判断，但不应该独自拥有最终控制权。

### 5. Security / Privacy / Governance

prompt injection、secret redaction、data leakage prevention、access control、audit trail、policy enforcement 和 compliance 都会随着 agent 能力增强而更重要。

模型越能行动，攻击面越大。

### 6. Data Integration / Permissions-aware Retrieval

企业 AI 难点常常不是模型，而是：

```text
数据在哪里？
谁能看？
数据新不新？
来源可信吗？
怎么追溯？
怎么删除？
```

这属于系统工程，不是语言能力问题。

### 7. Agent Runtime / Sandbox

Agent 要执行真实任务，就需要 sandbox、browser、terminal、filesystem、network policy、approval flow、rollback、long-running jobs、state persistence 和 audit log。

模型可以决定“做什么”，但 infrastructure 要保证它如何安全地做、失败后如何恢复、谁来审计。

### 8. Model Gateway / Routing / Cost Control

企业通常不会只用一个模型。只要存在 OpenAI、Anthropic、Gemini、本地模型、便宜模型、专用模型和 fallback model，就需要 gateway 处理 routing、credential、policy、cost accounting 和 latency optimization。

这层竞争会激烈，但控制面价值不会消失。

## 三档机会地图

### 第一档：最 future proof

- Inference optimization：serving、KV cache、routing、speculative decoding、GPU utilization、quantization、edge/on-prem inference。
- Eval + Observability：agent trajectory eval、context eval、regression testing、online monitoring、failure replay、LLM judge calibration。
- Security / Governance：prompt injection、data leakage、permissions-aware retrieval、audit、compliance。
- Context / Memory Infrastructure：context engine、LLM Wiki、memory lifecycle、session search、context eval、knowledge freshness、context governance。

这一档的共同点是：模型越强，使用越多，越需要这些层。

### 第二档：有机会，但要做深

- Agent Runtime：必须做到 sandbox、permissions、state、browser/terminal、rollback、long-running execution、human-in-the-loop。
- Enterprise RAG / Knowledge Layer：必须做到 ACL、freshness、lineage、citation、hybrid search、document workflows、eval、LLM Wiki 或 structured knowledge。
- Model Gateway：必须做到 routing quality、policy、cost optimization、observability、enterprise control plane。

这一档如果只做薄 wrapper，容易被吞；如果做成真实系统边界，则有机会。

### 第三档：容易商品化

- Prompt tools
- Simple chatbot builder
- Simple agent framework
- Basic vector DB wrapper
- Basic output parser

这些方向除非绑定行业数据、工作流、评测、部署或治理，否则壁垒偏弱。

## 一个判断标准

如果一个 AI Infra idea 的核心价值主要回答：

```text
如何让模型更会说话？
```

它大概率危险。

如果它回答的是：

```text
如何让模型在真实世界里可靠、安全、便宜、可观测、可治理地工作？
```

它更可能 future proof。

可以用两组问题快速筛选。

容易被吞的信号：

- 是否只是 prompt 模板
- 是否只是包一层 API
- 是否不持有数据、不控制权限、不管理状态
- 是否没有系统集成
- 是否没有 eval 或 observability
- 是否没有失败恢复和审计

更抗周期的信号：

- 是否管理真实资源，例如 GPU、数据、权限、成本
- 是否产生审计和可观测性
- 是否嵌入企业 workflow
- 是否处理失败恢复
- 是否跨模型、跨云、跨系统
- 是否能随着模型变强继续受益
- 是否越复杂越有价值

## 和已有页面的关系

这页和已有页面的分工是：

- [AI 产业分层地图（2026）](AI产业分层地图.md)：给出 AI 市场的总体产业层次。
- [AI 产业的付钱地图（2026）](AI产业的付钱地图.md)：解释资金和采购预算流向哪些层。
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../agent-harness-runtime/AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)：解释 runtime 与 eval 为什么决定结果确定性。
- [Context Engine：上下文编排层](../context-memory-knowledge-system/context-engine.md)：把 context / memory / wiki / RAG 的调度层单独拆出来。

本页提供的是一张“哪些 AI Infra 更容易被模型吞掉，哪些更 future proof”的判断地图。

## 来源依据

- `raw/personal/conversations/context-engine-ai-infra-2026-06-17.md`
