
## 核心洞察
- 学习的本质是反复地实践-总结，是在解决问题中发展出正确的方法论。科学或者工程经验就是是这些方法论的压缩和升华。然而，现在的学习经常被误认为是学概念、学理论。这面临一个问题是，这些概念/理论提出之前所经历的迭代、试错、脚手架被拆掉了，人们所见的只有一篇正确的论文、完整的工程产品，因而无法完全理解和内化其中的智慧。
	- 【Codex总结：*现代学习材料过度呈现已经稳定下来的概念、理论和成品，隐藏了知识生成时经历的混乱问题、现实阻力、判断分歧、失败路径和标准构造过程。结果是学习者学会了复述结论，却没有学会如何在不确定情境中形成方法论。*】
- AI时代真正稀缺的不是信息，而是高质量学习场。我们不应该再尝试给人信息，而是应该把人放到正确的环境里。高质量学习场是一个被设计过的探索环境。它设定合适的问题情境，为人提供行动空间，以及行动结果的校准点和复盘机制，让人重新长出一套知识背后的判断结构。
	- 【Codex总结：*AI 时代，稀缺的不是可获得的信息，而是能让人形成判断力的学习场。高质量学习场不是以讲解知识为中心，而是设计一个可探索的问题环境：它提供必要材料、行动空间和理解校准点，让学习者在预测、构造、比较、失败、修正和迁移中，逐步重建知识背后的判断结构。信息仍然重要，但它从主角变成脚手架。*】

