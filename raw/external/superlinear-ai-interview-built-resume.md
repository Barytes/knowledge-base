---
title: "别用昨天的方法准备今天的面试：AI 时代最好的简历，是做出来的"
source: "https://www.superlinear.academy/c/posts/interview"
author:
published:
created: 2026-06-28
description: "刚才在群里看到课代表分享了一篇 Jobright CTO 的采访，其中有句话让我很有感触：现在很多学生准备 AI 的方向其实有问题。Jobright 每天看大量求职数据，得出的结论是 95% 以上的学生其实没有认真对待找工作这件事，甚至连一个像样的 GitHub 和 AI 项目都没有。但有正确方法并认真去做的人，还是很容易 stand out。巧的是，我刚结束今年暑期实习招聘的终面。过去一个多月面了 26 位硕士和本科生，覆盖算法、开发、数据科学几个方向。面完之后最大的感受，和 Jobright..."
tags:
  - "clippings"
---
刚才在群里看到课代表分享了一篇 Jobright CTO 的采访，其中有句话让我很有感触：现在很多学生准备 AI 的方向其实有问题。Jobright 每天看大量求职数据，得出的结论是 95% 以上的学生其实没有认真对待找工作这件事，甚至连一个像样的 GitHub 和 AI 项目都没有。但有正确方法并认真去做的人，还是很容易 stand out。

巧的是，我刚结束今年暑期实习招聘的终面。过去一个多月面了 26 位硕士和本科生，覆盖算法、开发、数据科学几个方向。面完之后最大的感受，和 Jobright CTO 说的几乎一模一样：不是学生能力不行，而是大多数人还在用五年前的方式来准备一场 2026 年的面试。

## "说"正在贬值

我先说一个底层逻辑，理解了这个，后面的东西自然就通了。

AI 之前，校招的筛选机制是这样的：学生拿着简历，聊 30 分钟到一个小时。简历里的硬通货（学校、GPA、实习、论文、竞赛）提供背书，面试中看逻辑表达、专业深度和沟通能力。这套机制运转了十几年，大家都习惯了。

但 AI 时代这套机制正在失效。原因很简单：当 AI 能帮任何人生成一份漂亮的简历、写出看起来很专业的项目描述、甚至在面试中提供实时辅助的时候，"说"本身的可信度在急剧下降。

我面试中碰到一个真实的情况。有位同学简历上写了"AI Code Review 系统"，看上去很前沿。面试一追问，发现本质就是在 Cursor 里写了一个提示词，手动把代码贴进去跑一遍，再把结果复制给同事。他不是在骗人，但简历上那个词和实际做的事情之间的落差，在 AI 时代会被无限放大。

所以企业现在越来越看重一件事： **你能不能"show me"，而不只是"tell me"。**

