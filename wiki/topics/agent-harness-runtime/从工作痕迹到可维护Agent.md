# Agent 隐藏式工作平台：从自动化工具转向人的默认工作面

## 本轮纠正

上一版把想法理解成：用户继续在现有应用里工作，后台 agent 观察工作痕迹、发现重复流程、生成 workflow 或 agent，再通过回放、确认和逐级授权投入运行。

这套理解可以减少“搭自动化”的成本，但仍然把自动化系统当成产品主语。用户仍要面对候选流程、agent、权限升级和自动化维护，只是从亲手搭建变成审核系统替自己搭建的结果。它本质上仍然是更聪明的自动挡改装工具，没有改变人的默认工作平台。

用户真正想表达的是另一层产品：

> 给人一个直接完成工作的工作平台。人的主任务、项目和内容站在前台；agent、workflow、context routing 与工具编排退到最后，成为平台内部持续运行的能力。用户不再学习如何使用 agent，而是在自然工作时直接得到 agentic system 的能力。

## 本质差异

| 维度 | 上一版理解 | 用户当前理解 |
|---|---|---|
| 产品主语 | 自动化与 agent | 人的工作、项目和内容 |
| 用户动作 | 发现、确认、部署和管理自动化 | 直接阅读、写作、研究、决策和推进项目 |
| agent 的位置 | 产品对象，即使由系统自动创建 | 平台内部实现，默认不进入用户心智 |
| context 的用途 | 从历史行为中挖掘重复流程 | 持续理解人当前在做什么、为什么做、下一步需要什么 |
| proactive 的表现 | 给出候选自动化或主动通知 | 在工作发生的当下调整信息、界面与执行，不等人主动调用 agent |
| 成功标准 | 自动化数量、节省时间、运行成功率 | 从人的意图到结果之间还剩多少翻译、切换、配置和管理负担 |

所以差异不是 agent 是否藏在后台，而是用户是否仍然需要进行一层关于 AI 的元工作。

如果用户还要想“该不该调用 Codex”“该用哪个 agent”“怎样写 prompt”“是否要把这段流程自动化”“这个 automation contract 怎么配置”，那么 agent 即使运行在后台，仍然占据了人的工作心智。

真正隐藏以后，用户面对的只应是工作对象本身。系统根据当前内容、历史、项目状态和自然行为，决定该读取什么 context、调用什么工具、组合哪种 workflow、是否需要 agent，以及结果应该怎样回到当前工作面。

## 三个词在这里的具体含义

`frictionless interaction` 不是少点几次按钮，而是不要求用户离开正在做的工作，把自己的意图翻译成 prompt、workflow、agent 配置或知识库维护命令。系统学习所需的信号也应来自真实工作自然产生的痕迹，不能额外要求用户持续标注和训练它。

`contextual intelligence` 不是后台保存更多历史，而是平台对当前工作对象、项目阶段、相关材料、最近变化和用户协作方式保持持续有效的理解，使用户不必每次重新解释局面。

`proactive intelligence` 不是更频繁地弹提醒，而是系统能在用户显式调用之前判断当前需要什么，并以最低打扰方式改变工作面、准备结果或继续执行。主动性的质量取决于它是否减少人的中断，而不是它是否经常出现。

## “隐藏”不等于黑盒

agent 退到幕后，指的是操作上隐藏，不是机制上不可检查。

默认工作面不应让人管理 agent、session、prompt 和 workflow；但当系统遇到异常、需要不可逆权限、输出影响重大，或者用户主动追问时，仍应能够展开来源、执行轨迹、权限和接管入口。

这和自动挡汽车更接近：驾驶者不需要换挡，但变速系统仍然可诊断、可维修，也会在异常时暴露状态。隐藏的是日常操作负担，不是用户的知情权与最终控制权。

## 为什么 Codex 与 Power Automate 还没有解决它

Codex、Power Automate、workflow mining 和 agent builder 都可以成为这个平台的底层能力，但它们当前主要仍是用户需要主动进入和操作的工具。

它们回答的是“怎样把一项工作交给 AI 或自动化”；这个想法要回答的是“怎样让人的正常工作天然处于一个会理解、会预判、会执行的环境里”。

