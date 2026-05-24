# multica 与 clawhouse 的目标与核心价值差异

## 摘要

`multica` 和 `clawhouse` 表面上都在处理“分散在不同地方的 coding agent 应该怎样被访问和使用”这个问题，但它们真正定义的产品对象并不一样。

`clawhouse` 更像一个面向单用户、多设备场景的 agent launcher 与运行时工作台。按最新澄清，它最原始的动机其实非常直接：无论身在何处，都能访问“我的 agent”。当你离开原来的桌面后，能不能继续回到那台机器上的 agent，并看清它此刻到底在做什么，是这个动机展开后的具体要求。

`multica` 则更像一个面向团队任务流的 managed agents platform。它最关心的不是“我怎么连回我的 agent”，而是“一个团队怎样把 agent 当作真正的队友来分配任务、跟踪进展、沉淀技能和共享算力”。

因此，两者的差别不主要在功能清单，而在第一性目标和核心价值承诺。

## 目标差异

### 1. `clawhouse` 的目标首先是让 agent 成为可随身访问的对象

从当前设想和后续澄清看，`clawhouse` 要解决的首先不是抽象的“连续性”，而是更第一性的访问权问题：agent 还没有像账号、文件或云服务一样成为一种可随身访问的对象。

它在个人多设备环境中具体表现为连续性断裂。

静态文件可以同步，但运行时上下文不会自然同步。用户真正缺的是：

- 现在是哪台机器在跑任务
- 那台机器上的 agent 进行到哪里
- 项目和测试处于什么状态
- 手机和平板上如何无痛接回原来的工作现场

所以它的目标更像：

> 让用户无论身在何处，都能重新进入并继续使用自己的 agent。

统一入口、移动端可用和可观察，都是为这个目标服务的实现条件。这里的核心单位是“设备上的 agent 节点”与“节点上的项目运行时工作面”。

### 2. `multica` 的目标是把 agent 纳入团队任务系统

`multica` 的目标更靠组织层。

它不是先从“多设备访问”出发，而是先从“agent 应该像同事一样进入团队协作系统”出发。它要解决的是：

- agent 怎样像成员一样被分配 issue
- agent 执行任务时怎样持续更新状态和进度
- 本地 daemon 和云端 runtime 怎样统一接入
- 团队怎样复用 agent 在过去任务里形成的 skills

所以它的目标更像：

> 把 coding agent 从个人工具升级成团队工作流里的原生执行者。

这里的核心单位不是单台设备，而是 `workspace / issue / agent / runtime / skill` 这一整套协作对象。

### 3. 一个偏“回到原工作现场”，一个偏“重新定义工作组织方式”

如果再压缩一层，可以把目标差异概括成：

- `clawhouse` 更像在修复个人工作流中的断点。
- `multica` 更像在重写团队如何分工与调度 agent。

前者首先解决 continuity problem，后者首先解决 coordination problem。

## 核心价值差异

### 1. `clawhouse` 的核心价值是可达性加可观察性

`clawhouse` 最核心的价值，不是“能发消息给 agent”，而是：

- 让 agent 变成一种你走到哪里都能接回来的对象
- 让原来那台机器上的 agent 可达
- 让它的设备状态、项目状态、任务状态可见
- 让移动端看到的不只是聊天回执，而是运行时现场

换句话说，它交付的是一种更好的默认工作面。

它承诺给用户的价值是：

> 即使人离开了桌面，仍然能从手机或平板继续进入并使用自己的 agent，而不是把 agent 留在原来的那台机器上。

### 2. `multica` 的核心价值是 agent 协作基础设施

`multica` 的价值更重，也更组织化。它不只是让 agent 可见，而是让 agent 成为任务系统里的原生角色。

它承诺的价值包括：

- 可以把 issue 直接分配给 agent
- agent 会经历可追踪的任务生命周期
- 任务进展通过 WebSocket 持续同步到工作台
- skills 会被沉淀和复用
- runtime 可以统一接入和管理

所以它真正卖的不是“多设备入口”，而是：

> 一个让人类和 agent 在同一任务系统里协同工作的基础设施层。

### 3. `clawhouse` 的 magic 更偏“即时掌控感”，`multica` 的 magic 更偏“组织杠杆”

如果从用户主观体验来区分：

- `clawhouse` 的 magic 在于，你打开手机就能立刻知道哪台机器、哪个 agent、哪个项目现在是什么状态，黑盒感显著下降。
- `multica` 的 magic 在于，agent 不再像一次性工具，而像可以持续协作、被分配、被追踪、会积累能力的组织成员。

前者更像提升 control surface，后者更像提升 organizational leverage。

## 为什么它们会看起来相似

两者看起来相似，是因为它们共享了几条中间层机制：

- 都承认 agent 不只是一个聊天窗口
- 都需要某种 runtime / daemon / server 层
- 都需要把执行中的状态显式化
- 都在试图摆脱“聊天软件里的黑盒代理”形态

但这些更像相同的工程手段，而不是相同的产品目标。

## 一个更清楚的区分方式

可以把两者分别理解成：

- `clawhouse`：面向个人多设备场景的 agent access + observability layer
- `multica`：面向团队任务流的 managed agents orchestration layer

这个区分也解释了为什么你会觉得 `multica` “更近一步”。

不是因为它单点功能一定全面超过 `clawhouse`，而是因为它已经把 runtime 接入、任务分配、状态同步、workspace 和 skill 复利这些层收进了同一个系统叙事里。

但反过来说，这也意味着它未必天然最优地解决 `clawhouse` 最尖锐的那个问题：移动端上，如何以最清晰、最低摩擦的方式重新进入某台具体设备上的 agent 工作现场。

## 如果已经有 multica，clawhouse 还有没有意义

