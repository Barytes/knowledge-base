---
name: topic-deep-ingest
description: Deeply ingest a source material into this knowledge base by extracting every concrete topic, model, concept, checklist, named distinction, or recurring mechanism into its own linked Chinese wiki page, updating overview/index pages, and verifying GitHub Pages search coverage.
---

# Topic Deep Ingest

Use this skill when the user gives a book, paper, article, PDF, note collection, transcript, or other material and asks to build a complete topic-level wiki surface, not just a summary.

Read first:

- `AGENTS.md`
- `COMMUNICATION.md`
- `schemas/AGENTS.md`
- `schemas/ingest.md`
- `wiki/index.md`

Use `skills/kb-ops/` for repository maintenance rules and site regeneration.

Do not write to `notebook/`.

## Success Standard

The output is complete only when:

- each concrete topic in the material has either a dedicated page or an explicit mapping to an existing page
- broad chapters are not used as substitutes for concrete topics
- overview and index pages expose the topic set
- every new page links to related wiki pages and back to the material/index
- `wiki/site/` is regenerated
- search index checks prove representative keywords find the corresponding GitHub Pages HTML page

Concrete topic means a reusable model, mechanism, distinction, checklist item, named idea, practice, failure mode, or recurring claim. For example, `Latticework`, `Invert, Always Invert`, `安全边际`, `机会成本`, `Specific Knowledge`, and `幸福需要平静` are concrete topics. `判断力` or `投资智慧` alone are too broad.

## Workflow

### 1. Intake The Source

1. Identify the source path and source type.
2. If it is a PDF, extract text to `/private/tmp/` with a stable filename when useful.
3. Read the table of contents, headings, index, named lists, repeated terms, and chapter summaries.
4. Keep source evidence in `raw/` when it is repository material. Do not modify source PDFs.

Useful commands:

```bash
pdftotext -layout raw/external/source.pdf /private/tmp/source.txt
rg -n "keyword|model|checklist|chapter heading" /private/tmp/source.txt
```

### 2. Build A Candidate Topic Inventory

Create a working inventory before writing pages. Use three passes:

- Structure pass: chapters, sections, appendix titles, checklists, numbered lists, index entries.
- Concept pass: named models, repeated distinctions, memorable imperatives, mechanisms, failure modes, practices.
- Knowledge-base pass: `rg` existing `wiki/` pages for each candidate to decide whether to update or create.

For each candidate, record:

- topic title
- why it is concrete
- source evidence location
- target folder under `wiki/topics/`
- existing page or new page
- related pages to link

Do not collapse concrete subtopics into one broad page just because they share a theme.

### 3. Route Pages

Prefer existing topic directories under `wiki/topics/`. Create a new top-level topic only when no existing topic can honestly hold the material, and then update `wiki/topics/topics.json`.

Use these defaults:

- external knowledge, book concepts, research claims: `wiki/topics/<topic>/`
- personal recurring judgment patterns: `wiki/self/`
- reusable decision skeletons or query routers: `wiki/frameworks/`

Maintained wiki pages must default to Chinese. Keep original names for models, repos, commands, and technical terms when helpful.

### 4. Create The Navigation Surface First

For large materials, create or update:

- material overview page, such as `穷查理宝典.md`
- concrete topic index page, such as `穷查理宝典具体模型索引.md`
- cross-material map when comparing multiple sources, such as `纳瓦尔与穷查理主题地图.md`
- nearest topic `index.md`

The index page should distinguish:

- already covered topics
- existing pages reused
- topics still requiring pages

Before finishing, convert remaining "待建" items into either links or a clear residual gap.

### 5. Page Template

Each concrete topic page should include the parts that fit the topic:

```markdown
# 话题名

一句到两句说明它是什么，以及为什么值得单独成页。

## 核心含义

解释机制，不只复述原文。

## 要避免的误读

列出常见误解、失败模式、边界条件。

## 使用场景

说明它如何用于投资、职业、产品、研究、AI 系统、关系或知识库维护等真实问题。

## 与其他模型的关系

链接到 3-6 个相关页面，说明关系。

## 检查问题

给出 3-6 个可操作问题，帮助后续调用。

## 相关页面

- [相关页](相关页.md)
```

Do not paste long copyrighted passages. Paraphrase and cite local source paths in overview/index pages when needed.

### 6. Interlink Aggressively But Carefully

Every new page should link to:

- the material overview or topic index
- one or more broader theme pages
- sibling concrete topic pages
- cross-book or cross-domain parallels when useful

Update back-links from:

- material overview page
- concrete topic index page
- topic directory `index.md`
- cross-material map, if present
- `wiki/log.md`

### 7. Regenerate Site

After maintained wiki changes:

```bash
./skills/kb-ops/scripts/kb-ingest.sh site
```

Expect generated HTML and `search-index.json` churn. Do not touch `notebook/`.

### 8. Verify Coverage

Run the normal workflow checks:

```bash
python3 scripts/test_kb_workflow.py
git diff --check
```

Use the bundled audit helper for representative search terms:

```bash
python3 skills/topic-deep-ingest/scripts/topic_coverage_audit.py \
  --root wiki/topics/learning-judgment-mental-models \
  --terms /private/tmp/topic-terms.txt \
  --search-index wiki/site/search-index.json
```

The terms file is one keyword or page title per line. Include concrete names users are likely to search for.

For link checks on touched files, use a small Python script or the audit helper output rather than broad noisy scans when old unrelated broken links exist.

### 9. Final Report

Report compactly:

- source material processed
- number and type of pages created or updated
- site/search verification evidence
- known residual gaps, if any
- whether `notebook/` was left untouched