前者让人学会驾驶更强的工具。后者试图让 agentic capability 变成工作平台的环境属性，就像保存、搜索、同步不再被当作一个需要每次单独调用的工具。

## 用 gogo 场景具体化

当前 `gogo` 把 Wiki 和 Agent 放进了同一个界面，已经减少了 Obsidian 与 Codex 之间的切换，但它仍然是“Wiki + Agent”。用户仍能感觉到自己在浏览知识库，或者切到聊天里调用 agent；`ingest`、`write-back`、`lint` 等维护动作也仍然需要显式触发。

按当前理解继续演化，产品不应只是把这些命令自动执行，而应让它们从用户任务中消失。用户只负责阅读、捕获材料、写草稿、修改判断和推进项目；系统在背后自然完成材料归属、context 组织、相关内容带回、知识库维护和必要的 agent 执行。结果直接回到当前文章、项目或工作状态，而不是另开一个 agent 对话等待用户处理。

这时 `gogo` 的主语也不再是“llm-wiki 的 Agent 入口”，而是人的知识工作平台。`llm-wiki`、Pi、Codex、skills、schemas 和维护脚本都变成实现该工作体验的 substrate。

## 实时会议场景：谈话直接产生证据与作品

会议谈话可以被这套范式覆盖，而且比“后台挖掘重复工作流”更能说明它的独特性。

会议不是交给 agent 分析的一份录音材料，而是人正在工作的实时界面。参与者只负责谈问题、交换判断和形成想法；平台持续理解当前讨论、项目历史和相关资料，在后台识别两类可行动信号。

第一类是事实缺口。有人问到一个数据、案例或已有方案时，系统可以立即搜索、交叉核对，并把来源和结论放到当前讨论旁边。参与者不需要停下来打开浏览器、切到聊天框或指派“帮我查一下”。

第二类是可物化的想法。当讨论已经出现足够具体的对象、行为和预期效果时，系统可以在隔离环境里生成一个小 demo、图表、交互界面或代码原型，并在适合的时点把结果放回共享工作面。参与者看到的是想法已经有了可操作的形状，而不是某个 agent 完成了一项任务。

```text
自然谈话
-> 持续对话与项目 context
-> 识别事实缺口 / 可物化想法
-> 后台搜索或 sandbox build
-> 证据卡 / demo / 动态界面回到当前讨论
```

这个过程同时体现三种能力：谈话本身就是输入，所以不需要 prompt 或 delegation；系统知道当前问题为什么重要，所以检索和 demo 不是脱离语境的生成；系统在被明确调用前开始准备结果，所以具有主动性。

但“谈到一个想法”不能自动等于“用户要求正式实现”。会议里有大量玩笑、试探、反例和未完成表达。更合理的边界是：系统可以在 sandbox 里积极试做可丢弃的结果，但对人的注意力保持克制，对发布、发送、写入正式项目和改变外部状态保持保守。

因此这个场景最重要的交互原则是：

> 后台可以积极试做，前台必须克制打扰；低风险结果可以主动出现，外部承诺仍需明确的人类决定。

这也解释了为什么输出 UI 不会消失。agent 可以隐藏，但搜索证据、比较结果和 demo 需要以适合当前讨论的结构化界面出现。真正消失的是调用 agent 的输入界面，而不是人用来理解和判断结果的工作面。

## 架构策略：会议模式是第一个 adapter

会议 MVP 与长期通用工作台不必共享完整产品界面，但应共享同一条内部协议：`work event -> opportunity -> run -> artifact`。

```text
Meeting Adapter: audio / transcript
Future Adapters: file / browser / IDE / canvas
                    |
                WorkEvent
                    |
        Context Builder + Opportunity Detector
                    |
             Action Runtime
          search / build / analyze
                    |
                Artifact
       evidence / demo / chart / diff
                    |
          Dynamic Work Surface
```

第一版只需要四个稳定对象。

- `WorkEvent`：人在真实工作里自然产生的事件，包括来源、时间、参与者、文本或对象引用。会议里的 transcript segment 是第一种 event。
- `Opportunity`：系统从若干 events 中识别出的可行动机会，记录 `lookup` 或 `build` 类型、所依据的原话、所需 context、置信度、风险和是否值得现在打扰。
- `Run`：后台搜索或 sandbox build 的一次执行，承接状态、工具、trace、失败和取消。
- `Artifact`：返回工作面的成果，不是 agent 消息。第一版只有带来源的 `EvidenceCard` 和可打开的 `HTMLDemo`，以后再扩展为文档、图表、diff、任务状态和生成式 UI。