丢一个 GitHub 链接，代码质量、项目结构、迭代历史一目了然。打开你的 [CLAUDE.md](http://claude.md/) 文件，面试官立刻知道你和 AI 的协作到了什么程度。给面试官看一个你完整交付的东西，胜过你讲十分钟项目经历。

这不是面试官故意刁难。是因为在一个 AI 能帮你"说"的时代，只有"做出来的东西"才是不可伪造的信号。

## 面试官真正在看什么

再说一个视角。

现在校招面试一般分两轮。技术初面由团队骨干主持，考的是专业基本功，在细节层面看你是否合格。通过初面之后，终面由更高层级的面试官来做，这一轮基本不再考技术细节了。

为什么？一方面到了这个层级，面试官对具体技术细节的把控不一定比一线同事精准；另一方面，终面要判断的东西不一样——潜力、思维方式、成长性，这些更难量化的东西才是终面决定录不录你的核心。

以前这些东西靠经验和直觉判断。但现在面试官也有了AI，他们期待使用更好的方式以便更好的了解你：如果你有一个 GitHub 仓库、有一个完整的项目、有你自己的 AI 工作流配置文件，终面面试官可以在面试前就借助 AI 对你的项目做深度观测。你的代码组织方式、你的设计决策、你和 AI 的协作模式、你在项目中遇到问题时怎么解决的，这些信息全在那里。

一场面试，上下文浓度天差地别。这比你在面试中口头回答三个问题，信息密度高出一个量级。

**所以 AI 改变了两件事：一是"说"在贬值，二是"做出来的东西"可以被更高效地读取和评估。** 两头一挤，结论就很清楚了——有作品的人会越来越占优势。

## 我实际看到了什么

说回这 26 个人。我在面试中有一个习惯：直接让候选人打开他们的 [CLAUDE.md](http://claude.md/) 或 [agents.md](http://agents.md/) 文件给我看。

结果是大部分人愣住了。26 个人里只有 2 个有成熟的 AI 工作流。不到 8%。

剩下的人大致这几种情况。

**把 AI 当搜索引擎用。** 占了至少三分之一。我问"你平常用 AI 吗？"都说用。怎么用？打开浏览器问 ChatGPT 一个问题，看回答。有位同学很坦诚，我说"就把它当成高级版搜索"，她直接说"对，是的"。当整个行业已经从对话式交互迁移到 IDE 类工具的时候，这些同学还在浏览器里一问一答。

**研究 AI 但不用 AI。** 这个反差最让我意外。有位做大模型微调的同学，自己写代码只用豆包当搜索。有位本硕都读 AI 专业的，从没用过 Cursor。能把 PPO、DPO、GRPO 三种对齐算法讲得头头是道，但可能从没让 AI 帮自己完整做成过一件事。造工具和用工具，是两回事。

**用了很多工具但没有方法论。** 有位同学付费用了 GPT 和 Trae，使用频率很高。但当我问"你有 [agents.md](http://agents.md/) 吗？"他不知道。问他怎么约束 AI 不重复犯错，他说写了个文件，让他给我看，他说好像在实验室电脑上。这意味着 AI 每次都不知道他在做什么项目，相当于永远带着一个失忆的人一起工作。

让我眼前一亮的那 2 个人，共同特征是：问他们 AI 的问题，不像在回答面试题，而是在聊他们每天都在做的事。一个人业余时间自己搭了选股 Agent，写 skills 并持续迭代，出发点是真实需求。另一个在微软有无限 Copilot 额度，但选了 Claude Code 做主力，能说清为什么。

## 使用 AI 是动词，不是名词

这个社区一直在说的一个观点，我觉得特别到位：使用 AI 是一个"动词"，不是一个"名词"。

很多学生把"了解 AI"当标签。看了几篇文章、知道一些概念，觉得自己"会 AI"了。但 AI 的真正价值只有在动手的过程中才能体会。什么时候该信任它的输出，什么时候该打断它；怎么给 AI 足够的上下文让它做对事情；碰到它反复犯同一个错误该怎么约束它。这些东西看文章看不出来。

面试中有位同学让我印象深。他能引用 Anthropic CEO 的话，用比喻描述 AI 对工作方式的变革，讲得很有见地。但当我追问他自己的 AI 工作流是什么，他答不出来。认知超前但行动为零，这是我看到的最典型的错位。

在过去，企业希望学生除了上课和写论文，还能有实习和项目经历。实习经历意味着实践，现在在绝大多数企业都希望寻找到那些有 AI 属性的毕业生时，AI 时代的实践是什么？我想，跟过去的实习经验，又不同了。现在对实践的要求非常直白：你在 AI 上有没有动手能力。为什么会要求动手能力，是因为面试你的那群人，也都每天在承受被 AI 变化驱动带来的震撼或者焦虑，他们很清楚，AI 每天都在变化，应对这种变化，或者说，在这种变化中，与企业的业务做好结合的前提，就是 AI 体感。而这种体感只能从使用中获得，和所有快速变化的领域逻辑一样——光看方向盘说明书不行，你得真开过车。

## 具体怎么做

如果你正在准备找工作或者找实习，以下几件事我觉得值得好好考虑一下。

从今天开始， **用 AI 去做一件完整的事** 。什么事都行：一个小工具、一个自动化脚本、一个数据分析流水线。过程中你自然会碰到怎么选工具、怎么配上下文、怎么约束 AI 的问题，这些问题会逼你建立自己的方法论。

做完之后，你会有一个 GitHub 仓库，里面有你的代码、你的 [CLAUDE.md](http://claude.md/) 、可能还有几个你写的 skills。这些东西加在一起，就是你在这个时代最有说服力的能力证明。面试时打开给面试官看，比任何话术都管用。

如果你还有余力，把你做的东西、学到的东西分享出来。技术博客、小红书笔记、LinkedIn 上一段项目总结，什么形式都行。这些公开可见的内容就是"signal"——它传递的不是"我有多厉害"，而是"我知道什么是真正有价值的"。

GitHub、真实项目、技术博客、有干货的社交媒体 profile——把这几个装点齐全，三个月足够了。

## 写在最后

说这些不是为了制造焦虑。从我面试的情况看，绝大多数人还没有开始。你花两三周时间认真做一个东西出来，就已经站在前 5% 的位置了。

我自己在 AI 这条路上受益于课代表与鸭哥社区的课程和氛围。Architect 课程帮我建立了对 AI 架构和工作流的系统认知，社区里大家分享的实践让我少走了很多弯路。其实社区里面免费的文章就很多，除了免费文章外，有条件的同学如果有机会去看看系列课程，然后跟着做完一个项目，我想你能感受到不同，并且这种不同也能传递到你的面试官。如果条件不允许，我也建议从今天开始，把"名词"变为"动词"。因为我面试的过程中我都在想这个事情，如果这些学生，哪怕就上一周的课，哪怕有一点点"做出来的东西"，他们都会因为这种不对称优势，而迅速排到前列，而那恰恰是面试官最想看到的。

---

*Challen / 2026年5月*

Conversation summary

评论区围绕AI时代求职准备的转变展开讨论，强调了从认知到行动的重要性。大家普遍认同传统的准备方式已不适用，呼吁通过实际动手做项目来提升竞争力，并指出无论是学生还是资深开发者，都存在对AI应用的浅尝辄止。社区和课程被视为帮助转变思维和实践的有效途径。

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCSlZ6dGdrPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b901789bb65f42f263e9f9447accf1c2c5046a4e/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJc0FXa0NMQUU2Q25OaGRtVnlld1k2Q25OMGNtbHdWQT09IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--67365f61f655fbc86c65a51f2e9992ab818c41cd/lnlDLQ6DYGcX3K_na37rVk6QSEYi.jpg)](https://www.superlinear.academy/u/7273d669)

真的受益匪浅，作为一名身在高校的老师，自身也会不同程度的焦虑，这也是为什么不断在泡在社区学习和交流的原因，不仅仅是因为自己努力从user（花了很多钱成为多个产品的使用者）向builder的转变，且看到学校《ai通识教育》等很多课程都大谈AI，都说要融入AI和智能体最后发现就是发现把自己传统的专业跳入宏达的叙事中自保，思维惯性稳定且有效。国内高校本来就在高墙之中，“认知超前但行动为零”的错位无处不在。最后不断提醒自己行动胜过思考，思考胜过求知。

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRTJDRFFvPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--31e46f09f94cc8365b57a8acdc9e0911e0df104a/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJc0FXa0NMQUU2Q25OaGRtVnlld1k2Q25OMGNtbHdWQT09IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--86d5a93b1fb9d9a40ce4e61c041294c46ab790a5/sampotrait2.png)](https://www.superlinear.academy/u/4fc3571c)

目前求职中，感谢课代表的引路和老王老师的总结，庆幸1更加坚定目前学习的方向，成为builder的目标 2.老王老师的总结很清晰，让我准备的重点更清晰

不只是学生。我在一个项目组里，大家全都是资深开发，绝大部分代码都是AI产出的，但是长期维护AGENTS.md的人寥寥无几，更别说去沉淀自己的skills，或者研究如何把代码库做的更加agent friendly。大部分人对AI的运用太浅了

谢谢您的慷慨分享，我的体感也是这样，虽然大家都在说拥抱AI，但是经过我的闲聊发现真正动手去用AI的人寥寥无几，可能和我们行业特性有关。对于我自己而言，几年前在线下参加活动时，有腾讯的事业部经理结束后投来橄榄枝，但是我因为内心对996和技术更迭速度的concern拒绝了，现在上过课代表的课，有意识在培养自己builder mindset，我也在自学build开发自己的备婚dashboard，虽然总是报错，但我很喜欢这个做的过程，慢慢走起来总比一直在岸边观察来的好

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCTVNBTXdnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--4cdb078a6803ddf96a1c9fc02fe3d083d6ff8a62/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJc0FXa0NMQUU2Q25OaGRtVnlld1k2Q25OMGNtbHdWQT09IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--67365f61f655fbc86c65a51f2e9992ab818c41cd/%E5%A4%B4%E5%83%8F.jpg)](https://www.superlinear.academy/u/452cd000)

太棒了！感谢老王的分享！要知道，终面送到你面前，已经是几百个学生筛选出来的精英了，结果还是这样。“正确的路径”真的是当下很大的套利机会。  
  
可惜我们在跟学生讲这些道理的时候，学生们普遍反映是不想听的，觉得跟自己无关。觉得自己刷刷GPA，海投一下简历，就很努力了。其实无效的努力，还不如去好好玩。真是让人很痛心了。

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCTTRVMUFRPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--faa39cd74c55fe7dfda3df6745a7689b3087c6a3/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJc0FXa0NMQUU2Q25OaGRtVnlld1k2Q25OMGNtbHdWQT09IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--86d5a93b1fb9d9a40ce4e61c041294c46ab790a5/ChatGPT%20Image%202025%E5%B9%B44%E6%9C%881%E6%97%A5%2018_24_56.png)](https://www.superlinear.academy/u/7b136502)

立正 说的是啊，对学生来说，那一套也是思维惯性，并且可能绝大多数的学校，可能也依然在延续之前的就业辅导。这时候出来跟学生讲这些道理，学生可能觉得是江湖骗子。

感觉把那种“认知和行动的落差”说透了。读完后最大的感触是，与其一直盯着 AI 的宏大趋势看，不如像文中说的那样找个切入点先动起来。虽然已经不是学校学生好多年，但是这个理念同样适用AI时代下的大多数人。这个方向挺有启发，值得试试看

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCTTRVMUFRPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--faa39cd74c55fe7dfda3df6745a7689b3087c6a3/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJc0FXa0NMQUU2Q25OaGRtVnlld1k2Q25OMGNtbHdWQT09IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--86d5a93b1fb9d9a40ce4e61c041294c46ab790a5/ChatGPT%20Image%202025%E5%B9%B44%E6%9C%881%E6%97%A5%2018_24_56.png)](https://www.superlinear.academy/u/7b136502)

Jiamin Yan 试试看！