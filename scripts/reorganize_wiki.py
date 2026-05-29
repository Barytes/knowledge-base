#!/usr/bin/env python3
"""Reorganize wiki pages into topic directories and build a static site."""

from __future__ import annotations

import html
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
TOPICS_DIR = WIKI / "topics"
SITE_DIR = WIKI / "site"


@dataclass(frozen=True)
class Topic:
    slug: str
    title: str
    summary: str
    frameworks: tuple[str, ...] = ()
    self_pages: tuple[str, ...] = ()


TOPICS: tuple[Topic, ...] = (
    Topic(
        "agent-harness-runtime",
        "Agent / Harness / Runtime",
        "围绕 agent 外层控制壳、运行时、coding harness、多设备工作面与可验证执行系统的页面。",
        ("Harness架构判断框架.md", "AI系统产品判断框架.md"),
    ),
    Topic(
        "context-memory-knowledge-system",
        "Context / Memory / 知识系统",
        "围绕 context、memory、本地知识库、信息复利、AI 知识系统与 context infra 的页面。",
        ("知识系统判断框架.md", "Harness架构判断框架.md"),
        ("工作面摩擦敏感观察.md", "研究知识系统中的反共识写回观察.md"),
    ),
    Topic(
        "ai-product-product-definition",
        "AI 产品 / 产品定义 / 验证",
        "围绕 AI 产品分层、AI Architect、产品定义、MVP、Pre-PMF 与 go-to-market 的页面。",
        ("AI系统产品判断框架.md", "产品定义判断框架.md", "产品验证判断框架.md"),
        ("开箱即用洞察优先产品观察.md", "用户自主性优先产品取舍观察.md", "聚焦优先于通用观察.md"),
    ),
    Topic(
        "research-knowledge-governance",
        "研究知识库 / 公共知识治理",
        "围绕课题组公共知识库、多人知识治理、共享 AI Skills、公共层边界与研究判断基础设施的页面。",
        ("研究判断框架.md", "知识系统判断框架.md"),
        ("公共知识库实践启发他人写作观察.md", "知识库公开分享的阻力降低观察.md"),
    ),
    Topic(
        "career-positioning-job-search",
        "职业 / 定位 / 求职",
        "围绕 AI 时代职业路径、Agent Systems Engineer 定位、简历叙事、JD 信号与求职策略的页面。",
        ("职业判断框架.md", "职业信号与叙事框架.md"),
        ("职业决策与求职策略观察.md", "产品判断力与能力焦虑分离观察.md", "投简历恐惧观察.md", "go-to-market-strategy.md"),
    ),
    Topic(
        "ai-industry-investment",
        "AI 产业 / 投资 / 创业位置",
        "围绕 AI 产业分层、付钱地图、资本结构、创业环境与技术成熟度判断的页面。",
        ("AI产业与投资判断框架.md", "产品验证判断框架.md"),
    ),
    Topic(
        "learning-judgment-mental-models",
        "学习 / 判断 / 心智模型",
        "围绕 taste、科学与技艺、数学基础、Naval、内心游戏、人际理解与长期适配的页面。",
        ("方向与执行判断框架.md",),
        ("自由与当下的观察.md", "物理模型抽象人生问题观察.md"),
    ),
    Topic(
        "projects-roadmaps",
        "项目 / 路线图 / 执行计划",
        "围绕当前项目路线图、月度执行计划、agent harness core、Codex-like harness 与产品设想的页面。",
        ("产品定义判断框架.md", "Harness架构判断框架.md", "职业信号与叙事框架.md"),
        ("go-to-market-strategy.md",),
    ),
)

TOPIC_BY_SLUG = {topic.slug: topic for topic in TOPICS}


