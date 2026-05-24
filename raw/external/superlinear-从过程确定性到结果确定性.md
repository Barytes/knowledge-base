---
title: "从过程确定性到结果确定性：AI 时代的另一种安全感"
source: "https://www.superlinear.academy/c/ai-resources/result-certainty"
author:
published:
created: 2026-04-22
description: "即使在2026年，把AI从demo做成产品也不是一件容易的事。比如中翻英，大家都觉得早就被LLM解决了，不就是调个API的事情嘛。但我们最近因为要把Superlinear Academy社区加入一个中翻英自动同步的功能，才发现开发体验这么差。这个问题的核心在 AI 的输出有很多不确定性。比如一个帖子太长了，AI会偷懒，前面正常翻译，后面开始缩写。或者它会脑子短路，开始输出还是英文，中间非要夹几个中文。或者在格式里做一些小手脚，比如丢了个粗体。或者它可能会超时，输出一半就卡在那儿，直到挂掉。为..."
tags:
  - "clippings"
---
即使在2026年，把AI从demo做成产品也不是一件容易的事。比如中翻英，大家都觉得早就被LLM解决了，不就是调个API的事情嘛。但我们最近因为要把Superlinear Academy社区加入一个中翻英自动同步的功能，才发现开发体验这么差。

这个问题的核心在 AI 的输出有很多不确定性。比如一个帖子太长了，AI会偷懒，前面正常翻译，后面开始缩写。或者它会脑子短路，开始输出还是英文，中间非要夹几个中文。或者在格式里做一些小手脚，比如丢了个粗体。或者它可能会超时，输出一半就卡在那儿，直到挂掉。

