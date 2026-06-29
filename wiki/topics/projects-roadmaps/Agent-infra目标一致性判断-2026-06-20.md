# Agent infra 目标一致性判断（2026-06-20）

## 摘要

当前问题不是 `founder-skill`、`oh-share-it` 和 agent infra / context infra 风马牛不相及，而是它们必须被放回同一张分层图里。

压缩判断：

> `context-core` 是主线核心，`oh-share-it` 是真实部署和评测面，`my-little-agent-loop` / `agent-harness-core` 是 runtime ownership 支撑；`founder-skill` 只有在作为真实 workload、eval corpus 或 human-first workflow case 时才服务主线，不能膨胀成独立 founder product 主线。

## 当前主线

本库已有路线已经把目标压成：

> 构建一个 eval-first 的 agent context infrastructure 系统，覆盖 context core、shared context layer、trace / replay / evaluator loop、真实试点、部署与失败驱动迭代。

所以判断一个项目是否有利于最终目标，不看它表面是不是“产品”，而看它是否补强这条链路里的某一层：

| 层 | 项目 | 作用 |
|---|---|---|
| Context layer | `context-core` | 上下文写入、组织、路由、打包、trace、eval、writeback |
| Deployment / trial layer | `oh-share-it` | 多人共享知识、真实问题、路由质量、团队试点 |
| Runtime / harness layer | `my-little-agent-loop` 或 `agent-harness-core` | tool use、permission、trace、replay、evaluator loop |
| Workload / eval case layer | `founder-skill` | 提供高价值、非玩具的 founder workflow 任务和 human-first 判断边界 |

只有前三层是主线工程。第四层是输入源、测试场和案例，不应成为同等主线。

## `oh-share-it` 为什么不跑偏

`oh-share-it` 表面像公共知识库产品，但它的真实价值在 context infra：

- 多人知识有 owner、source、scope、visibility 边界。
- query 需要按场景加载不同层、不同人、不同版本的 context。
- 冲突观点不能被简单合并，需要保留 tension。
- agent 需要稳定的 external context provider，而不是临时搜索一堆文件。

因此 `oh-share-it` 最适合证明：

- context layer 可以进入真实协作场景；
- routed context 可以被评测；
- knowledge governance 可以变成 agent-facing tools；
- context infra 不只是个人记忆，而是多人协作里的可治理基础设施。

它不是偏离 agent infra，而是把 `context-core` 从本地设计推到真实部署面的关键项目。

## `founder-skill` 的正确位置

`founder-skill` 更危险，因为它很容易变成另一条产品线。

它服务主线的方式不是“做一个 founder 产品”，而是提供一组高质量 workload：

- Idea / MVP 阶段的证据整理；
- founder 判断、假设、反证、scope、metrics 的状态管理；
- AI 作为 evidence / state / contradiction backstop，而不是 AI coach；
- human-first workflow 中哪些判断不能外包给 agent。

这些 workload 对 agent infra 有价值，因为它们能测试：

- context 是否能保留判断边界；
- trace 是否能解释一次建议或结论来自哪里；
- replay 是否能复现同一 founder case 的状态演化；
- evaluator 是否能区分有用的证据整理和有倾向性的 AI 引导。

但如果 `founder-skill` 开始要求完整产品、完整交互、完整市场定位和独立增长路径，它就会稀释主线。它应被当作 case / workload / eval suite，而不是和 `context-core`、`oh-share-it` 并列的旗舰。

## 风险判断

当前真正的风险不是项目之间完全无关，而是层级没有写在工作台上。

如果每天的执行项长这样，就容易跑偏：

- 今天改 `founder-skill` 产品体验；
- 明天改 `oh-share-it` UI；
- 后天又想一个新的 agent app。

如果每天的执行项长这样，就仍然在主线内：

- 从 `founder-skill` 抽 5 个真实 workflow task，转成 `EvalCase`；
- 用 `oh-share-it` 跑 15 到 20 个真实 query，记录 routing failure；
- 让 `context-core` 生成 `ContextBundle` 和 `Trace`；
- 用 harness replay 同一批 case，标注失败来自 retrieval、routing、context packaging、tool execution 还是 model judgment。

## 外部教育 demo 的位置

如果一个外部教育项目已经从泛泛合作变成明确的 demo 交付，它不必自动视为偏离主线。关键要看它承担的是哪一层。

它服务主线的方式不是把自己升级成“教育产品 founder”，而是提供一个真实 workload 和 deployment 约束：

- 真实学生 / 老师 / 机构场景；
- 学情、题目、错因、反馈报告等结构化对象；
- 低并发但真实使用的 demo；
- 可记录的失败案例、人工接管边界和反馈闭环；
- 从 demo 走向多人试点时暴露出的可靠性、权限、数据、成本和观测问题。

这类项目在 10 到 100 人量级内，可以作为 `Agent Systems Engineer` 主线的训练场。它补的不是“大型后端工程师”身份，而是从产品定义、数据建模、AI workflow、eval、trace、deployment boundary 到 real usage 的一组系统证据。

但它开始偏航的信号也很明确：

- 主要时间被教培运营、销售、渠道和交付细节吃掉；
- demo 目标从验证核心诊断假设，膨胀成完整教育平台；
- 需要承诺生产级稳定性、万人级并发、合规安全和 SRE 责任；
- 没有沉淀 `EvalCase`、trace、failure taxonomy、context schema 或 case study；
- 无法解释这段工作如何回到 `context / harness / eval / reliability`。

因此更稳的边界是：

> 可以接 demo 与架构验证，不能把自己包装成生产级后端负责人；可以补后端基础，不能把万人级扩展能力当作短期个人承诺。

如果 demo 顺利，应尽早引入有生产级系统经验的人。自己的位置保留在产品定义、数据结构、AI workflow、验证指标、失败分析和原型架构上，同时借这个项目补齐最小后端工程常识。

## 下一步收束

建议把接下来两周的判断标准改成一句话：

> 每个项目必须产出一个能进入 `context-core / oh-share-it / trace-replay-eval` 闭环的证据对象。

具体切法：

1. `context-core`：只做最小对象模型与 context bundle / trace / eval case。
2. `oh-share-it`：只做真实问题集、routing eval、部署或半部署试点。
3. `founder-skill`：只抽取 5 到 10 个 founder workflow case，变成 eval workload，不做独立产品扩张。
4. `my-little-agent-loop` / `agent-harness-core`：只做 trace、replay、evaluator loop，不追完整 Codex-like 产品。

这样解释时，外部叙事不是“我做了一堆产品”，而是：

> 我在用真实产品场景压测 agent context infrastructure：从 context routing，到多人部署，到 trace / replay / eval，再到 failure-driven iteration。

## 相关页面

- [Agent 系统月度执行计划（2026-05-24 至 2026-06-21）](Agent系统月度执行计划-2026-05-24.md)
- [Agent 系统求职与项目路线图（2026-05）](Agent系统求职与项目路线图-2026-05.md)
- [Codex-like agent harness 路线图](Codex-like-agent-harness路线图.md)
- [Agent harness core 与三种 adapter 路线](Agent-harness-core与三种adapter路线.md)
- [oh-share-it 公共知识库产品](../research-knowledge-governance/oh-share-it公共知识库产品.md)
- [The Founder's Playbook：AI-native startup 的阶段纪律](../ai-product-product-definition/the-founders-playbook-ai-native-startup.md)
- [Context-Core 技术前沿调研报告（2026-05-25）](../context-memory-knowledge-system/context-core-technical-frontier-2026-05-25.md)