参考文献
 [为什么所有人都在学名词，但真正拉开差距的是动词](https://www.superlinear.academy/c/ai-resources/verb)
 https://www.superlinear.academy/c/posts/interview
 https://www.superlinear.academy/c/notes/challen-ai
 


## Problem Hypothesis
who exactly has this problem：希望主动学习一个自己真正想理解的主题的人（主动投入至少 2 小时学习行动）；不只是想查答案或完成一次任务，而是想理解原理、本质、适用边界或迁移方式。
how often：在读完/看完/问完之后，需要应用自己学习的时候。
how severely：投入了时间但没有形成稳定理解：记不住、反复学、只能复述、不会举例/反例/迁移，甚至因为反复失败而对学习产生恐惧或逃避。
what do they currently do about it：继续看更多材料、反复看、问 AI、记笔记、硬背、收藏课程/文章，但这些做法仍以信息输入为主，不能稳定帮助他们产生真正的理解。


## Pressure-testing PH

**反证 1：很多人并没有“深度理解”的真实 job**

MOOC 数据是一个很强的提醒：大量人报名/开始学习，并不代表他们真的有完成或深入理解的目标。Harvard/MIT 早期 MOOC 完成率低，后续研究也不断强调 learner intent 很关键。  
这会打掉 “主动学习复杂知识的人” 这个 who：他们可能只是探索、收藏、缓解焦虑、查答案，不是在追求“长出方法”。

来源：[MOOC completion discussion](https://en.wikipedia.org/wiki/Massive_open_online_course), [MOOC dropout patterns](https://arxiv.org/abs/2008.05209)

**反证 2：问题可能不是“缺试错总结”，而是用户用了低效学习策略**

用户卡住后表现出来的痛，未必是“缺少自己的判断和方法”；它可能是更普通的问题：材料太难、基础不够、没有时间、缺少清晰路径、考试压力、注意力不够、或只是缺更好的解释。

**反证 3：新手可能更需要清晰指导和样例，而不是尝试失败**

Kirschner/Sweller/Clark 和 Mayer 对 pure discovery learning 的批评说明：如果学习者缺少 schema，让他们尝试、失败、总结，可能只是增加认知负荷。  
这会打掉 “缺少尝试失败总结是主要原因” 这个 root cause。对很多人来说，真正问题可能是：材料太难、前置知识不足、样例不够、讲解顺序不对。

来源：[Kirschner et al. 2006](https://doi.org/10.1207/s15326985ep4102_1), [Mayer 2004](https://doi.org/10.1037/0003-066X.59.1.14)

**反证 4：用户可能不喜欢真正有效的学习体感**

Deslauriers 等人的 PNAS 研究发现，学生在 active learning 中实际学得更多，但主观上觉得自己学得更少。  
这会打击 severity/willingness：即使用户确实缺方法，他们也未必把“费劲的尝试和失败”识别为自己想要的解决路径。他们可能更喜欢“我听懂了”的流畅感。

来源：[Deslauriers et al. 2019](https://www.pnas.org/doi/10.1073/pnas.1821936116)

**反证 5：市场行为更像是在买答案，不是在买“长出方法”**

Chegg、QANDA、Brainly 这类产品的规模说明，学习场景里有巨大需求是“帮我解题/给我答案/快速推进”。QANDA 的公开资料显示其核心功能就是拍题给解法，并已有大规模用户。  
这不证明你的用户不存在，但证明 “学习复杂知识的人” 太宽了。很多人学习时真实购买的是速度和答案，不是反复试错总结。

来源：[Chegg](https://en.wikipedia.org/wiki/Chegg), [QANDA](https://en.wikipedia.org/wiki/QANDA), [Brainly](https://en.wikipedia.org/wiki/Brainly)

**反证 6：AI 可能已经把 workaround 变得足够好**

学生已经用 GenAI 做总结、写作、coding、解释和个性化辅导。一些研究/调查同时指出 dependency 和 shortcut 风险。  
这意味着用户可能并不认为 workaround 失败：他们可能觉得“多问几轮 AI”已经够了，除非你能证明他们在真实任务里反复撞墙。

来源：[Student perceptions of GenAI](https://arxiv.org/abs/2410.22289), [AI reliance in higher education](https://arxiv.org/abs/2506.13845)

**所以真正被打掉的是哪部分？**

不是打掉 “学习复杂知识会卡住”。这个大概率是真的。

被打掉的是这几个泛化：

- `who` 太宽：不是所有主动学习复杂知识的人都有这个痛。
- `root cause` 太早下结论：不能直接说原因是缺少尝试-失败-总结。
- `severity` 未证：很多人可能只是偶尔烦，不是强痛点。
- `workaround` 未证：对一部分高自驱用户，做题、复现、项目、问老师、问 AI 可能已经够好。
- `market pull` 未证：用户可能想要答案速度，不想要认知摩擦。

**吸收反证后的更硬版本**

> 在过去 30 天内，已有一定基础、并为了一个明确目标学习复杂知识的人，在投入数小时阅读、看课、问 AI 或记笔记后，仍然在尝试使用这些知识时卡住：他们能复述解释，但遇到变体问题、设计判断、证明思路、工程取舍或论文复现时，无法形成自己的方法。
> 
> 他们当前会继续看更多材料、问更多 AI、重读、整理笔记，或零散做题/实验；但如果这些方式没有帮助他们从“听懂解释”进入“自己能尝试、失败、修正和总结”，学习就会停滞。这个问题最可能出现在学习数学、AI、工程系统、科研方法或复杂理论，并且明确追求可迁移理解的人身上。

这版的关键变化是：  
**不要把“缺少试错总结”写成确定原因，而是把用户可观察的痛写成：能复述，但一到使用、变体、判断、复现就卡住。**

然后 customer discovery 就问一个更狠的问题：

> 你最近一次“看懂了但用不出来”的具体场景是什么？你之后做了什么？有没有真的前进？

如果他们说不出具体场景，problem 弱。  
如果他们说只是基础不够，problem 改。  
如果他们说 AI/题目/老师已经解决，problem 弱。  
如果他们反复描述“我懂解释，但一做判断就没有方法”，problem 才变强。

## Market Search
可以。基于当前 problem hypothesis，我会把市场先画成这样：

> 用户能看懂解释，但在自己处理新问题、判断方法适用性、解释取舍、复现论文/系统或完成变体任务时没有方法。

**结论先说**

这个市场不是空白。相反，它很拥挤。  
真正空白的不是“帮助学习”，而是：

> 帮已有基础的人，从“理解解释”走到“形成可迁移判断”。

但这个空白很窄，而且容易被 3 类东西吞掉：AI 问答、结构化练习平台、真实项目/老师/社区。

**Competitive Map**

|类别|代表|它解决什么|对你的威胁|没覆盖的缺口|
|---|---|---|---|---|
|AI 问答/学习助手|ChatGPT, Claude, Khanmigo, NotebookLM, Oboe|解释、总结、生成 quiz、答疑|用户已经习惯“问 AI”；边际成本极低|仍偏解释/问答，未必让用户形成方法|
|作业/答案工具|Photomath, QANDA, Gauth, Chegg, Brainly|快速解题、步骤、答案|说明用户真实行为常常是“给我答案”|优化完成任务，不优化迁移判断|
|结构化练习平台|Brilliant, Khan Academy, Codecademy, DataCamp, Kaggle Learn|互动题、课程路径、练习反馈|已经占据“active learning”心智|多数围绕题目/正确率/技能熟练，不一定重构判断过程|
|探索式模拟/解释|PhET, Distill, TensorFlow Playground, Observable notebooks|可视化、模拟、explorable explanation|最接近“学习场”|内容生产极重，领域不可轻易泛化|
|项目/复现/社区学习|fast.ai, Hugging Face course, Papers with Code, GitHub, Discord, bootcamps|真实项目、复现、实践共同体|对高动机用户很强|门槛高、碎片化、缺复盘结构|
|人类老师/导师|tutor, 研究组, cohort course|个性化反馈、判断训练、动机|质量最好|贵、不可得、不可规模化|

**强正面信号**

1. 用户确实大量寻求学习帮助。Photomath 2021 年已有 2.2 亿下载，QANDA 到 2024 年有 9000 万注册用户、63 亿次问题解决。这说明“学习卡住后找外部帮助”是高频行为。  
    来源：[Photomath](https://en.wikipedia.org/wiki/Photomath), [QANDA](https://en.wikipedia.org/wiki/QANDA)
    
2. Active learning 有强教育证据。STEM 中主动学习显著优于传统 lecture。  
    来源：[Freeman et al. 2014](https://www.pnas.org/doi/10.1073/pnas.1319030111)
    
3. Brilliant、Codecademy、PhET 都说明“互动/练习/模拟”不是小众幻想。Brilliant 有 90+ guided STEM courses，Codecademy 早期已到 4500 万用户，PhET 有 125+ simulations 且多语言传播。  
    来源：[Brilliant](https://en.wikipedia.org/wiki/Brilliant_%28website%29), [Codecademy](https://en.wikipedia.org/wiki/Codecademy), [PhET](https://en.wikipedia.org/wiki/PhET_Interactive_Simulations)
    

**强负面信号**

1. 用户可能不买“深度理解”，而买“答案速度”。Chegg 被 ChatGPT 冲击，Gauth/Photomath/QANDA 的规模都说明很多用户的 revealed preference 是快速完成任务。  
    来源：[Chegg/ChatGPT impact](https://www.investopedia.com/chegg-shares-plunge-after-company-warns-that-chatgpt-is-impacting-growth-7487968), [Gauth](https://www.wired.com/story/gauth-ai-math-homework-app)
    
2. AI tutor 已经在逼近。Khanmigo、NotebookLM、Oboe 都在把“解释 + quiz + 个性化课程”商品化。你的差异不能只是“AI 帮你学”。  
    来源：[Khanmigo](https://en.wikipedia.org/wiki/Khan_Academy#Khanmigo), [NotebookLM](https://en.wikipedia.org/wiki/NotebookLM), [Oboe](https://www.theverge.com/ai-artificial-intelligence/783624/oboe-ai-education-learning)
    
3. 高质量学习场供给很重。Distill 是很接近你审美的案例，但 2021 年 hiatus，本质问题是科学、设计、编辑、维护都太贵。  
    来源：[Distill Hiatus](https://distill.pub/2021/distill-hiatus/)
    
4. 个性化学习平台历史战绩不轻松。Knewton 融资很多，最后被 Wiley 以低于 1700 万美元收购；AltSchool 从开学校转成软件公司。这说明“更好的学习系统”不自动变成好生意。  
    来源：[Knewton](https://en.wikipedia.org/wiki/Knewton), [AltSchool/Altitude Learning](https://en.wikipedia.org/wiki/Altitude_Learning)
    

**最危险的竞争判断**

你的真正竞争对手不是 Brilliant 或 Khan Academy 单独某一家，而是用户的默认路径：

> 看材料 → 问 ChatGPT → 找 YouTube/博客 → 做几个题/项目 → 卡住就继续问 AI。

这个 workaround 免费、即时、足够灵活。  
你必须证明：在某些复杂主题上，它不能稳定把用户带到“我能自己判断/迁移/复现”。

**可能的 wedge**

最有希望的入口不是泛教育，而是：

> 已有基础、正在学 AI/数学/工程系统，并且已经经历过“看懂但用不出”的人。

尤其是 AI 学习可能更适合第一 wedge：材料新、论文密、架构复杂、用户有强动机，且“只看解释但不会复现/改造/判断取舍”的痛更明显。

**下一步建议**

不要继续做大市场判断了。直接做 10 个竞品用户访谈：

- Brilliant / Coursera / DeepLearning.AI 用户；
- ChatGPT 重度学习用户；
- 正在学 AI paper / 数学 / ML systems 的人；
- 做过论文复现或项目学习的人。

核心只问一句：

> 最近一次你“看懂了解释，但自己用不出来/判断不了/迁移不了”的具体场景是什么？

如果他们讲不出具体场景，这个 problem 弱。  
如果他们讲得很具体，而且 workaround 都只是继续看/问/收藏，那这个 problem 才开始站住。