PAGE_TOPICS: dict[str, str] = {
    "AAR knowledge sharing 的设计洞察与取舍.md": "agent-harness-runtime",
    "AI 时代的结果确定性 Agentic Runtime 与 Evaluation-First.md": "agent-harness-runtime",
    "AI 自演化研究 Harness.md": "agent-harness-runtime",
    "Agent 系统作为 OS 与 Cloud Runtime 问题.md": "agent-harness-runtime",
    "Bakery-iOS端远程开发APP.md": "agent-harness-runtime",
    "EvoMap-Agent 互联网与集体潜意识.md": "agent-harness-runtime",
    "Slock-人机协作平台.md": "agent-harness-runtime",
    "agent 复利工作模式.md": "agent-harness-runtime",
    "agent-runtime-os-cloud-runtime.md": "agent-harness-runtime",
    "agentic-design-patterns.md": "agent-harness-runtime",
    "agent时代的人机交互新命题.md": "agent-harness-runtime",
    "ai-self-evolution-research-harnesses.md": "agent-harness-runtime",
    "alchaincyf-nuwa-skill-repo-map.md": "agent-harness-runtime",
    "automated-weak-to-strong-researcher.md": "agent-harness-runtime",
    "badlogic-pi-mono-repo-map.md": "agent-harness-runtime",
    "claude-code-harness.md": "agent-harness-runtime",
    "clawhouse-多设备-agent-工作台.md": "agent-harness-runtime",
    "codebases-as-knowledge-sources.md": "agent-harness-runtime",
    "coding agent 的上下文压缩工作流.md": "agent-harness-runtime",
    "coding-agent-harness-comparison.md": "agent-harness-runtime",
    "harness-engineering.md": "agent-harness-runtime",
    "luliyanng-nono-cowork-repo-map.md": "agent-harness-runtime",
    "multica-ai-multica-repo-map.md": "agent-harness-runtime",
    "multica与clawhouse的目标与核心价值差异.md": "agent-harness-runtime",
    "openclaw-openclaw-repo-map.md": "agent-harness-runtime",
    "pi-coding-agent-harness.md": "agent-harness-runtime",
    "refactoringhq-tolaria-repo-map.md": "agent-harness-runtime",
    "reflexioai-reflexio-repo-map.md": "agent-harness-runtime",
    "safety-research-automated-w2s-research-repo-map.md": "agent-harness-runtime",
    "thin-harness-fat-skills.md": "agent-harness-runtime",
    "Tolaria 综合分析.md": "agent-harness-runtime",
    "yvonnegladwellstack-yvskills-repo-map.md": "agent-harness-runtime",
    "被持续委托的工作主体.md": "agent-harness-runtime",
    "agent-context-infra-2026-05-24.md": "context-memory-knowledge-system",
    "agent-context-infra-2026-05-25.md": "context-memory-knowledge-system",
    "ai-knowledge-systems-product-definition-beliefs.md": "context-memory-knowledge-system",
    "context-core-technical-frontier-2026-05-25.md": "context-memory-knowledge-system",
    "gogo.md": "context-memory-knowledge-system",
    "grapeot-context-infrastructure-repo-map.md": "context-memory-knowledge-system",
    "information-compounding-systems-design.md": "context-memory-knowledge-system",
    "knowledge-base-operating-model.md": "context-memory-knowledge-system",
    "local-knowledge-base-patterns.md": "context-memory-knowledge-system",
    "volcengine-openviking-repo-map.md": "context-memory-knowledge-system",
    "从Andrej Karpathy的LLM Wiki和鸭哥的context infrastructure看信息复利系统的设计.md": "context-memory-knowledge-system",
    "给自己做了一个llm-wiki的入口应用.md": "context-memory-knowledge-system",
    "AI 产品六层与 L3-L6 能力分层.md": "ai-product-product-definition",
    "GenAI 的共识边界与任务委托框架.md": "ai-product-product-definition",
    "ai-architect-advanced-architecture.md": "ai-product-product-definition",
    "ai-architect-context-intelligence.md": "ai-product-product-definition",
    "ai-architect-lens.md": "ai-product-product-definition",
    "ai-architect-proactive-intelligence.md": "ai-product-product-definition",
    "go-to-market-multiple-times.md": "ai-product-product-definition",
    "pre-pmf-validation-playbook.md": "ai-product-product-definition",
    "Superlinear社区AgentSkill知识治理信号.md": "research-knowledge-governance",
    "lab-research-knowledge-base-product-strategy.md": "research-knowledge-governance",
    "oh-share-it公共知识库产品.md": "research-knowledge-governance",
    "superlinear-team-skill-sharing.md": "research-knowledge-governance",
    "什么是公共知识库应该共享的公共知识.md": "research-knowledge-governance",
    "公共知识库、Reflexio与EvoMap的对比分析.md": "research-knowledge-governance",
    "多人协作AgentSkill知识治理-对外一页纸.md": "research-knowledge-governance",
    "课题组公共知识库-博客草稿.md": "research-knowledge-governance",
    "课题组公共知识库的产品定义信念.md": "research-knowledge-governance",
    "课题组公共知识库的架构风险与分层设计.md": "research-knowledge-governance",
    "课题组公共知识库的联邦架构设计.md": "research-knowledge-governance",
    "Agent Systems Engineer职业定位.md": "career-positioning-job-search",
    "Agent岗位JD抽样与能力信号.md": "career-positioning-job-search",
    "AI 时代大厂打工人的五条路.md": "career-positioning-job-search",
    "AI 焦虑的三种形态与行动解法.md": "career-positioning-job-search",
    "AI 让我们重新开始享受自己的职业.md": "career-positioning-job-search",
    "Anthropic与OpenAI的Agent Systems履历North Star.md": "career-positioning-job-search",
    "Barytes-GitHub项目与Agent层次评估.md": "career-positioning-job-search",
    "Databricks 的人才态度与双向选择.md": "career-positioning-job-search",
    "Naval财富框架应用于求职困境.md": "career-positioning-job-search",
    "增长工程师的职业押注与面试叙事.md": "career-positioning-job-search",
    "求职范式转变：让工作找到你.md": "career-positioning-job-search",
    "真实JD记录.md": "career-positioning-job-search",
    "真本事-从会工作到会赚钱.md": "career-positioning-job-search",
    "传统职业路径与Naval路径的投资模型.md": "career-positioning-job-search",
    "自我表达、Specific Knowledge与市场价值之间的桥梁.md": "career-positioning-job-search",
    "高级岗位简历的三条写法原则.md": "career-positioning-job-search",
    "AI 时代的投资与生存法则.md": "ai-industry-investment",
    "AI产业分层地图.md": "ai-industry-investment",
    "AI产业的付钱地图.md": "ai-industry-investment",
    "Auto-Research时代的算力霸权与博士分化.md": "ai-industry-investment",
    "衰退期的创业环境与技术判断.md": "ai-industry-investment",
    "Taste：感受良质的能力.md": "learning-judgment-mental-models",
    "ace-the-data-science-interview.md": "learning-judgment-mental-models",
    "go-to-yourself-框架.md": "learning-judgment-mental-models",
    "naval-mental-models.md": "learning-judgment-mental-models",
    "science-and-craft-cognitive-model.md": "learning-judgment-mental-models",
    "喜欢与擅长的命运飞轮.md": "learning-judgment-mental-models",
    "如何了解一个人.md": "learning-judgment-mental-models",
    "概率论入门.md": "learning-judgment-mental-models",
    "纳瓦尔宝典.md": "learning-judgment-mental-models",
    "线性代数正确入门.md": "learning-judgment-mental-models",
    "网球的内心游戏.md": "learning-judgment-mental-models",
    "Agent-harness-core与三种adapter路线.md": "projects-roadmaps",
    "Agent系统月度执行计划-2026-05-24.md": "projects-roadmaps",
    "Agent系统求职与项目路线图-2026-05.md": "projects-roadmaps",
    "Codex-like-agent-harness路线图.md": "projects-roadmaps",
    "Pulse-有呼吸感的项目工作台.md": "projects-roadmaps",
}

