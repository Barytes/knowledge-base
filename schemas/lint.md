# Lint Contract

Use this contract for repository cleanup and structural maintenance.

## Safety

- Be conservative with substantive content. Do not delete it unless the target and surviving source are clear.
- Do not modify `notebook/`, publish or index `life-record/`, or rewrite `raw/` evidence.
- Move genuinely uncertain material to `inbox/` rather than inventing a classification.
- Preserve historical entries in `wiki/log.md` even when they mention old paths.

## Repository Invariants

- Maintained topic, self, and framework pages belong in their corresponding `wiki/` layers.
- Maintained prose defaults to Chinese unless the user requests otherwise.
- Maintained pages should remain reachable through navigation or meaningful cross-links.
- Renames and removals require repairing active inbound links.
- Duplicate pages should be merged only when one clearly subsumes the other; partial overlap should usually be linked.
- Active prompts, tools, and documentation must not target retired wiki directories or contradict the canonical policy in `AGENTS.md`.

## Completion

Choose checks based on the requested scope. For meaningful maintenance changes, update the relevant log or navigation, regenerate `wiki/site/`, run applicable deterministic tests, and report residual uncertainty.

The checks may be performed in any effective order unless a change has a real dependency or safety precondition.
