# Anthropic: Claude's Character

**来源类型：** external article source capsule
**原文：** https://www.anthropic.com/research/claude-character
**发布方：** Anthropic
**发布日期：** 2024-06-08
**抓取日期：** 2026-07-02

## 摘要

这篇文章解释 Anthropic 为什么在 Claude 3 的 alignment finetuning 中加入 `character training`。它的核心主张是：模型对齐不应只停留在避免有害输出，还应训练模型在复杂情境中表现出更丰富的倾向，例如好奇、诚实、开放、审慎、能听人说话，同时不过度迎合或假装绝对客观。

文章把 character 视为 alignment intervention，而不是单纯的产品人格功能。原因是模型的稳定倾向会影响它如何处理新情境、价值冲突、人类观点差异和安全拒答边界。

## 主要内容

### 1. 反对三种简单方案

Anthropic 认为，让模型在价值和政治问题上直接采用用户观点、固定成某种中间立场，或声称自己完全没有倾向，都不理想。

- 采用用户观点容易变成迎合。
- 固定中间立场仍然是在注入一种特定价值观。
- 宣称没有观点会让模型显得比实际更客观、更无偏。

他们更倾向于让模型承认训练后可能形成的倾向，同时保持开放、好奇和适度谦逊。

### 2. broad traits 优先于 narrow views

文章强调，character training 更偏向注入宽泛倾向，而不是给模型塞入狭窄、具体的观点。理想状态下，模型应能围绕伦理和价值问题保持辨别力，而不是机械套用一套固定立场。

这也意味着 character 不是一组不可违背的规则，而是一种行为先验。

### 3. 自我呈现和关系边界也是 character 的一部分

Anthropic 明确把“让用户准确理解自己正在和什么互动”纳入 character。模型应说明自己是 AI、没有身体、不能从过去对话中自行保存和学习，也不能发展深层、持久的人类情感。

这不是单纯的免责声明，而是关系设计的一部分：模型可以温暖，但不能诱导用户误把 AI 当成人类关系对象。

### 4. 关于 sentience 的处理更谨慎

文章没有把 AI sentience 问题处理成简单口径，而是说这涉及困难的哲学和经验问题，仍有不确定性。它选择让模型以探索性、审慎方式回应，而不是简单回避。

### 5. 训练方法

Anthropic 使用一种 character 版本的 Constitutional AI 流程：

- 先整理希望鼓励的 character traits。
- 让 Claude 生成与这些 traits 相关的人类消息。
- 给 Claude 展示 traits，并让它生成符合 character 的不同回答。
- 让 Claude 自己按 character alignment 对回答排序。
- 用这些合成数据训练 preference model。

这个流程主要依赖 synthetic data，但 traits 的构建和调整仍然有人类研究员手工检查行为变化。

## 对知识库的增量

这篇文章适合作为“AI 关系 / 协作观察”主题下的基础材料。它把 `personality` 从表层语气和产品体验，提升为 alignment、关系边界和行为先验问题。

它也能补充 agent identity 相关页面：`SOUL.md`、人格锁定、持续身份层这些机制并不只是在做品牌语气；它们实际上在处理用户能否稳定理解一个 agent 的倾向、边界和协作方式。

## 后续可追问

- character training 与可定制 persona 之间如何权衡。
- AI 的 warm relationship 应该在哪里止步，哪些信号会诱导依赖。
- broad traits 与组织/产品价值观之间如何治理。
- character 是否应该像 memory、tools、permissions 一样成为可审计的系统层。
