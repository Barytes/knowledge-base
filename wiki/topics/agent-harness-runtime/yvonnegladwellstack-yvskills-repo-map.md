# yvonnegladwellstack/yvskills 仓库地图

## 摘要

这页是围绕主题“Claude skill 的打包方式与对话机制”维护的 `yvonnegladwellstack/yvskills` 第一版增强仓库地图。

在继续下钻 `action-coach/SKILL.md` 之后，这个仓库的定位已经很清楚了：它不是代码实现型工具仓库，而是一个**用极小包装分发单个 Claude skill 的仓库**。当前真正的产物不是程序逻辑，而是一份把“想做但动不了”收束成七阶段对话协议的 `SKILL.md`。

当前置信度已经从“只读过 README 的结构图”提高到“读过核心 skill contract 的机制层”。它已经足够回答这个仓库到底发布了什么、核心控制逻辑在哪里，但还不足以评价这个 skill 在真实用户上的长期有效性。

## 仓库目的

- README 的公开定位非常直接：这是一个用于解开“想行动但动不了”的 Claude Skills collection。
- 当前主产物是 `action-coach`，主题是 Adlerian psychology × MBTI 风格的行动教练。
- 安装路径也很轻：要么执行 `npx skills add yvonnegladwellstack/yvskills -g --all`，要么直接把 `action-coach/SKILL.md` 复制到 `.claude/skills/action-coach/`。
- 从目录形态看，它更像一个 **skill distribution repo**，而不是传统意义上的软件包仓库。
- 同目录下还放了 `gemini-gem-prompt.md`。这说明作者想分发的核心不是某个 Claude 专属工具调用层，而是可移植的对话协议本身。

## 架构地图

### 顶层目录

- `action-coach`

### 顶层文件

- `LICENSE`
- `README.md`

### 第一版子系统角色判断

- `README.md` 是发布页，负责说明 skill 的目标用户、安装方式、触发词、作用边界，并用英文 / 日文双语降低分发摩擦。
- `action-coach/SKILL.md` 是仓库本体。真正的能力都写在这里，包括角色设定、诊断信号、阶段流程、输出标准与免责声明。
- `action-coach/gemini-gem-prompt.md` 是平行分发物。它几乎复用了同一套协议，说明仓库的核心资产是 prompt contract，而不是某个 runtime 的专有能力。
- 当前仓库没有公开看到脚本、测试、CI 或评测文件，因此它主要依赖 skill 文本本身来约束行为。

### 执行流的第一版理解

1. 先用一句固定开场让用户把“动不了”的具体处境说出来。
2. 再用 MBTI 只做轻量分类，不让类型学取代用户原话。
3. 从用户表达中识别 6 类停滞信号，但一次只指出最核心的一类。
4. 接着检查用户脑中是否有一个具体的“那个人”，把主语从“我”挪到“我要服务的具体对象”。
5. 再用课题分离拆开“我该做什么”和“别人会怎么反应”。
6. 最后把目标压成一个今天就能开始、5 分钟内可启动、不会失败的物理动作。
7. 整个对话只有在用户手里留下“下一步具体动作”时才算成功。

## 机制清单

### 用单 skill 的极小包装压低安装与使用摩擦

- 这个仓库几乎把所有价值都收束在 `action-coach/SKILL.md` 中，安装方式也只要求 `npx skills add ...` 或手动复制文件。
- 这控制的是“一个小 skill 因为壳太厚、依赖太多而很难被尝试”的失败模式。
- 代价是基础设施非常薄。公开仓库里看不到评测、版本约束或行为验证层，后续维护主要靠文本本身的稳定性。

### 用七阶段对话协议防止停在共情和分析

- `SKILL.md` 把流程写得非常硬：聆听、类型判断、信号识别、脑中之人检查、课题分离、最小行动设计、closing。
- 它明确声明：如果对话结束时没有留下“下一步具体要做的一件事”，这次 session 就算失败。
- 这控制的是“心理支持型对话很容易让用户感觉被理解了，但没有任何行动变化”的失败模式。
- 代价是对话会带有明显脚手架感，不适合所有需要开放探索的情境。

### 用 6 类停滞信号把“卡住”的原因显式分类

