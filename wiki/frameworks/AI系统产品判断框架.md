# AI 系统产品判断框架

这页服务于 AI 产品、agent、runtime、workflow、tool use、任务委托这类问题。

## 先看什么

遇到 AI 系统问题时，优先先问五件事：

1. 这是 AI-assisted building，还是 AI runtime
2. 任务主要需要共识，还是非共识判断
3. 当前最难的是模型、runtime、还是契约
4. 这个场景真需要 agent，还是 workflow / RAG 已经够用
5. 人真正该保留的判断权在哪里

## 核心判断

### 1. 判断 AI 产品层级，先看 runtime，不看 build-time

很多 demo 是 AI 帮忙做出来的，但用户使用时 AI 并没有真实参与系统运行。判断是不是 AI 产品，关键看 AI 是否在 runtime 中承担理解、判断、调用工具和维护状态的责任。

主要依据：
- [AI 产品六层与 L3-L6 能力分层](../knowledge/AI 产品六层与 L3-L6 能力分层.md)

### 2. 真正的工程黑洞常在 runtime 与契约层

很多团队以为问题在模型或 API，实际耗时常死在：

- 状态管理
- 工具调用
- 上下文调度
- 验收标准
- 人工接管边界

主要依据：
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../knowledge/AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md)

### 3. 先判断任务要的是共识还是非共识

GenAI 更擅长压缩训练语料里的共识，不擅长稳定产出真正稀缺、反共识、决定方向的判断。

所以高价值做法常常不是“全部外包”，而是把共识化子任务交给 AI，把价值定义、品味和非共识下注留在人手里。

主要依据：
- [GenAI 的共识边界与任务委托框架](../knowledge/GenAI 的共识边界与任务委托框架.md)

### 4. 不是所有问题都值得上 agent

如果单轮调用、RAG 或固定 workflow 已经足够，就不该为了“更像 AI”而强行加 agentic 复杂度。

主要依据：
- [AI 产品六层与 L3-L6 能力分层](../knowledge/AI 产品六层与 L3-L6 能力分层.md)
- [Harness Engineering（约束壳工程）](../knowledge/harness-engineering.md)
- [Thin Harness, Fat Skills](../knowledge/thin-harness-fat-skills.md)

### 5. 人最该保留的是价值判断，不是机械步骤

AI 最适合接手的是 transformation、整理、草拟、重复执行；最不该轻易交出的，是：

- 成功标准
- 品味
- 优先级
- 风险边界
- 反共识判断

主要依据：
- [GenAI 的共识边界与任务委托框架](../knowledge/GenAI 的共识边界与任务委托框架.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../knowledge/AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md)

## 常见张力

- AI-assisted building vs AI runtime
- wrapper / RAG / workflow / agent
- 过程确定性 vs 结果确定性
- 共识任务 vs 非共识任务
- 自动执行 vs 人工接管

## 推荐阅读顺序

1. [AI 产品六层与 L3-L6 能力分层](../knowledge/AI 产品六层与 L3-L6 能力分层.md)
2. [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](../knowledge/AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md)
3. [GenAI 的共识边界与任务委托框架](../knowledge/GenAI 的共识边界与任务委托框架.md)
4. 如涉及控制壳，再读 [Harness Engineering（约束壳工程）](../knowledge/harness-engineering.md)

## 什么时候进入 bridge

如果问题已经具体到某个产品、仓库、团队或方案取舍，再进入相应 `bridges/` 页面做具体判断。

## 相关页面

- [框架路由入口](router.md)
- [Harness 架构判断框架](Harness架构判断框架.md)
- [产品定义判断框架](产品定义判断框架.md)
- [产品验证判断框架](产品验证判断框架.md)
- [让 query 真正调用判断框架](让query真正调用判断框架.md)
