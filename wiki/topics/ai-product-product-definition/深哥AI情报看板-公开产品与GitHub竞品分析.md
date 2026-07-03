# 深哥 AI 情报看板：公开产品与 GitHub 竞品分析

## 背景

这页单独分析公开产品和 GitHub 项目，用来证明另一个 claim：**市场上已经存在成规模的平台和开源替代品，AI 情报看板这个方向本身很拥挤。**

它和 [深哥 AI 情报看板：Superlinear 项目区竞品补充](深哥AI情报看板-Superlinear竞品补充.md) 的作用不同：

- Superlinear 项目区证明的是：AI builder 社区里会自然产生大量个人工具，`user-generated software` 是真实竞争层。
- 公开产品和 GitHub 项目证明的是：市场上已经有大规模商业产品、平台入口和高热度开源项目，深哥看板如果只做信息聚合、AI 摘要和 dashboard，会直接落入拥挤赛道。

## 公开产品竞品分析

排序口径：公开产品很难拿到严格市场份额，所以这里按公开可见的规模信号排序，包括官方声称用户数、读者数、生态影响、是否拥有趋势/排行榜/新闻入口。相似度是相对深哥当前定义的看板产品：`AI/Tech 行业信号源 + 新闻/项目/公司/技术变化 + 趋势/动量/榜单 + 简要分析/筛选 + 看板或日报形态`。AI 工具目录只覆盖“发现工具”这一小段需求，不应放在直接竞争者里。

### 直接竞争者

深哥看板的真实需求是“持续知道 AI 行业发生了什么、什么值得关注、哪些信号在变强”。所以直接竞争者应收窄到两类：AI 新闻/资讯雷达，以及行业趋势/媒体情报雷达。AI 工具发现平台只在“新工具发现”局部重合，降为间接竞争者。

