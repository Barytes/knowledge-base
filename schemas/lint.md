# Lint Schema

Use this schema for repository cleanup and maintenance.

## Goal

Keep the repository aligned with the current directory design, prevent content drift, and keep the maintained wiki navigable.

During cleanup, preserve the repository rule that maintained wiki pages under `wiki/` default to Chinese.

## Safety Rule

Be conservative.

- Do not delete substantive content unless it is clearly duplicate junk and the surviving copy is obvious.
- If the right destination is unclear, move the item to `inbox/` instead of guessing.
- Safe clutter such as `.DS_Store` and empty temporary directories may be removed.

## Lint Pass Order

Run lint in this order:

1. inventory files
2. reclassify mislocated content
3. remove obvious clutter
4. detect orphan pages
5. detect duplicate pages
6. detect and clean up references to deleted pages
7. normalize maintained wiki language to Chinese when needed
8. update indexes, links, and log entries

## Reclassification Rules

Move files to match the active directory plan:

- external source files should live in `raw/external/` or `inbox/`
- personal source files should live in `raw/personal/`
- maintained knowledge pages should live in `wiki/knowledge/`
- maintained self pages should live in `wiki/self/`
- mixed analysis pages should live in `wiki/bridges/`

If a file is clearly in the wrong top-level area, move it before doing deeper maintenance.

## Orphan Detection

Treat these as intentional roots, not orphans:

- `README.md`
- `wiki/index.md`
- `wiki/log.md`

For maintained pages in `wiki/knowledge/`, `wiki/self/`, and `wiki/bridges/`:

- each page should be linked from at least one index page or another maintained page
- if a page has no inbound path, add links or move it to `inbox/`

## Duplicate Detection

Check for likely duplicates using:

- same or nearly identical filenames
- same page title
- strongly overlapping headings or summaries
- one page fully subsuming another

When two pages are truly duplicates:

1. keep the clearer or more complete page
2. merge missing useful details if needed
3. remove or archive the weaker duplicate
4. repair links

When overlap is partial, link the pages instead of merging them.

## Deleted Page Reference Cleanup

After deleting a wiki page, scan all remaining `.md` files under `wiki/` for inbound links to the deleted file.

For each reference found:

1. **log.md**: keep as-is (historical record of queries/ingest operations)
2. **index pages** (e.g., `wiki/index.md`): remove or update the entry
3. **maintenance pages**: remove the reference from "相关页面" sections, or retarget to a surviving related page if appropriate
4. **content references in body text**: either remove the link (keep text), or rewrite to reference a related surviving page

When a deleted page is renamed (not truly deleted), update all links to point to the new filename.

## Wiki Language Normalization

Treat English-first maintained wiki pages under `wiki/` as a cleanup target.

When lint finds a maintained page whose main narrative content is still primarily in English:

1. keep the same file path unless there is a separate naming problem
2. preserve page structure, links, evidence anchors, and layer boundaries
3. rewrite the maintained narrative into Chinese
4. keep file paths, repository names, commands, code identifiers, direct quotes, and necessary technical terms in their original form when helpful
5. do not translate raw source files under `raw/`

Be conservative in these cases:

- if the page is intentionally bilingual, preserve that intent
- if the page contains source quotations, keep quotations minimal and faithful
- if the page is mostly identifiers or code-like content, normalize only the explanatory prose

## Index And Log Repair

After a lint pass:

- update `wiki/index.md` if major destinations changed
- repair broken internal links
- append a `lint` entry to `wiki/log.md`

## Current Repository Checks

When linting this repository, always check for:

- source files placed directly under `raw/` instead of its subfolders
- generated pages that are not under `wiki/`
- stale placeholder files in `skills/`
- unlinked pages under `wiki/bridges/essays/`
- English-first maintained pages under `wiki/knowledge/`, `wiki/self/`, and `wiki/bridges/`
