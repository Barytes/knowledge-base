
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
### Competitors

**1. Direct Competitors**

|Tier|Players|Why They Are A Real Threat|
|---|---|---|
|AI learning tutors|[Khanmigo](https://khanmigo.ai/), ChatGPT Study Mode, Google Learn About|它们直接打“不要直接给答案，而是引导学习”的心智。Khanmigo 明确说自己会让学习者 critical thinking、solve problems without giving direct answers。Google Learn About 则把搜索结果变成 structured learning experience。你的“AI learning field”如果只是问答加练习，很容易被它们吃掉。|
|Interactive STEM platforms|[Brilliant](https://brilliant.org/)|Brilliant 已经在说 “learn by doing”“visual and interactive”“work through problems step-by-step”。它还有 1000 万+ learners、10 万+ 5-star app reviews。它对数学、CS、科学直觉训练的定位非常接近你的早期 wedge。|
|AI-generated course builders|[Oboe](https://www.theverge.com/ai-artificial-intelligence/783624/oboe-ai-education-learning), NotebookLM study tools|Oboe 可以根据 prompt 生成课程、文本、音频、quiz、games。NotebookLM 已经能从用户材料生成 flashcards、quizzes、learning guide。它们威胁你的“把材料转成学习路径”部分，尤其是低成本、泛主题覆盖。|
|Coding/data interactive learning|[Codecademy](https://www.codecademy.com/), [DataCamp](https://www.datacamp.com/)|它们已经有 guided path、browser IDE、projects、AI assistant、career tracks。Codecademy 明确提供 step-by-step guidance、integrated code editor、AI Learning Assistant。若你的第一 wedge 是 AI/CS 学习，它们会从“技能获得”方向包抄。|

**2. Indirect Competitors**

|Tier|Players|Why They Are A Real Threat|
|---|---|---|
|General AI assistants|ChatGPT, Claude, Gemini|用户默认 workaround 已经是“继续问 AI”。它们免费/低价、即时、灵活，而且用户不需要迁移到新工具。你必须证明普通 AI 深聊不能稳定解决“看懂但用不出”。|
|Answer engines / homework help|[Photomath](https://en.wikipedia.org/wiki/Photomath), [QANDA](https://en.wikipedia.org/wiki/QANDA), Brainly, Chegg|它们证明用户的 revealed preference 往往是“快点给我答案/步骤”。QANDA 有 9000 万注册用户、63 亿+ solved questions；Photomath 被 Google 收购。你的深度理解产品会被“更快完成任务”的需求抢走大量用户。|
|MOOCs / course marketplaces|Coursera, Udemy, DeepLearning.AI, fast.ai|它们有品牌、内容供给、证书、企业预算。Coursera/Udemy 2026 年完成合并，定位就是 AI-era skills giant。它们不一定解决“判断力”，但能占据用户预算和学习入口。|
|Real projects / communities|GitHub, Papers with Code, Hugging Face, Discord, research groups|对高动机用户来说，真实复现、项目、社区反馈可能比任何 learning lab 更有说服力。你的产品若不比“做项目 + 问社区 + 问 AI”更省力，就很难留下这批人。|
|Human tutors / cohorts|私教、bootcamp、cohort course、导师制|它们贵，但对“形成判断”这件事非常强。真正愿意付费追求深度理解的人，可能更愿意买人类反馈，而不是软件。|

**3. Potential Acquirers**

|Tier|Players|Why They Might Acquire Or Crush You|
|---|---|---|
|Google|NotebookLM, Learn About, Gemini, Photomath, Classroom|Google 已经同时有搜索入口、学习模型、NotebookLM、Photomath、教育分发。它可以把“学习场”变成 Search/NotebookLM/Gemini 的一个模式，而不是独立产品。|
|OpenAI / Anthropic|ChatGPT, Claude, Edu/workspace plans|它们最容易把你的核心体验做成“study mode / tutor mode / lab mode”。如果模型端能长期记忆、生成交互练习、跟踪薄弱点，独立产品的差异会被压缩。|
|Coursera-Udemy|Course marketplace + AI reskilling|合并后的平台有课程供给、企业客户、证书和学习数据。如果它们发现“AI course completion/transfer”是痛点，可以把 learning lab 嵌进高价值课程。|
|Skillsoft / Codecademy|Enterprise learning + technical skills|Skillsoft 已经收购 Codecademy。它们若要提高技术学习完成率和项目迁移能力，会有动机买一个更强的 AI practice/reconstruction layer。|
|Microsoft / LinkedIn / GitHub|LinkedIn Learning, GitHub Copilot, enterprise budgets|对职业技能和开发者学习，它们拥有分发、身份、工作流入口。GitHub Copilot 已经在“边做边学框架/代码库”上天然接近你的 problem。|

**4. Adjacent Players Who Could Move In**

|Tier|Players|Why They Are Dangerous|
|---|---|---|
|AI coding environments|[Cursor](https://en.wikipedia.org/wiki/Cursor_%28code_editor%29), [Replit](https://en.wikipedia.org/wiki/Replit), GitHub Copilot|如果 AI/CS 是你的 wedge，它们可以把学习嵌入真实 coding workflow：解释代码、生成实验、改错、复现论文。对工程学习来说，真实 IDE 比独立 learning app 更接近问题现场。|
|Study tooling|[Quizlet](https://en.wikipedia.org/wiki/Quizlet), Anki, Coconote-like note-to-study tools|它们有学生入口和学习习惯。Quizlet 已经有 AI tutor、AI study materials、课程组织。它们可以从记忆/quiz 往 deeper learning 上走。|
|Gamified learning giants|[Duolingo](https://en.wikipedia.org/wiki/Duolingo)|Duolingo 已从语言扩展到 math、music、chess，并有极强 retention/habit machine。它未必适合复杂理论，但如果它选择“AI/math intuition”方向，会比你更会做 consumer engagement。|
|Explorable media / simulations|PhET, Observable, Labster, Distill-like content|它们最接近“学习场”的审美和机制。威胁不是规模，而是证明高质量 learning field 更像内容/媒体 craft，不像纯软件。|
|Knowledge work tools|Notion, Obsidian, NotebookLM, Readwise|用户学习复杂材料时已经在这些地方整理笔记、资料、摘要。如果它们把“从笔记生成练习/迁移题/复盘”做好，你的入口会被笔记工具吃掉。|

**最真实的威胁不是某一个竞品**

最危险的是组合替代：

> 用户用 ChatGPT/Claude 解释概念，用 NotebookLM 整理材料，用 YouTube/Coursera 补课，用 GitHub/Replit 做项目，用 Quizlet/Anki 记忆，用社区问问题。

这个组合免费或低价，足够灵活，而且已经在用户习惯里。你要赢，不能只是“更好的学习工具”，而要找到一个它们组合起来仍然解决不好的窄场景。

我现在会把你的 wedge 暂时压成：

> AI/数学/工程系统学习者，在已经看过解释后，仍无法处理变体、判断取舍或复现实现的那一刻。

因为这里 Brilliant 太浅，ChatGPT 太散，课程太线性，项目/社区太重。这个缝隙最像你的入口。

### Competitor Customer Complaints
对 review 做完一轮后，我看到的不是“没人解决学习”，而是：很多产品已经解决了**入门、路径、互动、动机**，但没稳定解决**从 guided exercise 走到独立判断/迁移/真实任务**。

我采样的主要来源：Trustpilot 的 [Brilliant](https://www.trustpilot.com/review/brilliant.org)、[Coursera](https://www.trustpilot.com/review/coursera.org)、[Khan Academy](https://www.trustpilot.com/review/www.khanacademy.org)、[edX](https://www.trustpilot.com/review/www.edx.org)、[Udacity](https://www.trustpilot.com/review/udacity.com)，以及 G2 的 [DataCamp](https://www.g2.com/products/datacamp/reviews)、[Codecademy](https://www.g2.com/products/codecademy/reviews)。注意：Trustpilot 容易放大 billing/support 怨气；G2 很多 review 是 vendor-invited/incentivized，所以要看模式，不要把单条评论当真相。

**Top Unresolved Complaints**

|Complaint|Where It Shows Up|What It Means|Does Our Hypothesis Address It?|
|---|---|---|---|
|太 beginner / 太浅，advanced learner 不够用|DataCamp G2 提到 advanced depth limited；Codecademy G2 提到 advanced topics limited；Brilliant review 有用户希望更多 advanced math/CS/AI infra 内容|现有平台擅长入门和结构化路径，但高阶学习者会觉得不够深|**Yes**，如果我们锁定“已有基础但卡在判断/迁移”的人|
|练习太 guided，像填空，不像独立解决问题|DataCamp G2 有用户说 exercises 过度引导，可能完成课程但没有真正掌握；Codecademy 也被抱怨缺 real-world projects|这非常贴近“能跟上步骤，但自己处理变体时没方法”|**Strong yes**，这是最支持 hypothesis 的信号|
|缺少真实项目、端到端场景、 messy reality|DataCamp 用户要求 larger-scale projects、messier real-world data、local setup；Codecademy 用户要求 real-life scenarios|用户不是只缺解释，而是缺从课程环境迁移到真实环境的桥|**Yes**，但这也暗示产品可能要接近项目/案例，而不只是概念 lab|
|反馈质量不稳定或不可信|Khan Academy review 抱怨 unclear lessons、incorrect answers、Khanmigo 生成错误问题；edX review 抱怨 peer grading variable/unreliable|学习者不是只需要更多反馈，而是需要可信反馈；AI/peer feedback 如果不稳，会伤害学习|**Partly**。我们的 hypothesis 指向判断形成，但 solution 必须解决 feedback trust|
|内容过期、依赖坏掉、课程维护差|edX review 多次提到 outdated content、404、旧代码跑不通；Udacity summary 也提到部分 content outdated|对 AI/工程系统尤其危险：材料一过期，学习体验直接断裂|**Indirectly**。如果做 AI/工程学习，这是必须解决的供给问题|
|平台/订阅/访问体验消耗学习动机|Coursera/edX Trustpilot 大量抱怨 subscription、refund、access、progress loss；Brilliant 也有 renewal/cancel 争议|这不是我们的核心 learning hypothesis，但会决定用户是否信任产品|**No**，这是运营/信任风险，不是 problem-solution fit 证据|

**最支持我们的证据**

最强的 pattern 是 DataCamp/Codecademy 这类“互动学习已经很强”的产品，用户仍然抱怨：

> 太 guided、太基础、缺真实场景、缺 open-ended challenge、缺端到端项目。

这和我们的 problem hypothesis 对得很准：

> 用户能完成结构化解释和练习，但一到独立处理变体、真实任务、设计判断时，就没有方法。

所以这不是“没人做 interactive learning”。恰恰相反，是 interactive learning 已经成立，但下一层痛点还在。

**不支持我们的证据**

很多差评其实跟“深度理解”没关系，而是 billing、客服、退款、访问、内容过期、平台稳定性。这说明市场里很多用户的痛不是“我没有形成判断”，而是“我被平台体验坑了”。如果我们只拿这些差评证明 problem，会误判。

还有一个危险点：Brilliant 的正面 review 很多，用户赞它 interactive、visual、progressive、fun。这说明如果我们做得只是“更好的互动解释 + 题目”，Brilliant 已经很强，不构成差异。

**Implication**

目前最可守的 wedge 不是泛学习场，而是：

> 面向已有基础的 AI/数学/工程系统学习者，解决“现有互动课程太 guided、太浅，不能让我独立处理真实变体/设计取舍/复现任务”的问题。

换句话说，我们的差异不应该是“更会教概念”，而应该是：

> 从 guided learning 过渡到 independent judgment。


### TASM/SAM/SOM
下面是更准确的 v1，不再把“AI education market”直接当你的 TAM。你的真实市场要从大池子里连续折损。

**0. 先定义市场边界**

你的产品不是泛在线教育，也不是普通 AI tutor。更准确的 category 是：

> complex knowledge judgment learning：帮助已有基础的学习者，从“能看懂解释”走到“能独立判断、迁移、复现、处理变体”。

所以市场要分三层：

|Layer|含义|是否属于你|
|---|---|---|
|AI in education|AI tutor、grading、LMS、内容生成、课堂管理|太宽，只能做 top-down 锚点|
|AI-enabled learning platforms|AI 辅助课程、tutor、adaptive learning、练习平台|部分相关|
|deep technical judgment learning|AI/数学/工程系统中，从解释到独立判断/迁移|你的真实 wedge|

**1. Top-Down TAM**

公开锚点：Grand View Research 估计 AI in education 市场 2025 年 $8.3B，2026 年 $11.4B，2033 年 $57.2B，2026-2033 CAGR 25.9%；learning platform & virtual facilitators 是最大应用段之一。[source](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-education-market-report)

但这包括 K-12、行政、grading、LMS、语言学习、学校系统等。不能全算你的 TAM。

我会这样折：

```
2026 AI in education market: $11.4B
× learning / tutoring / smart-content relevant share: 35%-55%
× complex knowledge / higher-ed / corporate / technical-learning share: 30%-50%
= relevant TAM: ~$1.2B-$3.1B today
```

2033 forward-looking TAM：

```
$57.2B
× 35%-55%
× 30%-50%
= ~$6B-$15.7B
```

所以更准确的说法是：

> Broad TAM 很大：$11B+。  
> Relevant TAM 现在大概 $1B-$3B，未来可能 $6B-$15B。  
> 但你的 early SAM 会小很多。

**2. SAM：真正可服务市场**

我建议拆成三个 SAM，而不是混在一起。

|Segment|User|Buyer|估算|
|---|---|---|---|
|Prosumer technical learners|学 AI/数学/工程系统的个人|学习者本人|$7M-$190M|
|Engineering / AI teams|工程团队、AI infra、研究团队|Eng manager / CTO / L&D|$10M-$200M|
|Course / school / creator layer|高阶课程、训练营、教育机构|课程方/学校|$5M-$80M|

**Prosumer SAM**

假设：

```
reachable serious AI/math/engineering learners: 10M-25M
× 有“看懂但用不出/判断不了”痛点: 20%-40%
× 愿意为此付费: 3%-8%
× ARPU: $120-$240/year
= $7M-$192M
```

Base case：

```
18M × 30% × 5% × $180 = ~$49M/year
```

这比上一版低，但更诚实。很多人会免费问 ChatGPT，不会为“判断力”额外付费。

**Enterprise / Team SAM**

Coursera + Udemy 合并后覆盖 290M learners、18,000 enterprise customers、95,000 instructors；这说明企业学习预算真实存在，但也说明平台正在整合。[source](https://www.axios.com/2026/05/11/coursera-udemy-ai-skills)

假设：

```
enterprise learning customers reachable anchor: 18,000
× advanced technical / AI judgment need: 5%-15%
× ACV: $10k-$75k
= $9M-$203M/year
```

Base case：

```
18,000 × 10% × $30k = ~$54M/year
```

这可能比 prosumer 更健康，因为 buyer 有预算。但它也会逼你做 SSO、admin、reporting、security、ROI，不再是纯学习体验。

**Course / Creator / Institution SAM**

这是“lab layer”卖给课程方，而不是直接卖给学习者。

```
高阶 AI/CS/math/course providers
× 每年 $2k-$20k tooling/license/content enhancement
= $5M-$80M
```

这个渠道可能更适合早期验证，但天花板取决于课程方是否愿意把你嵌进它的核心体验。

**Refined SAM**

更可信区间：

> **$70M-$350M/year**

Base case 大概：

> **$120M-$180M/year**

这已经不是小市场，但也不是随便讲 billion-dollar 的市场。它要求 wedge 非常准。

**3. SOM：3-5 年可拿到的部分**

我会分成三种路线：

|Route|3-year SOM|5-year SOM|核心条件|
|---|---|---|---|
|Prosumer-only|$1M-$5M ARR|$5M-$20M ARR|内容/体验强，低 CAC，有自然传播|
|Team-first|$2M-$8M ARR|$10M-$40M ARR|能证明 onboarding / AI skill / engineering judgment ROI|
|Platform layer for courses|$500k-$3M ARR|$5M-$15M ARR|能嵌入课程方工作流，供给成本低|

最现实的 early target：

> 3 年 $3M-$10M ARR。  
> 5 年 $15M-$40M ARR。  
> $100M ARR 需要你从 niche lab 变成 technical learning infrastructure，而不只是内容产品。

**4. Market State**

|Market|状态|对你的含义|
|---|---|---|
|AI education|快速扩张|timing 好，但竞争密度高|
|Online courses|成熟 + 整合|Coursera/Udemy 合并说明平台型课程在集中|
|Consumer learning|成熟、retention 驱动|Duolingo 2026 Q1 有 56.5M DAU、12.5M paid users，但增长预期压力很大，说明 consumer learning 要赢很难 [source](https://www.barrons.com/articles/duolingo-earnings-stock-price-d3729e51)|
|AI skills training|高速增长|Coursera 称 2026 年生成式 AI 课程每 3 秒有一次 enrollment；Udemy 数据显示 GitHub Copilot / Microsoft Copilot 学习需求暴涨 [source](https://www.axios.com/2025/09/19/workers-ai-skills-microsoft-copilot-udemy)|
|Deep technical judgment learning|未成熟|机会在这里，但 demand 未充分验证|

**5. Buyer Landscape**

|Segment|Budget Holder|Influencer|User|是否同一人|购买理由|
|---|---|---|---|---|---|
|Prosumer|学习者本人|技术 KOL、课程作者、朋友|Same|是|我想学懂、转岗、研究、做项目|
|Engineering team|EM / CTO / VP Eng|Staff engineer、tech lead|工程师|否|新人 onboarding、AI 工具使用质量、减少低质量产出|
|Enterprise L&D|L&D / HR / procurement|CTO / business leader|员工|否|AI reskilling、skills matrix、completion、credential|
|Higher ed|教授、院系、instructional design|学生反馈、学校政策|学生|否|提高课程学习效果|
|Course creator|课程作者/训练营|学员反馈|学员|部分重合|提高课程转化、完成率、口碑|

**我现在会推荐的 buyer 顺序**

不要先打 enterprise L&D。它会把你拖进 completion dashboard 和 credential。  
也不要只打 consumer 泛学习者，流失会很高。

最好的 wedge 可能是：

> 高动机 prosumer + 小团队 technical learning。

比如：AI engineer、ML infra learner、研究生、indie builder、工程团队中新技术 onboarding 的人。

**6. Pressure Test**

最脆弱假设：

1. **问题发生率**：到底有多少人真的有“看懂但判断不了”的痛？
2. **付费意愿**：他们愿意为此单独付费，还是继续用 ChatGPT + 课程 + 项目？
3. **买方错位**：真正痛的是 learner，但有预算的是企业/学校；企业/学校买的可能不是深度理解。
4. **供给成本**：如果每个 lab 都像 Distill 一样重，毛利和扩展性会很差。
5. **AI tutor commoditization**：ChatGPT/NotebookLM/Khanmigo 会不断吞掉“解释、练习、quiz、学习路径”。
6. **ROI 证明**：企业会问它是否减少 onboarding 时间、提高项目交付、降低 AI 误用，而不是“学生感觉更懂”。

**更准确的结论**

这个市场不是：

> online education 很大，所以可以做。

而是：

> AI reskilling 和 technical upskilling 正在扩张，课程平台正在整合，AI tutor 正在商品化；在这个背景下，仍可能存在一个未成熟但有价值的窄市场：帮助已有基础的技术学习者从“理解解释”进入“独立判断和迁移”。

我会把 v1 模型定为：

```
Relevant TAM: $1B-$3B today, $6B-$15B by 2033
SAM: $70M-$350M/year
Base SAM: $120M-$180M/year
3-year SOM: $3M-$10M ARR
5-year SOM: $15M-$40M ARR
```

这版更适合 founder decision：够大，可以继续；但没有大到允许泛化。早期必须用一个很窄的 AI/数学/工程系统 wedge 去验证。

### Trends
**Timing Signal**

截至 2026-07-01，我会判断：**timing 是好的，但窗口不是“做 AI tutor”，而是“AI 让解释/答案泛滥之后，学习者开始意识到自己缺独立判断”。**

这对你的 hypothesis 是顺风：

> 用户不是没信息，而是看了很多解释、问了很多 AI，仍然在真实任务/变体/判断里失去方法。

**Early Indicators**

我看到的社区语言已经很贴近你的 problem：

|场域|用户语言|信号|
|---|---|---|
|r/learnprogramming|“I used AI a lot… now I feel like I know nothing”|AI 帮忙推进任务，但学习者感觉没有形成能力|
|r/learnprogramming|“I can’t code without AI”|典型的“看懂/通过考试/完成项目，但无法独立构造”|
|r/learnprogramming|“How do I make a project as a beginner… I don’t know where to begin”|从课程/解释到真实项目的断层|
|r/learnmath|“I don’t want resources that start by presenting definitions… I want to reconstruct how concepts were discovered”|几乎直接命中“结论式学习不够，要理解生成过程”|
|r/learnmath|“ChatGPT is frying my brain trying to explain it”|AI 解释多，但不一定产生理解|
|r/learnmachinelearning|“structure… before diving deeper into increasingly complex projects”|AI/ML 学习者在课程和项目之间找脚手架|

来源：公开 Reddit 页面 [r/learnprogramming](https://www.reddit.com/r/learnprogramming/)、[r/learnmath](https://www.reddit.com/r/learnmath/)、[r/learnmachinelearning](https://www.reddit.com/r/learnmachinelearning/)。

LinkedIn 我不建议现在当作硬证据，因为公开搜索不稳定。但可以持续监控这些关键词：`AI upskilling`, `AI literacy`, `hands-on AI training`, `learning by doing`, `AI skills gap`, `junior engineer AI`, `from tutorial to project`, `critical thinking with AI`。

**Analogous Markets**

1. **LeetCode**
    
    - Worked: 外部高压场景、明确反馈、可重复练习。
    - Didn’t: 容易训练成题型反应，不等于工程判断。
    - 启发：你的产品也需要明确 feedback loop，但不能变成题库。来源：[LeetCode](https://en.wikipedia.org/wiki/LeetCode)
2. **Kaggle**
    
    - Worked: 真实数据、排行榜、社区 notebook、立即反馈。
    - Didn’t: 竞赛环境和 production ML 有距离。
    - 启发：真实任务 + 可比较结果很强，但要防止 benchmark gaming。来源：[Kaggle](https://en.wikipedia.org/wiki/Kaggle)
3. **Coding bootcamps**
    
    - Worked: 把学习和就业结果绑定。
    - Didn’t: 当 entry-level hiring 变差、AI 改变初级岗位后，承诺开始崩。
    - 启发：如果你的价值挂在“就业/转岗”，要小心宏观招聘周期；如果挂在“判断力/能力形成”，要找到更直接的证明方式。来源：[Axios on bootcamp closure](https://www.axios.com/local/raleigh/2024/04/01/triangle-coding-bootcamp-momentum-closes-citing-ai)
4. **ChatGPT Study Mode / AI tutor**
    
    - Worked: 主流 AI 平台已承认“直接给答案会伤害学习”，开始加入 Socratic / step-by-step / self-reflection。
    - Didn’t: 用户可以绕过学习模式，且通用 tutor 很难稳定训练领域判断。
    - 启发：这既验证你的方向，也压缩你的差异空间。来源：[Axios on ChatGPT Study Mode](https://www.axios.com/2025/07/29/openai-chatgpt-study-mode)

**Three External Trends**

|Trend|Type|Tailwind / Headwind|Why It Matters|
|---|---|---|---|
|AI skills gap becomes board-level|Demographic / labor|**Tailwind**|WEF 2025 报告说 39% worker skill sets 到 2030 会变化，63% employers 认为 skill gaps 是业务转型最大障碍，85% 计划优先 upskilling。你的市场有预算和紧迫感。来源：[WEF Future of Jobs 2025](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/)|
|AI assistants commoditize explanation|Technological|**Mixed**|Stack Overflow 2025 显示 84% respondents 已使用或计划使用 AI tools，33.1% currently mostly use AI for learning new concepts，47.4% partially use AI for learning。但 46% distrust AI accuracy，复杂任务信任仍低。你的机会在“AI 解释之后的判断训练”，不是解释本身。来源：[Stack Overflow 2025 AI](https://survey.stackoverflow.co/2025/ai/)|
|AI governance pushes human oversight / AI literacy|Regulatory|**Tailwind for serious learning, headwind for school deployment**|EU AI Act 把 education 中部分 AI use cases 归入 high-risk 语境，强调 transparency、human oversight、quality obligations。若你卖给学校/企业，会增加合规成本；但也会提高“不能只会用 AI，要会判断 AI 输出”的需求。来源：[EU AI Act overview](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)|

**Bottom Line**

现在进入的理由不是“大家需要一个更好的学习软件”。这个太泛。

更准确的 timing thesis 是：

> AI 已经把解释和答案变得极度便宜，但也制造了新的焦虑：我是不是只是会问 AI、会跟上解释，却没有形成独立判断？这个焦虑正在程序员、AI 学习者、数学学习者、工程团队里变得可见。

所以未来 6-8 周最该验证的 early indicator 是：

> 用户是否会自发表达“AI/课程让我前进很快，但我没有真的会”的焦虑，并愿意为摆脱这种依赖付出时间或钱。


## Customer Discovery
### Who to talk to
**A. Result-Driven ICP**

他们的语言是：

> 我需要把这个东西做出来。  
> 我需要 debug。  
> 我需要复现 paper。  
> 我需要在工作里做判断。

优点：痛强、付费可能高、容易验证。  
风险：他们会把你推向 Copilot、debugger、project assistant、workflow tool。

|Priority|Profile|Job Titles|Company / Team|Why Pain Is Acute|
|---|---|---|---|---|
|P0|软件工程师转 AI builder|Founding AI Engineer, AI Product Engineer, Full-stack Engineer building AI features, Applied AI Engineer|Seed-Series A AI startup；2-8 人工程团队；没有成熟 ML mentor|必须边学边 ship。ChatGPT/课程能解释，但遇到 RAG、eval、agent reliability、model choice 时要自己判断|
|P1|非 AI 公司里的 AI 转型工程师|Senior SWE, Staff SWE, AI Platform Engineer, MLOps Engineer, Data Engineer moving into AI|中型 SaaS/企业内部平台；3-10 人 AI enablement / platform team|被公司要求“用 AI 提效/做 agent”，但团队缺判断结构和训练路径|
|P2|ML/AI 学习到复现阶段的人|Research Engineer, ML Engineer, MS/PhD student, independent AI researcher|实验室、开源项目、个人研究；经常读 paper / reproduce repo|最典型的“论文看懂了，但复现/改造/判断取舍时卡住”|
|P3|高阶技术课程 creator / instructor|AI course creator, bootcamp instructor, ML educator, developer educator|小型课程、cohort、训练营、技术社区|他们能观察很多学生卡在 guided exercise 到 independent project 的断层|

**Reachable Places**

|Segment|Where To Find Them|
|---|---|
|P0 AI builders|[AI Engineer](https://www.ai.engineer/) events/newsletter；Latent Space 读者；X/LinkedIn 上发 AI build log 的 founders；Hugging Face Spaces/GitHub repo contributors|
|P1 AI platform / MLOps|[MLOps Community](https://mlops.community/)；MLOps Slack/meetups；LinkedIn 搜 `AI Platform Engineer`, `MLOps Engineer`, `LLMOps`, `AI enablement`|
|P2 paper/reproduction learners|Hugging Face Discord；r/MachineLearning、r/learnmachinelearning、r/LocalLLaMA；Papers with Code repo contributors；NeurIPS/ICML workshop Discords|
|P3 educators|DeepLearning.AI forums；fast.ai forum；technical course creators on LinkedIn/X；cohort-based AI course communities|

有几个公开锚点说明这些地方不是虚的：MLOps Community 自称有 70k-90k AI/ML professionals，并有 events/workshops；AI Engineer 面向 AI engineers/founders/AI architects，2026 World’s Fair 标称 6,000+ AI engineers/founders/VPs of AI；Latent Space 有 189k+ subscribers。

**Prioritization Framework**

每个潜在人选打 0-2 分，总分 8+ 才优先约。

|Signal|0|1|2|
|---|---|---|---|
|Recent pain|没有最近学习场景|最近泛泛学过|过去 30 天具体卡在 AI/数学/系统主题|
|Real task pressure|只是兴趣|有目标但不急|正在项目/工作/复现中需要判断|
|Independence gap|只是看不懂|能看懂但还需更多解释|能看懂解释，但用不出/判断不了/复现不了|
|Workaround failure|没试过|只问过 AI/看课|已经问 AI、看课、读文档，仍卡住|
|Reachability|冷启动困难|可 LinkedIn DM|同社区/二度连接/公开发过相关困惑|
|Budget/influence|无付费能力|个人可付费|团队/课程/公司有预算或影响力|

**First 20 Outreach List Composition**

我会这样配：

- 8 个 P0：正在 build AI product 的工程师/technical founder；
- 5 个 P1：AI platform / MLOps / Staff SWE 转 AI；
- 4 个 P2：正在复现 paper 或做 ML systems 项目的人；
- 3 个 P3：AI/ML 技术课程 creator 或 instructor。

这样既能验证 user pain，也能看 buyer 路径。

**最优先的一句话筛选问题**

> 你最近有没有遇到过：材料/AI 解释你都能看懂，但一到自己实现、复现、改造、判断方案取舍时就卡住？

能立刻讲出具体案例的人，才是高优先级访谈对象。讲不出来的，先放后面。

**B. Understanding-Driven ICP**

他们的语言是：

> 我不满足于会用。  
> 我想知道为什么是这样。  
> 我想把这个东西想透。  
> 我想建立自己的判断结构。  
> 我不想只是跟着教程走。

优点：更贴近你的 learning field thesis。  
风险：痛不一定急，付费不一定强，可能更像 passion market。

|Priority|Profile|Why They May Care About Understanding|
|---|---|---|
|U0|高动机自学者，长期学数学/AI/CS 理论|他们学习不完全为了交付，而是为了理解本身；会反复遇到“看懂但没想透”|
|U1|研究生/准研究者/独立研究者|他们必须形成问题感和判断，不只是完成任务；理解质量直接影响研究能力|
|U2|技术写作者/课程作者/科普创作者|要给别人讲清楚，必须自己理解为什么；他们对“生成过程/取舍/反例”更敏感|
|U3|优秀工程师中的 principle seeker|不满足于调 API，想理解系统设计、架构取舍、抽象边界|
|U4|数学/理论型学习社区成员|他们天然 care proof intuition、definition motivation、conceptual understanding|
|U5|AI-native indie learners / builders with intellectual taste|既想做东西，也想理解底层；比纯工程交付者更接近你的动机|

我会把第一批访谈从 P0/P1/P2 改成混合：

- 40% understanding-driven：U0/U1/U2；
- 40% result-driven but reflective：P0/P2 里会写复盘、技术文章、paper notes 的人；
- 20% educators：能观察学生从“会跟”到“会想”的断层。

**Reachability**

理解驱动的人不一定在企业 LinkedIn 里最好找，反而在这些地方：

- Math/CS/AI 自学社区：r/learnmath, r/math, r/learnmachinelearning, r/MachineLearning, r/LocalLLaMA；
- 技术写作者圈：Substack、知乎、博客、X 上写 long-form technical notes 的人；
- paper reading / study group：Hugging Face Discord、MLOps Community、Latent Space、AI Engineer 社区；
- 高阶学习论坛：fast.ai forum、LessWrong/Alignment Forum、StackExchange Math/CS Theory；
- 创作者/课程作者：YouTube/Bilibili 技术讲解、DeepLearning.AI/fast.ai 周边社区。

**新的优先级判断**

不要问他是不是 AI engineer。问这几个信号：

1. 过去 30 天有没有主动学一个复杂主题？
2. 有没有花数小时以上，不只是查答案？
3. 有没有说过“我能看懂解释，但我没有真正想透”？
4. 有没有主动写过笔记、文章、推导、复现、讲解？
5. 有没有为了理解而做过非必要动作，比如找反例、追历史、比较方案、重写证明？
6. 有没有表达过对“教程化/答案化/AI 代劳”的不满？

如果 4-6 命中，才是理解驱动。

所以我会把 target profile 改成：

> 过去 30 天内，主动投入数小时学习 AI、数学、CS 理论或复杂工程系统，并且有明确“理解本身”动机的人。他们通常会写笔记、推导、技术文章、paper notes、复现记录或公开提问；他们不满足于完成任务，而想理解为什么这个方法成立、边界在哪里、如何迁移。

这个比 P0/P1/P2 更贴近你的 thesis。  
P0/P1/P2 可以作为商业化压力测试，但不应该作为唯一 ICP。

### What to ask
访谈目标只有一个：验证用户过去是否真的经历过这个 problem。

当前要验证的 problem：

> 学习复杂知识时，用户能看懂解释/复述概念，但在自己处理变体、形成判断、复现、解释取舍或迁移时没有方法。

**访谈对象分三类**

|Persona|要验证什么|
|---|---|
|U: Understanding-driven learner|是否真的为了理解本身投入时间，而不是只想完成任务|
|R: Reflective builder/researcher|在真实项目/复现中，是否出现“看懂但判断不了”的断层|
|E: Educator/creator|是否反复观察到学生从 guided learning 到 independent judgment 的断层|

**通用访谈框架**

开场：

> 我不是来推产品的，也没有 demo。只想了解你最近一次学习复杂主题的真实经历，尤其是你怎么判断自己有没有真的学会。

1. **筛选最近场景**
    
    - 过去 30 天，你有没有主动学过一个你觉得比较复杂的主题？
    - 那个主题是什么？
    - 你为什么要学它？
    - 你大概投入了多少时间？
    - 你用了哪些材料或工具？
2. **锁定具体事件**
    
    - 回想最近一次你觉得“我好像看懂了，但自己做/判断/迁移时卡住”的经历。发生在什么时候？
    - 当时你正在尝试做什么？
    - 你是怎么发现自己其实还没掌握的？
3. **追行为，不追观点**
    
    - 卡住之后，你第一步做了什么？
    - 你问了 AI 吗？怎么问的？
    - 你看了更多材料吗？看了哪些？
    - 你有没有做题、复现、写代码、推导、画图、写笔记、讲给别人听？
    - 哪个动作最有帮助？哪个动作基本没用？
4. **判断严重性**
    
    - 这个卡点耽误了你多久？
    - 它有没有让你放弃、推迟、重学或换资料？
    - 这是偶尔发生，还是你学复杂东西时经常发生？
    - 如果这个问题没解决，会有什么实际后果？
5. **判断 workaround 是否足够**
    
    - 你最后解决了吗？
    - 如果解决了，是靠什么解决的？
    - 如果没解决，现在停在哪一步？
    - 你觉得当时缺的是什么：更好的解释、更多例子、反馈、项目、老师、练习、还是别的？
6. **不要问未来购买，问过去付出**
    
    - 你过去有没有为类似学习问题付过钱？
    - 买过什么课程、书、会员、工具、cohort、导师？
    - 哪个最值？哪个最不值？为什么？

**Persona-Specific Questions**

U 类理解驱动学习者：

- 你怎么判断一个东西是“真的理解了”？
- 最近有没有一个主题，你明明没有外部压力，但还是想把它想透？
- 你有没有为了理解做过非必要动作，比如找反例、重写证明、追历史、比较不同解释？

R 类 builder/researcher：

- 最近一次你从论文/教程走到实现或复现时，哪里断了？
- 你当时缺的是代码细节、实验经验、设计判断，还是理论理解？
- 有没有一个地方你能复述原理，但不能决定怎么改方案？

E 类 educator/creator：

- 你最常看到学生在哪一步从“听懂”掉到“不会自己做”？
- 他们通常怎么补救？
- 你觉得普通课程/题目/AI 答疑最解决不了哪类卡点？

**要避免的问题**

这些问题会污染答案：

- “你会用一个帮助你试错总结的学习场吗？” 未来假设 + 暴露方案。
- “你是不是觉得现在学习缺少实践？” 引导。
- “你想不想更深入理解？” 社会期待答案，几乎人人会说想。
- “AI 是不是不能帮你真正理解？” 引导用户批评 AI。
- “如果有个工具能解决这个问题你愿意付费吗？” 低信号。

**最容易出现 deflection 的地方**

当用户说“我就是基础不够”时，追问：

> 你怎么判断是基础不够？当时具体缺哪块基础？你后来补了吗？补完之后问题消失了吗？

当用户说“我多问 AI 就好了”时，追问：

> 能不能打开或回忆一下你当时怎么问的？最后 AI 帮你推进到了哪一步？还有什么没解决？

当用户说“我看懂了但不会用”时，追问：

> 当时那个“不会用”具体表现是什么？是不知道第一步做什么，还是做了之后不知道对不对，还是遇到变体就失效？

**访谈后打分**

每个人按 0-2 分打：

- 最近 30 天有具体复杂学习场景；
- 明确出现“看懂但用不出/判断不了”；
- 尝试过多个 workaround；
- workaround 没有稳定解决；
- 问题反复发生；
- 曾为类似学习问题付出时间或金钱。

8 分以上是高信号用户。  
5-7 分是可继续观察。  
4 分以下不是早期 ICP。

最关键的一句访谈问题其实是：

> 你最近一次“看懂了解释，但自己处理变体/判断取舍/复现时没有方法”的具体经历是什么？

如果对方不能讲出具体故事，后面都不用深挖。