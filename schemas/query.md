# Query Contract

Use this contract for repository-grounded questions and evaluations.

## Evidence Policy

Relevant maintained wiki material is the default interpretive context, not an exclusive source. Prefer `wiki/` over `raw/` when the maintained layer already answers the question; use raw evidence when the wiki is incomplete or a claim needs verification.

Web search is allowed and may be used proactively when it improves freshness, correctness, completeness, verification, or source attribution. It is especially appropriate for current information, externally verifiable claims, named sources, or material local gaps.

When external evidence is used:

- cite the external sources
- distinguish external evidence from local knowledge and agent inference
- state material local gaps when they affect the conclusion

If local material is absent, the answer may be primarily externally grounded. Do not force a local interpretation where none exists.

## Judgment Boundaries

- Keep source facts, inferred patterns, agent synthesis, and user-specific judgment distinguishable.
- Do not present a personal preference as an objective fact.
- Preserve uncertainty instead of inventing confidence.
- Use `wiki/topics/`, `wiki/self/`, and `wiki/frameworks/` according to the ownership rules in `AGENTS.md`; routing is contextual rather than a fixed reading sequence.

## Output And Write-Back

Choose the response structure and level of detail that best serves the question. Mention or link the evidence needed to make the answer inspectable, but no fixed opening or answer template is required.

Queries are read-only by default. Write back only when the user requests repository changes or the active task explicitly includes maintenance. When authorized, update the smallest appropriate existing page and append a `query` entry to `wiki/log.md` for a durable change.
