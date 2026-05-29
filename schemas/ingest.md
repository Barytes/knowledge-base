# Ingest Schema

Use this schema when classifying and compiling new material into the repository.

## Goal

Turn new source material into maintained wiki pages without mixing raw evidence, world knowledge, and personal judgment.

All maintained wiki outputs should default to Chinese, while preserving original file paths, repository names, commands, code identifiers, and necessary technical terms.

## Intake Order

Process new materials in this order:

1. Read the source file.
2. Identify whether it is `external`, `personal`, or `mixed`.
3. Place or move the source into the correct raw or inbox location if needed.
4. Update the correct wiki layer.
5. Append a short note to `wiki/log.md`.

## Source Classification

Classify sources by evidence type:

- `external`: articles, papers, reports, clips, books, meeting notes from outside sources
- `personal`: journals, conversations, drafts, work logs, decision notes, user-authored reflections
- `mixed`: writing that combines outside materials with the user's own judgment

When unsure, keep the original file in `raw/` or `inbox/` and place the derived page in the most relevant topic under `wiki/topics/`.

## Correct Source Locations

Use these default locations:

- external source files -> `raw/external/`
- personal writing -> `raw/personal/writings/`
- personal conversations or transcripts -> `raw/personal/conversations/`
- ambiguous or unprocessed material -> `inbox/`
- uncertain generated pages -> `inbox/`

## External Ingest

For an `external` source:

1. Preserve the source in `raw/external/`.
2. Look for an existing page in `wiki/topics/` that should be updated.
3. If no good target exists, create a new topic page or source summary under the closest `wiki/topics/<topic>/`.
4. Capture:
   - what the source is about
   - key claims or takeaways
   - important tensions, caveats, or contradictions
   - links to related knowledge pages
5. Prefer updating over creating duplicates.

## Personal Ingest

For a `personal` source:

1. Preserve the source in `raw/personal/`.
2. Extract one or more observations.
3. Compare those observations against existing self pages.
4. Promote to higher-level pages only when the evidence is stable.

Use this promotion ladder:

- observation -> one useful signal
- pattern -> repeated signal across time or context
- axiom -> stable decision principle with strong support

Never jump from a single source directly to a strong axiom unless the user explicitly asks for a speculative draft.

## Mixed Ingest

For a `mixed` source:

1. Preserve the original file in the correct raw folder if it is source evidence.
2. Extract any world-facing knowledge into `wiki/topics/` when it has durable value.
3. Extract any recurring user judgment into `wiki/self/` only if supported by repeated evidence.
4. Save the integrated interpretation in the relevant topic under `wiki/topics/`.

## Topic Essay Re-Distillation

Essay-like pages under `wiki/topics/` may be revisited as secondary evidence for `wiki/self/`, but they should not be treated as raw evidence.

Use this workflow:

1. Treat the essay as evidence of how the user frames, compares, and expresses ideas, not as direct proof of a stable axiom.
2. Extract low-level self signals first, especially:
   - recurring abstractions or framing moves
   - repeated comparison habits
   - stable-looking writing tendencies
   - consistent ways of defining tradeoffs, criteria, or default work surfaces
3. Save those signals to `wiki/self/` as `observation` by default.
4. Promote to `pattern` only when the same tendency appears across multiple bridge essays, or across a bridge essay plus independent personal evidence in `raw/personal/`.
5. Do not promote from a single bridge essay directly to `axiom`.

Treat writing-style evidence conservatively:

- one topic essay can justify a writing-style observation
- multiple essays or essays plus personal writing are needed for a writing-style pattern
- style preferences should stay separate from factual conclusions about the outside world

When useful, a topic essay may therefore produce two outputs at once:

- the essay remains under the relevant `wiki/topics/<topic>/`
- a new or updated `wiki/self/` page captures repeated judgment or expression signals exposed by that essay

## Naming And Linking

- Prefer short, stable filenames based on topic rather than date-only filenames.
- Add at least one link from a maintained page to another maintained page.
- Update `wiki/index.md` when a new durable page changes the shape of the repository.

## Logging

Append one short entry to `wiki/log.md` for every meaningful ingest or reclassification.

Use:

- `ingest` for new source compilation
- `reflection` for self distillation
- `lint` for reclassification or cleanup
