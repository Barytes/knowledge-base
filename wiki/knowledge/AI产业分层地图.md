# AI 产业分层地图（2026）

## 背景

围绕“怎么了解 AI 市场”这个问题，一个更自然的入口不是先枚举公司，而是先建立一张产业分层地图。

因为公司是点，产业结构是面。先有面，再看点，认知负担会明显下降。

这页尝试基于一组截至 `2026-04-23` 的公开材料，压出一版足够好用的 AI 产业地图。

需要先说明两点：

1. 这不是严格意义上的“上下游产业链”图。AI 更像一个 **分层堆栈**，层与层之间既有依赖，也有打包、替代与平台化关系。
2. 这页明显带有时间性。尤其是融资分布、企业支出重心与模型竞争格局，未来很可能继续快速变化。

---

## 核心判断

如果把今天的 AI 市场压成一句话，可以写成：

> **AI 产业更像“算力 -> 模型 -> 推理/训练基础设施 -> 数据与运行时基础设施 -> 工作流应用 -> 行业系统重写”的分层结构，而不是一条简单的线性上下游。**

进一步说，今天至少可以看到三个同时成立的趋势：

1. **VC 的钱最集中在底层，尤其是 frontier labs 与 compute。**
2. **企业的真钱更快流向上层，尤其是 coding、copilot、vertical ROI 场景。**
3. **中间层仍在早期，runtime、eval、observability、agent orchestration 还没有完全定型。**

---

## 为什么不用“线性上下游”来理解

传统产业链常常是：

- 原材料
- 零部件
- 组装
- 渠道
- 终端产品

但 AI 更复杂。原因包括：

- 同一家公司可能同时做模型、产品和分发
- 上层应用会反过来塑造底层模型需求
- 数据、runtime、评测、安全不是单纯“上游供货商”，而是横向渗透多层
- 企业用户在买的往往不是模型本身，而是“某个工作流被重写后的结果”

因此，与其问“谁在上下游”，不如先问：

- 这个生态主要分哪几层
- 每一层在创造什么价值
- 每一层的控制点和瓶颈在哪里

---

## AI 产业地图 1.0

### 第一层：算力 / 芯片 / 数据中心 / 电力

这是最底层的约束层。

它之所以重要，不只是因为有 GPU，而是 frontier model 的训练与部署已经高度受制于资本开支、数据中心能力与电力供给。

外部资料支持：