从当前本地材料看，答案是：有，但前提是 `clawhouse` 不去和 `multica` 正面做同一个“团队任务系统”。

如果 `clawhouse` 只是想证明“多设备 agent 可以被统一接入、被分配任务、被看见在线状态”，那它和 `multica` 的重叠已经很高，意义会迅速下降。

但如果 `clawhouse` 把自己收束成下面这个问题，它仍然有很清楚的存在空间：

> 当用户离开原来的桌面设备后，怎样在手机或平板上以最低摩擦重新进入并继续使用那个 agent，而不是把它留在原地。

“可靠判断它此刻到底在做什么”是这个问题的第二层，而不是第一层。当前看，这仍然不是 `multica` 当前材料里最中心的承诺。

## multica 已经 address 了多少黑盒问题

基于当前本地证据，`multica` 不是完全忽略黑盒问题。

已有材料明确显示它至少承诺了这些可见性：

- agent 的任务生命周期是显式的，有 `enqueue -> claim -> start -> complete/fail`
- 任务进展会通过 WebSocket 实时推回前端
- agent 会出现在 board 上，能评论、改状态、报告 blocker
- runtime 是被显式注册和展示的，用户能看到机器作为 active runtime 存在
- 平台强调 execution monitoring，而不是只强调 prompt 发送

所以严格说，`multica` 已经在解决“agent 完全不可见”这个问题。

但当前本地材料还没有证明另一件更强的事：

> 用户是否能像看一个真实工作台那样，看见 agent 执行中的关键运行时内容。

也就是，目前还看不出它是否稳定暴露了这些东西：

- 实时命令输出
- 测试流和失败点
- `git status`、分支、diff 级变化
- 当前打开的是哪个项目工作树
- 本机资源状态和 agent 使用的具体设备环境
- agent 此刻为什么卡住、卡在哪个子步骤

README 里有 “real-time progress streaming” 和 “execution monitoring”，但这更像证明它有状态流和任务监控，不足以证明它已经把 agent 从黑盒变成了高分辨率、可诊断的运行时工作面。

因此，更准确的说法不是 “multica 没有 address 黑盒问题”，而是：

> `multica` 已经 address 了任务层的黑盒问题，但是否 address 了运行时现场层的黑盒问题，当前证据还不够。

## clawhouse 可能提供的独特价值

如果要让 `clawhouse` 有独特价值，它最有希望的方向不是比 `multica` 更像“另一个 agent team platform”，而是比 `multica` 更彻底地把 agent 工作现场显式化。

当前最可能的独特价值有四条。

### 1. 面向“具体那台机器”的高分辨率可观察性

`multica` 的 runtime 视角更像平台资源视角，而 `clawhouse` 可以把重点放在“实验室台式机上的这个 agent 此刻在这个 repo 里做什么”。

这是一种更贴近个人真实使用现场的 observability：

- 哪个 repo
- 哪个 worktree
- 哪个分支
- 当前测试到哪里
- 生成了哪些页面或文件
- 设备 CPU、内存、uptime 和 agent 任务并列展示

### 2. 移动端优先的 re-entry 体验

`clawhouse` 的问题定义从一开始就是手机和平板场景，而 `multica` 当前叙事更像桌面上的团队工作台。

如果 `clawhouse` 能把“掏出手机，十秒内重新接回原任务现场”做到极致，它就不是 `multica` 的弱化版，而是在优化另一条关键体验曲线。

### 3. 项目级 dashboard，而不是只停留在任务卡片和状态流

`multica` 当前材料更强调 issue、board、status、runtime、skills。

`clawhouse` 如果继续强化“每个项目都能由 agent 动态编译出一个 dashboard”，那它提供的就不是任务系统视图，而是项目运行时视图。这个视图更适合回答：

- 现在最该看什么
- 当前项目哪里坏了
- 下一步接管应该从哪开始

### 4. 可信可见，而不只是可协作

你现在最敏感的一点，其实不是“agent 能不能接任务”，而是“我能不能相信它真的按我理解的方式在工作”。

这会把 `clawhouse` 推向一个更尖锐的价值主张：

> 不只是让 agent 成为队友，而是让 agent 的工作过程足够可见，所以用户敢把任务真正交给它。

这条价值和 `multica` 的团队协作价值并不相同。

## 当前判断

基于当前本地材料，一个简化但有用的判断是：

> `clawhouse` 优先优化“我如何继续我的 agent 工作”，`multica` 优先优化“我们如何把 agent 纳入团队工作系统”。

这两者并不冲突，甚至可能是上下游关系。

如果 `clawhouse` 往前长，它可能会进入 `multica` 的 territory；如果 `multica` 往移动端和单用户多设备场景继续打磨，它也可能吃进 `clawhouse` 的核心问题。

但在当前定义下，它们的第一性目标和核心价值仍然是不同的。

如果要把这条判断再压缩成一句对产品决策最有帮助的话，那就是：

> `clawhouse` 只有在“让 agent 真正成为可随身访问对象”这件事上，比 `multica` 做得明显更好时，才有强存在意义。

## 来源依据

- [Clawhouse：多设备 Agent 的统一入口与运行时工作台](clawhouse-多设备-agent-工作台.md)
- [multica-ai/multica 仓库地图](../knowledge/multica-ai-multica-repo-map.md)
- [multica GitHub repo snapshot](../../raw/external/github-repo-multica-ai-multica.md)

## 相关页面

- [Clawhouse：多设备 Agent 的统一入口与运行时工作台](clawhouse-多设备-agent-工作台.md)
- [multica-ai/multica 仓库地图](../knowledge/multica-ai-multica-repo-map.md)
- [Claude Code、Codex 与 pi 的 harness 对比](../knowledge/coding-agent-harness-comparison.md)
