# oh-share-it eval layer

This skeleton turns `oh-share-it` into a real trial and evaluation surface for `context-core`.

## Purpose

`oh-share-it` should prove that shared research knowledge can become agent-usable context without collapsing into a generic shared folder.

The strongest signal is not "it stores notes." The strongest signal is:

> Real users ask research questions, the system routes maintained context, answers are grounded, failures are visible, and useful discoveries are written back.

## V0 Trial

Pick one research direction or lab project.

Collect 15-20 questions:

- onboarding questions
- idea-screening questions
- literature-positioning questions
- method-comparison questions
- "what should I read next?" questions

For each question, record:

- who asked it
- scenario
- expected sources
- answer usefulness
- failure labels

## Suggested Tree

```text
oh-share-it/
  eval/
    cases/
      001-onboarding.yaml
      002-method-comparison.yaml
    reports/
      first-trial.md
    rubrics/
      answer-quality.md
      routing-quality.md
  docs/
    trial-plan.md
    deployment-note.md
    route-quality-report.md
```

## Trial Success Criteria

Minimum credible signal:

- 15 real or semi-real questions.
- At least 5 answers grounded in maintained wiki pages.
- At least 5 routing failures labeled and explained.
- At least 3 writeback candidates reviewed by a human.
- One short case study showing how a failure improved the system.

## Resume Bullet Draft

Designed and evaluated a shared research context layer for agent-assisted knowledge work, using 15-20 real research questions, route-quality checks, grounding rubrics, and writeback review to expose failures and improve maintained knowledge assets.