同时需要三组可替换接口。

- `InputAdapter` 把会议、文件、浏览器、IDE 和画板转成统一的 `WorkEvent`。
- `ActionProvider` 把搜索、编码、数据分析和确定性工具接入同一个 runtime。
- `SurfaceRenderer` 把不同 `Artifact` 放回会议侧栏、项目页、文档、画板或 IDE，而不是统一塞进聊天框。

`Context Builder`、`Opportunity Detector`、`Action Runtime`、`Artifact Store`、attention / permission policy 和 trace / eval 才是长期共用的底座。会议转写、日历、参会人管理和会议纪要模板都属于会议 adapter，不应进入 core。

### 一天可完成的会议 MVP

明天可用的版本只做一个网页：开始 / 暂停麦克风转写，读取一份预先上传的项目 brief，每隔一小段对话判断是否出现事实问题或足够具体的可演示想法。

事实问题调用现成搜索能力，产出带来源的 evidence card；可演示想法把最近几分钟对话和项目 brief 交给现成 coding agent，在隔离目录中生成单页 HTML demo。右侧工作面只展示这两种成果，不提供 agent chat、workflow editor 或 agent 管理界面。

为了明天可用，V0 不做跨会议 memory、全局屏幕观察、多用户编辑、自动发布、通用工具编排和个性化学习。它只验证一个完整体验：用户正常谈话，系统不经显式指派，能在相关时点带回一条真正有用的证据，或一个足以继续讨论的 demo。

这个实现以后可以这样扩展：增加新的 `InputAdapter`，让文件编辑、浏览器阅读、IDE 操作和画板变化进入同一条 event pipeline；增加新的 `Artifact` 与 renderer，让结果回到对应工作对象。会议模式因此是通用工作台的第一种输入与输出形态，而不是必须独立发展的会议产品。

## 更准确的产品定义

> 一个以人的工作和项目为主语的 AI-native 工作平台。用户通过自然工作行为表达意图；平台持续维护当前 context，在合适时机主动准备信息、改变工作面或执行任务，并在内部调用或生成 agent、workflow 与工具。agent 默认不作为用户需要理解和管理的对象出现。

它不是 agent factory，也不是无代码自动化工具，更不是在传统软件旁边加一个聊天框。它要改变的是人的默认工作面：工作本身具备 context、prediction 与 agency。

## 真正需要验证的问题

这条产品路线最难的不是 agent 能不能执行，而是：人的自然工作痕迹是否足以让系统理解当前意图，而不要求额外配置；系统能否区分真实问题、探索性表达和应被忽略的闲谈；主动行为能否稳定减少中断，而不是制造新的审查负担；平台能否在隐藏 agent 的同时，让异常、风险与接管仍然清楚。

如果这三件事成立，自动挖掘和搭建 agent 只是底层能力之一。如果不成立，即使后台生成了很多高质量 workflow，产品仍然只是更自动的 agent builder，而不是新的工作平台。

## 相关页面

- [日历 + Agent：从时间管理工具到未来工作的委托协议](../ai-product-product-definition/日历作为Agent的自然委托协议.md)
- [gogo：本地 llm-wiki 桌面应用](../context-memory-knowledge-system/gogo.md)
- [给自己做了一个 llm-wiki 的入口应用](../context-memory-knowledge-system/essays/给自己做了一个llm-wiki的入口应用.md)
- [Agent 时代的人机交互新命题](agent时代的人机交互新命题.md)
- [后台守护进程式 Agent 与持续情境理解](后台守护进程式Agent与持续情境理解.md)
- [被持续委托的工作主体](被持续委托的工作主体.md)
- [AI Architect 的 Context Intelligence 镜头](../ai-product-product-definition/ai-architect-context-intelligence.md)
- [AI Architect 的 Proactive Intelligence 镜头](../ai-product-product-definition/ai-architect-proactive-intelligence.md)
- [工作面摩擦敏感观察](../../self/工作面摩擦敏感观察.md)
- [产品探索保真优先观察](../../self/产品探索保真优先观察.md)
