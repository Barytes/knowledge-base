# Coding Agent 情绪缓冲与失败恢复插件分析

这页分析一种 `Rage Compiler`：让用户把对 Coding Agent 的挫败留在本地表达，再把可见失败编译成不扩大权限、可验证的恢复指令。

> 状态：产品假设与当前能力核实。尚未实现，也没有真实用户验证。

## 核心判断

这个想法不应被定义成“脏话词库”或“文明用语过滤器”。更准确的产品是一个 `Rage Compiler`：允许用户在本地完成一次有趣、明确的情绪表达，同时把“上一轮已经严重失败”编译成 Agent 可执行的恢复指令。

它同时包含两个价值：

- 情绪体验：用户连续按 Tab，得到荒诞、非重复的表达，重新获得一点控制感。
- 任务恢复：发送时不把无信息量的词语交给模型，而是让 Agent 停止重复旧路径，基于会话证据定位失败并完成最小可验证修复。

前者决定产品是否有趣、愿不愿意传播；后者决定它是否会被长期使用。不能用其中一个代替另一个。

## 最小运行契约

第一版只需要保留五个对象：

```text
用户原本的技术诉求
插件生成的 rage spans
rage level
上一轮可见失败证据
实际发送的 repair contract
```

`rage spans` 应由编辑器状态精确标记，而不是在提交时扫描整条消息里的脏词。这样才能避免误删代码、日志、引用、测试样例，以及用户真正想保留的技术信息。

原始发泄内容默认只存在本地 UI 状态，不写入会话、不上传、不进入遥测。遥测如果存在，只记录是否触发、强度、是否撤销和后续结果，不记录原文。

## 交互应该保留什么

用户需要显式进入 `rage mode`，例如输入 `/rage` 或按专用快捷键；进入后，Tab 才用于循环生成。不能全局劫持 Tab，因为它在输入框中还承担焦点移动、补全或模式切换。

发送时，UI 应短暂显示“实际发送内容”，并允许展开、撤销或选择原样发送。静默替换会损害信任，每次弹出完整确认又会破坏爽感，所以更适合轻量、可下钻的透明度。

如果拦截器不确定自己是否保留了完整技术诉求，应阻止发送并让用户检查，而不是把原始内容或错误转换结果直接交给 Agent。

词库应以荒诞、非定向表达为主，不生成针对受保护群体的 slur、威胁或性暴力内容。这个边界不仅是安全要求，也能让产品保持“对故障发火”，而不是变成骚扰生成器。

## 不要把愤怒直接翻译成更大权限

“用户彻底怒了，请广泛尝试各种方案”不是好的转换。它可能让 Agent 扩大修改范围、增加 token 消耗，甚至把情绪强度误当作破坏性操作授权。

更稳的 `repair contract` 是：

> 用户对上一轮结果强烈不满。不要把情绪视为扩大权限、改变原目标或执行破坏性操作的授权。先根据本会话指出上一轮没有满足的具体要求和可见证据；停止重复原假设；提出少量互相竞争的原因并通过检查排除；保持原作用域，实施最小可验证修复并运行相关检查；没有证据时不要宣称已经解决。

长期价值不在这段固定措辞，而在系统能否从当前会话识别具体失败：是忽略要求、重复无效方案、改动越界、缺少验证，还是环境本身阻塞。固定模板只是冷启动。

## Codex 当前实现边界

