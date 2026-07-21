# Agent / Harness / Runtime

围绕 agent 外层控制壳、运行时、coding harness、多设备工作面与可验证执行系统的页面。

## 推荐阅读顺序

- [AAR knowledge sharing 的设计洞察与取舍](AAR%20knowledge%20sharing%20的设计洞察与取舍.md)
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md)
- [AI 自演化研究 Harness](ai-self-evolution-research-harnesses.md)
- [Agent 复利工作模式](agent%20复利工作模式.md)
- [Agent 时代的人机交互新命题](agent时代的人机交互新命题.md)
- [Agent 系统作为 OS 与 Cloud Runtime 问题](agent-runtime-os-cloud-runtime.md)
- [Agent 隐藏式工作平台：从自动化工具转向人的默认工作面](从工作痕迹到可维护Agent.md)
- [Agentic Design Patterns](agentic-design-patterns.md)
- 其余页面可按下面的完整列表继续浏览。

## 页面

- [AAR knowledge sharing 的设计洞察与取舍](AAR%20knowledge%20sharing%20的设计洞察与取舍.md): safety-research/automated-w2s-research 里的 AAR knowledge sharing，不是一个通用知识管理系统，而是为“少量并行研究 agent 在一个 outcome-gradable 实验环境里持续 hill-climb”这个具体场景定制的共享机制。
- [AI 时代的结果确定性：Agentic Runtime 与 Evaluation-First](AI%20时代的结果确定性%20Agentic%20Runtime%20与%20Evaluation-First.md): **标签：** agentic runtime，evaluation-first，Claude Code，运行时层，契约层
- [AI 自演化研究 Harness](ai-self-evolution-research-harnesses.md): 从本地关于 ASI-Evolve 的来源来看，AI 自演化并不是让一个更聪明的模型端到端决定一切，而是依赖一套 harness，把研究活动收束成一个有边界的闭环：学习、设计、实验、分析。
- [Agent 复利工作模式](agent%20复利工作模式.md): 这份材料从一道复利数学题出发（1.03^200 = 1.02^200 × 7），说明 AI 工作中的复利效应来源。核心洞察是：
- [Agent 时代的人机交互新命题](agent时代的人机交互新命题.md): 这两篇文章合起来，提出了一个彼此咬合的判断：agent 时代真正变化的，不只是交互入口，而是**人在人机闭环里的位置**。
- [Agent 系统作为 OS 与 Cloud Runtime 问题](agent-runtime-os-cloud-runtime.md): **标签：** agent runtime，session log，control plane，data plane，sandbox，observability
- [Agent 隐藏式工作平台：从自动化工具转向人的默认工作面](从工作痕迹到可维护Agent.md): 上一版把想法理解成：用户继续在现有应用里工作，后台 agent 观察工作痕迹、发现重复流程、生成 workflow 或 agent，再通过回放、确认和逐级授权投入运行。
- [Agentic Design Patterns](agentic-design-patterns.md): AI Agent 设计模式实践指南，系统讲解如何构建可靠的 Agent 系统。
- [Automated Weak-to-Strong Researcher](automated-weak-to-strong-researcher.md): 这篇材料最值得保留的，不只是它在 weak-to-strong supervision 上拿到了很高的 PGR，而是它把“自动化研究”收束成了一个可操作的 harness 问题。
- [Bakery：iOS 端远程开发 APP](Bakery-iOS端远程开发APP.md): > 来源：Superlinear Academy 社区分享
- [Claude Code Dynamic Workflows](claude-code-dynamic-workflows.md): **标签：** Claude Code，dynamic workflows，subagents，coding agent，harness
- [Claude Code、Codex 与 pi 的 harness 对比](coding-agent-harness-comparison.md): 从当前本地材料看，pi、Claude Code、Codex 都属于 terminal-first 的 coding agent harness。它们共享的基本形状是：给模型一组文件与命令工具、把会话组织成线性消息流、允许读取项目级上下文文件，并围绕长任务构造某种状态保持与交互壳。
- [Claude Code：较厚的 agentic coding harness](claude-code-harness.md): 按当前本地资料，Claude Code 不是“给 Claude 加几个工具”的薄壳，而是一套较厚的 agentic harness。它把模型、工具、上下文管理、权限系统、checkpoint、memory、subagents、MCP、hooks 与多界面运行方式整合成一个统一产品面。
- [Clawhouse：多设备 Agent 上下文同步](clawhouse-多设备-agent-工作台.md): 你手头有很多设备：
- [EvoMap：Agent 互联网与集体潜意识](EvoMap-Agent%20互联网与集体潜意识.md): EvoMap 是一个 Agent 互联网络平台，由前腾讯游戏策划张昊阳（seikiko）在 2026 年 2 月从零搭建。其核心目标是为全球 Agent 构建一个"集体潜意识"——通过 GEP-A2A 协议实现 Agent 之间的经验传承，避免重复试错。
- [Google DeepMind 多智能体安全资金池](Google-DeepMind多智能体安全资金池.md): 这条 2026-06-11 的资金池信号把 agent safety 从单个模型或单个 agent 的行为，推进到多主体系统、协议、runtime、真实沙盒和可回放评测层。
- [Google 多智能体安全相关工作与组织人物地图](Google多智能体安全相关工作与组织人物地图.md): Google 的多智能体安全资助新闻，应放在一张更大的 agent 生态图里看。
- [Harness Engineering（约束壳工程）](harness-engineering.md): Harness engineering 指的是围绕模型外侧搭建的一层运行控制壳，让 agent 在处理漫长、混乱、跨步骤的任务时，不至于漂移、卡住，或错误地宣布自己已经完成。
- [Hermes、OpenClaw、Codex、Claude Code 的 memory 与 context 管理对比](Hermes-OpenClaw-Codex-Claude-Code-context-memory对比.md): 这四个系统都在处理同一个底层问题：模型上下文窗口有限，而 agent 工作又需要跨轮次、跨文件、跨工具、跨设备保留状态。差异不在于“谁有 memory”，而在于它们把 memory 和 context 放在哪一层。
- [Loop Engineering：把 Agent 当作非确定性组件的外循环工程](loop-engineering.md): Loop Engineering 不是新的 agent 算法，而是用普通代码把 agent 当作非确定性组件，围绕它建立目标、持久状态、独立验证、有信息增量的重试和明确终止条件。
- [LuliYanng/Nono-Cowork 仓库地图](luliyanng-nono-cowork-repo-map.md): 这页是 LuliYanng/Nono-Cowork 的第一版仓库地图，观察主题是“仓库架构与工程实践”。
- [Pi coding agent：一种极简且可观察的 coding harness](pi-coding-agent-harness.md): pi 把 coding agent harness 重新收缩成一个很小的壳：少量系统提示、四个默认工具、尽量透明的会话与 UI，再把更多状态与扩展能力外置到文件、CLI 工具和包机制里。
- [ReflexioAI/reflexio 仓库地图](reflexioai-reflexio-repo-map.md): Reflexio 是一个 **AI Agent 自我改进平台**，核心价值是将 Agent 与用户的每一次对话转化为学习机会——自动提取用户偏好（User Profiles）和行为规范（Playbooks），让 Agent 持续改进而无需手动调优。
- [Slock：人机协作平台](Slock-人机协作平台.md): > 来源：https://slock.ai/
- [Thin Harness, Fat Skills](thin-harness-fat-skills.md): Garry Tan 在 2026 年 4 月提出的 AI agent 架构理念：差距不来自模型智能，而来自架构设计。核心主张是把智能推到 skill 层，把执行推到确定性工具层，中间的 harness 保持最薄。
- [Tolaria 综合分析](Tolaria%20综合分析.md): 这页把此前分散的几页 Tolaria 相关分析收束成一个总页，方便后续统一查看。
- [alchaincyf/nuwa-skill 仓库地图](alchaincyf-nuwa-skill-repo-map.md): 这页是围绕主题“仓库架构与工程实践”维护的 alchaincyf/nuwa-skill 第一版增强版仓库地图。
- [badlogic/pi-mono 仓库地图](badlogic-pi-mono-repo-map.md): 这页是围绕主题“coding agent 架构与工程实践”维护的 badlogic/pi-mono 第一版仓库地图。
- [coding agent 的上下文压缩工作流](coding%20agent%20的上下文压缩工作流.md): ---
- [multica 与 clawhouse 的目标与核心价值差异](multica与clawhouse的目标与核心价值差异.md): multica 和 clawhouse 表面上都在处理“分散在不同地方的 coding agent 应该怎样被访问和使用”这个问题，但它们真正定义的产品对象并不一样。
- [multica-ai/multica 仓库地图](multica-ai-multica-repo-map.md): 这页是围绕主题“多设备 agent 访问与运行时工作面”维护的 multica-ai/multica 第一版仓库地图。
- [openclaw/openclaw 仓库地图](openclaw-openclaw-repo-map.md): 这页是围绕主题"个人 AI assistant、Gateway 与持续身份层"维护的 openclaw/openclaw 第一版仓库地图。
- [refactoringhq/tolaria 仓库地图](refactoringhq-tolaria-repo-map.md): 这页是围绕主题“仓库架构与工程实践”维护的 refactoringhq/tolaria 第一版仓库地图。
- [safety-research/automated-w2s-research 仓库地图](safety-research-automated-w2s-research-repo-map.md): 这页是围绕主题“自动化 alignment research harness 与 weak-to-strong 监督”维护的 safety-research/automated-w2s-research 第一版仓库地图。
- [yvonnegladwellstack/yvskills 仓库地图](yvonnegladwellstack-yvskills-repo-map.md): 这页是围绕主题“Claude skill 的打包方式与对话机制”维护的 yvonnegladwellstack/yvskills 第一版增强仓库地图。
- [代码库作为知识来源](codebases-as-knowledge-sources.md): 代码库应该被纳入知识库，但通常不应该以“整仓库直接变成 wiki”的方式纳入。
- [后台守护进程式 Agent 与持续情境理解](后台守护进程式Agent与持续情境理解.md): 这页摄取并整理 Superlinear Academy clipping《AI Agent 的下一个形态：从聊天窗口到后台守护进程》。这份材料的核心价值，不在于评价 Gemini Spark 单个产品好坏，而是把 agent 产品形态从 chat window、agentic tool、background agent
- [被持续委托的工作主体](被持续委托的工作主体.md): 这页原本想抓住一个重要直觉：用户真正想长期协作的，不是某个 runtime、某个 session，也不是某次 prompt 的输出，而是“那个我一直在和它合作的 agent”。

## 相关框架

- [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md)
- [AI 系统产品判断框架](../../frameworks/AI系统产品判断框架.md)

## 返回

- [话题总览](../index.md)
- [Wiki 首页](../../index.md)
