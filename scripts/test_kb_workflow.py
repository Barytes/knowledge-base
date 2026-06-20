#!/usr/bin/env python3
"""Lightweight regression checks for the knowledge base ingest workflow."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def assert_contains(text: str, expected: str, context: str) -> None:
    if expected not in text:
        raise AssertionError(f"{context}: expected to find {expected!r}")


def assert_contains_any(text: str, expected: list[str], context: str) -> None:
    lowered = text.lower()
    if not any(item.lower() in lowered for item in expected):
        raise AssertionError(f"{context}: expected to find one of {expected!r}")


def test_kb_ingest_uses_repo_root() -> None:
    result = run(["./skills/kb-ops/scripts/kb-ingest.sh", "list"])
    if result.returncode != 0:
        raise AssertionError(result.stdout)
    if "inbox 目录不存在" in result.stdout:
        raise AssertionError("kb-ingest.sh should resolve inbox/ from the repository root")


def test_kb_ingest_exposes_site_refresh() -> None:
    result = run(["./skills/kb-ops/scripts/kb-ingest.sh", "help"])
    if result.returncode != 0:
        raise AssertionError(result.stdout)
    assert_contains(result.stdout, "site", "kb-ingest.sh help")
    assert_contains(result.stdout, "重新生成", "kb-ingest.sh help")


def test_ingest_docs_require_site_refresh() -> None:
    docs = [
        ROOT / "AGENTS.md",
        ROOT / "schemas" / "AGENTS.md",
        ROOT / "schemas" / "ingest.md",
        ROOT / "skills" / "kb-ops" / "SKILL.md",
        ROOT / "skills" / "kb-ops" / "scripts" / "README.md",
    ]
    for path in docs:
        text = path.read_text(encoding="utf-8")
        assert_contains(text, "wiki/site", str(path.relative_to(ROOT)))
        assert_contains_any(text, ["自动", "automatic"], str(path.relative_to(ROOT)))


def test_topics_config_is_externalized() -> None:
    config_path = ROOT / "wiki" / "topics" / "topics.json"
    if not config_path.exists():
        raise AssertionError("topic metadata should live in wiki/topics/topics.json")

    config = json.loads(config_path.read_text(encoding="utf-8"))
    topics = config.get("topics")
    if not isinstance(topics, list) or not topics:
        raise AssertionError("wiki/topics/topics.json should contain a non-empty topics list")

    first = topics[0]
    for key in ["slug", "title", "summary"]:
        if key not in first:
            raise AssertionError(f"topic entries should include {key!r}")


def test_site_search_indexes_all_maintained_pages() -> None:
    result = run(["./skills/kb-ops/scripts/kb-ingest.sh", "site"])
    if result.returncode != 0:
        raise AssertionError(result.stdout)

    site = ROOT / "wiki" / "site"
    search_index_path = site / "search-index.json"
    search_page_path = site / "search.html"
    search_script_path = site / "search.js"

    for path in [search_index_path, search_page_path, search_script_path]:
        if not path.exists():
            raise AssertionError(f"site search should generate {path.relative_to(ROOT)}")

    index = json.loads(search_index_path.read_text(encoding="utf-8"))
    if not isinstance(index, list) or len(index) < 20:
        raise AssertionError("site search index should cover maintained pages across the wiki")

    required_fields = {"title", "url", "path", "layer", "summary", "body"}
    for entry in index:
        if not isinstance(entry, dict) or not required_fields.issubset(entry):
            raise AssertionError(f"search index entry missing fields: {entry!r}")

    def matching_titles(keyword: str) -> list[str]:
        lowered = keyword.lower()
        return [
            entry["title"]
            for entry in index
            if lowered in f"{entry['title']} {entry['summary']} {entry['body']}".lower()
        ]

    munger_hits = matching_titles("latticework")
    if "穷查理宝典" not in munger_hits:
        raise AssertionError("search should find 穷查理宝典 by a body keyword")

    runtime_hits = matching_titles("Claude Code")
    if not any("Claude Code" in title for title in runtime_hits):
        raise AssertionError("search should find a different page by another keyword")

    index_html = (site / "index.html").read_text(encoding="utf-8")
    assert_contains(index_html, "search.html", "site home navigation")


def test_site_exposes_notebook_but_not_life_record() -> None:
    result = run(["./skills/kb-ops/scripts/kb-ingest.sh", "site"])
    if result.returncode != 0:
        raise AssertionError(result.stdout)

    site = ROOT / "wiki" / "site"
    notebook_layer = site / "layers" / "notebook.html"
    notebook_page = site / "content" / "notebook" / "founder-skill.html"
    search_index_path = site / "search-index.json"

    for path in [notebook_layer, notebook_page, search_index_path]:
        if not path.exists():
            raise AssertionError(f"notebook site output should generate {path.relative_to(ROOT)}")

    index_html = (site / "index.html").read_text(encoding="utf-8")
    layer_html = notebook_layer.read_text(encoding="utf-8")
    search_index_text = search_index_path.read_text(encoding="utf-8")

    assert_contains(index_html, "layers/notebook.html", "site home notebook navigation")
    assert_contains(layer_html, "notebook/founder-skill.md", "notebook layer listing")
    assert_contains(search_index_text, "notebook/founder-skill.md", "search index notebook coverage")
    if "life-record/" in search_index_text:
        raise AssertionError("life-record must stay out of the generated search index")


def main() -> None:
    tests = [
        test_kb_ingest_uses_repo_root,
        test_kb_ingest_exposes_site_refresh,
        test_ingest_docs_require_site_refresh,
        test_topics_config_is_externalized,
        test_site_search_indexes_all_maintained_pages,
        test_site_exposes_notebook_but_not_life_record,
    ]
    for test in tests:
        test()
    print(f"{len(tests)} kb workflow checks passed")


if __name__ == "__main__":
    main()
