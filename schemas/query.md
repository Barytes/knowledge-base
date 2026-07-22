# Query Schema

Use this schema when answering questions from the repository and deciding what to write back.

## Goal

Answer from the maintained wiki first, keep facts and judgment separate, and save durable work back into the repository.

When a query result is written back into `wiki/`, write the maintained page in Chinese by default. Keep paths, commands, code identifiers, repository names, and necessary technical terms in their original form when useful.

Default mode for repository-related questions is `knowledge-anchored`: start from the local knowledge base and use web search when it materially improves the answer.

## Query Routing

Route each question before synthesizing:

- factual or topic question -> read `wiki/topics/`
- self-modeling question -> read `wiki/self/`
- design, evaluation, comparison, or decision question -> read `wiki/frameworks/router.md` first, then the most relevant framework page, then pull in `wiki/topics/` as needed
- advisory or evaluative question with a concrete situational output -> synthesize through the most relevant topic under `wiki/topics/`

If the repository lacks enough material, say what is missing instead of faking confidence.

## Knowledge-Anchored Rule

For repository-related questions:

- read `wiki/index.md` first
- prefer `wiki/` over `raw/`
- browse the web when it materially improves freshness, correctness, or completeness
- do not let external search replace relevant local knowledge
- do not produce a purely web-derived answer unless local material is absent and external information is necessary to answer well

When local material is incomplete and external evidence is used, say:

1. what local pages were consulted
2. what is still missing
3. which parts of the answer are supported by external evidence

## Required Opening For Knowledge-Anchored Answers

For repository-related answers, start by listing the local pages or files actually consulted.

Preferred format:

- `Consulted local pages:`
- a flat list of specific `wiki/` or `raw/` paths

Do this before the main answer so the user can verify the answer really came from the repository.

## Answer Layers

When a response mixes evidence and judgment, keep the layers explicit:

1. What the material says.
2. What recurring user tendencies suggest.
3. What recommendation follows from combining the two.

Do not present user-specific judgment as if it were objective fact.

## Source Hierarchy

Prefer these sources in order:

1. directly relevant maintained wiki pages
2. raw source files when the wiki is incomplete
3. cautious synthesis based on the available evidence

Do not skip the wiki layer if it already contains the needed work.
Use web search as a supplement when useful, not as a substitute for relevant repository knowledge.

## Write-Back Rules

Write the result back into the repository when it is likely to be useful again.

Save to:

- `wiki/topics/` for factual syntheses, topic summaries, comparisons, recommendations, essays, and applied analyses
- `wiki/self/` for stable user judgment patterns derived from repeated evidence
- `wiki/frameworks/` for reusable judgment frameworks, compact router pages, and high-frequency entry surfaces

## Useful-Again Heuristic

Treat a result as "likely to be useful again" when it is not just correct for this turn, but likely to save future re-reading, re-synthesis, or repeated judgment.

Strong write-back signals include:

- the answer explains a concept, mechanism, workflow, or distinction that is likely to be asked again
- the answer compresses multiple source files or pages into one reusable synthesis
- the answer resolves an ambiguity or naming distinction that would otherwise recur
- the answer captures a durable recommendation for this repository or for the user's recurring projects
- the answer creates a bridge between existing pages that makes later navigation easier

Also write back when the current conversation itself produces a genuinely good insight, new finding, or reusable distinction that is likely to improve future judgment, navigation, or synthesis in the repository.

If only one weak signal is present, prefer leaving the result in chat unless the user explicitly asks to save it.

## Do Not Write Back

Do not create a new page when the output is:

- a one-off chat answer with no reuse value
- redundant with an existing page
- based on weak or ambiguous personal evidence
- highly time-sensitive and likely to go stale quickly
- temporary task status, progress chatter, or narrow operational output
- really a concrete memo that should update an existing topic page instead of spawning another framework page

Update an existing page instead whenever possible.

When deciding between `wiki/frameworks/` and `wiki/topics/`, use this distinction:

- `wiki/frameworks/` answers “what lens or routing surface should future queries start from?”
- `wiki/topics/` answers “what does this topic contain, and what concrete conclusion follows in this case after combining knowledge and judgment?”

## Web Supplement

Web search is appropriate when one of these is true:

- the user asks to search online or asks for current public information
- the answer depends on time-sensitive or externally verifiable facts
- external primary sources would materially improve accuracy, completeness, or source attribution
- the repository exposes a material gap that can be filled responsibly from the web

When web search is used, explicitly label which parts came from outside the repository. Preserve the local knowledge base as the main interpretive context whenever it contains relevant material. A purely web-derived answer is acceptable only when local material is absent and external information is necessary; say so explicitly.

## Query Logging

Append a `query` entry to `wiki/log.md` when a question produces a durable page or materially updates an existing one.
