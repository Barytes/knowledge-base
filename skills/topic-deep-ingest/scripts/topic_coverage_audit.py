#!/usr/bin/env python3
"""Audit topic-term coverage in wiki pages and the generated site search index."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)(#[^)]+)?\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def strip_fenced_code(text: str) -> str:
    return FENCE_RE.sub("", text)


def read_terms(path: Path) -> list[str]:
    terms: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        term = line.strip()
        if term and not term.startswith("#"):
            terms.append(term)
    return terms


def load_markdown(root: Path) -> list[tuple[Path, str]]:
    return [(path, path.read_text(encoding="utf-8")) for path in sorted(root.rglob("*.md"))]


def check_markdown_terms(
    pages: list[tuple[Path, str]], terms: list[str]
) -> dict[str, list[str]]:
    hits: dict[str, list[str]] = {}
    for term in terms:
        matched = [str(path) for path, text in pages if term in text or term in path.name]
        hits[term] = matched
    return hits


def check_search_terms(search_index: Path, terms: list[str]) -> dict[str, list[str]]:
    if not search_index.exists():
        return {term: [] for term in terms}

    entries = json.loads(search_index.read_text(encoding="utf-8"))
    hits: dict[str, list[str]] = {}
    for term in terms:
        matched: list[str] = []
        for entry in entries:
            haystack = " ".join(
                [
                    str(entry.get("title", "")),
                    str(entry.get("text", "")),
                    str(entry.get("url", "")),
                ]
            )
            if term in haystack:
                matched.append(str(entry.get("url", "")))
        hits[term] = matched
    return hits


def check_links(paths: list[Path]) -> list[tuple[str, str]]:
    missing: list[tuple[str, str]] = []
    for path in paths:
        text = strip_fenced_code(path.read_text(encoding="utf-8"))
        for match in LINK_RE.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if "://" in target or target.startswith("/"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                missing.append((str(path), target))
    return missing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--terms", required=True, type=Path)
    parser.add_argument("--search-index", type=Path)
    parser.add_argument(
        "--link-scope",
        choices=["root", "term-hit-pages"],
        default="term-hit-pages",
        help="Which markdown files to link-check.",
    )
    args = parser.parse_args()

    terms = read_terms(args.terms)
    pages = load_markdown(args.root)
    markdown_hits = check_markdown_terms(pages, terms)
    markdown_missing = [term for term, hits in markdown_hits.items() if not hits]

    search_missing: list[str] = []
    search_hits: dict[str, list[str]] = {}
    if args.search_index:
        search_hits = check_search_terms(args.search_index, terms)
        search_missing = [term for term, hits in search_hits.items() if not hits]

    if args.link_scope == "root":
        link_paths = [path for path, _ in pages]
    else:
        seen = {
            Path(path)
            for hits in markdown_hits.values()
            for path in hits
            if Path(path).exists()
        }
        link_paths = sorted(seen)

    missing_links = check_links(link_paths)

    print(f"terms_checked {len(terms)}")
    print(f"markdown_pages {len(pages)}")
    print(f"markdown_missing {markdown_missing}")
    if args.search_index:
        print(f"search_missing {search_missing}")
    print(f"link_checked_files {len(link_paths)}")
    print(f"missing_links {len(missing_links)}")
    for source, target in missing_links[:50]:
        print(f"missing_link {source} -> {target}")

    return 1 if markdown_missing or search_missing or missing_links else 0


if __name__ == "__main__":
    raise SystemExit(main())
