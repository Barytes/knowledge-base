---
name: kb-query
description: Answer repository questions with relevant local knowledge as the default interpretive context and web search whenever it improves the result.
---

# KB Query

## Goal

Give an evidence-grounded answer that benefits from the maintained knowledge base without treating it as a closed world.

## Evidence Contract

- Consult relevant maintained wiki pages; use raw evidence when the maintained layer is incomplete or needs verification.
- Web search is allowed and may be used proactively for freshness, correctness, completeness, verification, primary-source attribution, or a material local gap.
- When web evidence is used, cite it and keep it distinguishable from local material and agent inference.
- If the repository has no relevant material, an externally grounded answer is acceptable; say so when the gap matters.
- Preserve the distinction between world facts, recurring user judgment, and recommendations.

No fixed reading order, opening, or answer shape is required. Choose the research method and presentation that best serve the question. Follow `schemas/query.md` for write-back authority; queries are read-only unless repository changes are requested.