LINK_RE = re.compile(r"(?P<prefix>!?\[[^\]]*\]\()(?P<url>[^)\n]+?\.md)(?P<anchor>#[^)]+)?(?P<suffix>\))")


def relative_link(target: Path, source_dir: Path) -> str:
    from os.path import relpath

    return relpath(target, source_dir).replace("\\", "/").replace(" ", "%20")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def page_title(path: Path) -> str:
    text = read_text(path)
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def page_summary(path: Path) -> str:
    text = read_text(path)
    in_frontmatter = False
    if text.startswith("---"):
        in_frontmatter = True
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if in_frontmatter:
            if line == "---":
                in_frontmatter = False
            continue
        if not line or line.startswith("#") or line.startswith("- ") or line.startswith("**来源"):
            continue
        cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)
        return cleaned[:160]
    return "暂无摘要。"


def topic_pages(topic_slug: str) -> list[Path]:
    topic_dir = TOPICS_DIR / topic_slug
    if not topic_dir.exists():
        return []
    return sorted(
        [p for p in topic_dir.rglob("*.md") if p.name != "index.md"],
        key=lambda p: page_title(p),
    )


def discover_source_pages() -> list[Path]:
    roots = [WIKI / "knowledge", WIKI / "bridges", WIKI / "bridges" / "essays"]
    pages: list[Path] = []
    for root in roots:
        if root.exists():
            pages.extend(p for p in root.glob("*.md") if p.name != "README.md")
    return sorted(pages)


