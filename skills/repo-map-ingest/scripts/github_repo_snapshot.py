#!/usr/bin/env python3
"""Fetch a minimal GitHub repository evidence snapshot into raw/external/.

The snapshot is meant to preserve a compact, inspectable evidence bundle for
later knowledge extraction rather than clone or mirror the whole repository.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


USER_AGENT = "repo-map-ingest/1.0"
API_ACCEPT = "application/vnd.github+json"
MAX_FILE_BYTES = 50_000
MAX_WORKFLOW_FILES = 12
MAX_CURSOR_RULES = 12

TOP_LEVEL_FILES = {
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".cursorrules",
    ".cursorignore",
    ".github/copilot-instructions.md",
    "README.md",
    "README.mdx",
    "README.rst",
    "README.txt",
    "package.json",
    "pnpm-workspace.yaml",
    "turbo.json",
    "nx.json",
    "pyproject.toml",
    "requirements.txt",
    "setup.py",
    "Cargo.toml",
    "go.mod",
    "Makefile",
    "justfile",
    "Dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
}

WORKFLOW_PREFIX = ".github/workflows/"
CURSOR_RULES_PREFIX = ".cursor/rules/"


@dataclass
class RepoTarget:
    owner: str
    repo: str
    ref: Optional[str]
    canonical_url: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a compact GitHub repository evidence snapshot."
    )
    parser.add_argument("repo_url", help="GitHub repository URL")
    parser.add_argument(
        "--outdir",
        default="raw/external",
        help="Destination directory for the snapshot markdown file",
    )
    parser.add_argument(
        "--ref",
        default=None,
        help="Branch, tag, or commit to inspect. Overrides any ref in the URL.",
    )
    parser.add_argument(
        "--topic",
        default="repository architecture and engineering practices",
        help="Study topic recorded in the snapshot metadata",
    )
    return parser.parse_args()


def parse_repo_url(repo_url: str, explicit_ref: Optional[str]) -> RepoTarget:
    parsed = urllib.parse.urlparse(repo_url)
    if parsed.netloc not in {"github.com", "www.github.com"}:
        raise ValueError(f"Unsupported host for repo URL: {parsed.netloc}")

    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        raise ValueError("GitHub URL must include both owner and repo")

    owner = parts[0]
    repo = parts[1]
    if repo.endswith(".git"):
        repo = repo[:-4]

    ref = explicit_ref
    if ref is None and len(parts) >= 4 and parts[2] in {"tree", "blob"}:
        ref = urllib.parse.unquote(parts[3])

    return RepoTarget(
        owner=owner,
        repo=repo,
        ref=ref,
        canonical_url=f"https://github.com/{owner}/{repo}",
    )


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def request_json(url: str) -> Dict:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": API_ACCEPT,
            "User-Agent": USER_AGENT,
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def request_text(url: str, accept: Optional[str] = None) -> str:
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()
    return data.decode("utf-8", errors="replace")


def fetch_repo_metadata(target: RepoTarget) -> Dict:
    return request_json(
        f"https://api.github.com/repos/{target.owner}/{target.repo}"
    )


def fetch_commit(target: RepoTarget, ref: str) -> Dict:
    encoded_ref = urllib.parse.quote(ref, safe="")
    return request_json(
        f"https://api.github.com/repos/{target.owner}/{target.repo}/commits/{encoded_ref}"
    )


def fetch_tree(target: RepoTarget, ref: str) -> Dict:
    encoded_ref = urllib.parse.quote(ref, safe="")
    return request_json(
        f"https://api.github.com/repos/{target.owner}/{target.repo}/git/trees/{encoded_ref}?recursive=1"
    )


def find_top_level_readme(tree_paths: Sequence[str]) -> Optional[str]:
    candidates = []
    for path in tree_paths:
        if "/" in path:
            continue
        if path.lower().startswith("readme"):
            candidates.append(path)
    if not candidates:
        return None
    candidates.sort(key=lambda path: (path.lower() != "readme.md", path.lower()))
    return candidates[0]


def select_paths(tree_paths: Sequence[str]) -> List[str]:
    selected = set()

    readme = find_top_level_readme(tree_paths)
    if readme:
        selected.add(readme)

    for path in tree_paths:
        if path in TOP_LEVEL_FILES:
            selected.add(path)

    workflow_count = 0
    cursor_rule_count = 0
    for path in tree_paths:
        if path.startswith(WORKFLOW_PREFIX) and workflow_count < MAX_WORKFLOW_FILES:
            selected.add(path)
            workflow_count += 1
        elif path.startswith(CURSOR_RULES_PREFIX) and cursor_rule_count < MAX_CURSOR_RULES:
            selected.add(path)
            cursor_rule_count += 1

    return sorted(selected)


def fetch_file_content(target: RepoTarget, path: str, ref: str) -> Tuple[str, bool]:
    encoded_path = urllib.parse.quote(path)
    encoded_ref = urllib.parse.quote(ref, safe="")
    data = request_json(
        "https://api.github.com/repos/"
        f"{target.owner}/{target.repo}/contents/{encoded_path}?ref={encoded_ref}"
    )
    if data.get("type") != "file":
        raise ValueError(f"Path is not a file: {path}")

    content = data.get("content", "")
    encoding = data.get("encoding", "")
    if encoding == "base64":
        raw_bytes = base64.b64decode(content)
    else:
        raw_bytes = content.encode("utf-8")

    truncated = False
    if len(raw_bytes) > MAX_FILE_BYTES:
        raw_bytes = raw_bytes[:MAX_FILE_BYTES]
        truncated = True

    return raw_bytes.decode("utf-8", errors="replace"), truncated


def fence_language(path: str) -> str:
    suffix = Path(path).suffix.lower()
    return {
        ".md": "md",
        ".mdx": "mdx",
        ".yml": "yaml",
        ".yaml": "yaml",
        ".json": "json",
        ".toml": "toml",
        ".py": "python",
        ".ts": "ts",
        ".tsx": "tsx",
        ".js": "js",
        ".sh": "bash",
        ".rb": "ruby",
        ".go": "go",
        ".rs": "rust",
        ".java": "java",
    }.get(suffix, "")


def summarize_top_level(tree_items: Sequence[Dict]) -> Tuple[List[str], List[str]]:
    dirs = sorted(
        {
            item["path"]
            for item in tree_items
            if item["type"] == "tree" and "/" not in item["path"]
        }
    )
    files = sorted(
        {
            item["path"]
            for item in tree_items
            if item["type"] == "blob" and "/" not in item["path"]
        }
    )
    return dirs, files


def format_list(items: Iterable[str]) -> str:
    return "\n".join(f"- `{item}`" for item in items) or "- none"


def write_snapshot(
    outdir: Path,
    target: RepoTarget,
    repo_meta: Dict,
    ref: str,
    commit: Dict,
    tree_items: Sequence[Dict],
    selected_paths: Sequence[str],
    fetched_files: Sequence[Tuple[str, str, bool]],
    topic: str,
) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    filename = f"github-repo-{slugify(target.owner)}-{slugify(target.repo)}.md"
    outfile = outdir / filename

    top_dirs, top_files = summarize_top_level(tree_items)
    commit_sha = commit.get("sha", "")
    commit_date = (
        commit.get("commit", {})
        .get("committer", {})
        .get("date", "")
    )

    frontmatter = textwrap.dedent(
        f"""\
        ---
        title: "GitHub repo snapshot: {target.owner}/{target.repo}"
        source: "{target.canonical_url}"
        author:
        published:
        created: {timestamp}
        description: "Compact GitHub repository evidence snapshot for repo-map-ingest."
        tags:
          - "github"
          - "repo-snapshot"
        ---
        """
    ).strip()

    lines: List[str] = [
        frontmatter,
        "",
        f"# GitHub Repo Snapshot: `{target.owner}/{target.repo}`",
        "",
        "## Observation Scope",
        "",
        f"- Repository: `{target.owner}/{target.repo}`",
        f"- URL: {target.canonical_url}",
        f"- Requested topic: {topic}",
        f"- Observed ref: `{ref}`",
        f"- Latest resolved commit: `{commit_sha}`",
        f"- Commit date: `{commit_date}`",
        f"- Snapshot date (UTC): `{timestamp}`",
        "",
        "## Repository Metadata",
        "",
        f"- Description: {repo_meta.get('description') or '(none)'}",
        f"- Default branch: `{repo_meta.get('default_branch') or ''}`",
        f"- Language: `{repo_meta.get('language') or ''}`",
        f"- Stars: `{repo_meta.get('stargazers_count', 0)}`",
        f"- Forks: `{repo_meta.get('forks_count', 0)}`",
        f"- Open issues: `{repo_meta.get('open_issues_count', 0)}`",
        "",
        "## Top-Level Tree",
        "",
        "### Directories",
        "",
        format_list(top_dirs),
        "",
        "### Files",
        "",
        format_list(top_files),
        "",
        "## Selected Evidence Anchors",
        "",
        format_list(selected_paths),
        "",
        "## Captured Files",
        "",
    ]

    for path, content, truncated in fetched_files:
        lines.extend(
            [
                f"### `{path}`",
                "",
                f"- Source path: `{path}`",
                f"- Truncated: `{'yes' if truncated else 'no'}`",
                "",
                f"```{fence_language(path)}",
                content.rstrip(),
                "```",
                "",
            ]
        )

    outfile.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return outfile


def main() -> int:
    args = parse_args()
    target = parse_repo_url(args.repo_url, args.ref)

    try:
        repo_meta = fetch_repo_metadata(target)
        ref = target.ref or repo_meta.get("default_branch")
        if not ref:
            raise ValueError("Could not determine repository ref")
        commit = fetch_commit(target, ref)
        tree = fetch_tree(target, ref)
    except urllib.error.HTTPError as exc:
        sys.stderr.write(f"GitHub API request failed: HTTP {exc.code}\n")
        return 1
    except urllib.error.URLError as exc:
        sys.stderr.write(f"Network request failed: {exc}\n")
        return 1
    except ValueError as exc:
        sys.stderr.write(f"{exc}\n")
        return 1

    tree_items = tree.get("tree", [])
    tree_paths = [item["path"] for item in tree_items if item.get("type") == "blob"]
    selected_paths = select_paths(tree_paths)

    fetched_files: List[Tuple[str, str, bool]] = []
    for path in selected_paths:
        try:
            content, truncated = fetch_file_content(target, path, ref)
        except Exception as exc:  # pragma: no cover - best-effort capture
            content = f"[failed to fetch file content: {exc}]"
            truncated = False
        fetched_files.append((path, content, truncated))

    outfile = write_snapshot(
        outdir=Path(args.outdir),
        target=target,
        repo_meta=repo_meta,
        ref=ref,
        commit=commit,
        tree_items=tree_items,
        selected_paths=selected_paths,
        fetched_files=fetched_files,
        topic=args.topic,
    )
    print(outfile)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
