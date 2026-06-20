# Notebook Agent Guide

This directory is the user's personal draft notebook.

Agents may read files in this directory when the user explicitly asks about them, or when they are directly relevant context for a repository question.

Agents must not create, edit, rename, move, delete, format, lint, ingest into maintained wiki pages, normalize, reorganize, or otherwise write content files in this directory.

This directory may be synced to git and mirrored into the generated static site as a separate notebook navigation entry. That publishing path must preserve files as user-authored drafts rather than converting them into maintained wiki pages.

Do not include this directory in wiki ingest, link repair, cleanup, lint, normalization, or repository reorganization.

If a future task appears to require writing here, stop and ask the user to either edit the draft manually or explicitly change this directory policy first.
