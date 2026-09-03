# lizheng-open-context：来源模型与主题路由

`lizheng-open-context` 在本知识库中不是“立正人格提示词”，也不是一批等待逐篇改写的摘要。它是一份版本化、可回查、带时间与权利字段的第一方证据底座；维护层只把其中能够跨查询复用的主题关系编译进现有 wiki。

## 本地快照与可验证事实

- 上游仓库：[sunyuzheng/lizheng-open-context](https://github.com/sunyuzheng/lizheng-open-context)
- 本地快照：`raw/external/lizheng-open-context-2026-08-30-6ed5fec/`
- 上游提交：`6ed5fec701095601e1348ac85bac8f11490aacaa`
- 内容快照日期：2026-08-30
- 本地发布校验：`scripts/validate_release.py` 通过，清单内 463 个文件的大小和哈希一致；上游 14 项单元测试通过

发布清单记录的覆盖范围是：

| 材料 | 覆盖 |
| --- | ---: |
| 立正本人社区帖子目录 / 全文 | 223 / 223 |
| 从本人评论中审核 / 纳入 | 2,519 / 10 |
| Knowledge Bank 目录 / 立正全文 | 169 / 35 |
| 视频目录 / 本人单独主讲字幕 | 536 / 201 |
| 视频仅元数据 | 335 |
| 已知嘉宾视频 | 242 |

这些数字描述 2026-08-30 的发布投影，不代表平台今天的实时数量。准确字段与哈希以本地 [release-manifest.json](../../../raw/external/lizheng-open-context-2026-08-30-6ed5fec/release-manifest.json) 为准。

## 权利不是一个仓库级开关

| 材料 | 默认权利范围 | 本库如何使用 |
| --- | --- | --- |
| 标有 `author: Yuzheng Sun` 与 `license: CC-BY-4.0` 的第一方内容 | CC BY 4.0 | 可归因地摘录、改写和综合，并保留标题、作者、日期与来源 |
| `catalog/` 中的规范化公开元数据 | CC0 1.0（在维护者有权授予的范围内） | 用于发现、去重和路由；元数据不等于正文 |
| `scripts/`、`tests/`、`docs/` 等代码与操作文档 | MIT | 可复用检索和校验工具 |
| 嘉宾、其他作者、第三方引文、链接后内容 | 未被重新授权 | 只把明确许可的元数据当发现入口，不复制或冒充立正观点 |

文件级声明优先；若文件级声明与总说明冲突，采用更窄的范围。完整边界见本地 [LICENSE-CONTENT.md](../../../raw/external/lizheng-open-context-2026-08-30-6ed5fec/LICENSE-CONTENT.md) 与 [privacy-and-rights.md](../../../raw/external/lizheng-open-context-2026-08-30-6ed5fec/docs/privacy-and-rights.md)。

## 与 2026-06-22 课程归档的分工

本库已有的 [Superlinear Academy 课程与洞见总索引](../ai-product-product-definition/superlinear-academy-course-insights-index.md) 对应一次登录态抓取，共 535 条原文记录：172 条 lesson、363 条 post。两批材料不是新版替代旧版，而是权利与查询用途不同的两种证据面。

| 维度 | 2026-06-22 课程归档 | lizheng-open-context |
| --- | --- | --- |
| 主要用途 | 课程结构、Deep News、Knowledge Bank 与多作者材料的连续检索 | 立正第一方表达、当前 thesis、视频时间码与公开复用 |
| 来源形态 | 登录态页面抓取，保存页面正文与课程空间 | 公开版本化发布，带 front matter、目录、筛选规则和哈希 |
| 作者范围 | 混合作者 | 第一方全文正向筛选；其他作者只留元数据 |
| 权利语义 | 保留来源归属，不由本库重新授权 | 文件级 CC BY / CC0 / MIT / metadata-only 明确分层 |
| 时间语义 | 抓取于 2026-06-22 | 同时保留 `published_at`、`updated_at` 与 `snapshot_at` |

按规范化原始 URL 精确比较，旧归档与新快照有 30 条第一方社区帖子 URL 重叠、162 条 Knowledge Bank URL 重叠；新快照另有 193 条第一方帖子 URL 不在旧归档中。这个数字只说明 URL 级覆盖，不证明语义独立，也不应把两个重叠数相加当成唯一文章数。

因此：

- 查询“立正何时、在什么来源说过什么”或需要公开复用时，默认从 `lizheng-open-context` 开始。
- 查询课程 lesson、Deep News、其他作者全文或 2026-06-22 当时的页面状态时，使用旧课程归档。
- 同一材料在两边都存在时，新快照负责作者、时间、权利和当前来源关系；旧归档可补课程位置与当时页面上下文，但不能覆盖更窄的权利声明。

一个具体例子是 [AI 鞭子：Accountability、AI 理解与 AI-native 团队](../human-ai-relationship/AI鞭子-accountability与AI-native团队.md)：新快照只把原文列为 Barytes 的 `metadata-only` 条目，本库旧归档保存了 Barytes 的页面正文。它可以与立正的 `fake work` 论点形成张力，但不能被归为立正原话。

## 默认来源优先级

| 优先级 | 来源 | 适合回答 | 不能自动推出 |
| ---: | --- | --- | --- |
| 1 | `context/core-thesis.md` | 2026-08-29 整理的当前稳定主张与概念关系 | 具体历史事实、今天仍未变化的实时状态 |
| 2 | 有日期的立正本人帖子，尤其 Knowledge Bank | 完整论证、历史变化、具体案例 | 一篇旧文就是永久立场 |
| 3 | 本库原书归档 + `zhenbenshi-frameworks.md` 与 reading map | 原书的强命题，以及作者在 2026-08-29 开放 V1 中的重述 | V1 自动覆盖原书，或原书自动代表今天的唯一措辞 |
| 4 | 本人单独主讲视频字幕 | 历史解释、案例与可定位时间码 | 自动字幕逐字无误 |
| 5 | 精选本人评论 | 对原帖的补充与边界 | 脱离对话语境后的完整理论 |
| 6 | 嘉宾视频与全量 Knowledge Bank 目录 | 发现其他人和延伸材料 | 元数据就是正文，或嘉宾观点代表立正 |
| 7 | `public-axioms-v1.md` | 选择检索方向和提出追问 | “立正人格定律”或普遍定律 |

优先级决定默认解释权，不取消任务匹配和时间。比如一篇 2026 年帖子可能比 2022 年视频更适合回答当前判断，但旧视频仍可能是观点变化的历史证据。

《真本事》需要额外保留版本差异。原书归档写有“个人价值 = 了解市场 + 打造产品 + 利用杠杆”“选择大于努力”“本职工作和副业的结合，才是破局之路”等强表述；2026 开放 V1 对其中一些命题使用了不同公式或增加了适用边界。查询原书时不得用 V1 无声降格，查询 V1 时也不得把原书措辞冒充成 2026 版本。维护页 [真本事：从会工作到会赚钱](../career-positioning-job-search/真本事-从会工作到会赚钱.md) 并置两层来源，不替作者裁决。

## 回答时保留四种证据状态

1. **直接来源**：某篇文章或视频明确表达过，给标题、日期、链接；视频尽量给时间码。
2. **跨来源综合**：多个来源共同支持、但没有单篇逐字说出，明确写“综合来看”。
3. **当前主张**：来自 2026-08-29 的 `core-thesis.md`，注明这是作者整理版而不是全部历史材料的替代品。
4. **本库推断**：为当前问题建立的关系或应用判断，允许读者看见它不是本人原话。

每个重要材料至少保留 `source`、`published_at` / `snapshot_at`、`author` 与 `rights_scope`。如果公开材料没有直接答案，应说“没有直接材料”，而不是写“立正一定会说”。上游发布帖本身还提醒：材料由 AI 整理，不能保证完整等同于本人思想；本库因此把它当有来源的公共材料，而不是数字分身。

## 主题路由

| 查询主题 | 先读维护页 | 再回查原始层 |
| --- | --- | --- |
| `做点真东西`、`MAKE WHAT LASTS`、代表作、authorship | [做点真东西：现实反馈、作品与作者责任](../learning-judgment-mental-models/做点真东西-现实反馈作品与作者责任.md) | `context/core-thesis.md`、Build in Public 原帖 |
| `fake work`、内部记分牌、先删除再自动化 | [fake work：从内部记分牌到真实结果](../career-positioning-job-search/fake-work-从内部记分牌到真实结果.md) | `20260828-fake-work-35921998.md` |
| 《真本事》、职业、市场、手艺、杠杆 | [真本事：从会工作到会赚钱](../career-positioning-job-search/真本事-从会工作到会赚钱.md) | 本库原书上下篇归档 + `context/zhenbenshi-frameworks.md` 与 reading map；按版本分别引用 |
| AI Native、结果确定性、agent 工作重构 | [AI 系统产品判断框架](../../frameworks/AI系统产品判断框架.md) | AI Native / organization / result-certainty 帖子与视频 |
| 课程、Deep News、其他作者 | [Superlinear Academy 课程与洞见总索引](../ai-product-product-definition/superlinear-academy-course-insights-index.md) | 2026-06-22 的 `pages.jsonl` |
| 来源治理、Agent / Skill 派生 | 本页 | `docs/source-model.md`、`docs/answering-contract.md`、`docs/build-your-own-agent.md` |

## 本地检索

优先使用快照自带的搜索脚本，它会返回标题、日期、原链接和命中片段；视频结果尽可能带时间码：

```bash
python3 raw/external/lizheng-open-context-2026-08-30-6ed5fec/scripts/search.py "fake work" --top 8
python3 raw/external/lizheng-open-context-2026-08-30-6ed5fec/scripts/search.py "如何建立信念" --type community
python3 raw/external/lizheng-open-context-2026-08-30-6ed5fec/scripts/search.py "Conviction" --type video
python3 raw/external/lizheng-open-context-2026-08-30-6ed5fec/scripts/search.py "context architecture" --type comment
```

检索命中只负责发现候选来源。写入维护页或形成重要回答前，仍要打开完整文件，检查作者、日期、上下文、更新状态与许可。

## 更新规则

- 上游有新版本时，新增带日期与提交号的快照，不覆盖本快照。
- 观点变化写成“当时判断 → 后来修正”，不无声平均。
- 原书强命题与后续开放 V1 分版本保留；本库可以增加应用边界，但必须标成综合或本库判断，不能伪装成作者降调。
- 主题页只吸收跨查询可复用的关系，不按帖子、视频或人物机械增殖页面。
- `raw/` 继续作为不可改写证据层；维护页是本库综合，可被修订，但要保留归因和不确定性。

## 原始入口

- [本地 README](../../../raw/external/lizheng-open-context-2026-08-30-6ed5fec/README.md)
- [来源模型](../../../raw/external/lizheng-open-context-2026-08-30-6ed5fec/docs/source-model.md)
- [回答协议](../../../raw/external/lizheng-open-context-2026-08-30-6ed5fec/docs/answering-contract.md)
- [隐私与权利](../../../raw/external/lizheng-open-context-2026-08-30-6ed5fec/docs/privacy-and-rights.md)
- [构建衍生 Agent](../../../raw/external/lizheng-open-context-2026-08-30-6ed5fec/docs/build-your-own-agent.md)
