# Harness Engineering（约束壳工程）

## 摘要

Harness engineering 指的是围绕模型外侧搭建的一层运行控制壳，让 agent 在处理漫长、混乱、跨步骤的任务时，不至于漂移、卡住，或错误地宣布自己已经完成。

这份来源材料最核心的判断是：agent 表现中很多肉眼可见的进步，不一定来自模型权重本身，而更可能来自外层控制系统的改进。

## 核心层次

### 1. 长流程任务的过程控制

第一层把原本松散的 agent 行为改造成可管理的工作流。

关键动作包括：

- 把进度外化到文件里
- 用结构化格式约束任务状态
- 强制每次会话启动时执行重新定向的例行步骤
- 把回滚点放进版本控制

这一层存在的原因是：仅仅把记忆外化，并不能保证 agent 真会按计划推进，也不能保证它会诚实地校验是否完成。

### 2. 并行工作的协同控制

当多个 agent 同时操作一个代码库或任务图时，第二层就会出现。

关键动作包括：

- planner、worker、judge 的角色分离
- 通过状态机或工作流引擎做门控执行
- 用边界明确的 ownership 避免冲突与空转
- 用把全局故障拆成更小搜索空间的调试方法

这里的主要风险不只是答错，而是协同坍塌：agent 彼此阻塞、优化琐碎改动，或覆盖共享工作。

### 3. 独立验证

第三层针对的是 agent 容易高估自己输出质量这一问题。

关键动作包括：

- 分离独立 evaluator 角色
- 用真实环境测试，而不是只看代码表面
- 建立带怀疑态度的验证闭环
- 采用强 sandbox，避免 agent 篡改测试本身

来源材料把这视为独立的控制问题：即使协同做得很好，agent 仍然可能“很自信地错”。

## 重要区分

文章强调，不应把 harness 和所有 agent infrastructure 混为一谈。

- Harness 主要负责行为约束、顺序推进、协同与验证。
- 更广义的 agent 基础设施还包括 CLI 访问、skills、memory store、MCP 式集成、环境配置等工具层。

这个区分重要，因为工具更强、记忆更大，并不会自动解决流程纪律问题。

## 补偿面

来源材料里最强的一个概念，是把 harness 组件看作对当前模型弱点的阶段性补偿。

- 如果模型上下文保持能力不够，团队就会加 reset 或压缩系统。
- 如果模型不擅长定义完成标准，团队就会加 contract 或带门控的状态格式。
- 如果模型无法可靠自评，团队就会加外部验证闭环。

随着模型能力变强，其中一些组件会从杠杆变成负担。真正持久的优势不是“壳越厚越好”，而是持续追踪哪些补偿仍然必要，哪些该拆掉。

后续材料 [Agent 系统作为 OS 与 Cloud Runtime 问题](agent-runtime-os-cloud-runtime.md) 补充了一个更底层的处理方式：把易腐化的策略留在 harness，把更稳定的抽象下沉为 runtime interface，例如 session log、execute、wake、provision、sandbox lifecycle 和权限边界。这样可以降低某一代模型或工具补丁固化成长期包袱的风险。

## 向研究闭环的延伸

这页重点讨论软件 agent 的 harness，但同样的控制逻辑也能延伸到 AI for AI 的研究系统里。

- 研究型 harness 包住的不只是编码任务，而是从假设到实验的整个闭环。
- 更稳定的模式仍然相同：约束生成、运行有边界的实验、保存结构化结果、把结果反馈到下一轮。
- 在这种场景里，对人类先验知识的检索，以及把失败实验转成可复用经验的 analyzer，都应被视为 harness 组件，而不只是记忆工具。

这带来一个有用区分：

- context system 决定有哪些信息可用
- harness system 决定循环如何推进，以及什么才算合格证据

具体例子见 [AI 自演化研究 Harness](ai-self-evolution-research-harnesses.md)。

## 开放问题

来源材料最后提出了一个更宽的判断：补偿面不只是在移动，它甚至可能从纯执行控制向更一般的基础设施外扩，例如主动时机控制、适配性权限系统，以及类似插件的扩展点。

## 来源依据

- [Harness Engineering 来源](../../../raw/external/一文读懂%20Harness%20Engineering：从%2014%20篇工程文章中，寻找那个让%20AI%20不再离经叛道的壳.md)

## 相关页面

- [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)
- [Agent 系统作为 OS 与 Cloud Runtime 问题](agent-runtime-os-cloud-runtime.md)
- [coding agent 的上下文压缩工作流](coding%20agent%20的上下文压缩工作流.md)
- [本地知识库模式](../context-memory-knowledge-system/local-knowledge-base-patterns.md)
- [知识库运行模型](../context-memory-knowledge-system/knowledge-base-operating-model.md)
- [AI 自演化研究 Harness](ai-self-evolution-research-harnesses.md)
- [Pi coding agent：一种极简且可观察的 coding harness](pi-coding-agent-harness.md)