| 排名 | 产品 | 热门/规模信号 | 相似度 | 竞争含义 |
| --- | --- | --- | --- | --- |
| 1 | [The Rundown AI](https://www.therundown.ai/) | 首页称 `2,000,000+ readers`，定位是每天 5 分钟了解最新 AI news、why it matters、how to apply it。 | 88% | AI 新闻/资讯雷达型直接竞品。它不是 dashboard，但在“每天帮用户知道 AI 行业发生了什么”这件事上极强，直接抢走轻量情报消费需求。 |
| 2 | [Superhuman AI](https://www.superhuman.ai/) | 首页称 `#1 AI & Tech Newsletter`，并称有 `1,500,000+ professionals`。 | 86% | AI 新闻/趋势 newsletter 竞品。它把 AI news、tech news、tools 打包成 3 分钟日报，和深哥看板的日报/摘要形态高度重合。 |
| 3 | [TLDR AI](https://tldr.tech/ai) | 页面称 `1,100,000 readers`，覆盖 AI news、research、tools，每个工作日发送。 | 85% | 更偏工程师和研究人员的 AI 新闻雷达。它说明“高信噪 AI 行业摘要”已经有成熟订阅入口。 |
| 4 | [ReadPartner](https://readpartner.com/) | 首页定位为一个 dashboard，用于 monitor news、track sentiment、uncover emerging trends，并称 `10,000+ leading professionals` 使用。 | 80% | 行业新闻/媒体情报雷达型竞品。它不是 AI 垂直，但在“监控媒体、发现趋势、生成 briefing、支持团队决策”上与深哥看板的高阶形态非常接近。 |
| 5 | [Feedly](https://feedly.com/) | 作为 news reader 有长期用户基础；当前企业页强调 AI threat intelligence、10,000+ trusted sources、real-time threat graph、Ask AI 和 briefing/report 交付。 | 80% | 行业情报雷达型竞品。它不是 AI 行业看板，但“可信源聚合 + AI 抽取 + 图谱 + briefing”的机制非常接近深哥看板可能演化出的形态。 |

### 间接竞争者

这些产品不完全是深哥看板，但会从相邻方向吃掉用户需求：产品发现、模型/论文趋势、通用趋势发现、企业市场情报、AI 搜索、AI 工具发现。AI 工具发现平台虽然用户规模大，但只覆盖“找工具”需求，不覆盖新闻连续追踪、行业判断、趋势复盘和异常信号，所以在本页降权处理。

| 排名 | 产品 | 热门/规模信号 | 相似度 | 竞争含义 |
| --- | --- | --- | --- | --- |
| 1 | [Product Hunt](https://www.producthunt.com/) | 主站定位是 `launch and discover new tech products`，有每日、昨日、周、月榜单和 AI 类别；也是深哥原型想抓取的核心公开信号源之一。 | 75% | 不是 AI 专用，也没有深度 AI 解读，但它拥有产品发布社区和 upvote 信号。深哥看板更像是在 Product Hunt 等源之上做 AI 行业二次筛选。 |
| 2 | [Hugging Face Models / Daily Papers / Spaces](https://huggingface.co/) | Models 页显示约 `2,874,961` models；Daily Papers 支持 daily/weekly/monthly；Spaces 自称 `The AI App Directory`，并按 trending 展示。 | 74% | 对 AI 技术/模型/应用趋势的信号非常强。它不是市场看板，但如果用户关心 AI 技术前沿，Hugging Face 本身就是高频入口。 |
| 3 | [Exploding Topics](https://explodingtopics.com/) | 官方称监控 millions of unstructured data points，提前发现趋势；有 1.1M+ 用户、1.1M+ trends database、Trending Startups、Top Websites、Trend API。 | 70% | 不是 AI 垂直，但在“早期趋势发现、增长曲线、趋势 API、startup radar”上能力更成熟。深哥看板如果强调 trend / momentum，会自然被拿来比较。 |
| 4 | [Glimpse](https://meetglimpse.com/) | 定位为发现早期趋势；称分析 hundreds of millions of consumer behavior signals，Chrome extension 有 `170,000+ users`，覆盖 Technology / AI 等分类。 | 68% | 更偏消费趋势和搜索数据，不是 AI 行业新闻。但它代表另一种趋势雷达：用搜索和跨平台行为信号发现上升趋势。 |
| 5 | [AlphaSense](https://www.alphasense.com/) | 企业级 AI market research / market intelligence 平台；WSJ 报道其 2026 年融资后估值约 `$7.5B`，ARR 超 `$600M`。 | 65% | 面向企业、金融和战略研究，不是公开 AI 行业轻量看板。但它代表“高信任市场情报”的上限：专有内容、财报、专家访谈、可追溯研究流。 |
| 6 | [CB Insights](https://www.cbinsights.com/) / [Crunchbase](https://www.crunchbase.com/) | 私营公司、融资、投资人和市场研究数据库；更偏公司与资本市场 intelligence。 | 60% | 如果深哥看板加入融资、公司、投资事件、创业机会评分，就会接近这些市场情报产品。但它们不是 AI 行业普通用户的轻量看板。 |
| 7 | [There's An AI For That](https://theresanaiforthat.com/) / [Toolify](https://www.toolify.ai/) / [Futurepedia](https://www.futurepedia.io/) / [AI 工具集](https://ai-bot.cn/) | 这些平台有很大的目录、榜单或用户规模，其中 TAAFT、Toolify、Futurepedia 是全球性 AI 工具发现入口，AI 工具集是中文入口。 | 55% | 降权为间接竞品：它们能证明“找 AI 工具”已经非常拥挤，但深哥看板若定位为新闻、趋势和机会判断，就不应被它们定义产品边界。 |
| 8 | [FutureTools](https://futuretools.io/) | 产品形态包含 AI Tool Database、AI News、newsletter、submit a tool。 | 55% | 比纯工具目录更接近一点，因为有 AI News；但主体仍是工具库和轻资讯，不应作为核心直接竞品。 |
| 9 | Perplexity / 秘塔 AI 搜索 / 纳米 AI 搜索 | AI search 能把“今天某领域发生了什么”变成即时问答。 | 55% | 它们不是固定看板，但会吞掉临时查询需求。深哥看板必须证明“持续追踪 + 历史信号 + 异常变化”比一次性搜索更有价值。 |

## GitHub 项目竞品分析

排序口径：GitHub 直接竞争者按 stars 从高到低排列，数据截至 2026-07-02 的 GitHub API 查询。这里区分两类：直接竞争者是已经做成“新闻/趋势/AI 行业雷达/看板/日报”的项目；间接竞争者按相关性优先、stars 作为辅助参考。AI 工具目录类项目在间接竞品里降权。

### 直接竞争者

| 排名 | GitHub 项目 | Stars / Forks | 相似度 | 竞争含义 |
| --- | --- | --- | --- | --- |
| 1 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | `7761 / 1109` | 92% | 最重要的开源直接竞品。README 定位就是 `AI-powered news radar`，可追踪 Hacker News、Reddit、Telegram、RSS、GitHub、OpenBB，并做去重、评分、过滤、背景补充、邮件/飞书投递。 |
| 2 | [finaldie/auto-news](https://github.com/finaldie/auto-news) | `892 / 111` | 84% | 个人信息聚合 + LLM 洞察 + Notion/移动端/自托管。它不是 AI 行业专用，但强在个人信息流、噪声过滤、recap、action extraction。 |
| 3 | [SuYxh/ai-news-aggregator](https://github.com/SuYxh/ai-news-aggregator) | `285 / 56` | 94% | 直接 AI 行业资讯聚合：14 个专业平台、70+ RSS、52 个微信公众号、每 2 小时更新、双语标题、React 可视化、结构化 JSON。 |
| 4 | [Jackychen-12/AI-Search](https://github.com/Jackychen-12/AI-Search) | `109 / 0` | 94% | 零服务器、零数据库、GitHub Actions + Pages 的 AI 行业资讯站。包括 AI 解读、每日精选、周报、趋势图、话题聚合、时间线、个性化、本地收藏、开放 API。 |
| 5 | [hoodini/yuv-ai-trends](https://github.com/hoodini/yuv-ai-trends) | `101 / 19` | 88% | 面向开发者的 GenAI / ML news aggregator，强在 AI trends 内容流和 UI。规模不大，但形态非常近。 |
| 6 | [youzhenxing/info_hub](https://github.com/youzhenxing/info_hub) | `25 / 2` | 86% | 抓 podcast、Hacker News、GitHub Trend、Reddit、Product Hunt、公众号，并用 AI 做信息提取。和深哥原型的数据源重合度高。 |
| 7 | [YanCheng-go/my-focal-ai](https://github.com/YanCheng-go/my-focal-ai) | `11 / 0` | 90% | 个人 news intelligence：聚合 curated AI content，用 LLM 打分，再提供自己的 dashboard。虽然星少，但概念高度相似。 |
| 8 | [kkkano/tech-digest-daily](https://github.com/kkkano/tech-digest-daily) | `8 / 3` | 91% | 自动推送 GitHub Trending、Hacker News、Product Hunt、Dev.to，AI 总结和个性化推荐。低星但与“技术趋势日报”高度同构。 |
| 9 | [dongzhang84/trend-monitor](https://github.com/dongzhang84/trend-monitor) | `6 / 5` | 98% | 和深哥看板几乎同构：监控 Product Hunt、Toolify、There's An AI For That、Chrome Extensions、GitHub、Hacker News，生成邮件和 GitHub Pages dashboard，并对 solo-builder opportunity 打分。 |

### 间接竞争者

| 排名 | GitHub 项目 | Stars / Forks | 相似度 | 竞争含义 |
| --- | --- | --- | --- | --- |
| 1 | [karakanb/devo](https://github.com/karakanb/devo) | `432 / 51` | 68% | 浏览器新标签页展示 GitHub Trending、Hacker News、Product Hunt、Designer News。没有 AI 分析，但抓取源与深哥看板高度重合。 |
| 2 | [Mayandev/hacker-feeds-cli](https://github.com/Mayandev/hacker-feeds-cli) | `161 / 5` | 64% | CLI 聚合 Hacker News、Product Hunt、GitHub Trending、Reddit、V2EX。属于信息源聚合层竞品。 |
| 3 | [marc-shade/world-intel-mcp](https://github.com/marc-shade/world-intel-mcp) | `36 / 13` | 62% | 100+ tool MCP server，覆盖 markets、FX、bonds、earnings、SEC filings、conflict、military、cyber、climate、news、company enrichment。不是前端看板，但可成为情报 agent 的底层工具。 |
| 4 | [zakirkun/blossom-terminal](https://github.com/zakirkun/blossom-terminal) | `17 / 9` | 61% | Bloomberg-style global intelligence dashboard，聚合全球新闻、金融市场、天气和 AI 地缘分析。不是 AI 行业垂直，但接近“个人情报终端”。 |
| 5 | [best-of-ai/ai-directories](https://github.com/best-of-ai/ai-directories) | `841 / 434` | 45% | 降权为弱间接竞品：它不是看板，而是“AI 目录的目录”。它只能证明 AI 工具导航拥挤，不能证明新闻/趋势判断产品没有空间。 |
| 6 | [someu/aigotools](https://github.com/someu/aigotools) | `656 / 120` | 45% | 降权为弱间接竞品：它是快速创建网站目录的生产工具，说明 AI 工具目录可以被大量生成，但不直接覆盖行业雷达需求。 |

## 竞品 landscape 的结论

如果按市场和热度排序，深哥看板真正要面对四层竞争：

1. **AI 新闻 / 资讯雷达**：The Rundown AI、Superhuman AI、TLDR AI。这层吃掉“每天知道 AI 行业发生了什么”的轻量需求。
2. **行业趋势 / 媒体情报雷达**：ReadPartner、Feedly、Exploding Topics、Glimpse。这层不一定 AI 垂直，但已经把新闻监控、趋势发现、briefing、图谱、告警和行业决策做成成熟形态。
3. **产品/技术生态源头**：Product Hunt、Hugging Face、GitHub Trending、Hacker News。这层提供原始信号，本身也是用户直接访问的入口。
4. **开源个人新闻雷达**：Horizon、auto-news、AI Search、ai-news-aggregator、trend-monitor。这层证明“个人化抓取 + AI 总结 + dashboard / newsletter”已经可以被开源项目覆盖。
5. **企业级市场情报平台**：AlphaSense、CB Insights、Crunchbase。这层不直接抢早期轻量用户，但定义了高价值情报产品的上限：可信数据、可追溯来源、公司/融资/市场结构数据。
6. **弱间接的 AI 工具发现平台**：There's An AI For That、Toolify、Futurepedia、AI 工具集。这层只能说明“找工具/看工具榜”拥挤，不应主导深哥看板的产品定义。

因此，深哥看板不能把壁垒放在“抓更多源、总结更好、界面更像 dashboard”。更稳的差异化应该是：

- 围绕一个明确使用者：我们自己如何判断 AI 行业机会。
- 围绕一个明确对象：项目、公司、技术方向、投资事件或异常信号。
- 保留来源链、时间线、重复信号、反常变化和被忽视的弱信号。
- 做“判断复盘”：上周看好的项目后来怎样了、哪些信号被证伪、哪些来源更可靠。
- 把用户当前关心的问题作为筛选器，而不是做通用 AI 工具导航。

## 相关页面

- [深哥 AI 情报看板：Superlinear 项目区竞品补充](深哥AI情报看板-Superlinear竞品补充.md)
- [AI 产品反向筛选经验：避免 wrapper 与 slop](AI产品反向筛选经验-避免wrapper与slop.md)
- [Dogfooding 作为产品验证机制](Dogfooding作为产品验证机制.md)
