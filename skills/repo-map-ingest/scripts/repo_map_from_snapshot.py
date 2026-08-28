#!/usr/bin/env python3
"""Generate a maintained repo map note from a GitHub repo snapshot markdown."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple


HEADING_RE = re.compile(r"^## (.+)$", re.MULTILINE)
SUBHEADING_RE = re.compile(r"^### `?(.+?)`?$", re.MULTILINE)
INDEX_LINK_RE = re.compile(r"^- \[(.+?)\]\((.+?)\):\s*(.+)$")
TITLE_RE = re.compile(r"^# (.+)$", re.MULTILINE)

MANIFEST_FILES = {
    "package.json",
    "pyproject.toml",
    "requirements.txt",
    "setup.py",
    "Cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
}

AGENT_CONTROL_NAMES = {
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".cursorrules",
    ".cursorignore",
    ".github/copilot-instructions.md",
}

STOPWORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "how",
    "in",
    "into",
    "of",
    "on",
    "or",
    "the",
    "to",
    "use",
    "with",
}

RELATED_PAGE_SCORE_THRESHOLD = 5
SECTION_ALIASES = {
    "Knowledge": "knowledge",
    "知识": "knowledge",
    "Bridges": "bridges",
    "桥接": "bridges",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a maintained repo map note from a repo snapshot."
    )
    parser.add_argument("snapshot_path", help="Path to a repo snapshot markdown file")
    parser.add_argument(
        "--outdir",
        default="wiki/topics/agent-harness-runtime",
        help="Destination directory for the generated repo map note",
    )
    parser.add_argument(
        "--topic",
        default=None,
        help="Override study topic shown in the generated note",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def extract_bullets(section_text: str) -> List[str]:
    return [match.group(1).strip() for match in re.finditer(r"^- (.+)$", section_text, re.MULTILINE)]


def extract_metadata_map(section_text: str) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for bullet in extract_bullets(section_text):
        if ": " in bullet:
            key, value = bullet.split(": ", 1)
            result[key.strip("- ").strip()] = value.strip()
    return result


def extract_captured_file(text: str, path: str) -> Optional[str]:
    pattern = re.compile(
        rf"^### `{re.escape(path)}`\n.*?```[^\n]*\n(.*?)\n```",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else None


def parse_repo_identity(observation: Dict[str, str]) -> Tuple[str, str]:
    repo = observation.get("Repository", "").strip("`")
    if "/" in repo:
        owner, name = repo.split("/", 1)
        return owner, name
    return "unknown", repo or "repo"


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def normalize_inline_code(value: str) -> str:
    value = value.strip()
    if value.startswith("`") and value.endswith("`") and len(value) >= 2:
        return value[1:-1]
    return value


def best_relative_path(from_path: Path, target_path: Path) -> str:
    try:
        return str(target_path.resolve().relative_to(Path.cwd().resolve()))
    except Exception:
        return str(target_path)


def clean_code_fence_text(text: str) -> List[str]:
    return [line.rstrip() for line in text.splitlines()]


def tokenize(text: str) -> Set[str]:
    tokens = set(re.findall(r"[a-z0-9]+", text.lower()))
    return {token for token in tokens if token not in STOPWORDS and len(token) > 1}


def summarize_readme(readme_text: Optional[str], fallback_description: str) -> Tuple[str, List[str]]:
    if not readme_text:
        if fallback_description:
            return "从仓库公开描述看，它已经有明确主题定位，但更精确的运行方式仍需结合源码与控制文件确认。", []
        return "这个仓库的具体定位仍需通过更深入的源码阅读来确认。", []

    lines = []
    for raw_line in clean_code_fence_text(readme_text):
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        if line.startswith("![") or line.startswith("[!["):
            continue
        if line.startswith("```"):
            continue
        if re.match(r"^[\-\*\d]", line):
            continue
        lines.append(line)

    if lines:
        summary = "从 README 与顶层结构看，这个仓库已经形成清晰的主题定位与控制边界，适合继续按机制而非按文件做定向深读。"
    elif fallback_description:
        summary = "从仓库公开描述看，它已经有明确主题定位，但更精确的运行方式仍需结合源码与控制文件确认。"
    else:
        summary = "这个仓库的具体定位仍需通过更深入的源码阅读来确认。"
    return summary, []


def build_mechanism_inventory(
    top_dirs: Sequence[str], anchors: Sequence[str]
) -> List[Tuple[str, List[str]]]:
    inventory: List[Tuple[str, List[str]]] = []

    if any(path.startswith(".github/workflows/") for path in anchors):
        inventory.append(
            (
                "自动化与仓库契约",
                [
                    "这个仓库通过 GitHub Actions 工作流把质量与交付预期外化出来，而不是只依赖贡献者的非正式自觉。",
                    "这很可能是在补偿本地开发与合并时质量检查之间的漂移。",
                ],
            )
        )

    if any(path in MANIFEST_FILES for path in anchors):
        inventory.append(
            (
                "构建与依赖边界",
                [
                    "Manifest 文件把运行时与打包契约显式放在仓库根部。",
                    "这能帮助后续阅读者在深入实现文件之前先找到真正的执行边界。",
                ],
            )
        )

    if any(path in AGENT_CONTROL_NAMES or path.startswith(".cursor/rules/") for path in anchors):
        inventory.append(
            (
                "Agent 或贡献者控制层",
                [
                    "这个仓库似乎包含显式的指令文件或编辑器规则，用来约束自动化贡献者或人工贡献者的行为方式。",
                    "这些文件是研究控制逻辑、权限机制与任务塑形方式的强证据点。",
                ],
            )
        )

    if "tests" in top_dirs:
        inventory.append(
            (
                "验证层",
                [
                    "单独的 `tests/` 目录说明这个仓库把验证当作一级维护子系统。",
                    "这里最可迁移的问题不只是“测了什么”，而是测试结构如何与 CI 和发布规则相互作用。",
                ],
            )
        )

    if "src" in top_dirs:
        inventory.append(
            (
                "实现边界",
                [
                    "单独的 `src/` 目录把实现代码与仓库控制文件清楚分开。",
                    "这有助于区分运行支架与核心运行时表面。",
                ],
            )
        )

    if not inventory:
        inventory.append(
            (
                "仍是初版仓库地图",
                [
                    "当前 snapshot 足以为后续定向阅读提供锚点，但还不足以支撑强工程实践结论。",
                    "在把仓库特定模式提升为可迁移建议之前，还需要进一步回读实现文件。",
                ],
            )
        )

    return inventory


def infer_open_questions(top_dirs: Sequence[str], anchors: Sequence[str]) -> List[str]:
    questions = [
        "围绕当前研究主题，哪些实现文件承载了主要运行路径？",
        "README 的叙述与代码、CI 真正执行的路径之间，哪里开始出现偏差？",
    ]
    if "src" in top_dirs:
        questions.append("哪些 `src/` 模块定义了杠杆最高的执行路径或架构接缝？")
    if any(path.startswith(".github/workflows/") for path in anchors):
        questions.append("哪些 workflow 检查是真正的硬门，哪些只是信息性自动化？")
    return questions


def infer_repo_root() -> Path:
    return Path.cwd()


def read_page_title(page_path: Path) -> Optional[str]:
    if not page_path.exists():
        return None
    text = read_text(page_path)
    match = TITLE_RE.search(text)
    return match.group(1).strip() if match else None


def load_related_candidates(index_path: Path) -> List[Dict[str, str]]:
    if not index_path.exists():
        return []

    candidates: List[Dict[str, str]] = []
    current_section = None
    for line in index_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current_section = SECTION_ALIASES.get(line[3:].strip())
            continue
        match = INDEX_LINK_RE.match(line)
        if not match or current_section not in {"knowledge", "bridges"}:
            continue

        label, rel_path, description = match.groups()
        if rel_path.endswith("README.md"):
            continue

        page_path = (index_path.parent / rel_path).resolve()
        page_title = read_page_title(page_path) or label
        candidates.append(
            {
                "section": current_section,
                "label": label,
                "title": page_title,
                "description": description.strip(),
                "path": str(page_path),
            }
        )
    return candidates


def score_related_candidate(
    candidate: Dict[str, str],
    query_tokens: Set[str],
    topic_text: str,
    mechanism_titles: Sequence[str],
) -> int:
    haystack = " ".join(
        [candidate["title"], candidate["label"], candidate["description"]]
    )
    candidate_tokens = tokenize(haystack)
    overlap = query_tokens & candidate_tokens
    score = len(overlap) * 3

    haystack_lower = haystack.lower()
    topic_lower = topic_text.lower()
    if topic_lower and topic_lower in haystack_lower:
        score += 6

    for title in mechanism_titles:
        title_lower = title.lower()
        if title_lower in haystack_lower:
            score += 2

    if candidate["section"] == "knowledge":
        score += 1
    return score


def infer_related_pages(
    topic: str,
    mechanisms: Sequence[Tuple[str, List[str]]],
    summary_line: str,
    repo_meta: Dict[str, str],
    outfile: Path,
) -> List[Tuple[str, str]]:
    repo_root = infer_repo_root()
    index_path = repo_root / "wiki/index.md"
    candidates = load_related_candidates(index_path)
    if not candidates:
        return []

    mechanism_titles = [title for title, _ in mechanisms]
    query_text = " ".join(
        [
            topic,
            summary_line,
            repo_meta.get("Description", ""),
            " ".join(mechanism_titles),
        ]
    )
    query_tokens = tokenize(query_text)

    scored: List[Tuple[int, Dict[str, str]]] = []
    for candidate in candidates:
        score = score_related_candidate(candidate, query_tokens, topic, mechanism_titles)
        if score > 0:
            scored.append((score, candidate))

    scored.sort(key=lambda item: (-item[0], item[1]["title"].lower()))

    selected: List[Tuple[str, str]] = []
    seen_paths: Set[str] = set()

    # Always include the repo-study bridge if it exists.
    for score, candidate in scored:
        candidate_path = Path(candidate["path"]).name
        if candidate_path == "codebases-as-knowledge-sources.md":
            rel = os.path.relpath(candidate["path"], outfile.parent)
            selected.append((candidate["title"], rel))
            seen_paths.add(candidate["path"])
            break

    for score, candidate in scored:
        if candidate["path"] in seen_paths:
            continue
        if score < RELATED_PAGE_SCORE_THRESHOLD:
            continue
        rel = os.path.relpath(candidate["path"], outfile.parent)
        selected.append((candidate["title"], rel))
        seen_paths.add(candidate["path"])
        if len(selected) >= 4:
            break

    return selected


def generate_note(snapshot_path: Path, outdir: Path, topic_override: Optional[str]) -> Path:
    text = read_text(snapshot_path)

    observation = extract_metadata_map(extract_section(text, "Observation Scope"))
    repo_meta = extract_metadata_map(extract_section(text, "Repository Metadata"))
    top_tree = extract_section(text, "Top-Level Tree")
    top_dirs = extract_bullets(extract_section(top_tree, "Directories")) if "##" in top_tree else []
    if not top_dirs:
        dirs_match = re.search(r"### Directories\n(.*?)\n### Files", top_tree, re.DOTALL)
        files_match = re.search(r"### Files\n(.*)$", top_tree, re.DOTALL)
        top_dirs = extract_bullets(dirs_match.group(1)) if dirs_match else []
        top_files = extract_bullets(files_match.group(1)) if files_match else []
    else:
        top_files = []
    if not top_files:
        files_match = re.search(r"### Files\n(.*)$", top_tree, re.DOTALL)
        top_files = extract_bullets(files_match.group(1)) if files_match else []

    top_dirs = [normalize_inline_code(item) for item in top_dirs]
    top_files = [normalize_inline_code(item) for item in top_files]
    anchors = [
        normalize_inline_code(item)
        for item in extract_bullets(extract_section(text, "Selected Evidence Anchors"))
    ]
    owner, repo = parse_repo_identity(observation)
    readme_name = next((path for path in anchors if Path(path).name.lower().startswith("readme")), "README.md")
    readme_text = extract_captured_file(text, readme_name)
    summary_line, supporting_lines = summarize_readme(
        readme_text, repo_meta.get("Description", "").strip()
    )
    topic = topic_override or observation.get("Requested topic", "").strip("`") or "仓库架构与工程实践"
    if topic == "repository architecture and engineering practices":
        topic = "仓库架构与工程实践"
    mechanisms = build_mechanism_inventory(top_dirs, anchors)
    questions = infer_open_questions(top_dirs, anchors)

    outdir.mkdir(parents=True, exist_ok=True)
    outfile = outdir / f"{slugify(owner)}-{slugify(repo)}-repo-map.md"
    related_pages = infer_related_pages(
        topic=topic,
        mechanisms=mechanisms,
        summary_line=summary_line,
        repo_meta=repo_meta,
        outfile=outfile,
    )

    try:
        source_basis_link = os.path.relpath(snapshot_path.resolve(), outfile.parent.resolve())
    except Exception:
        source_basis_link = str(snapshot_path)

    lines: List[str] = [
        f"# {owner}/{repo} 仓库地图",
        "",
        "## 摘要",
        "",
        f"这页是围绕主题“{topic}”维护的 `{owner}/{repo}` 第一版仓库地图。",
        "",
        summary_line,
    ]
    for line in supporting_lines:
        lines.extend(["", line])

    lines.extend(
        [
            "",
            "当前置信度仍停留在“架构地图”层，而不是“实现已读透”层：它已经足够支撑定向追问，但还不足以裁定每一条工程实践判断。",
            "",
            "## 仓库目的",
            "",
            "- 公开定位：仓库元数据与 README 表明它有明确主题定位；更精确的中文摘要建议在后续深读时补全。",
            f"- 观察时默认分支：{observation.get('Observed ref', '(未知)')}",
            f"- 主要语言：{repo_meta.get('Language', '(未知)')}",
            f"- 仓库地址：{observation.get('URL', '(未知)')}",
            "",
            "## 架构地图",
            "",
            "### 顶层目录",
            "",
        ]
    )
    lines.extend(f"- `{item.strip('`')}`" for item in top_dirs or ["(未记录)"])
    lines.extend(
        [
            "",
            "### 顶层文件",
            "",
        ]
    )
    lines.extend(f"- `{item.strip('`')}`" for item in top_files or ["(未记录)"])

    lines.extend(
        [
            "",
            "## 机制清单",
            "",
        ]
    )
    for title, bullets in mechanisms:
        lines.extend([f"### {title}", ""])
        lines.extend(f"- {bullet}" for bullet in bullets)
        lines.append("")

    lines.extend(
        [
            "## 证据锚点",
            "",
            f"- Snapshot 来源：[{snapshot_path.name}]({source_basis_link})",
            f"- 仓库：{observation.get('Repository', '(未知)')}",
            f"- 观察分支：{observation.get('Observed ref', '(未知)')}",
            f"- 解析到的 commit：{observation.get('Latest resolved commit', '(未知)')}",
            "",
        ]
    )
    lines.extend(f"- `{anchor.strip('`')}`" for anchor in anchors or ["(none captured)"])

    lines.extend(
        [
            "",
            "## 开放问题",
            "",
        ]
    )
    lines.extend(f"- {question}" for question in questions)
    lines.extend(
        [
            "",
            "## 来源依据",
            "",
            f"- [仓库 snapshot]({source_basis_link})",
            "",
            "## 相关页面",
            "",
        ]
    )
    if related_pages:
        lines.extend(f"- [{title}]({path})" for title, path in related_pages)
    else:
        codebase_page = Path.cwd() / "wiki/topics/agent-harness-runtime/codebases-as-knowledge-sources.md"
        codebase_link = os.path.relpath(codebase_page, outfile.parent)
        lines.append(f"- [代码库作为知识来源]({codebase_link})")

    outfile.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return outfile


def main() -> int:
    args = parse_args()
    output = generate_note(
        snapshot_path=Path(args.snapshot_path),
        outdir=Path(args.outdir),
        topic_override=args.topic,
    )
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