def destination_for(source: Path) -> Path:
    topic_slug = PAGE_TOPICS.get(source.name)
    if topic_slug is None:
        raise SystemExit(f"Unmapped wiki page: {source.relative_to(ROOT)}")
    if source.parent.name == "essays":
        return TOPICS_DIR / topic_slug / "essays" / source.name
    return TOPICS_DIR / topic_slug / source.name


def move_pages() -> dict[Path, Path]:
    old_to_new: dict[Path, Path] = {}
    for source in discover_source_pages():
        destination = destination_for(source)
        source_abs = source.resolve()
        destination_abs = destination.resolve()
        if source_abs == destination_abs:
            continue
        if destination.exists():
            raise SystemExit(f"Destination already exists: {destination.relative_to(ROOT)}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.rename(destination)
        old_to_new[source_abs] = destination_abs
    return old_to_new


def remove_obsolete_readmes_and_dirs() -> None:
    for path in [
        WIKI / "knowledge" / "README.md",
        WIKI / "bridges" / "README.md",
        WIKI / "bridges" / "essays" / "README.md",
    ]:
        if path.exists():
            path.unlink()
    for path in [WIKI / "bridges" / "essays", WIKI / "knowledge", WIKI / "bridges"]:
        if path.exists():
            try:
                path.rmdir()
            except OSError:
                pass


def rewrite_links(old_to_new: dict[Path, Path]) -> None:
    new_to_old = {new: old for old, new in old_to_new.items()}

    def replace_for_file(path: Path, text: str) -> str:
        old_source = new_to_old.get(path.resolve(), path.resolve())

        def repl(match: re.Match[str]) -> str:
            url = match.group("url")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith("#"):
                return match.group(0)
            decoded = unquote(url)
            target_old = (old_source.parent / decoded).resolve()
            if target_old in old_to_new:
                target_new = old_to_new[target_old]
            elif target_old.exists():
                target_new = target_old
            else:
                return match.group(0)
            new_url = relative_link(target_new, path.parent)
            return f"{match.group('prefix')}{new_url}{match.group('anchor') or ''}{match.group('suffix')}"

        return LINK_RE.sub(repl, text)

    for path in sorted(WIKI.rglob("*.md")):
        if SITE_DIR in path.parents:
            continue
        text = read_text(path)
        updated = replace_for_file(path, text)
        if updated != text:
            write_text(path, updated)


def markdown_link(target: Path, source: Path | None = None) -> str:
    source_dir = source.parent if source else WIKI
    return relative_link(target, source_dir)


def write_topic_indexes() -> None:
    lines = [
        "# 话题总览",
        "",
        "这里按话题组织原 `knowledge/` 与 `bridges/` 的维护页。`self/` 与 `frameworks/` 仍保持独立层级。",
        "",
    ]
    for topic in TOPICS:
        pages = topic_pages(topic.slug)
        lines.append(f"## [{topic.title}]({topic.slug}/index.md)")
        lines.append("")
        lines.append(topic.summary)
        lines.append("")
        lines.append(f"- 页面数：{len(pages)}")
        lines.append("")
    write_text(TOPICS_DIR / "index.md", "\n".join(lines).rstrip() + "\n")

    for topic in TOPICS:
        pages = topic_pages(topic.slug)
        content = [
            f"# {topic.title}",
            "",
            topic.summary,
            "",
            "## 推荐阅读顺序",
            "",
        ]
        for page in pages[:8]:
            content.append(f"- [{page_title(page)}]({markdown_link(page, TOPICS_DIR / topic.slug / 'index.md')})")
        if len(pages) > 8:
            content.append("- 其余页面可按下面的完整列表继续浏览。")
        content.extend(["", "## 页面", ""])
        for page in pages:
            content.append(f"- [{page_title(page)}]({markdown_link(page, TOPICS_DIR / topic.slug / 'index.md')}): {page_summary(page)}")
        if topic.frameworks:
            content.extend(["", "## 相关框架", ""])
            for name in topic.frameworks:
                target = WIKI / "frameworks" / name
                if target.exists():
                    content.append(f"- [{page_title(target)}]({markdown_link(target, TOPICS_DIR / topic.slug / 'index.md')})")
        if topic.self_pages:
            content.extend(["", "## 相关自我页面", ""])
            for name in topic.self_pages:
                target = WIKI / "self" / name
                if target.exists():
                    content.append(f"- [{page_title(target)}]({markdown_link(target, TOPICS_DIR / topic.slug / 'index.md')})")
        content.extend(["", "## 返回", "", "- [话题总览](../index.md)", "- [Wiki 首页](../../index.md)"])
        write_text(TOPICS_DIR / topic.slug / "index.md", "\n".join(content).rstrip() + "\n")


def write_wiki_index() -> None:
    content = [
        "# 索引",
        "",
        "维护层说明见 [README.md](README.md)。静态网页入口见 [site/index.html](site/index.html)。",
        "",
        "## 按话题浏览",
        "",
        "原 `knowledge/` 与 `bridges/` 已合并到 `topics/`，按主题组织。每个话题目录都有一个 `index.md`。",
        "",
        "- [话题总览](topics/index.md)",
    ]
    for topic in TOPICS:
        content.append(f"- [{topic.title}](topics/{topic.slug}/index.md): {topic.summary}")
    content.extend(
        [
            "",
            "## 按层级浏览",
            "",
            "- [主题层](topics/index.md): 原外部知识与应用分析的主入口。",
            "- [自我层](self/README.md): 稳定偏好、判断模式与个人观察。",
            "- [框架层](frameworks/README.md): 可复用判断框架与 query 路由入口。",
            "",
            "## 网页视图",
            "",
            "- [知识库网页首页](site/index.html)",
            "- [话题层网页](site/layers/topics.html)",
            "- [自我层网页](site/layers/self.html)",
            "- [框架层网页](site/layers/frameworks.html)",
            "",
            "## 最近工作",
            "",
            "摄取、查询与维护历史见 [log.md](log.md)。",
        ]
    )
    write_text(WIKI / "index.md", "\n".join(content).rstrip() + "\n")


def write_wiki_readme() -> None:
    content = """# 维护层

`wiki/` 是由 agent 维护和持续更新的知识层。

- `topics/` 按话题组织外部知识与应用分析，承接原 `knowledge/` 与 `bridges/`。
- `self/` 保存关于你稳定偏好与判断模式的结构化知识。
- `frameworks/` 保存高复用、低噪音的判断框架与 query 入口页。
- `site/` 保存从 Markdown 生成的静态网页视图。

优先更新已有页面，而不是制造重复页面。新维护页默认写中文。
"""
    write_text(WIKI / "README.md", content)


def md_to_site_path(md_path: Path) -> Path:
    rel = md_path.relative_to(WIKI)
    if rel.name == "index.md":
        rel = rel.with_name("index.html")
    else:
        rel = rel.with_suffix(".html")
    return SITE_DIR / "content" / rel


def site_href(from_html: Path, target: Path) -> str:
    return relative_link(target, from_html.parent)


def md_link_to_html(url: str, source_md: Path, html_path: Path) -> str:
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith("#"):
        return html.escape(url, quote=True)
    decoded = unquote(url)
    target = (source_md.parent / decoded).resolve()
    if target == WIKI / "log.md":
        return relative_link(target, html_path.parent)
    if target.exists() and target.suffix == ".md" and WIKI in target.parents:
        return site_href(html_path, md_to_site_path(target))
    if target.exists():
        return relative_link(target, html_path.parent)
    return html.escape(url, quote=True)


def simple_markdown_to_html(md_path: Path, html_path: Path) -> str:
    result: list[str] = []
    in_list = False
    in_code = False
    code_lines: list[str] = []

    def inline(text: str) -> str:
        escaped = html.escape(text)
        escaped = re.sub(
            r"\[([^\]]+)\]\(([^)]+)\)",
            lambda m: f'<a href="{md_link_to_html(html.unescape(m.group(2)), md_path, html_path)}">{m.group(1)}</a>',
            escaped,
        )
        escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
        return escaped

    for raw in read_text(md_path).splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                result.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_code = False
            else:
                if in_list:
                    result.append("</ul>")
                    in_list = False
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line:
            if in_list:
                result.append("</ul>")
                in_list = False
            continue
        if line.startswith("#"):
            if in_list:
                result.append("</ul>")
                in_list = False
            level = min(len(line) - len(line.lstrip("#")), 6)
            text = line[level:].strip()
            result.append(f"<h{level}>{inline(text)}</h{level}>")
        elif line.startswith("- "):
            if not in_list:
                result.append("<ul>")
                in_list = True
            result.append(f"<li>{inline(line[2:].strip())}</li>")
        else:
            if in_list:
                result.append("</ul>")
                in_list = False
            result.append(f"<p>{inline(line)}</p>")
    if in_list:
        result.append("</ul>")
    return "\n".join(result)


def page_shell(title: str, body: str, current: Path) -> str:
    css_href = site_href(current, SITE_DIR / "style.css")
    home_href = site_href(current, SITE_DIR / "index.html")
    topics_href = site_href(current, SITE_DIR / "layers" / "topics.html")
    self_href = site_href(current, SITE_DIR / "layers" / "self.html")
    frameworks_href = site_href(current, SITE_DIR / "layers" / "frameworks.html")
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} · Knowledge Base</title>
  <link rel="stylesheet" href="{css_href}">