- [Stanford AI Index 2024](https://hai.stanford.edu/ai-index/2024-ai-index-report) 提到，`GPT-4` 训练计算成本约 `7800 万美元`，`Gemini Ultra` 约 `1.91 亿美元`。
- [Stanford AI Index 2025 - Research and Development](https://hai.stanford.edu/ai-index/2025-ai-index-report/research-and-development) 指出 notable AI models 的训练算力约每 `5` 个月翻倍，AI 硬件性能、价格性能和能效也持续提升。

这一层的典型玩家包括：

- 芯片与系统：`NVIDIA`、`AMD`、`TPU` 生态
- 云与集群：`AWS`、`Azure`、`GCP`、`Oracle`、`CoreWeave`
- 数据中心、电力与配套基础设施

这层的特点是：**资本密集、赢家通吃、对上层有强约束力。**

### 第二层：基础模型层

这是“智能供给层”。

它的核心不是某个聊天产品，而是谁能持续提供更强、更稳、更便宜、可集成的 intelligence。

外部资料支持：

- [Stanford AI Index 2025 - Research and Development](https://hai.stanford.edu/ai-index/2025-ai-index-report/research-and-development) 说，`2024` 年近 `90%` 的 notable AI models 来自 industry。
- 同页指出，`2024` 年美国机构产出了 `40` 个 notable AI models，中国 `15` 个，欧洲 `3` 个。

这层内部可以再分成两种生态：

- **闭源 API 模型**
  例如 `OpenAI`、`Anthropic`、`Google`
- **开源 / 开放权重模型生态**
  例如 `Llama`、`Qwen`、`DeepSeek`、`Mistral`、`GLM`、`Kimi`

当前更值得注意的不是“谁一定会赢”，而是：

- 企业侧更倾向闭源高性能模型
- 开发者与 startup 侧对 open-weight / 中国模型的试用和采用更活跃

### 第三层：训练 / 推理基础设施层

这一层负责把模型能力变成可规模化供给。

它包括：

- 训练系统
- 推理 serving
- 模型路由
- 推理加速
- 低延迟、低成本部署

[Menlo Ventures 2025: The State of Generative AI in the Enterprise](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) 把基础设施侧支出拆成：

- `foundation model APIs`：`125 亿美元`
- `model training infrastructure`：`40 亿美元`
- `AI infrastructure`：`15 亿美元`

同页点名的推理平台包括：

- `Fireworks`
- `Baseten`
- `Modal`
- `Together`

这层的本质是：**把“模型能力”工程化成稳定、经济、可复用的服务。**

### 第四层：数据与运行时基础设施层

这是模型真正进入工作流之前最容易被低估的一层。

它更接近：

- `runtime`
- `orchestration`
- `state management`
- `tool calling`
- `RAG`
- `eval / tracing / observability`
- `security / governance`

这层为什么重要，本地已有页 [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md) 已经给出很强解释：很多 AI 产品真正难的，不是模型层，而是运行时层对不确定性的吸收，以及契约层对“什么算完成”的定义。

外部资料也支持这一点：

- [OpenAI - The next phase of enterprise AI](https://openai.com/index/next-phase-of-enterprise-ai/) 明确强调 `Stateful Runtime Environment`、company-wide agents、与 `Databricks`、`Snowflake`、`AWS` 等系统的整合。
- [Menlo 2025 enterprise report](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) 指出，今天真正算得上“真 agent”的生产部署比例仍然不高：企业约 `16%`，startup 约 `27%`。多数系统仍然是 prompt、RAG、固定路由等较简单架构。

这一层的典型玩家包括：

- 数据与平台底座：`Databricks`、`Snowflake`、`MongoDB`、`Datadog`
- 向量与数据库：`Pinecone`、`Supabase`、`Neon`
- 开发框架与编排：`LangChain`
- Eval / tracing / observability：`Braintrust`、`Judgment Labs`

这层的核心张力是：

- 业务价值很大
- 市场结构还不稳定
- 护城河还在形成

### 第五层：通用应用层（horizontal AI）

这是“所有白领都可能用”的层。

它主要包括：

- `copilot`
- `assistant`
- `general-purpose agent platform`
- 个人生产力工具

[Menlo 2025 enterprise report](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) 的拆法里，horizontal AI 在 `2025` 年约 `84 亿美元`，其中：

- `copilot` 占 `86%`
- `agent platforms` 约占 `10%`
- 其余为个人生产力工具

典型代表：

- Copilot：`ChatGPT Enterprise`、`Claude for Work`、`Microsoft Copilot`
- Agent platform：`Salesforce Agentforce`、`Writer`、`Glean`
- 个人生产力：`Granola`、`Fyxer`

这一层的核心不是模型最强，而是：**能不能进入默认工作面，成为员工的日常入口。**

### 第六层：部门型工作流应用层（departmental AI）

这是某个岗位或部门的 killer use case 层。

按 [Menlo 2025 enterprise report](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)：

- 部门型 AI 约 `73 亿美元`
- 其中 `coding` 一项约 `40 亿美元`
- 占部门型 AI 的 `55%`

这也是当前最值得注意的现象之一：

> **coding 已经成为生成式 AI 第一个真正成立的 killer use case。**

同页还指出：

- `50%` 的开发者现在每天使用 AI coding tools
- 顶尖组织里这个比例达到 `65%`
- code completion 之外，`code agents` 和 `AI app builders` 在快速上升

这一层的典型玩家包括：

- `Cursor`
- `Claude Code`
- `Codex`
- `Lovable`
- `Replit`
- `OpenHands`
- `Graphite`
- `Meticulous`
- `Harness`

这一层的本质是：**把 AI 嵌进某类职业的完整工作回路。**

### 第七层：垂直行业应用层（vertical AI）

这是“行业知识 + AI workflow”层。

按 [Menlo 2025 enterprise report](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)：

- vertical AI 在 `2025` 年约 `35 亿美元`
- 其中医疗 alone 约 `15 亿美元`
- 占 vertical AI 的 `43%`

[Menlo 2025: The State of AI in Healthcare](https://menlovc.com/perspective/2025-the-state-of-ai-in-the-healthcare/) 进一步指出：

- 医疗 AI 部署速度已达 broader economy 的 `2.2x`
- 医疗 AI 支出约 `14 亿美元`
- 其中 `85%` 的 generative AI spend 流向 startup

这一层当前最强的行业包括：

- 医疗
- 法律
- 金融 / 会计
- 政府
- creator economy
- 药物发现 / 科学

这层的护城河通常不是模型本身，而是：

- 行业数据
- 合规与流程整合
- 真实 ROI
- 采购路径和切入 wedge

---

## 两个横切面

### 一、分发与渠道

AI 时代的分发已经不只是传统 enterprise sales。

更准确地说，今天至少有三种并行渠道：

- `consumer distribution`
- `PLG`
- `enterprise sales / partnerships`

外部资料支持：

- [OpenAI - Accelerating the next phase of AI](https://openai.com/index/accelerating-the-next-phase-ai/) 把自己的飞轮明确写成：consumer adoption、enterprise deployment、developer usage、compute。
- [Menlo 2025 enterprise report](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) 指出，AI 的 PLG 在企业里明显强于传统 SaaS，AI 应用层里有相当一部分支出来自 bottom-up adoption。

这意味着，分发不再只是销售问题，而是在很多场景里变成产品本身的一部分。

### 二、安全 / 治理 / 评测

这不是一层独立产品面，而是会横穿多层的能力面。

外部资料支持：

- [Stanford AI Index 2024](https://hai.stanford.edu/ai-index/2024-ai-index-report) 明确指出，领先模型在 responsible AI 上缺乏标准化评测。
- [Menlo 2025 enterprise report](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) 预测 explainability、governance、audit logs 会越来越重要。

这意味着：

- 安全不是大厂专属问题
- eval、audit、observability、policy compliance 会越来越成为基础设施的一部分

---

## 从“钱”来看，这张地图的结构是什么

如果只看 `2025-2026` 的公开资料，可以看到三种不同的钱。

### 1. VC 的钱

最集中在底层，尤其是 frontier labs 与 compute。

- [Stanford AI Index 2025 - Economy](https://hai.stanford.edu/ai-index/2025-ai-index-report/economy%C2%A0) 说，`2024` 年 corporate AI investment 达到 `2523 亿美元`，generative AI private investment 达到 `339 亿美元`。
- [Crunchbase Q1 2026](https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/) 则显示，`2026 Q1` AI 占了全球 venture funding 的 `80%`，而且高度集中在少数大公司。

### 2. 企业预算的钱

更快流向应用层。

- [Menlo 2025 enterprise report](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) 显示，企业 `2025` 年 generative AI 总支出约 `370 亿美元`，其中应用层 `190 亿美元`，基础设施层 `180 亿美元`。

### 3. 用户时间和注意力的钱

更偏 consumer 与工具默认入口。

- [a16z Top 100 Gen AI Consumer Apps - 5th Edition](https://a16z.com/100-gen-ai-apps-5/) 显示，consumer AI 的主流入口已经开始稳定，`ChatGPT`、`Claude`、`Perplexity`、`Cursor`、`Lovable`、`Replit` 等都在形成长期心智。

---

## 一个更实用的压缩版本

如果只为了建立方向感，而不是写行业报告，这张地图可以再压成四句话：

1. **最贵的是底层：算力与 frontier model。**
2. **最热的是上层：coding / developer workflow。**
3. **最早但重要的是中层：runtime / eval / observability / orchestration。**
4. **最明确见 ROI 的 vertical 是医疗。**

---

## 这张地图该怎么用

这页的意义，不是让人背公司名，而是让人先回答三个问题：

1. **哪一层的钱最多？**
2. **哪一层的结构还没定型？**
3. **哪一层最适合我的能力进入？**

如果把它用在职业判断上，一个很直接的后续动作是：

- 先选你想研究的层
- 再看这一层里有哪些典型玩家
- 再看这些玩家分别依赖上下哪几层
- 最后才看招聘和公司名单

也就是说，先看结构，再看公司。

---

## 限制

这页有几个边界需要保留：

1. **它更偏英文公开市场与美国企业资料。**  
   对中国本土 AI 产业的资本结构、商业化路径与政策约束，这里没有展开足够多。

2. **很多数字来自投资机构报告。**  
   这类报告有方法论价值，但也会带有自身视角、口径和投资偏好。

3. **这是一张“足够好用”的地图，不是唯一正确的地图。**  
   不同问题会需要不同切法。比如如果关心科研与国家竞争，地缘与政策层会更重要；如果关心求职，工作流层与应用层会更重要。

---

## 与现有知识的关联

- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md)：这页给出 `模型 / 协议 / 运行时 / 契约` 四层，能直接嵌入本页的中间层理解。
- [Claude Code、Codex 与 pi 的 harness 对比](coding-agent-harness-comparison.md)：这页更细地解释 `harness` 这类中间层到底在解决什么问题。
- [Agent 时代的人机交互新命题](agent时代的人机交互新命题.md)：可对应上层应用与判断界面的重写。
- [衰退期的创业环境与技术判断](衰退期的创业环境与技术判断.md)：这页提供“看一项技术是否在重写岗位和产业结构”的宏观标准。
- [求职范式转变：让工作找到你](求职范式转变：让工作找到你.md)：如果把这张产业地图用于职业定位，那页解释如何把自己组织成市场能识别的产品。

---

## 来源依据

以下材料为本页的主要外部依据，均为截至 `2026-04-23` 可访问的公开网页：

- [Stanford AI Index 2025 - Economy](https://hai.stanford.edu/ai-index/2025-ai-index-report/economy%C2%A0)
- [Stanford AI Index 2025 - Research and Development](https://hai.stanford.edu/ai-index/2025-ai-index-report/research-and-development)
- [Stanford AI Index 2024](https://hai.stanford.edu/ai-index/2024-ai-index-report)
- [Menlo Ventures - 2025: The State of Generative AI in the Enterprise](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)
- [Menlo Ventures - 2025: The State of AI in Healthcare](https://menlovc.com/perspective/2025-the-state-of-ai-in-healthcare/)
- [a16z - The Top 100 Gen AI Consumer Apps - 5th Edition](https://a16z.com/100-gen-ai-apps-5/)
- [OpenAI - The next phase of enterprise AI](https://openai.com/index/next-phase-of-enterprise-ai/)
- [OpenAI - Accelerating the next phase of AI](https://openai.com/index/accelerating-the-next-phase-ai/)
- [Crunchbase - Q1 2026 Shatters Venture Funding Records As AI Boom Pushes Startup Investment To $300B](https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/)
- [Crunchbase - Venture Funding To Foundational AI Startups In Q1 Was Double All Of 2025](https://news.crunchbase.com/venture/foundational-ai-startup-funding-doubled-openai-anthropic-xai-q1-2026/)

> 注：本页中的“产业地图”本身属于基于上述资料的综合推理，而不是任何单一来源原样给出的现成图。
