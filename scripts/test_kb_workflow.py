#!/usr/bin/env python3
"""Lightweight regression checks for the knowledge base ingest workflow."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from reorganize_wiki import redact_private_lines


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
        ROOT / "schemas" / "ingest.md",
        ROOT / "skills" / "kb-ops" / "SKILL.md",
        ROOT / "skills" / "kb-ops" / "scripts" / "README.md",
    ]
    for path in docs:
        text = path.read_text(encoding="utf-8")
        assert_contains(text, "wiki/site", str(path.relative_to(ROOT)))
        assert_contains_any(text, ["自动", "automatic", "regenerat"], str(path.relative_to(ROOT)))


def active_prompt_and_control_files() -> list[Path]:
    files = [
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / "COMMUNICATION.md",
        ROOT / "README.md",
        ROOT / "notebook" / "AGENTS.md",
        ROOT / "skills" / "README.md",
        ROOT / "skills" / "repo-map-ingest" / "references" / "output-template.md",
        ROOT / "skills" / "kb-ops" / "scripts" / "kb-ingest.sh",
        ROOT / "skills" / "repo-map-ingest" / "scripts" / "github_repo_ingest.py",
        ROOT / "skills" / "repo-map-ingest" / "scripts" / "repo_map_from_snapshot.py",
    ]
    files.extend(sorted((ROOT / "schemas").glob("*.md")))
    files.extend(sorted((ROOT / "skills").glob("*/SKILL.md")))
    files.extend(sorted((ROOT / "skills").glob("*/agents/openai.yaml")))
    return files


def test_prompt_policy_has_one_global_source() -> None:
    if (ROOT / "schemas" / "AGENTS.md").exists():
        raise AssertionError("AGENTS.md should be the only global repository policy source")
    if (ROOT / "skills" / "action-coach" / "gemini-gem-prompt.md").exists():
        raise AssertionError("action-coach should not maintain a duplicate platform prompt")


def test_active_prompts_do_not_target_retired_layers() -> None:
    retired = ["wiki/knowledge", "wiki/bridges"]
    for path in active_prompt_and_control_files():
        text = path.read_text(encoding="utf-8")
        for value in retired:
            if value in text:
                raise AssertionError(f"{path.relative_to(ROOT)} targets retired layer {value!r}")


def test_local_evidence_policy_allows_web_search() -> None:
    policy_files = [
        ROOT / "AGENTS.md",
        ROOT / "schemas" / "query.md",
        ROOT / "skills" / "kb-query" / "SKILL.md",
    ]
    for path in policy_files:
        text = path.read_text(encoding="utf-8").lower()
        assert_contains(text, "web search", str(path.relative_to(ROOT)))
        assert_contains_any(text, ["allowed", "proactively"], str(path.relative_to(ROOT)))


def test_launcher_prompts_only_invoke_their_skill() -> None:
    for path in sorted((ROOT / "skills").glob("*/agents/openai.yaml")):
        skill_name = path.parents[1].name
        text = path.read_text(encoding="utf-8")
        expected = f'default_prompt: "Use ${skill_name}."'
        assert_contains(text, expected, str(path.relative_to(ROOT)))


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


def test_private_path_redaction_keeps_non_source_mentions() -> None:
    text = "\n".join(
        [
            "本页只整理 `notebook/` 草稿，不混入 `life-record/` 访谈记录。",
            "- `life-record/陈子深- AI教育产品定义.md`",
        ]
    )

    redacted = redact_private_lines(text)
    expected = "\n".join(
        [
            "本页只整理 `notebook/` 草稿，不混入 `life-record/` 访谈记录。",
            "- 私密记录路径已隐藏。",
        ]
    )
    if redacted != expected:
        raise AssertionError(f"unexpected redaction output: {redacted!r}")


def main() -> None:
    tests = [
        test_kb_ingest_uses_repo_root,
        test_kb_ingest_exposes_site_refresh,
        test_ingest_docs_require_site_refresh,
        test_prompt_policy_has_one_global_source,
        test_active_prompts_do_not_target_retired_layers,
        test_local_evidence_policy_allows_web_search,
        test_launcher_prompts_only_invoke_their_skill,
        test_topics_config_is_externalized,
        test_site_search_indexes_all_maintained_pages,
        test_site_exposes_notebook_but_not_life_record,
        test_private_path_redaction_keeps_non_source_mentions,
    ]
    for test in tests:
        test()
    print(f"{len(tests)} kb workflow checks passed")


if __name__ == "__main__":
    main()
