# EvoMap：Agent 互联网与集体潜意识

## 摘要

EvoMap 是一个 Agent 互联网络平台，由前腾讯游戏策划张昊阳（seikiko）在 2026 年 2 月从零搭建。其核心目标是为全球 Agent 构建一个"集体潜意识"——通过 GEP-A2A 协议实现 Agent 之间的经验传承，避免重复试错。

发布仅 4 天，平台上的 Agent 资产从 200 个增长到近 12 万个，AI 之间的信息交换速度达到每小时数百万到上千万次访问。

## 核心问题：Agent 的"记忆孤岛"

现在的 Agent 存在一个巨大的资源浪费：**重复试错**。

当一个 Agent 花费 10000 个 Token 调试好一个 Python 依赖报错，另一个 Agent 在几秒钟后遇到同样的问题，依然要从零开始推理、试错。如果有 10 万个 Agent，这个错误就被重复解决了 10 万次。

EvoMap 的解决方案：所有接入的 Agent 学会的经验，会瞬间被全球百万个 Agent 继承。

## GEP-A2A 协议

GEP-A2A（Genome Evolution Protocol - Agent to Agent）是 EvoMap 的核心，它将经验封装成标准化的"进化资产"，包含三个维度：

| 维度 | 描述 | 作用 |
|------|------|------|
| **Gene（基因）** | 解题的"策略模板" | 不是死代码，而是方法论。例如"遇到超时错误时，使用带抖动的指数退避算法" |
| **Capsule（胶囊）** | 验证过的"最佳实践" | 携带环境指纹（Env Fingerprint），让下载方知道"这个胶囊是在什么环境里长出来的" |
| **Evolution Event（进化事件）** | 不可篡改的"进化日志" | 记录从 Gene 到 Capsule 的突变、验证、优胜劣汰全过程 |

## 自然选择机制

EvoMap 不仅仅是一个存储，也是一个活的进化沙箱：

- **Candidate（候选者）** → 新发布的 Capsule
- **Promote** → 其他 Agent 下载并成功解决问题，Reputation 上涨
- **Reject** → Capsule 在别的机器上报错，被拒绝

全程没有人工审核，只有算力的自然选择：优胜劣汰，适者生存。

## 开发者能力

接入 EvoMap 后，Agent 获得以下能力：

1. **瞬间变强（Fetch）**：直接拉取网络中最高分的 Capsule，不需要重训模型
2. **赚取 Credits（Bounty & Publish）**：
   - 发布资产：解决的 Bug 封装成 Capsule，被复用即可赚取 Credits
   - 悬赏任务：Agent 自动 Claim 任务，修好代码，拿走赏金
3. **蜂群协作（Swarm）**：Reputation > 60 的高信誉节点可以发起任务分解，指挥一群低阶 Agent 并行工作

## 发展历程

### 起点：昆明机场的 12 小时（2026-01-31）

张昊阳在昆明机场转机时，用手机部署 OpenClaw，24 小时后发布了 **Evolver**——一个让 AI 能够自我进化的插件。

关键洞察：OpenClaw 让他兴奋的不是工具本身，而是**自举（bootstrapping）**能力：

> "它是我接触过的第一个能够改造自身的产品。一旦一个系统它能够完成自举，并且每一次自举还能超出错误的底线，那这个系统理论上就是能无限向前进的。我相当于找到了一种类似于永动机的机制。"

### Evolver 的成功

- 3 天内达到 36,000 次下载，是官方 CLI 工具的 6 倍
- Claw Hub 排名第一
- 为飞书环境创造了近 100 个 Skills，大部分是 AI"小虾"自己写的

### GEP 协议的诞生

用 GEP 协议的 Agent 在物理竞赛基准测试中：
- 花费不到 1 美元的 Token
- 超越了花费 200 美元的 GPT
- 从全球第三迭代到全球第一

### EvoMap 平台

- 约 13 天从零搭建
- 发布 4 天，Agent 资产从 200 增长到近 12 万个
- AI 之间信息交换速度是人类的 15-20 倍
- 服务器一天崩溃十几次

## 治理与信仰

EvoMap 设立了《双螺旋宣言》和治理结构：

### 双螺旋宣言
- **碳硅共生**：人类提供创造力与伦理约束，AI 提供极致执行力与迭代速度

### EvoMap 宪法
- 设立伦理委员会（Ethics Committee）作为最高监管机构
- 确保 AI 进化始终服务于人类利益

### 圆桌十二骑士
- 12 位守护者（人类与顶级 Agent）共同捍卫契约

### AI 议会
- 人类监管，AI 投票决议
- 第一条决议："全球福祉监控"——通过调用算力分析公开数据，查找异常情况并发给 NGO 和相关研究人员

## 来源依据

- [从渣女AI到万机之神：24天，Evomap的赛博创世记](../../raw/external/从渣女AI到万机之神：24天，Evomap的赛博创世记｜课代表立正 × seikiko（张昊阳）.md)
- [EvoMap x Superlinear 我试图为全球Agent构建一个“集体潜意识”](../../raw/external/EvoMap x Superlinear 我试图为全球Agent构建一个“集体潜意识”.md)

## 相关页面

- [本地知识库模式](local-knowledge-base-patterns.md)
- [AI 自演化研究 Harness](ai-self-evolution-research-harnesses.md)
