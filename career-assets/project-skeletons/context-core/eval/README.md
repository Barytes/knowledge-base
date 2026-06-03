# context-core eval

The first eval suite should be small and explainable.

## Case Format

Each case should include:

- `task`
- `user_context`
- `expected_sources`
- `expected_behavior`
- `scoring_fields`
- `failure_labels`

## Initial Scoring Fields

| Field | Question |
|---|---|
| `grounding` | Did the answer use the right local sources? |
| `routing_relevance` | Were selected context units actually relevant? |
| `layer_separation` | Did it separate facts, user-specific judgment, and recommendation? |
| `next_step_quality` | Did it produce a concrete useful next action? |
| `writeback_fit` | If it proposes a durable update, is the target layer correct? |

## Initial Failure Labels

- `missing_source`
- `wrong_layer`
- `overbroad_context`
- `unsupported_claim`
- `generic_advice`
- `no_next_step`
- `bad_writeback_target`