</head>
<body>
  <header class="topbar">
    <a href="{home_href}">首页</a>
    <a href="{topics_href}">话题</a>
    <a href="{self_href}">自我</a>
    <a href="{frameworks_href}">框架</a>
  </header>
  <main>
{body}
  </main>
</body>
</html>
"""


def card(title: str, href: str, summary: str, meta: str = "") -> str:
    meta_html = f'<div class="meta">{html.escape(meta)}</div>' if meta else ""
    return f"""<article class="card">
  {meta_html}
  <h3><a href="{href}">{html.escape(title)}</a></h3>
  <p>{html.escape(summary)}</p>
</article>"""


def write_site_css() -> None:
    css = """
:root {
  color-scheme: light;
  --bg: #f7f7f4;
  --paper: #ffffff;
  --ink: #20201d;
  --muted: #666b61;
  --line: #d9ddd2;
  --accent: #2d6a6a;
  --accent-2: #8a4f2a;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
a { color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: 3px; }
.topbar {
  position: sticky;
  top: 0;
  z-index: 1;
  display: flex;
  gap: 18px;
  padding: 12px 28px;
  border-bottom: 1px solid var(--line);
  background: rgba(247, 247, 244, 0.94);
  backdrop-filter: blur(8px);
}
main { max-width: 1180px; margin: 0 auto; padding: 32px 28px 56px; }
.hero { display: grid; gap: 10px; margin-bottom: 28px; }
h1 { margin: 0; font-size: clamp(32px, 5vw, 56px); line-height: 1.05; letter-spacing: 0; }
h2 { margin-top: 34px; border-top: 1px solid var(--line); padding-top: 22px; }
h3 { margin: 6px 0 8px; font-size: 18px; line-height: 1.3; }
p { margin: 8px 0 12px; }
.subtitle { max-width: 780px; color: var(--muted); font-size: 18px; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; }
.card {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  padding: 16px;
}
.meta { color: var(--accent-2); font-size: 13px; margin-bottom: 4px; }
.count { color: var(--muted); font-size: 14px; }
.article {
  max-width: 860px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  padding: 26px;
}
code, pre { background: #eef0ea; border-radius: 6px; }
code { padding: 1px 4px; }
pre { padding: 14px; overflow: auto; }
ul { padding-left: 1.4rem; }
@media (max-width: 640px) {
  .topbar { padding: 10px 16px; overflow-x: auto; }
  main { padding: 24px 16px 42px; }
  .article { padding: 18px; }
}
"""
    write_text(SITE_DIR / "style.css", css.strip() + "\n")


def write_site() -> None:
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    write_site_css()

    topic_cards = []
    for topic in TOPICS:
        html_path = SITE_DIR / "topics" / f"{topic.slug}.html"
        topic_cards.append(card(topic.title, site_href(SITE_DIR / "index.html", html_path), topic.summary, f"{len(topic_pages(topic.slug))} 页"))
    index_body = f"""    <section class="hero">
      <h1>知识库</h1>
      <p class="subtitle">按话题浏览原知识层与桥接层，同时保留自我层和框架层。Markdown 仍是维护源，HTML 用来快速看见结构。</p>
    </section>
    <section class="grid">
      {''.join(topic_cards)}
      {card('自我层', site_href(SITE_DIR / 'index.html', SITE_DIR / 'layers' / 'self.html'), '稳定偏好、判断模式与个人观察。')}
      {card('框架层', site_href(SITE_DIR / 'index.html', SITE_DIR / 'layers' / 'frameworks.html'), '可复用判断框架与 query 路由入口。')}
    </section>
"""
    write_text(SITE_DIR / "index.html", page_shell("知识库", index_body, SITE_DIR / "index.html"))

    for topic in TOPICS:
        pages = topic_pages(topic.slug)
        cards = [
            card(
                page_title(page),
                site_href(SITE_DIR / "topics" / f"{topic.slug}.html", md_to_site_path(page)),
                page_summary(page),
                str(page.relative_to(WIKI)),
            )
            for page in pages
        ]
        body = f"""    <section class="hero">
      <h1>{html.escape(topic.title)}</h1>
      <p class="subtitle">{html.escape(topic.summary)}</p>
      <div class="count">{len(pages)} 个页面</div>
    </section>
    <section class="grid">
      {''.join(cards)}
    </section>
"""
        write_text(SITE_DIR / "topics" / f"{topic.slug}.html", page_shell(topic.title, body, SITE_DIR / "topics" / f"{topic.slug}.html"))

    layer_pages = {
        "topics": [(TOPICS_DIR / topic.slug / "index.md") for topic in TOPICS],
        "self": sorted((WIKI / "self").glob("*.md"), key=lambda p: page_title(p)),
        "frameworks": sorted((WIKI / "frameworks").glob("*.md"), key=lambda p: page_title(p)),
    }
    layer_titles = {"topics": "话题层", "self": "自我层", "frameworks": "框架层"}
    layer_summaries = {
        "topics": "原知识层与桥接层的按话题入口。",
        "self": "稳定偏好、判断模式与个人观察。",
        "frameworks": "可复用判断框架与 query 路由入口。",
    }
    for layer, pages in layer_pages.items():
        current = SITE_DIR / "layers" / f"{layer}.html"
        cards = [
            card(page_title(page), site_href(current, md_to_site_path(page)), page_summary(page), str(page.relative_to(WIKI)))
            for page in pages
        ]
        body = f"""    <section class="hero">
      <h1>{layer_titles[layer]}</h1>
      <p class="subtitle">{layer_summaries[layer]}</p>
      <div class="count">{len(pages)} 个页面</div>
    </section>
    <section class="grid">
      {''.join(cards)}
    </section>
"""
        write_text(current, page_shell(layer_titles[layer], body, current))

    for md_path in sorted(WIKI.rglob("*.md")):
        if SITE_DIR in md_path.parents:
            continue
        if md_path == WIKI / "log.md":
            continue
        html_path = md_to_site_path(md_path)
        body = f"""    <article class="article">
      <div class="meta">{html.escape(str(md_path.relative_to(WIKI)))}</div>
      {simple_markdown_to_html(md_path, html_path)}
    </article>
"""
        write_text(html_path, page_shell(page_title(md_path), body, html_path))


def append_log_entry() -> None:
    log = WIKI / "log.md"
    if not log.exists():
        return
    marker = "## [2026-05-29] lint | 按话题重组 wiki 并生成静态网页"
    text = read_text(log)
    if marker in text:
        return
    entry = f"""

{marker}

将原 `wiki/knowledge/` 与 `wiki/bridges/` 的维护页合并迁移到 `wiki/topics/`，按话题建立索引；保留 `wiki/self/` 与 `wiki/frameworks/` 作为独立层级。同时生成 `wiki/site/` 静态网页入口，用于从网页视角浏览话题层、自我层与框架层。

**新增结构**
- `wiki/topics/`
- `wiki/site/`

**说明**
- Markdown 仍是维护源，HTML 是可重新生成的浏览视图。
- 历史维护记录中的旧路径不主动重写。
"""
    write_text(log, text.rstrip() + entry)


def main() -> None:
    old_to_new = move_pages()
    remove_obsolete_readmes_and_dirs()
    rewrite_links(old_to_new)
    write_topic_indexes()
    write_wiki_index()
    write_wiki_readme()
    write_site()
    append_log_entry()
    print(f"Moved {len(old_to_new)} pages into {TOPICS_DIR.relative_to(ROOT)}")
    print(f"Generated topic indexes and static site at {SITE_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