截至 2026-08-08，Codex 插件可以打包 skill、MCP server 和 lifecycle hooks。`UserPromptSubmit` hook 能看到即将发送的 `prompt`，并且可以阻止发送或增加 developer context；当前官方文档没有提供改写用户 prompt 的 `updatedInput`。因此它可以实现“检测到 rage 后阻止或补充恢复要求”，但不能完整实现“删除原文并无感替换”。[Hooks](https://learn.chatgpt.com/docs/hooks)

Codex 当前也没有文档化的插件接口，用于给桌面端原生 composer 增加 Tab 候选或接管按键。插件 UI 是 MCP 返回的会话内组件，不是 composer 扩展；官方明确要求工具在不渲染 UI 的客户端里仍然可用，因此不能假设 Codex 桌面端一定提供所需组件能力。[Plugin architecture](https://developers.openai.com/plugins/concepts/plugins) [Add UI to your MCP server](https://developers.openai.com/plugins/build/chatgpt-ui)

实现路径可以分成四层：

| 路径 | 能完成什么 | 关键限制 |
|---|---|---|
| Codex 原生插件 + `UserPromptSubmit` hook | 识别、阻止、附加恢复上下文 | 不能按文档直接改写 prompt，也没有 composer Tab 扩展点 |
| MCP UI 中的独立 rage pad | 自己处理按键、把原始内容留在 UI，再发送清洗后的 follow-up | 不是原生输入框；Codex 桌面端是否渲染所需 UI 能力没有明确保证 |
| 自定义 Codex App Server 客户端 | 完整控制 composer，在调用 `turn/start` 前本地转换，再流式接收 Agent 事件 | 是自定义客户端或小 harness，不再只是原生插件 |
| macOS Accessibility / 输入法 / 全局键盘层 | 可覆盖多个 Coding Agent | 权限重、像 keylogger、容易受宿主 UI 更新影响，信任与维护成本高 |

如果目标是完整还原这个体验，最稳的工程路径是自定义本地 composer，通过 Codex App Server 在 `turn/start` 前完成确定性拦截。App Server 本来就是给自定义 rich client 使用的接口，支持 thread、turn、审批和流式 Agent 事件。[Codex App Server](https://learn.chatgpt.com/docs/app-server)

如果只想先验证“恢复指令是否有用”，可以做一个本地 Codex 插件，用 `UserPromptSubmit` hook 附加恢复上下文，但要明确它还没有完成真正的过滤体验。

公开发布还有一条现实限制：当前插件指南要求插件适合 13–17 岁一般受众，并说明成熟 18+ 体验要等待年龄验证能力。因此显式的大规模脏话生成器更适合先通过本地或私人 marketplace 验证，不能预设会通过公共目录审核。[Plugin guidelines](https://developers.openai.com/plugins/app-guidelines#appropriateness)

## 最小可信验证

第一版不需要先嵌入 Codex 原生输入框。先做一个自己控制的本地 composer，使用确定性词组组合器、显式 rage mode、三个强度等级和一套恢复协议，记录真实失败场景中的后续结果。

对同一批会话做四组回放：

```text
原始发泄内容
只删除发泄内容
通用“用户很生气”提示
基于会话证据生成的 repair contract
```

任务侧看下一轮是否解决、相关检查是否通过、还需要几轮纠正、是否产生越界修改、用户是否接受结果。交互侧看用户是否在真实卡住时主动触发、第二周是否仍会使用、是否经常撤销、有没有误拦截或原文泄漏。

“很好笑”“想要更多词包”和分享截图只能证明传播性。更强的产品信号是用户在非演示场景反复使用，并且恢复轮数显著下降。

## 两个不能预设成立的假设

第一，不能宣称“骂人一定不影响模型”或“骂人一定让模型更差”。现有实验结论并不一致，影响会随模型、任务和语言变化。更稳的结论只是：没有证据支持把“更粗鲁”当作稳定、可迁移的性能控制手段。[Yin et al., SICon 2024](https://aclanthology.org/2024.sicon-1.2/) [Cai et al., 2025](https://arxiv.org/abs/2512.12812)

第二，不能把产品宣传成“发泄会让人冷静”。一项覆盖 154 项研究的 meta-analysis 不支持 venting 是普遍有效的愤怒管理方式；这并不直接否定幽默化的输入仪式，但说明情绪价值必须实测，不能借用 catharsis 常识直接成立。[Kjærvik and Bushman, 2024](https://pubmed.ncbi.nlm.nih.gov/38518585/)

因此更准确的定位是“有趣的失败恢复仪式”，不是情绪治疗产品。

## 最终建议

值得做，而且非常适合作为一个小而有传播性的项目。但应把第一版命名和架构锚定在 `Rage Compiler`，不是“脏话过滤器”。

先用自定义 composer 完整验证魔法时刻，再决定是否做 Codex hook 版、MCP UI 版或跨 Agent adapter。只做固定 prompt 改写会很快被模型和平台能力吞掉；如果它能积累真实失败样本、会话证据到恢复策略的映射，以及转换前后的结果评测，它才会从 gimmick 长成一个小型 `agent failure-recovery layer`。

## 相关页面

- [产品定义判断框架](../../frameworks/产品定义判断框架.md)
- [产品验证判断框架](../../frameworks/产品验证判断框架.md)
- [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md)
- [Agent 时代的人机交互新命题](../agent-harness-runtime/agent时代的人机交互新命题.md)
- [提示词会消失吗：Agent 编程的长期分工](../agent-harness-runtime/提示词会消失吗-Agent编程的长期分工.md)
- [AI-Infra 的抗模型吞噬地图](../ai-industry-investment/AI-Infra的抗模型吞噬地图.md)