- 仓库把常见卡住模式拆成 6 类：实执行模拟、思考反刍、方向跳跃、知识成瘾、完美主义、外部归因。
- 规则不是把 6 类都讲一遍，而是一次只挑最核心的一类回给用户确认。
- 这控制的是“泛泛鼓励”与“把所有问题都解释成焦虑”这两种失真。
- 代价是这个诊断框架本身带有作者视角，可能会过度偏向“行动规避”解释，而低估真实的环境约束或心理困扰。

### 用“脑中的具体某个人”替换自我中心叙事

- 这份 skill 最有辨识度的机制之一，是反复检查用户脑中是否有一个具体的服务对象，而不是抽象的“用户”“市场”或“别人怎么看我”。
- 它控制的是“主语一直是我自己，结果行动永远在自我评估层打转”的失败模式。
- 代价是这个方法默认很多卡住问题都能通过引入具体他人而缓解；对某些不以外部交付为核心的问题，这个杠杆可能没那么强。

### 用课题分离切断“我行动”和“他人反应”的绑定

- `SKILL.md` 把恐惧拆成两列：哪些是我的课题，哪些是对方的课题。
- 这控制的是“因为预演别人的拒绝、评价或否定，所以连自己的动作都不做”的失败模式。
- 代价是它会天然把问题重写成边界问题，因此对一些真实存在的权力关系、资源约束和长期风险，会显得偏简化。

### 用“5 分钟内可开始的物理动作”做强输出约束

- 它对行动的定义很窄：必须是物理动作，必须今天能做，必须 5 分钟内能开始，最好几乎不会失败。
- 这控制的是“把思考、决定、查资料误当成行动”的失败模式。
- 代价是这种收束方式更适合作为解冻动作，而不是完整规划方法；它擅长把人推出静止态，不负责给出中长期路线。

### 用免责声明和禁做项约束使用边界

- 仓库明确写了三条边界：不是心理咨询替代品、不替用户决定方向、不允许停在分析层。
- README 与 `SKILL.md` 也都保留了心理健康免责声明。
- 这控制的是“skill 因语气强、命题大而被误当成治疗工具或人生导师”的失败模式。
- 代价是它主动放弃了一部分“万能顾问”幻觉，使用范围更窄，但边界更诚实。

### 用平行 Gemini prompt 证明核心资产是协议而不是工具

- `action-coach/gemini-gem-prompt.md` 与 `SKILL.md` 基本是同一套内容的另一种承载形式。
- 这说明 repo 的可迁移性来自方法论文本，而不是某个特定工具 API。
- 这控制的是“skill 价值被锁死在某个 runtime 里”的失败模式。
- 代价是维护上会出现重复文本，跨载体更新时也更容易漂移。

## 证据锚点

- Snapshot 来源：[github-repo-yvonnegladwellstack-yvskills.md](../../../raw/external/github-repo-yvonnegladwellstack-yvskills.md)
- 核心 skill 源文件快照：[yvskills-action-coach-SKILL.md](../../../raw/external/yvskills-action-coach-SKILL.md)
- 本地安装路径：`skills/action-coach/SKILL.md`
- 仓库：`yvonnegladwellstack/yvskills`
- 观察分支：`main`
- 解析到的 commit：`ac1fa5994879b9fc5fce26711a9b3e0b6d8ac891`

值得回查的关键文件与路径：

- `README.md`
- `action-coach/SKILL.md`
- `action-coach/gemini-gem-prompt.md`

## 开放问题

- 公开仓库里没有看到评测、用户反馈样例或版本化测试，因此还无法判断这个 skill 的长期有效性与失败分布。
- README 是英日双语，但核心 `SKILL.md` 当前主要是日文；跨语言使用时是否会影响效果，仍是开放问题。
- 现在仓库名叫 `yvskills`，但公开内容几乎全部集中在 `action-coach`。后续它会继续扩成 skills collection，还是维持单 skill 仓库形态，尚不明确。

## 来源依据

- [仓库 snapshot](../../../raw/external/github-repo-yvonnegladwellstack-yvskills.md)
- [Action Coach skill 原文](../../../raw/external/yvskills-action-coach-SKILL.md)

## 相关页面

- [Thin Harness, Fat Skills](thin-harness-fat-skills.md)
- [Claude Code：较厚的 agentic coding harness](claude-code-harness.md)
- [alchaincyf/nuwa-skill 仓库地图](alchaincyf-nuwa-skill-repo-map.md)
- [代码库作为知识来源](codebases-as-knowledge-sources.md)