为了克服这些不确定性，我们就要在程序里面做很多细节处理。比如如果帖子太长，就要分几段分别调用API，最后再拼接起来（ [Wide Research](https://yage.ai/wide-research.html) ）。但这会带来另一个问题，不同段之间的术语未必统一，所以我们还要进一步设计工作流，来保证同一个中文术语第一段跟第二段之间不至于翻译成两个不同的英文单词。最后我们还得加一个检查，如果输出还有中文字符，就需要再翻译一遍。为了解决超时的同时避免重复翻译，我们还要做断点续传，只把失败的那一小部分翻译，回头再插进去。

用这样的方式，我们确实大幅提升了成功率，保证即使对社区里面很长的帖子，AI也能正常翻译。但整个感觉就是累。我们90%的时间都没有花在怎么让AI翻译得更好，而是用workflow跟orchestration来给AI擦屁股。而且到后来，因为总会出各种意外情况，很多只出现一两次的问题我们就没修了，因为感觉永远修不完。总之完全没有感觉到生产力的提升。还不如调以前的机翻API。

后来我们换了一种完全不同的思路问题反而解决了。但在介绍具体怎么做之前，我想先解释一下我们对这个问题成因的更深一层的思考。

## Agent调用的四层结构

像前面提到的，调用AI的API不是调用完了就甩手不管了这么简单。它需要做很多配套的事情。而这些事情从集成的角度来看可以分成四层：

1. 模型层：我们是用Claude还是GPT？用Opus还是Haiku？用什么Reasoning Effort？
2. 协议层：用Chat Completion API还是Response API？用MCP还是RESTful API？Rate Limit怎么解决？JSON Mode要不要开启？当我们说调用API的时候，大多数情况下我们指的是协议层。
3. 运行时层：状态怎么管理？工具怎么调用？文件的内容怎么给AI？权限怎么控制？用多少并发？这一层不是传统意义调用API的开发内容，但是但凡想要把AI稳定用到生产环境，这是绕不过去的一层。
4. 契约层：到底什么样的标准算成功？比如拿到AI的结果之后做什么检查？Guardrail怎么设？什么时候要引入人工干预？怎么保证不违反社会主义核心价值观？这一层决定了我们能不能信任AI的输出，并且真的把它用于生产。

一说到AI产品开发，大家讨论最多的是协议层。但实际的开发过程中，最花时间的反而是运行时层。这是因为协议层和传统的API调用不一样，LLM引入了太多的不确定性，而这些不确定性都需要运行时层来吸收和处理。问题是，运行时层跟业务逻辑没什么关系。无论是做翻译、代码生成、还是客服机器人，我们都要处理偷懒、拼接、上下文管理、并发控制这些事情。这意味着每个团队都在重复造轮子。所以一个自然的想法就是：能不能把运行时层外包出去？

这件事没那么简单。不同模型的 failure pattern 是不一样的。有些模型遵循指令的能力很强，但容易在长文本上偷懒；有些模型创造力好，但格式控制一塌糊涂。针对不同模型，我们擦屁股的方式也不同，尤其是长尾failure pattern更是如此。因此运行时层很多时候是针对模型高度定制化的，也就很难复用，外包更无从谈起。

但最近有一件事情让这个局面有了改观：Claude Code 本身不是开源项目，但越来越多的模型提供商开始主动兼容。Kimi、DeepSeek、GLM 都提供了官方接口，只要改几个环境变量，就能让 Claude Code 在后台调用这些模型。这件事很有意思。它意味着 Claude Code 已经超越了工具本身，变成了一种可复用的东西。

更重要的是，当模型提供商宣称兼容 Claude Code的时候，他们实际上做的事情是：把自己模型的 failure pattern 适配到 Claude Code 的预期行为上。换句话说，擦屁股这件事没有消失，但擦的人变了——从我们开发者变成了模型提供商。他们为了进入这个生态，必须确保自己的模型在 Claude Code 的运行时里表现稳定。（这个讨论也对其他类似的工具比如Codex/Cursor Agent也适用，因为它和Claude Code的命令行接口也非常类似，适配很简单）

换言之，Claude Code/Codex/Cursor Agent 正在成为一种可以复用的 Agentic Runtime。

这就解决了前面提到的长尾问题。那些零星出现的 edge case，一个团队修不完，但整个生态可以。每一个想兼容 Claude Code 的模型提供商，甚至包括Anthropic本身，都在帮我们填坑。所以一个新的思路就是，对于翻译这个任务，我们完全可以从“调 API然后自己擦屁股”改成“直接交给 Claude Code”。这里我们通过白嫖整个生态为了兼容它而做的适配工作，事实上复用了它的运行时层，或者说，我们从自己造轮子，变成了站在一个正在收敛的标准上面。

## 实战：把翻译交给 Claude Code

这就是我们决定换一条路的原因：与其继续在运行时层自己处理不确定性，不如直接站到这个正在收敛的标准上。所以我们就试着把社区翻译这个任务交给 Claude Code 去做。最直观的感受就是：之前我们花大量时间处理的问题，现在大部分自动消失了。

先说偷懒的问题。之前调 API，我们需要自己做分段、拼接、校验。但 Claude Code 的工作方式天然就不一样——它操作的基本单位是文件。文件是一个 stateful 的东西，它存在磁盘上，可以序列化、持久化。所以我们可以让 Claude 一章一章地翻译，每翻完一章它自己就写回文件，整个过程不需要我们在外面再包一层 orchestration 来追踪和管理进度。

断点续传也一样。以前调 API 超时了，我们要记录断点、只翻失败的部分、再拼回去。现在不用了。翻译到一半挂掉，文件就在那儿，已经翻好的部分总之不会丢。重启之后让 Claude Code 接着翻就行，它自己会读文件、看到哪里没翻、继续往下做。

术语统一的问题以前需要我们设计专门的流程，用总分或者递进的形式，让第一段的术语传递给第二段。现在 Claude Code 每次修改之前会先读整个文件，它天然能看到前面的上下文。所以术语统一的问题一个简单的 prompt 就能解决，比如先读整个文件，看看之前用的是什么术语，翻译第XX行到第XX行。

输出夹杂中文这个问题，以前我们要做检测、判断、重试。现在可以直接在 prompt 里跟 Claude 说：翻译完成后，从头到尾检查一遍，确保没有残留的中文字符。更进一步，因为 Claude Code 可以调用 Python，我们甚至可以让它写一个简单的脚本来验证最终文件的格式是否符合要求。它自己写检查逻辑，自己跑，自己修。

这些变化的共同点是：以前需要在 workflow 层面解决的问题，现在可以用自然语言在 prompt 里说清楚，让 agent 自己处理，而且还很可靠。我们终于可以把精力放在怎么让翻译效果更好，而不是怎么防止系统脑残出幺蛾子上。

## Agentic Loop 与 Evaluation-First Mindset

这些变化让我们终于可以把精力放在翻译效果本身上。但做完以后我开始好奇：为什么 Claude Code 能做到这些？换一个方式调用 API 真的有这么大区别吗？

前面我们说过，一个重要原因是我们在复用整个生态的适配工作。但这只是更高层更表面的原因。如果从四层结构的角度来看，Claude Code 能 work 的直接原因是：它让 AI 能够观察到自己行动的结果。

这听起来像废话，但它是 agentic AI 和传统 API 调用的本质区别。当你用 API 的时候，AI 只能看到喂给它的 prompt，它吐出一个结果，然后就结束了。如果结果有问题，比如 JSON 格式不对、漏了字段、后半段开始偷懒，AI 自己不知道。发现问题的是你，决定要不要重试的也是你，怎么修复的逻辑还是你来写。这是为什么我们觉得AI很傻，我们要跟着收拾的直接原因。

但 Claude Code 不一样。它改完一个文件之后，可以调用 Python 跑一个JSON parser，看到报错说第 9527 行有语法错误。这个报错会反馈给它，它就知道该去修哪里。修完再跑一遍，通过了，继续往下。这个执行 → 观测 → 纠错的循环，就是 agentic loop。

这也是为什么文件这个形态这么重要的原因。文件是状态的载体，状态可见才能让闭环成立。我们把翻译任务从调一次 API 拿结果变成让 agent 在一个工作目录里操作文件，这在事实上给 AI 装上了一双眼睛。它能看见自己上一步做了什么，能看见验证脚本的输出，能根据这些信息决定下一步怎么做。这是运行时层带来的能力。

但 agentic loop 能跑起来，不代表它能跑对。观测到结果是一回事，知道什么结果才算"对"是另一回事。这是契约层要回答的问题。回到翻译这个例子。即使用了 Claude Code，它也不是我们换了个工具，一下就神奇地work了的。

如果只说"把这个文件翻译成英文"。Claude 翻了，结果里还是会有几段夹着中文字符。和之前调 API 遇到的问题一样，只不过这次修起来容易很多：我们可以在 prompt 里加一句：翻译完之后跑一个 Python 脚本检查有没有残留的中文字符，有的话自己修。Claude Code就会可靠地写一个简单的正则检查，跑一遍，发现问题就回去改，改完再跑，直到通过。

但这件事体现了一个更重要的问题：之前出错不是因为 Claude 笨，而是因为它不知道什么叫翻译完了。对它来说，保证对每一章都做了一次中翻英这个操作，任务就结束了。但对我们来说，翻译完了还包括格式正确、没有残留中文、术语统一这些隐含的期望。这些期望在我们脑子里，Claude 看不到。而一旦我们把这些期望显式地写出来，并且告诉它怎么验证，它就能自己判断做没做完。

我喜欢做的一个比喻是：想象你在给一个有健忘症的实习生交代任务。这个实习生没有任何上下文，不知道你之前聊过什么，不知道你的隐含期望，只能看到你这一次给他的指令。你需要把验收标准写到这种程度：只根据这些信息，他就能判断自己做完了没有。如果他觉得没做完，他知道还差什么。我的经验是，写到这种详细程度，基本上可以期待Claude Code/Codex可以可靠地完成任务。如果搞不定，别慌抱怨AI，我们应该首先检查是不是标准没写清楚。

所以现在我们就可以把这两层的关系说清楚了。运行时层给了 agent 观测能力，让它能看见自己做了什么、结果是什么。契约层告诉它什么算成功，让它能判断自己做完了没有。两者缺一不可：只有观测没有标准，agent 会在那里瞎转，给出一个非常漂亮但未必满足我们要求的结果；只有标准没有观测，agent 做完一次就停了，对不对全靠运气。Agentic loop 加上 evaluation-first，才构成一个完整的闭环。

## 从过程确定性到结果确定性

这个闭环一旦建立起来，会带来一种微妙的对 AI 信任来源的改变。它背后其实是两种不一样的确定性。

传统程序员的安全感来自过程确定性。我写的每一行代码都在我的控制之下，每一个分支、每一个边界条件我都考虑过。程序的行为是我设计出来的，只要它照着这些逻辑做，就一定会得到符合要求的结果。这种确定性是切实可感的，这种把结果翻译成程序行为的能力也是我们长期训练出来的基本功。

但我们刚才看到的 agentic loop 和 evaluation-first mindset，其实是另一种确定性。我们不规定每一步怎么走，而是规定终点长什么样、怎么验证到了终点。过程是不确定的——Claude 可能先翻译再检查，也可能边翻边查，可能用正则也可能用别的方法——但结果是确定的：只要验收标准写对了，最终产物就是对的。这是结果确定性。

这两种确定性背后，其实是两种不同的成本结构。过程确定性的经济学是：代码执行起来几乎不花钱，但写代码的人力很贵。所以我们要精心设计逻辑、追求复用、避免重复，把人力成本摊薄到每一次执行上。结果确定性的经济学正好反过来：intelligence越来越便宜，让AI反复尝试、检查、纠错的成本在快速下降。我们可以挥霍token来换取确定性——不是通过写更多的防御性代码，而是让AI用它的推理能力去对抗不确定性。

这和我之前在 [《一次性软件与被压缩的现实》](https://yage.ai/ai-native-cost-structure.html) 中讨论的是同一个逻辑。那篇文章讲的是当写代码的成本趋近于零，一次性软件反而成了最优策略。这里的变化更广：不只是代码，而是整个推理和智能都在变便宜。翻译不是写代码，但它同样是燃烧token所产出的东西。当这个成本足够低，我们就可以让AI每次都现场做检查、现场写验证脚本、反复循环直到结果正确，而不需要像以前那样把所有可能的情况都预先在代码里写成规则。

在成本结构的变化之外，这也带来了天花板的差别。过程确定性的上限是我们的想象力和精力，我们能想到的情况、能写出来的逻辑，就是系统能处理的边界。结果确定性的上限更高：我们不需要穷举所有可能的路径，只需要定义清楚什么是对的，agent 会自己想办法到达那个状态。

但我们不太习惯结果确定性，往往会觉得不踏实。因为我们在职业生涯中引以为豪的一项核心技能，恰恰就是把结果翻译成过程：老板说想要一个能处理十万并发的系统，我们就设计出一套架构来保证这个结果；PM 说用户上传的文件不能超过 10MB，我们就写一个校验逻辑来拦截超限的请求。所以当我们开始用 AI 的时候，这种习惯会很自然地延续——我们本能地想用规则来规定 AI 的行为：输出必须是 JSON 格式，每个字段必须存在，遇到这种情况要这样处理，遇到那种情况要那样处理。

但这条路是有上限的。AI 不是一个确定性的系统，用过程去约束它，你会发现自己在做的事情是用大量的 rule 来控制它的不确定性。规则越写越多，漏洞越补越多，最后你花在防御上的精力比花在解决问题上的还多。这就是我们最开始拿 API 做翻译时遇到的困境。

但如果我们可以接受一点让步呢？如果我们愿意接受过程上的不确定性，转而通过规定结果来约束 AI 的行为，事情会变得不一样。我们不再说"你必须用这个方法处理这种情况"，而是说"最终产物必须满足这些条件，怎么满足你自己想办法"。这样一来，AI 的灵活性不再是我们需要控制的风险，而是它完成任务的资源。

当然，以前这条路没那么容易走。如果你想让 AI 能够自己观测结果、自己判断对错、自己决定下一步怎么做，你得自己搓一个 agentic loop 出来。而 agent 套壳比它看上去要更难：你要处理工具调用的格式，要解析 AI 的输出，要管理上下文窗口，还要针对不同模型的特性做适配。这套东西做下来，你会发现自己又在做另一种形式的用过程换确定性。（而且引入 Agentic 框架往往会 [带来更大的技术债](https://yage.ai/why-forget-all-frameworks.html) ）

但现在不用了。Claude Code、Codex、Cursor Agent 这些工具已经把运行时层的脏活干完了。Agentic loop 是现成的，文件系统是现成的，工具调用的封装也是现成的。你要做的，就是想清楚你要什么结果，怎么验证这个结果，然后用自然语言告诉它。

所以我有一个建议：尝试拥抱过程上的不确定性。不要条件反射地去规定 AI 的每一步行为，而是直接描述你对最终结果的期望，把它 codify 成可验证的标准。运行时层的事情交给 Claude Code 这类工具去处理，你专注于契约层：定义什么是对的，定义怎么检验。

这是一种不一样的工作方式，也是一种不一样的安全感来源。

## 结语

当然，这种工作方式不是没有边界的。

首先是任务本身的性质。结果确定性能 work，前提是你能清晰地定义什么是"对的"。翻译这个任务之所以适合，是因为验收标准可以形式化：格式正确、没有残留中文、术语一致，这些都可以写成脚本让 agent 自己跑。但有些任务的"对"很难定义，或者定义出来的标准本身就有歧义——不过话说回来，这种情况下用 rules 来约束过程只会更难。至少 evaluation-first 还给了一个明确的失败信号。

其次是安全。用 API 的时候，AI 对你的系统没有任何控制权。它只能接收 prompt、返回文本，仅此而已。但 Claude Code 这类工具不一样。它能读写文件，能执行 Python，能跑 bash 命令。这是它强大的原因，也是一个危险因素。这个问题要认真对待。我们的做法是在配置层面收紧权限：用 --allowedTools 参数限制它能调用的工具，把可执行的范围收敛到特定的脚本上。更进一步，可以结合现在比较流行的轻量级 sandbox 方案，让 agent 就算搞砸了也只会把 sandbox 里的文件弄乱，不至于影响宿主系统。

这方面确实还有很多坑。权限模型怎么设计、sandbox 怎么配置、出了问题怎么回滚，这些都是开放的问题，没有标准答案。但我对这个方向还是乐观的。安全问题是工程问题，工程问题是可以解决的。不会因为有这些风险，这条路就走不通。

回到开头的问题：到底是把 AI 作为系统的一部分，用程序去调用它，我们做的是一个带AI功能的翻译产品？还是把 AI 作为系统的核心，让它去调用程序，我们做的是一个完成翻译任务的AI Agent？

我们试了两条路，发现后者的成功率和稳定性意外地高很多。这可能是因为后者让我们可以复用整个生态的适配工作，因为 agentic loop 让 AI 能够自我纠错，因为 evaluation-first 让我们可以用结果而不是过程来约束 AI 的行为。这些因素叠加在一起，构成了一种不同的工作方式。

它需要我们放弃一些东西：对过程的掌控感，对每一步行为的确定性，以及我们花了很多年训练出来的那种把结果翻译成流程的本能。但它也给了我们一些东西：更高的上限，更少的体力活，以及一种新的、基于结果的安全感。

这个模式能推广到多远？我不确定，但至少在翻译这个场景上，它彻底改变了我们的开发体验。我们把这套实践整理成了一份 [操作指南](https://gist.github.com/grapeot/9cbdcf7f26bd1d69a11c39414b54dbe6) ，你也可以发给自己的AI，让它现在就试试看。

Conversation summary

评论区围绕文章提出的AI开发中四层结构和agentic loop展开了深入讨论，大家普遍认同运行时层的重要性及其复杂性。许多评论者分享了自身在构建和使用agent时的经验，探讨了如何通过明确验收标准和利用现有agentic工具（如Claude Code、Codex）提升AI任务的稳定性和成功率。讨论还涉及了prompt设计、工具复用、安全性以及未来产品设计的挑战与方向。

最近在用Trea-cn，主要是美元付费对我来说不方便，想知道它跟claude/codex/cursor等的差别很大吗

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRlh5TlFnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b3188cbb609f09767a8e9e7eeb3ffafb3d77aed0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQ0xBRnBBaXdCT2dwellYWmxjbnNHT2dwemRISnBjRlE9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--ef295ed08e817a599d692fd6d8761673d3ed547f/IMG_2643.jpeg)](https://www.superlinear.academy/u/f7e34206)

Wareron 我没有用过，但猜差别不大。因为GLM-5现在很强了，可以试试。但GLM目前就是很慢。

Yan Wang 鸭哥 目前还在摸索中，用trea-cn+Glm-5做了一个提取图片内容自动翻译英语并自动输出成中英对照word文档的小软件，感觉Trea用来学习还可以

醍醐灌顶 解释了很多我现在看不懂研发神操作结果不尽如人意的部分 非常inspiring

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCUEdQSHdNPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--af89ba2beee5506119e9e3b35521631d594ab0a3/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJc0FXa0NMQUU2Q25OaGRtVnlld1k2Q25OMGNtbHdWQT09IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--86d5a93b1fb9d9a40ce4e61c041294c46ab790a5/Screenshot%202024-08-06%20at%2021.52.56.png)](https://www.superlinear.academy/u/f07618d2)

这个对于新手来说是福音，0编程基础不会有掌控感/期望。就是一直点“run”有点无趣 😂，而且“trust” 也有问题。

非常棒，和我在做SaaS Global 多语言翻译一样，还是 Yan Wang 鸭哥 总结的清晰！

但最近有一件事情让这个局面有了改观：Claude Code 本身不是开源项目，但越来越多的模型提供商开始主动兼容。Kimi、DeepSeek、GLM 都提供了官方接口，只要改几个环境变量，就能让 Claude Code 在后台调用这些模型。这件事很有意思。它意味着 Claude Code 已经超越了工具本身，变成了一种可复用的东西。 —— 这里想请教下鸭哥是类似export ANTHROPIC\_MODEL=deepseek,然后Claude Code执行任务的时候就会调用指定的模型吗

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRlh5TlFnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b3188cbb609f09767a8e9e7eeb3ffafb3d77aed0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQ0xBRnBBaXdCT2dwellYWmxjbnNHT2dwemRISnBjRlE9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--ef295ed08e817a599d692fd6d8761673d3ed547f/IMG_2643.jpeg)](https://www.superlinear.academy/u/f7e34206)

RainTan [https://docs.z.ai/scenario-example/develop-tools/claude](https://docs.z.ai/scenario-example/develop-tools/claude) 是这样的，甚至还有一些工具来帮助你自动设置，具体可以看一下这篇教程。

鸭哥！这个有点夸张了😂！相当于20刀的gpt plus月费享受到了几乎无限(45-225 messages/5 hrs)的API+SOTA agentic loop

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRlh5TlFnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b3188cbb609f09767a8e9e7eeb3ffafb3d77aed0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQ0xBRnBBaXdCT2dwellYWmxjbnNHT2dwemRISnBjRlE9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--ef295ed08e817a599d692fd6d8761673d3ed547f/IMG_2643.jpeg)](https://www.superlinear.academy/u/f7e34206)

豪仔Gary 是啊，我是觉得 GLM 的性价比是无敌的，尤其是加到 20 美元一个月的计划，基本用不完。

Yan Wang 鸭哥 很喜欢鸭哥在文中提出的四层架构（模型/协议/运行时/契约）以及 “agentic loop + evaluation-first” 的思维模型。我过去一两周在项目中直接把 SOTA Agentic Loop（通过 Codex subprocess）嵌入到原有系统里，基本将协议层和运行时层都 delegate 给 OpenAI。模型层也只是选择模型和 reasoning level。我主要负责给codex的prompt（ 整理context、定义输出/验收标准），以及通过评测结果迭代 prompt，但这也给我带来了一些困惑。

鸭哥文中强调 “evaluation-first”，我目前的理解是：通过明确验收标准→根据evaluation结果迭代 prompt，从而间接影响 agent 的行为。但对codex subprocess的内循环，我只能加observability（例如通过 JSON mode 可视化事件 trace），但无法 intervene（至少不是我们在过程确定性时代改代码的deterministic intervene。我可以给codex连mcp server和SKILL.md，在prompt里面告诉codex他有这些工具然后遇到问题要怎么做，我甚至可以evaluate看看codex在执行任务过程中要没有根据我的prompt用工具并更新prompt。但最终怎么干，干多少的选择权似乎还是在codex那里。）

想请教一下鸭哥：在你理解的 agentic loop + evaluation-first 框架下，evaluation 之后的“intervention”有哪些？除了迭代prompt，还存在哪些更高效更结构性的干预方式？谢谢！

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRlh5TlFnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b3188cbb609f09767a8e9e7eeb3ffafb3d77aed0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQ0xBRnBBaXdCT2dwellYWmxjbnNHT2dwemRISnBjRlE9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--ef295ed08e817a599d692fd6d8761673d3ed547f/IMG_2643.jpeg)](https://www.superlinear.academy/u/f7e34206)

豪仔Gary 我觉得这是一个特别好的问题。我有两点建议：  
  
第一点建议是如果我们发现AI做出的结果不尽如人意，我们不妨更佛系一些，只告诉它哪里有问题，而不具体限定它如何改变自己的策略。等它做了几轮相对稳定之后，让它总结一个SOP出来。这就有点像是一个Working Doc，未来的AI在遇到同样的问题跟着SOP走，基本上就能覆盖大部分的情况。

或者从更抽象的角度来说，我们在干两件事情：第一件事情是提供一个working doc，让AI遵循一定的章法，而不是像完全第一次遇到问题的新手一样乱撞。这有点像是ingest domain knowledge。第二件事情是把简要的domain knowledge转化成具体的SOP过程，这可以delegate给AI。我们不是从头给它写详尽的working doc，而是手把手教，让它在实战中自己总结出心法。

第二个建议是我们也要把握确定性和不确定性操作的合理分配。举个最简单的例子，我们的工作里需要频繁做一个有挑战性又有重复性的操作，比如抓取LinkedIn上的帖子。AI从头写程序能做到，但每次都要磕磕绊绊，迭代15分钟才能写出能用的抓取工具。

像这样的工具就值得复用，这就是skill里面除了prompt以外的另一个方面：确定性的工具。我们可以直接把它变成命令行工具，然后在skills里告诉AI，当你需要抓取LinkedIn post时，直接调用这个命令行就好。这样就能极大地简化它的体力和脑力负担，让它把时间花在真正富于变化的事情上。

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCTFZsa0FnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--4314cc9c4280130e433583e52de12c82496a7266/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQ0xBRnBBaXdCT2dwellYWmxjbnNHT2dwemRISnBjRlE9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--ef295ed08e817a599d692fd6d8761673d3ed547f/IMG_8065.jpeg)](https://www.superlinear.academy/u/5ab3ebed)

“怎么不违反社会主义核心价值观”，一不小心就捕捉到了鸭哥风趣的幽默😆

感谢鸭哥，又出神作！！  
好奇问个小白的问题：那么是否有可能将「运行时层」包装成一个 API 服务暴露出去呢？不用管底层是 Claude Code、Codex 还是其他，用户想要的就是一个确定性的结果，至于路径是什么不 Care，那么似乎把运行时层包装成 API 更符合直觉😅

怎么说呢，就类似于：  
协议层的 API 算是一种 Raw API  
运行时层如果能包装成 API 则是一种抽象层级更高的 API，类似于 SQL  
  

tingbo 包装成api，被调用的时候使用命令行调用claudecode和codex就可以了

可能我想表达的意思是：能否把「运行时」从 Claude Code 或者 Codex 这类的产品形态中剥离出来。  
  
运行时层 = 接口+ 运行时 (Runtime) + 存储  
  
如果能够剥离，那么就可以有新的方式

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCS0ZJS2dNPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--02fe52a7471ae9de8a016303da288c73270cd16f/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJc0FXa0NMQUU2Q25OaGRtVnlld1k2Q25OMGNtbHdWQT09IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--67365f61f655fbc86c65a51f2e9992ab818c41cd/stein_gate.jpg)](https://www.superlinear.academy/u/370b15cd)

把这些期望显式地写出来，并且告诉它怎么验证，它就能自己判断做没做完。

这个描述特别好，非常清晰，close了我之前一直想告诉team的一个用ai的gap

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCTVNBTXdnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--4cdb078a6803ddf96a1c9fc02fe3d083d6ff8a62/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJc0FXa0NMQUU2Q25OaGRtVnlld1k2Q25OMGNtbHdWQT09IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--67365f61f655fbc86c65a51f2e9992ab818c41cd/%E5%A4%B4%E5%83%8F.jpg)](https://www.superlinear.academy/u/452cd000)

认真读完，太棒了。我读到的几个点

1. 四层结构的抽象非常厉害，尤其是“我们关注的是协议层，但问题大多出在运行时层”，非常有启发。不知道这个结构抽象是不是首次被提出来。
2. 让“AI自动改正错误”的前提是AI能观察到错误，而这里面最直觉的方法就是文件，文件是stateful的。
3. 我的直觉是，这个agentic loop非常厉害，很必要，而且是典型的“随着模型变强，生态变好，会变得更完善”的技术进步获益方。Claude Code是恰好走到了这一步（因为生态互相支持的另外动机），但未必是最有效的形式？
4. “想象你在给一个有健忘症的实习生交代任务。这个实习生没有任何上下文，不知道你之前聊过什么，不知道你的隐含期望，只能看到你这一次给他的指令。你需要把验收标准写到这种程度：只根据这些信息，他就能判断自己做完了没有。如果他觉得没做完，他知道还差什么。”这个很重要，记忆和隐含期望，是大多数人blame AI不好用，但其实是自己缺乏认知同理心，所犯的两个主要错误。
5. 如果鸭哥你来自己做一个产品，或者完善builder space，帮助用户能更好地从掌控过程转向掌控结果，你会如何做？

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRlh5TlFnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b3188cbb609f09767a8e9e7eeb3ffafb3d77aed0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQ0xBRnBBaXdCT2dwellYWmxjbnNHT2dwemRISnBjRlE9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--ef295ed08e817a599d692fd6d8761673d3ed547f/IMG_2643.jpeg)](https://www.superlinear.academy/u/f7e34206)

我觉得这些都是非常好的问题。

1. 我的理解是这种四层结构的抽象有一些相关的工作，比如 Claude Code 有一个 AI Harness 的概念，类似我们的运行时层。业界管契约层可能会叫 Guardrail 或者 Eval，但是我个人不知道有其他的类似这样系统性的总结。
2. 这个Agentic Loop虽然在概念上和我们在去年的课程中提出的Agentic AI三大元素是一样的，但是它做了很多工程上的打磨，比如用文件做状态，加入了Claude Code或者Codex打磨过的工作流（Harness）。我觉得Claude Code这样的General Coding Agent算是比较理想的形式了。比如它还有Sub-Agent、有Skills、有Allowed Tools、有Sandbox，这些都可以让用户非常精细地控制Agent Lifecycle的各个方面。  
	但目前主要痛点是，它还是一个独立的命令行。AI在集成的时候往往会遇到各种障碍。如果能做成我们之前提到的General Kernel的概念就最完美了。 [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) 算是往这个方向走了一步，但我觉得还远远不够。
3. 我觉得如果要自己做一个帮助用户掌控结果的 app，有两个挑战：第一是跟用户一起 brainstorm 最终的结果的评判标准。这件事其实特别难，因为我越来越发现”用精准可验证的语言把自己想要什么表达出来”是人类一个很稀有的能力。所以我可能会花更多的精力在帮助用户提升自我探索想要什么的能力上。第二是工作流的设计。这也是我们在和 Trae 的访谈中反复强调的一点：一个软件的 UX 的设计需要体现它自己的产品哲学。我们会把工作流向提升对结果的观测、反馈和定义上，而不是像传统软件 focus 在过程上。这属于更底层一点的举措。

太棒了，感谢鸭哥。解决了我另外一个产品的一个困惑。最开始我是直接用cloud code来进行deep research的，效果其实还挺好，但是后面封装成前端给更多人用的时候，就遇到了不稳定的情况，这里过程也不稳定，结果也不稳定。

首先没让claude code做到流式日志输出，有的时候可能要等个10分钟，有的时候更长可能任务失败了也没有提示。很难debug或优化。可能也受限于模型能力。当时用的是GLM 4.6，我让他生成一些文件之后再调用一个脚本，处理的不是很好，于是后面只让他生成文件，我用程序来执行那个脚本，但是没法很好的给出输出文件的路径。当时的方案是在文件系统里面找最新创建的文件，这其实会带来非常大的不确定性。

第2版本迭代是打算自己实现一个agentic loop。以实现结果和过程的可控，但是发现其实就是再重新造一个claude code 或manus，文件流，工具流（工具的设计和定义）等等。甚至像grep和glob 这种工具也要给他设计和提供。所以这个项目进行到一半又搁置了。目前跑的是一个预定义的workflow，那这个其实又回到了很早以前的老路。

所以鸭哥这里给我的启发就是，用claude code 复用整个agentic生态，并且把中间过程流式透明的输出。结合最新的skills，把固定性的逻辑用脚本的形式让他执行。并且用上最新的codex和GPT5.2。其实模型能力是非常重要的一环。这样其实也是可以形成复利的，因为每一次生态的提升、模型能力的提升都代表着你的项目效果预期会变得更好。水涨船高。

感谢鸭哥！V3迭代的思路很清晰了。

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRlh5TlFnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b3188cbb609f09767a8e9e7eeb3ffafb3d77aed0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQ0xBRnBBaXdCT2dwellYWmxjbnNHT2dwemRISnBjRlE9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--ef295ed08e817a599d692fd6d8761673d3ed547f/IMG_2643.jpeg)](https://www.superlinear.academy/u/f7e34206)

你这个总结和分享太好了！是的我也觉得这是个很适合你的项目的下一步。

看到邮件推送马上点进来了，看完之后对运行时层有相同感触。最近在做一个校验Agent，根据文件描述和校验任务对一个word和一个excel做文件内和文件之间的校验。自己实现调试好几天都效果平平，对widesearch提示词魔改后，codex能很完美的完成。有点不太明白想请教鸭哥的是，为什么code agent泛化效果能够那么好？还有什么情况需要自己构建agent吗？当因为隐私不得不自己构建agent时，最好是根据任务构建不同的工具还是参考code agent，提供最简单的读写文件，执行脚本呢？

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRlh5TlFnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b3188cbb609f09767a8e9e7eeb3ffafb3d77aed0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQ0xBRnBBaXdCT2dwellYWmxjbnNHT2dwemRISnBjRlE9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--ef295ed08e817a599d692fd6d8761673d3ed547f/IMG_2643.jpeg)](https://www.superlinear.academy/u/f7e34206)

我觉得它是有三方面的原因：

第一是它本身是一个Agentic Loop，所以天生就有Agentic AI自我修正、多步决策的特性，这个特性是特别强大的。只要做到了这一点，就可以看见AI完成任务的效果、性能有巨大的提升，和单纯调用API不可同日而语。

第二是Claude Code、Codex这样的通用Coding Agent面对的本来就是非常通用、可范化的问题，各大厂商都在这些工具上投入了海量的精力来让它变得好用，因此Prompt和Workflow已经是经过打磨的产品了，比我们自己手搓的初步产品又要好不少。

第三个原因是像我们在 [这篇文章](https://www.superlinear.academy/c/ai-resources/manus-agentic-ai) 中提到的那样，每多一个工具对于Agent系统完成任务的能力都是个巨大的提升。而General Coding Agent它可以上网搜索，可以撰写代码，可以执行代码，这些都是特别强大的工具，因而也比一般的Agent又要更强。

Yan Wang 鸭哥 感谢鸭哥回复  
第一点确实，我觉得我从AI Builder到AI Architect已经内化了Agentic Loop强大的感受。  
第二点关于Prompt我比较好奇的是鸭哥是怎么写出来那么好用的Prompt的，在写Prompt的时候有什么流程，会考虑哪些问题，如何调优。从最开始的cursorRule到widesearch都是我现在每天都一直使用的，我印象里没有直接聊过这个，不知道是不是我漏了或者看完忘了，如果之前聊过麻烦给我关键词我去找找。  
第三点我觉得我还是得再内化coding的强大与ai coding带来的成本降低

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRlh5TlFnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b3188cbb609f09767a8e9e7eeb3ffafb3d77aed0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQ0xBRnBBaXdCT2dwellYWmxjbnNHT2dwemRISnBjRlE9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--ef295ed08e817a599d692fd6d8761673d3ed547f/IMG_2643.jpeg)](https://www.superlinear.academy/u/f7e34206)

Howie 这个确实是个特别好的问题，但也没有太多秘诀。核心还是 evaluation-first mindset。

一个好的 prompt 有它自己的标准。比如我们可以新建一个 benchmark，用任务完成的成功率作为 metric，然后在这上面迭代，尽可能增加成功率。在这个过程中，如果遇到不满意的情况，可以做 failure pattern analysis，有针对性地改进 prompt。

因此你也可以看出来，在有了这个 benchmark 之后，prompt 的改进更多是一种体力活，也可以交给 AI 用来做自动化。