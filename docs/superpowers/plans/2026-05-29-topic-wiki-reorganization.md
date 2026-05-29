# Topic Wiki Reorganization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganize `wiki/knowledge/` and `wiki/bridges/` into topic directories, keep `wiki/self/` and `wiki/frameworks/`, and generate a static HTML site for topic and layer browsing.

**Architecture:** Markdown remains the source of truth. A Python script owns the migration mapping, repairs internal Markdown links after moving pages, writes topic `index.md` files, rewrites `wiki/index.md`, and generates `wiki/site/` HTML views from the reorganized wiki.

**Tech Stack:** Python standard library, Markdown files, generated static HTML/CSS.

---

### Task 1: Add Reorganization Script

**Files:**
- Create: `scripts/reorganize_wiki.py`
- Modify: `docs/superpowers/plans/2026-05-29-topic-wiki-reorganization.md`

- [ ] **Step 1: Create `scripts/reorganize_wiki.py`**

The script defines topic metadata, maps every non-README page from `wiki/knowledge/`, `wiki/bridges/`, and `wiki/bridges/essays/` into `wiki/topics/<topic>/`, and uses `pathlib`, `re`, `html`, and `urllib.parse` from the standard library.

- [ ] **Step 2: Implement link rewriting**

For each Markdown file under `wiki/`, the script resolves local `.md` links against the file's old path, looks up moved targets, and rewrites the link relative to the file's new path. Links to `raw/`, `self/`, and `frameworks/` must remain valid.

- [ ] **Step 3: Implement generated indexes and HTML**

The script writes:
- `wiki/topics/<topic>/index.md`
- `wiki/topics/index.md`
- `wiki/index.md`
- `wiki/site/index.html`
- `wiki/site/topics/<topic>.html`
- `wiki/site/layers/topics.html`
- `wiki/site/layers/self.html`
- `wiki/site/layers/frameworks.html`

### Task 2: Run Migration

**Files:**
- Move: `wiki/knowledge/*.md` into `wiki/topics/**`
- Move: `wiki/bridges/*.md` into `wiki/topics/**`
- Move: `wiki/bridges/essays/*.md` into `wiki/topics/context-memory-knowledge-system/essays/`
- Keep: `wiki/self/**`
- Keep: `wiki/frameworks/**`

- [ ] **Step 1: Run `python3 scripts/reorganize_wiki.py`**

Expected result: topic directories are created, old `wiki/knowledge/` and `wiki/bridges/` content pages are moved, topic indexes are generated, and static HTML is written.

- [ ] **Step 2: Inspect `git status --short`**

Expected result: file moves show as deletions plus additions or renames; existing user edits remain represented in the moved files.

### Task 3: Verify Links And Site

**Files:**
- Read: all generated `wiki/**/*.md`
- Read: all generated `wiki/site/**/*.html`

- [ ] **Step 1: Run link check**

Run a local Python link checker over Markdown links under `wiki/`. Expected result: no broken local `.md` links except historical `wiki/log.md` links if any stale paths are retained as historical records.

- [ ] **Step 2: Run HTML smoke check**

Check that all generated HTML files exist and contain links to their expected Markdown sources.

- [ ] **Step 3: Review top-level navigation**

Read `wiki/index.md` and `wiki/topics/index.md`. Expected result: `wiki/index.md` links to every topic index, plus `self/`, `frameworks/`, `wiki/site/index.html`, and `log.md`.

