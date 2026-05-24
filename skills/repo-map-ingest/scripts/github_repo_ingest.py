#!/usr/bin/env python3
"""One-shot GitHub repo ingest: raw snapshot plus maintained repo map."""

from __future__ import annotations

import argparse
from datetime import datetime
import os
from pathlib import Path

import github_repo_snapshot
import repo_map_from_snapshot


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="抓取 GitHub 仓库 snapshot，并生成维护过的仓库地图。"
    )
    parser.add_argument("repo_url", help="GitHub repository URL")
    parser.add_argument(
        "--raw-outdir",
        default="raw/external",
        help="Destination for the raw snapshot markdown",
    )
    parser.add_argument(
        "--wiki-outdir",
        default="wiki/knowledge",
        help="Destination for the maintained repo map note",
    )
    parser.add_argument(
        "--ref",
        default=None,
        help="Branch, tag, or commit to inspect",
    )
    parser.add_argument(
        "--topic",
        default="仓库架构与工程实践",
        help="记录在输出中的研究主题",
    )
    parser.add_argument(
        "--index-path",
        default="wiki/index.md",
        help="Index file to update after generating the repo map",
    )
    parser.add_argument(
        "--log-path",
        default="wiki/log.md",
        help="Log file to append after generating the repo map",
    )
    parser.add_argument(
        "--skip-index-update",
        action="store_true",
        help="Do not update the index file",
    )
    parser.add_argument(
        "--skip-log-update",
        action="store_true",
        help="Do not append a log entry",
    )
    return parser.parse_args()


def build_index_bullet(target: github_repo_snapshot.RepoTarget, note_path: Path, index_path: Path, topic: str) -> str:
    relative_note = os.path.relpath(note_path, index_path.parent)
    topic_text = topic.strip()
    if topic_text == "仓库架构与工程实践":
        description = f"`{target.owner}/{target.repo}` 的第一版仓库地图，覆盖架构、证据锚点与关键工程机制。"
    else:
        description = f"`{target.owner}/{target.repo}` 的第一版仓库地图，聚焦主题“{topic_text}”。"
    return f"- [{target.owner}/{target.repo} 仓库地图]({relative_note}): {description}"


def update_index(index_path: Path, target: github_repo_snapshot.RepoTarget, note_path: Path, topic: str) -> None:
    if not index_path.exists():
        return

    text = index_path.read_text(encoding="utf-8")
    bullet = build_index_bullet(target, note_path, index_path, topic)
    marker = f"[{target.owner}/{target.repo} 仓库地图]"

    if marker in text:
        lines = text.splitlines()
        updated_lines = [bullet if marker in line else line for line in lines]
        index_path.write_text("\n".join(updated_lines).rstrip() + "\n", encoding="utf-8")
        return

    knowledge_heading = "## 知识\n" if "## 知识\n" in text else "## Knowledge\n"
    self_heading = "\n## 自我\n" if "\n## 自我\n" in text else "\n## Self\n"
    if knowledge_heading not in text or self_heading not in text:
        return

    start = text.index(knowledge_heading) + len(knowledge_heading)
    end = text.index(self_heading, start)
    knowledge_block = text[start:end].rstrip("\n")
    if knowledge_block:
        knowledge_block = knowledge_block + "\n" + bullet + "\n"
    else:
        knowledge_block = bullet + "\n"
    new_text = text[:start] + knowledge_block + text[end:]
    index_path.write_text(new_text.rstrip() + "\n", encoding="utf-8")


def append_log(log_path: Path, target: github_repo_snapshot.RepoTarget, snapshot_path: Path, note_path: Path, topic: str) -> None:
    if not log_path.exists():
        return

    date = datetime.now().strftime("%Y-%m-%d")
    try:
        snapshot_rel = snapshot_path.resolve().relative_to(Path.cwd().resolve())
    except Exception:
        snapshot_rel = snapshot_path
    try:
        note_rel = note_path.resolve().relative_to(Path.cwd().resolve())
    except Exception:
        note_rel = note_path

    entry = (
        f"\n## [{date}] 摄取 | {target.owner}/{target.repo} 仓库地图\n\n"
        f"把紧凑的 GitHub 仓库 snapshot 抓取到 `{snapshot_rel}`，并围绕主题“{topic}”在 `{note_rel}` 生成了初始维护页。\n"
    )
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(entry)


def main() -> int:
    args = parse_args()
    target = github_repo_snapshot.parse_repo_url(args.repo_url, args.ref)
    repo_meta = github_repo_snapshot.fetch_repo_metadata(target)
    ref = target.ref or repo_meta.get("default_branch")
    if not ref:
        raise SystemExit("Could not determine repository ref")
    commit = github_repo_snapshot.fetch_commit(target, ref)
    tree = github_repo_snapshot.fetch_tree(target, ref)

    tree_items = tree.get("tree", [])
    tree_paths = [item["path"] for item in tree_items if item.get("type") == "blob"]
    selected_paths = github_repo_snapshot.select_paths(tree_paths)

    fetched_files = []
    for path in selected_paths:
        try:
            content, truncated = github_repo_snapshot.fetch_file_content(target, path, ref)
        except Exception as exc:  # pragma: no cover - best effort capture
            content = f"[failed to fetch file content: {exc}]"
            truncated = False
        fetched_files.append((path, content, truncated))

    snapshot_path = github_repo_snapshot.write_snapshot(
        outdir=Path(args.raw_outdir),
        target=target,
        repo_meta=repo_meta,
        ref=ref,
        commit=commit,
        tree_items=tree_items,
        selected_paths=selected_paths,
        fetched_files=fetched_files,
        topic=args.topic,
    )

    note_path = repo_map_from_snapshot.generate_note(
        snapshot_path=snapshot_path,
        outdir=Path(args.wiki_outdir),
        topic_override=args.topic,
    )

    index_path = Path(args.index_path)
    log_path = Path(args.log_path)
    if not args.skip_index_update:
        update_index(index_path, target, note_path, args.topic)
    if not args.skip_log_update:
        append_log(log_path, target, snapshot_path, note_path, args.topic)

    print(snapshot_path)
    print(note_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
