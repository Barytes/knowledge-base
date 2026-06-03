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


def main() -> None:
    tests = [
        test_kb_ingest_uses_repo_root,
        test_kb_ingest_exposes_site_refresh,
        test_ingest_docs_require_site_refresh,
        test_topics_config_is_externalized,
    ]
    for test in tests:
        test()
    print(f"{len(tests)} kb workflow checks passed")


if __name__ == "__main__":
    main()
