---
title: "GitHub repo snapshot: openclaw/openclaw"
source: "https://github.com/openclaw/openclaw"
author:
published:
created: 2026-04-12
description: "Compact GitHub repository evidence snapshot for repo-map-ingest."
tags:
  - "github"
  - "repo-snapshot"
---

# GitHub Repo Snapshot: `openclaw/openclaw`

## Observation Scope

- Repository: `openclaw/openclaw`
- URL: https://github.com/openclaw/openclaw
- Requested topic: 个人 AI assistant、Gateway 与持续身份层
- Observed ref: `main`
- Latest resolved commit: `f2c7cec8de2c7c5867f126b93fec3349c5cbe385`
- Commit date: `2026-04-12T09:53:47Z`
- Snapshot date (UTC): `2026-04-12`

## Repository Metadata

- Description: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 
- Default branch: `main`
- Language: `TypeScript`
- Stars: `355268`
- Forks: `71885`
- Open issues: `18208`

## Top-Level Tree

### Directories

- `.agents`
- `.github`
- `.pi`
- `.vscode`
- `Swabble`
- `apps`
- `assets`
- `docs`
- `extensions`
- `git-hooks`
- `packages`
- `patches`
- `qa`
- `scripts`
- `skills`
- `src`
- `test`
- `test-fixtures`
- `ui`
- `vendor`

### Files

- `.codex`
- `.detect-secrets.cfg`
- `.dockerignore`
- `.env.example`
- `.gitattributes`
- `.gitignore`
- `.jscpd.json`
- `.mailmap`
- `.markdownlint-cli2.jsonc`
- `.npmignore`
- `.npmrc`
- `.oxfmtrc.jsonc`
- `.oxlintrc.json`
- `.pre-commit-config.yaml`
- `.prettierignore`
- `.secrets.baseline`
- `.shellcheckrc`
- `.swiftformat`
- `.swiftlint.yml`
- `AGENTS.md`
- `CHANGELOG.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `Dockerfile`
- `Dockerfile.sandbox`
- `Dockerfile.sandbox-browser`
- `Dockerfile.sandbox-common`
- `INCIDENT_RESPONSE.md`
- `LICENSE`
- `Makefile`
- `README.md`
- `SECURITY.md`
- `VISION.md`
- `appcast.xml`
- `docker-compose.yml`
- `docker-setup.sh`
- `docs.acp.md`
- `dream-diary-preview-v2.html`
- `dream-diary-preview-v3.html`
- `fix2.py`
- `fly.private.toml`
- `fly.toml`
- `knip.config.ts`
- `openclaw.mjs`
- `openclaw.podman.env`
- `package.json`
- `pnpm-lock.yaml`
- `pnpm-workspace.yaml`
- `pyproject.toml`
- `render.yaml`
- `setup-podman.sh`
- `tsconfig.json`
- `tsconfig.oxlint.json`
- `tsconfig.plugin-sdk.dts.json`
- `tsdown.config.ts`
- `vitest.config.ts`
- `zizmor.yml`

## Selected Evidence Anchors

- `.github/workflows/auto-response.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/control-ui-locale-refresh.yml`
- `.github/workflows/docker-release.yml`
- `.github/workflows/docs-sync-publish.yml`
- `.github/workflows/docs-translate-trigger-release.yml`
- `.github/workflows/install-smoke.yml`
- `.github/workflows/labeler.yml`
- `.github/workflows/macos-release.yml`
- `.github/workflows/openclaw-npm-release.yml`
- `.github/workflows/plugin-clawhub-release.yml`
- `AGENTS.md`
- `CLAUDE.md`
- `Dockerfile`
- `Makefile`
- `README.md`
- `docker-compose.yml`
- `package.json`
- `pnpm-workspace.yaml`
- `pyproject.toml`

## Captured Files

### `.github/workflows/auto-response.yml`

- Source path: `.github/workflows/auto-response.yml`
- Truncated: `no`

```yaml
name: Auto response

on:
  issues:
    types: [opened, edited, labeled]
  issue_comment:
    types: [created]
  pull_request_target: # zizmor: ignore[dangerous-triggers] maintainer-owned label automation; no untrusted checkout or code execution
    types: [labeled]

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref || github.run_id }}
  cancel-in-progress: ${{ github.event_name == 'pull_request_target' }}

permissions: {}

jobs:
  auto-response:
    permissions:
      issues: write
      pull-requests: write
    runs-on: blacksmith-16vcpu-ubuntu-2404
    steps:
      - uses: actions/create-github-app-token@v2
        id: app-token
        continue-on-error: true
        with:
          app-id: "2729701"
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
      - uses: actions/create-github-app-token@v2
        id: app-token-fallback
        if: steps.app-token.outcome == 'failure'
        with:
          app-id: "2971289"
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY_FALLBACK }}
      - name: Handle labeled items
        uses: actions/github-script@v8
        with:
          github-token: ${{ steps.app-token.outputs.token || steps.app-token-fallback.outputs.token }}
          script: |
            // Labels prefixed with "r:" are auto-response triggers.
            const activePrLimit = 10;
            const rules = [
              {
                label: "r: skill",
                close: true,
                message:
                  "Thanks for the contribution! New skills should be published to [Clawhub](https://clawhub.ai) for everyone to use. We’re keeping the core lean on skills, so I’m closing this out.",
              },
              {
                label: "r: support",
                close: true,
                message:
                  "Please use [our support server](https://discord.gg/clawd) and ask in #help or #users-helping-users to resolve this, or follow the stuck FAQ at https://docs.openclaw.ai/help/faq#im-stuck-whats-the-fastest-way-to-get-unstuck.",
              },
              {
                label: "r: no-ci-pr",
                close: true,
                message:
                  "Please don't make PRs for test failures on main.\n\n" +
                  "The team is aware of those and will handle them directly on the codebase, not only fixing the tests but also investigating what the root cause is. Having to sift through test-fix-PRs (including some that have been out of date for weeks...) on top of that doesn't help. There are already way too many PRs for humans to manage; please don't make the flood worse.\n\n" +
                  "Thank you.",
              },
              {
                label: "r: too-many-prs",
                close: true,
                message:
                  `Closing this PR because the author has more than ${activePrLimit} active PRs in this repo. ` +
                  "Please reduce the active PR queue and reopen or resubmit once it is back under the limit. You can close your own PRs to get back under the limit.",
              },
              {
                label: "r: testflight",
                close: true,
                commentTriggers: ["testflight"],
                message: "Not available, build from source.",
              },
              {
                label: "r: third-party-extension",
                close: true,
                message:
                  "Please make this as a third-party plugin that you maintain yourself in your own repo. Docs: https://docs.openclaw.ai/plugin. Feel free to open a PR after to add it to our community plugins page: https://docs.openclaw.ai/plugins/community",
              },
              {
                label: "r: moltbook",
                close: true,
                lock: true,
                lockReason: "off-topic",
                commentTriggers: ["moltbook"],
                message:
                  "OpenClaw is not affiliated with Moltbook, and issues related to Moltbook should not be submitted here.",
              },
            ];

            const maintainerTeam = "maintainer";
            const pingWarningMessage =
              "Please don’t spam-ping multiple maintainers at once. Be patient, or join our community Discord for help: https://discord.gg/clawd";
            const mentionRegex = /@([A-Za-z0-9-]+)/g;
            const maintainerCache = new Map();
            const normalizeLogin = (login) => login.toLowerCase();
            const bugSubtypeLabelSpecs = {
              regression: {
                color: "D93F0B",
                description: "Behavior that previously worked and now fails",
              },
              "bug:crash": {
                color: "B60205",
                description: "Process/app exits unexpectedly or hangs",
              },
              "bug:behavior": {
                color: "D73A4A",
                description: "Incorrect behavior without a crash",
              },
            };
            const bugTypeToLabel = {
              "Regression (worked before, now fails)": "regression",
              "Crash (process/app exits or hangs)": "bug:crash",
              "Behavior bug (incorrect output/state without crash)": "bug:behavior",
            };
            const bugSubtypeLabels = Object.keys(bugSubtypeLabelSpecs);

            const extractIssueFormValue = (body, field) => {
              if (!body) {
                return "";
              }
              const escapedField = field.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
              const regex = new RegExp(
                `(?:^|\\n)###\\s+${escapedField}\\s*\\n([\\s\\S]*?)(?=\\n###\\s+|$)`,
                "i",
              );
              const match = body.match(regex);
              if (!match) {
                return "";
              }
              for (const line of match[1].split("\n")) {
                const trimmed = line.trim();
                if (trimmed) {
                  return trimmed;
                }
              }
              return "";
            };

            const ensureLabelExists = async (name, color, description) => {
              try {
                await github.rest.issues.getLabel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  name,
                });
              } catch (error) {
                if (error?.status !== 404) {
                  throw error;
                }
                await github.rest.issues.createLabel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  name,
                  color,
                  description,
                });
              }
            };

            const syncBugSubtypeLabel = async (issue, labelSet) => {
              if (!labelSet.has("bug")) {
                return;
              }

              const selectedBugType = extractIssueFormValue(issue.body ?? "", "Bug type");
              const targetLabel = bugTypeToLabel[selectedBugType];
              if (!targetLabel) {
                return;
              }

              const targetSpec = bugSubtypeLabelSpecs[targetLabel];
              await ensureLabelExists(targetLabel, targetSpec.color, targetSpec.description);

              for (const subtypeLabel of bugSubtypeLabels) {
                if (subtypeLabel === targetLabel) {
                  continue;
                }
                if (!labelSet.has(subtypeLabel)) {
                  continue;
                }
                try {
                  await github.rest.issues.removeLabel({
                    owner: context.repo.owner,
                    repo: context.repo.repo,
                    issue_number: issue.number,
                    name: subtypeLabel,
                  });
                  labelSet.delete(subtypeLabel);
                } catch (error) {
                  if (error?.status !== 404) {
                    throw error;
                  }
                }
              }

              if (!labelSet.has(targetLabel)) {
                await github.rest.issues.addLabels({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: issue.number,
                  labels: [targetLabel],
                });
                labelSet.add(targetLabel);
              }
            };

            const isMaintainer = async (login) => {
              if (!login) {
                return false;
              }
              const normalized = normalizeLogin(login);
              if (maintainerCache.has(normalized)) {
                return maintainerCache.get(normalized);
              }
              let isMember = false;
              try {
                const membership = await github.rest.teams.getMembershipForUserInOrg({
                  org: context.repo.owner,
                  team_slug: maintainerTeam,
                  username: normalized,
                });
                isMember = membership?.data?.state === "active";
              } catch (error) {
                if (error?.status !== 404) {
                  throw error;
                }
              }
              maintainerCache.set(normalized, isMember);
              return isMember;
            };

            const countMaintainerMentions = async (body, authorLogin) => {
              if (!body) {
                return 0;
              }
              const normalizedAuthor = authorLogin ? normalizeLogin(authorLogin) : "";
              if (normalizedAuthor && (await isMaintainer(normalizedAuthor))) {
                return 0;
              }

              const haystack = body.toLowerCase();
              const teamMention = `@${context.repo.owner.toLowerCase()}/${maintainerTeam}`;
              if (haystack.includes(teamMention)) {
                return 3;
              }

              const mentions = new Set();
              for (const match of body.matchAll(mentionRegex)) {
                mentions.add(normalizeLogin(match[1]));
              }
              if (normalizedAuthor) {
                mentions.delete(normalizedAuthor);
              }

              let count = 0;
              for (const login of mentions) {
                if (await isMaintainer(login)) {
                  count += 1;
                }
              }
              return count;
            };

            const triggerLabel = "trigger-response";
            const activePrLimitLabel = "r: too-many-prs";
            const activePrLimitOverrideLabel = "r: too-many-prs-override";
            const target = context.payload.issue ?? context.payload.pull_request;
            if (!target) {
              return;
            }

            const labelSet = new Set(
              (target.labels ?? [])
                .map((label) => (typeof label === "string" ? label : label?.name))
                .filter((name) => typeof name === "string"),
            );

            const issue = context.payload.issue;
            const pullRequest = context.payload.pull_request;
            const comment = context.payload.comment;
            if (comment) {
              const authorLogin = comment.user?.login ?? "";
              if (comment.user?.type === "Bot" || authorLogin.endsWith("[bot]")) {
                return;
              }

              const commentBody = comment.body ?? "";
              const responses = [];
              const mentionCount = await countMaintainerMentions(commentBody, authorLogin);
              if (mentionCount >= 3) {
                responses.push(pingWarningMessage);
              }

              const commentHaystack = commentBody.toLowerCase();
              const commentRule = rules.find((item) =>
                (item.commentTriggers ?? []).some((trigger) =>
                  commentHaystack.includes(trigger),
                ),
              );
              if (commentRule) {
                responses.push(commentRule.message);
              }

              if (responses.length > 0) {
                await github.rest.issues.createComment({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: target.number,
                  body: responses.join("\n\n"),
                });
              }
              return;
            }

            if (issue) {
              const action = context.payload.action;
              if (action === "opened" || action === "edited") {
                const issueText = `${issue.title ?? ""}\n${issue.body ?? ""}`.trim();
                const authorLogin = issue.user?.login ?? "";
                const mentionCount = await countMaintainerMentions(
                  issueText,
                  authorLogin,
                );
                if (mentionCount >= 3) {
                  await github.rest.issues.createComment({
                    owner: context.repo.owner,
                    repo: context.repo.repo,
                    issue_number: issue.number,
                    body: pingWarningMessage,
                  });
                }

                await syncBugSubtypeLabel(issue, labelSet);
              }
            }

            const hasTriggerLabel = labelSet.has(triggerLabel);
            if (hasTriggerLabel) {
              labelSet.delete(triggerLabel);
              try {
                await github.rest.issues.removeLabel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: target.number,
                  name: triggerLabel,
                });
              } catch (error) {
                if (error?.status !== 404) {
                  throw error;
                }
              }
            }

            const isLabelEvent = context.payload.action === "labeled";
            if (!hasTriggerLabel && !isLabelEvent) {
              return;
            }

            if (issue) {
              const title = issue.title ?? "";
              const body = issue.body ?? "";
              const haystack = `${title}\n${body}`.toLowerCase();
              const hasMoltbookLabel = labelSet.has("r: moltbook");
              const hasTestflightLabel = labelSet.has("r: testflight");
              const hasSecurityLabel = labelSet.has("security");
              if (title.toLowerCase().includes("security") && !hasSecurityLabel) {
                await github.rest.issues.addLabels({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: issue.number,
                  labels: ["security"],
                });
                labelSet.add("security");
              }
              if (title.toLowerCase().includes("testflight") && !hasTestflightLabel) {
                await github.rest.issues.addLabels({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: issue.number,
                  labels: ["r: testflight"],
                });
                labelSet.add("r: testflight");
              }
              if (haystack.includes("moltbook") && !hasMoltbookLabel) {
                await github.rest.issues.addLabels({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: issue.number,
                  labels: ["r: moltbook"],
                });
                labelSet.add("r: moltbook");
              }
            }

            const invalidLabel = "invalid";
            const spamLabel = "r: spam";
            const dirtyLabel = "dirty";
            const badBarnacleLabel = "bad-barnacle";
            const noisyPrMessage =
              "Closing this PR because it looks dirty (too many unrelated or unexpected changes). This usually happens when a branch picks up unrelated commits or a merge went sideways. Please recreate the PR from a clean branch.";

            if (pullRequest) {
              if (labelSet.has(badBarnacleLabel)) {
                core.info(`Skipping PR auto-response checks for #${pullRequest.number} because ${badBarnacleLabel} is present.`);
                return;
              }

              if (labelSet.has(dirtyLabel)) {
                await github.rest.issues.createComment({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pullRequest.number,
                  body: noisyPrMessage,
                });
                await github.rest.issues.update({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pullRequest.number,
                  state: "closed",
                });
                return;
              }
              const labelCount = labelSet.size;
              if (labelCount > 20) {
                await github.rest.issues.createComment({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pullRequest.number,
                  body: noisyPrMessage,
                });
                await github.rest.issues.update({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pullRequest.number,
                  state: "closed",
                });
                return;
              }
              if (labelSet.has(spamLabel)) {
                await github.rest.issues.update({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pullRequest.number,
                  state: "closed",
                });
                await github.rest.issues.lock({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pullRequest.number,
                  lock_reason: "spam",
                });
                return;
              }
              if (labelSet.has(invalidLabel)) {
                await github.rest.issues.update({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pullRequest.number,
                  state: "closed",
                });
                return;
              }
            }

            if (issue && labelSet.has(spamLabel)) {
              await github.rest.issues.update({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                state: "closed",
                state_reason: "not_planned",
              });
              await github.rest.issues.lock({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                lock_reason: "spam",
              });
              return;
            }

            if (issue && labelSet.has(invalidLabel)) {
              await github.rest.issues.update({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                state: "closed",
                state_reason: "not_planned",
              });
              return;
            }

            if (pullRequest && labelSet.has(activePrLimitOverrideLabel)) {
              labelSet.delete(activePrLimitLabel);
            }

            const rule = rules.find((item) => labelSet.has(item.label));
            if (!rule) {
              return;
            }

            const issueNumber = target.number;

            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: issueNumber,
              body: rule.message,
            });

            if (rule.close) {
              await github.rest.issues.update({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issueNumber,
                state: "closed",
              });
            }

            if (rule.lock) {
              await github.rest.issues.lock({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issueNumber,
                lock_reason: rule.lockReason ?? "resolved",
              });
            }
```

### `.github/workflows/ci.yml`

- Source path: `.github/workflows/ci.yml`
- Truncated: `yes`

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    types: [opened, reopened, synchronize, ready_for_review, converted_to_draft]

permissions:
  contents: read

concurrency:
  group: ${{ github.event_name == 'pull_request' && format('{0}-{1}', github.workflow, github.event.pull_request.number) || format('{0}-{1}', github.workflow, github.run_id) }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"

jobs:
  # Preflight: establish routing truth and job matrices once, then let real
  # work fan out from a single source of truth.
  preflight:
    if: github.event_name != 'pull_request' || !github.event.pull_request.draft
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 20
    outputs:
      docs_only: ${{ steps.manifest.outputs.docs_only }}
      docs_changed: ${{ steps.manifest.outputs.docs_changed }}
      run_node: ${{ steps.manifest.outputs.run_node }}
      run_macos: ${{ steps.manifest.outputs.run_macos }}
      run_android: ${{ steps.manifest.outputs.run_android }}
      run_skills_python: ${{ steps.manifest.outputs.run_skills_python }}
      run_skills_python_job: ${{ steps.manifest.outputs.run_skills_python_job }}
      run_windows: ${{ steps.manifest.outputs.run_windows }}
      has_changed_extensions: ${{ steps.manifest.outputs.has_changed_extensions }}
      changed_extensions_matrix: ${{ steps.manifest.outputs.changed_extensions_matrix }}
      run_build_artifacts: ${{ steps.manifest.outputs.run_build_artifacts }}
      run_checks_fast: ${{ steps.manifest.outputs.run_checks_fast }}
      checks_fast_core_matrix: ${{ steps.manifest.outputs.checks_fast_core_matrix }}
      checks_node_extensions_matrix: ${{ steps.manifest.outputs.checks_node_extensions_matrix }}
      run_checks: ${{ steps.manifest.outputs.run_checks }}
      checks_matrix: ${{ steps.manifest.outputs.checks_matrix }}
      checks_node_core_test_matrix: ${{ steps.manifest.outputs.checks_node_core_test_matrix }}
      run_extension_fast: ${{ steps.manifest.outputs.run_extension_fast }}
      extension_fast_matrix: ${{ steps.manifest.outputs.extension_fast_matrix }}
      run_check: ${{ steps.manifest.outputs.run_check }}
      run_check_additional: ${{ steps.manifest.outputs.run_check_additional }}
      run_build_smoke: ${{ steps.manifest.outputs.run_build_smoke }}
      run_check_docs: ${{ steps.manifest.outputs.run_check_docs }}
      run_control_ui_i18n: ${{ steps.manifest.outputs.run_control_ui_i18n }}
      run_checks_windows: ${{ steps.manifest.outputs.run_checks_windows }}
      checks_windows_matrix: ${{ steps.manifest.outputs.checks_windows_matrix }}
      run_macos_node: ${{ steps.manifest.outputs.run_macos_node }}
      macos_node_matrix: ${{ steps.manifest.outputs.macos_node_matrix }}
      run_macos_swift: ${{ steps.manifest.outputs.run_macos_swift }}
      run_android_job: ${{ steps.manifest.outputs.run_android_job }}
      android_matrix: ${{ steps.manifest.outputs.android_matrix }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          fetch-depth: 1
          fetch-tags: false
          persist-credentials: false
          submodules: false

      - name: Ensure preflight base commit
        uses: ./.github/actions/ensure-base-commit
        with:
          base-sha: ${{ github.event_name == 'push' && github.event.before || github.event.pull_request.base.sha }}
          fetch-ref: ${{ github.event_name == 'push' && github.ref_name || github.event.pull_request.base.ref }}

      - name: Detect docs-only changes
        id: docs_scope
        uses: ./.github/actions/detect-docs-changes

      - name: Detect changed scopes
        id: changed_scope
        if: steps.docs_scope.outputs.docs_only != 'true'
        shell: bash
        run: |
          set -euo pipefail

          if [ "${{ github.event_name }}" = "push" ]; then
            BASE="${{ github.event.before }}"
          else
            BASE="${{ github.event.pull_request.base.sha }}"
          fi

          node scripts/ci-changed-scope.mjs --base "$BASE" --head HEAD

      - name: Setup Node environment
        if: steps.docs_scope.outputs.docs_only != 'true'
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          install-deps: "false"
          use-sticky-disk: "false"

      - name: Detect changed extensions
        id: changed_extensions
        if: steps.docs_scope.outputs.docs_only != 'true' && steps.changed_scope.outputs.run_node == 'true'
        env:
          BASE_SHA: ${{ github.event_name == 'push' && github.event.before || github.event.pull_request.base.sha }}
          BASE_REF: ${{ github.event_name == 'push' && github.ref_name || github.event.pull_request.base.ref }}
        run: |
          node --input-type=module <<'EOF'
          import { appendFileSync } from "node:fs";
          import { listChangedExtensionIds } from "./scripts/lib/changed-extensions.mjs";

          const extensionIds = listChangedExtensionIds({
            base: process.env.BASE_SHA,
            head: "HEAD",
            fallbackBaseRef: process.env.BASE_REF,
            unavailableBaseBehavior: "all",
          });
          const matrix = JSON.stringify({ include: extensionIds.map((extension) => ({ extension })) });

          appendFileSync(process.env.GITHUB_OUTPUT, `has_changed_extensions=${extensionIds.length > 0}\n`, "utf8");
          appendFileSync(process.env.GITHUB_OUTPUT, `changed_extensions_matrix=${matrix}\n`, "utf8");
          EOF

      - name: Build CI manifest
        id: manifest
        env:
          OPENCLAW_CI_DOCS_ONLY: ${{ steps.docs_scope.outputs.docs_only }}
          OPENCLAW_CI_DOCS_CHANGED: ${{ steps.docs_scope.outputs.docs_changed }}
          OPENCLAW_CI_RUN_NODE: ${{ steps.changed_scope.outputs.run_node || 'false' }}
          OPENCLAW_CI_RUN_MACOS: ${{ steps.changed_scope.outputs.run_macos || 'false' }}
          OPENCLAW_CI_RUN_ANDROID: ${{ steps.changed_scope.outputs.run_android || 'false' }}
          OPENCLAW_CI_RUN_WINDOWS: ${{ steps.changed_scope.outputs.run_windows || 'false' }}
          OPENCLAW_CI_RUN_SKILLS_PYTHON: ${{ steps.changed_scope.outputs.run_skills_python || 'false' }}
          OPENCLAW_CI_RUN_CONTROL_UI_I18N: ${{ steps.changed_scope.outputs.run_control_ui_i18n || 'false' }}
          OPENCLAW_CI_HAS_CHANGED_EXTENSIONS: ${{ steps.changed_extensions.outputs.has_changed_extensions || 'false' }}
          OPENCLAW_CI_CHANGED_EXTENSIONS_MATRIX: ${{ steps.changed_extensions.outputs.changed_extensions_matrix || '{"include":[]}' }}
        run: |
          node --input-type=module <<'EOF'
          import { appendFileSync } from "node:fs";
          import {
            createNodeTestShards,
          } from "./scripts/lib/ci-node-test-plan.mjs";
          import {
            createExtensionTestShards,
            DEFAULT_EXTENSION_TEST_SHARD_COUNT,
          } from "./scripts/lib/extension-test-plan.mjs";

          const parseBoolean = (value, fallback = false) => {
            if (value === undefined) return fallback;
            const normalized = value.trim().toLowerCase();
            if (normalized === "true" || normalized === "1") return true;
            if (normalized === "false" || normalized === "0" || normalized === "") return false;
            return fallback;
          };

          const parseJson = (value, fallback) => {
            try {
              return value ? JSON.parse(value) : fallback;
            } catch {
              return fallback;
            }
          };

          const createMatrix = (include) => ({ include });
          const outputPath = process.env.GITHUB_OUTPUT;
          const eventName = process.env.GITHUB_EVENT_NAME ?? "pull_request";
          const isPush = eventName === "push";
          const docsOnly = parseBoolean(process.env.OPENCLAW_CI_DOCS_ONLY);
          const docsChanged = parseBoolean(process.env.OPENCLAW_CI_DOCS_CHANGED);
          const runNode = parseBoolean(process.env.OPENCLAW_CI_RUN_NODE) && !docsOnly;
          const runMacos = parseBoolean(process.env.OPENCLAW_CI_RUN_MACOS) && !docsOnly;
          const runAndroid = parseBoolean(process.env.OPENCLAW_CI_RUN_ANDROID) && !docsOnly;
          const runWindows = parseBoolean(process.env.OPENCLAW_CI_RUN_WINDOWS) && !docsOnly;
          const runSkillsPython = parseBoolean(process.env.OPENCLAW_CI_RUN_SKILLS_PYTHON) && !docsOnly;
          const runControlUiI18n =
            parseBoolean(process.env.OPENCLAW_CI_RUN_CONTROL_UI_I18N) && !docsOnly;
          const hasChangedExtensions =
            parseBoolean(process.env.OPENCLAW_CI_HAS_CHANGED_EXTENSIONS) && !docsOnly;
          const changedExtensionsMatrix = hasChangedExtensions
            ? parseJson(process.env.OPENCLAW_CI_CHANGED_EXTENSIONS_MATRIX, { include: [] })
            : { include: [] };
          const extensionShardMatrix = createMatrix(
            runNode
              ? createExtensionTestShards({
                  shardCount: DEFAULT_EXTENSION_TEST_SHARD_COUNT,
                }).map((shard) => ({
                  check_name: shard.checkName,
                  extensions_csv: shard.extensionIds.join(","),
                  shard_index: shard.index + 1,
                  task: "extensions-batch",
                }))
              : [],
          );

          const manifest = {
            docs_only: docsOnly,
            docs_changed: docsChanged,
            run_node: runNode,
            run_macos: runMacos,
            run_android: runAndroid,
            run_skills_python: runSkillsPython,
            run_windows: runWindows,
            has_changed_extensions: hasChangedExtensions,
            changed_extensions_matrix: changedExtensionsMatrix,
            run_build_artifacts: runNode,
            run_checks_fast: runNode,
            checks_fast_core_matrix: createMatrix(
              runNode
                ? [
                    { check_name: "checks-fast-bundled", runtime: "node", task: "bundled" },
                    {
                      check_name: "checks-fast-contracts-protocol",
                      runtime: "node",
                      task: "contracts-protocol",
                    },
                  ]
                : [],
            ),
            checks_node_extensions_matrix: extensionShardMatrix,
            run_checks: runNode,
            checks_matrix: createMatrix(
              runNode
                ? [
                    { check_name: "checks-node-channels", runtime: "node", task: "channels" },
                    ...(isPush
                      ? [
                          {
                            check_name: "checks-node-compat-node22",
                            runtime: "node",
                            task: "compat-node22",
                            node_version: "22.x",
                            cache_key_suffix: "node22",
                          },
                        ]
                      : []),
                  ]
                : [],
            ),
            checks_node_core_test_matrix: createMatrix(
              runNode
                ? createNodeTestShards().map((shard) => ({
                    check_name: shard.checkName,
                    runtime: "node",
                    task: "test-shard",
                    shard_name: shard.shardName,
                    configs: shard.configs,
                  }))
                : [],
            ),
            run_extension_fast: hasChangedExtensions,
            extension_fast_matrix: createMatrix(
              hasChangedExtensions
                ? (changedExtensionsMatrix.include ?? []).map((entry) => ({
                    check_name: `extension-fast-${entry.extension}`,
                    extension: entry.extension,
                  }))
                : [],
            ),
            run_check: runNode,
            run_check_additional: runNode,
            run_build_smoke: runNode,
            run_check_docs: docsChanged,
            run_control_ui_i18n: runControlUiI18n,
            run_skills_python_job: runSkillsPython,
            run_checks_windows: runWindows,
            checks_windows_matrix: createMatrix(
              runWindows
                ? [{ check_name: "checks-windows-node-test", runtime: "node", task: "test" }]
                : [],
            ),
            run_macos_node: runMacos,
            macos_node_matrix: createMatrix(
              runMacos ? [{ check_name: "macos-node", runtime: "node", task: "test" }] : [],
            ),
            run_macos_swift: runMacos,
            run_android_job: runAndroid,
            android_matrix: createMatrix(
              runAndroid
                ? [
                    { check_name: "android-test-play", task: "test-play" },
                    { check_name: "android-test-third-party", task: "test-third-party" },
                    { check_name: "android-build-play", task: "build-play" },
                    { check_name: "android-build-third-party", task: "build-third-party" },
                  ]
                : [],
            ),
          };

          for (const [key, value] of Object.entries(manifest)) {
            appendFileSync(
              outputPath,
              `${key}=${typeof value === "string" ? value : JSON.stringify(value)}\n`,
              "utf8",
            );
          }
          EOF

  # Run the fast security/SCM checks in parallel with scope detection so the
  # main Node jobs do not have to wait for Python/pre-commit setup.
  security-fast:
    if: github.event_name != 'pull_request' || !github.event.pull_request.draft
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 20
    env:
      PRE_COMMIT_CACHE_KEY_SUFFIX: ${{ github.event_name == 'pull_request' && github.event.pull_request.base.sha || github.sha }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          fetch-depth: 1
          fetch-tags: false
          persist-credentials: false
          submodules: false

      - name: Ensure security base commit
        uses: ./.github/actions/ensure-base-commit
        with:
          base-sha: ${{ github.event_name == 'push' && github.event.before || github.event.pull_request.base.sha }}
          fetch-ref: ${{ github.event_name == 'push' && github.ref_name || github.event.pull_request.base.ref }}

      - name: Prepare trusted pre-commit config
        if: github.event_name == 'pull_request'
        env:
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
        run: |
          set -euo pipefail
          trusted_config="$RUNNER_TEMP/pre-commit-base.yaml"
          git show "${BASE_SHA}:.pre-commit-config.yaml" > "$trusted_config"
          echo "PRE_COMMIT_CONFIG_PATH=$trusted_config" >> "$GITHUB_ENV"

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          install-deps: "false"
          use-sticky-disk: "false"

      - name: Setup Python
        id: setup-python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"
          cache: "pip"
          cache-dependency-path: |
            pyproject.toml
            .pre-commit-config.yaml
            .github/workflows/ci.yml

      - name: Restore pre-commit cache
        uses: actions/cache@v5
        with:
          path: ~/.cache/pre-commit
          key: pre-commit-${{ runner.os }}-${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('.pre-commit-config.yaml') }}-${{ env.PRE_COMMIT_CACHE_KEY_SUFFIX }}
          restore-keys: |
            pre-commit-${{ runner.os }}-${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('.pre-commit-config.yaml') }}-

      - name: Install pre-commit
        run: |
          python -m pip install --upgrade pip
          python -m pip install pre-commit==4.2.0

      - name: Detect committed private keys
        run: pre-commit run --config "${PRE_COMMIT_CONFIG_PATH:-.pre-commit-config.yaml}" --all-files detect-private-key

      - name: Audit changed GitHub workflows with zizmor
        env:
          BASE_SHA: ${{ github.event_name == 'push' && github.event.before || github.event.pull_request.base.sha }}
        run: |
          set -euo pipefail

          if [ -z "${BASE_SHA:-}" ] || [ "${BASE_SHA}" = "0000000000000000000000000000000000000000" ]; then
            echo "No usable base SHA detected; skipping zizmor."
            exit 0
          fi

          if ! git cat-file -e "${BASE_SHA}^{commit}" 2>/dev/null; then
            echo "Base SHA ${BASE_SHA} is unavailable; skipping zizmor."
            exit 0
          fi

          mapfile -t workflow_files < <(
            git diff --name-only "${BASE_SHA}" HEAD -- '.github/workflows/*.yml' '.github/workflows/*.yaml'
          )
          if [ "${#workflow_files[@]}" -eq 0 ]; then
            echo "No workflow changes detected; skipping zizmor."
            exit 0
          fi

          printf 'Auditing workflow files:\n%s\n' "${workflow_files[@]}"
          pre-commit run --config "${PRE_COMMIT_CONFIG_PATH:-.pre-commit-config.yaml}" zizmor --files "${workflow_files[@]}"

      - name: Audit production dependencies
        run: pre-commit run --config "${PRE_COMMIT_CONFIG_PATH:-.pre-commit-config.yaml}" --all-files pnpm-audit-prod

  # Build dist once for Node-relevant changes and share it with downstream jobs.
  # Keep this overlapping with the fast correctness lanes so green PRs get heavy
  # test/build feedback sooner instead of waiting behind a full `check` pass.
  build-artifacts:
    needs: [preflight]
    if: needs.preflight.outputs.run_build_artifacts == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 20
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Ensure secrets base commit (PR fast path)
        if: github.event_name == 'pull_request'
        uses: ./.github/actions/ensure-base-commit
        with:
          base-sha: ${{ github.event.pull_request.base.sha }}
          fetch-ref: ${{ github.event.pull_request.base.ref }}

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Build dist
        run: pnpm build

      - name: Build Control UI
        run: pnpm ui:build

      - name: Upload dist artifact
        uses: actions/upload-artifact@v7
        with:
          name: dist-build
          path: dist/
          retention-days: 1

      - name: Upload A2UI bundle artifact
        uses: actions/upload-artifact@v7
        with:
          name: canvas-a2ui-bundle
          path: src/canvas-host/a2ui/
          include-hidden-files: true
          retention-days: 1

  checks-fast-core:
    name: ${{ matrix.check_name }}
    needs: [preflight]
    if: needs.preflight.outputs.run_checks_fast == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 60
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.preflight.outputs.checks_fast_core_matrix) }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Run ${{ matrix.task }} (${{ matrix.runtime }})
        env:
          OPENCLAW_TEST_PROJECTS_PARALLEL: 3
          TASK: ${{ matrix.task }}
        shell: bash
        run: |
          set -euo pipefail
          case "$TASK" in
            bundled)
              pnpm test:bundled
              ;;
            contracts|contracts-protocol)
              pnpm build
              pnpm test:contracts
              pnpm protocol:check
              ;;
            *)
              echo "Unsupported checks-fast task: $TASK" >&2
              exit 1
              ;;
          esac

  checks-node-extensions-shard:
    name: ${{ matrix.check_name }}
    needs: [preflight]
    if: needs.preflight.outputs.run_checks_fast == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 60
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.preflight.outputs.checks_node_extensions_matrix) }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Run extension shard
        env:
          OPENCLAW_EXTENSION_BATCH: ${{ matrix.extensions_csv }}
        run: pnpm test:extensions:batch -- "$OPENCLAW_EXTENSION_BATCH"

  checks-node-extensions:
    name: checks-node-extensions
    needs: [preflight, checks-node-extensions-shard]
    if: always() && needs.preflight.outputs.run_checks_fast == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 5
    steps:
      - name: Verify extension shards
        env:
          SHARD_RESULT: ${{ needs.checks-node-extensions-shard.result }}
        run: |
          if [ "$SHARD_RESULT" != "success" ]; then
            echo "Extension shard checks failed: $SHARD_RESULT" >&2
            exit 1
          fi

  checks:
    name: ${{ matrix.check_name }}
    needs: [preflight, build-artifacts]
    if: always() && needs.preflight.outputs.run_checks == 'true' && needs.build-artifacts.result == 'success'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 60
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.preflight.outputs.checks_matrix) }}
    steps:
      - name: Skip compatibility lanes on pull requests
        if: github.event_name == 'pull_request' && matrix.task == 'compat-node22'
        run: echo "Skipping push-only lane on pull requests."

      - name: Checkout
        if: github.event_name != 'pull_request' || matrix.task != 'compat-node22'
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Node environment
        if: github.event_name != 'pull_request' || matrix.task != 'compat-node22'
        uses: ./.github/actions/setup-node-env
        with:
          node-version: "${{ matrix.node_version || '24.x' }}"
          cache-key-suffix: "${{ matrix.cache_key_suffix || 'node24' }}"
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Configure Node test resources
        if: (github.event_name != 'pull_request' || matrix.task != 'compat-node22') && matrix.runtime == 'node' && (matrix.task == 'test' || matrix.task == 'channels' || matrix.task == 'compat-node22')
        env:
          TASK: ${{ matrix.task }}
        run: |
          echo "OPENCLAW_VITEST_MAX_WORKERS=2" >> "$GITHUB_ENV"
          if [ "$TASK" = "test" ]; then
            echo "OPENCLAW_TEST_PROJECTS_LEAF_SHARDS=1" >> "$GITHUB_ENV"
            echo "OPENCLAW_TEST_SKIP_FULL_EXTENSIONS_SHARD=1" >> "$GITHUB_ENV"
          fi
          if [ "$TASK" = "channels" ]; then
            echo "OPENCLAW_VITEST_MAX_WORKERS=1" >> "$GITHUB_ENV"
          fi

      - name: Download dist artifact
        if: matrix.task == 'test'
        uses: actions/download-artifact@v8
        with:
          name: dist-build
          path: dist/

      - name: Download A2UI bundle artifact
        if: matrix.task == 'test' || matrix.task == 'channels'
        uses: actions/download-artifact@v8
        with:
          name: canvas-a2ui-bundle
          path: src/canvas-host/a2ui/

      - name: Run ${{ matrix.task }} (${{ matrix.runtime }})
        if: github.event_name != 'pull_request' || matrix.task != 'compat-node22'
        env:
          TASK: ${{ matrix.task }}
          NODE_OPTIONS: --max-old-space-size=6144
        shell: bash
        run: |
          set -euo pipefail
          case "$TASK" in
            test)
              pnpm test
              ;;
            channels)
              pnpm test:channels
              ;;
            compat-node22)
              pnpm build
              pnpm ui:build
              node openclaw.mjs --help
              node openclaw.mjs status --json --timeout 1
              pnpm test:build:singleton
              ;;
            *)
              echo "Unsupported checks task: $TASK" >&2
              exit 1
              ;;
          esac

  checks-node-core-test-shard:
    name: ${{ matrix.check_name }}
    needs: [preflight, build-artifacts]
    if: always() && needs.preflight.outputs.run_checks == 'true' && needs.build-artifacts.result == 'success'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 60
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.preflight.outputs.checks_node_core_test_matrix) }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          node-version: "${{ matrix.node_version || '24.x' }}"
          cache-key-suffix: "${{ matrix.cache_key_suffix || 'node24' }}"
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Configure Node test resources
        run: echo "OPENCLAW_VITEST_MAX_WORKERS=2" >> "$GITHUB_ENV"

      - name: Download dist artifact
        uses: actions/download-artifact@v8
        with:
          name: dist-build
          path: dist/

      - name: Download A2UI bundle artifact
        uses: actions/download-artifact@v8
        with:
          name: canvas-a2ui-bundle
          path: src/canvas-host/a2ui/

      - name: Run Node test shard
        env:
          NODE_OPTIONS: --max-old-space-size=6144
          OPENCLAW_NODE_TEST_CONFIGS_JSON: ${{ toJson(matrix.configs) }}
        shell: bash
        run: |
          set -euo pipefail
          node --input-type=module <<'EOF'
          import { spawnSync } from "node:child_process";
          import { resolveVitestCliEntry, resolveVitestNodeArgs } from "./scripts/run-vitest.mjs";

          const configs = JSON.parse(process.env.OPENCLAW_NODE_TEST_CONFIGS_JSON ?? "[]");
          if (!Array.isArray(configs) || configs.length === 0) {
            console.error("Missing node test shard configs");
            process.exit(1);
          }

          for (const config of configs) {
            console.error(`[test] starting ${config}`);
            const result = spawnSync(
              "pnpm",
              [
                "exec",
                "node",
                ...resolveVitestNodeArgs(process.env),
                resolveVitestCliEntry(),
                "run",
                "--config",
                config,
              ],
              {
                env: process.env,
                stdio: "inherit",
              },
            );
            if ((result.status ?? 1) !== 0) {
              process.exit(result.status ?? 1);
            }
          }
          EOF

  checks-node-core-test:
    name: checks-node-core
    needs: [preflight, checks-node-core-test-shard]
    if: always() && needs.preflight.outputs.run_checks == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 5
    steps:
      - name: Verify node test shards
        env:
          SHARD_RESULT: ${{ needs.checks-node-core-test-shard.result }}
        run: |
          if [ "$SHARD_RESULT" != "success" ]; then
            echo "Node test shards failed: $SHARD_RESULT" >&2
            exit 1
          fi

  extension-fast:
    name: "extension-fast"
    needs: [preflight]
    if: needs.preflight.outputs.run_extension_fast == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 60
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.preflight.outputs.extension_fast_matrix) }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Run changed extension tests
        env:
          OPENCLAW_CHANGED_EXTENSION: ${{ matrix.extension }}
        run: pnpm test:extension "$OPENCLAW_CHANGED_EXTENSION"

  # Types, lint, and format check.
  check:
    name: "check"
    needs: [preflight]
    if: always() && needs.preflight.outputs.run_check == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 20
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Check types and lint and oxfmt
        env:
          OPENCLAW_LOCAL_CHECK: "0"
        run: pnpm check

      - name: Strict TS build smoke
        run: pnpm build:strict-smoke

  check-additional:
    name: "check-additional"
    needs: [preflight]
    if: always() && needs.preflight.outputs.run_check_additional == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 20
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Run plugin extension boundary guard
        id: plugin_extension_boundary
        continue-on-error: true
        run: pnpm run lint:plugins:no-extension-imports

      - name: Run no-random-messaging guard
        id: no_random_messaging
        continue-on-error: true
        run: pnpm run lint:tmp:no-random-messaging

      - name: Run channel-agnostic boundary guard
        id: channel_agnostic_boundaries
        continue-on-error: true
        run: pnpm run lint:tmp:channel-agnostic-boundaries

      - name: Run no-raw-channel-fetch guard
        id: no_raw_channel_fetch
        continue-on-error: true
        run: pnpm run lint:tmp:no-raw-channel-fetch

      - name: Run ingress owner guard
        id: ingress_owner
        continue-on-error: true
        run: pnpm run lint:agent:ingress-owner

      - name: Run no-register-http-handler guard
        id: no_register_http_handler
        continue-on-error: true
        run: pnpm run lint:plugins:no-register-http-handler

      - name: Run no-monolithic plugin-sdk entry import guard
        id: no_monolithic_plugin_sdk_entry_imports
        continue-on-error: true
        run: pnpm run lint:plugins:no-monolithic-plugin-sdk-entry-imports

      - name: Run no-extension-src-imports guard
        id: no_extension_src_imports
        continue-on-error: true
        run: pnpm run lint:plugins:no-extension-src-imports

      - name: Run no-extension-test-core-imports guard
        id: no_extension_test_core_imports
        continue-on-error: true
        run: pnpm run lint:plugins:no-extension-test-core-imports

      - name: Run plugin-sdk subpaths exported guard
        id: plugin_sdk_subpaths_exported
        continue-on-error: true
        run: pnpm run lint:plugins:plugin-sdk-subpaths-exported

      - name: Run web search provider boundary guard
        id: web_search_provider_boundary
        continue-on-error: true
        run: pnpm run lint:web-search-provider-boundaries

      - name: Run web fetch provider boundary guard
        id: web_fetch_provider_boundary
        continue-on-error: true
        run: pnpm run lint:web-fetch-provider-boundaries

      - name: Run extension src boundary guard
        id: extension_src_outside_plugin_sdk_boundary
        continue-on-error: true
        run: pnpm run lint:extensions:no-src-outside-plugin-sdk

      - name: Run extension plugin-sdk-internal guard
        id: extension_plugin_sdk_internal_boundary
        continue-on-error: true
        run: pnpm run lint:extensions:no-plugin-sdk-internal

      - name: Run extension relative-outside-package guard
        id: extension_relative_outside_package_boundary
        continue-on-error: true
        run: pnpm run lint:extensions:no-relative-outside-package

      - name: Run extension channel lint
        id: extension_channel_lint
        continue-on-error: true
        run: pnpm run lint:extensions:channels

      - name: Run bundled extension lint
        id: extension_bundled_lint
        continue-on-error: true
        run: pnpm run lint:extensions:bundled

      - name: Run extension package boundary TypeScript check
        id: extension_package_boundary_tsc
        continue-on-error: true
        run: pnpm run test:extensions:package-boundary

      - name: Enforce safe external URL opening policy
        id: no_raw_window_open
        continue-on-error: true
        run: pnpm lint:ui:no-raw-window-open

      - name: Check control UI locale sync
        id: control_ui_i18n
        if: needs.preflight.outputs.run_control_ui_i18n == 'true'
        continue-on-error: true
        run: pnpm ui:i18n:check

      - name: Run gateway watch regression harness
        id: gateway_watch_regression
        continue-on-error: true
        run: pnpm test:gateway:watch-regression

      - name: Run import cycle guard
        id: import_cycles
        continue-on-error: true
        run: pnpm check:import-cycles

      - name: Run static import SCC guard
        id: static_import_sccs
        continue-on-error: true
        run: pnpm check:static-import-sccs

      - name: Upload gateway watch regression artifacts
        if: always()
        uses: actions/upload-artifact@v7
        with:
          name: gateway-watch-regression
          path: .local/gateway-watch-regression/
          retention-days: 7

      - name: Fail if any additional check failed
        if: always()
        env:
          PLUGIN_EXTENSION_BOUNDARY_OUTCOME: ${{ steps.plugin_extension_boundary.outcome }}
          NO_RANDOM_MESSAGING_OUTCOME: ${{ steps.no_random_messaging.outcome }}
          CHANNEL_AGNOSTIC_BOUNDARIES_OUTCOME: ${{ steps.channel_agnostic_boundaries.outcome }}
          NO_RAW_CHANNEL_FETCH_OUTCOME: ${{ steps.no_raw_channel_fetch.outcome }}
          INGRESS_OWNER_OUTCOME: ${{ steps.ingress_owner.outcome }}
          NO_REGISTER_HTTP_HANDLER_OUTCOME: ${{ steps.no_register_http_handler.outcome }}
          NO_MONOLITHIC_PLUGIN_SDK_ENTRY_IMPORTS_OUTCOME: ${{ steps.no_monolithic_plugin_sdk_entry_imports.outcome }}
          NO_EXTENSION_SRC_IMPORTS_OUTCOME: ${{ steps.no_extension_src_imports.outcome }}
          NO_EXTENSION_TEST_CORE_IMPORTS_OUTCOME: ${{ steps.no_extension_test_core_imports.outcome }}
          PLUGIN_SDK_SUBPATHS_EXPORTED_OUTCOME: ${{ steps.plugin_sdk_subpaths_exported.outcome }}
          WEB_SEARCH_PROVIDER_BOUNDARY_OUTCOME: ${{ steps.web_search_provider_boundary.outcome }}
          WEB_FETCH_PROVIDER_BOUNDARY_OUTCOME: ${{ steps.web_fetch_provider_boundary.outcome }}
          EXTENSION_SRC_OUTSIDE_PLUGIN_SDK_BOUNDARY_OUTCOME: ${{ steps.extension_src_outside_plugin_sdk_boundary.outcome }}
          EXTENSION_PLUGIN_SDK_INTERNAL_BOUNDARY_OUTCOME: ${{ steps.extension_plugin_sdk_internal_boundary.outcome }}
          EXTENSION_RELATIVE_OUTSIDE_PACKAGE_BOUNDARY_OUTCOME: ${{ steps.extension_relative_outside_package_boundary.outcome }}
          EXTENSION_CHANNEL_LINT_OUTCOME: ${{ steps.extension_channel_lint.outcome }}
          EXTENSION_BUNDLED_LINT_OUTCOME: ${{ steps.extension_bundled_lint.outcome }}
          EXTENSION_PACKAGE_BOUNDARY_TSC_OUTCOME: ${{ steps.extension_package_boundary_tsc.outcome }}
          NO_RAW_WINDOW_OPEN_OUTCOME: ${{ steps.no_raw_window_open.outcome }}
          CONTROL_UI_I18N_OUTCOME: ${{ steps.control_ui_i18n.outcome == 'skipped' && 'success' || steps.control_ui_i18n.outcome }}
          GATEWAY_WATCH_REGRESSION_OUTCOME: ${{ steps.gateway_watch_regression.outcome }}
          IMPORT_CYCLES_OUTCOME: ${{ steps.import_cycles.outcome }}
          STATIC_IMPORT_SCCS_OUTCOME: ${{ steps.static_import_sccs.outcome }}
        run: |
          failures=0
          for result in \
            "plugin-extension-boundary|$PLUGIN_EXTENSION_BOUNDARY_OUTCOME" \
            "lint:tmp:no-random-messaging|$NO_RANDOM_MESSAGING_OUTCOME" \
            "lint:tmp:channel-agnostic-boundaries|$CHANNEL_AGNOSTIC_BOUNDARIES_OUTCOME" \
            "lint:tmp:no-raw-channel-fetch|$NO_RAW_CHANNEL_FETCH_OUTCOME" \
            "lint:agent:ingress-owner|$INGRESS_OWNER_OUTCOME" \
            "lint:plugins:no-register-http-handler|$NO_REGISTER_HTTP_HANDLER_OUTCOME" \
            "lint:plugins:no-monolithic-plugin-sdk-entry-imports|$NO_MONOLITHIC_PLUGIN_SDK_ENTRY_IMPORTS_OUTCOME" \
            "lint:plugins:no-extension-src-imports|$NO_EXTENSION_SRC_IMPORTS_OUTCOME" \
            "lint:plugins:no-extension-test-core-imports|$NO_EXTENSION_TEST_CORE_IMPORTS_OUTCOME" \
            "lint:plugins:plugin-sdk-subpaths-exported|$PLUGIN_SDK_SUBPATHS_EXPORTED_OUTCOME" \
            "web-search-provider-boundary|$WEB_SEARCH_PROVIDER_BOUNDARY_OUTCOME" \
            "web-fetch-provider-boundary|$WEB_FETCH_PROVIDER_BOUNDARY_OUTCOME" \
            "extension-src-outside-plugin-sdk-boundary|$EXTENSION_SRC_OUTSIDE_PLUGIN_SDK_BOUNDARY_OUTCOME" \
            "extension-plugin-sdk-internal-boundary|$EXTENSION_PLUGIN_SDK_INTERNAL_BOUNDARY_OUTCOME" \
            "extension-relative-outside-package-boundary|$EXTENSION_RELATIVE_OUTSIDE_PACKAGE_BOUNDARY_OUTCOME" \
            "lint:extensions:channels|$EXTENSION_CHANNEL_LINT_OUTCOME" \
            "lint:extensions:bundled|$EXTENSION_BUNDLED_LINT_OUTCOME" \
            "test:extensions:package-boundary|$EXTENSION_PACKAGE_BOUNDARY_TSC_OUTCOME" \
            "lint:ui:no-raw-window-open|$NO_RAW_WINDOW_OPEN_OUTCOME" \
            "ui:i18n:check|$CONTROL_UI_I18N_OUTCOME" \
            "gateway-watch-regression|$GATEWAY_WATCH_REGRESSION_OUTCOME" \
            "check:import-cycles|$IMPORT_CYCLES_OUTCOME" \
            "check:static-import-sccs|$STATIC_IMPORT_SCCS_OUTCOME"; do
            name="${result%%|*}"
            outcome="${result#*|}"
            if [ "$outcome" != "success" ]; then
              echo "::error title=${name} failed::${name} outcome: ${outcome}"
              failures=1
            fi
          done

          exit "$failures"

  build-smoke:
    name: "build-smoke"
    needs: [preflight, build-artifacts]
    if: always() && needs.preflight.outputs.run_build_smoke == 'true' && (github.event_name != 'push' || needs.build-artifacts.result == 'success')
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 20
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Download dist artifact
        if: github.event_name == 'push'
        uses: actions/download-artifact@v8
        with:
          name: dist-build
          path: dist/

      - name: Build dist
        if: github.event_name != 'push'
        run: pnpm build

      - name: Smoke test CLI launcher help
        run: node openclaw.mjs --help

      - name: Smoke test CLI launcher status json
        run: node openclaw.mjs status --json --timeout 1

      - name: Smoke test built bundled plugin singleton
        run: pnpm test:build:singleton

      - name: Check CLI startup memory
        run: pnpm test:startup:memory

  # Validate docs (format, lint, broken links) only when docs files changed.
  check-docs:
    needs: [preflight]
    if: needs.preflight.outputs.run_check_docs == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 20
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Check docs
        run: pnpm check:docs

  skills-python:
    needs: [preflight]
    if: needs.preflight.outputs.run_skills_python_job == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 20
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Install Python tooling
        run: |
          python -m pip install --upgrade pip
          python -m pip install pytest ruff pyyaml

      - name: Lint Python skill scripts
        run: python -m ruff check skills

      - name: Test skill Python scripts
        run: python -m pytest -q skills

  checks-windows:
    name: ${{ matrix.check_name }}
    needs: [preflight, build-artifacts]
    if: always() && needs.preflight.outputs.run_checks_windows == 'true' && needs.build-artifacts.result == 'success'
    runs-on: blacksmith-32vcpu-windows-2025
    timeout-minutes: 60
    env:
      NODE_OPTIONS: --max-old-space-size=6144
      # Keep total concurrency predictable on the 32 vCPU runner.
      OPENCLAW_VITEST_MAX_WORKERS: 1
      OPENCLAW_TEST_SKIP_FULL_EXTENSIONS_SHARD: 1
    defaults:
      run:
        shell: bash
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.preflight.outputs.checks_windows_matrix) }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Try to exclude workspace from Windows Defender (best-effort)
        shell: pwsh
        run: |
          $cmd = Get-Command Add-MpPreference -ErrorAction SilentlyContinue
          if (-not $cmd) {
            Write-Host "Add-MpPreference not available, skipping Defender exclusions."
            exit 0
          }

          try {
            # Defender sometimes intercepts process spawning (vitest workers). If this fails
            # (eg hardened images), keep going and rely on worker limiting above.
            Add-MpPreference -ExclusionPath "$env:GITHUB_WORKSPACE" -ErrorAction Stop
            Add-MpPreference -ExclusionProcess "node.exe" -ErrorAction Stop
            Write-Host "Defender exclusions applied."
          } catch {
            Write-Warning "Failed to apply Defender exclusions, continuing. $($_.Exception.Message)"
          }

      - name: Setup Node.js
        uses: actions/setup-node@v6
        with:
          node-version: 24.x
          check-latest: false

      - name: Setup pnpm + cache store
        uses: ./.github/actions/setup-pnpm-store-cache
        with:
          pnpm-version: "10.32.1"
          cache-key-suffix: "node24"
          # Sticky disk mount currently retries/fails on every shard and adds ~50s
          # before install while still yielding zero pnpm store reuse.
          # Try exact-key actions/cache restores instead to recover store reuse
          # without the sticky-disk mount penalty.
          use-sticky-disk: "false"
          use-restore-keys: "false"
          use-actions-cache: "true"

      - name: Runtime versions
        run: |
          node -v
          npm -v
          pnpm -v

      - name: Capture node path
        run: echo "NODE_BIN=$(dirname \"$(node -p \"process.execPath\")\")" >> "$GITHUB_ENV"

      - name: Install dependencies
        env:
          CI: true
        run: |
          export PATH="$NODE_BIN:$PATH"
          which node
          node -v
          pnpm -v
          # Persist Windows-native postinstall outputs in the pnpm store so restored
          # caches can skip repeated rebuild/download work on later shards/runs.
          pnpm install --frozen-lockfile --prefer-offline --ignore-scripts=false --config.engine-strict=false --config.enable-pre-post-scripts=true --config.side-effects-cache=true || pnpm install --frozen-lockfile --prefer-offline --ignore-scripts=false --config.engine-strict=false --config.enable-pre-post-scripts=true --config.side-effects-cache=true

      - name: Download dist artifact
        if: matrix.task == 'test'
        uses: actions/download-artifact@v8
        with:
          name: dist-build
          path: dist/

      - name: Download A2UI bundle artifact
        if: matrix.task == 'test'
        uses: actions/download-artifact@v8
        with:
          name: canvas-a2ui-bundle
          path: src/canvas-host/a2ui/

      - name: Run ${{ matrix.task }} (${{ matrix.runtime }})
        env:
          TASK: ${{ matrix.task }}
        shell: bash
        run: |
          set -euo pipefail
          case "$TASK" in
            test)
              # Linux owns the full repo test suite. Keep the Windows runner focused on
              # Windows-native process/path wrappers so platform regressions fail fast.
              pnpm test:windows:ci
              ;;
            *)
              echo "Unsupported Windows checks task: $TASK" >&2
              exit 1
              ;;
          esac

  macos-node:
    name: ${{ matrix.check_name }}
    needs: [preflight, build-artifacts]
    if: always() && needs.preflight.outputs.run_macos_node == 'true' && needs.build-artifacts.result == 'success'
    runs-on: macos-latest
    timeout-minutes: 20
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.preflight.outputs.macos_node_matrix) }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"

      - name: Download dist artifact
        uses: actions/download-artifact@v8
        with:
          name: dist-build
          path: dist/

      - name: Download A2UI bundle artifact
        uses: actions/download-artifact@v8
        with:
          name: canvas-a2ui-bundle
          path: src/canvas-host/a2ui/

      - name: TS tests (macOS)
        env:
          NODE_OPTIONS: --max-old-space-size=4096
          OPENCLAW_VITEST_MAX_WORKERS: 2
          TASK: ${{ matrix.task }}
        shell: bash
        run: |
          set -euo pipefail
          case "$TASK" in
            test)
              # Linux owns the full repo test suite. Keep macOS CI focused on
              # launchd/Homebrew/runtime path coverage and the process-group wrapper.
              pnpm test:macos:ci
              ;;
            *)
              echo "Unsupported macOS node task: $TASK" >&2
              exit 1
              ;;
          esac

  macos-swift:
    name: "macos-swift"
    needs: [preflight]
    if: needs.preflight.outputs.run_macos_swift == 'true'
    runs-on: macos-latest
    timeout-minutes: 20
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Select Xcode 26.1
        run: |
          sudo xcode-select -s /Applications/Xcode_26.1.app
          xcodebuild -version

      - name: Install XcodeGen / SwiftLint / SwiftFormat
        run: brew install xcodegen swiftlint swiftformat

      - name: Cache SwiftPM
        uses: actions/cache@v5
        with:
          path: ~/Library/Caches/org.swift.swiftpm
          key: ${{ runner.os }}-swiftpm-${{ hashFiles('apps/macos/Package.resolved') }}
          restore-keys: |
            ${{ runner.os }}-swiftpm-

      - name: Show toolchain
        run: |
          sw_vers
          xcodebuild -version
          swift --version

      - name: Swift lint
        run: |
          swiftlint --config .swiftlint.yml
          swiftformat --lint apps/macos/Sources --config .swiftformat

      - name: Swift build (release)
        run: |
          set -euo pipefail
          for attempt in 1 2 3; do
            if swift build --package-path apps/macos --configuration release; then
              exit 0
            fi
            echo "swift build failed (attempt $attempt/3). Retrying…"
            sleep $((attempt * 20))
          done
          exit 1

      - name: Swift test
        run: |
          set -euo pipefail
          for attempt in 1 2 3; do
            if swift test --package-path apps/macos --parallel --enable-code-coverage --show-codecov-path; then
              exit 0
            fi
            echo "swift test failed (attempt $attempt/3). Retrying…"
            sleep $((attempt * 20))
          done
          exit 1

  android:
    name: ${{ matrix.check_name }}
    needs: [preflight]
    if: needs.preflight.outputs.run_android_job == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    timeout-minutes: 20
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.preflight.outputs.android_matrix) }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: false
          submodules: false

      - name: Setup Java
        uses: actions/setup-java@v5
        with:
          distribution: temurin
          # Keep sdkmanager on the stable JDK path for Linux CI runners.
          java-version: 17

      - name: Setup Android SDK cmdline-tools
        run: |
          set -euo pipefail
          ANDROID_SDK_ROOT="$HOME/.android-sdk"
          CMDLINE_TOOLS_VERSION="12266719"
          ARCHIVE="commandlinetools-linux-${CMDLINE_TOOLS_VERSION}_late
```

### `.github/workflows/codeql.yml`

- Source path: `.github/workflows/codeql.yml`
- Truncated: `no`

```yaml
name: CodeQL

on:
  workflow_dispatch:

concurrency:
  group: codeql-${{ github.workflow }}-${{ github.event.pull_request.number || github.sha }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"

permissions:
  actions: read
  contents: read
  security-events: write

jobs:
  analyze:
    name: Analyze (${{ matrix.language }})
    runs-on: ${{ matrix.runs_on }}
    strategy:
      fail-fast: false
      matrix:
        include:
          - language: javascript-typescript
            runs_on: blacksmith-16vcpu-ubuntu-2404
            needs_node: true
            needs_python: false
            needs_java: false
            needs_swift_tools: false
            needs_manual_build: false
            needs_autobuild: false
            config_file: ./.github/codeql/codeql-javascript-typescript.yml
          - language: actions
            runs_on: blacksmith-16vcpu-ubuntu-2404
            needs_node: false
            needs_python: false
            needs_java: false
            needs_swift_tools: false
            needs_manual_build: false
            needs_autobuild: false
            config_file: ""
          - language: python
            runs_on: blacksmith-16vcpu-ubuntu-2404
            needs_node: false
            needs_python: true
            needs_java: false
            needs_swift_tools: false
            needs_manual_build: false
            needs_autobuild: false
            config_file: ""
          - language: java-kotlin
            runs_on: blacksmith-16vcpu-ubuntu-2404
            needs_node: false
            needs_python: false
            needs_java: true
            needs_swift_tools: false
            needs_manual_build: true
            needs_autobuild: false
            config_file: ""
          - language: swift
            runs_on: macos-latest
            needs_node: false
            needs_python: false
            needs_java: false
            needs_swift_tools: true
            needs_manual_build: true
            needs_autobuild: false
            config_file: ""
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          submodules: false

      - name: Setup Node environment
        if: matrix.needs_node
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Setup Python
        if: matrix.needs_python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Setup Java
        if: matrix.needs_java
        uses: actions/setup-java@v5
        with:
          distribution: temurin
          java-version: "21"

      - name: Setup Swift build tools
        if: matrix.needs_swift_tools
        run: |
          sudo xcode-select -s /Applications/Xcode_26.1.app
          xcodebuild -version
          brew install xcodegen swiftlint swiftformat
          swift --version

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v4
        with:
          languages: ${{ matrix.language }}
          queries: security-and-quality
          config-file: ${{ matrix.config_file || '' }}

      - name: Autobuild
        if: matrix.needs_autobuild
        uses: github/codeql-action/autobuild@v4

      - name: Build Android for CodeQL
        if: matrix.language == 'java-kotlin'
        working-directory: apps/android
        run: ./gradlew --no-daemon :app:assemblePlayDebug

      - name: Build Swift for CodeQL
        if: matrix.language == 'swift'
        run: |
          set -euo pipefail
          swift build --package-path apps/macos --configuration release
          cd apps/ios
          xcodegen generate
          xcodebuild build \
            -project OpenClaw.xcodeproj \
            -scheme OpenClaw \
            -destination "generic/platform=iOS Simulator" \
            CODE_SIGNING_ALLOWED=NO

      - name: Analyze
        uses: github/codeql-action/analyze@v4
        with:
          category: "/language:${{ matrix.language }}"
```

### `.github/workflows/control-ui-locale-refresh.yml`

- Source path: `.github/workflows/control-ui-locale-refresh.yml`
- Truncated: `no`

```yaml
name: Control UI Locale Refresh

on:
  push:
    branches:
      - main
    paths:
      - ui/src/i18n/locales/en.ts
      - ui/src/i18n/locales/*.ts
      - ui/src/i18n/.i18n/*
      - ui/src/i18n/lib/types.ts
      - ui/src/i18n/lib/registry.ts
      - scripts/control-ui-i18n.ts
      - .github/workflows/control-ui-locale-refresh.yml
  release:
    types:
      - published
  schedule:
    - cron: "23 4 * * *"
  workflow_dispatch:

permissions:
  contents: write

concurrency:
  group: control-ui-locale-refresh
  cancel-in-progress: false

jobs:
  plan:
    if: github.repository == 'openclaw/openclaw' && (github.event_name != 'push' || github.actor != 'github-actions[bot]')
    runs-on: ubuntu-latest
    outputs:
      has_locales: ${{ steps.plan.outputs.has_locales }}
      locales_json: ${{ steps.plan.outputs.locales_json }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          fetch-depth: 0
          persist-credentials: false
          submodules: false

      - name: Plan locale matrix
        id: plan
        env:
          BEFORE_SHA: ${{ github.event.before }}
          EVENT_NAME: ${{ github.event_name }}
        run: |
          set -euo pipefail

          all_locales_json='["zh-CN","zh-TW","pt-BR","de","es","ja-JP","ko","fr","tr","uk","id","pl"]'

          if [ "$EVENT_NAME" != "push" ]; then
            echo "has_locales=true" >> "$GITHUB_OUTPUT"
            echo "locales_json=$all_locales_json" >> "$GITHUB_OUTPUT"
            exit 0
          fi

          before_ref="$BEFORE_SHA"
          if [ -z "$before_ref" ] || [ "$before_ref" = "0000000000000000000000000000000000000000" ]; then
            before_ref="$(git rev-parse HEAD^)"
          fi

          changed_files="$(git diff --name-only "$before_ref" HEAD)"
          echo "changed files:"
          printf '%s\n' "$changed_files"

          if printf '%s\n' "$changed_files" | grep -Eq '^(ui/src/i18n/locales/en\.ts|ui/src/i18n/lib/types\.ts|ui/src/i18n/lib/registry\.ts|scripts/control-ui-i18n\.ts|\.github/workflows/control-ui-locale-refresh\.yml)$'; then
            echo "has_locales=true" >> "$GITHUB_OUTPUT"
            echo "locales_json=$all_locales_json" >> "$GITHUB_OUTPUT"
            exit 0
          fi

          locales_json="$(printf '%s\n' "$changed_files" | node <<'EOF'
          const fs = require("node:fs");
          const changed = fs.readFileSync(0, "utf8").split(/\r?\n/).filter(Boolean);
          const locales = new Set();
          for (const file of changed) {
            let match = file.match(/^ui\/src\/i18n\/locales\/(.+)\.ts$/);
            if (match && match[1] !== "en") {
              locales.add(match[1]);
              continue;
            }
            match = file.match(/^ui\/src\/i18n\/\.i18n\/(.+)\.(?:meta\.json|tm\.jsonl)$/);
            if (match) {
              locales.add(match[1]);
            }
          }
          process.stdout.write(JSON.stringify([...locales]));
          EOF
          )"

          if [ "$locales_json" = "[]" ]; then
            echo "has_locales=false" >> "$GITHUB_OUTPUT"
            echo "locales_json=[]" >> "$GITHUB_OUTPUT"
            exit 0
          fi

          echo "has_locales=true" >> "$GITHUB_OUTPUT"
          echo "locales_json=$locales_json" >> "$GITHUB_OUTPUT"

  refresh:
    needs: plan
    if: github.repository == 'openclaw/openclaw' && needs.plan.outputs.has_locales == 'true'
    strategy:
      fail-fast: false
      max-parallel: 4
      matrix:
        locale: ${{ fromJson(needs.plan.outputs.locales_json) }}
    runs-on: ubuntu-latest
    name: Refresh ${{ matrix.locale }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          persist-credentials: true
          submodules: false

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Ensure translation provider secrets exist
        env:
          OPENAI_API_KEY: ${{ secrets.OPENCLAW_DOCS_I18N_OPENAI_API_KEY || secrets.OPENAI_API_KEY }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          set -euo pipefail
          if [ -z "${OPENAI_API_KEY:-}" ] && [ -z "${ANTHROPIC_API_KEY:-}" ]; then
            echo "Missing OPENCLAW_DOCS_I18N_OPENAI_API_KEY, OPENAI_API_KEY, or ANTHROPIC_API_KEY secret."
            exit 1
          fi

      - name: Refresh control UI locale files
        env:
          OPENAI_API_KEY: ${{ secrets.OPENCLAW_DOCS_I18N_OPENAI_API_KEY || secrets.OPENAI_API_KEY }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENCLAW_CONTROL_UI_I18N_MODEL: gpt-5.4
          OPENCLAW_CONTROL_UI_I18N_THINKING: low
        run: node --import tsx scripts/control-ui-i18n.ts sync --locale "${{ matrix.locale }}" --write

      - name: Commit and push locale updates
        env:
          LOCALE: ${{ matrix.locale }}
          TARGET_BRANCH: ${{ github.event.repository.default_branch }}
        run: |
          set -euo pipefail
          if git diff --quiet -- ui/src/i18n; then
            echo "No control UI locale changes for ${LOCALE}."
            exit 0
          fi

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add -A ui/src/i18n
          git commit --no-verify -m "chore(ui): refresh ${LOCALE} control ui locale"

          for attempt in 1 2 3 4 5; do
            git fetch origin "${TARGET_BRANCH}"
            git rebase --autostash "origin/${TARGET_BRANCH}"
            if git push origin HEAD:"${TARGET_BRANCH}"; then
              exit 0
            fi
            echo "Push attempt ${attempt} for ${LOCALE} failed; retrying."
            sleep $((attempt * 2))
          done

          echo "Failed to push ${LOCALE} locale update after retries."
          exit 1
```

### `.github/workflows/docker-release.yml`

- Source path: `.github/workflows/docker-release.yml`
- Truncated: `no`

```yaml
name: Docker Release

on:
  push:
    tags:
      - "v*"
    paths-ignore:
      - "docs/**"
      - "**/*.md"
      - "**/*.mdx"
      - ".agents/**"
      - "skills/**"
  workflow_dispatch:
    inputs:
      tag:
        description: Existing release tag to backfill (for example v2026.3.22)
        required: true
        type: string

concurrency:
  group: ${{ github.event_name == 'workflow_dispatch' && format('docker-release-manual-{0}', inputs.tag) || format('docker-release-push-{0}', github.run_id) }}
  cancel-in-progress: false

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  validate_manual_backfill:
    if: github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-24.04
    permissions:
      contents: read
    steps:
      - name: Validate tag input format
        env:
          RELEASE_TAG: ${{ inputs.tag }}
        run: |
          set -euo pipefail
          if [[ ! "${RELEASE_TAG}" =~ ^v[0-9]{4}\.[1-9][0-9]*\.[1-9][0-9]*(-beta\.[1-9][0-9]*)?$ ]]; then
            echo "Invalid release tag: ${RELEASE_TAG}"
            exit 1
          fi

      - name: Checkout selected tag
        uses: actions/checkout@v6
        with:
          ref: refs/tags/${{ inputs.tag }}
          fetch-depth: 0

  approve_manual_backfill:
    if: github.event_name == 'workflow_dispatch'
    needs: validate_manual_backfill
    # WARNING: KEEP MANUAL BACKFILLS GATED BY THE docker-release ENVIRONMENT.
    runs-on: ubuntu-24.04
    environment: docker-release
    steps:
      - name: Approve Docker backfill
        env:
          RELEASE_TAG: ${{ inputs.tag }}
        run: echo "Approved Docker backfill for $RELEASE_TAG"

  # KEEP THIS WORKFLOW ON GITHUB-HOSTED RUNNERS.
  # DO NOT MOVE IT BACK TO BLACKSMITH WITHOUT RE-VALIDATING TAG BUILDS AND BACKFILLS.
  # Build amd64 images (default + slim share the build stage cache)
  build-amd64:
    needs: [approve_manual_backfill]
    if: ${{ always() && (github.event_name != 'workflow_dispatch' || needs.approve_manual_backfill.result == 'success') }}
    # WARNING: DO NOT REVERT THIS TO A BLACKSMITH RUNNER WITHOUT RE-VALIDATING TAG BACKFILLS.
    runs-on: ubuntu-24.04
    permissions:
      packages: write
      contents: read
    outputs:
      digest: ${{ steps.build.outputs.digest }}
      slim-digest: ${{ steps.build-slim.outputs.digest }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          ref: ${{ github.event_name == 'workflow_dispatch' && format('refs/tags/{0}', inputs.tag) || github.ref }}
          fetch-depth: 0

      - name: Set up Docker Builder
        uses: docker/setup-buildx-action@v4

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v4
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.repository_owner }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Resolve image tags (amd64)
        id: tags
        shell: bash
        env:
          IMAGE: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          SOURCE_REF: ${{ github.event_name == 'workflow_dispatch' && format('refs/tags/{0}', inputs.tag) || github.ref }}
        run: |
          set -euo pipefail
          tags=()
          slim_tags=()
          if [[ "${SOURCE_REF}" == "refs/heads/main" ]]; then
            tags+=("${IMAGE}:main-amd64")
            slim_tags+=("${IMAGE}:main-slim-amd64")
          fi
          if [[ "${SOURCE_REF}" == refs/tags/v* ]]; then
            version="${SOURCE_REF#refs/tags/v}"
            tags+=("${IMAGE}:${version}-amd64")
            slim_tags+=("${IMAGE}:${version}-slim-amd64")
          fi
          if [[ ${#tags[@]} -eq 0 ]]; then
            echo "::error::No amd64 tags resolved for ref ${SOURCE_REF}"
            exit 1
          fi
          {
            echo "value<<EOF"
            printf "%s\n" "${tags[@]}"
            echo "EOF"
          } >> "$GITHUB_OUTPUT"
          {
            echo "slim<<EOF"
            printf "%s\n" "${slim_tags[@]}"
            echo "EOF"
          } >> "$GITHUB_OUTPUT"

      - name: Resolve OCI labels (amd64)
        id: labels
        shell: bash
        env:
          SOURCE_REF: ${{ github.event_name == 'workflow_dispatch' && format('refs/tags/{0}', inputs.tag) || github.ref }}
        run: |
          set -euo pipefail
          source_sha="$(git rev-parse HEAD)"
          version="${source_sha}"
          if [[ "${SOURCE_REF}" == "refs/heads/main" ]]; then
            version="main"
          fi
          if [[ "${SOURCE_REF}" == refs/tags/v* ]]; then
            version="${SOURCE_REF#refs/tags/v}"
          fi
          created="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
          {
            echo "value<<EOF"
            echo "org.opencontainers.image.revision=${source_sha}"
            echo "org.opencontainers.image.version=${version}"
            echo "org.opencontainers.image.created=${created}"
            echo "EOF"
          } >> "$GITHUB_OUTPUT"

      - name: Build and push amd64 image
        id: build
        # WARNING: KEEP THE OFFICIAL DOCKER ACTION HERE; DO NOT SWITCH THIS BACK TO BLACKSMITH BLINDLY.
        uses: docker/build-push-action@v6
        with:
          context: .
          platforms: linux/amd64
          cache-from: type=gha,scope=docker-release-amd64
          cache-to: type=gha,mode=max,scope=docker-release-amd64
          tags: ${{ steps.tags.outputs.value }}
          labels: ${{ steps.labels.outputs.value }}
          provenance: false
          push: true

      - name: Build and push amd64 slim image
        id: build-slim
        # WARNING: KEEP THE OFFICIAL DOCKER ACTION HERE; DO NOT SWITCH THIS BACK TO BLACKSMITH BLINDLY.
        uses: docker/build-push-action@v6
        with:
          context: .
          platforms: linux/amd64
          cache-from: type=gha,scope=docker-release-amd64
          cache-to: type=gha,mode=max,scope=docker-release-amd64
          build-args: |
            OPENCLAW_VARIANT=slim
          tags: ${{ steps.tags.outputs.slim }}
          labels: ${{ steps.labels.outputs.value }}
          provenance: false
          push: true

  # Build arm64 images (default + slim share the build stage cache)
  build-arm64:
    needs: [approve_manual_backfill]
    if: ${{ always() && (github.event_name != 'workflow_dispatch' || needs.approve_manual_backfill.result == 'success') }}
    # WARNING: DO NOT REVERT THIS TO A BLACKSMITH RUNNER WITHOUT RE-VALIDATING TAG BACKFILLS.
    runs-on: ubuntu-24.04-arm
    permissions:
      packages: write
      contents: read
    outputs:
      digest: ${{ steps.build.outputs.digest }}
      slim-digest: ${{ steps.build-slim.outputs.digest }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          ref: ${{ github.event_name == 'workflow_dispatch' && format('refs/tags/{0}', inputs.tag) || github.ref }}
          fetch-depth: 0

      - name: Set up Docker Builder
        uses: docker/setup-buildx-action@v4

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v4
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.repository_owner }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Resolve image tags (arm64)
        id: tags
        shell: bash
        env:
          IMAGE: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          SOURCE_REF: ${{ github.event_name == 'workflow_dispatch' && format('refs/tags/{0}', inputs.tag) || github.ref }}
        run: |
          set -euo pipefail
          tags=()
          slim_tags=()
          if [[ "${SOURCE_REF}" == "refs/heads/main" ]]; then
            tags+=("${IMAGE}:main-arm64")
            slim_tags+=("${IMAGE}:main-slim-arm64")
          fi
          if [[ "${SOURCE_REF}" == refs/tags/v* ]]; then
            version="${SOURCE_REF#refs/tags/v}"
            tags+=("${IMAGE}:${version}-arm64")
            slim_tags+=("${IMAGE}:${version}-slim-arm64")
          fi
          if [[ ${#tags[@]} -eq 0 ]]; then
            echo "::error::No arm64 tags resolved for ref ${SOURCE_REF}"
            exit 1
          fi
          {
            echo "value<<EOF"
            printf "%s\n" "${tags[@]}"
            echo "EOF"
          } >> "$GITHUB_OUTPUT"
          {
            echo "slim<<EOF"
            printf "%s\n" "${slim_tags[@]}"
            echo "EOF"
          } >> "$GITHUB_OUTPUT"

      - name: Resolve OCI labels (arm64)
        id: labels
        shell: bash
        env:
          SOURCE_REF: ${{ github.event_name == 'workflow_dispatch' && format('refs/tags/{0}', inputs.tag) || github.ref }}
        run: |
          set -euo pipefail
          source_sha="$(git rev-parse HEAD)"
          version="${source_sha}"
          if [[ "${SOURCE_REF}" == "refs/heads/main" ]]; then
            version="main"
          fi
          if [[ "${SOURCE_REF}" == refs/tags/v* ]]; then
            version="${SOURCE_REF#refs/tags/v}"
          fi
          created="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
          {
            echo "value<<EOF"
            echo "org.opencontainers.image.revision=${source_sha}"
            echo "org.opencontainers.image.version=${version}"
            echo "org.opencontainers.image.created=${created}"
            echo "EOF"
          } >> "$GITHUB_OUTPUT"

      - name: Build and push arm64 image
        id: build
        # WARNING: KEEP THE OFFICIAL DOCKER ACTION HERE; DO NOT SWITCH THIS BACK TO BLACKSMITH BLINDLY.
        uses: docker/build-push-action@v6
        with:
          context: .
          platforms: linux/arm64
          cache-from: type=gha,scope=docker-release-arm64
          cache-to: type=gha,mode=max,scope=docker-release-arm64
          tags: ${{ steps.tags.outputs.value }}
          labels: ${{ steps.labels.outputs.value }}
          provenance: false
          push: true

      - name: Build and push arm64 slim image
        id: build-slim
        # WARNING: KEEP THE OFFICIAL DOCKER ACTION HERE; DO NOT SWITCH THIS BACK TO BLACKSMITH BLINDLY.
        uses: docker/build-push-action@v6
        with:
          context: .
          platforms: linux/arm64
          cache-from: type=gha,scope=docker-release-arm64
          cache-to: type=gha,mode=max,scope=docker-release-arm64
          build-args: |
            OPENCLAW_VARIANT=slim
          tags: ${{ steps.tags.outputs.slim }}
          labels: ${{ steps.labels.outputs.value }}
          provenance: false
          push: true

  # Create multi-platform manifests
  create-manifest:
    needs: [approve_manual_backfill, build-amd64, build-arm64]
    if: ${{ always() && needs.build-amd64.result == 'success' && needs.build-arm64.result == 'success' && (github.event_name != 'workflow_dispatch' || needs.approve_manual_backfill.result == 'success') }}
    # WARNING: DO NOT REVERT THIS TO A BLACKSMITH RUNNER WITHOUT RE-VALIDATING TAG BACKFILLS.
    runs-on: ubuntu-24.04
    permissions:
      packages: write
      contents: read
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          ref: ${{ github.event_name == 'workflow_dispatch' && format('refs/tags/{0}', inputs.tag) || github.ref }}
          fetch-depth: 0

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v4
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.repository_owner }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Resolve manifest tags
        id: tags
        shell: bash
        env:
          IMAGE: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          SOURCE_REF: ${{ github.event_name == 'workflow_dispatch' && format('refs/tags/{0}', inputs.tag) || github.ref }}
          IS_MANUAL_BACKFILL: ${{ github.event_name == 'workflow_dispatch' && '1' || '0' }}
        run: |
          set -euo pipefail
          tags=()
          slim_tags=()
          if [[ "${SOURCE_REF}" == "refs/heads/main" ]]; then
            tags+=("${IMAGE}:main")
            slim_tags+=("${IMAGE}:main-slim")
          fi
          if [[ "${SOURCE_REF}" == refs/tags/v* ]]; then
            version="${SOURCE_REF#refs/tags/v}"
            tags+=("${IMAGE}:${version}")
            slim_tags+=("${IMAGE}:${version}-slim")
            # Manual backfills should only republish the requested version tags.
            if [[ "${IS_MANUAL_BACKFILL}" != "1" && "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[0-9]+)?$ ]]; then
              tags+=("${IMAGE}:latest")
              slim_tags+=("${IMAGE}:slim")
            fi
          fi
          if [[ ${#tags[@]} -eq 0 ]]; then
            echo "::error::No manifest tags resolved for ref ${SOURCE_REF}"
            exit 1
          fi
          {
            echo "value<<EOF"
            printf "%s\n" "${tags[@]}"
            echo "EOF"
          } >> "$GITHUB_OUTPUT"
          {
            echo "slim<<EOF"
            printf "%s\n" "${slim_tags[@]}"
            echo "EOF"
          } >> "$GITHUB_OUTPUT"

      - name: Create and push default manifest
        shell: bash
        run: |
          set -euo pipefail
          mapfile -t tags <<< "${{ steps.tags.outputs.value }}"
          args=()
          for tag in "${tags[@]}"; do
            [ -z "$tag" ] && continue
            args+=("-t" "$tag")
          done
          docker buildx imagetools create "${args[@]}" \
            ${{ needs.build-amd64.outputs.digest }} \
            ${{ needs.build-arm64.outputs.digest }}

      - name: Create and push slim manifest
        shell: bash
        run: |
          set -euo pipefail
          mapfile -t tags <<< "${{ steps.tags.outputs.slim }}"
          args=()
          for tag in "${tags[@]}"; do
            [ -z "$tag" ] && continue
            args+=("-t" "$tag")
          done
          docker buildx imagetools create "${args[@]}" \
            ${{ needs.build-amd64.outputs.slim-digest }} \
            ${{ needs.build-arm64.outputs.slim-digest }}
```

### `.github/workflows/docs-sync-publish.yml`

- Source path: `.github/workflows/docs-sync-publish.yml`
- Truncated: `no`

```yaml
name: Docs Sync Publish Repo

on:
  push:
    branches:
      - main
    paths:
      - docs/**
      - scripts/docs-sync-publish.mjs
      - .github/workflows/docs-sync-publish.yml
  workflow_dispatch:

permissions:
  contents: read

jobs:
  sync-publish-repo:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout source repo
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Clone publish repo
        env:
          OPENCLAW_DOCS_SYNC_TOKEN: ${{ secrets.OPENCLAW_DOCS_SYNC_TOKEN }}
        run: |
          set -euo pipefail
          git clone \
            "https://x-access-token:${OPENCLAW_DOCS_SYNC_TOKEN}@github.com/openclaw/docs.git" \
            publish

      - name: Sync docs into publish repo
        run: |
          node scripts/docs-sync-publish.mjs \
            --target "$GITHUB_WORKSPACE/publish" \
            --source-repo "$GITHUB_REPOSITORY" \
            --source-sha "$GITHUB_SHA"

      - name: Commit publish repo sync
        working-directory: publish
        run: |
          set -euo pipefail
          if git diff --quiet -- docs .openclaw-sync; then
            echo "No publish-repo changes."
            exit 0
          fi

          git config user.name "openclaw-docs-sync[bot]"
          git config user.email "openclaw-docs-sync[bot]@users.noreply.github.com"
          git add docs .openclaw-sync
          git commit -m "chore(sync): mirror docs from $GITHUB_REPOSITORY@$GITHUB_SHA"
          for attempt in 1 2 3 4 5; do
            git fetch origin main
            git rebase origin/main
            if git push origin HEAD:main; then
              exit 0
            fi
            echo "Push attempt ${attempt} failed; retrying."
            sleep $((attempt * 2))
          done

          echo "Failed to push publish-repo sync after retries."
          exit 1
```

### `.github/workflows/docs-translate-trigger-release.yml`

- Source path: `.github/workflows/docs-translate-trigger-release.yml`
- Truncated: `no`

```yaml
name: Docs Trigger Locale Translate On Release

on:
  release:
    types:
      - published

permissions:
  contents: read

jobs:
  dispatch-translate:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger locale translates in publish repo
        env:
          GH_TOKEN: ${{ secrets.OPENCLAW_DOCS_SYNC_TOKEN }}
          RELEASE_TAG: ${{ github.event.release.tag_name }}
        run: |
          set -euo pipefail
          for event_type in \
            translate-zh-cn-release \
            translate-ja-jp-release \
            translate-es-release \
            translate-pt-br-release \
            translate-ko-release \
            translate-de-release \
            translate-fr-release \
            translate-ar-release \
            translate-it-release \
            translate-tr-release \
            translate-uk-release \
            translate-id-release \
            translate-pl-release
          do
            gh api repos/openclaw/docs/dispatches \
              --method POST \
              -f event_type="${event_type}" \
              -f client_payload[release_tag]="${RELEASE_TAG}" \
              -f client_payload[source_repository]="${GITHUB_REPOSITORY}" \
              -f client_payload[source_sha]="${GITHUB_SHA}"
          done
```

### `.github/workflows/install-smoke.yml`

- Source path: `.github/workflows/install-smoke.yml`
- Truncated: `no`

```yaml
name: Install Smoke

on:
  push:
    branches: [main]
  pull_request:
    types: [opened, reopened, synchronize, ready_for_review, converted_to_draft]
  workflow_dispatch:

concurrency:
  group: ${{ github.event_name == 'pull_request' && format('{0}-{1}', github.workflow, github.event.pull_request.number) || format('{0}-{1}', github.workflow, github.run_id) }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"

jobs:
  preflight:
    if: github.event_name != 'pull_request' || !github.event.pull_request.draft
    runs-on: blacksmith-16vcpu-ubuntu-2404
    outputs:
      docs_only: ${{ steps.manifest.outputs.docs_only }}
      run_install_smoke: ${{ steps.manifest.outputs.run_install_smoke }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          fetch-depth: 1
          fetch-tags: false
          persist-credentials: false
          submodules: false

      - name: Ensure preflight base commit
        uses: ./.github/actions/ensure-base-commit
        with:
          base-sha: ${{ github.event_name == 'push' && github.event.before || github.event.pull_request.base.sha }}
          fetch-ref: ${{ github.event_name == 'push' && github.ref_name || github.event.pull_request.base.ref }}

      - name: Detect docs-only changes
        id: docs_scope
        uses: ./.github/actions/detect-docs-changes

      - name: Detect changed smoke scope
        id: changed_scope
        if: steps.docs_scope.outputs.docs_only != 'true'
        shell: bash
        run: |
          set -euo pipefail

          if [ "${{ github.event_name }}" = "push" ]; then
            BASE="${{ github.event.before }}"
          else
            BASE="${{ github.event.pull_request.base.sha }}"
          fi

          node scripts/ci-changed-scope.mjs --base "$BASE" --head HEAD

      - name: Setup Node environment
        if: steps.docs_scope.outputs.docs_only != 'true'
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          install-deps: "false"
          use-sticky-disk: "false"

      - name: Build install-smoke CI manifest
        id: manifest
        env:
          OPENCLAW_CI_DOCS_ONLY: ${{ steps.docs_scope.outputs.docs_only }}
          OPENCLAW_CI_RUN_CHANGED_SMOKE: ${{ steps.changed_scope.outputs.run_changed_smoke || 'false' }}
        run: |
          docs_only="${OPENCLAW_CI_DOCS_ONLY:-false}"
          run_changed_smoke="${OPENCLAW_CI_RUN_CHANGED_SMOKE:-false}"
          run_install_smoke=false
          if [ "$docs_only" != "true" ] && [ "$run_changed_smoke" = "true" ]; then
            run_install_smoke=true
          fi
          {
            echo "docs_only=$docs_only"
            echo "run_install_smoke=$run_install_smoke"
          } >> "$GITHUB_OUTPUT"

  install-smoke:
    needs: [preflight]
    if: needs.preflight.outputs.run_install_smoke == 'true'
    runs-on: blacksmith-16vcpu-ubuntu-2404
    env:
      DOCKER_BUILD_SUMMARY: "false"
      DOCKER_BUILD_RECORD_UPLOAD: "false"
    steps:
      - name: Checkout CLI
        uses: actions/checkout@v6

      - name: Set up Docker Builder
        uses: docker/setup-buildx-action@v4

      # Blacksmith can fall back to the local docker driver, which rejects gha
      # cache export/import. Keep smoke builds driver-agnostic.
      - name: Build root Dockerfile smoke image
        uses: useblacksmith/build-push-action@v2
        with:
          context: .
          file: ./Dockerfile
          build-args: |
            OPENCLAW_DOCKER_APT_UPGRADE=0
          tags: openclaw-dockerfile-smoke:local
          load: true
          push: false
          provenance: false

      - name: Run root Dockerfile CLI smoke
        run: |
          docker run --rm --entrypoint sh openclaw-dockerfile-smoke:local -lc 'which openclaw && openclaw --version'

      # This smoke validates that the build-arg path preinstalls the matrix
      # runtime deps declared by the plugin and that matrix discovery stays
      # healthy in the final runtime image.
      - name: Build extension Dockerfile smoke image
        uses: useblacksmith/build-push-action@v2
        with:
          context: .
          file: ./Dockerfile
          build-args: |
            OPENCLAW_DOCKER_APT_UPGRADE=0
            OPENCLAW_EXTENSIONS=matrix
          tags: openclaw-ext-smoke:local
          load: true
          push: false
          provenance: false

      - name: Smoke test Dockerfile with matrix extension build arg
        run: |
          docker run --rm --entrypoint sh openclaw-ext-smoke:local -lc '
            which openclaw &&
            openclaw --version &&
            node -e "
              const Module = require(\"node:module\");
              const matrixPackage = require(\"/app/extensions/matrix/package.json\");
              const requireFromMatrix = Module.createRequire(\"/app/extensions/matrix/package.json\");
              const runtimeDeps = Object.keys(matrixPackage.dependencies ?? {});
              if (runtimeDeps.length === 0) {
                throw new Error(
                  \"matrix package has no declared runtime dependencies; smoke cannot validate install mirroring\",
                );
              }
              for (const dep of runtimeDeps) {
                requireFromMatrix.resolve(dep);
              }
              const { spawnSync } = require(\"node:child_process\");
              const run = spawnSync(\"openclaw\", [\"plugins\", \"list\", \"--json\"], { encoding: \"utf8\" });
              if (run.status !== 0) {
                process.stderr.write(run.stderr || run.stdout || \"plugins list failed\\n\");
                process.exit(run.status ?? 1);
              }
              const parsed = JSON.parse(run.stdout);
              const matrix = (parsed.plugins || []).find((entry) => entry.id === \"matrix\");
              if (!matrix) {
                throw new Error(\"matrix plugin missing from bundled plugin list\");
              }
              const matrixDiag = (parsed.diagnostics || []).filter(
                (diag) =>
                  typeof diag.source === \"string\" &&
                  diag.source.includes(\"/extensions/matrix\") &&
                  typeof diag.message === \"string\" &&
                  diag.message.includes(\"extension entry escapes package directory\"),
              );
              if (matrixDiag.length > 0) {
                throw new Error(
                  \"unexpected matrix diagnostics: \" +
                    matrixDiag.map((diag) => diag.message).join(\"; \"),
                );
              }
            "
          '

      - name: Build installer smoke image
        uses: useblacksmith/build-push-action@v2
        with:
          context: ./scripts/docker
          file: ./scripts/docker/install-sh-smoke/Dockerfile
          tags: openclaw-install-smoke:local
          load: true
          push: false
          provenance: false

      - name: Build installer non-root image
        if: github.event_name != 'pull_request'
        uses: useblacksmith/build-push-action@v2
        with:
          context: ./scripts/docker
          file: ./scripts/docker/install-sh-nonroot/Dockerfile
          tags: openclaw-install-nonroot:local
          load: true
          push: false
          provenance: false

      - name: Setup Node environment for local pack smoke
        uses: ./.github/actions/setup-node-env
        with:
          install-bun: "false"
          install-deps: "true"
          use-sticky-disk: "false"

      - name: Run installer docker tests
        env:
          OPENCLAW_INSTALL_URL: https://openclaw.ai/install.sh
          OPENCLAW_INSTALL_CLI_URL: https://openclaw.ai/install-cli.sh
          OPENCLAW_NO_ONBOARD: "1"
          OPENCLAW_INSTALL_SMOKE_SKIP_CLI: "1"
          OPENCLAW_INSTALL_SMOKE_SKIP_IMAGE_BUILD: "1"
          OPENCLAW_INSTALL_NONROOT_SKIP_IMAGE_BUILD: ${{ github.event_name == 'pull_request' && '0' || '1' }}
          OPENCLAW_INSTALL_SMOKE_SKIP_NONROOT: ${{ github.event_name == 'pull_request' && '1' || '0' }}
          OPENCLAW_INSTALL_SMOKE_SKIP_PREVIOUS: "1"
        run: bash scripts/test-install-sh-docker.sh
```

### `.github/workflows/labeler.yml`

- Source path: `.github/workflows/labeler.yml`
- Truncated: `no`

```yaml
name: Labeler

on:
  pull_request_target: # zizmor: ignore[dangerous-triggers] maintainer-owned triage workflow; no untrusted checkout or PR code execution
    types: [opened, synchronize, reopened, edited]
  issues:
    types: [opened, edited]
  workflow_dispatch:
    inputs:
      max_prs:
        description: "Maximum number of open PRs to process (0 = all)"
        required: false
        default: "200"
      per_page:
        description: "PRs per page (1-100)"
        required: false
        default: "50"

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref || github.run_id }}
  cancel-in-progress: ${{ github.event_name == 'pull_request_target' }}

permissions: {}

jobs:
  label:
    permissions:
      contents: read
      pull-requests: write
    runs-on: blacksmith-16vcpu-ubuntu-2404
    steps:
      - uses: actions/create-github-app-token@v2
        id: app-token
        continue-on-error: true
        with:
          app-id: "2729701"
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
      - uses: actions/create-github-app-token@v2
        id: app-token-fallback
        if: steps.app-token.outcome == 'failure'
        with:
          app-id: "2971289"
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY_FALLBACK }}
      - uses: actions/labeler@v6
        with:
          configuration-path: .github/labeler.yml
          repo-token: ${{ steps.app-token.outputs.token || steps.app-token-fallback.outputs.token }}
          sync-labels: true
      - name: Apply PR size label
        uses: actions/github-script@v8
        with:
          github-token: ${{ steps.app-token.outputs.token || steps.app-token-fallback.outputs.token }}
          script: |
            const pullRequest = context.payload.pull_request;
            if (!pullRequest) {
              return;
            }

            const sizeLabels = ["size: XS", "size: S", "size: M", "size: L", "size: XL"];
            const labelColor = "b76e79";

            for (const label of sizeLabels) {
              try {
                await github.rest.issues.getLabel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  name: label,
                });
              } catch (error) {
                if (error?.status !== 404) {
                  throw error;
                }
                await github.rest.issues.createLabel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  name: label,
                  color: labelColor,
                });
              }
            }

            const files = await github.paginate(github.rest.pulls.listFiles, {
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: pullRequest.number,
              per_page: 100,
            });

            const excludedLockfiles = new Set(["pnpm-lock.yaml", "package-lock.json", "yarn.lock", "bun.lockb"]);
            const totalChangedLines = files.reduce((total, file) => {
              const path = file.filename ?? "";
              if (path === "docs.acp.md" || path.startsWith("docs/") || excludedLockfiles.has(path)) {
                return total;
              }
              return total + (file.additions ?? 0) + (file.deletions ?? 0);
            }, 0);

            let targetSizeLabel = "size: XL";
            if (totalChangedLines < 50) {
              targetSizeLabel = "size: XS";
            } else if (totalChangedLines < 200) {
              targetSizeLabel = "size: S";
            } else if (totalChangedLines < 500) {
              targetSizeLabel = "size: M";
            } else if (totalChangedLines < 1000) {
              targetSizeLabel = "size: L";
            }

            const currentLabels = await github.paginate(github.rest.issues.listLabelsOnIssue, {
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: pullRequest.number,
              per_page: 100,
            });

            for (const label of currentLabels) {
              const name = label.name ?? "";
              if (!sizeLabels.includes(name)) {
                continue;
              }
              if (name === targetSizeLabel) {
                continue;
              }
              await github.rest.issues.removeLabel({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: pullRequest.number,
                name,
              });
            }

            await github.rest.issues.addLabels({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: pullRequest.number,
              labels: [targetSizeLabel],
            });
      - name: Apply maintainer or trusted-contributor label
        uses: actions/github-script@v8
        with:
          github-token: ${{ steps.app-token.outputs.token || steps.app-token-fallback.outputs.token }}
          script: |
            const login = context.payload.pull_request?.user?.login;
            if (!login) {
              return;
            }

            const repo = `${context.repo.owner}/${context.repo.repo}`;
            // const trustedLabel = "trusted-contributor";
            // const experiencedLabel = "experienced-contributor";
            // const trustedThreshold = 4;
            // const experiencedThreshold = 10;

            let isMaintainer = false;
            try {
              const membership = await github.rest.teams.getMembershipForUserInOrg({
                org: context.repo.owner,
                team_slug: "maintainer",
                username: login,
              });
              isMaintainer = membership?.data?.state === "active";
            } catch (error) {
              if (error?.status !== 404) {
                throw error;
              }
            }

            if (isMaintainer) {
              await github.rest.issues.addLabels({
                ...context.repo,
                issue_number: context.payload.pull_request.number,
                labels: ["maintainer"],
              });
              return;
            }

            // trusted-contributor and experienced-contributor labels disabled.
            // const mergedQuery = `repo:${repo} is:pr is:merged author:${login}`;
            // let mergedCount = 0;
            // try {
            //   const merged = await github.rest.search.issuesAndPullRequests({
            //     q: mergedQuery,
            //     per_page: 1,
            //   });
            //   mergedCount = merged?.data?.total_count ?? 0;
            // } catch (error) {
            //   if (error?.status !== 422) {
            //     throw error;
            //   }
            //   core.warning(`Skipping merged search for ${login}; treating as 0.`);
            // }
            //
            // if (mergedCount >= experiencedThreshold) {
            //   await github.rest.issues.addLabels({
            //     ...context.repo,
            //     issue_number: context.payload.pull_request.number,
            //     labels: [experiencedLabel],
            //   });
            //   return;
            // }
            //
            // if (mergedCount >= trustedThreshold) {
            //   await github.rest.issues.addLabels({
            //     ...context.repo,
            //     issue_number: context.payload.pull_request.number,
            //     labels: [trustedLabel],
            //   });
            // }
      - name: Apply beta-blocker title label
        uses: actions/github-script@v8
        with:
          github-token: ${{ steps.app-token.outputs.token || steps.app-token-fallback.outputs.token }}
          script: |
            const pullRequest = context.payload.pull_request;
            if (!pullRequest) {
              return;
            }

            const labelName = "beta-blocker";
            const matchesBetaBlocker = /\bbeta blocker\b/i.test(pullRequest.title ?? "");

            try {
              await github.rest.issues.getLabel({
                owner: context.repo.owner,
                repo: context.repo.repo,
                name: labelName,
              });
            } catch (error) {
              if (error?.status !== 404) {
                throw error;
              }
              core.info(`Skipping ${labelName} labeling because the label does not exist in the repository.`);
              return;
            }

            const currentLabels = await github.paginate(github.rest.issues.listLabelsOnIssue, {
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: pullRequest.number,
              per_page: 100,
            });
            const hasLabel = currentLabels.some((label) => label.name === labelName);

            if (matchesBetaBlocker && !hasLabel) {
              await github.rest.issues.addLabels({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: pullRequest.number,
                labels: [labelName],
              });
              return;
            }

            if (!matchesBetaBlocker && hasLabel) {
              await github.rest.issues.removeLabel({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: pullRequest.number,
                name: labelName,
              });
            }
      - name: Apply too-many-prs label
        uses: actions/github-script@v8
        with:
          github-token: ${{ steps.app-token.outputs.token || steps.app-token-fallback.outputs.token }}
          script: |
            const pullRequest = context.payload.pull_request;
            if (!pullRequest) {
              return;
            }

            const activePrLimitLabel = "r: too-many-prs";
            const activePrLimitOverrideLabel = "r: too-many-prs-override";
            const activePrLimit = 10;
            const labelColor = "B60205";
            const labelDescription = `Author has more than ${activePrLimit} active PRs in this repo`;
            const authorLogin = pullRequest.user?.login;
            if (!authorLogin) {
              return;
            }

            const currentLabels = await github.paginate(github.rest.issues.listLabelsOnIssue, {
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: pullRequest.number,
              per_page: 100,
            });

            const labelNames = new Set(
              currentLabels
                .map((label) => (typeof label === "string" ? label : label?.name))
                .filter((name) => typeof name === "string"),
            );

            if (labelNames.has(activePrLimitOverrideLabel)) {
              if (labelNames.has(activePrLimitLabel)) {
                try {
                  await github.rest.issues.removeLabel({
                    owner: context.repo.owner,
                    repo: context.repo.repo,
                    issue_number: pullRequest.number,
                    name: activePrLimitLabel,
                  });
                } catch (error) {
                  if (error?.status !== 404) {
                    throw error;
                  }
                }
              }
              return;
            }

            const ensureLabelExists = async () => {
              try {
                await github.rest.issues.getLabel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  name: activePrLimitLabel,
                });
              } catch (error) {
                if (error?.status !== 404) {
                  throw error;
                }
                await github.rest.issues.createLabel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  name: activePrLimitLabel,
                  color: labelColor,
                  description: labelDescription,
                });
              }
            };

            const isPrivilegedAuthor = async () => {
              if (pullRequest.author_association === "OWNER") {
                return true;
              }

              let isMaintainer = false;
              try {
                const membership = await github.rest.teams.getMembershipForUserInOrg({
                  org: context.repo.owner,
                  team_slug: "maintainer",
                  username: authorLogin,
                });
                isMaintainer = membership?.data?.state === "active";
              } catch (error) {
                if (error?.status !== 404) {
                  throw error;
                }
              }

              if (isMaintainer) {
                return true;
              }

              try {
                const permission = await github.rest.repos.getCollaboratorPermissionLevel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  username: authorLogin,
                });
                const roleName = (permission?.data?.role_name ?? "").toLowerCase();
                return roleName === "admin" || roleName === "maintain";
              } catch (error) {
                if (error?.status !== 404) {
                  throw error;
                }
              }

              return false;
            };

            if (await isPrivilegedAuthor()) {
              if (labelNames.has(activePrLimitLabel)) {
                try {
                  await github.rest.issues.removeLabel({
                    owner: context.repo.owner,
                    repo: context.repo.repo,
                    issue_number: pullRequest.number,
                    name: activePrLimitLabel,
                  });
                } catch (error) {
                  if (error?.status !== 404) {
                    throw error;
                  }
                }
              }
              return;
            }

            let openPrCount = 0;
            try {
              const result = await github.rest.search.issuesAndPullRequests({
                q: `repo:${context.repo.owner}/${context.repo.repo} is:pr is:open author:${authorLogin}`,
                per_page: 1,
              });
              openPrCount = result?.data?.total_count ?? 0;
            } catch (error) {
              if (error?.status !== 422) {
                throw error;
              }
              core.warning(`Skipping open PR count for ${authorLogin}; treating as 0.`);
            }

            if (openPrCount > activePrLimit) {
              await ensureLabelExists();
              if (!labelNames.has(activePrLimitLabel)) {
                await github.rest.issues.addLabels({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pullRequest.number,
                  labels: [activePrLimitLabel],
                });
              }
              return;
            }

            if (labelNames.has(activePrLimitLabel)) {
              try {
                await github.rest.issues.removeLabel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: pullRequest.number,
                  name: activePrLimitLabel,
                });
              } catch (error) {
                if (error?.status !== 404) {
                  throw error;
                }
              }
            }

  backfill-pr-labels:
    if: github.event_name == 'workflow_dispatch'
    permissions:
      contents: read
      pull-requests: write
    runs-on: blacksmith-16vcpu-ubuntu-2404
    steps:
      - uses: actions/create-github-app-token@v2
        id: app-token
        continue-on-error: true
        with:
          app-id: "2729701"
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
      - uses: actions/create-github-app-token@v2
        id: app-token-fallback
        if: steps.app-token.outcome == 'failure'
        with:
          app-id: "2971289"
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY_FALLBACK }}
      - name: Backfill PR labels
        uses: actions/github-script@v8
        with:
          github-token: ${{ steps.app-token.outputs.token || steps.app-token-fallback.outputs.token }}
          script: |
            const owner = context.repo.owner;
            const repo = context.repo.repo;
            const repoFull = `${owner}/${repo}`;
            const inputs = context.payload.inputs ?? {};
            const maxPrsInput = inputs.max_prs ?? "200";
            const perPageInput = inputs.per_page ?? "50";
            const parsedMaxPrs = Number.parseInt(maxPrsInput, 10);
            const parsedPerPage = Number.parseInt(perPageInput, 10);
            const maxPrs = Number.isFinite(parsedMaxPrs) ? parsedMaxPrs : 200;
            const perPage = Number.isFinite(parsedPerPage) ? Math.min(100, Math.max(1, parsedPerPage)) : 50;
            const processAll = maxPrs <= 0;
            const maxCount = processAll ? Number.POSITIVE_INFINITY : Math.max(1, maxPrs);

            const sizeLabels = ["size: XS", "size: S", "size: M", "size: L", "size: XL"];
            const betaBlockerLabel = "beta-blocker";
            const labelColor = "b76e79";
            // const trustedLabel = "trusted-contributor";
            // const experiencedLabel = "experienced-contributor";
            // const trustedThreshold = 4;
            // const experiencedThreshold = 10;

            const contributorCache = new Map();

            async function ensureSizeLabels() {
              for (const label of sizeLabels) {
                try {
                  await github.rest.issues.getLabel({
                    owner,
                    repo,
                    name: label,
                  });
                } catch (error) {
                  if (error?.status !== 404) {
                    throw error;
                  }
                  await github.rest.issues.createLabel({
                    owner,
                    repo,
                    name: label,
                    color: labelColor,
                  });
                }
              }
            }

            async function hasBetaBlockerLabel() {
              try {
                await github.rest.issues.getLabel({
                  owner,
                  repo,
                  name: betaBlockerLabel,
                });
                return true;
              } catch (error) {
                if (error?.status !== 404) {
                  throw error;
                }
                return false;
              }
            }

            async function resolveContributorLabel(login) {
              if (contributorCache.has(login)) {
                return contributorCache.get(login);
              }

              let isMaintainer = false;
              try {
                const membership = await github.rest.teams.getMembershipForUserInOrg({
                  org: owner,
                  team_slug: "maintainer",
                  username: login,
                });
                isMaintainer = membership?.data?.state === "active";
              } catch (error) {
                if (error?.status !== 404) {
                  throw error;
                }
              }

              if (isMaintainer) {
                contributorCache.set(login, "maintainer");
                return "maintainer";
              }

              // trusted-contributor and experienced-contributor labels disabled.
              // const mergedQuery = `repo:${repoFull} is:pr is:merged author:${login}`;
              // let mergedCount = 0;
              // try {
              //   const merged = await github.rest.search.issuesAndPullRequests({
              //     q: mergedQuery,
              //     per_page: 1,
              //   });
              //   mergedCount = merged?.data?.total_count ?? 0;
              // } catch (error) {
              //   if (error?.status !== 422) {
              //     throw error;
              //   }
              //   core.warning(`Skipping merged search for ${login}; treating as 0.`);
              // }

              const label = null;
              // if (mergedCount >= experiencedThreshold) {
              //   label = experiencedLabel;
              // } else if (mergedCount >= trustedThreshold) {
              //   label = trustedLabel;
              // }

              contributorCache.set(login, label);
              return label;
            }

            async function applySizeLabel(pullRequest, currentLabels, labelNames) {
              const files = await github.paginate(github.rest.pulls.listFiles, {
                owner,
                repo,
                pull_number: pullRequest.number,
                per_page: 100,
              });

              const excludedLockfiles = new Set(["pnpm-lock.yaml", "package-lock.json", "yarn.lock", "bun.lockb"]);
              const totalChangedLines = files.reduce((total, file) => {
                const path = file.filename ?? "";
                if (path === "docs.acp.md" || path.startsWith("docs/") || excludedLockfiles.has(path)) {
                  return total;
                }
                return total + (file.additions ?? 0) + (file.deletions ?? 0);
              }, 0);

              let targetSizeLabel = "size: XL";
              if (totalChangedLines < 50) {
                targetSizeLabel = "size: XS";
              } else if (totalChangedLines < 200) {
                targetSizeLabel = "size: S";
              } else if (totalChangedLines < 500) {
                targetSizeLabel = "size: M";
              } else if (totalChangedLines < 1000) {
                targetSizeLabel = "size: L";
              }

              for (const label of currentLabels) {
                const name = label.name ?? "";
                if (!sizeLabels.includes(name)) {
                  continue;
                }
                if (name === targetSizeLabel) {
                  continue;
                }
                await github.rest.issues.removeLabel({
                  owner,
                  repo,
                  issue_number: pullRequest.number,
                  name,
                });
                labelNames.delete(name);
              }

              if (!labelNames.has(targetSizeLabel)) {
                await github.rest.issues.addLabels({
                  owner,
                  repo,
                  issue_number: pullRequest.number,
                  labels: [targetSizeLabel],
                });
                labelNames.add(targetSizeLabel);
              }
            }

            async function applyContributorLabel(pullRequest, labelNames) {
              const login = pullRequest.user?.login;
              if (!login) {
                return;
              }

              const label = await resolveContributorLabel(login);
              if (!label) {
                return;
              }

              if (labelNames.has(label)) {
                return;
              }

              await github.rest.issues.addLabels({
                owner,
                repo,
                issue_number: pullRequest.number,
                labels: [label],
              });
              labelNames.add(label);
            }

            async function applyBetaBlockerTitleLabel(pullRequest, labelNames) {
              const matchesBetaBlocker = /\bbeta blocker\b/i.test(pullRequest.title ?? "");

              if (matchesBetaBlocker) {
                if (!labelNames.has(betaBlockerLabel)) {
                  await github.rest.issues.addLabels({
                    owner,
                    repo,
                    issue_number: pullRequest.number,
                    labels: [betaBlockerLabel],
                  });
                  labelNames.add(betaBlockerLabel);
                }
                return;
              }

              if (!labelNames.has(betaBlockerLabel)) {
                return;
              }

              await github.rest.issues.removeLabel({
                owner,
                repo,
                issue_number: pullRequest.number,
                name: betaBlockerLabel,
              });
              labelNames.delete(betaBlockerLabel);
            }

            await ensureSizeLabels();
            const betaBlockerLabelExists = await hasBetaBlockerLabel();

            let page = 1;
            let processed = 0;

            while (processed < maxCount) {
              const remaining = maxCount - processed;
              const pageSize = processAll ? perPage : Math.min(perPage, remaining);
              const { data: pullRequests } = await github.rest.pulls.list({
                owner,
                repo,
                state: "open",
                per_page: pageSize,
                page,
              });

              if (pullRequests.length === 0) {
                break;
              }

              for (const pullRequest of pullRequests) {
                if (!processAll && processed >= maxCount) {
                  break;
                }

                const currentLabels = await github.paginate(github.rest.issues.listLabelsOnIssue, {
                  owner,
                  repo,
                  issue_number: pullRequest.number,
                  per_page: 100,
                });

                const labelNames = new Set(
                  currentLabels.map((label) => label.name).filter((name) => typeof name === "string"),
                );

                await applySizeLabel(pullRequest, currentLabels, labelNames);
                await applyContributorLabel(pullRequest, labelNames);
                if (betaBlockerLabelExists) {
                  await applyBetaBlockerTitleLabel(pullRequest, labelNames);
                }

                processed += 1;
              }

              if (pullRequests.length < pageSize) {
                break;
              }

              page += 1;
            }

            core.info(`Processed ${processed} pull requests.`);

  label-issues:
    permissions:
      issues: write
    runs-on: blacksmith-16vcpu-ubuntu-2404
    steps:
      - uses: actions/create-github-app-token@v2
        id: app-token
        continue-on-error: true
        with:
          app-id: "2729701"
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY }}
      - uses: actions/create-github-app-token@v2
        id: app-token-fallback
        if: steps.app-token.outcome == 'failure'
        with:
          app-id: "2971289"
          private-key: ${{ secrets.GH_APP_PRIVATE_KEY_FALLBACK }}
      - name: Apply maintainer or trusted-contributor label
        uses: actions/github-script@v8
        with:
          github-token: ${{ steps.app-token.outputs.token || steps.app-token-fallback.outputs.token }}
          script: |
            const login = context.payload.issue?.user?.login;
            if (!login) {
              return;
            }

            const repo = `${context.repo.owner}/${context.repo.repo}`;
            // const trustedLabel = "trusted-contributor";
            // const experiencedLabel = "experienced-contributor";
            // const trustedThreshold = 4;
            // const experiencedThreshold = 10;

            let isMaintainer = false;
            try {
              const membership = await github.rest.teams.getMembershipForUserInOrg({
                org: context.repo.owner,
                team_slug: "maintainer",
                username: login,
              });
              isMaintainer = membership?.data?.state === "active";
            } catch (error) {
              if (error?.status !== 404) {
                throw error;
              }
            }

            if (isMaintainer) {
              await github.rest.issues.addLabels({
                ...context.repo,
                issue_number: context.payload.issue.number,
                labels: ["maintainer"],
              });
              return;
            }

            // trusted-contributor and experienced-contributor labels disabled.
            // const mergedQuery = `repo:${repo} is:pr is:merged author:${login}`;
            // let mergedCount = 0;
            // try {
            //   const merged = await github.rest.search.issuesAndPullRequests({
            //     q: mergedQuery,
            //     per_page: 1,
            //   });
            //   mergedCount = merged?.data?.total_count ?? 0;
            // } catch (error) {
            //   if (error?.status !== 422) {
            //     throw error;
            //   }
            //   core.warning(`Skipping merged search for ${login}; treating as 0.`);
            // }
            //
            // if (mergedCount >= experiencedThreshold) {
            //   await github.rest.issues.addLabels({
            //     ...context.repo,
            //     issue_number: context.payload.issue.number,
            //     labels: [experiencedLabel],
            //   });
            //   return;
            // }
            //
            // if (mergedCount >= trustedThreshold) {
            //   await github.rest.issues.addLabels({
            //     ...context.repo,
            //     issue_number: context.payload.issue.number,
            //     labels: [trustedLabel],
            //   });
            // }
      - name: Apply beta-blocker title label
        uses: actions/github-script@v8
        with:
          github-token: ${{ steps.app-token.outputs.token || steps.app-token-fallback.outputs.token }}
          script: |
            const issue = context.payload.issue;
            if (!issue || issue.pull_request) {
              return;
            }

            const labelName = "beta-blocker";
            const matchesBetaBlocker = /^beta blocker:/i.test(issue.title ?? "");

            try {
              await github.rest.issues.getLabel({
                owner: context.repo.owner,
                repo: context.repo.repo,
                name: labelName,
              });
            } catch (error) {
              if (error?.status !== 404) {
                throw error;
              }
              core.info(`Skipping ${labelName} labeling because the label does not exist in the repository.`);
              return;
            }

            const currentLabels = await github.paginate(github.rest.issues.listLabelsOnIssue, {
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: issue.number,
              per_page: 100,
            });
            const hasLabel = currentLabels.some((label) => label.name === labelName);

            if (matchesBetaBlocker && !hasLabel) {
              await github.rest.issues.addLabels({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                labels: [labelName],
              });
              return;
            }

            if (!matchesBetaBlocker && hasLabel) {
              await github.rest.issues.removeLabel({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                name: labelName,
              });
            }
```

### `.github/workflows/macos-release.yml`

- Source path: `.github/workflows/macos-release.yml`
- Truncated: `no`

```yaml
name: macOS Release

on:
  workflow_dispatch:
    inputs:
      tag:
        description: Existing release tag to validate for macOS release handoff (for example v2026.3.22 or v2026.3.22-beta.1)
        required: true
        type: string
      preflight_only:
        description: Retained for operator compatibility; this public workflow is validation-only
        required: true
        default: true
        type: boolean

concurrency:
  group: macos-release-${{ inputs.tag }}
  cancel-in-progress: false

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"
  NODE_VERSION: "24.x"
  PNPM_VERSION: "10.32.1"

jobs:
  validate_macos_release_request:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Validate tag input format
        env:
          RELEASE_TAG: ${{ inputs.tag }}
        run: |
          set -euo pipefail
          if [[ ! "${RELEASE_TAG}" =~ ^v[0-9]{4}\.[1-9][0-9]*\.[1-9][0-9]*((-beta\.[1-9][0-9]*)|(-[1-9][0-9]*))?$ ]]; then
            echo "Invalid release tag format: ${RELEASE_TAG}"
            exit 1
          fi

      - name: Checkout selected tag
        uses: actions/checkout@v6
        with:
          ref: refs/tags/${{ inputs.tag }}
          fetch-depth: 0

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          node-version: ${{ env.NODE_VERSION }}
          pnpm-version: ${{ env.PNPM_VERSION }}
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Ensure matching GitHub release exists
        env:
          GH_TOKEN: ${{ github.token }}
          RELEASE_TAG: ${{ inputs.tag }}
        run: gh release view "$RELEASE_TAG" --repo "$GITHUB_REPOSITORY" >/dev/null

      - name: Build
        run: pnpm build

      - name: Build Control UI
        run: pnpm ui:build

      - name: Validate release tag and package metadata
        env:
          RELEASE_TAG: ${{ inputs.tag }}
          RELEASE_MAIN_REF: origin/main
        run: |
          set -euo pipefail
          RELEASE_SHA=$(git rev-parse HEAD)
          export RELEASE_SHA RELEASE_TAG RELEASE_MAIN_REF
          git fetch --no-tags origin +refs/heads/main:refs/remotes/origin/main
          pnpm release:openclaw:npm:check

      - name: Summarize next step
        env:
          RELEASE_TAG: ${{ inputs.tag }}
        run: |
          {
            echo "## Public macOS validation only"
            echo
            echo "This workflow validates the public release handoff and still builds JS artifacts needed for release checks."
            echo "It does not sign, notarize, or upload macOS assets."
            echo
            echo "Next step:"
            echo "- Run \`openclaw/releases-private/.github/workflows/openclaw-macos-validate.yml\` with tag \`${RELEASE_TAG}\` and wait for the private mac validation lane to pass."
            echo "- Run \`openclaw/releases-private/.github/workflows/openclaw-macos-publish.yml\` with tag \`${RELEASE_TAG}\` and \`preflight_only=true\` for the full private mac preflight."
            echo "- For the real publish path, run the same private mac publish workflow from \`main\` with the successful private preflight \`preflight_run_id\` so it promotes the prepared artifacts instead of rebuilding them."
            echo "- For stable releases, also download \`macos-appcast-${RELEASE_TAG}\` from the successful private run and commit \`appcast.xml\` back to \`main\` in \`openclaw/openclaw\`."
          } >> "$GITHUB_STEP_SUMMARY"
```

### `.github/workflows/openclaw-npm-release.yml`

- Source path: `.github/workflows/openclaw-npm-release.yml`
- Truncated: `no`

```yaml
name: OpenClaw NPM Release

on:
  workflow_dispatch:
    inputs:
      tag:
        description: Release tag to publish (for example v2026.3.22, v2026.3.22-beta.1, or fallback v2026.3.22-1)
        required: true
        type: string
      preflight_only:
        description: Run validation/build only and skip the gated publish job
        required: true
        default: false
        type: boolean
      preflight_run_id:
        description: Existing successful preflight workflow run id to promote without rebuilding
        required: false
        type: string
      npm_dist_tag:
        description: npm dist-tag to publish to for stable releases
        required: true
        default: beta
        type: choice
        options:
          - beta
          - latest
      promote_beta_to_latest:
        description: Skip publish and promote the stable version already on npm beta to latest
        required: true
        default: false
        type: boolean

concurrency:
  group: openclaw-npm-release-${{ github.event_name == 'workflow_dispatch' && format('{0}-{1}-{2}', inputs.tag, inputs.npm_dist_tag, inputs.promote_beta_to_latest) || github.ref }}
  cancel-in-progress: false

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"
  NODE_VERSION: "24.x"
  PNPM_VERSION: "10.32.1"

jobs:
  preflight_openclaw_npm:
    if: ${{ inputs.preflight_only && !inputs.promote_beta_to_latest }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Validate tag input format
        env:
          RELEASE_TAG: ${{ inputs.tag }}
          RELEASE_NPM_DIST_TAG: ${{ inputs.npm_dist_tag }}
        run: |
          set -euo pipefail
          if [[ ! "${RELEASE_TAG}" =~ ^v[0-9]{4}\.[1-9][0-9]*\.[1-9][0-9]*((-beta\.[1-9][0-9]*)|(-[1-9][0-9]*))?$ ]]; then
            echo "Invalid release tag format: ${RELEASE_TAG}"
            exit 1
          fi
          if [[ "${RELEASE_TAG}" == *"-beta."* && "${RELEASE_NPM_DIST_TAG}" != "beta" ]]; then
            echo "Beta prerelease tags must publish to npm dist-tag beta."
            exit 1
          fi

      - name: Forbid preflight artifact promotion on validation-only runs
        if: ${{ inputs.preflight_only && inputs.preflight_run_id != '' }}
        run: |
          echo "preflight_run_id is only valid for real publish runs."
          exit 1

      - name: Checkout
        uses: actions/checkout@v6
        with:
          ref: refs/tags/${{ inputs.tag }}
          fetch-depth: 0

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          node-version: ${{ env.NODE_VERSION }}
          pnpm-version: ${{ env.PNPM_VERSION }}
          install-bun: "true"
          use-sticky-disk: "false"

      - name: Ensure version is not already published
        env:
          PREFLIGHT_ONLY: ${{ inputs.preflight_only }}
        run: |
          set -euo pipefail
          PACKAGE_VERSION=$(node -p "require('./package.json').version")

          if npm view "openclaw@${PACKAGE_VERSION}" version >/dev/null 2>&1; then
            if [[ "${PREFLIGHT_ONLY}" == "true" ]]; then
              echo "openclaw@${PACKAGE_VERSION} is already published on npm; continuing because preflight_only=true."
              exit 0
            fi
            echo "openclaw@${PACKAGE_VERSION} is already published on npm."
            exit 1
          fi

          echo "Publishing openclaw@${PACKAGE_VERSION}"

      - name: Check
        env:
          OPENCLAW_LOCAL_CHECK: "0"
        run: pnpm check

      - name: Build
        run: pnpm build

      - name: Build Control UI
        run: pnpm ui:build

      - name: Validate release tag and package metadata
        if: ${{ inputs.preflight_run_id == '' }}
        env:
          OPENCLAW_NPM_RELEASE_SKIP_PACK_CHECK: "1"
          RELEASE_TAG: ${{ inputs.tag }}
          RELEASE_MAIN_REF: origin/main
          OPENCLAW_NPM_PUBLISH_TAG: ${{ inputs.npm_dist_tag }}
        run: |
          set -euo pipefail
          RELEASE_SHA=$(git rev-parse HEAD)
          export RELEASE_SHA RELEASE_TAG RELEASE_MAIN_REF
          # Fetch the full main ref so merge-base ancestry checks keep working
          # for older tagged commits that are still contained in main.
          git fetch --no-tags origin +refs/heads/main:refs/remotes/origin/main
          pnpm release:openclaw:npm:check

      - name: Verify release contents
        run: pnpm release:check

      - name: Validate live cache credentials
        if: ${{ github.ref == 'refs/heads/main' }}
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          set -euo pipefail
          if [[ -z "${OPENAI_API_KEY}" ]]; then
            echo "Missing OPENAI_API_KEY secret for release live cache validation." >&2
            exit 1
          fi
          if [[ -z "${ANTHROPIC_API_KEY}" ]]; then
            echo "Missing ANTHROPIC_API_KEY secret for release live cache validation." >&2
            exit 1
          fi

      - name: Verify live prompt cache floors
        if: ${{ github.ref == 'refs/heads/main' }}
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENCLAW_LIVE_CACHE_TEST: "1"
          OPENCLAW_LIVE_TEST: "1"
        run: pnpm test:live:cache

      - name: Pack prepared npm tarball
        id: packed_tarball
        env:
          OPENCLAW_PREPACK_PREPARED: "1"
          RELEASE_TAG: ${{ inputs.tag }}
          RELEASE_NPM_DIST_TAG: ${{ inputs.npm_dist_tag }}
        run: |
          set -euo pipefail
          PACK_OUTPUT="$RUNNER_TEMP/npm-pack-output.txt"
          npm pack --json 2>&1 | tee "$PACK_OUTPUT"
          PACK_PATH="$(node - "$PACK_OUTPUT" <<'NODE'
          const fs = require("node:fs");
          const input = fs.readFileSync(process.argv[2], "utf8");

          function arrayEndFrom(start) {
            let depth = 0;
            let inString = false;
            let escape = false;
            for (let i = start; i < input.length; i += 1) {
              const char = input[i];
              if (inString) {
                if (escape) {
                  escape = false;
                } else if (char === "\\") {
                  escape = true;
                } else if (char === "\"") {
                  inString = false;
                }
                continue;
              }
              if (char === "\"") {
                inString = true;
              } else if (char === "[") {
                depth += 1;
              } else if (char === "]") {
                depth -= 1;
                if (depth === 0) {
                  return i + 1;
                }
              }
            }
            return -1;
          }

          for (let start = input.indexOf("["); start !== -1; start = input.indexOf("[", start + 1)) {
            const end = arrayEndFrom(start);
            if (end === -1) {
              continue;
            }
            try {
              const parsed = JSON.parse(input.slice(start, end));
              const first = Array.isArray(parsed) ? parsed[0] : null;
              if (first && typeof first.filename === "string" && first.filename) {
                process.stdout.write(first.filename);
                process.exit(0);
              }
            } catch {
              // Keep scanning; npm lifecycle output can legally precede the JSON.
            }
          }

          console.error("Could not find npm pack --json output with a filename.");
          process.exit(1);
          NODE
          )"
          if [[ -z "$PACK_PATH" || ! -f "$PACK_PATH" ]]; then
            echo "npm pack did not produce a tarball file." >&2
            exit 1
          fi
          RELEASE_SHA="$(git rev-parse HEAD)"
          ARTIFACT_DIR="$RUNNER_TEMP/openclaw-npm-preflight"
          rm -rf "$ARTIFACT_DIR"
          mkdir -p "$ARTIFACT_DIR"
          cp "$PACK_PATH" "$ARTIFACT_DIR/"
          printf '%s\n' "$RELEASE_TAG" > "$ARTIFACT_DIR/release-tag.txt"
          printf '%s\n' "$RELEASE_SHA" > "$ARTIFACT_DIR/release-sha.txt"
          printf '%s\n' "$RELEASE_NPM_DIST_TAG" > "$ARTIFACT_DIR/release-npm-dist-tag.txt"
          echo "dir=$ARTIFACT_DIR" >> "$GITHUB_OUTPUT"

      - name: Upload prepared npm publish bundle
        uses: actions/upload-artifact@v7
        with:
          name: openclaw-npm-preflight-${{ inputs.tag }}
          path: ${{ steps.packed_tarball.outputs.dir }}
          if-no-files-found: error

  validate_publish_request:
    if: ${{ !inputs.preflight_only && !inputs.promote_beta_to_latest }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Require main workflow ref for publish
        env:
          WORKFLOW_REF: ${{ github.ref }}
        run: |
          set -euo pipefail
          if [[ "${WORKFLOW_REF}" != "refs/heads/main" ]]; then
            echo "Real publish runs must be dispatched from main. Use preflight_only=true for branch validation."
            exit 1
          fi

      - name: Require preflight artifact promotion on real publish
        env:
          PREFLIGHT_RUN_ID: ${{ inputs.preflight_run_id }}
        run: |
          set -euo pipefail
          if [[ -z "${PREFLIGHT_RUN_ID}" ]]; then
            echo "Real publish requires preflight_run_id from a successful npm preflight run." >&2
            exit 1
          fi

  publish_openclaw_npm:
    # npm trusted publishing + provenance requires a GitHub-hosted runner.
    needs: [validate_publish_request]
    if: ${{ !inputs.preflight_only && !inputs.promote_beta_to_latest }}
    runs-on: ubuntu-latest
    environment: npm-release
    permissions:
      actions: read
      contents: read
      id-token: write
    steps:
      - name: Validate tag input format
        env:
          RELEASE_TAG: ${{ inputs.tag }}
          RELEASE_NPM_DIST_TAG: ${{ inputs.npm_dist_tag }}
        run: |
          set -euo pipefail
          if [[ ! "${RELEASE_TAG}" =~ ^v[0-9]{4}\.[1-9][0-9]*\.[1-9][0-9]*((-beta\.[1-9][0-9]*)|(-[1-9][0-9]*))?$ ]]; then
            echo "Invalid release tag format: ${RELEASE_TAG}"
            exit 1
          fi
          if [[ "${RELEASE_TAG}" == *"-beta."* && "${RELEASE_NPM_DIST_TAG}" != "beta" ]]; then
            echo "Beta prerelease tags must publish to npm dist-tag beta."
            exit 1
          fi

      - name: Checkout
        uses: actions/checkout@v6
        with:
          ref: refs/tags/${{ inputs.tag }}
          fetch-depth: 0

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          node-version: ${{ env.NODE_VERSION }}
          pnpm-version: ${{ env.PNPM_VERSION }}
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Ensure version is not already published
        run: |
          set -euo pipefail
          PACKAGE_VERSION=$(node -p "require('./package.json').version")

          if npm view "openclaw@${PACKAGE_VERSION}" version >/dev/null 2>&1; then
            echo "openclaw@${PACKAGE_VERSION} is already published on npm."
            exit 1
          fi

          echo "Publishing openclaw@${PACKAGE_VERSION}"

      - name: Verify preflight run metadata
        env:
          GH_TOKEN: ${{ github.token }}
          PREFLIGHT_RUN_ID: ${{ inputs.preflight_run_id }}
        run: |
          set -euo pipefail
          RUN_JSON="$(gh run view "$PREFLIGHT_RUN_ID" --repo "$GITHUB_REPOSITORY" --json workflowName,headBranch,event,conclusion,url)"
          printf '%s' "$RUN_JSON" | node -e 'const fs = require("node:fs"); const run = JSON.parse(fs.readFileSync(0, "utf8")); const checks = [["workflowName", "OpenClaw NPM Release"], ["headBranch", "main"], ["event", "workflow_dispatch"], ["conclusion", "success"]]; for (const [key, expected] of checks) { if (run[key] !== expected) { console.error(`Referenced npm preflight run ${process.env.PREFLIGHT_RUN_ID} must have ${key}=${expected}, got ${run[key] ?? "<missing>"}.`); process.exit(1); } } console.log(`Using npm preflight run ${process.env.PREFLIGHT_RUN_ID}: ${run.url}`);'

      - name: Download prepared npm tarball
        uses: actions/download-artifact@v8
        with:
          name: openclaw-npm-preflight-${{ inputs.tag }}
          path: preflight-tarball
          repository: ${{ github.repository }}
          run-id: ${{ inputs.preflight_run_id }}
          github-token: ${{ github.token }}

      - name: Validate release tag and package metadata
        if: ${{ inputs.preflight_run_id == '' }}
        env:
          OPENCLAW_NPM_RELEASE_SKIP_PACK_CHECK: "1"
          RELEASE_TAG: ${{ inputs.tag }}
          RELEASE_MAIN_REF: origin/main
        run: |
          set -euo pipefail
          RELEASE_SHA=$(git rev-parse HEAD)
          export RELEASE_SHA RELEASE_TAG RELEASE_MAIN_REF
          # Fetch the full main ref so merge-base ancestry checks keep working
          # for older tagged commits that are still contained in main.
          git fetch --no-tags origin +refs/heads/main:refs/remotes/origin/main
          pnpm release:openclaw:npm:check

      - name: Verify prepared tarball provenance
        env:
          RELEASE_TAG: ${{ inputs.tag }}
          RELEASE_NPM_DIST_TAG: ${{ inputs.npm_dist_tag }}
        run: |
          set -euo pipefail
          EXPECTED_RELEASE_SHA="$(git rev-parse HEAD)"
          TAG_FILE="preflight-tarball/release-tag.txt"
          SHA_FILE="preflight-tarball/release-sha.txt"
          NPM_DIST_TAG_FILE="preflight-tarball/release-npm-dist-tag.txt"
          if [[ ! -f "$TAG_FILE" || ! -f "$SHA_FILE" || ! -f "$NPM_DIST_TAG_FILE" ]]; then
            echo "Prepared preflight metadata is missing." >&2
            ls -la preflight-tarball >&2 || true
            exit 1
          fi
          ARTIFACT_RELEASE_TAG="$(tr -d '\r\n' < "$TAG_FILE")"
          ARTIFACT_RELEASE_SHA="$(tr -d '\r\n' < "$SHA_FILE")"
          ARTIFACT_RELEASE_NPM_DIST_TAG="$(tr -d '\r\n' < "$NPM_DIST_TAG_FILE")"
          if [[ "$ARTIFACT_RELEASE_TAG" != "$RELEASE_TAG" ]]; then
            echo "Prepared preflight tag mismatch: expected $RELEASE_TAG, got $ARTIFACT_RELEASE_TAG" >&2
            exit 1
          fi
          if [[ "$ARTIFACT_RELEASE_SHA" != "$EXPECTED_RELEASE_SHA" ]]; then
            echo "Prepared preflight SHA mismatch: expected $EXPECTED_RELEASE_SHA, got $ARTIFACT_RELEASE_SHA" >&2
            exit 1
          fi
          if [[ "$ARTIFACT_RELEASE_NPM_DIST_TAG" != "$RELEASE_NPM_DIST_TAG" ]]; then
            echo "Prepared preflight npm dist-tag mismatch: expected $RELEASE_NPM_DIST_TAG, got $ARTIFACT_RELEASE_NPM_DIST_TAG" >&2
            exit 1
          fi

      - name: Resolve publish tarball
        id: publish_tarball
        run: |
          set -euo pipefail
          TARBALL_PATH="$(find preflight-tarball -type f -name '*.tgz' -print | sort | tail -n 1)"
          if [[ -z "$TARBALL_PATH" ]]; then
            echo "Prepared preflight tarball not found." >&2
            ls -la preflight-tarball >&2 || true
            exit 1
          fi
          echo "path=$TARBALL_PATH" >> "$GITHUB_OUTPUT"

      - name: Publish
        env:
          OPENCLAW_PREPACK_PREPARED: "1"
          OPENCLAW_NPM_PUBLISH_TAG: ${{ inputs.npm_dist_tag }}
        run: |
          set -euo pipefail
          publish_target="${{ steps.publish_tarball.outputs.path }}"
          if [[ -n "${publish_target}" ]]; then
            publish_target="./${publish_target}"
          fi
          bash scripts/openclaw-npm-publish.sh --publish "${publish_target}"

  promote_beta_to_latest:
    if: ${{ inputs.promote_beta_to_latest }}
    runs-on: ubuntu-latest
    environment: npm-release
    permissions:
      contents: read
    steps:
      - name: Require main workflow ref for promotion
        env:
          WORKFLOW_REF: ${{ github.ref }}
        run: |
          set -euo pipefail
          if [[ "${WORKFLOW_REF}" != "refs/heads/main" ]]; then
            echo "Promotion runs must be dispatched from main."
            exit 1
          fi

      - name: Validate promotion inputs
        env:
          PREFLIGHT_ONLY: ${{ inputs.preflight_only }}
          PREFLIGHT_RUN_ID: ${{ inputs.preflight_run_id }}
          RELEASE_NPM_DIST_TAG: ${{ inputs.npm_dist_tag }}
        run: |
          set -euo pipefail
          if [[ "${PREFLIGHT_ONLY}" == "true" ]]; then
            echo "Promotion mode cannot run with preflight_only=true."
            exit 1
          fi
          if [[ -n "${PREFLIGHT_RUN_ID}" ]]; then
            echo "Promotion mode does not use preflight_run_id."
            exit 1
          fi
          if [[ "${RELEASE_NPM_DIST_TAG}" != "beta" ]]; then
            echo "Promotion mode expects npm_dist_tag=beta because it moves beta to latest without publishing."
            exit 1
          fi

      - name: Validate stable tag input format
        env:
          RELEASE_TAG: ${{ inputs.tag }}
        run: |
          set -euo pipefail
          if [[ ! "${RELEASE_TAG}" =~ ^v[0-9]{4}\.[1-9][0-9]*\.[1-9][0-9]*(-[1-9][0-9]*)?$ ]]; then
            echo "Invalid stable release tag format: ${RELEASE_TAG}" >&2
            exit 1
          fi
          echo "RELEASE_VERSION=${RELEASE_TAG#v}" >> "$GITHUB_ENV"

      - name: Checkout
        uses: actions/checkout@v6

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          node-version: ${{ env.NODE_VERSION }}
          pnpm-version: ${{ env.PNPM_VERSION }}
          install-bun: "false"
          use-sticky-disk: "false"
          install-deps: "false"

      - name: Validate npm dist-tags
        env:
          RELEASE_VERSION: ${{ env.RELEASE_VERSION }}
        run: |
          set -euo pipefail
          beta_version="$(npm view openclaw dist-tags.beta)"
          latest_version="$(npm view openclaw dist-tags.latest)"

          echo "Current beta dist-tag: ${beta_version}"
          echo "Current latest dist-tag: ${latest_version}"

          if [[ "${beta_version}" != "${RELEASE_VERSION}" ]]; then
            echo "npm beta points at ${beta_version}, expected ${RELEASE_VERSION}." >&2
            exit 1
          fi

          if ! npm view "openclaw@${RELEASE_VERSION}" version >/dev/null 2>&1; then
            echo "openclaw@${RELEASE_VERSION} is not published on npm." >&2
            exit 1
          fi

      - name: Promote beta to latest
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
          RELEASE_VERSION: ${{ env.RELEASE_VERSION }}
        run: |
          set -euo pipefail
          printf '//registry.npmjs.org/:_authToken=%s\n' "${NODE_AUTH_TOKEN}" > "${HOME}/.npmrc"
          npm whoami >/dev/null
          npm dist-tag add "openclaw@${RELEASE_VERSION}" latest
          promoted_latest="$(npm view openclaw dist-tags.latest)"
          if [[ "${promoted_latest}" != "${RELEASE_VERSION}" ]]; then
            echo "npm latest points at ${promoted_latest}, expected ${RELEASE_VERSION} after promotion." >&2
            exit 1
          fi
          echo "Promoted openclaw@${RELEASE_VERSION} from beta to latest."
```

### `.github/workflows/plugin-clawhub-release.yml`

- Source path: `.github/workflows/plugin-clawhub-release.yml`
- Truncated: `no`

```yaml
name: Plugin ClawHub Release

on:
  workflow_dispatch:
    inputs:
      publish_scope:
        description: Publish the selected plugins or all ClawHub-publishable plugins from the workflow ref
        required: true
        default: selected
        type: choice
        options:
          - selected
          - all-publishable
      plugins:
        description: Comma-separated plugin package names to publish when publish_scope=selected
        required: false
        type: string

concurrency:
  group: plugin-clawhub-release-${{ github.sha }}
  cancel-in-progress: false

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"
  NODE_VERSION: "24.x"
  PNPM_VERSION: "10.32.1"
  CLAWHUB_REGISTRY: "https://clawhub.ai"
  CLAWHUB_REPOSITORY: "openclaw/clawhub"
  # Pinned to a reviewed ClawHub commit so release behavior stays reproducible.
  CLAWHUB_REF: "4af2bd50a71465683dbf8aa269af764b9d39bdf5"

jobs:
  preview_plugins_clawhub:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      ref_sha: ${{ steps.ref.outputs.sha }}
      has_candidates: ${{ steps.plan.outputs.has_candidates }}
      candidate_count: ${{ steps.plan.outputs.candidate_count }}
      skipped_published_count: ${{ steps.plan.outputs.skipped_published_count }}
      matrix: ${{ steps.plan.outputs.matrix }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          ref: ${{ github.sha }}
          fetch-depth: 0

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          node-version: ${{ env.NODE_VERSION }}
          pnpm-version: ${{ env.PNPM_VERSION }}
          install-bun: "false"
          use-sticky-disk: "false"

      - name: Resolve checked-out ref
        id: ref
        run: echo "sha=$(git rev-parse HEAD)" >> "$GITHUB_OUTPUT"

      - name: Validate ref is on main
        run: |
          set -euo pipefail
          git fetch --no-tags origin +refs/heads/main:refs/remotes/origin/main
          git merge-base --is-ancestor HEAD origin/main

      - name: Validate publishable plugin metadata
        env:
          PUBLISH_SCOPE: ${{ github.event_name == 'workflow_dispatch' && inputs.publish_scope || '' }}
          RELEASE_PLUGINS: ${{ github.event_name == 'workflow_dispatch' && inputs.plugins || '' }}
          BASE_REF: ${{ github.event_name != 'workflow_dispatch' && github.event.before || '' }}
          HEAD_REF: ${{ steps.ref.outputs.sha }}
        run: |
          set -euo pipefail
          if [[ -n "${PUBLISH_SCOPE}" ]]; then
            release_args=(--selection-mode "${PUBLISH_SCOPE}")
            if [[ -n "${RELEASE_PLUGINS}" ]]; then
              release_args+=(--plugins "${RELEASE_PLUGINS}")
            fi
            pnpm release:plugins:clawhub:check -- "${release_args[@]}"
          elif [[ -n "${BASE_REF}" ]]; then
            pnpm release:plugins:clawhub:check -- --base-ref "${BASE_REF}" --head-ref "${HEAD_REF}"
          else
            pnpm release:plugins:clawhub:check
          fi

      - name: Resolve plugin release plan
        id: plan
        env:
          PUBLISH_SCOPE: ${{ github.event_name == 'workflow_dispatch' && inputs.publish_scope || '' }}
          RELEASE_PLUGINS: ${{ github.event_name == 'workflow_dispatch' && inputs.plugins || '' }}
          BASE_REF: ${{ github.event_name != 'workflow_dispatch' && github.event.before || '' }}
          HEAD_REF: ${{ steps.ref.outputs.sha }}
          CLAWHUB_REGISTRY: ${{ env.CLAWHUB_REGISTRY }}
        run: |
          set -euo pipefail
          mkdir -p .local
          if [[ -n "${PUBLISH_SCOPE}" ]]; then
            plan_args=(--selection-mode "${PUBLISH_SCOPE}")
            if [[ -n "${RELEASE_PLUGINS}" ]]; then
              plan_args+=(--plugins "${RELEASE_PLUGINS}")
            fi
            node --import tsx scripts/plugin-clawhub-release-plan.ts "${plan_args[@]}" > .local/plugin-clawhub-release-plan.json
          elif [[ -n "${BASE_REF}" ]]; then
            node --import tsx scripts/plugin-clawhub-release-plan.ts --base-ref "${BASE_REF}" --head-ref "${HEAD_REF}" > .local/plugin-clawhub-release-plan.json
          else
            node --import tsx scripts/plugin-clawhub-release-plan.ts > .local/plugin-clawhub-release-plan.json
          fi

          cat .local/plugin-clawhub-release-plan.json

          candidate_count="$(jq -r '.candidates | length' .local/plugin-clawhub-release-plan.json)"
          skipped_published_count="$(jq -r '.skippedPublished | length' .local/plugin-clawhub-release-plan.json)"
          has_candidates="false"
          if [[ "${candidate_count}" != "0" ]]; then
            has_candidates="true"
          fi
          matrix_json="$(jq -c '.candidates' .local/plugin-clawhub-release-plan.json)"

          {
            echo "candidate_count=${candidate_count}"
            echo "skipped_published_count=${skipped_published_count}"
            echo "has_candidates=${has_candidates}"
            echo "matrix=${matrix_json}"
          } >> "$GITHUB_OUTPUT"

          echo "Plugin release candidates:"
          jq -r '.candidates[]? | "- \(.packageName)@\(.version) [\(.publishTag)] from \(.packageDir)"' .local/plugin-clawhub-release-plan.json

          echo "Already published / skipped:"
          jq -r '.skippedPublished[]? | "- \(.packageName)@\(.version)"' .local/plugin-clawhub-release-plan.json

      - name: Fail manual publish when target versions already exist
        if: github.event_name == 'workflow_dispatch' && inputs.publish_scope == 'selected' && steps.plan.outputs.skipped_published_count != '0'
        run: |
          echo "::error::One or more selected plugin versions already exist on ClawHub. Bump the version before running a real publish."
          exit 1

  preview_plugin_pack:
    needs: preview_plugins_clawhub
    if: needs.preview_plugins_clawhub.outputs.has_candidates == 'true'
    runs-on: ubuntu-latest
    permissions:
      contents: read
    strategy:
      fail-fast: false
      matrix:
        plugin: ${{ fromJson(needs.preview_plugins_clawhub.outputs.matrix) }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          ref: ${{ needs.preview_plugins_clawhub.outputs.ref_sha }}
          fetch-depth: 1

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          node-version: ${{ env.NODE_VERSION }}
          pnpm-version: ${{ env.PNPM_VERSION }}
          install-bun: "true"
          use-sticky-disk: "false"
          install-deps: "false"

      - name: Checkout ClawHub CLI source
        uses: actions/checkout@v6
        with:
          repository: ${{ env.CLAWHUB_REPOSITORY }}
          ref: ${{ env.CLAWHUB_REF }}
          path: clawhub-source
          fetch-depth: 1

      - name: Install ClawHub CLI dependencies
        working-directory: clawhub-source
        run: bun install --frozen-lockfile

      - name: Bootstrap ClawHub CLI
        run: |
          cat > "$RUNNER_TEMP/clawhub" <<'EOF'
          #!/usr/bin/env bash
          set -euo pipefail
          exec bun "$GITHUB_WORKSPACE/clawhub-source/packages/clawhub/src/cli.ts" "$@"
          EOF
          chmod +x "$RUNNER_TEMP/clawhub"
          echo "$RUNNER_TEMP" >> "$GITHUB_PATH"

      - name: Preview publish command
        env:
          CLAWHUB_REGISTRY: ${{ env.CLAWHUB_REGISTRY }}
          SOURCE_REPO: ${{ github.repository }}
          SOURCE_COMMIT: ${{ needs.preview_plugins_clawhub.outputs.ref_sha }}
          SOURCE_REF: ${{ github.ref }}
          PACKAGE_TAG: ${{ matrix.plugin.publishTag }}
          PACKAGE_DIR: ${{ matrix.plugin.packageDir }}
        run: bash scripts/plugin-clawhub-publish.sh --dry-run "${PACKAGE_DIR}"

  publish_plugins_clawhub:
    needs: [preview_plugins_clawhub, preview_plugin_pack]
    if: github.event_name == 'workflow_dispatch' && needs.preview_plugins_clawhub.outputs.has_candidates == 'true'
    runs-on: ubuntu-latest
    environment: clawhub-plugin-release
    permissions:
      contents: read
      id-token: write
    strategy:
      fail-fast: false
      matrix:
        plugin: ${{ fromJson(needs.preview_plugins_clawhub.outputs.matrix) }}
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          ref: ${{ needs.preview_plugins_clawhub.outputs.ref_sha }}
          fetch-depth: 1

      - name: Setup Node environment
        uses: ./.github/actions/setup-node-env
        with:
          node-version: ${{ env.NODE_VERSION }}
          pnpm-version: ${{ env.PNPM_VERSION }}
          install-bun: "true"
          use-sticky-disk: "false"
          install-deps: "false"

      - name: Checkout ClawHub CLI source
        uses: actions/checkout@v6
        with:
          repository: ${{ env.CLAWHUB_REPOSITORY }}
          ref: ${{ env.CLAWHUB_REF }}
          path: clawhub-source
          fetch-depth: 1

      - name: Install ClawHub CLI dependencies
        working-directory: clawhub-source
        run: bun install --frozen-lockfile

      - name: Bootstrap ClawHub CLI
        run: |
          cat > "$RUNNER_TEMP/clawhub" <<'EOF'
          #!/usr/bin/env bash
          set -euo pipefail
          exec bun "$GITHUB_WORKSPACE/clawhub-source/packages/clawhub/src/cli.ts" "$@"
          EOF
          chmod +x "$RUNNER_TEMP/clawhub"
          echo "$RUNNER_TEMP" >> "$GITHUB_PATH"

      - name: Ensure version is not already published
        env:
          PACKAGE_NAME: ${{ matrix.plugin.packageName }}
          PACKAGE_VERSION: ${{ matrix.plugin.version }}
          CLAWHUB_REGISTRY: ${{ env.CLAWHUB_REGISTRY }}
        run: |
          set -euo pipefail
          encoded_name="$(node -e 'console.log(encodeURIComponent(process.env.PACKAGE_NAME ?? ""))')"
          encoded_version="$(node -e 'console.log(encodeURIComponent(process.env.PACKAGE_VERSION ?? ""))')"
          url="${CLAWHUB_REGISTRY%/}/api/v1/packages/${encoded_name}/versions/${encoded_version}"
          status="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' "${url}")"
          if [[ "${status}" =~ ^2 ]]; then
            echo "${PACKAGE_NAME}@${PACKAGE_VERSION} is already published on ClawHub."
            exit 1
          fi
          if [[ "${status}" != "404" ]]; then
            echo "Unexpected ClawHub response (${status}) for ${PACKAGE_NAME}@${PACKAGE_VERSION}."
            exit 1
          fi

      - name: Publish
        env:
          CLAWHUB_REGISTRY: ${{ env.CLAWHUB_REGISTRY }}
          SOURCE_REPO: ${{ github.repository }}
          SOURCE_COMMIT: ${{ needs.preview_plugins_clawhub.outputs.ref_sha }}
          SOURCE_REF: ${{ github.ref }}
          PACKAGE_TAG: ${{ matrix.plugin.publishTag }}
          PACKAGE_DIR: ${{ matrix.plugin.packageDir }}
        run: bash scripts/plugin-clawhub-publish.sh --publish "${PACKAGE_DIR}"
```

### `AGENTS.md`

- Source path: `AGENTS.md`
- Truncated: `no`

```md
# Repository Guidelines

- Repo: https://github.com/openclaw/openclaw
- In chat replies, file references must be repo-root relative only (example: `src/telegram/index.ts:80`); never absolute paths or `~/...`.
- Do not edit files covered by security-focused `CODEOWNERS` rules unless a listed owner explicitly asked for the change or is already reviewing it with you. Treat those paths as restricted surfaces, not drive-by cleanup.

## Project Structure & Module Organization

- Source code: `src/` (CLI wiring in `src/cli`, commands in `src/commands`, web provider in `src/provider-web.ts`, infra in `src/infra`, media pipeline in `src/media`).
- Tests: colocated `*.test.ts`.
- Docs: `docs/` (images, queue, Pi config). Built output lives in `dist/`.
- Nomenclature: use "plugin" / "plugins" in docs, UI, changelogs, and contributor guidance. The bundled workspace plugin tree remains the internal package layout to avoid repo-wide churn from a rename.
- Bundled plugin naming: for repo-owned workspace plugins, keep the canonical plugin id aligned across `openclaw.plugin.json:id`, the default workspace folder name, and package names anchored to the same id (`@openclaw/<id>` or approved suffix forms like `-provider`, `-plugin`, `-speech`, `-sandbox`, `-media-understanding`). Keep `openclaw.install.npmSpec` equal to the package name and `openclaw.channel.id` equal to the plugin id when present. Exceptions must be explicit and covered by the repo invariant test.
- Plugins: live in the bundled workspace plugin tree (workspace packages). Keep plugin-only deps in the extension `package.json`; do not add them to the root `package.json` unless core uses them.
- Plugins: install runs `npm install --omit=dev` in plugin dir; runtime deps must live in `dependencies`. Avoid `workspace:*` in `dependencies` (npm install breaks); put `openclaw` in `devDependencies` or `peerDependencies` instead (runtime resolves `openclaw/plugin-sdk` via jiti alias).
- Import boundaries: extension production code should treat `openclaw/plugin-sdk/*` plus local `api.ts` / `runtime-api.ts` barrels as the public surface. Do not import core `src/**`, `src/plugin-sdk-internal/**`, or another extension's `src/**` directly.
- Installers served from `https://openclaw.ai/*`: live in the sibling repo `../openclaw.ai` (`public/install.sh`, `public/install-cli.sh`, `public/install.ps1`).
- Messaging channels: always consider **all** built-in + extension channels when refactoring shared logic (routing, allowlists, pairing, command gating, onboarding, docs).
  - Core channel docs: `docs/channels/`
  - Core channel code: `src/telegram`, `src/discord`, `src/slack`, `src/signal`, `src/imessage`, `src/web` (WhatsApp web), `src/channels`, `src/routing`
  - Bundled plugin channels: the workspace plugin tree (for example Matrix, Zalo, ZaloUser, Voice Call)
- When adding channels/plugins/apps/docs, update `.github/labeler.yml` and create matching GitHub labels (use existing channel/plugin label colors).

## Architecture Boundaries

- Start here for the repo map:
  - bundled workspace plugin tree = bundled plugins and the closest example surface for third-party plugins
  - `src/plugin-sdk/*` = the public plugin contract that extensions are allowed to import
  - `src/channels/*` = core channel implementation details behind the plugin/channel boundary
  - `src/plugins/*` = plugin discovery, manifest validation, loader, registry, and contract enforcement
  - `src/gateway/protocol/*` = typed Gateway control-plane and node wire protocol
- Progressive disclosure lives in local boundary guides:
  - repo root `AGENTS.md`
  - bundled-plugin-tree `extensions/AGENTS.md`
  - `src/plugin-sdk/AGENTS.md`
  - `src/channels/AGENTS.md`
  - `src/plugins/AGENTS.md`
  - `src/gateway/protocol/AGENTS.md`
- Workflow hygiene:
  - Do not grep or existence-check every `docs/*.md`, `AGENTS.md`, or guide path mentioned in this file before starting work.
  - Read only the guides and docs that are directly relevant to the files or boundary you are touching.
  - Only do full broken-link or missing-guide sweeps when the task is explicitly about docs or repo-instruction maintenance.
- Plugin and extension boundary:
  - Public docs: `docs/plugins/building-plugins.md`, `docs/plugins/architecture.md`, `docs/plugins/sdk-overview.md`, `docs/plugins/sdk-entrypoints.md`, `docs/plugins/sdk-runtime.md`, `docs/plugins/manifest.md`, `docs/plugins/sdk-channel-plugins.md`, `docs/plugins/sdk-provider-plugins.md`
  - Definition files: `src/plugin-sdk/plugin-entry.ts`, `src/plugin-sdk/core.ts`, `src/plugin-sdk/provider-entry.ts`, `src/plugin-sdk/channel-contract.ts`, `scripts/lib/plugin-sdk-entrypoints.json`, `package.json`
  - Invariant: core must stay extension-agnostic. Adding a bundled or third-party extension should not require unrelated core edits just to teach core that the extension exists.
  - Rule: extensions must cross into core only through `openclaw/plugin-sdk/*`, manifest metadata, and documented runtime helpers. Do not import `src/**` from extension production code.
  - Rule: core code and tests must not deep-import bundled plugin internals such as a plugin's `src/**` files or `onboard.js`. If core needs a bundled plugin helper, expose it through that plugin's `api.ts` and, when it is a real cross-package contract, through `src/plugin-sdk/<id>.ts`.
  - Rule: do not add hardcoded bundled extension/provider/channel/capability id lists, maps, or named special cases in core when a manifest, capability, registry, or plugin-owned contract can express the same behavior.
  - Rule: extension-owned compatibility behavior belongs to the owning extension. Core may orchestrate generic doctor/config flows, but extension-specific legacy repairs, detection rules, onboarding, auth detection, and provider defaults should live in plugin-owned contracts.
  - Rule: for legacy config specifically, prefer doctor-owned repair paths over startup/load-time core migrations. Do not add new plugin-specific legacy migration logic to shared core/runtime surfaces when `openclaw doctor --fix` can own it.
  - Rule: when a test is asserting extension-specific behavior, keep that coverage in the owning extension when feasible. Core tests should assert generic contracts and registry/capability behavior, not extension internals.
  - Refactor trigger: if you encounter core code or tests that name a specific extension/provider/channel for extension-owned behavior, refactor toward a generic registry/capability/plugin-owned seam instead of adding another special case.
  - Compatibility: new plugin seams are allowed, but they must be added as documented, backwards-compatible, versioned contracts. We have third-party plugins in the wild and do not break them casually.
- Channel boundary:
  - Public docs: `docs/plugins/sdk-channel-plugins.md`, `docs/plugins/architecture.md`
  - Definition files: `src/channels/plugins/types.plugin.ts`, `src/channels/plugins/types.core.ts`, `src/channels/plugins/types.adapters.ts`, `src/plugin-sdk/core.ts`, `src/plugin-sdk/channel-contract.ts`
  - Rule: `src/channels/**` is core implementation. If plugin authors need a new seam, add it to the Plugin SDK instead of telling them to import channel internals.
- Provider/model boundary:
  - Public docs: `docs/plugins/sdk-provider-plugins.md`, `docs/concepts/model-providers.md`, `docs/plugins/architecture.md`
  - Definition files: `src/plugins/types.ts`, `src/plugin-sdk/provider-entry.ts`, `src/plugin-sdk/provider-auth.ts`, `src/plugin-sdk/provider-catalog-shared.ts`, `src/plugin-sdk/provider-model-shared.ts`
  - Rule: core owns the generic inference loop; provider plugins own provider-specific behavior through registration and typed hooks. Do not solve provider needs by reaching into unrelated core internals.
  - Rule: avoid ad hoc reads of `plugins.entries.<id>.config` from unrelated core code. If core needs plugin-owned auth/config behavior, add or use a generic seam (`resolveSyntheticAuth`, public SDK/helper facades, manifest metadata, plugin auto-enable hooks) and honor plugin disablement plus SecretRef semantics.
  - Rule: vendor-owned tools and settings belong in the owning plugin. Do not add provider-specific tool config, secret collection, or runtime enablement to core `tools.*` surfaces unless the tool is intentionally core-owned.
- Gateway protocol boundary:
  - Public docs: `docs/gateway/protocol.md`, `docs/gateway/bridge-protocol.md`, `docs/concepts/architecture.md`
  - Definition files: `src/gateway/protocol/schema.ts`, `src/gateway/protocol/schema/*.ts`, `src/gateway/protocol/index.ts`
  - Rule: protocol changes are contract changes. Prefer additive evolution; incompatible changes require explicit versioning, docs, and client/codegen follow-through.
- Config contract boundary:
  - Canonical public config lives in exported config types, zod/schema surfaces, schema help/labels, generated config metadata, config baselines, and any user-facing gateway/config payloads. Keep those surfaces aligned.
  - When a legacy config key is retired from the public contract, remove it from every public config surface above. Keep backward compatibility only through raw-config migration/doctor seams unless explicit product policy says otherwise.
  - Do not reintroduce removed legacy aliases into public types/schema/help/baselines “for convenience”. If old configs still need to load, handle that in `legacy.migrations.*`, config ingest, or `openclaw doctor --fix`.
  - `hooks.internal.entries` is the canonical public hook config model. `hooks.internal.handlers` is compatibility-only input and must not be re-exposed in public schema/help/baseline surfaces.
- Bundled plugin contract boundary:
  - Public docs: `docs/plugins/architecture.md`, `docs/plugins/manifest.md`, `docs/plugins/sdk-overview.md`
  - Definition files: `src/plugins/contracts/registry.ts`, `src/plugins/types.ts`, `src/plugins/public-artifacts.ts`
  - Rule: keep manifest metadata, runtime registration, public SDK exports, and contract tests aligned. Do not create a hidden path around the declared plugin interfaces.
- Extension test boundary:
  - Keep extension-owned onboarding/config/provider coverage under the owning bundled plugin package when feasible.
  - If core tests need bundled plugin behavior, consume it through public `src/plugin-sdk/<id>.ts` facades or the plugin's `api.ts`, not private extension modules.
  - Shared helpers under `test/helpers/**` are part of that same boundary. Do not hardcode repo-relative `extensions/**` imports there, and do not keep plugin-local deep mocks in shared helpers just because multiple tests use them.
  - When core tests or shared helpers need bundled plugin public surfaces, use `src/test-utils/bundled-plugin-public-surface.ts` for `api.ts`, `runtime-api.ts`, `contract-api.ts`, `test-api.ts`, plugin entrypoint `index.js`, and resolved module ids for dynamic import or mocking.
  - If a core test is asserting extension-specific behavior instead of a generic contract, move it to the owning extension package.
- Scoped guides still matter:
  - `extensions/AGENTS.md` expands extension/plugin boundary rules.
  - `src/channels/AGENTS.md` expands core channel boundary and hot-path rules.
  - `src/plugin-sdk/AGENTS.md` expands public SDK contract rules.
  - `src/plugins/AGENTS.md` expands plugin loading, registry, and manifest rules.
  - `src/gateway/protocol/AGENTS.md` expands typed Gateway protocol rules.
  - `test/helpers/AGENTS.md` and `test/helpers/channels/AGENTS.md` expand shared test helper boundary rules.
- Plugin architecture direction:
  - Keep a manifest-first control plane: discovery, validation, enablement, setup hints, and activation planning should stay metadata-driven by default.
  - Keep runtime execution separate: actual provider/channel/tool execution should resolve through narrow targeted loaders, not broad registry materialization.
  - Host loads plugins; plugins do not load host internals. Prefer a small versioned host/kernel seam plus documented SDK entrypoints over ambient reachability.
  - Treat broad runtime registries and mutable global plugin state as transitional compatibility surfaces, not the target architecture.
  - If a setup or config flow truly needs plugin runtime, make that explicit instead of silently importing runtime code on the cold path.

## Scoped Workflow Guides

- `docs/AGENTS.md` owns Mintlify docs, docs links, and docs i18n rules.
- `ui/AGENTS.md` owns Control UI i18n and generated locale rules.
- `scripts/AGENTS.md` owns script-runner, local-check lock, and test/lint wrapper rules.

## exe.dev VM ops (general)

- Access: stable path is `ssh exe.dev` then `ssh vm-name` (assume SSH key already set).
- SSH flaky: use exe.dev web terminal or Shelley (web agent); keep a tmux session for long ops.
- Update: `sudo npm i -g openclaw@latest` (global install needs root on `/usr/lib/node_modules`).
- Config: use `openclaw config set ...`; ensure `gateway.mode=local` is set.
- Discord: store raw token only (no `DISCORD_BOT_TOKEN=` prefix).
- Restart: stop old gateway and run:
  `pkill -9 -f openclaw-gateway || true; nohup openclaw gateway run --bind loopback --port 18789 --force > /tmp/openclaw-gateway.log 2>&1 &`
- Verify: `openclaw channels status --probe`, `ss -ltnp | rg 18789`, `tail -n 120 /tmp/openclaw-gateway.log`.

## Build, Test, and Development Commands

- Runtime baseline: Node **22+** (keep Node + Bun paths working).
- Install deps: `pnpm install`
- If deps are missing (for example `node_modules` missing, `vitest not found`, or `command not found`), run the repo’s package-manager install command (prefer lockfile/README-defined PM), then rerun the exact requested command once. Apply this to test/build/lint/typecheck/dev commands; if retry still fails, report the command and first actionable error.
- Pre-commit hooks: `prek install`. The hook runs the repo verification flow, including `pnpm check`.
- `FAST_COMMIT=1` skips the repo-wide `pnpm format` and `pnpm check` inside the pre-commit hook only. Use it when you intentionally want a faster commit path and are running equivalent targeted verification manually. It does not change CI and does not change what `pnpm check` itself does.
- Also supported: `bun install` (keep `pnpm-lock.yaml` + Bun patching in sync when touching deps/patches).
- Prefer Bun for TypeScript execution (scripts, dev, tests): `bun <file.ts>` / `bunx <tool>`.
- Run CLI in dev: `pnpm openclaw ...` (bun) or `pnpm dev`.
- Node remains supported for running built output (`dist/*`) and production installs.
- Mac packaging (dev): `scripts/package-mac-app.sh` defaults to current arch.
- Type-check/build: `pnpm build`
- TypeScript checks: `pnpm tsgo`
- Lint/format: `pnpm check`
- Local agent/dev shells default to host-aware `OPENCLAW_LOCAL_CHECK=1` behavior for `pnpm tsgo` and `pnpm lint`; set `OPENCLAW_LOCAL_CHECK_MODE=throttled` to force the lower-memory profile, `OPENCLAW_LOCAL_CHECK_MODE=full` to keep lock-only behavior, or `OPENCLAW_LOCAL_CHECK=0` in CI/shared runs.
- Format check: `pnpm format` (oxfmt --check)
- Format fix: `pnpm format:fix` (oxfmt --write)
- Terminology:
  - "gate" means a verification command or command set that must be green for the decision you are making.
  - A local dev gate is the fast default loop, usually `pnpm check` plus any scoped test you actually need.
  - A landing gate is the broader bar before pushing `main`, usually `pnpm check`, `pnpm test`, and `pnpm build` when the touched surface can affect build output, packaging, lazy-loading/module boundaries, or published surfaces.
  - A CI gate is whatever the relevant workflow enforces for that lane (for example `check`, `check-additional`, `build-smoke`, or release validation).
- Local dev gate: prefer `pnpm check` for the normal edit loop. It keeps the repo-architecture policy guards out of the default local loop.
- CI architecture gate: `check-additional` enforces architecture and boundary policy guards that are intentionally kept out of the default local loop.
- Formatting gate: the pre-commit hook runs `pnpm format` before `pnpm check`. If you want a formatting-only preflight locally, run `pnpm format` explicitly.
- If you need a fast commit loop, `FAST_COMMIT=1 git commit ...` skips the hook’s repo-wide `pnpm format` and `pnpm check`; use that only when you are deliberately covering the touched surface some other way.
- Tests: `pnpm test` (vitest); coverage: `pnpm test:coverage`
- Generated baseline drift detection uses SHA-256 hash files under `docs/.generated/` (`.sha256` files tracked in git; full JSON baselines are gitignored, generated locally for inspection).
- Config schema drift uses `pnpm config:docs:gen` / `pnpm config:docs:check`.
- Plugin SDK API drift uses `pnpm plugin-sdk:api:gen` / `pnpm plugin-sdk:api:check`.
- If you change config schema/help or the public Plugin SDK surface, run the matching gen command and commit the updated `.sha256` hash file. Keep the two drift-check flows adjacent in scripts/workflows/docs guidance rather than inventing a third pattern.
- When `pnpm tsgo` fails, triage by coherent surface instead of by raw error count: rerun the gate, group failures by package/module/type contract, open the source-of-truth type or export file first, fix the root mismatch, then rerun `pnpm tsgo` before widening into downstream consumers. Check `origin/main` before doing broad cleanup because some apparent type debt is already fixed upstream.
- For narrowly scoped changes, prefer narrowly scoped tests that directly validate the touched behavior. If no meaningful scoped test exists, say so explicitly and use the next most direct validation available.
- Verification modes for work on `main`:
  - Default mode: `main` is relatively stable. Count pre-commit hook coverage when it already verified the current tree, avoid rerunning the exact same checks just for ceremony, and prefer keeping CI/main green before landing.
  - Fast-commit mode: `main` is moving fast and you intentionally optimize for shorter commit loops. Prefer explicit local verification close to the final landing point, and it is acceptable to use `--no-verify` for intermediate or catch-up commits after equivalent checks have already run locally.
- Preferred landing bar for pushes to `main`: in Default mode, favor `pnpm check` and `pnpm test` near the final rebase/push point when feasible. In fast-commit mode, verify the touched surface locally near landing without insisting every intermediate commit replay the full hook.
- Scoped tests prove the change itself. `pnpm test` remains the default `main` landing bar; scoped tests do not replace full-suite gates by default.
- Hard gate: if the change can affect build output, packaging, lazy-loading/module boundaries, or published surfaces, `pnpm build` MUST be run and MUST pass before pushing `main`.
- Default rule: do not land changes with failing format, lint, type, build, or required test checks when those failures are caused by the change or plausibly related to the touched surface. Fast-commit mode changes how verification is sequenced; it does not lower the requirement to validate and clean up the touched surface before final landing.
- For narrowly scoped changes, if unrelated failures already exist on latest `origin/main`, state that clearly, report the scoped tests you ran, and ask before broadening scope into unrelated fixes or landing despite those failures.
- Do not use scoped tests as permission to ignore plausibly related failures.

## Prompt Cache Stability

- Treat prompt-cache stability as correctness/perf-critical, not cosmetic.
- Any code that assembles model or tool payloads from maps, sets, registries, plugin lists, MCP catalogs, filesystem reads, or network results must make ordering deterministic before building the request.
- Do not rewrite older transcript/history bytes on every turn unless you intentionally want to invalidate the cached prefix. Legacy cleanup, pruning, normalization, and migration logic should preserve recent prompt bytes when possible.
- If truncation or compaction is required, prefer mutating newest or tail content first so the cached prefix stays byte-identical for as long as possible.
- For cache-sensitive changes, require a regression test that proves turn-to-turn prefix stability or deterministic request assembly; helper-local tests alone are not enough.

## Coding Style & Naming Conventions

- Language: TypeScript (ESM). Prefer strict typing; avoid `any`.
- Formatting/linting via Oxlint and Oxfmt.
- Never add `@ts-nocheck` and do not add inline lint suppressions by default. Fix root causes first; only keep a suppression when the code is intentionally correct, the rule cannot express that safely, and the comment explains why.
- Do not disable `no-explicit-any`; prefer real types, `unknown`, or a narrow adapter/helper instead. Update Oxlint/Oxfmt config only when required.
- Prefer `zod` or existing schema helpers at external boundaries such as config, webhook payloads, CLI/JSON output, persisted JSON, and third-party API responses.
- Prefer discriminated unions when parameter shape changes runtime behavior.
- Prefer `Result<T, E>`-style outcomes and closed error-code unions for recoverable runtime decisions.
- Keep human-readable strings for logs, CLI output, and UI; do not use freeform strings as the source of truth for internal branching.
- Avoid `?? 0`, empty-string, empty-object, or magic-string sentinels when they can change runtime meaning silently.
- If introducing a new optional field or nullable semantic in core logic, prefer an explicit union or dedicated type when the value changes behavior.
- New runtime control-flow code should not branch on `error: string` or `reason: string` when a closed code union would be reasonable.
- Dynamic import guardrail: do not mix `await import("x")` and static `import ... from "x"` for the same module in production code paths. If you need lazy loading, create a dedicated `*.runtime.ts` boundary (that re-exports from `x`) and dynamically import that boundary from lazy callers only.
- Dynamic import verification: after refactors that touch lazy-loading/module boundaries, run `pnpm build` and check for `[INEFFECTIVE_DYNAMIC_IMPORT]` warnings before submitting.
- Circular dependencies: keep both `pnpm check:import-cycles` and `pnpm check:static-import-sccs` green; do not reintroduce runtime import cycles or static SCCs.
- Extension SDK self-import guardrail: inside an extension package, do not import that same extension via `openclaw/plugin-sdk/<extension>` from production files. Route internal imports through a local barrel such as `./api.ts` or `./runtime-api.ts`, and keep the `plugin-sdk/<extension>` path as the external contract only.
- Extension package boundary guardrail: inside a bundled plugin package, do not use relative imports/exports that resolve outside that same package root. If shared code belongs in the plugin SDK, import `openclaw/plugin-sdk/<subpath>` instead of reaching into `src/plugin-sdk/**` or other repo paths via `../`.
- Extension API surface rule: `openclaw/plugin-sdk/<subpath>` is the only public cross-package contract for extension-facing SDK code. If an extension needs a new seam, add a public subpath first; do not reach into `src/plugin-sdk/**` by relative path.
- Never share class behavior via prototype mutation (`applyPrototypeMixins`, `Object.defineProperty` on `.prototype`, or exporting `Class.prototype` for merges). Use explicit inheritance/composition (`A extends B extends C`) or helper composition so TypeScript can typecheck.
- If this pattern is needed, stop and get explicit approval before shipping; default behavior is to split/refactor into an explicit class hierarchy and keep members strongly typed.
- In tests, prefer per-instance stubs over prototype mutation (`SomeClass.prototype.method = ...`) unless a test explicitly documents why prototype-level patching is required.
- Add brief code comments for tricky or non-obvious logic.
- Keep files concise; extract helpers instead of “V2” copies. Use existing patterns for CLI options and dependency injection via `createDefaultDeps`.
- Aim to keep files under ~700 LOC; guideline only (not a hard guardrail). Split/refactor when it improves clarity or testability.
- Naming: use **OpenClaw** for product/app/docs headings; use `openclaw` for CLI command, package/binary, paths, and config keys.
- Written English: use American spelling and grammar in code, comments, docs, and UI strings (e.g. "color" not "colour", "behavior" not "behaviour", "analyze" not "analyse").

## Release / Advisory Workflows

- Use `$openclaw-release-maintainer` at `.agents/skills/openclaw-release-maintainer/SKILL.md` for release naming, version coordination, release auth, and changelog-backed release-note workflows.
- Use `$openclaw-ghsa-maintainer` at `.agents/skills/openclaw-ghsa-maintainer/SKILL.md` for GHSA advisory inspection, patch/publish flow, private-fork checks, and GHSA API validation.
- Release and publish remain explicit-approval actions even when using the skill.

## Testing Guidelines

- Framework: Vitest with V8 coverage thresholds (70% lines/branches/functions/statements).
- Naming: match source names with `*.test.ts`; e2e in `*.e2e.test.ts`.
- When tests need example Anthropic/OpenAI model constants, prefer `sonnet-4.6` and `gpt-5.4`; update older Anthropic/GPT examples when you touch those tests.
- Run `pnpm test` (or `pnpm test:coverage`) before pushing when you touch logic.
- Write tests to clean up timers, env, globals, mocks, sockets, temp dirs, and module state so `--isolate=false` stays green.
- Test performance guardrail: do not put `vi.resetModules()` plus `await import(...)` in `beforeEach`/per-test loops for heavy modules unless module state truly requires it. Prefer static imports or one-time `beforeAll` imports, then reset mocks/runtime state directly.
- Test performance guardrail: if a test file uses stable `vi.mock(...)` hoists or other static module mocks, do not pair them with `vi.resetModules()` and a fresh `await import(...)` in every `beforeEach`. Import the heavy module once in `beforeAll`, then reset/prime mocks in `beforeEach` so Browser/Matrix-style hotspot tests do not pay the module graph cost per case.
- Test performance guardrail: inside an extension package, prefer a thin local seam (`./api.ts`, `./runtime-api.ts`, or a narrower local `*.runtime-api.ts`) over direct `openclaw/plugin-sdk/*` imports for internal production code. Keep local seams curated and lightweight; only reach for direct `plugin-sdk/*` imports when you are crossing a real package boundary or when no suitable local seam exists yet.
- Test performance guardrail: keep expensive runtime fallback work such as snapshotting, migration, installs, or bootstrap behind dedicated `*.runtime.ts` boundaries so tests can mock the seam instead of accidentally invoking real work.
- Test performance guardrail: for import-only/runtime-wrapper tests, keep the wrapper lazy. Do not eagerly load heavy verification/bootstrap/runtime modules at module top level if the exported function can import them on demand.
- Test performance guardrail: prefer explicit mock factories over `importOriginal()` for broad modules. Reserve `importOriginal()` for narrow modules where partial-real behavior is genuinely needed.
- Test performance guardrail: do not partial-mock broad `openclaw/plugin-sdk/*` barrels in hot tests. Add a plugin-local `*.runtime.ts` seam and mock that seam instead.
- Test performance guardrail: when production code already accepts `deps`, callbacks, or runtime injection, use that seam in tests before adding module-level mocks.
- Test performance guardrail: prefer narrow public SDK subpaths such as `models-provider-runtime`, `skill-commands-runtime`, and `reply-dispatch-runtime` over older broad helper barrels when both expose the needed helper.
- Test performance guardrail: treat import-dominated test time as a boundary bug. Refactor the import surface before adding more cases to the slow file.
- Agents MUST NOT modify baseline, inventory, ignore, snapshot, or expected-failure files to silence failing checks without explicit approval in this chat.
- For targeted/local debugging, use the native root-project entrypoint: `pnpm test <path-or-filter> [vitest args...]` (for example `pnpm test src/commands/onboard-search.test.ts -t "shows registered plugin providers"`); do not default to raw `pnpm vitest run ...` because it bypasses the repo's default config/profile/pool routing.
- Do not set test workers above 16; tried already.
- Vitest now defaults to native root-project `threads`, with hard `forks` exceptions for `gateway`, `agents`, and `commands`. Keep new pool changes explicit and justified; use `OPENCLAW_VITEST_POOL=forks` for full local fork debugging.
- If local Vitest runs cause memory pressure, the default worker budget now derives from host capabilities (CPU, memory band, current load). For a conservative explicit override during land/gate runs, use `OPENCLAW_VITEST_MAX_WORKERS=1 pnpm test`.
- Live tests (real keys): `OPENCLAW_LIVE_TEST=1 pnpm test:live` (OpenClaw-only) or `LIVE=1 pnpm test:live` (includes provider live tests). Docker: `pnpm test:docker:live-models`, `pnpm test:docker:live-gateway`. Onboarding Docker E2E: `pnpm test:docker:onboard`.
- `pnpm test:live` defaults quiet now. Keep `[live]` progress; suppress profile/gateway chatter. Full logs: `OPENCLAW_LIVE_TEST_QUIET=0 pnpm test:live`.
- Full kit + what’s covered: `docs/help/testing.md`.
- Changelog: user-facing changes only; no internal/meta notes (version alignment, appcast reminders, release process).
- Changelog placement: in the active version block, append new entries to the end of the target section (`### Changes` or `### Fixes`); do not insert new entries at the top of a section.
- Changelog attribution: use at most one contributor mention per line; prefer `Thanks @author` and do not also add `by @author` on the same entry.
- Pure test additions/fixes generally do **not** need a changelog entry unless they alter user-facing behavior or the user asks for one.
- Mobile: before using a simulator, check for connected real devices (iOS + Android) and prefer them when available.

## Commit & Pull Request Guidelines

- Use `$openclaw-pr-maintainer` at `.agents/skills/openclaw-pr-maintainer/SKILL.md` for maintainer PR triage, review, close, search, and landing workflows.
- This includes auto-close labels, bug-fix evidence gates, GitHub comment/search footguns, and maintainer PR decision flow.
- For the repo's end-to-end maintainer PR workflow, use `$openclaw-pr-maintainer` at `.agents/skills/openclaw-pr-maintainer/SKILL.md`.

- `/landpr` lives in the global Codex prompts (`~/.codex/prompts/landpr.md`); when landing or merging any PR, always follow that `/landpr` process.
- Create commits with `scripts/committer "<msg>" <file...>`; avoid manual `git add`/`git commit` so staging stays scoped.
- Follow concise, action-oriented commit messages (e.g., `CLI: add verbose flag to send`).
- Group related changes; avoid bundling unrelated refactors.
- PR submission template (canonical): `.github/pull_request_template.md`
- Issue submission templates (canonical): `.github/ISSUE_TEMPLATE/`

## Git Notes

- If `git branch -d/-D <branch>` is policy-blocked, delete the local ref directly: `git update-ref -d refs/heads/<branch>`.
- Agents MUST NOT create or push merge commits on `main`. If `main` has advanced, rebase local commits onto the latest `origin/main` before pushing.
- Bulk PR close/reopen safety: if a close action would affect more than 5 PRs, first ask for explicit user confirmation with the exact PR count and target scope/query.

## Security & Configuration Tips

- Web provider stores creds at `~/.openclaw/credentials/`; rerun `openclaw login` if logged out.
- Pi sessions live under `~/.openclaw/sessions/` by default; the base directory is not configurable.
- Environment variables: see `~/.profile`.
- Never commit or publish real phone numbers, videos, or live configuration values. Use obviously fake placeholders in docs, tests, and examples.
- Release flow: use the private [maintainer release docs](https://github.com/openclaw/maintainers/blob/main/release/README.md) for the actual runbook, `docs/reference/RELEASING.md` for the public release policy, and `$openclaw-release-maintainer` for the maintainership workflow.

## Local Runtime / Platform Notes

- Vocabulary: "makeup" = "mac app".
- Rebrand/migration issues or legacy config/service warnings: run `openclaw doctor` (see `docs/gateway/doctor.md`).
- Use `$openclaw-parallels-smoke` at `.agents/skills/openclaw-parallels-smoke/SKILL.md` for Parallels smoke, rerun, upgrade, debug, and result-interpretation workflows across macOS, Windows, and Linux guests.
- For the macOS Discord roundtrip deep dive, use the narrower `.agents/skills/parallels-discord-roundtrip/SKILL.md` companion skill.
- Never edit `node_modules` (global/Homebrew/npm/git installs too). Updates overwrite. Skill notes go in `tools.md` or `AGENTS.md`.
- If you need local-only `.agents` ignores, use `.git/info/exclude` instead of repo `.gitignore`.
- When adding a new `AGENTS.md` anywhere in the repo, also add a `CLAUDE.md` symlink pointing to it (example: `ln -s AGENTS.md CLAUDE.md`).
- Signal: "update fly" => `fly ssh console -a flawd-bot -C "bash -lc 'cd /data/clawd/openclaw && git pull --rebase origin main'"` then `fly machines restart e825232f34d058 -a flawd-bot`.
- CLI progress: use `src/cli/progress.ts` (`osc-progress` + `@clack/prompts` spinner); don’t hand-roll spinners/bars.
- Status output: keep tables + ANSI-safe wrapping (`src/terminal/table.ts`); `status --all` = read-only/pasteable, `status --deep` = probes.
- Gateway currently runs only as the menubar app; there is no separate LaunchAgent/helper label installed. Restart via the OpenClaw Mac app or `scripts/restart-mac.sh`; to verify/kill use `launchctl print gui/$UID | grep openclaw` rather than assuming a fixed label. **When debugging on macOS, start/stop the gateway via the app, not ad-hoc tmux sessions; kill any temporary tunnels before handoff.**
- macOS logs: use `./scripts/clawlog.sh` to query unified logs for the OpenClaw subsystem; it supports follow/tail/category filters and expects passwordless sudo for `/usr/bin/log`.
- If shared guardrails are available locally, review them; otherwise follow this repo's guidance.
- SwiftUI state management (iOS/macOS): prefer the `Observation` framework (`@Observable`, `@Bindable`) over `ObservableObject`/`@StateObject`; don’t introduce new `ObservableObject` unless required for compatibility, and migrate existing usages when touching related code.
- Connection providers: when adding a new connection, update every UI surface and docs (macOS app, web UI, mobile if applicable, onboarding/overview docs) and add matching status + configuration forms so provider lists and settings stay in sync.
- Version locations: `package.json` (CLI), `apps/android/app/build.gradle.kts` (versionName/versionCode), `apps/ios/Sources/Info.plist` + `apps/ios/Tests/Info.plist` (CFBundleShortVersionString/CFBundleVersion), `apps/macos/Sources/OpenClaw/Resources/Info.plist` (CFBundleShortVersionString/CFBundleVersion), `docs/install/updating.md` (pinned npm version), and Peekaboo Xcode projects/Info.plists (MARKETING_VERSION/CURRENT_PROJECT_VERSION).
- "Bump version everywhere" means all version locations above **except** `appcast.xml` (only touch appcast when cutting a new macOS Sparkle release).
- **Restart apps:** “restart iOS/Android apps” means rebuild (recompile/install) and relaunch, not just kill/launch.
- **Device checks:** before testing, verify connected real devices (iOS/Android) before reaching for simulators/emulators.
- Mobile pairing: `ws://` (cleartext) is allowed for private LAN addresses (RFC 1918, link-local, mDNS `.local`) and loopback. Private LAN hosts typically lack PKI-backed identity, so requiring TLS there adds complexity without meaningful security gain. `wss://` is required for Tailscale and public endpoints.
- Security report scope: reports that treat cleartext `ws://` mobile pairing over private LAN as a vulnerability are out of scope unless they demonstrate a trust-boundary bypass beyond passive network observation on the same LAN.
- iOS Team ID lookup: `security find-identity -p codesigning -v` → use Apple Development (…) TEAMID. Fallback: `defaults read com.apple.dt.Xcode IDEProvisioningTeamIdentifiers`.
- A2UI bundle hash: `src/canvas-host/a2ui/.bundle.hash` is auto-generated; ignore unexpected changes, and only regenerate via `pnpm canvas:a2ui:bundle` (or `scripts/bundle-a2ui.sh`) when needed. Commit the hash as a separate commit.
- Release signing/notary credentials are managed outside the repo; maintainers keep that setup in the private [maintainer release docs](https://github.com/openclaw/maintainers/tree/main/release).
- Lobster palette: use the shared CLI palette in `src/terminal/palette.ts` (no hardcoded colors); apply palette to onboarding/config prompts and other TTY UI output as needed.
- When asked to open a “session” file, open the Pi session logs under `~/.openclaw/agents/<agentId>/sessions/*.jsonl` (use the `agent=<id>` value in the Runtime line of the system prompt; newest unless a specific ID is given), not the default `sessions.json`. If logs are needed from another machine, SSH via Tailscale and read the same path there.
- Do not rebuild the macOS app over SSH; rebuilds must be run directly on the Mac.
- Voice wake forwarding tips:
  - Command template should stay `openclaw-mac agent --message "${text}" --thinking low`; `VoiceWakeForwarder` already shell-escapes `${text}`. Don’t add extra quotes.
  - launchd PATH is minimal; ensure the app’s launch agent PATH includes standard system paths plus your pnpm bin (typically `$HOME/Library/pnpm`) so `pnpm`/`openclaw` binaries resolve when invoked via `openclaw-mac`.

## Collaboration / Safety Notes

- When working on a GitHub Issue or PR, print the full URL at the end of the task.
- When answering questions, respond with high-confidence answers only: verify in code; do not guess.
- Carbon version edits are owner-only: do not change `@buape/carbon` version pins unless you are Shadow (@thewilloftheshadow) as verified by gh.
- Any dependency with `pnpm.patchedDependencies` must use an exact version (no `^`/`~`).
- Patching dependencies (pnpm patches, overrides, or vendored changes) requires explicit approval; do not do this by default.
- **Multi-agent safety:** do **not** create/apply/drop `git stash` entries unless explicitly requested (this includes `git pull --rebase --autostash`). Assume other agents may be working; keep unrelated WIP untouched and avoid cross-cutting state changes.
- **Multi-agent safety:** when the user says "push", you may `git pull --rebase` to integrate latest changes (never discard other agents' work). When the user says "commit", scope to your changes only. When the user says "commit all", commit everything in grouped chunks.
- **Multi-agent safety:** prefer grouped `commit` / `pull --rebase` / `push` cycles for related work instead of many tiny syncs.
- **Multi-agent safety:** do **not** create/remove/modify `git worktree` checkouts (or edit `.worktrees/*`) unless explicitly requested.
- **Multi-agent safety:** do **not** switch branches / check out a different branch unless explicitly requested.
- **Multi-agent safety:** running multiple agents is OK as long as each agent has its own session.
- **Multi-agent safety:** when you see unrecognized files, keep going; focus on your changes and commit only those.
- Lint/format churn:
  - If staged+unstaged diffs are formatting-only, auto-resolve without asking.
  - If commit/push already requested, auto-stage and include formatting-only follow-ups in the same commit (or a tiny follow-up commit if needed), no extra confirmation.
  - Only ask when changes are semantic (logic/data/behavior).
- **Multi-agent safety:** focus reports on your edits; avoid guard-rail disclaimers unless truly blocked; when multiple agents touch the same file, continue if safe; end with a brief “other files present” note only if relevant.
- Bug investigations: read source code of relevant npm dependencies and all related local code before concluding; aim for high-confidence root cause.
- Code style: add brief comments for tricky logic; keep files under ~700 LOC when feasible (split/refactor as needed).
- Tool schema guardrails (google-antigravity): avoid `Type.Union` in tool input schemas; no `anyOf`/`oneOf`/`allOf`. Use `stringEnum`/`optionalStringEnum` (Type.Unsafe enum) for string lists, and `Type.Optional(...)` instead of `... | null`. Keep top-level tool schema as `type: "object"` with `properties`.
- Tool schema guardrails: avoid raw `format` property names in tool schemas; some validators treat `format` as a reserved keyword and reject the schema.
- Never send streaming/partial replies to external messaging surfaces (WhatsApp, Telegram); only final replies should be delivered there. Streaming/tool events may still go to internal UIs/control channel.
- For manual `openclaw message send` messages that include `!`, use the heredoc pattern noted below to avoid the Bash tool’s escaping.
- Release guardrails: do not change version numbers without operator’s explicit consent; always ask permission before running any npm publish/release step.
- Beta release guardrail: when using a beta Git tag (for example `vYYYY.M.D-beta.N`), publish npm with a matching beta version suffix (for example `YYYY.M.D-beta.N`) rather than a plain version on `--tag beta`; otherwise the plain version name gets consumed/blocked.
```

### `CLAUDE.md`

- Source path: `CLAUDE.md`
- Truncated: `no`

```md
# Repository Guidelines

- Repo: https://github.com/openclaw/openclaw
- In chat replies, file references must be repo-root relative only (example: `src/telegram/index.ts:80`); never absolute paths or `~/...`.
- Do not edit files covered by security-focused `CODEOWNERS` rules unless a listed owner explicitly asked for the change or is already reviewing it with you. Treat those paths as restricted surfaces, not drive-by cleanup.

## Project Structure & Module Organization

- Source code: `src/` (CLI wiring in `src/cli`, commands in `src/commands`, web provider in `src/provider-web.ts`, infra in `src/infra`, media pipeline in `src/media`).
- Tests: colocated `*.test.ts`.
- Docs: `docs/` (images, queue, Pi config). Built output lives in `dist/`.
- Nomenclature: use "plugin" / "plugins" in docs, UI, changelogs, and contributor guidance. The bundled workspace plugin tree remains the internal package layout to avoid repo-wide churn from a rename.
- Bundled plugin naming: for repo-owned workspace plugins, keep the canonical plugin id aligned across `openclaw.plugin.json:id`, the default workspace folder name, and package names anchored to the same id (`@openclaw/<id>` or approved suffix forms like `-provider`, `-plugin`, `-speech`, `-sandbox`, `-media-understanding`). Keep `openclaw.install.npmSpec` equal to the package name and `openclaw.channel.id` equal to the plugin id when present. Exceptions must be explicit and covered by the repo invariant test.
- Plugins: live in the bundled workspace plugin tree (workspace packages). Keep plugin-only deps in the extension `package.json`; do not add them to the root `package.json` unless core uses them.
- Plugins: install runs `npm install --omit=dev` in plugin dir; runtime deps must live in `dependencies`. Avoid `workspace:*` in `dependencies` (npm install breaks); put `openclaw` in `devDependencies` or `peerDependencies` instead (runtime resolves `openclaw/plugin-sdk` via jiti alias).
- Import boundaries: extension production code should treat `openclaw/plugin-sdk/*` plus local `api.ts` / `runtime-api.ts` barrels as the public surface. Do not import core `src/**`, `src/plugin-sdk-internal/**`, or another extension's `src/**` directly.
- Installers served from `https://openclaw.ai/*`: live in the sibling repo `../openclaw.ai` (`public/install.sh`, `public/install-cli.sh`, `public/install.ps1`).
- Messaging channels: always consider **all** built-in + extension channels when refactoring shared logic (routing, allowlists, pairing, command gating, onboarding, docs).
  - Core channel docs: `docs/channels/`
  - Core channel code: `src/telegram`, `src/discord`, `src/slack`, `src/signal`, `src/imessage`, `src/web` (WhatsApp web), `src/channels`, `src/routing`
  - Bundled plugin channels: the workspace plugin tree (for example Matrix, Zalo, ZaloUser, Voice Call)
- When adding channels/plugins/apps/docs, update `.github/labeler.yml` and create matching GitHub labels (use existing channel/plugin label colors).

## Architecture Boundaries

- Start here for the repo map:
  - bundled workspace plugin tree = bundled plugins and the closest example surface for third-party plugins
  - `src/plugin-sdk/*` = the public plugin contract that extensions are allowed to import
  - `src/channels/*` = core channel implementation details behind the plugin/channel boundary
  - `src/plugins/*` = plugin discovery, manifest validation, loader, registry, and contract enforcement
  - `src/gateway/protocol/*` = typed Gateway control-plane and node wire protocol
- Progressive disclosure lives in local boundary guides:
  - repo root `AGENTS.md`
  - bundled-plugin-tree `extensions/AGENTS.md`
  - `src/plugin-sdk/AGENTS.md`
  - `src/channels/AGENTS.md`
  - `src/plugins/AGENTS.md`
  - `src/gateway/protocol/AGENTS.md`
- Workflow hygiene:
  - Do not grep or existence-check every `docs/*.md`, `AGENTS.md`, or guide path mentioned in this file before starting work.
  - Read only the guides and docs that are directly relevant to the files or boundary you are touching.
  - Only do full broken-link or missing-guide sweeps when the task is explicitly about docs or repo-instruction maintenance.
- Plugin and extension boundary:
  - Public docs: `docs/plugins/building-plugins.md`, `docs/plugins/architecture.md`, `docs/plugins/sdk-overview.md`, `docs/plugins/sdk-entrypoints.md`, `docs/plugins/sdk-runtime.md`, `docs/plugins/manifest.md`, `docs/plugins/sdk-channel-plugins.md`, `docs/plugins/sdk-provider-plugins.md`
  - Definition files: `src/plugin-sdk/plugin-entry.ts`, `src/plugin-sdk/core.ts`, `src/plugin-sdk/provider-entry.ts`, `src/plugin-sdk/channel-contract.ts`, `scripts/lib/plugin-sdk-entrypoints.json`, `package.json`
  - Invariant: core must stay extension-agnostic. Adding a bundled or third-party extension should not require unrelated core edits just to teach core that the extension exists.
  - Rule: extensions must cross into core only through `openclaw/plugin-sdk/*`, manifest metadata, and documented runtime helpers. Do not import `src/**` from extension production code.
  - Rule: core code and tests must not deep-import bundled plugin internals such as a plugin's `src/**` files or `onboard.js`. If core needs a bundled plugin helper, expose it through that plugin's `api.ts` and, when it is a real cross-package contract, through `src/plugin-sdk/<id>.ts`.
  - Rule: do not add hardcoded bundled extension/provider/channel/capability id lists, maps, or named special cases in core when a manifest, capability, registry, or plugin-owned contract can express the same behavior.
  - Rule: extension-owned compatibility behavior belongs to the owning extension. Core may orchestrate generic doctor/config flows, but extension-specific legacy repairs, detection rules, onboarding, auth detection, and provider defaults should live in plugin-owned contracts.
  - Rule: for legacy config specifically, prefer doctor-owned repair paths over startup/load-time core migrations. Do not add new plugin-specific legacy migration logic to shared core/runtime surfaces when `openclaw doctor --fix` can own it.
  - Rule: when a test is asserting extension-specific behavior, keep that coverage in the owning extension when feasible. Core tests should assert generic contracts and registry/capability behavior, not extension internals.
  - Refactor trigger: if you encounter core code or tests that name a specific extension/provider/channel for extension-owned behavior, refactor toward a generic registry/capability/plugin-owned seam instead of adding another special case.
  - Compatibility: new plugin seams are allowed, but they must be added as documented, backwards-compatible, versioned contracts. We have third-party plugins in the wild and do not break them casually.
- Channel boundary:
  - Public docs: `docs/plugins/sdk-channel-plugins.md`, `docs/plugins/architecture.md`
  - Definition files: `src/channels/plugins/types.plugin.ts`, `src/channels/plugins/types.core.ts`, `src/channels/plugins/types.adapters.ts`, `src/plugin-sdk/core.ts`, `src/plugin-sdk/channel-contract.ts`
  - Rule: `src/channels/**` is core implementation. If plugin authors need a new seam, add it to the Plugin SDK instead of telling them to import channel internals.
- Provider/model boundary:
  - Public docs: `docs/plugins/sdk-provider-plugins.md`, `docs/concepts/model-providers.md`, `docs/plugins/architecture.md`
  - Definition files: `src/plugins/types.ts`, `src/plugin-sdk/provider-entry.ts`, `src/plugin-sdk/provider-auth.ts`, `src/plugin-sdk/provider-catalog-shared.ts`, `src/plugin-sdk/provider-model-shared.ts`
  - Rule: core owns the generic inference loop; provider plugins own provider-specific behavior through registration and typed hooks. Do not solve provider needs by reaching into unrelated core internals.
  - Rule: avoid ad hoc reads of `plugins.entries.<id>.config` from unrelated core code. If core needs plugin-owned auth/config behavior, add or use a generic seam (`resolveSyntheticAuth`, public SDK/helper facades, manifest metadata, plugin auto-enable hooks) and honor plugin disablement plus SecretRef semantics.
  - Rule: vendor-owned tools and settings belong in the owning plugin. Do not add provider-specific tool config, secret collection, or runtime enablement to core `tools.*` surfaces unless the tool is intentionally core-owned.
- Gateway protocol boundary:
  - Public docs: `docs/gateway/protocol.md`, `docs/gateway/bridge-protocol.md`, `docs/concepts/architecture.md`
  - Definition files: `src/gateway/protocol/schema.ts`, `src/gateway/protocol/schema/*.ts`, `src/gateway/protocol/index.ts`
  - Rule: protocol changes are contract changes. Prefer additive evolution; incompatible changes require explicit versioning, docs, and client/codegen follow-through.
- Config contract boundary:
  - Canonical public config lives in exported config types, zod/schema surfaces, schema help/labels, generated config metadata, config baselines, and any user-facing gateway/config payloads. Keep those surfaces aligned.
  - When a legacy config key is retired from the public contract, remove it from every public config surface above. Keep backward compatibility only through raw-config migration/doctor seams unless explicit product policy says otherwise.
  - Do not reintroduce removed legacy aliases into public types/schema/help/baselines “for convenience”. If old configs still need to load, handle that in `legacy.migrations.*`, config ingest, or `openclaw doctor --fix`.
  - `hooks.internal.entries` is the canonical public hook config model. `hooks.internal.handlers` is compatibility-only input and must not be re-exposed in public schema/help/baseline surfaces.
- Bundled plugin contract boundary:
  - Public docs: `docs/plugins/architecture.md`, `docs/plugins/manifest.md`, `docs/plugins/sdk-overview.md`
  - Definition files: `src/plugins/contracts/registry.ts`, `src/plugins/types.ts`, `src/plugins/public-artifacts.ts`
  - Rule: keep manifest metadata, runtime registration, public SDK exports, and contract tests aligned. Do not create a hidden path around the declared plugin interfaces.
- Extension test boundary:
  - Keep extension-owned onboarding/config/provider coverage under the owning bundled plugin package when feasible.
  - If core tests need bundled plugin behavior, consume it through public `src/plugin-sdk/<id>.ts` facades or the plugin's `api.ts`, not private extension modules.
  - Shared helpers under `test/helpers/**` are part of that same boundary. Do not hardcode repo-relative `extensions/**` imports there, and do not keep plugin-local deep mocks in shared helpers just because multiple tests use them.
  - When core tests or shared helpers need bundled plugin public surfaces, use `src/test-utils/bundled-plugin-public-surface.ts` for `api.ts`, `runtime-api.ts`, `contract-api.ts`, `test-api.ts`, plugin entrypoint `index.js`, and resolved module ids for dynamic import or mocking.
  - If a core test is asserting extension-specific behavior instead of a generic contract, move it to the owning extension package.
- Scoped guides still matter:
  - `extensions/AGENTS.md` expands extension/plugin boundary rules.
  - `src/channels/AGENTS.md` expands core channel boundary and hot-path rules.
  - `src/plugin-sdk/AGENTS.md` expands public SDK contract rules.
  - `src/plugins/AGENTS.md` expands plugin loading, registry, and manifest rules.
  - `src/gateway/protocol/AGENTS.md` expands typed Gateway protocol rules.
  - `test/helpers/AGENTS.md` and `test/helpers/channels/AGENTS.md` expand shared test helper boundary rules.
- Plugin architecture direction:
  - Keep a manifest-first control plane: discovery, validation, enablement, setup hints, and activation planning should stay metadata-driven by default.
  - Keep runtime execution separate: actual provider/channel/tool execution should resolve through narrow targeted loaders, not broad registry materialization.
  - Host loads plugins; plugins do not load host internals. Prefer a small versioned host/kernel seam plus documented SDK entrypoints over ambient reachability.
  - Treat broad runtime registries and mutable global plugin state as transitional compatibility surfaces, not the target architecture.
  - If a setup or config flow truly needs plugin runtime, make that explicit instead of silently importing runtime code on the cold path.

## Scoped Workflow Guides

- `docs/AGENTS.md` owns Mintlify docs, docs links, and docs i18n rules.
- `ui/AGENTS.md` owns Control UI i18n and generated locale rules.
- `scripts/AGENTS.md` owns script-runner, local-check lock, and test/lint wrapper rules.

## exe.dev VM ops (general)

- Access: stable path is `ssh exe.dev` then `ssh vm-name` (assume SSH key already set).
- SSH flaky: use exe.dev web terminal or Shelley (web agent); keep a tmux session for long ops.
- Update: `sudo npm i -g openclaw@latest` (global install needs root on `/usr/lib/node_modules`).
- Config: use `openclaw config set ...`; ensure `gateway.mode=local` is set.
- Discord: store raw token only (no `DISCORD_BOT_TOKEN=` prefix).
- Restart: stop old gateway and run:
  `pkill -9 -f openclaw-gateway || true; nohup openclaw gateway run --bind loopback --port 18789 --force > /tmp/openclaw-gateway.log 2>&1 &`
- Verify: `openclaw channels status --probe`, `ss -ltnp | rg 18789`, `tail -n 120 /tmp/openclaw-gateway.log`.

## Build, Test, and Development Commands

- Runtime baseline: Node **22+** (keep Node + Bun paths working).
- Install deps: `pnpm install`
- If deps are missing (for example `node_modules` missing, `vitest not found`, or `command not found`), run the repo’s package-manager install command (prefer lockfile/README-defined PM), then rerun the exact requested command once. Apply this to test/build/lint/typecheck/dev commands; if retry still fails, report the command and first actionable error.
- Pre-commit hooks: `prek install`. The hook runs the repo verification flow, including `pnpm check`.
- `FAST_COMMIT=1` skips the repo-wide `pnpm format` and `pnpm check` inside the pre-commit hook only. Use it when you intentionally want a faster commit path and are running equivalent targeted verification manually. It does not change CI and does not change what `pnpm check` itself does.
- Also supported: `bun install` (keep `pnpm-lock.yaml` + Bun patching in sync when touching deps/patches).
- Prefer Bun for TypeScript execution (scripts, dev, tests): `bun <file.ts>` / `bunx <tool>`.
- Run CLI in dev: `pnpm openclaw ...` (bun) or `pnpm dev`.
- Node remains supported for running built output (`dist/*`) and production installs.
- Mac packaging (dev): `scripts/package-mac-app.sh` defaults to current arch.
- Type-check/build: `pnpm build`
- TypeScript checks: `pnpm tsgo`
- Lint/format: `pnpm check`
- Local agent/dev shells default to host-aware `OPENCLAW_LOCAL_CHECK=1` behavior for `pnpm tsgo` and `pnpm lint`; set `OPENCLAW_LOCAL_CHECK_MODE=throttled` to force the lower-memory profile, `OPENCLAW_LOCAL_CHECK_MODE=full` to keep lock-only behavior, or `OPENCLAW_LOCAL_CHECK=0` in CI/shared runs.
- Format check: `pnpm format` (oxfmt --check)
- Format fix: `pnpm format:fix` (oxfmt --write)
- Terminology:
  - "gate" means a verification command or command set that must be green for the decision you are making.
  - A local dev gate is the fast default loop, usually `pnpm check` plus any scoped test you actually need.
  - A landing gate is the broader bar before pushing `main`, usually `pnpm check`, `pnpm test`, and `pnpm build` when the touched surface can affect build output, packaging, lazy-loading/module boundaries, or published surfaces.
  - A CI gate is whatever the relevant workflow enforces for that lane (for example `check`, `check-additional`, `build-smoke`, or release validation).
- Local dev gate: prefer `pnpm check` for the normal edit loop. It keeps the repo-architecture policy guards out of the default local loop.
- CI architecture gate: `check-additional` enforces architecture and boundary policy guards that are intentionally kept out of the default local loop.
- Formatting gate: the pre-commit hook runs `pnpm format` before `pnpm check`. If you want a formatting-only preflight locally, run `pnpm format` explicitly.
- If you need a fast commit loop, `FAST_COMMIT=1 git commit ...` skips the hook’s repo-wide `pnpm format` and `pnpm check`; use that only when you are deliberately covering the touched surface some other way.
- Tests: `pnpm test` (vitest); coverage: `pnpm test:coverage`
- Generated baseline drift detection uses SHA-256 hash files under `docs/.generated/` (`.sha256` files tracked in git; full JSON baselines are gitignored, generated locally for inspection).
- Config schema drift uses `pnpm config:docs:gen` / `pnpm config:docs:check`.
- Plugin SDK API drift uses `pnpm plugin-sdk:api:gen` / `pnpm plugin-sdk:api:check`.
- If you change config schema/help or the public Plugin SDK surface, run the matching gen command and commit the updated `.sha256` hash file. Keep the two drift-check flows adjacent in scripts/workflows/docs guidance rather than inventing a third pattern.
- When `pnpm tsgo` fails, triage by coherent surface instead of by raw error count: rerun the gate, group failures by package/module/type contract, open the source-of-truth type or export file first, fix the root mismatch, then rerun `pnpm tsgo` before widening into downstream consumers. Check `origin/main` before doing broad cleanup because some apparent type debt is already fixed upstream.
- For narrowly scoped changes, prefer narrowly scoped tests that directly validate the touched behavior. If no meaningful scoped test exists, say so explicitly and use the next most direct validation available.
- Verification modes for work on `main`:
  - Default mode: `main` is relatively stable. Count pre-commit hook coverage when it already verified the current tree, avoid rerunning the exact same checks just for ceremony, and prefer keeping CI/main green before landing.
  - Fast-commit mode: `main` is moving fast and you intentionally optimize for shorter commit loops. Prefer explicit local verification close to the final landing point, and it is acceptable to use `--no-verify` for intermediate or catch-up commits after equivalent checks have already run locally.
- Preferred landing bar for pushes to `main`: in Default mode, favor `pnpm check` and `pnpm test` near the final rebase/push point when feasible. In fast-commit mode, verify the touched surface locally near landing without insisting every intermediate commit replay the full hook.
- Scoped tests prove the change itself. `pnpm test` remains the default `main` landing bar; scoped tests do not replace full-suite gates by default.
- Hard gate: if the change can affect build output, packaging, lazy-loading/module boundaries, or published surfaces, `pnpm build` MUST be run and MUST pass before pushing `main`.
- Default rule: do not land changes with failing format, lint, type, build, or required test checks when those failures are caused by the change or plausibly related to the touched surface. Fast-commit mode changes how verification is sequenced; it does not lower the requirement to validate and clean up the touched surface before final landing.
- For narrowly scoped changes, if unrelated failures already exist on latest `origin/main`, state that clearly, report the scoped tests you ran, and ask before broadening scope into unrelated fixes or landing despite those failures.
- Do not use scoped tests as permission to ignore plausibly related failures.

## Prompt Cache Stability

- Treat prompt-cache stability as correctness/perf-critical, not cosmetic.
- Any code that assembles model or tool payloads from maps, sets, registries, plugin lists, MCP catalogs, filesystem reads, or network results must make ordering deterministic before building the request.
- Do not rewrite older transcript/history bytes on every turn unless you intentionally want to invalidate the cached prefix. Legacy cleanup, pruning, normalization, and migration logic should preserve recent prompt bytes when possible.
- If truncation or compaction is required, prefer mutating newest or tail content first so the cached prefix stays byte-identical for as long as possible.
- For cache-sensitive changes, require a regression test that proves turn-to-turn prefix stability or deterministic request assembly; helper-local tests alone are not enough.

## Coding Style & Naming Conventions

- Language: TypeScript (ESM). Prefer strict typing; avoid `any`.
- Formatting/linting via Oxlint and Oxfmt.
- Never add `@ts-nocheck` and do not add inline lint suppressions by default. Fix root causes first; only keep a suppression when the code is intentionally correct, the rule cannot express that safely, and the comment explains why.
- Do not disable `no-explicit-any`; prefer real types, `unknown`, or a narrow adapter/helper instead. Update Oxlint/Oxfmt config only when required.
- Prefer `zod` or existing schema helpers at external boundaries such as config, webhook payloads, CLI/JSON output, persisted JSON, and third-party API responses.
- Prefer discriminated unions when parameter shape changes runtime behavior.
- Prefer `Result<T, E>`-style outcomes and closed error-code unions for recoverable runtime decisions.
- Keep human-readable strings for logs, CLI output, and UI; do not use freeform strings as the source of truth for internal branching.
- Avoid `?? 0`, empty-string, empty-object, or magic-string sentinels when they can change runtime meaning silently.
- If introducing a new optional field or nullable semantic in core logic, prefer an explicit union or dedicated type when the value changes behavior.
- New runtime control-flow code should not branch on `error: string` or `reason: string` when a closed code union would be reasonable.
- Dynamic import guardrail: do not mix `await import("x")` and static `import ... from "x"` for the same module in production code paths. If you need lazy loading, create a dedicated `*.runtime.ts` boundary (that re-exports from `x`) and dynamically import that boundary from lazy callers only.
- Dynamic import verification: after refactors that touch lazy-loading/module boundaries, run `pnpm build` and check for `[INEFFECTIVE_DYNAMIC_IMPORT]` warnings before submitting.
- Circular dependencies: keep both `pnpm check:import-cycles` and `pnpm check:static-import-sccs` green; do not reintroduce runtime import cycles or static SCCs.
- Extension SDK self-import guardrail: inside an extension package, do not import that same extension via `openclaw/plugin-sdk/<extension>` from production files. Route internal imports through a local barrel such as `./api.ts` or `./runtime-api.ts`, and keep the `plugin-sdk/<extension>` path as the external contract only.
- Extension package boundary guardrail: inside a bundled plugin package, do not use relative imports/exports that resolve outside that same package root. If shared code belongs in the plugin SDK, import `openclaw/plugin-sdk/<subpath>` instead of reaching into `src/plugin-sdk/**` or other repo paths via `../`.
- Extension API surface rule: `openclaw/plugin-sdk/<subpath>` is the only public cross-package contract for extension-facing SDK code. If an extension needs a new seam, add a public subpath first; do not reach into `src/plugin-sdk/**` by relative path.
- Never share class behavior via prototype mutation (`applyPrototypeMixins`, `Object.defineProperty` on `.prototype`, or exporting `Class.prototype` for merges). Use explicit inheritance/composition (`A extends B extends C`) or helper composition so TypeScript can typecheck.
- If this pattern is needed, stop and get explicit approval before shipping; default behavior is to split/refactor into an explicit class hierarchy and keep members strongly typed.
- In tests, prefer per-instance stubs over prototype mutation (`SomeClass.prototype.method = ...`) unless a test explicitly documents why prototype-level patching is required.
- Add brief code comments for tricky or non-obvious logic.
- Keep files concise; extract helpers instead of “V2” copies. Use existing patterns for CLI options and dependency injection via `createDefaultDeps`.
- Aim to keep files under ~700 LOC; guideline only (not a hard guardrail). Split/refactor when it improves clarity or testability.
- Naming: use **OpenClaw** for product/app/docs headings; use `openclaw` for CLI command, package/binary, paths, and config keys.
- Written English: use American spelling and grammar in code, comments, docs, and UI strings (e.g. "color" not "colour", "behavior" not "behaviour", "analyze" not "analyse").

## Release / Advisory Workflows

- Use `$openclaw-release-maintainer` at `.agents/skills/openclaw-release-maintainer/SKILL.md` for release naming, version coordination, release auth, and changelog-backed release-note workflows.
- Use `$openclaw-ghsa-maintainer` at `.agents/skills/openclaw-ghsa-maintainer/SKILL.md` for GHSA advisory inspection, patch/publish flow, private-fork checks, and GHSA API validation.
- Release and publish remain explicit-approval actions even when using the skill.

## Testing Guidelines

- Framework: Vitest with V8 coverage thresholds (70% lines/branches/functions/statements).
- Naming: match source names with `*.test.ts`; e2e in `*.e2e.test.ts`.
- When tests need example Anthropic/OpenAI model constants, prefer `sonnet-4.6` and `gpt-5.4`; update older Anthropic/GPT examples when you touch those tests.
- Run `pnpm test` (or `pnpm test:coverage`) before pushing when you touch logic.
- Write tests to clean up timers, env, globals, mocks, sockets, temp dirs, and module state so `--isolate=false` stays green.
- Test performance guardrail: do not put `vi.resetModules()` plus `await import(...)` in `beforeEach`/per-test loops for heavy modules unless module state truly requires it. Prefer static imports or one-time `beforeAll` imports, then reset mocks/runtime state directly.
- Test performance guardrail: if a test file uses stable `vi.mock(...)` hoists or other static module mocks, do not pair them with `vi.resetModules()` and a fresh `await import(...)` in every `beforeEach`. Import the heavy module once in `beforeAll`, then reset/prime mocks in `beforeEach` so Browser/Matrix-style hotspot tests do not pay the module graph cost per case.
- Test performance guardrail: inside an extension package, prefer a thin local seam (`./api.ts`, `./runtime-api.ts`, or a narrower local `*.runtime-api.ts`) over direct `openclaw/plugin-sdk/*` imports for internal production code. Keep local seams curated and lightweight; only reach for direct `plugin-sdk/*` imports when you are crossing a real package boundary or when no suitable local seam exists yet.
- Test performance guardrail: keep expensive runtime fallback work such as snapshotting, migration, installs, or bootstrap behind dedicated `*.runtime.ts` boundaries so tests can mock the seam instead of accidentally invoking real work.
- Test performance guardrail: for import-only/runtime-wrapper tests, keep the wrapper lazy. Do not eagerly load heavy verification/bootstrap/runtime modules at module top level if the exported function can import them on demand.
- Test performance guardrail: prefer explicit mock factories over `importOriginal()` for broad modules. Reserve `importOriginal()` for narrow modules where partial-real behavior is genuinely needed.
- Test performance guardrail: do not partial-mock broad `openclaw/plugin-sdk/*` barrels in hot tests. Add a plugin-local `*.runtime.ts` seam and mock that seam instead.
- Test performance guardrail: when production code already accepts `deps`, callbacks, or runtime injection, use that seam in tests before adding module-level mocks.
- Test performance guardrail: prefer narrow public SDK subpaths such as `models-provider-runtime`, `skill-commands-runtime`, and `reply-dispatch-runtime` over older broad helper barrels when both expose the needed helper.
- Test performance guardrail: treat import-dominated test time as a boundary bug. Refactor the import surface before adding more cases to the slow file.
- Agents MUST NOT modify baseline, inventory, ignore, snapshot, or expected-failure files to silence failing checks without explicit approval in this chat.
- For targeted/local debugging, use the native root-project entrypoint: `pnpm test <path-or-filter> [vitest args...]` (for example `pnpm test src/commands/onboard-search.test.ts -t "shows registered plugin providers"`); do not default to raw `pnpm vitest run ...` because it bypasses the repo's default config/profile/pool routing.
- Do not set test workers above 16; tried already.
- Vitest now defaults to native root-project `threads`, with hard `forks` exceptions for `gateway`, `agents`, and `commands`. Keep new pool changes explicit and justified; use `OPENCLAW_VITEST_POOL=forks` for full local fork debugging.
- If local Vitest runs cause memory pressure, the default worker budget now derives from host capabilities (CPU, memory band, current load). For a conservative explicit override during land/gate runs, use `OPENCLAW_VITEST_MAX_WORKERS=1 pnpm test`.
- Live tests (real keys): `OPENCLAW_LIVE_TEST=1 pnpm test:live` (OpenClaw-only) or `LIVE=1 pnpm test:live` (includes provider live tests). Docker: `pnpm test:docker:live-models`, `pnpm test:docker:live-gateway`. Onboarding Docker E2E: `pnpm test:docker:onboard`.
- `pnpm test:live` defaults quiet now. Keep `[live]` progress; suppress profile/gateway chatter. Full logs: `OPENCLAW_LIVE_TEST_QUIET=0 pnpm test:live`.
- Full kit + what’s covered: `docs/help/testing.md`.
- Changelog: user-facing changes only; no internal/meta notes (version alignment, appcast reminders, release process).
- Changelog placement: in the active version block, append new entries to the end of the target section (`### Changes` or `### Fixes`); do not insert new entries at the top of a section.
- Changelog attribution: use at most one contributor mention per line; prefer `Thanks @author` and do not also add `by @author` on the same entry.
- Pure test additions/fixes generally do **not** need a changelog entry unless they alter user-facing behavior or the user asks for one.
- Mobile: before using a simulator, check for connected real devices (iOS + Android) and prefer them when available.

## Commit & Pull Request Guidelines

- Use `$openclaw-pr-maintainer` at `.agents/skills/openclaw-pr-maintainer/SKILL.md` for maintainer PR triage, review, close, search, and landing workflows.
- This includes auto-close labels, bug-fix evidence gates, GitHub comment/search footguns, and maintainer PR decision flow.
- For the repo's end-to-end maintainer PR workflow, use `$openclaw-pr-maintainer` at `.agents/skills/openclaw-pr-maintainer/SKILL.md`.

- `/landpr` lives in the global Codex prompts (`~/.codex/prompts/landpr.md`); when landing or merging any PR, always follow that `/landpr` process.
- Create commits with `scripts/committer "<msg>" <file...>`; avoid manual `git add`/`git commit` so staging stays scoped.
- Follow concise, action-oriented commit messages (e.g., `CLI: add verbose flag to send`).
- Group related changes; avoid bundling unrelated refactors.
- PR submission template (canonical): `.github/pull_request_template.md`
- Issue submission templates (canonical): `.github/ISSUE_TEMPLATE/`

## Git Notes

- If `git branch -d/-D <branch>` is policy-blocked, delete the local ref directly: `git update-ref -d refs/heads/<branch>`.
- Agents MUST NOT create or push merge commits on `main`. If `main` has advanced, rebase local commits onto the latest `origin/main` before pushing.
- Bulk PR close/reopen safety: if a close action would affect more than 5 PRs, first ask for explicit user confirmation with the exact PR count and target scope/query.

## Security & Configuration Tips

- Web provider stores creds at `~/.openclaw/credentials/`; rerun `openclaw login` if logged out.
- Pi sessions live under `~/.openclaw/sessions/` by default; the base directory is not configurable.
- Environment variables: see `~/.profile`.
- Never commit or publish real phone numbers, videos, or live configuration values. Use obviously fake placeholders in docs, tests, and examples.
- Release flow: use the private [maintainer release docs](https://github.com/openclaw/maintainers/blob/main/release/README.md) for the actual runbook, `docs/reference/RELEASING.md` for the public release policy, and `$openclaw-release-maintainer` for the maintainership workflow.

## Local Runtime / Platform Notes

- Vocabulary: "makeup" = "mac app".
- Rebrand/migration issues or legacy config/service warnings: run `openclaw doctor` (see `docs/gateway/doctor.md`).
- Use `$openclaw-parallels-smoke` at `.agents/skills/openclaw-parallels-smoke/SKILL.md` for Parallels smoke, rerun, upgrade, debug, and result-interpretation workflows across macOS, Windows, and Linux guests.
- For the macOS Discord roundtrip deep dive, use the narrower `.agents/skills/parallels-discord-roundtrip/SKILL.md` companion skill.
- Never edit `node_modules` (global/Homebrew/npm/git installs too). Updates overwrite. Skill notes go in `tools.md` or `AGENTS.md`.
- If you need local-only `.agents` ignores, use `.git/info/exclude` instead of repo `.gitignore`.
- When adding a new `AGENTS.md` anywhere in the repo, also add a `CLAUDE.md` symlink pointing to it (example: `ln -s AGENTS.md CLAUDE.md`).
- Signal: "update fly" => `fly ssh console -a flawd-bot -C "bash -lc 'cd /data/clawd/openclaw && git pull --rebase origin main'"` then `fly machines restart e825232f34d058 -a flawd-bot`.
- CLI progress: use `src/cli/progress.ts` (`osc-progress` + `@clack/prompts` spinner); don’t hand-roll spinners/bars.
- Status output: keep tables + ANSI-safe wrapping (`src/terminal/table.ts`); `status --all` = read-only/pasteable, `status --deep` = probes.
- Gateway currently runs only as the menubar app; there is no separate LaunchAgent/helper label installed. Restart via the OpenClaw Mac app or `scripts/restart-mac.sh`; to verify/kill use `launchctl print gui/$UID | grep openclaw` rather than assuming a fixed label. **When debugging on macOS, start/stop the gateway via the app, not ad-hoc tmux sessions; kill any temporary tunnels before handoff.**
- macOS logs: use `./scripts/clawlog.sh` to query unified logs for the OpenClaw subsystem; it supports follow/tail/category filters and expects passwordless sudo for `/usr/bin/log`.
- If shared guardrails are available locally, review them; otherwise follow this repo's guidance.
- SwiftUI state management (iOS/macOS): prefer the `Observation` framework (`@Observable`, `@Bindable`) over `ObservableObject`/`@StateObject`; don’t introduce new `ObservableObject` unless required for compatibility, and migrate existing usages when touching related code.
- Connection providers: when adding a new connection, update every UI surface and docs (macOS app, web UI, mobile if applicable, onboarding/overview docs) and add matching status + configuration forms so provider lists and settings stay in sync.
- Version locations: `package.json` (CLI), `apps/android/app/build.gradle.kts` (versionName/versionCode), `apps/ios/Sources/Info.plist` + `apps/ios/Tests/Info.plist` (CFBundleShortVersionString/CFBundleVersion), `apps/macos/Sources/OpenClaw/Resources/Info.plist` (CFBundleShortVersionString/CFBundleVersion), `docs/install/updating.md` (pinned npm version), and Peekaboo Xcode projects/Info.plists (MARKETING_VERSION/CURRENT_PROJECT_VERSION).
- "Bump version everywhere" means all version locations above **except** `appcast.xml` (only touch appcast when cutting a new macOS Sparkle release).
- **Restart apps:** “restart iOS/Android apps” means rebuild (recompile/install) and relaunch, not just kill/launch.
- **Device checks:** before testing, verify connected real devices (iOS/Android) before reaching for simulators/emulators.
- Mobile pairing: `ws://` (cleartext) is allowed for private LAN addresses (RFC 1918, link-local, mDNS `.local`) and loopback. Private LAN hosts typically lack PKI-backed identity, so requiring TLS there adds complexity without meaningful security gain. `wss://` is required for Tailscale and public endpoints.
- Security report scope: reports that treat cleartext `ws://` mobile pairing over private LAN as a vulnerability are out of scope unless they demonstrate a trust-boundary bypass beyond passive network observation on the same LAN.
- iOS Team ID lookup: `security find-identity -p codesigning -v` → use Apple Development (…) TEAMID. Fallback: `defaults read com.apple.dt.Xcode IDEProvisioningTeamIdentifiers`.
- A2UI bundle hash: `src/canvas-host/a2ui/.bundle.hash` is auto-generated; ignore unexpected changes, and only regenerate via `pnpm canvas:a2ui:bundle` (or `scripts/bundle-a2ui.sh`) when needed. Commit the hash as a separate commit.
- Release signing/notary credentials are managed outside the repo; maintainers keep that setup in the private [maintainer release docs](https://github.com/openclaw/maintainers/tree/main/release).
- Lobster palette: use the shared CLI palette in `src/terminal/palette.ts` (no hardcoded colors); apply palette to onboarding/config prompts and other TTY UI output as needed.
- When asked to open a “session” file, open the Pi session logs under `~/.openclaw/agents/<agentId>/sessions/*.jsonl` (use the `agent=<id>` value in the Runtime line of the system prompt; newest unless a specific ID is given), not the default `sessions.json`. If logs are needed from another machine, SSH via Tailscale and read the same path there.
- Do not rebuild the macOS app over SSH; rebuilds must be run directly on the Mac.
- Voice wake forwarding tips:
  - Command template should stay `openclaw-mac agent --message "${text}" --thinking low`; `VoiceWakeForwarder` already shell-escapes `${text}`. Don’t add extra quotes.
  - launchd PATH is minimal; ensure the app’s launch agent PATH includes standard system paths plus your pnpm bin (typically `$HOME/Library/pnpm`) so `pnpm`/`openclaw` binaries resolve when invoked via `openclaw-mac`.

## Collaboration / Safety Notes

- When working on a GitHub Issue or PR, print the full URL at the end of the task.
- When answering questions, respond with high-confidence answers only: verify in code; do not guess.
- Carbon version edits are owner-only: do not change `@buape/carbon` version pins unless you are Shadow (@thewilloftheshadow) as verified by gh.
- Any dependency with `pnpm.patchedDependencies` must use an exact version (no `^`/`~`).
- Patching dependencies (pnpm patches, overrides, or vendored changes) requires explicit approval; do not do this by default.
- **Multi-agent safety:** do **not** create/apply/drop `git stash` entries unless explicitly requested (this includes `git pull --rebase --autostash`). Assume other agents may be working; keep unrelated WIP untouched and avoid cross-cutting state changes.
- **Multi-agent safety:** when the user says "push", you may `git pull --rebase` to integrate latest changes (never discard other agents' work). When the user says "commit", scope to your changes only. When the user says "commit all", commit everything in grouped chunks.
- **Multi-agent safety:** prefer grouped `commit` / `pull --rebase` / `push` cycles for related work instead of many tiny syncs.
- **Multi-agent safety:** do **not** create/remove/modify `git worktree` checkouts (or edit `.worktrees/*`) unless explicitly requested.
- **Multi-agent safety:** do **not** switch branches / check out a different branch unless explicitly requested.
- **Multi-agent safety:** running multiple agents is OK as long as each agent has its own session.
- **Multi-agent safety:** when you see unrecognized files, keep going; focus on your changes and commit only those.
- Lint/format churn:
  - If staged+unstaged diffs are formatting-only, auto-resolve without asking.
  - If commit/push already requested, auto-stage and include formatting-only follow-ups in the same commit (or a tiny follow-up commit if needed), no extra confirmation.
  - Only ask when changes are semantic (logic/data/behavior).
- **Multi-agent safety:** focus reports on your edits; avoid guard-rail disclaimers unless truly blocked; when multiple agents touch the same file, continue if safe; end with a brief “other files present” note only if relevant.
- Bug investigations: read source code of relevant npm dependencies and all related local code before concluding; aim for high-confidence root cause.
- Code style: add brief comments for tricky logic; keep files under ~700 LOC when feasible (split/refactor as needed).
- Tool schema guardrails (google-antigravity): avoid `Type.Union` in tool input schemas; no `anyOf`/`oneOf`/`allOf`. Use `stringEnum`/`optionalStringEnum` (Type.Unsafe enum) for string lists, and `Type.Optional(...)` instead of `... | null`. Keep top-level tool schema as `type: "object"` with `properties`.
- Tool schema guardrails: avoid raw `format` property names in tool schemas; some validators treat `format` as a reserved keyword and reject the schema.
- Never send streaming/partial replies to external messaging surfaces (WhatsApp, Telegram); only final replies should be delivered there. Streaming/tool events may still go to internal UIs/control channel.
- For manual `openclaw message send` messages that include `!`, use the heredoc pattern noted below to avoid the Bash tool’s escaping.
- Release guardrails: do not change version numbers without operator’s explicit consent; always ask permission before running any npm publish/release step.
- Beta release guardrail: when using a beta Git tag (for example `vYYYY.M.D-beta.N`), publish npm with a matching beta version suffix (for example `YYYY.M.D-beta.N`) rather than a plain version on `--tag beta`; otherwise the plain version name gets consumed/blocked.
```

### `Dockerfile`

- Source path: `Dockerfile`
- Truncated: `no`

```
# syntax=docker/dockerfile:1.7

# Opt-in extension dependencies at build time (space-separated directory names).
# Example: docker build --build-arg OPENCLAW_EXTENSIONS="diagnostics-otel matrix" .
#
# Multi-stage build produces a minimal runtime image without build tools,
# source code, or Bun. Works with Docker, Buildx, and Podman.
# The ext-deps stage extracts only the package.json files we need from the
# bundled plugin workspace tree, so the main build layer is not invalidated by
# unrelated plugin source changes.
#
# Two runtime variants:
#   Default (bookworm):      docker build .
#   Slim (bookworm-slim):    docker build --build-arg OPENCLAW_VARIANT=slim .
ARG OPENCLAW_EXTENSIONS=""
ARG OPENCLAW_VARIANT=default
ARG OPENCLAW_BUNDLED_PLUGIN_DIR=extensions
ARG OPENCLAW_DOCKER_APT_UPGRADE=1
ARG OPENCLAW_NODE_BOOKWORM_IMAGE="node:24-bookworm@sha256:3a09aa6354567619221ef6c45a5051b671f953f0a1924d1f819ffb236e520e6b"
ARG OPENCLAW_NODE_BOOKWORM_DIGEST="sha256:3a09aa6354567619221ef6c45a5051b671f953f0a1924d1f819ffb236e520e6b"
ARG OPENCLAW_NODE_BOOKWORM_SLIM_IMAGE="node:24-bookworm-slim@sha256:e8e2e91b1378f83c5b2dd15f0247f34110e2fe895f6ca7719dbb780f929368eb"
ARG OPENCLAW_NODE_BOOKWORM_SLIM_DIGEST="sha256:e8e2e91b1378f83c5b2dd15f0247f34110e2fe895f6ca7719dbb780f929368eb"

# Base images are pinned to SHA256 digests for reproducible builds.
# Trade-off: digests must be updated manually when upstream tags move.
# To update, run: docker buildx imagetools inspect node:24-bookworm (or podman)
# and replace the digest below with the current multi-arch manifest list entry.

FROM ${OPENCLAW_NODE_BOOKWORM_IMAGE} AS ext-deps
ARG OPENCLAW_EXTENSIONS
ARG OPENCLAW_BUNDLED_PLUGIN_DIR
COPY ${OPENCLAW_BUNDLED_PLUGIN_DIR} /tmp/${OPENCLAW_BUNDLED_PLUGIN_DIR}
# Copy package.json for opted-in extensions so pnpm resolves their deps.
RUN mkdir -p /out && \
    for ext in $OPENCLAW_EXTENSIONS; do \
      if [ -f "/tmp/${OPENCLAW_BUNDLED_PLUGIN_DIR}/$ext/package.json" ]; then \
        mkdir -p "/out/$ext" && \
        cp "/tmp/${OPENCLAW_BUNDLED_PLUGIN_DIR}/$ext/package.json" "/out/$ext/package.json"; \
      fi; \
    done

# ── Stage 2: Build ──────────────────────────────────────────────
FROM ${OPENCLAW_NODE_BOOKWORM_IMAGE} AS build
ARG OPENCLAW_BUNDLED_PLUGIN_DIR

# Install Bun (required for build scripts). Retry the whole bootstrap flow to
# tolerate transient 5xx failures from bun.sh/GitHub during CI image builds.
RUN set -eux; \
    for attempt in 1 2 3 4 5; do \
      if curl --retry 5 --retry-all-errors --retry-delay 2 -fsSL https://bun.sh/install | bash; then \
        break; \
      fi; \
      if [ "$attempt" -eq 5 ]; then \
        exit 1; \
      fi; \
      sleep $((attempt * 2)); \
    done
ENV PATH="/root/.bun/bin:${PATH}"

RUN corepack enable

WORKDIR /app

COPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./
COPY openclaw.mjs ./
COPY ui/package.json ./ui/package.json
COPY patches ./patches
COPY scripts/postinstall-bundled-plugins.mjs scripts/npm-runner.mjs scripts/windows-cmd-helpers.mjs ./scripts/

COPY --from=ext-deps /out/ ./${OPENCLAW_BUNDLED_PLUGIN_DIR}/

# Reduce OOM risk on low-memory hosts during dependency installation.
# Docker builds on small VMs may otherwise fail with "Killed" (exit 137).
RUN --mount=type=cache,id=openclaw-pnpm-store,target=/root/.local/share/pnpm/store,sharing=locked \
    NODE_OPTIONS=--max-old-space-size=2048 pnpm install --frozen-lockfile

COPY . .

# Normalize extension paths now so runtime COPY preserves safe modes
# without adding a second full extensions layer.
RUN for dir in /app/${OPENCLAW_BUNDLED_PLUGIN_DIR} /app/.agent /app/.agents; do \
      if [ -d "$dir" ]; then \
        find "$dir" -type d -exec chmod 755 {} +; \
        find "$dir" -type f -exec chmod 644 {} +; \
      fi; \
    done

# A2UI bundle may fail under QEMU cross-compilation (e.g. building amd64
# on Apple Silicon). CI builds natively per-arch so this is a no-op there.
# Stub it so local cross-arch builds still succeed.
RUN pnpm canvas:a2ui:bundle || \
    (echo "A2UI bundle: creating stub (non-fatal)" && \
     mkdir -p src/canvas-host/a2ui && \
     echo "/* A2UI bundle unavailable in this build */" > src/canvas-host/a2ui/a2ui.bundle.js && \
     echo "stub" > src/canvas-host/a2ui/.bundle.hash && \
     rm -rf vendor/a2ui apps/shared/OpenClawKit/Tools/CanvasA2UI)
RUN pnpm build:docker
# Force pnpm for UI build (Bun may fail on ARM/Synology architectures)
ENV OPENCLAW_PREFER_PNPM=1
RUN pnpm ui:build
RUN pnpm qa:lab:build

# Prune dev dependencies and strip build-only metadata before copying
# runtime assets into the final image.
FROM build AS runtime-assets
ARG OPENCLAW_EXTENSIONS
ARG OPENCLAW_BUNDLED_PLUGIN_DIR
# Keep the install layer frozen, but allow prune to run against the full copied
# workspace tree subset used during `pnpm install`. The build stage only copied
# the root, `ui`, and opted-in plugin manifests into the install layer, so
# prune must not rediscover unrelated workspaces from the later full source
# copy.
RUN printf 'packages:\n  - .\n  - ui\n' > /tmp/pnpm-workspace.runtime.yaml && \
    for ext in $OPENCLAW_EXTENSIONS; do \
      printf '  - %s/%s\n' "$OPENCLAW_BUNDLED_PLUGIN_DIR" "$ext" >> /tmp/pnpm-workspace.runtime.yaml; \
    done && \
    cp /tmp/pnpm-workspace.runtime.yaml pnpm-workspace.yaml && \
    CI=true NPM_CONFIG_FROZEN_LOCKFILE=false pnpm prune --prod && \
    find dist -type f \( -name '*.d.ts' -o -name '*.d.mts' -o -name '*.d.cts' -o -name '*.map' \) -delete

# ── Runtime base images ─────────────────────────────────────────
FROM ${OPENCLAW_NODE_BOOKWORM_IMAGE} AS base-default
ARG OPENCLAW_NODE_BOOKWORM_DIGEST
LABEL org.opencontainers.image.base.name="docker.io/library/node:24-bookworm" \
  org.opencontainers.image.base.digest="${OPENCLAW_NODE_BOOKWORM_DIGEST}"

FROM ${OPENCLAW_NODE_BOOKWORM_SLIM_IMAGE} AS base-slim
ARG OPENCLAW_NODE_BOOKWORM_SLIM_DIGEST
LABEL org.opencontainers.image.base.name="docker.io/library/node:24-bookworm-slim" \
  org.opencontainers.image.base.digest="${OPENCLAW_NODE_BOOKWORM_SLIM_DIGEST}"

# ── Stage 3: Runtime ────────────────────────────────────────────
FROM base-${OPENCLAW_VARIANT}
ARG OPENCLAW_VARIANT
ARG OPENCLAW_BUNDLED_PLUGIN_DIR
ARG OPENCLAW_DOCKER_APT_UPGRADE

# OCI base-image metadata for downstream image consumers.
# If you change these annotations, also update:
# - docs/install/docker.md ("Base image metadata" section)
# - https://docs.openclaw.ai/install/docker
LABEL org.opencontainers.image.source="https://github.com/openclaw/openclaw" \
  org.opencontainers.image.url="https://openclaw.ai" \
  org.opencontainers.image.documentation="https://docs.openclaw.ai/install/docker" \
  org.opencontainers.image.licenses="MIT" \
  org.opencontainers.image.title="OpenClaw" \
  org.opencontainers.image.description="OpenClaw gateway and CLI runtime container image"

WORKDIR /app

# Install system utilities present in bookworm but missing in bookworm-slim.
# On the full bookworm image these are already installed (apt-get is a no-op).
# Smoke workflows can opt out of distro upgrades to cut repeated CI time while
# keeping the default runtime image behavior unchanged.
RUN --mount=type=cache,id=openclaw-bookworm-apt-cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,id=openclaw-bookworm-apt-lists,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    if [ "${OPENCLAW_DOCKER_APT_UPGRADE}" != "0" ]; then \
      DEBIAN_FRONTEND=noninteractive apt-get upgrade -y --no-install-recommends; \
    fi && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      procps hostname curl git lsof openssl

RUN chown node:node /app

COPY --from=runtime-assets --chown=node:node /app/dist ./dist
COPY --from=runtime-assets --chown=node:node /app/node_modules ./node_modules
COPY --from=runtime-assets --chown=node:node /app/package.json .
COPY --from=runtime-assets --chown=node:node /app/openclaw.mjs .
COPY --from=runtime-assets --chown=node:node /app/${OPENCLAW_BUNDLED_PLUGIN_DIR} ./${OPENCLAW_BUNDLED_PLUGIN_DIR}
COPY --from=runtime-assets --chown=node:node /app/skills ./skills
COPY --from=runtime-assets --chown=node:node /app/docs ./docs
COPY --from=runtime-assets --chown=node:node /app/qa ./qa

# Keep pnpm available in the runtime image for container-local workflows.
# Use a shared Corepack home so the non-root `node` user does not need a
# first-run network fetch when invoking pnpm.
ENV COREPACK_HOME=/usr/local/share/corepack
RUN install -d -m 0755 "$COREPACK_HOME" && \
    corepack enable && \
    for attempt in 1 2 3 4 5; do \
      if corepack prepare "$(node -p "require('./package.json').packageManager")" --activate; then \
        break; \
      fi; \
      if [ "$attempt" -eq 5 ]; then \
        exit 1; \
      fi; \
      sleep $((attempt * 2)); \
    done && \
    chmod -R a+rX "$COREPACK_HOME"

# Install additional system packages needed by your skills or extensions.
# Example: docker build --build-arg OPENCLAW_DOCKER_APT_PACKAGES="python3 wget" .
ARG OPENCLAW_DOCKER_APT_PACKAGES=""
RUN --mount=type=cache,id=openclaw-bookworm-apt-cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,id=openclaw-bookworm-apt-lists,target=/var/lib/apt,sharing=locked \
    if [ -n "$OPENCLAW_DOCKER_APT_PACKAGES" ]; then \
      apt-get update && \
      DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends $OPENCLAW_DOCKER_APT_PACKAGES; \
    fi

# Optionally install Chromium and Xvfb for browser automation.
# Build with: docker build --build-arg OPENCLAW_INSTALL_BROWSER=1 ...
# Adds ~300MB but eliminates the 60-90s Playwright install on every container start.
# Must run after node_modules COPY so playwright-core is available.
ARG OPENCLAW_INSTALL_BROWSER=""
RUN --mount=type=cache,id=openclaw-bookworm-apt-cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,id=openclaw-bookworm-apt-lists,target=/var/lib/apt,sharing=locked \
    if [ -n "$OPENCLAW_INSTALL_BROWSER" ]; then \
      apt-get update && \
      DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends xvfb && \
      mkdir -p /home/node/.cache/ms-playwright && \
      PLAYWRIGHT_BROWSERS_PATH=/home/node/.cache/ms-playwright \
      node /app/node_modules/playwright-core/cli.js install --with-deps chromium && \
      chown -R node:node /home/node/.cache/ms-playwright; \
    fi

# Optionally install Docker CLI for sandbox container management.
# Build with: docker build --build-arg OPENCLAW_INSTALL_DOCKER_CLI=1 ...
# Adds ~50MB. Only the CLI is installed — no Docker daemon.
# Required for agents.defaults.sandbox to function in Docker deployments.
ARG OPENCLAW_INSTALL_DOCKER_CLI=""
ARG OPENCLAW_DOCKER_GPG_FINGERPRINT="9DC858229FC7DD38854AE2D88D81803C0EBFCD88"
RUN --mount=type=cache,id=openclaw-bookworm-apt-cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,id=openclaw-bookworm-apt-lists,target=/var/lib/apt,sharing=locked \
    if [ -n "$OPENCLAW_INSTALL_DOCKER_CLI" ]; then \
      apt-get update && \
      DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates curl gnupg && \
      install -m 0755 -d /etc/apt/keyrings && \
      # Verify Docker apt signing key fingerprint before trusting it as a root key.
      # Update OPENCLAW_DOCKER_GPG_FINGERPRINT when Docker rotates release keys.
      curl -fsSL https://download.docker.com/linux/debian/gpg -o /tmp/docker.gpg.asc && \
      expected_fingerprint="$(printf '%s' "$OPENCLAW_DOCKER_GPG_FINGERPRINT" | tr '[:lower:]' '[:upper:]' | tr -d '[:space:]')" && \
      actual_fingerprint="$(gpg --batch --show-keys --with-colons /tmp/docker.gpg.asc | awk -F: '$1 == "fpr" { print toupper($10); exit }')" && \
      if [ -z "$actual_fingerprint" ] || [ "$actual_fingerprint" != "$expected_fingerprint" ]; then \
        echo "ERROR: Docker apt key fingerprint mismatch (expected $expected_fingerprint, got ${actual_fingerprint:-<empty>})" >&2; \
        exit 1; \
      fi && \
      gpg --dearmor -o /etc/apt/keyrings/docker.gpg /tmp/docker.gpg.asc && \
      rm -f /tmp/docker.gpg.asc && \
      chmod a+r /etc/apt/keyrings/docker.gpg && \
      printf 'deb [arch=%s signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bookworm stable\n' \
        "$(dpkg --print-architecture)" > /etc/apt/sources.list.d/docker.list && \
      apt-get update && \
      DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        docker-ce-cli docker-compose-plugin; \
    fi

# Expose the CLI binary without requiring npm global writes as non-root.
RUN ln -sf /app/openclaw.mjs /usr/local/bin/openclaw \
 && chmod 755 /app/openclaw.mjs

ENV NODE_ENV=production

# Security hardening: Run as non-root user
# The node:24-bookworm image includes a 'node' user (uid 1000)
# This reduces the attack surface by preventing container escape via root privileges
USER node

# Start gateway server with default config.
# Binds to loopback (127.0.0.1) by default for security.
#
# IMPORTANT: With Docker bridge networking (-p 18789:18789), loopback bind
# makes the gateway unreachable from the host. Either:
#   - Use --network host, OR
#   - Override --bind to "lan" (0.0.0.0) and set auth credentials
#
# Built-in probe endpoints for container health checks:
#   - GET /healthz (liveness) and GET /readyz (readiness)
#   - aliases: /health and /ready
# For external access from host/ingress, override bind to "lan" and set auth.
HEALTHCHECK --interval=3m --timeout=10s --start-period=15s --retries=3 \
  CMD node -e "fetch('http://127.0.0.1:18789/healthz').then((r)=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"
CMD ["node", "openclaw.mjs", "gateway", "--allow-unconfigured"]
```

### `Makefile`

- Source path: `Makefile`
- Truncated: `no`

```
.PHONY: build

build:
	pnpm build
```

### `README.md`

- Source path: `README.md`
- Truncated: `yes`

```md
# 🦞 OpenClaw — Personal AI Assistant

<p align="center">
    <picture>
        <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-logo-text-dark.svg">
        <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-logo-text.svg" alt="OpenClaw" width="500">
    </picture>
</p>

<p align="center">
  <strong>EXFOLIATE! EXFOLIATE!</strong>
</p>

<p align="center">
  <a href="https://github.com/openclaw/openclaw/actions/workflows/ci.yml?branch=main"><img src="https://img.shields.io/github/actions/workflow/status/openclaw/openclaw/ci.yml?branch=main&style=for-the-badge" alt="CI status"></a>
  <a href="https://github.com/openclaw/openclaw/releases"><img src="https://img.shields.io/github/v/release/openclaw/openclaw?include_prereleases&style=for-the-badge" alt="GitHub release"></a>
  <a href="https://discord.gg/clawd"><img src="https://img.shields.io/discord/1456350064065904867?label=Discord&logo=discord&logoColor=white&color=5865F2&style=for-the-badge" alt="Discord"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
</p>

**OpenClaw** is a _personal AI assistant_ you run on your own devices.
It answers you on the channels you already use (WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, BlueBubbles, IRC, Microsoft Teams, Matrix, Feishu, LINE, Mattermost, Nextcloud Talk, Nostr, Synology Chat, Tlon, Twitch, Zalo, Zalo Personal, WeChat, WebChat). It can speak and listen on macOS/iOS/Android, and can render a live Canvas you control. The Gateway is just the control plane — the product is the assistant.

If you want a personal, single-user assistant that feels local, fast, and always-on, this is it.

[Website](https://openclaw.ai) · [Docs](https://docs.openclaw.ai) · [Vision](VISION.md) · [DeepWiki](https://deepwiki.com/openclaw/openclaw) · [Getting Started](https://docs.openclaw.ai/start/getting-started) · [Updating](https://docs.openclaw.ai/install/updating) · [Showcase](https://docs.openclaw.ai/start/showcase) · [FAQ](https://docs.openclaw.ai/help/faq) · [Onboarding](https://docs.openclaw.ai/start/wizard) · [Nix](https://github.com/openclaw/nix-openclaw) · [Docker](https://docs.openclaw.ai/install/docker) · [Discord](https://discord.gg/clawd)

Preferred setup: run `openclaw onboard` in your terminal.
OpenClaw Onboard guides you step by step through setting up the gateway, workspace, channels, and skills. It is the recommended CLI setup path and works on **macOS, Linux, and Windows (via WSL2; strongly recommended)**.
Works with npm, pnpm, or bun.
New install? Start here: [Getting started](https://docs.openclaw.ai/start/getting-started)

## Sponsors

<table>
  <tr>
    <td align="center" width="16.66%">
      <a href="https://openai.com/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/openai-light.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/openai.svg" alt="OpenAI" height="28">
        </picture>
      </a>
    </td>
    <td align="center" width="16.66%">
      <a href="https://github.com/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/github-light.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/github.svg" alt="GitHub" height="28">
        </picture>
      </a>
    </td>
    <td align="center" width="16.66%">
      <a href="https://www.nvidia.com/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/nvidia.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/nvidia-dark.svg" alt="NVIDIA" height="28">
        </picture>
      </a>
    </td>
    <td align="center" width="16.66%">
      <a href="https://vercel.com/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/vercel-light.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/vercel.svg" alt="Vercel" height="24">
        </picture>
      </a>
    </td>
    <td align="center" width="16.66%">
      <a href="https://blacksmith.sh/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/blacksmith-light.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/blacksmith.svg" alt="Blacksmith" height="28">
        </picture>
      </a>
    </td>
    <td align="center" width="16.66%">
      <a href="https://www.convex.dev/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/convex-light.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/convex.svg" alt="Convex" height="24">
        </picture>
      </a>
    </td>
  </tr>
</table>

**Subscriptions (OAuth):**

- **[OpenAI](https://openai.com/)** (ChatGPT/Codex)

Model note: while many providers and models are supported, prefer a current flagship model from the provider you trust and already use. See [Onboarding](https://docs.openclaw.ai/start/onboarding).

## Models (selection + auth)

- Models config + CLI: [Models](https://docs.openclaw.ai/concepts/models)
- Auth profile rotation (OAuth vs API keys) + fallbacks: [Model failover](https://docs.openclaw.ai/concepts/model-failover)

## Install (recommended)

Runtime: **Node 24 (recommended) or Node 22.16+**.

```bash
npm install -g openclaw@latest
# or: pnpm add -g openclaw@latest

openclaw onboard --install-daemon
```

OpenClaw Onboard installs the Gateway daemon (launchd/systemd user service) so it stays running.

## Quick start (TL;DR)

Runtime: **Node 24 (recommended) or Node 22.16+**.

Full beginner guide (auth, pairing, channels): [Getting started](https://docs.openclaw.ai/start/getting-started)

```bash
openclaw onboard --install-daemon

openclaw gateway --port 18789 --verbose

# Send a message
openclaw message send --to +1234567890 --message "Hello from OpenClaw"

# Talk to the assistant (optionally deliver back to any connected channel: WhatsApp/Telegram/Slack/Discord/Google Chat/Signal/iMessage/BlueBubbles/IRC/Microsoft Teams/Matrix/Feishu/LINE/Mattermost/Nextcloud Talk/Nostr/Synology Chat/Tlon/Twitch/Zalo/Zalo Personal/WeChat/WebChat)
openclaw agent --message "Ship checklist" --thinking high
```

Upgrading? [Updating guide](https://docs.openclaw.ai/install/updating) (and run `openclaw doctor`).

## Development channels

- **stable**: tagged releases (`vYYYY.M.D` or `vYYYY.M.D-<patch>`), npm dist-tag `latest`.
- **beta**: prerelease tags (`vYYYY.M.D-beta.N`), npm dist-tag `beta` (macOS app may be missing).
- **dev**: moving head of `main`, npm dist-tag `dev` (when published).

Switch channels (git + npm): `openclaw update --channel stable|beta|dev`.
Details: [Development channels](https://docs.openclaw.ai/install/development-channels).

## From source (development)

Prefer `pnpm` for builds from source. Bun is optional for running TypeScript directly.

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw

pnpm install
pnpm ui:build # auto-installs UI deps on first run
pnpm build

pnpm openclaw onboard --install-daemon

# Dev loop (auto-reload on source/config changes)
pnpm gateway:watch
```

Note: `pnpm openclaw ...` runs TypeScript directly (via `tsx`). `pnpm build` produces `dist/` for running via Node / the packaged `openclaw` binary.

## Security defaults (DM access)

OpenClaw connects to real messaging surfaces. Treat inbound DMs as **untrusted input**.

Full security guide: [Security](https://docs.openclaw.ai/gateway/security)

Default behavior on Telegram/WhatsApp/Signal/iMessage/Microsoft Teams/Discord/Google Chat/Slack:

- **DM pairing** (`dmPolicy="pairing"` / `channels.discord.dmPolicy="pairing"` / `channels.slack.dmPolicy="pairing"`; legacy: `channels.discord.dm.policy`, `channels.slack.dm.policy`): unknown senders receive a short pairing code and the bot does not process their message.
- Approve with: `openclaw pairing approve <channel> <code>` (then the sender is added to a local allowlist store).
- Public inbound DMs require an explicit opt-in: set `dmPolicy="open"` and include `"*"` in the channel allowlist (`allowFrom` / `channels.discord.allowFrom` / `channels.slack.allowFrom`; legacy: `channels.discord.dm.allowFrom`, `channels.slack.dm.allowFrom`).

Run `openclaw doctor` to surface risky/misconfigured DM policies.

## Highlights

- **[Local-first Gateway](https://docs.openclaw.ai/gateway)** — single control plane for sessions, channels, tools, and events.
- **[Multi-channel inbox](https://docs.openclaw.ai/channels)** — WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, BlueBubbles (iMessage), iMessage (legacy), IRC, Microsoft Teams, Matrix, Feishu, LINE, Mattermost, Nextcloud Talk, Nostr, Synology Chat, Tlon, Twitch, Zalo, Zalo Personal, WeChat, WebChat, macOS, iOS/Android.
- **[Multi-agent routing](https://docs.openclaw.ai/gateway/configuration)** — route inbound channels/accounts/peers to isolated agents (workspaces + per-agent sessions).
- **[Voice Wake](https://docs.openclaw.ai/nodes/voicewake) + [Talk Mode](https://docs.openclaw.ai/nodes/talk)** — wake words on macOS/iOS and continuous voice on Android (ElevenLabs + system TTS fallback).
- **[Live Canvas](https://docs.openclaw.ai/platforms/mac/canvas)** — agent-driven visual workspace with [A2UI](https://docs.openclaw.ai/platforms/mac/canvas#canvas-a2ui).
- **[First-class tools](https://docs.openclaw.ai/tools)** — browser, canvas, nodes, cron, sessions, and Discord/Slack actions.
- **[Companion apps](https://docs.openclaw.ai/platforms/macos)** — macOS menu bar app + iOS/Android [nodes](https://docs.openclaw.ai/nodes).
- **[Onboarding](https://docs.openclaw.ai/start/wizard) + [skills](https://docs.openclaw.ai/tools/skills)** — onboarding-driven setup with bundled/managed/workspace skills.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=openclaw/openclaw&type=date&legend=top-left)](https://www.star-history.com/#openclaw/openclaw&type=date&legend=top-left)

## Everything we built so far

### Core platform

- [Gateway WS control plane](https://docs.openclaw.ai/gateway) with sessions, presence, config, cron, webhooks, [Control UI](https://docs.openclaw.ai/web), and [Canvas host](https://docs.openclaw.ai/platforms/mac/canvas#canvas-a2ui).
- [CLI surface](https://docs.openclaw.ai/tools/agent-send): gateway, agent, send, [onboarding](https://docs.openclaw.ai/start/wizard), and [doctor](https://docs.openclaw.ai/gateway/doctor).
- [Pi agent runtime](https://docs.openclaw.ai/concepts/agent) in RPC mode with tool streaming and block streaming.
- [Session model](https://docs.openclaw.ai/concepts/session): `main` for direct chats, group isolation, activation modes, queue modes, reply-back. Group rules: [Groups](https://docs.openclaw.ai/channels/groups).
- [Media pipeline](https://docs.openclaw.ai/nodes/images): images/audio/video, transcription hooks, size caps, temp file lifecycle. Audio details: [Audio](https://docs.openclaw.ai/nodes/audio).

### Channels

- [Channels](https://docs.openclaw.ai/channels): [WhatsApp](https://docs.openclaw.ai/channels/whatsapp) (Baileys), [Telegram](https://docs.openclaw.ai/channels/telegram) (grammY), [Slack](https://docs.openclaw.ai/channels/slack) (Bolt), [Discord](https://docs.openclaw.ai/channels/discord) (discord.js), [Google Chat](https://docs.openclaw.ai/channels/googlechat) (Chat API), [Signal](https://docs.openclaw.ai/channels/signal) (signal-cli), [BlueBubbles](https://docs.openclaw.ai/channels/bluebubbles) (iMessage, recommended), [iMessage](https://docs.openclaw.ai/channels/imessage) (legacy imsg), [IRC](https://docs.openclaw.ai/channels/irc), [Microsoft Teams](https://docs.openclaw.ai/channels/msteams), [Matrix](https://docs.openclaw.ai/channels/matrix), [Feishu](https://docs.openclaw.ai/channels/feishu), [LINE](https://docs.openclaw.ai/channels/line), [Mattermost](https://docs.openclaw.ai/channels/mattermost), [Nextcloud Talk](https://docs.openclaw.ai/channels/nextcloud-talk), [Nostr](https://docs.openclaw.ai/channels/nostr), [Synology Chat](https://docs.openclaw.ai/channels/synology-chat), [Tlon](https://docs.openclaw.ai/channels/tlon), [Twitch](https://docs.openclaw.ai/channels/twitch), [Zalo](https://docs.openclaw.ai/channels/zalo), [Zalo Personal](https://docs.openclaw.ai/channels/zalouser), WeChat (`@tencent-weixin/openclaw-weixin`), [WebChat](https://docs.openclaw.ai/web/webchat).
- [Group routing](https://docs.openclaw.ai/channels/group-messages): mention gating, reply tags, per-channel chunking and routing. Channel rules: [Channels](https://docs.openclaw.ai/channels).

### Apps + nodes

- [macOS app](https://docs.openclaw.ai/platforms/macos): menu bar control plane, [Voice Wake](https://docs.openclaw.ai/nodes/voicewake)/PTT, [Talk Mode](https://docs.openclaw.ai/nodes/talk) overlay, [WebChat](https://docs.openclaw.ai/web/webchat), debug tools, [remote gateway](https://docs.openclaw.ai/gateway/remote) control.
- [iOS node](https://docs.openclaw.ai/platforms/ios): [Canvas](https://docs.openclaw.ai/platforms/mac/canvas), [Voice Wake](https://docs.openclaw.ai/nodes/voicewake), [Talk Mode](https://docs.openclaw.ai/nodes/talk), camera, screen recording, Bonjour + device pairing.
- [Android node](https://docs.openclaw.ai/platforms/android): Connect tab (setup code/manual), chat sessions, voice tab, [Canvas](https://docs.openclaw.ai/platforms/mac/canvas), camera/screen recording, and Android device commands (notifications/location/SMS/photos/contacts/calendar/motion/app update).
- [macOS node mode](https://docs.openclaw.ai/nodes): system.run/notify + canvas/camera exposure.

### Tools + automation

- [Browser control](https://docs.openclaw.ai/tools/browser): dedicated openclaw Chrome/Chromium, snapshots, actions, uploads, profiles.
- [Canvas](https://docs.openclaw.ai/platforms/mac/canvas): [A2UI](https://docs.openclaw.ai/platforms/mac/canvas#canvas-a2ui) push/reset, eval, snapshot.
- [Nodes](https://docs.openclaw.ai/nodes): camera snap/clip, screen record, [location.get](https://docs.openclaw.ai/nodes/location-command), notifications.
- [Cron + wakeups](https://docs.openclaw.ai/automation/cron-jobs); [webhooks](https://docs.openclaw.ai/automation/webhook); [Gmail Pub/Sub](https://docs.openclaw.ai/automation/gmail-pubsub).
- [Skills platform](https://docs.openclaw.ai/tools/skills): bundled, managed, and workspace skills with install gating + UI.

### Runtime + safety

- [Channel routing](https://docs.openclaw.ai/channels/channel-routing), [retry policy](https://docs.openclaw.ai/concepts/retry), and [streaming/chunking](https://docs.openclaw.ai/concepts/streaming).
- [Presence](https://docs.openclaw.ai/concepts/presence), [typing indicators](https://docs.openclaw.ai/concepts/typing-indicators), and [usage tracking](https://docs.openclaw.ai/concepts/usage-tracking).
- [Models](https://docs.openclaw.ai/concepts/models), [model failover](https://docs.openclaw.ai/concepts/model-failover), and [session pruning](https://docs.openclaw.ai/concepts/session-pruning).
- [Security](https://docs.openclaw.ai/gateway/security) and [troubleshooting](https://docs.openclaw.ai/channels/troubleshooting).

### Ops + packaging

- [Control UI](https://docs.openclaw.ai/web) + [WebChat](https://docs.openclaw.ai/web/webchat) served directly from the Gateway.
- [Tailscale Serve/Funnel](https://docs.openclaw.ai/gateway/tailscale) or [SSH tunnels](https://docs.openclaw.ai/gateway/remote) with token/password auth.
- [Nix mode](https://docs.openclaw.ai/install/nix) for declarative config; [Docker](https://docs.openclaw.ai/install/docker)-based installs.
- [Doctor](https://docs.openclaw.ai/gateway/doctor) migrations, [logging](https://docs.openclaw.ai/logging).

## How it works (short)

```
WhatsApp / Telegram / Slack / Discord / Google Chat / Signal / iMessage / BlueBubbles / IRC / Microsoft Teams / Matrix / Feishu / LINE / Mattermost / Nextcloud Talk / Nostr / Synology Chat / Tlon / Twitch / Zalo / Zalo Personal / WeChat / WebChat
               │
               ▼
┌───────────────────────────────┐
│            Gateway            │
│       (control plane)         │
│     ws://127.0.0.1:18789      │
└──────────────┬────────────────┘
               │
               ├─ Pi agent (RPC)
               ├─ CLI (openclaw …)
               ├─ WebChat UI
               ├─ macOS app
               └─ iOS / Android nodes
```

## Key subsystems

- **[Gateway WebSocket network](https://docs.openclaw.ai/concepts/architecture)** — single WS control plane for clients, tools, and events (plus ops: [Gateway runbook](https://docs.openclaw.ai/gateway)).
- **[Tailscale exposure](https://docs.openclaw.ai/gateway/tailscale)** — Serve/Funnel for the Gateway dashboard + WS (remote access: [Remote](https://docs.openclaw.ai/gateway/remote)).
- **[Browser control](https://docs.openclaw.ai/tools/browser)** — openclaw‑managed Chrome/Chromium with CDP control.
- **[Canvas + A2UI](https://docs.openclaw.ai/platforms/mac/canvas)** — agent‑driven visual workspace (A2UI host: [Canvas/A2UI](https://docs.openclaw.ai/platforms/mac/canvas#canvas-a2ui)).
- **[Voice Wake](https://docs.openclaw.ai/nodes/voicewake) + [Talk Mode](https://docs.openclaw.ai/nodes/talk)** — wake words on macOS/iOS plus continuous voice on Android.
- **[Nodes](https://docs.openclaw.ai/nodes)** — Canvas, camera snap/clip, screen record, `location.get`, notifications, plus macOS‑only `system.run`/`system.notify`.

## Tailscale access (Gateway dashboard)

OpenClaw can auto-configure Tailscale **Serve** (tailnet-only) or **Funnel** (public) while the Gateway stays bound to loopback. Configure `gateway.tailscale.mode`:

- `off`: no Tailscale automation (default).
- `serve`: tailnet-only HTTPS via `tailscale serve` (uses Tailscale identity headers by default).
- `funnel`: public HTTPS via `tailscale funnel` (requires shared password auth).

Notes:

- `gateway.bind` must stay `loopback` when Serve/Funnel is enabled (OpenClaw enforces this).
- Serve can be forced to require a password by setting `gateway.auth.mode: "password"` or `gateway.auth.allowTailscale: false`.
- Funnel refuses to start unless `gateway.auth.mode: "password"` is set.
- Optional: `gateway.tailscale.resetOnExit` to undo Serve/Funnel on shutdown.

Details: [Tailscale guide](https://docs.openclaw.ai/gateway/tailscale) · [Web surfaces](https://docs.openclaw.ai/web)

## Remote Gateway (Linux is great)

It’s perfectly fine to run the Gateway on a small Linux instance. Clients (macOS app, CLI, WebChat) can connect over **Tailscale Serve/Funnel** or **SSH tunnels**, and you can still pair device nodes (macOS/iOS/Android) to execute device‑local actions when needed.

- **Gateway host** runs the exec tool and channel connections by default.
- **Device nodes** run device‑local actions (`system.run`, camera, screen recording, notifications) via `node.invoke`.
  In short: exec runs where the Gateway lives; device actions run where the device lives.

Details: [Remote access](https://docs.openclaw.ai/gateway/remote) · [Nodes](https://docs.openclaw.ai/nodes) · [Security](https://docs.openclaw.ai/gateway/security)

## macOS permissions via the Gateway protocol

The macOS app can run in **node mode** and advertises its capabilities + permission map over the Gateway WebSocket (`node.list` / `node.describe`). Clients can then execute local actions via `node.invoke`:

- `system.run` runs a local command and returns stdout/stderr/exit code; set `needsScreenRecording: true` to require screen-recording permission (otherwise you’ll get `PERMISSION_MISSING`).
- `system.notify` posts a user notification and fails if notifications are denied.
- `canvas.*`, `camera.*`, `screen.record`, and `location.get` are also routed via `node.invoke` and follow TCC permission status.

Elevated bash (host permissions) is separate from macOS TCC:

- Use `/elevated on|off` to toggle per‑session elevated access when enabled + allowlisted.
- Gateway persists the per‑session toggle via `sessions.patch` (WS method) alongside `thinkingLevel`, `verboseLevel`, `model`, `sendPolicy`, and `groupActivation`.

Details: [Nodes](https://docs.openclaw.ai/nodes) · [macOS app](https://docs.openclaw.ai/platforms/macos) · [Gateway protocol](https://docs.openclaw.ai/concepts/architecture)

## Agent to Agent (sessions\_\* tools)

- Use these to coordinate work across sessions without jumping between chat surfaces.
- `sessions_list` — discover active sessions (agents) and their metadata.
- `sessions_history` — fetch transcript logs for a session.
- `sessions_send` — message another session; optional reply‑back ping‑pong + announce step (`REPLY_SKIP`, `ANNOUNCE_SKIP`).

Details: [Session tools](https://docs.openclaw.ai/concepts/session-tool)

## Skills registry (ClawHub)

ClawHub is a minimal skill registry. With ClawHub enabled, the agent can search for skills automatically and pull in new ones as needed.

[ClawHub](https://clawhub.com)

## Chat commands

Send these in WhatsApp/Telegram/Slack/Google Chat/Microsoft Teams/WebChat (group commands are owner-only):

- `/status` — compact session status (model + tokens, cost when available)
- `/new` or `/reset` — reset the session
- `/compact` — compact session context (summary)
- `/think <level>` — off|minimal|low|medium|high|xhigh (GPT-5.2 + Codex models only)
- `/verbose on|off`
- `/usage off|tokens|full` — per-response usage footer
- `/restart` — restart the gateway (owner-only in groups)
- `/activation mention|always` — group activation toggle (groups only)

## Apps (optional)

The Gateway alone delivers a great experience. All apps are optional and add extra features.

If you plan to build/run companion apps, follow the platform runbooks below.

### macOS (OpenClaw.app) (optional)

- Menu bar control for the Gateway and health.
- Voice Wake + push-to-talk overlay.
- WebChat + debug tools.
- Remote gateway control over SSH.

Note: signed builds required for macOS permissions to stick across rebuilds (see [macOS Permissions](https://docs.openclaw.ai/platforms/mac/permissions)).

### iOS node (optional)

- Pairs as a node over the Gateway WebSocket (device pairing).
- Voice trigger forwarding + Canvas surface.
- Controlled via `openclaw nodes …`.

Runbook: [iOS connect](https://docs.openclaw.ai/platforms/ios).

### Android node (optional)

- Pairs as a WS node via device pairing (`openclaw devices ...`).
- Exposes Connect/Chat/Voice tabs plus Canvas, Camera, Screen capture, and Android device command families.
- Runbook: [Android connect](https://docs.openclaw.ai/platforms/android).

## Agent workspace + skills

- Workspace root: `~/.openclaw/workspace` (configurable via `agents.defaults.workspace`).
- Injected prompt files: `AGENTS.md`, `SOUL.md`, `TOOLS.md`.
- Skills: `~/.openclaw/workspace/skills/<skill>/SKILL.md`.

## Configuration

Minimal `~/.openclaw/openclaw.json` (model + defaults):

```json5
{
  agent: {
    model: "<provider>/<model-id>",
  },
}
```

[Full configuration reference (all keys + examples).](https://docs.openclaw.ai/gateway/configuration)

## Security model (important)

- **Default:** tools run on the host for the **main** session, so the agent has full access when it’s just you.
- **Group/channel safety:** set `agents.defaults.sandbox.mode: "non-main"` to run **non‑main sessions** (groups/channels) inside per‑session Docker sandboxes; bash then runs in Docker for those sessions.
- **Sandbox defaults:** allowlist `bash`, `process`, `read`, `write`, `edit`, `sessions_list`, `sessions_history`, `sessions_send`, `sessions_spawn`; denylist `browser`, `canvas`, `nodes`, `cron`, `discord`, `gateway`.

Details: [Security guide](https://docs.openclaw.ai/gateway/security) · [Docker + sandboxing](https://docs.openclaw.ai/install/docker) · [Sandbox config](https://docs.openclaw.ai/gateway/configuration)

### [WhatsApp](https://docs.openclaw.ai/channels/whatsapp)

- Link the device: `pnpm openclaw channels login` (stores creds in `~/.openclaw/credentials`).
- Allowlist who can talk to the assistant via `channels.whatsapp.allowFrom`.
- If `channels.whatsapp.groups` is set, it becomes a group allowlist; include `"*"` to allow all.

### [Telegram](https://docs.openclaw.ai/channels/telegram)

- Set `TELEGRAM_BOT_TOKEN` or `channels.telegram.botToken` (env wins).
- Optional: set `channels.telegram.groups` (with `channels.telegram.groups."*".requireMention`); when set, it is a group allowlist (include `"*"` to allow all). Also `channels.telegram.allowFrom` or `channels.telegram.webhookUrl` + `channels.telegram.webhookSecret` as needed.

```json5
{
  channels: {
    telegram: {
      botToken: "123456:ABCDEF",
    },
  },
}
```

### [Slack](https://docs.openclaw.ai/channels/slack)

- Set `SLACK_BOT_TOKEN` + `SLACK_APP_TOKEN` (or `channels.slack.botToken` + `channels.slack.appToken`).

### [Discord](https://docs.openclaw.ai/channels/discord)

- Set `DISCORD_BOT_TOKEN` or `channels.discord.token`.
- Optional: set `commands.native`, `commands.text`, or `commands.useAccessGroups`, plus `channels.discord.allowFrom`, `channels.discord.guilds`, or `channels.discord.mediaMaxMb` as needed.

```json5
{
  channels: {
    discord: {
      token: "1234abcd",
    },
  },
}
```

### [Signal](https://docs.openclaw.ai/channels/signal)

- Requires `signal-cli` and a `channels.signal` config section.

### [BlueBubbles (iMessage)](https://docs.openclaw.ai/channels/bluebubbles)

- **Recommended** iMessage integration.
- Configure `channels.bluebubbles.serverUrl` + `channels.bluebubbles.password` and a webhook (`channels.bluebubbles.webhookPath`).
- The BlueBubbles server runs on macOS; the Gateway can run on macOS or elsewhere.

### [iMessage (legacy)](https://docs.openclaw.ai/channels/imessage)

- Legacy macOS-only integration via `imsg` (Messages must be signed in).
- If `channels.imessage.groups` is set, it becomes a group allowlist; include `"*"` to allow all.

### [Microsoft Teams](https://docs.openclaw.ai/channels/msteams)

- Configure a Teams app + Bot Framework, then add a `msteams` config section.
- Allowlist who can talk via `msteams.allowFrom`; group access via `msteams.groupAllowFrom` or `msteams.groupPolicy: "open"`.

### WeChat

- Official Tencent plugin via [`@tencent-weixin/openclaw-weixin`](https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin) (iLink Bot API). Private chats only; v2.x requires OpenClaw `>=2026.3.22`.
- Install: `openclaw plugins install "@tencent-weixin/openclaw-weixin"`, then `openclaw channels login --channel openclaw-weixin` to scan the QR code.
- Requires the WeChat ClawBot plugin (WeChat > Me > Settings > Plugins); gradual rollout by Tencent.

### [WebChat](https://docs.openclaw.ai/web/webchat)

- Uses the Gateway WebSocket; no separate WebChat port/config.

Browser control (optional):

```json5
{
  browser: {
    enabled: true,
    color: "#FF4500",
  },
}
```

## Docs

Use these when you’re past the onboarding flow and want the deeper reference.

- [Start with the docs index for navigation and “what’s where.”](https://docs.openclaw.ai)
- [Read the architecture overview for the gateway + protocol model.](https://docs.openclaw.ai/concepts/architecture)
- [Use the full configuration reference when you need every key and example.](https://docs.openclaw.ai/gateway/configuration)
- [Run the Gateway by the book with the operational runbook.](https://docs.openclaw.ai/gateway)
- [Learn how the Control UI/Web surfaces work and how to expose them safely.](https://docs.openclaw.ai/web)
- [Understand remote access over SSH tunnels or tailnets.](https://docs.openclaw.ai/gateway/remote)
- [Follow OpenClaw Onboard for a guided setup.](https://docs.openclaw.ai/start/wizard)
- [Wire external triggers via the webhook surface.](https://docs.openclaw.ai/automation/webhook)
- [Set up Gmail Pub/Sub triggers.](https://docs.openclaw.ai/automation/gmail-pubsub)
- [Learn the macOS menu bar companion details.](https://docs.openclaw.ai/platforms/mac/menu-bar)
- [Platform guides: Windows (WSL2)](https://docs.openclaw.ai/platforms/windows), [Linux](https://docs.openclaw.ai/platforms/linux), [macOS](https://docs.openclaw.ai/platforms/macos), [iOS](https://docs.openclaw.ai/platforms/ios), [Android](https://docs.openclaw.ai/platforms/android)
- [Debug common failures with the troubleshooting guide.](https://docs.openclaw.ai/channels/troubleshooting)
- [Review security guidance before exposing anything.](https://docs.openclaw.ai/gateway/security)

## Advanced docs (discovery + control)

- [Discovery + transports](https://docs.openclaw.ai/gateway/discovery)
- [Bonjour/mDNS](https://docs.openclaw.ai/gateway/bonjour)
- [Gateway pairing](https://docs.openclaw.ai/gateway/pairing)
- [Remote gateway README](https://docs.openclaw.ai/gateway/remote-gateway-readme)
- [Control UI](https://docs.openclaw.ai/web/control-ui)
- [Dashboard](https://docs.openclaw.ai/web/dashboard)

## Operations & troubleshooting

- [Health checks](https://docs.openclaw.ai/gateway/health)
- [Gateway lock](https://docs.openclaw.ai/gateway/gateway-lock)
- [Background process](https://docs.openclaw.ai/gateway/background-process)
- [Browser troubleshooting (Linux)](https://docs.openclaw.ai/tools/browser-linux-troubleshooting)
- [Logging](https://docs.openclaw.ai/logging)

## Deep dives

- [Agent loop](https://docs.openclaw.ai/concepts/agent-loop)
- [Presence](https://docs.openclaw.ai/concepts/presence)
- [TypeBox schemas](https://docs.openclaw.ai/concepts/typebox)
- [RPC adapters](https://docs.openclaw.ai/reference/rpc)
- [Queue](https://docs.openclaw.ai/concepts/queue)

## Workspace & skills

- [Skills config](https://docs.openclaw.ai/tools/skills-config)
- [Default AGENTS](https://docs.openclaw.ai/reference/AGENTS.default)
- [Templates: AGENTS](https://docs.openclaw.ai/reference/templates/AGENTS)
- [Templates: BOOTSTRAP](https://docs.openclaw.ai/reference/templates/BOOTSTRAP)
- [Templates: IDENTITY](https://docs.openclaw.ai/reference/templates/IDENTITY)
- [Templates: SOUL](https://docs.openclaw.ai/reference/templates/SOUL)
- [Templates: TOOLS](https://docs.openclaw.ai/reference/templates/TOOLS)
- [Templates: USER](https://docs.openclaw.ai/reference/templates/USER)

## Platform internals

- [macOS dev setup](https://docs.openclaw.ai/platforms/mac/dev-setup)
- [macOS menu bar](https://docs.openclaw.ai/platforms/mac/menu-bar)
- [macOS voice wake](https://docs.openclaw.ai/platforms/mac/voicewake)
- [iOS node](https://docs.openclaw.ai/platforms/ios)
- [Android node](https://docs.openclaw.ai/platforms/android)
- [Windows (WSL2)](https://docs.openclaw.ai/platforms/windows)
- [Linux app](https://docs.openclaw.ai/platforms/linux)

## Email hooks (Gmail)

- [docs.openclaw.ai/gmail-pubsub](https://docs.openclaw.ai/automation/gmail-pubsub)

## Molty

OpenClaw was built for **Molty**, a space lobster AI assistant. 🦞
by Peter Steinberger and the community.

- [openclaw.ai](https://openclaw.ai)
- [soul.md](https://soul.md)
- [steipete.me](https://steipete.me)
- [@openclaw](https://x.com/openclaw)

## Community

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, maintainers, and how to submit PRs.
AI/vibe-coded PRs welcome! 🤖

Special thanks to [Mario Zechner](https://mariozechner.at/) for his support and for
[pi-mono](https://github.com/badlogic/pi-mono).
Special thanks to Adam Doppelt for lobster.bot.

Thanks to all clawtributors:

<p align="left">
  <a href="https://github.com/steipete"><img src="https://avatars.githubusercontent.com/u/58493?v=4&s=48" width="48" height="48" alt="steipete" title="steipete"/></a> <a href="https://github.com/vincentkoc"><img src="https://avatars.githubusercontent.com/u/25068?v=4&s=48" width="48" height="48" alt="vincentkoc" title="vincentkoc"/></a> <a href="https://github.com/vignesh07"><img src="https://avatars.githubusercontent.com/u/1436853?v=4&s=48" width="48" height="48" alt="vignesh07" title="vignesh07"/></a> <a href="https://github.com/obviyus"><img src="https://avatars.githubusercontent.com/u/22031114?v=4&s=48" width="48" height="48" alt="obviyus" title="obviyus"/></a> <a href="https://github.com/mbelinky"><img src="https://avatars.githubusercontent.com/u/132747814?v=4&s=48" width="48" height="48" alt="Mariano Belinky" title="Mariano Belinky"/></a> <a href="https://github.com/sebslight"><img src="https://avatars.githubusercontent.com/u/19554889?v=4&s=48" width="48" height="48" alt="sebslight" title="sebslight"/></a> <a href="https://github.com/gumadeiras"><img src="https://avatars.githubusercontent.com/u/5599352?v=4&s=48" width="48" height="48" alt="gumadeiras" title="gumadeiras"/></a> <a href="https://github.com/Takhoffman"><img src="https://avatars.githubusercontent.com/u/781889?v=4&s=48" width="48" height="48" alt="Takhoffman" title="Takhoffman"/></a> <a href="https://github.com/thewilloftheshadow"><img src="https://avatars.githubusercontent.com/u/35580099?v=4&s=48" width="48" height="48" alt="thewilloftheshadow" title="thewilloftheshadow"/></a> <a href="https://github.com/cpojer"><img src="https://avatars.githubusercontent.com/u/13352?v=4&s=48" width="48" height="48" alt="cpojer" title="cpojer"/></a>
  <a href="https://github.com/tyler6204"><img src="https://avatars.githubusercontent.com/u/64381258?v=4&s=48" width="48" height="48" alt="tyler6204" title="tyler6204"/></a> <a href="https://github.com/joshp123"><img src="https://avatars.githubusercontent.com/u/1497361?v=4&s=48" width="48" height="48" alt="joshp123" title="joshp123"/></a> <a href="https://github.com/Glucksberg"><img src="https://avatars.githubusercontent.com/u/80581902?v=4&s=48" width="48" height="48" alt="Glucksberg" title="Glucksberg"/></a> <a href="https://github.com/mcaxtr"><img src="https://avatars.githubusercontent.com/u/7562095?v=4&s=48" width="48" height="48" alt="mcaxtr" title="mcaxtr"/></a> <a href="https://github.com/quotentiroler"><img src="https://avatars.githubusercontent.com/u/40643627?v=4&s=48" width="48" height="48" alt="quotentiroler" title="quotentiroler"/></a> <a href="https://github.com/osolmaz"><img src="https://avatars.githubusercontent.com/u/2453968?v=4&s=48" width="48" height="48" alt="osolmaz" title="osolmaz"/></a> <a href="https://github.com/Sid-Qin"><img src="https://avatars.githubusercontent.com/u/201593046?v=4&s=48" width="48" height="48" alt="Sid-Qin" title="Sid-Qin"/></a> <a href="https://github.com/joshavant"><img src="https://avatars.githubusercontent.com/u/830519?v=4&s=48" width="48" height="48" alt="joshavant" title="joshavant"/></a> <a href="https://github.com/shakkernerd"><img src="https://avatars.githubusercontent.com/u/165377636?v=4&s=48" width="48" height="48" alt="shakkernerd" title="shakkernerd"/></a> <a href="https://github.com/bmendonca3"><img src="https://avatars.githubusercontent.com/u/208517100?v=4&s=48" width="48" height="48" alt="bmendonca3" title="bmendonca3"/></a>
  <a href="https://github.com/mukhtharcm"><img src="https://avatars.githubusercontent.com/u/56378562?v=4&s=48" width="48" height="48" alt="mukhtharcm" title="mukhtharcm"/></a> <a href="https://github.com/zerone0x"><img src="https://avatars.githubusercontent.com/u/39543393?v=4&s=48" width="48" height="48" alt="zerone0x" title="zerone0x"/></a> <a href="https://github.com/mcinteerj"><img src="https://avatars.githubusercontent.com/u/3613653?v=4&s=48" width="48" height="48" alt="mcinteerj" title="mcinteerj"/></a> <a href="https://github.com/ngutman"><img src="https://avatars.githubusercontent.com/u/1540134?v=4&s=48" width="48" height="48" alt="ngutman" title="ngutman"/></a> <a href="https://github.com/lailoo"><img src="https://avatars.githubusercontent.com/u/20536249?v=4&s=48" width="48" height="48" alt="lailoo" title="lailoo"/></a> <a href="https://github.com/arosstale"><img src="https://avatars.githubusercontent.com/u/117890364?v=4&s=48" width="48" height="48" alt="arosstale" title="arosstale"/></a> <a href="https://github.com/rodrigouroz"><img src="https://avatars.githubusercontent.com/u/384037?v=4&s=48" width="48" height="48" alt="rodrigouroz" title="rodrigouroz"/></a> <a href="https://github.com/robbyczgw-cla"><img src="https://avatars.githubusercontent.com/u/239660374?v=4&s=48" width="48" height="48" alt="robbyczgw-cla" title="robbyczgw-cla"/></a> <a href="https://github.com/0xRaini"><img src="https://avatars.githubusercontent.com/u/190923101?v=4&s=48" width="48" height="48" alt="Elonito" title="Elonito"/></a> <a href="https://github.com/Clawborn"><img src="https://avatars.githubusercontent.com/u/261310391?v=4&s=48" width="48" height="48" alt="Clawborn" title="Clawborn"/></a>
  <a href="https://github.com/yinghaosang"><img src="https://avatars.githubusercontent.com/u/261132136?v=4&s=48" width="48" height="48" alt="yinghaosang" title="yinghaosang"/></a> <a href="https://github.com/BunsDev"><img src="https://avatars.githubusercontent.com/u/68980965?v=4&s=48" width="48" height="48" alt="BunsDev" title="BunsDev"/></a> <a href="https://github.com/christianklotz"><img src="https://avatars.githubusercontent.com/u/69443?v=4&s=48" width="48" height="48" alt="christianklotz" title="christianklotz"/></a> <a href="https://github.com/echoVic"><img src="https://avatars.githubusercontent.com/u/16428813?v=4&s=48" width="48" height="48" alt="echoVic" title="echoVic"/></a> <a href="https://github.com/coygeek"><img src="https://avatars.githubusercontent.com/u/65363919?v=4&s=48" width="48" height="48" alt="coygeek" title="coygeek"/></a> <a href="https://github.com/roshanasingh4"><img src="https://avatars.githubusercontent.com/u/88576930?v=4&s=48" width="48" height="48" alt="roshanasingh4" title="roshanasingh4"/></a> <a href="https://github.com/mneves75"><img src="https://avatars.githubusercontent.com/u/2423436?v=4&s=48" width="48" height="48" alt="mneves75" title="mneves75"/></a> <a href="https://github.com/joaohlisboa"><img src="https://avatars.githubusercontent.com/u/8200873?v=4&s=48" width="48" height="48" alt="joaohlisboa" title="joaohlisboa"/></a> <a href="https://github.com/bohdanpodvirnyi"><img src="https://avatars.githubusercontent.com/u/31819391?v=4&s=48" width="48" height="48" alt="bohdanpodvirnyi" title="bohdanpodvirnyi"/></a> <a href="https://github.com/Nachx639"><img src="https://avatars.githubusercontent.com/u/71144023?v=4&s=48" width="48" height="48" alt="nachx639" title="nachx639"/></a>
  <a href="https://github.com/onutc"><img src="https://avatars.githubusercontent.com/u/152018508?v=4&s=48" width="48" height="48" alt="onutc" title="onutc"/></a> <a href="https://github.com/VeriteIgiraneza"><img src="https://avatars.githubusercontent.com/u/69280208?v=4&s=48" width="48" height="48" alt="Verite Igiraneza" title="Verite Igiraneza"/></a> <a href="https://github.com/widingmarcus-cyber"><img src="https://avatars.githubusercontent.com/u/245375637?v=4&s=48" width="48" height="48" alt="widingmarcus-cyber" title="widingmarcus-cyber"/></a> <a href="https://github.com/akramcodez"><img src="https://avatars.githubusercontent.com/u/179671552?v=4&s=48" width="48" height="48" alt="akramcodez" title="akramcodez"/></a> <a href="https://github.com/aether-ai-agent"><img src="https://avatars.githubusercontent.com/u/261339948?v=4&s=48" width="48" height="48" alt="aether-ai-agent" title="aether-ai-agent"/></a> <a href="https://github.com/bjesuiter"><img src="https://avatars.githubusercontent.com/u/2365676?v=4&s=48" width="48" height="48" alt="bjesuiter" title="bjesuiter"/></a> <a href="https://github.com/MaudeBot"><img src="https://avatars.githubusercontent.com/u/255777700?v=4&s=48" width="48" height="48" alt="MaudeBot" title="MaudeBot"/></a> <a href="https://github.com/YuriNachos"><img src="https://avatars.githubusercontent.com/u/19365375?v=4&s=48" width="48" height="48" alt="YuriNachos" title="YuriNachos"/></a> <a href="https://github.com/chilu18"><img src="https://avatars.githubusercontent.com/u/7957943?v=4&s=48" width="48" height="48" alt="chilu18" title="chilu18"/></a> <a href="https://github.com/byungsker"><img src="https://avatars.githubusercontent.com/u/72309817?v=4&s=48" width="48" height="48" alt="byungsker" title="byungsker"/></a>
  <a href="https://github.com/dbhurley"><img src="https://avatars.githubusercontent.com/u/5251425?v=4&s=48" width="48" height="48" alt="dbhurley" title="dbhurley"/></a> <a href="https://github.com/JayMishra-source"><img src="https://avatars.githubusercontent.com/u/82963117?v=4&s=48" width="48" height="48" alt="JayMishra-source" title="JayMishra-source"/></a> <a href="https://github.com/iHildy"><img src="https://avatars.githubusercontent.com/u/25069719?v=4&s=48" width="48" height="48" alt="iHildy" title="iHildy"/></a> <a href="https://github.com/mudrii"><img src="https://avatars.githubusercontent.com/u/220262?v=4&s=48" width="48" height="48" alt="mudrii" title="mudrii"/></a> <a href="https://github.com/dlauer"><img src="https://avatars.githubusercontent.com/u/757041?v=4&s=48" width="48" height="48" alt="dlauer" title="dlauer"/></a> <a href="https://github.com/Solvely-Colin"><img src="https://avatars.githubusercontent.com/u/211764741?v=4&s=48" width="48" height="48" alt="Solvely-Colin" title="Solvely-Colin"/></a> <a href="https://github.com/czekaj"><img src="https://avatars.githubusercontent.com/u/1464539?v=4&s=48" width="48" height="48" alt="czekaj" title="czekaj"/></a> <a href="https://github.com/advaitpaliwal"><img src="https://avatars.githubusercontent.com/u/66044327?v=4&s=48" width="48" height="48" alt="advaitpaliwal" title="advaitpaliwal"/></a> <a href="https://github.com/lc0rp"><img src="https://avatars.githubusercontent.com/u/2609441?v=4&s=48" width="48" height="48" alt="lc0rp" title="lc0rp"/></a> <a href="https://github.com/grp06"><img src="https://avatars.githubusercontent.com/u/1573959?v=4&s=48" width="48" height="48" alt="grp06" title="grp06"/></a>
  <a href="https://github.com/HenryLoenwind"><img src="https://avatars.githubusercontent.com/u/1485873?v=4&s=48" width="48" height="48" alt="HenryLoenwind" title="HenryLoenwind"/></a> <a href="https://github.com/azade-c"><img src="https://avatars.githubusercontent.com/u/252790079?v=4&s=48" width="48" height="48" alt="azade-c" title="azade-c"/></a> <a href="https://github.com/Lukavyi"><img src="https://avatars.githubusercontent.com/u/1013690?v=4&s=48" width="48" height="48" alt="Lukavyi" title="Lukavyi"/></a> <a href="https://github.com/vrknetha"><img src="https://avatars.githubusercontent.com/u/20596261?v=4&s=48" width="48" height="48" alt="vrknetha" title="vrknetha"/></a> <a href="https://github.com/brandonwise"><img src="https://avatars.githubusercontent.com/u/21148772?v=4&s=48" width="48" height="48" alt="brandonwise" title="brandonwise"/></a> <a href="https://github.com/conroywhitney"><img src="https://avatars.githubusercontent.com/u/249891?v=4&s=48" width="48" height="48" alt="conroywhitney" title="conroywhitney"/></a> <a href="https://github.com/tobiasbischoff"><img src="https://avatars.githubusercontent.com/u/711564?v=4&s=48" width="48" height="48" alt="Tobias Bischoff" title="Tobias Bischoff"/></a> <a href="https://github.com/davidrudduck"><img src="https://avatars.githubusercontent.com/u/47308254?v=4&s=48" width="48" height="48" alt="davidrudduck" title="davidrudduck"/></a> <a href="https://github.com/xinhuagu"><img src="https://avatars.githubusercontent.com/u/562450?v=4&s=48" width="48" height="48" alt="xinhuagu" title="xinhuagu"/></a> <a href="https://github.com/jaydenfyi"><img src="https://avatars.githubusercontent.com/u/213395523?v=4&s=48" width="48" height="48" alt="jaydenfyi" title="jaydenfyi"/></a>
  <a href="https://github.com/petter-b"><img src="https://avatars.githubusercontent.com/u/62076402?v=4&s=48" width="48" height="48" alt="petter-b" title="petter-b"/></a> <a href="https://github.com/heyhudson"><img src="https://avatars.githubusercontent.com/u/258693705?v=4&s=48" width="48" height="48" alt="heyhudson" title="heyhudson"/></a> <a href="https://github.com/MatthieuBizien"><img src="https://avatars.githubusercontent.com/u/173090?v=4&s=48" width="48" height="48" alt="MatthieuBizien" title="MatthieuBizien"/></a> <a href="https://github.com/huntharo"><img src="https://avatars.githubusercontent.com/u/5617868?v=4&s=48" width="48" height="48" alt="huntharo" title="huntharo"/></a> <a href="https://github.com/omair445"><img src="https://avatars.githubusercontent.com/u/32237905?v=4&s=48" width="48" height="48" alt="omair445" title="omair445"/></a> <a href="https://github.com/adam91holt"><img src="https://avatars.githubusercontent.com/u/9592417?v=4&s=48" width="48" height="48" alt="adam91holt" title="adam91holt"/></a> <a href="https://github.com/adhitShet"><img src="https://avatars.githubusercontent.com/u/131381638?v=4&s=48" width="48" height="48" alt="adhitShet" title="adhitShet"/></a> <a href="https://github.com/smartprogrammer93"><img src="https://avatars.githubusercontent.com/u/33181301?v=4&s=48" width="48" height="48" alt="smartprogrammer93" title="smartprogrammer93"/></a> <a href="https://github.com/radek-paclt"><img src="https://avatars.githubusercontent.com/u/50451445?v=4&s=48" width="48" height="48" alt="radek-paclt" title="radek-paclt"/></a> <a href="https://github.com/frankekn"><img src="https://avatars.githubusercontent.com/u/4488090?v=4&s=48" width="48" height="48" alt="frankekn" title="frankekn"/></a>
  <a href="https://github.com/bradleypriest"><img src="https://avatars.githubusercontent.com/u/167215?v=4&s=48" width="48" height="48" alt="bradleypriest" title="bradleypriest"/></a> <a href="https://github.com/rahthakor"><img src="https://avatars.githubusercontent.com/u/8470553?v=4&s=48" width="48" height="48" alt="rahthakor" title="rahthakor"/></a> <a href="https://github.com/shadril238"><img src="https://avatars.githubusercontent.com/u/63901551?v=4&s=48" width="48" height="48" alt="shadril238" title="shadril238"/></a> <a href="https://github.com/VACInc"><img src="https://avatars.githubusercontent.com/u/3279061?v=4&s=48" width="48" height="48" alt="VACInc" title="VACInc"/></a> <a href="https://github.com/juanpablodlc"><img src="https://avatars.githubusercontent.com/u/92012363?v=4&s=48" width="48" height="48" alt="juanpablodlc" title="juanpablodlc"/></a> <a href="https://github.com/jonisjongithub"><img src="https://avatars.githubusercontent.com/u/86072337?v=4&s=48" width="48" height="48" alt="jonisjongithub" title="jonisjongithub"/></a> <a href="https://github.com/magimetal"><img src="https://avatars.githubusercontent.com/u/36491250?v=4&s=48" width="48" height="48" alt="magimetal" title="magimetal"/></a> <a href="https://github.com/stakeswky"><img src="https://avatars.githubusercontent.com/u/64798754?v=4&s=48" width="48" height="48" alt="stakeswky" title="stakeswky"/></a> <a href="https://github.com/AbhisekBasu1"><img src="https://avatars.githubusercontent.com/u/40645221?v=4&s=48" width="48" height="48" alt="abhisekbasu1" title="abhisekbasu1"/></a> <a href="https://github.com/MisterGuy420"><img src="https://avatars.githubusercontent.com/u/255743668?v=4&s=48" width="48" height="48" alt="MisterGuy420" title="MisterGuy420"/></a>
  <a href="https://github.com/hsrvc"><img src="https://avatars.githubusercontent.com/u/129702169?v=4&s=48" width="48" height="48" alt="hsrvc" title="hsrvc"/></a> <a href="https://github.com/nabbilkhan"><img src="https://avatars.githubusercontent.com/u/203121263?v=4&s=48" width="48" height="48" alt="nabbilkhan" title="nabbilkhan"/></a> <a href="https://github.com/aldoeliacim"><img src="https://avatars.githubusercontent.com/u/17973757?v=4&s=48" width="48" height="48" alt="aldoeliacim" title="aldoeliacim"/></a> <a href="https://github.com/jamesgroat"><img src="https://avatars.githubusercontent.com/u/2634024?v=4&s=48" width="48" height="48" alt="jamesgroat" title="jamesgroat"/></a> <a href="https://github.com/orlyjamie"><img src="https://avatars.githubusercontent.com/u/6668807?v=4&s=48" width="48" height="48" alt="orlyjamie" title="orlyjamie"/></a> <a href="https://github.com/Elarwei001"><img src="https://avatars.githubusercontent.com/u/168552401?v=4&s=48" width="48" height="48" alt="Elarwei001" title="Elarwei001"/></a> <a href="https://github.com/rubyrunsstuff"><img src="https://avatars.githubusercontent.com/u/246602379?v=4&s=48" width="48" height="48" alt="rubyrunsstuff" title="rubyrunsstuff"/></a> <a href="https://github.com/Phineas1500"><img src="https://avatars.githubusercontent.com/u/41450967?v=4&s=48" width="48" height="48" alt="Phineas1500" title="Phineas1500"/></a> <a href="https://github.com/meaningfool"><img src="https://avatars.githubusercontent.com/u/2862331?v=4&s=48" width="48" height="48" alt="meaningfool" title="meaningfool"/></a> <a href="https://github.com/sfo2001"><img src="https://avatars.githubusercontent.com/u/103369858?v=4&s=48" width="48" height="48" alt="sfo2001" title="sfo2001"/></a>
  <a href="https://github.com/Marvae"><img src="https://avatars.githubusercontent.com/u/11957602?v=4&s=48" width="48" height="48" alt="Marvae" title="Marvae"/></a> <a href="https://github.com/liuy"><img src="https://avatars.githubusercontent.com/u/1192888?v=4&s=48" width="48" height="48" alt="liuy" title="liuy"/></a> <a href="https://github.com/shtse
```

### `docker-compose.yml`

- Source path: `docker-compose.yml`
- Truncated: `no`

```yaml
services:
  openclaw-gateway:
    image: ${OPENCLAW_IMAGE:-openclaw:local}
    environment:
      HOME: /home/node
      TERM: xterm-256color
      OPENCLAW_GATEWAY_TOKEN: ${OPENCLAW_GATEWAY_TOKEN:-}
      OPENCLAW_ALLOW_INSECURE_PRIVATE_WS: ${OPENCLAW_ALLOW_INSECURE_PRIVATE_WS:-}
      CLAUDE_AI_SESSION_KEY: ${CLAUDE_AI_SESSION_KEY:-}
      CLAUDE_WEB_SESSION_KEY: ${CLAUDE_WEB_SESSION_KEY:-}
      CLAUDE_WEB_COOKIE: ${CLAUDE_WEB_COOKIE:-}
      TZ: ${OPENCLAW_TZ:-UTC}
    volumes:
      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw
      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace
      ## Uncomment the lines below to enable sandbox isolation
      ## (agents.defaults.sandbox). Requires Docker CLI in the image
      ## (build with --build-arg OPENCLAW_INSTALL_DOCKER_CLI=1) or use
      ## scripts/docker/setup.sh with OPENCLAW_SANDBOX=1 for automated setup.
      ## Set DOCKER_GID to the host's docker group GID (run: stat -c '%g' /var/run/docker.sock).
      # - /var/run/docker.sock:/var/run/docker.sock
    # group_add:
    #   - "${DOCKER_GID:-999}"
    ports:
      - "${OPENCLAW_GATEWAY_PORT:-18789}:18789"
      - "${OPENCLAW_BRIDGE_PORT:-18790}:18790"
    init: true
    restart: unless-stopped
    command:
      [
        "node",
        "dist/index.js",
        "gateway",
        "--bind",
        "${OPENCLAW_GATEWAY_BIND:-lan}",
        "--port",
        "18789",
      ]
    healthcheck:
      test:
        [
          "CMD",
          "node",
          "-e",
          "fetch('http://127.0.0.1:18789/healthz').then((r)=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))",
        ]
      interval: 30s
      timeout: 5s
      retries: 5
      start_period: 20s

  openclaw-cli:
    image: ${OPENCLAW_IMAGE:-openclaw:local}
    network_mode: "service:openclaw-gateway"
    cap_drop:
      - NET_RAW
      - NET_ADMIN
    security_opt:
      - no-new-privileges:true
    environment:
      HOME: /home/node
      TERM: xterm-256color
      OPENCLAW_GATEWAY_TOKEN: ${OPENCLAW_GATEWAY_TOKEN:-}
      OPENCLAW_ALLOW_INSECURE_PRIVATE_WS: ${OPENCLAW_ALLOW_INSECURE_PRIVATE_WS:-}
      BROWSER: echo
      CLAUDE_AI_SESSION_KEY: ${CLAUDE_AI_SESSION_KEY:-}
      CLAUDE_WEB_SESSION_KEY: ${CLAUDE_WEB_SESSION_KEY:-}
      CLAUDE_WEB_COOKIE: ${CLAUDE_WEB_COOKIE:-}
      TZ: ${OPENCLAW_TZ:-UTC}
    volumes:
      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw
      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace
    stdin_open: true
    tty: true
    init: true
    entrypoint: ["node", "dist/index.js"]
    depends_on:
      - openclaw-gateway
```

### `package.json`

- Source path: `package.json`
- Truncated: `yes`

```json
{
  "name": "openclaw",
  "version": "2026.4.11",
  "description": "Multi-channel AI gateway with extensible messaging integrations",
  "keywords": [],
  "homepage": "https://github.com/openclaw/openclaw#readme",
  "bugs": {
    "url": "https://github.com/openclaw/openclaw/issues"
  },
  "license": "MIT",
  "author": "",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/openclaw/openclaw.git"
  },
  "bin": {
    "openclaw": "openclaw.mjs"
  },
  "directories": {
    "doc": "docs",
    "test": "test"
  },
  "files": [
    "CHANGELOG.md",
    "LICENSE",
    "openclaw.mjs",
    "README.md",
    "assets/",
    "dist/",
    "!dist/**/*.map",
    "!dist/plugin-sdk/.tsbuildinfo",
    "!dist/extensions/qa-channel/**",
    "dist/extensions/qa-channel/runtime-api.js",
    "!dist/extensions/qa-lab/**",
    "dist/extensions/qa-lab/runtime-api.js",
    "docs/",
    "!docs/.generated/**",
    "!docs/.i18n/zh-CN.tm.jsonl",
    "qa/scenarios/",
    "skills/",
    "scripts/npm-runner.mjs",
    "scripts/postinstall-bundled-plugins.mjs",
    "scripts/windows-cmd-helpers.mjs"
  ],
  "type": "module",
  "main": "dist/index.js",
  "exports": {
    ".": "./dist/index.js",
    "./plugin-sdk": {
      "types": "./dist/plugin-sdk/index.d.ts",
      "default": "./dist/plugin-sdk/index.js"
    },
    "./plugin-sdk/core": {
      "types": "./dist/plugin-sdk/core.d.ts",
      "default": "./dist/plugin-sdk/core.js"
    },
    "./plugin-sdk/provider-setup": {
      "types": "./dist/plugin-sdk/provider-setup.d.ts",
      "default": "./dist/plugin-sdk/provider-setup.js"
    },
    "./plugin-sdk/sandbox": {
      "types": "./dist/plugin-sdk/sandbox.d.ts",
      "default": "./dist/plugin-sdk/sandbox.js"
    },
    "./plugin-sdk/self-hosted-provider-setup": {
      "types": "./dist/plugin-sdk/self-hosted-provider-setup.d.ts",
      "default": "./dist/plugin-sdk/self-hosted-provider-setup.js"
    },
    "./plugin-sdk/routing": {
      "types": "./dist/plugin-sdk/routing.d.ts",
      "default": "./dist/plugin-sdk/routing.js"
    },
    "./plugin-sdk/runtime": {
      "types": "./dist/plugin-sdk/runtime.d.ts",
      "default": "./dist/plugin-sdk/runtime.js"
    },
    "./plugin-sdk/runtime-doctor": {
      "types": "./dist/plugin-sdk/runtime-doctor.d.ts",
      "default": "./dist/plugin-sdk/runtime-doctor.js"
    },
    "./plugin-sdk/runtime-env": {
      "types": "./dist/plugin-sdk/runtime-env.d.ts",
      "default": "./dist/plugin-sdk/runtime-env.js"
    },
    "./plugin-sdk/proxy-capture": {
      "types": "./dist/plugin-sdk/proxy-capture.d.ts",
      "default": "./dist/plugin-sdk/proxy-capture.js"
    },
    "./plugin-sdk/runtime-secret-resolution": {
      "types": "./dist/plugin-sdk/runtime-secret-resolution.d.ts",
      "default": "./dist/plugin-sdk/runtime-secret-resolution.js"
    },
    "./plugin-sdk/setup": {
      "types": "./dist/plugin-sdk/setup.d.ts",
      "default": "./dist/plugin-sdk/setup.js"
    },
    "./plugin-sdk/setup-adapter-runtime": {
      "types": "./dist/plugin-sdk/setup-adapter-runtime.d.ts",
      "default": "./dist/plugin-sdk/setup-adapter-runtime.js"
    },
    "./plugin-sdk/setup-runtime": {
      "types": "./dist/plugin-sdk/setup-runtime.d.ts",
      "default": "./dist/plugin-sdk/setup-runtime.js"
    },
    "./plugin-sdk/channel-setup": {
      "types": "./dist/plugin-sdk/channel-setup.d.ts",
      "default": "./dist/plugin-sdk/channel-setup.js"
    },
    "./plugin-sdk/channel-streaming": {
      "types": "./dist/plugin-sdk/channel-streaming.d.ts",
      "default": "./dist/plugin-sdk/channel-streaming.js"
    },
    "./plugin-sdk/setup-tools": {
      "types": "./dist/plugin-sdk/setup-tools.d.ts",
      "default": "./dist/plugin-sdk/setup-tools.js"
    },
    "./plugin-sdk/approval-auth-runtime": {
      "types": "./dist/plugin-sdk/approval-auth-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-auth-runtime.js"
    },
    "./plugin-sdk/approval-client-runtime": {
      "types": "./dist/plugin-sdk/approval-client-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-client-runtime.js"
    },
    "./plugin-sdk/approval-delivery-runtime": {
      "types": "./dist/plugin-sdk/approval-delivery-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-delivery-runtime.js"
    },
    "./plugin-sdk/approval-gateway-runtime": {
      "types": "./dist/plugin-sdk/approval-gateway-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-gateway-runtime.js"
    },
    "./plugin-sdk/approval-handler-adapter-runtime": {
      "types": "./dist/plugin-sdk/approval-handler-adapter-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-handler-adapter-runtime.js"
    },
    "./plugin-sdk/approval-handler-runtime": {
      "types": "./dist/plugin-sdk/approval-handler-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-handler-runtime.js"
    },
    "./plugin-sdk/channel-runtime-context": {
      "types": "./dist/plugin-sdk/channel-runtime-context.d.ts",
      "default": "./dist/plugin-sdk/channel-runtime-context.js"
    },
    "./plugin-sdk/approval-native-runtime": {
      "types": "./dist/plugin-sdk/approval-native-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-native-runtime.js"
    },
    "./plugin-sdk/approval-reply-runtime": {
      "types": "./dist/plugin-sdk/approval-reply-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-reply-runtime.js"
    },
    "./plugin-sdk/approval-runtime": {
      "types": "./dist/plugin-sdk/approval-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-runtime.js"
    },
    "./plugin-sdk/config-runtime": {
      "types": "./dist/plugin-sdk/config-runtime.d.ts",
      "default": "./dist/plugin-sdk/config-runtime.js"
    },
    "./plugin-sdk/config-schema": {
      "types": "./dist/plugin-sdk/config-schema.d.ts",
      "default": "./dist/plugin-sdk/config-schema.js"
    },
    "./plugin-sdk/reply-runtime": {
      "types": "./dist/plugin-sdk/reply-runtime.d.ts",
      "default": "./dist/plugin-sdk/reply-runtime.js"
    },
    "./plugin-sdk/reply-dispatch-runtime": {
      "types": "./dist/plugin-sdk/reply-dispatch-runtime.d.ts",
      "default": "./dist/plugin-sdk/reply-dispatch-runtime.js"
    },
    "./plugin-sdk/reply-reference": {
      "types": "./dist/plugin-sdk/reply-reference.d.ts",
      "default": "./dist/plugin-sdk/reply-reference.js"
    },
    "./plugin-sdk/reply-chunking": {
      "types": "./dist/plugin-sdk/reply-chunking.d.ts",
      "default": "./dist/plugin-sdk/reply-chunking.js"
    },
    "./plugin-sdk/reply-payload": {
      "types": "./dist/plugin-sdk/reply-payload.d.ts",
      "default": "./dist/plugin-sdk/reply-payload.js"
    },
    "./plugin-sdk/agent-media-payload": {
      "types": "./dist/plugin-sdk/agent-media-payload.d.ts",
      "default": "./dist/plugin-sdk/agent-media-payload.js"
    },
    "./plugin-sdk/inbound-reply-dispatch": {
      "types": "./dist/plugin-sdk/inbound-reply-dispatch.d.ts",
      "default": "./dist/plugin-sdk/inbound-reply-dispatch.js"
    },
    "./plugin-sdk/inbound-envelope": {
      "types": "./dist/plugin-sdk/inbound-envelope.d.ts",
      "default": "./dist/plugin-sdk/inbound-envelope.js"
    },
    "./plugin-sdk/channel-reply-pipeline": {
      "types": "./dist/plugin-sdk/channel-reply-pipeline.d.ts",
      "default": "./dist/plugin-sdk/channel-reply-pipeline.js"
    },
    "./plugin-sdk/channel-runtime": {
      "types": "./dist/plugin-sdk/channel-runtime.d.ts",
      "default": "./dist/plugin-sdk/channel-runtime.js"
    },
    "./plugin-sdk/interactive-runtime": {
      "types": "./dist/plugin-sdk/interactive-runtime.d.ts",
      "default": "./dist/plugin-sdk/interactive-runtime.js"
    },
    "./plugin-sdk/outbound-media": {
      "types": "./dist/plugin-sdk/outbound-media.d.ts",
      "default": "./dist/plugin-sdk/outbound-media.js"
    },
    "./plugin-sdk/outbound-runtime": {
      "types": "./dist/plugin-sdk/outbound-runtime.d.ts",
      "default": "./dist/plugin-sdk/outbound-runtime.js"
    },
    "./plugin-sdk/infra-runtime": {
      "types": "./dist/plugin-sdk/infra-runtime.d.ts",
      "default": "./dist/plugin-sdk/infra-runtime.js"
    },
    "./plugin-sdk/runtime-config-snapshot": {
      "types": "./dist/plugin-sdk/runtime-config-snapshot.d.ts",
      "default": "./dist/plugin-sdk/runtime-config-snapshot.js"
    },
    "./plugin-sdk/runtime-group-policy": {
      "types": "./dist/plugin-sdk/runtime-group-policy.d.ts",
      "default": "./dist/plugin-sdk/runtime-group-policy.js"
    },
    "./plugin-sdk/ssrf-policy": {
      "types": "./dist/plugin-sdk/ssrf-policy.d.ts",
      "default": "./dist/plugin-sdk/ssrf-policy.js"
    },
    "./plugin-sdk/ssrf-runtime": {
      "types": "./dist/plugin-sdk/ssrf-runtime.d.ts",
      "default": "./dist/plugin-sdk/ssrf-runtime.js"
    },
    "./plugin-sdk/media-runtime": {
      "types": "./dist/plugin-sdk/media-runtime.d.ts",
      "default": "./dist/plugin-sdk/media-runtime.js"
    },
    "./plugin-sdk/media-mime": {
      "types": "./dist/plugin-sdk/media-mime.d.ts",
      "default": "./dist/plugin-sdk/media-mime.js"
    },
    "./plugin-sdk/media-generation-runtime": {
      "types": "./dist/plugin-sdk/media-generation-runtime.d.ts",
      "default": "./dist/plugin-sdk/media-generation-runtime.js"
    },
    "./plugin-sdk/conversation-binding-runtime": {
      "types": "./dist/plugin-sdk/conversation-binding-runtime.d.ts",
      "default": "./dist/plugin-sdk/conversation-binding-runtime.js"
    },
    "./plugin-sdk/conversation-runtime": {
      "types": "./dist/plugin-sdk/conversation-runtime.d.ts",
      "default": "./dist/plugin-sdk/conversation-runtime.js"
    },
    "./plugin-sdk/matrix-runtime-heavy": {
      "types": "./dist/plugin-sdk/matrix-runtime-heavy.d.ts",
      "default": "./dist/plugin-sdk/matrix-runtime-heavy.js"
    },
    "./plugin-sdk/matrix-runtime-shared": {
      "types": "./dist/plugin-sdk/matrix-runtime-shared.d.ts",
      "default": "./dist/plugin-sdk/matrix-runtime-shared.js"
    },
    "./plugin-sdk/thread-bindings-runtime": {
      "types": "./dist/plugin-sdk/thread-bindings-runtime.d.ts",
      "default": "./dist/plugin-sdk/thread-bindings-runtime.js"
    },
    "./plugin-sdk/text-runtime": {
      "types": "./dist/plugin-sdk/text-runtime.d.ts",
      "default": "./dist/plugin-sdk/text-runtime.js"
    },
    "./plugin-sdk/text-chunking": {
      "types": "./dist/plugin-sdk/text-chunking.d.ts",
      "default": "./dist/plugin-sdk/text-chunking.js"
    },
    "./plugin-sdk/agent-runtime": {
      "types": "./dist/plugin-sdk/agent-runtime.d.ts",
      "default": "./dist/plugin-sdk/agent-runtime.js"
    },
    "./plugin-sdk/simple-completion-runtime": {
      "types": "./dist/plugin-sdk/simple-completion-runtime.d.ts",
      "default": "./dist/plugin-sdk/simple-completion-runtime.js"
    },
    "./plugin-sdk/speech-core": {
      "types": "./dist/plugin-sdk/speech-core.d.ts",
      "default": "./dist/plugin-sdk/speech-core.js"
    },
    "./plugin-sdk/plugin-runtime": {
      "types": "./dist/plugin-sdk/plugin-runtime.d.ts",
      "default": "./dist/plugin-sdk/plugin-runtime.js"
    },
    "./plugin-sdk/channel-secret-basic-runtime": {
      "types": "./dist/plugin-sdk/channel-secret-basic-runtime.d.ts",
      "default": "./dist/plugin-sdk/channel-secret-basic-runtime.js"
    },
    "./plugin-sdk/channel-secret-runtime": {
      "types": "./dist/plugin-sdk/channel-secret-runtime.d.ts",
      "default": "./dist/plugin-sdk/channel-secret-runtime.js"
    },
    "./plugin-sdk/channel-secret-tts-runtime": {
      "types": "./dist/plugin-sdk/channel-secret-tts-runtime.d.ts",
      "default": "./dist/plugin-sdk/channel-secret-tts-runtime.js"
    },
    "./plugin-sdk/secret-ref-runtime": {
      "types": "./dist/plugin-sdk/secret-ref-runtime.d.ts",
      "default": "./dist/plugin-sdk/secret-ref-runtime.js"
    },
    "./plugin-sdk/security-runtime": {
      "types": "./dist/plugin-sdk/security-runtime.d.ts",
      "default": "./dist/plugin-sdk/security-runtime.js"
    },
    "./plugin-sdk/gateway-runtime": {
      "types": "./dist/plugin-sdk/gateway-runtime.d.ts",
      "default": "./dist/plugin-sdk/gateway-runtime.js"
    },
    "./plugin-sdk/github-copilot-login": {
      "types": "./dist/plugin-sdk/github-copilot-login.d.ts",
      "default": "./dist/plugin-sdk/github-copilot-login.js"
    },
    "./plugin-sdk/github-copilot-token": {
      "types": "./dist/plugin-sdk/github-copilot-token.d.ts",
      "default": "./dist/plugin-sdk/github-copilot-token.js"
    },
    "./plugin-sdk/cli-runtime": {
      "types": "./dist/plugin-sdk/cli-runtime.d.ts",
      "default": "./dist/plugin-sdk/cli-runtime.js"
    },
    "./plugin-sdk/cli-backend": {
      "types": "./dist/plugin-sdk/cli-backend.d.ts",
      "default": "./dist/plugin-sdk/cli-backend.js"
    },
    "./plugin-sdk/agent-harness": {
      "types": "./dist/plugin-sdk/agent-harness.d.ts",
      "default": "./dist/plugin-sdk/agent-harness.js"
    },
    "./plugin-sdk/hook-runtime": {
      "types": "./dist/plugin-sdk/hook-runtime.d.ts",
      "default": "./dist/plugin-sdk/hook-runtime.js"
    },
    "./plugin-sdk/host-runtime": {
      "types": "./dist/plugin-sdk/host-runtime.d.ts",
      "default": "./dist/plugin-sdk/host-runtime.js"
    },
    "./plugin-sdk/process-runtime": {
      "types": "./dist/plugin-sdk/process-runtime.d.ts",
      "default": "./dist/plugin-sdk/process-runtime.js"
    },
    "./plugin-sdk/windows-spawn": {
      "types": "./dist/plugin-sdk/windows-spawn.d.ts",
      "default": "./dist/plugin-sdk/windows-spawn.js"
    },
    "./plugin-sdk/acp-runtime": {
      "types": "./dist/plugin-sdk/acp-runtime.d.ts",
      "default": "./dist/plugin-sdk/acp-runtime.js"
    },
    "./plugin-sdk/acp-binding-runtime": {
      "types": "./dist/plugin-sdk/acp-binding-runtime.d.ts",
      "default": "./dist/plugin-sdk/acp-binding-runtime.js"
    },
    "./plugin-sdk/lazy-runtime": {
      "types": "./dist/plugin-sdk/lazy-runtime.d.ts",
      "default": "./dist/plugin-sdk/lazy-runtime.js"
    },
    "./plugin-sdk/testing": {
      "types": "./dist/plugin-sdk/testing.d.ts",
      "default": "./dist/plugin-sdk/testing.js"
    },
    "./plugin-sdk/temp-path": {
      "types": "./dist/plugin-sdk/temp-path.d.ts",
      "default": "./dist/plugin-sdk/temp-path.js"
    },
    "./plugin-sdk/logging-core": {
      "types": "./dist/plugin-sdk/logging-core.d.ts",
      "default": "./dist/plugin-sdk/logging-core.js"
    },
    "./plugin-sdk/markdown-table-runtime": {
      "types": "./dist/plugin-sdk/markdown-table-runtime.d.ts",
      "default": "./dist/plugin-sdk/markdown-table-runtime.js"
    },
    "./plugin-sdk/account-helpers": {
      "types": "./dist/plugin-sdk/account-helpers.d.ts",
      "default": "./dist/plugin-sdk/account-helpers.js"
    },
    "./plugin-sdk/account-core": {
      "types": "./dist/plugin-sdk/account-core.d.ts",
      "default": "./dist/plugin-sdk/account-core.js"
    },
    "./plugin-sdk/account-id": {
      "types": "./dist/plugin-sdk/account-id.d.ts",
      "default": "./dist/plugin-sdk/account-id.js"
    },
    "./plugin-sdk/account-resolution": {
      "types": "./dist/plugin-sdk/account-resolution.d.ts",
      "default": "./dist/plugin-sdk/account-resolution.js"
    },
    "./plugin-sdk/agent-config-primitives": {
      "types": "./dist/plugin-sdk/agent-config-primitives.d.ts",
      "default": "./dist/plugin-sdk/agent-config-primitives.js"
    },
    "./plugin-sdk/allow-from": {
      "types": "./dist/plugin-sdk/allow-from.d.ts",
      "default": "./dist/plugin-sdk/allow-from.js"
    },
    "./plugin-sdk/allowlist-config-edit": {
      "types": "./dist/plugin-sdk/allowlist-config-edit.d.ts",
      "default": "./dist/plugin-sdk/allowlist-config-edit.js"
    },
    "./plugin-sdk/bluebubbles": {
      "types": "./dist/plugin-sdk/bluebubbles.d.ts",
      "default": "./dist/plugin-sdk/bluebubbles.js"
    },
    "./plugin-sdk/bluebubbles-policy": {
      "types": "./dist/plugin-sdk/bluebubbles-policy.d.ts",
      "default": "./dist/plugin-sdk/bluebubbles-policy.js"
    },
    "./plugin-sdk/browser-cdp": {
      "types": "./dist/plugin-sdk/browser-cdp.d.ts",
      "default": "./dist/plugin-sdk/browser-cdp.js"
    },
    "./plugin-sdk/browser-config": {
      "types": "./dist/plugin-sdk/browser-config.d.ts",
      "default": "./dist/plugin-sdk/browser-config.js"
    },
    "./plugin-sdk/browser-config-runtime": {
      "types": "./dist/plugin-sdk/browser-config-runtime.d.ts",
      "default": "./dist/plugin-sdk/browser-config-runtime.js"
    },
    "./plugin-sdk/browser-config-support": {
      "types": "./dist/plugin-sdk/browser-config-support.d.ts",
      "default": "./dist/plugin-sdk/browser-config-support.js"
    },
    "./plugin-sdk/browser-control-auth": {
      "types": "./dist/plugin-sdk/browser-control-auth.d.ts",
      "default": "./dist/plugin-sdk/browser-control-auth.js"
    },
    "./plugin-sdk/browser-node-runtime": {
      "types": "./dist/plugin-sdk/browser-node-runtime.d.ts",
      "default": "./dist/plugin-sdk/browser-node-runtime.js"
    },
    "./plugin-sdk/browser-profiles": {
      "types": "./dist/plugin-sdk/browser-profiles.d.ts",
      "default": "./dist/plugin-sdk/browser-profiles.js"
    },
    "./plugin-sdk/browser-security-runtime": {
      "types": "./dist/plugin-sdk/browser-security-runtime.d.ts",
      "default": "./dist/plugin-sdk/browser-security-runtime.js"
    },
    "./plugin-sdk/browser-setup-tools": {
      "types": "./dist/plugin-sdk/browser-setup-tools.d.ts",
      "default": "./dist/plugin-sdk/browser-setup-tools.js"
    },
    "./plugin-sdk/browser-support": {
      "types": "./dist/plugin-sdk/browser-support.d.ts",
      "default": "./dist/plugin-sdk/browser-support.js"
    },
    "./plugin-sdk/boolean-param": {
      "types": "./dist/plugin-sdk/boolean-param.d.ts",
      "default": "./dist/plugin-sdk/boolean-param.js"
    },
    "./plugin-sdk/dangerous-name-runtime": {
      "types": "./dist/plugin-sdk/dangerous-name-runtime.d.ts",
      "default": "./dist/plugin-sdk/dangerous-name-runtime.js"
    },
    "./plugin-sdk/command-auth": {
      "types": "./dist/plugin-sdk/command-auth.d.ts",
      "default": "./dist/plugin-sdk/command-auth.js"
    },
    "./plugin-sdk/command-auth-native": {
      "types": "./dist/plugin-sdk/command-auth-native.d.ts",
      "default": "./dist/plugin-sdk/command-auth-native.js"
    },
    "./plugin-sdk/command-status": {
      "types": "./dist/plugin-sdk/command-status.d.ts",
      "default": "./dist/plugin-sdk/command-status.js"
    },
    "./plugin-sdk/command-detection": {
      "types": "./dist/plugin-sdk/command-detection.d.ts",
      "default": "./dist/plugin-sdk/command-detection.js"
    },
    "./plugin-sdk/command-surface": {
      "types": "./dist/plugin-sdk/command-surface.d.ts",
      "default": "./dist/plugin-sdk/command-surface.js"
    },
    "./plugin-sdk/collection-runtime": {
      "types": "./dist/plugin-sdk/collection-runtime.d.ts",
      "default": "./dist/plugin-sdk/collection-runtime.js"
    },
    "./plugin-sdk/compat": {
      "types": "./dist/plugin-sdk/compat.d.ts",
      "default": "./dist/plugin-sdk/compat.js"
    },
    "./plugin-sdk/direct-dm": {
      "types": "./dist/plugin-sdk/direct-dm.d.ts",
      "default": "./dist/plugin-sdk/direct-dm.js"
    },
    "./plugin-sdk/device-bootstrap": {
      "types": "./dist/plugin-sdk/device-bootstrap.d.ts",
      "default": "./dist/plugin-sdk/device-bootstrap.js"
    },
    "./plugin-sdk/diagnostic-runtime": {
      "types": "./dist/plugin-sdk/diagnostic-runtime.d.ts",
      "default": "./dist/plugin-sdk/diagnostic-runtime.js"
    },
    "./plugin-sdk/diagnostics-otel": {
      "types": "./dist/plugin-sdk/diagnostics-otel.d.ts",
      "default": "./dist/plugin-sdk/diagnostics-otel.js"
    },
    "./plugin-sdk/diffs": {
      "types": "./dist/plugin-sdk/diffs.d.ts",
      "default": "./dist/plugin-sdk/diffs.js"
    },
    "./plugin-sdk/error-runtime": {
      "types": "./dist/plugin-sdk/error-runtime.d.ts",
      "default": "./dist/plugin-sdk/error-runtime.js"
    },
    "./plugin-sdk/extension-shared": {
      "types": "./dist/plugin-sdk/extension-shared.d.ts",
      "default": "./dist/plugin-sdk/extension-shared.js"
    },
    "./plugin-sdk/channel-config-helpers": {
      "types": "./dist/plugin-sdk/channel-config-helpers.d.ts",
      "default": "./dist/plugin-sdk/channel-config-helpers.js"
    },
    "./plugin-sdk/channel-config-writes": {
      "types": "./dist/plugin-sdk/channel-config-writes.d.ts",
      "default": "./dist/plugin-sdk/channel-config-writes.js"
    },
    "./plugin-sdk/channel-config-primitives": {
      "types": "./dist/plugin-sdk/channel-config-primitives.d.ts",
      "default": "./dist/plugin-sdk/channel-config-primitives.js"
    },
    "./plugin-sdk/channel-config-schema": {
      "types": "./dist/plugin-sdk/channel-config-schema.d.ts",
      "default": "./dist/plugin-sdk/channel-config-schema.js"
    },
    "./plugin-sdk/channel-actions": {
      "types": "./dist/plugin-sdk/channel-actions.d.ts",
      "default": "./dist/plugin-sdk/channel-actions.js"
    },
    "./plugin-sdk/channel-plugin-common": {
      "types": "./dist/plugin-sdk/channel-plugin-common.d.ts",
      "default": "./dist/plugin-sdk/channel-plugin-common.js"
    },
    "./plugin-sdk/channel-core": {
      "types": "./dist/plugin-sdk/channel-core.d.ts",
      "default": "./dist/plugin-sdk/channel-core.js"
    },
    "./plugin-sdk/channel-entry-contract": {
      "types": "./dist/plugin-sdk/channel-entry-contract.d.ts",
      "default": "./dist/plugin-sdk/channel-entry-contract.js"
    },
    "./plugin-sdk/channel-contract": {
      "types": "./dist/plugin-sdk/channel-contract.d.ts",
      "default": "./dist/plugin-sdk/channel-contract.js"
    },
    "./plugin-sdk/channel-feedback": {
      "types": "./dist/plugin-sdk/channel-feedback.d.ts",
      "default": "./dist/plugin-sdk/channel-feedback.js"
    },
    "./plugin-sdk/channel-inbound": {
      "types": "./dist/plugin-sdk/channel-inbound.d.ts",
      "default": "./dist/plugin-sdk/channel-inbound.js"
    },
    "./plugin-sdk/channel-inbound-roots": {
      "types": "./dist/plugin-sdk/channel-inbound-roots.d.ts",
      "default": "./dist/plugin-sdk/channel-inbound-roots.js"
    },
    "./plugin-sdk/channel-lifecycle": {
      "types": "./dist/plugin-sdk/channel-lifecycle.d.ts",
      "default": "./dist/plugin-sdk/channel-lifecycle.js"
    },
    "./plugin-sdk/channel-pairing": {
      "types": "./dist/plugin-sdk/channel-pairing.d.ts",
      "default": "./dist/plugin-sdk/channel-pairing.js"
    },
    "./plugin-sdk/channel-policy": {
      "types": "./dist/plugin-sdk/channel-policy.d.ts",
      "default": "./dist/plugin-sdk/channel-policy.js"
    },
    "./plugin-sdk/channel-send-result": {
      "types": "./dist/plugin-sdk/channel-send-result.d.ts",
      "default": "./dist/plugin-sdk/channel-send-result.js"
    },
    "./plugin-sdk/channel-targets": {
      "types": "./dist/plugin-sdk/channel-targets.d.ts",
      "default": "./dist/plugin-sdk/channel-targets.js"
    },
    "./plugin-sdk/feishu": {
      "types": "./dist/plugin-sdk/feishu.d.ts",
      "default": "./dist/plugin-sdk/feishu.js"
    },
    "./plugin-sdk/feishu-conversation": {
      "types": "./dist/plugin-sdk/feishu-conversation.d.ts",
      "default": "./dist/plugin-sdk/feishu-conversation.js"
    },
    "./plugin-sdk/feishu-setup": {
      "types": "./dist/plugin-sdk/feishu-setup.d.ts",
      "default": "./dist/plugin-sdk/feishu-setup.js"
    },
    "./plugin-sdk/file-lock": {
      "types": "./dist/plugin-sdk/file-lock.d.ts",
      "default": "./dist/plugin-sdk/file-lock.js"
    },
    "./plugin-sdk/fetch-runtime": {
      "types": "./dist/plugin-sdk/fetch-runtime.d.ts",
      "default": "./dist/plugin-sdk/fetch-runtime.js"
    },
    "./plugin-sdk/group-access": {
      "types": "./dist/plugin-sdk/group-access.d.ts",
      "default": "./dist/plugin-sdk/group-access.js"
    },
    "./plugin-sdk/global-singleton": {
      "types": "./dist/plugin-sdk/global-singleton.d.ts",
      "default": "./dist/plugin-sdk/global-singleton.js"
    },
    "./plugin-sdk/directory-runtime": {
      "types": "./dist/plugin-sdk/directory-runtime.d.ts",
      "default": "./dist/plugin-sdk/directory-runtime.js"
    },
    "./plugin-sdk/googlechat": {
      "types": "./dist/plugin-sdk/googlechat.d.ts",
      "default": "./dist/plugin-sdk/googlechat.js"
    },
    "./plugin-sdk/googlechat-runtime-shared": {
      "types": "./dist/plugin-sdk/googlechat-runtime-shared.d.ts",
      "default": "./dist/plugin-sdk/googlechat-runtime-shared.js"
    },
    "./plugin-sdk/media-generation-runtime-shared": {
      "types": "./dist/plugin-sdk/media-generation-runtime-shared.d.ts",
      "default": "./dist/plugin-sdk/media-generation-runtime-shared.js"
    },
    "./plugin-sdk/image-generation": {
      "types": "./dist/plugin-sdk/image-generation.d.ts",
      "default": "./dist/plugin-sdk/image-generation.js"
    },
    "./plugin-sdk/image-generation-runtime": {
      "types": "./dist/plugin-sdk/image-generation-runtime.d.ts",
      "default": "./dist/plugin-sdk/image-generation-runtime.js"
    },
    "./plugin-sdk/image-generation-core": {
      "types": "./dist/plugin-sdk/image-generation-core.d.ts",
      "default": "./dist/plugin-sdk/image-generation-core.js"
    },
    "./plugin-sdk/music-generation": {
      "types": "./dist/plugin-sdk/music-generation.d.ts",
      "default": "./dist/plugin-sdk/music-generation.js"
    },
    "./plugin-sdk/music-generation-core": {
      "types": "./dist/plugin-sdk/music-generation-core.d.ts",
      "default": "./dist/plugin-sdk/music-generation-core.js"
    },
    "./plugin-sdk/video-generation": {
      "types": "./dist/plugin-sdk/video-generation.d.ts",
      "default": "./dist/plugin-sdk/video-generation.js"
    },
    "./plugin-sdk/video-generation-runtime": {
      "types": "./dist/plugin-sdk/video-generation-runtime.d.ts",
      "default": "./dist/plugin-sdk/video-generation-runtime.js"
    },
    "./plugin-sdk/video-generation-core": {
      "types": "./dist/plugin-sdk/video-generation-core.d.ts",
      "default": "./dist/plugin-sdk/video-generation-core.js"
    },
    "./plugin-sdk/irc": {
      "types": "./dist/plugin-sdk/irc.d.ts",
      "default": "./dist/plugin-sdk/irc.js"
    },
    "./plugin-sdk/irc-surface": {
      "types": "./dist/plugin-sdk/irc-surface.d.ts",
      "default": "./dist/plugin-sdk/irc-surface.js"
    },
    "./plugin-sdk/reply-history": {
      "types": "./dist/plugin-sdk/reply-history.d.ts",
      "default": "./dist/plugin-sdk/reply-history.js"
    },
    "./plugin-sdk/realtime-transcription": {
      "types": "./dist/plugin-sdk/realtime-transcription.d.ts",
      "default": "./dist/plugin-sdk/realtime-transcription.js"
    },
    "./plugin-sdk/realtime-voice": {
      "types": "./dist/plugin-sdk/realtime-voice.d.ts",
      "default": "./dist/plugin-sdk/realtime-voice.js"
    },
    "./plugin-sdk/media-understanding": {
      "types": "./dist/plugin-sdk/media-understanding.d.ts",
      "default": "./dist/plugin-sdk/media-understanding.js"
    },
    "./plugin-sdk/media-understanding-runtime": {
      "types": "./dist/plugin-sdk/media-understanding-runtime.d.ts",
      "default": "./dist/plugin-sdk/media-understanding-runtime.js"
    },
    "./plugin-sdk/messaging-targets": {
      "types": "./dist/plugin-sdk/messaging-targets.d.ts",
      "default": "./dist/plugin-sdk/messaging-targets.js"
    },
    "./plugin-sdk/request-url": {
      "types": "./dist/plugin-sdk/request-url.d.ts",
      "default": "./dist/plugin-sdk/request-url.js"
    },
    "./plugin-sdk/runtime-store": {
      "types": "./dist/plugin-sdk/runtime-store.d.ts",
      "default": "./dist/plugin-sdk/runtime-store.js"
    },
    "./plugin-sdk/json-store": {
      "types": "./dist/plugin-sdk/json-store.d.ts",
      "default": "./dist/plugin-sdk/json-store.js"
    },
    "./plugin-sdk/persistent-dedupe": {
      "types": "./dist/plugin-sdk/persistent-dedupe.d.ts",
      "default": "./dist/plugin-sdk/persistent-dedupe.js"
    },
    "./plugin-sdk/keyed-async-queue": {
      "types": "./dist/plugin-sdk/keyed-async-queue.d.ts",
      "default": "./dist/plugin-sdk/keyed-async-queue.js"
    },
    "./plugin-sdk/line": {
      "types": "./dist/plugin-sdk/line.d.ts",
      "default": "./dist/plugin-sdk/line.js"
    },
    "./plugin-sdk/line-core": {
      "types": "./dist/plugin-sdk/line-core.d.ts",
      "default": "./dist/plugin-sdk/line-core.js"
    },
    "./plugin-sdk/line-runtime": {
      "types": "./dist/plugin-sdk/line-runtime.d.ts",
      "default": "./dist/plugin-sdk/line-runtime.js"
    },
    "./plugin-sdk/line-surface": {
      "types": "./dist/plugin-sdk/line-surface.d.ts",
      "default": "./dist/plugin-sdk/line-surface.js"
    },
    "./plugin-sdk/llm-task": {
      "types": "./dist/plugin-sdk/llm-task.d.ts",
      "default": "./dist/plugin-sdk/llm-task.js"
    },
    "./plugin-sdk/matrix": {
      "types": "./dist/plugin-sdk/matrix.d.ts",
      "default": "./dist/plugin-sdk/matrix.js"
    },
    "./plugin-sdk/matrix-helper": {
      "types": "./dist/plugin-sdk/matrix-helper.d.ts",
      "default": "./dist/plugin-sdk/matrix-helper.js"
    },
    "./plugin-sdk/matrix-runtime-surface": {
      "types": "./dist/plugin-sdk/matrix-runtime-surface.d.ts",
      "default": "./dist/plugin-sdk/matrix-runtime-surface.js"
    },
    "./plugin-sdk/matrix-surface": {
      "types": "./dist/plugin-sdk/matrix-surface.d.ts",
      "default": "./dist/plugin-sdk/matrix-surface.js"
    },
    "./plugin-sdk/matrix-thread-bindings": {
      "types": "./dist/plugin-sdk/matrix-thread-bindings.d.ts",
      "default": "./dist/plugin-sdk/matrix-thread-bindings.js"
    },
    "./plugin-sdk/mattermost": {
      "types": "./dist/plugin-sdk/mattermost.d.ts",
      "default": "./dist/plugin-sdk/mattermost.js"
    },
    "./plugin-sdk/mattermost-policy": {
      "types": "./dist/plugin-sdk/mattermost-policy.d.ts",
      "default": "./dist/plugin-sdk/mattermost-policy.js"
    },
    "./plugin-sdk/memory-core": {
      "types": "./dist/plugin-sdk/memory-core.d.ts",
      "default": "./dist/plugin-sdk/memory-core.js"
    },
    "./plugin-sdk/memory-core-engine-runtime": {
      "types": "./dist/plugin-sdk/memory-core-engine-runtime.d.ts",
      "default": "./dist/plugin-sdk/memory-core-engine-runtime.js"
    },
    "./plugin-sdk/memory-core-host-engine-embeddings": {
      "types": "./dist/plugin-sdk/memory-core-host-engine-embeddings.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-engine-embeddings.js"
    },
    "./plugin-sdk/memory-core-host-engine-foundation": {
      "types": "./dist/plugin-sdk/memory-core-host-engine-foundation.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-engine-foundation.js"
    },
    "./plugin-sdk/memory-core-host-engine-qmd": {
      "types": "./dist/plugin-sdk/memory-core-host-engine-qmd.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-engine-qmd.js"
    },
    "./plugin-sdk/memory-core-host-engine-storage": {
      "types": "./dist/plugin-sdk/memory-core-host-engine-storage.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-engine-storage.js"
    },
    "./plugin-sdk/memory-core-host-multimodal": {
      "types": "./dist/plugin-sdk/memory-core-host-multimodal.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-multimodal.js"
    },
    "./plugin-sdk/memory-core-host-query": {
      "types": "./dist/plugin-sdk/memory-core-host-query.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-query.js"
    },
    "./plugin-sdk/memory-core-host-secret": {
      "types": "./dist/plugin-sdk/memory-core-host-secret.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-secret.js"
    },
    "./plugin-sdk/memory-core-host-events": {
      "types": "./dist/plugin-sdk/memory-core-host-events.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-events.js"
    },
    "./plugin-sdk/memory-core-host-status": {
      "types": "./dist/plugin-sdk/memory-core-host-status.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-status.js"
    },
    "./plugin-sdk/memory-core-host-runtime-cli": {
      "types": "./dist/plugin-sdk/memory-core-host-runtime-cli.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-runtime-cli.js"
    },
    "./plugin-sdk/memory-core-host-runtime-core": {
      "types": "./dist/plugin-sdk/memory-core-host-runtime-core.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-runtime-core.js"
    },
    "./plugin-sdk/memory-core-host-runtime-files": {
      "types": "./dist/plugin-sdk/memory-core-host-runtime-files.d.ts",
      "default": "./dist/plugin-sdk/memory-core-host-runtime-files.js"
    },
    "./plugin-sdk/memory-host-core": {
      "types": "./dist/plugin-sdk/memory-host-core.d.ts",
      "default": "./dist/plugin-sdk/memory-host-core.js"
    },
    "./plugin-sdk/memory-host-events": {
      "types": "./dist/plugin-sdk/memory-host-events.d.ts",
      "default": "./dist/plugin-sdk/memory-host-events.js"
    },
    "./plugin-sdk/memory-host-files": {
      "types": "./dist/plugin-sdk/memory-host-files.d.ts",
      "default": "./dist/plugin-sdk/memory-host-files.js"
    },
    "./plugin-sdk/memory-host-markdown": {
      "types": "./dist/plugin-sdk/memory-host-markdown.d.ts",
      "default": "./dist/plugin-sdk/memory-host-markdown.js"
    },
    "./plugin-sdk/memory-host-search": {
      "types": "./dist/plugin-sdk/memory-host-search.d.ts",
      "default": "./dist/plugin-sdk/memory-host-search.js"
    },
    "./plugin-sdk/memory-host-status": {
      "types": "./dist/plugin-sdk/memory-host-status.d.ts",
      "default": "./dist/plugin-sdk/memory-host-status.js"
    },
    "./plugin-sdk/memory-lancedb": {
      "types": "./dist/plugin-sdk/memory-lancedb.d.ts",
      "default": "./dist/plugin-sdk/memory-lancedb.js"
    },
    "./plugin-sdk/msteams": {
      "types": "./dist/plugin-sdk/msteams.d.ts",
      "default": "./dist/plugin-sdk/msteams.js"
    },
    "./plugin-sdk/models-provider-runtime": {
      "types": "./dist/plugin-sdk/models-provider-runtime.d.ts",
      "default": "./dist/plugin-sdk/models-provider-runtime.js"
    },
    "./plugin-sdk/skill-commands-runtime": {
      "types": "./dist/plugin-sdk/skill-commands-runtime.d.ts",
      "default": "./dist/plugin-sdk/skill-commands-runtime.js"
    },
    "./plugin-sdk/native-command-registry": {
      "types": "./dist/plugin-sdk/native-command-registry.d.ts",
      "default": "./dist/plugin-sdk/native-command-registry.js"
    },
    "./plugin-sdk/nextcloud-talk": {
      "types": "./dist/plugin-sdk/nextcloud-talk.d.ts",
      "default": "./dist/plugin-sdk/nextcloud-talk.js"
    },
    "./plugin-sdk/nostr": {
      "types": "./dist/plugin-sdk/nostr.d.ts",
      "default": "./dist/plugin-sdk/nostr.js"
    },
    "./plugin-sdk/qa-channel": {
      "types": "./dist/plugin-sdk/qa-channel.d.ts",
      "default": "./dist/plugin-sdk/qa-channel.js"
    },
    "./plugin-sdk/provider-auth": {
      "types": "./dist/plugin-sdk/provider-auth.d.ts",
      "default": "./dist/plugin-sdk/provider-auth.js"
    },
    "./plugin-sdk/provider-auth-runtime": {
      "types": "./dist/plugin-sdk/provider-auth-runtime.d.ts",
      "default": "./dist/plugin-sdk/provider-auth-runtime.js"
    },
    "./plugin-sdk/provider-auth-api-key": {
      "types": "./dist/plugin-sdk/provider-auth-api-key.d.ts",
      "default": "./dist/plugin-sdk/provider-auth-api-key.js"
    },
    "./plugin-sdk/provider-auth-result": {
      "types": "./dist/plugin-sdk/provider-auth-result.d.ts",
      "default": "./dist/plugin-sdk/provider-auth-result.js"
    },
    "./plugin-sdk/provider-auth-login": {
      "types": "./dist/plugin-sdk/provider-auth-login.d.ts",
      "default": "./dist/plugin-sdk/provider-auth-login.js"
    },
    "./plugin-sdk/plugin-entry": {
      "types": "./dist/plugin-sdk/plugin-entry.d.ts",
      "default": "./dist/plugin-sdk/plugin-entry.js"
    },
    "./plugin-sdk/provider-catalog-shared": {
      "types": "./dist/plugin-sdk/provider-catalog-shared.d.ts",
      "default": "./dist/plugin-sdk/provider-catalog-shared.js"
    },
    "./plugin-sdk/provider-entry": {
      "types": "./dist/plugin-sdk/provider-entry.d.ts",
      "default": "./dist/plugin-sdk/provider-entry.js"
    },
    "./plugin-sdk/provider-env-vars": {
      "types": "./dist/plugin-sdk/provider-env-vars.d.ts",
      "default": "./dist/plugin-sdk/provider-env-vars.js"
    },
    "./plugin-sdk/provider-http": {
      "types": "./dist/plugin-sdk/provider-http.d.ts",
      "default": "./dist/plugin-sdk/provider-http.js"
    },
    "./plugin-sdk/provider-model-types": {
      "types": "./dist/plugin-sdk/provider-model-types.d.ts",
      "default": "./dist/plugin-sdk/provider-model-types.js"
    },
    "./plugin-sdk/provider-model-shared": {
      "types": "./dist/plugin-sdk/provider-model-shared.d.ts",
      "default": "./dist/plugin-sdk/provider-model-shared.js"
    },
    "./plugin-sdk/volc-model-catalog-shared": {
      "types": "./dist/plugin-sdk/volc-model-catalog-shared.d.ts",
      "default": "./dist/plugin-sdk/volc-model-catalog-shared.js"
    },
    "./plugin-sdk/provider-onboard": {
      "types": "./dist/plugin-sdk/provider-onboard.d.ts",
      "default": "./dist/plugin-sdk/provider-onboard.js"
    },
    "./plugin-sdk/provider-stream-family": {
      "types": "./dist/plugin-sdk/provider-stream-family.d.ts",
      "default": "./dist/plugin-sdk/provider-stream-family.js"
    },
    "./plugin-sdk/provider-stream-shared": {
      "types": "./dist/plugin-sdk/provider-stream-shared.d.ts",
      "default": "./dist/plugin-sdk/provider-stream-shared.js"
    },
    "./plugin-sdk/provider-stream": {
      "types": "./dist/plugin-sdk/provider-stream.d.ts",
      "default": "./dist/plugin-sdk/provider-stream.js"
    },
    "./plugin-sdk/provider-tools": {
      "types": "./dist/plugin-sdk/provider-tools.d.ts",
      "default": "./dist/plugin-sdk/provider-tools.js"
    },
    "./plugin-sdk/provider-usage": {
      "types": "./dist/plugin-sdk/provider-usage.d.ts",
      "default": "./dist/plugin-sdk/provider-usage.js"
    },
    "./plugin-sdk/provider-web-fetch-contract": {
      "types": "./dist/plugin-sdk/provider-web-fetch-contract.d.ts",
      "default": "./dist/plugin-sdk/provider-web-fetch-contract.js"
    },
    "./plugin-sdk/provider-web-fetch": {
      "types": "./dist/plugin-sdk/provider-web-fetch.d.ts",
      "default": "./dist/plugin-sdk/provider-web-fetch.js"
    },
    "./plugin-sdk/provider-web-search-config-contract": {
      "types": "./dist/plugin-sdk/provider-web-search-config-contract.d.ts",
      "default": "./dist/plugin-sdk/provider-web-search-config-contract.js"
    },
    "./plugin-sdk/provider-web-search-contract": {
      "types": "./dist/plugin-sdk/provider-web-search-contract.d.ts",
      "default": "./dist/plugin-sdk/provider-web-search-contract.js"
    },
    "./plugin-sdk/provider-web-search": {
      "types": "./dist/plugin-sdk/provider-web-search.d.ts",
      "default": "./dist/plugin-sdk/provider-web-search.js"
    },
    "./plugin-sdk/retry-runtime": {
      "types": "./dist/plugin-sdk/retry-runtime.d.ts",
      "default": "./dist/plugin-sdk/retry-runtime.js"
    },
    "./plugin-sdk/run-command": {
      "types": "./dist/plugin-sdk/run-command.d.ts",
      "default": "./dist/plugin-sdk/run-command.js"
    },
    "./plugin-sdk/param-readers": {
      "types": "./dist/plugin-sdk/param-readers.d.ts",
      "default": "./dist/plugin-sdk/param-readers.js"
    },
    "./plugin-sdk/provider-zai-endpoint": {
      "types": "./dist/plugin-sdk/provider-zai-endpoint.d.ts",
      "default": "./dist/plugin-sdk/provider-zai-endpoint.js"
    },
    "./plugin-sdk/secret-input": {
      "types": "./dist/plugin-sdk/secret-input.d.ts",
      "default": "./dist/plugin-sdk/secret-input.js"
    },
    "./plugin-sdk/channel-status": {
      "types": "./dist/plugin-sdk/channel-status.d.ts",
      "default": "./dist/plugin-sdk/channel-status.js"
    },
    "./plugin-sdk/status-helpers": {
      "types": "./dist/plugin-sdk/status-helpers.d.ts",
      "default": "./dist/plugin-sdk/status-helpers.js"
    },
    "./plugin-sdk/speech": {
      "types": "./dist/plugin-sdk/speech.d.ts",
      "default": "./dist/plugin-sdk/speech.js"
    },
    "./plugin-sdk/session-store-runtime": {
      "types": "./dist/plugin-sdk/session-store-runtime.d.ts",
      "default": "./dist/plugin-sdk/session-store-runtime.js"
    },
    "./plugin-sdk/string-normalization-runtime": {
      "types": "./dist/plugin-sdk/string-normalization-runtime.d.ts",
      "default": "./dist/plugin-sdk/string-normalization-runtime.js"
    },
    "./plugin-sdk/state-paths": {
      "types": "./dist/plugin-sdk/state-paths.d.ts",
      "default": "./dist/plugin-sdk/state-paths.js"
    },
    "./plugin-sdk/target-resolver-runtime": {
      "types": "./dist/plugin-sdk/target-resolver-runtime.d.ts",
      "default": "./dist/plugin-sdk/target-resolver-runtime.js"
    },
    "./plugin-sdk/telegram-command-config": {
      "types": "./dist/plugin-sdk/telegram-command-config.d.ts",
      "default": "./dist/plugin-sdk/telegram-command-config.js"
    },
    "./plugin-sdk/thread-ownership": {
      "types": "./dist/plugin-sdk/thread-ownership.d.ts",
      "default": "./dist/plugin-sdk/thread-ownership.js"
    },
    "./plugin-sdk/tlon": {
      "types": "./dist/plugin-sdk/tlon.d.ts",
      "default": "./dist/plugin-sdk/tlon.js"
    },
    "./plugin-sdk/tool-payload": {
      "types": "./dist/plugin-sdk/tool-payload.d.ts",
      "default": "./dist/plugin-sdk/tool-payload.js"
    },
    "./plugin-sdk/tool-send": {
      "types": "./dist/plugin-sdk/tool-send.d.ts",
      "default": "./dist/plugin-sdk/tool-send.js"
    },
    "./plugin-sdk/twitch": {
      "types": "./dist/plugin-sdk/twitch.d.ts",
      "default": "./dist/plugin-sdk/twitch.js"
    },
    "./plugin-sdk/webhook-ingress": {
      "types": "./dist/plugin-sdk/webhook-ingress.d.ts",
      "default": "./dist/plugin-sdk/webhook-ingress.js"
    },
    "./plugin-sdk/webhook-targets": {
      "types": "./dist/plugin-sdk/webhook-targets.d.ts",
      "default": "./dist/plugin-sdk/webhook-targets.js"
    },
    "./plugin-sdk/webhook-request-guards": {
      "types": "./dist/plugin-sdk/webhook-request-guards.d.ts",
      "default": "./dist/plugin-sdk/webhook-request-guards.js"
    },
    "./plugin-sdk/webhook-path": {
      "types": "./dist/plugin-sdk/webhook-path.d.ts",
      "default": "./dist/plugin-sdk/webhook-path.js"
    },
    "./plugin-sdk/web-media": {
      "types": "./dist/plugin-sdk/web-media.d.ts",
      "default": "./dist/plugin-sdk/web-media.js"
    },
    "./plugin-sdk/voice-call": {
      "types": "./dist/plugin-sdk/voice-call.d.ts",
      "default": "./dist/plugin-sdk/voice-call.js"
    },
    "./plugin-sdk/zalo": {
      "types": "./dist/plugin-sdk/zalo.d.ts",
      "default": "./dist/plugin-sdk/zalo.js"
    },
    "./plugin-sdk/zalo-setup": {
      "types": "./dist/plugin-sdk/zalo-setup.d.ts",
      "default": "./dist/plugin-sdk/zalo-setup.js"
    },
    "./plugin-sdk/zalouser": {
      "types": "./dist/plugin-sdk/zalouser.d.ts",
      "default": "./dist/plugin-sdk/zalouser.js"
    },
    "./plugin-sdk/zod": {
      "types": "./dist/plugin-sdk/zod.d.ts",
      "default": "./dist/plugin-sdk/zod.js"
    },
    "./extension-api": "./dist/extensionAPI.js",
    "./cli-entry": "./openclaw.mjs"
  },
  "scripts": {
    "android:assemble": "cd apps/android && ./gradlew :app:assemblePlayDebug",
    "android:assemble:third-party": "cd apps/android && ./gradlew :app:assembleThirdPartyDebug",
    "android:bundle:release": "bun apps/android/scripts/build-release-aab.ts",
    "android:format": "cd apps/android && ./gradlew :app:ktlintFormat :benchmark:ktlintFormat",
    "android:install": "cd apps/android && ./gradlew :app:installPlayDebug",
    "android:install:third-party": "cd apps/android && ./gradlew :app:installThirdPartyDebug",
    "android:lint": "cd apps/android && ./gradlew :app:ktlintCheck :benchmark:ktlintCheck",
    "android:lint:android": "cd apps/android && ./gradlew :app:lintDebug",
    "android:run": "cd apps/android && ./gradlew :app:installPlayDebug && adb shell am start -n ai.openclaw.app/.MainActivity",
    "android:run:third-party": "cd apps/android && ./gradlew :app:installThirdPartyDebug && adb shell am start -n ai.openclaw.app/.MainActivity",
    "android:test": "cd apps/android && ./gradlew :app:testPlayDebugUnitTest",
    "android:test:integration": "OPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_ANDROID_NODE=1 node scripts/run-vitest.mjs run --config test/vitest/vitest.live.config.ts src/gateway/android-node.capabilities.live.test.ts",
    "android:test:third-party": "cd apps/android && ./gradlew :app:testThirdPartyDebugUnitTest",
    "audit:seams": "node scripts/audit-seams.mjs",
    "build": "node scripts/build-all.mjs",
    "build:docker": "node scripts/tsdown-build.mjs && node scripts/runtime-postbuild.mjs && node scripts/build-stamp.mjs && node --import tsx scripts/canvas-a2ui-copy.ts && node --import tsx scripts/copy-hook-metadata.ts && node --import tsx scripts/copy-export-html-templates.ts && node --import tsx scripts/write-build-info.ts && node --experimental-strip-types scripts/write-cli-startup-metadata.ts && node --import tsx scripts/write-cli-compat.ts",
    "build:plugin-sdk:dts": "tsc -p tsconfig.plugin-sdk.dts.json",
    "build:strict-smoke": "pnpm canvas:a2ui:bundle && node scripts/tsdown-build.mjs && node scripts/runtime-postbuild.mjs && node scripts/build-stamp.mjs && pnpm build:plugin-sdk:dts && node --import tsx scripts/write-plugin-sdk-entry-dts.ts && node scripts/check-plugin-sdk-exports.mjs",
    "canon:check": "node scripts/canon.mjs check",
    "canon:check:json": "node scripts/canon.mjs check --json",
    "canon:enforce": "node scripts/canon.mjs enforce --json",
    "canvas:a2ui:bundle": "node scripts/bundle-a2ui.mjs",
    "check": "pnpm check:no-conflict-markers && pnpm tool-display:check && pnpm check:host-env-policy:swift && pnpm check:import-cycles && pnpm check:static-import-sccs && pnpm tsgo && node scripts/prepare-extension-package-boundary-artifacts.mjs && pnpm lint && pnpm lint:webhook:no-low-level-body-read && pnpm lint:auth:no-pairing-store-group && pnpm lint:auth:pairing-account-scope",
    "check:base-config-schema": "node --import tsx scripts/generate-base-config-schema.ts --check",
    "check:bundled-channel-config-metadata": "node --import tsx scripts/generate-bundled-channel-config-metadata.ts --check",
    "check:docs": "pnpm format:docs:check && pnpm lint:docs && pnpm docs:check-i18n-glossary && pnpm docs:check-links",
    "check:host-env-policy:swift": "node scripts/generate-host-env-security-policy-swift.mjs --check",
    "check:import-cycles": "node --import tsx scripts/check-import-cycles.ts",
    "check:loc": "node --import tsx scripts/check-ts-max-loc.ts --max 500",
    "check:no-conflict-markers": "node scripts/check-no-conflict-markers.mjs",
    "check:static-import-sccs": "node --import tsx scripts/check-static-import-sccs.ts",
    "codex-app-server:protocol:check": "node --import tsx scripts/check-codex-app-server-protocol.ts",
    "config:channels:check": "node --import tsx scripts/generate-bundled-channel-config-metadata.ts --check",
    "config:channels:gen": "node --import tsx scripts/generate-bundled-channel-config-metadata.ts --write",
    "config:docs:check": "node --import tsx scripts/generate-config-doc-baseline.ts --check",
    "config:docs:gen": "node --import tsx scripts/generate-config-doc-baseline.ts --write",
    "config:schema:check": "node --import tsx scripts/generate-base-config-schema.ts --check",
    "config:schema:gen": "node --import tsx scripts/generate-base-config-schema.ts --write",
    "deadcode:ci": "pnpm deadcode:report:ci:knip",
    "deadcode:knip": "pnpm dlx knip --config knip.config.ts --production --no-progress --reporter compact --files --dependencies",
    "deadcode:report": "pnpm deadcode:knip; pnpm deadcode:ts-prune; pnpm deadcode:ts-unused",
    "deadcode:report:ci:knip": "mkdir -p .artifacts/deadcode && pnpm deadcode:knip > .artifacts/deadcode/knip.txt 2>&1 || true",
    "deadcode:report:ci:ts-prune": "mkdir -p .artifacts/deadcode && pnpm deadcode:ts-prune > .artifacts/deadcode/ts-prune.txt 2>&1 || true",
    "deadcode:report:ci:ts-unused": "mkdir -p .artifacts/deadcode && pnpm deadcode:ts-unused > .artifacts/deadcode/ts-unused-exports.txt 2>&1 || true",
    "deadcode:ts-prune": "pnpm dlx ts-prune src extensions scripts",
    "deadcode:ts-unused": "pnpm dlx ts-unused-exports tsconfig.json --ignoreTestFiles --exitWithCount",
    "dev": "node scripts/run-node.mjs",
    "docs:bin": "node scripts/build-docs-list.mjs",
    "docs:check-i18n-glossary": "node scripts/check-docs-i18n-glossary.mjs",
    "docs:check-links": "node scripts/docs-link-audit.mjs",
    "docs:check-links:anchors": "node scripts/docs-link-audit.mjs --anchors",
    "docs:dev": "cd docs && mint dev",
    "docs:list": "node scripts/docs-list.js",
    "docs:spellcheck": "bash scripts/docs-spellcheck.sh",
    "docs:spellcheck:fix": "bash scripts/docs-spellcheck.sh --write",
    "dup:check": "jscpd src extensions test scripts --format typescript,javascript --pattern \"**/*.{ts,tsx,js,mjs,cjs}\" --gitignore --noSymlinks --ignore \"**/node_modules/**,**/dist/**,**/.git/**,**/coverage/**,**/build/**,**/.build/**,**/.artifacts/**\" --min-lines 12 --min-tokens 80 --reporters console",
    "dup:check:json": "jscpd src extensions test scripts --format typescript,javascript --pattern \"**/*.{ts,tsx,js,mjs,cjs}\" --gitignore --noSymlinks --ignore \"**/node_modules/**,**/dist/**,**/.git/**,**/coverage/**,**/build/**,**/.build/**,**/.artifacts/**\" --min-lines 12 --min-tokens 80 --reporters json --output .artifacts/jscpd",
    "format": "oxfmt --write",
    "format:all": "pnpm format && pnpm format:swift",
    "format:check":
```

### `pnpm-workspace.yaml`

- Source path: `pnpm-workspace.yaml`
- Truncated: `no`

```yaml
packages:
  - .
  - ui
  - packages/*
  - extensions/*

minimumReleaseAge: 2880

minimumReleaseAgeExclude:
  - "acpx"
  - "axios"
  - "basic-ftp"
  - "hono"
  - "openclaw"
  - "@buape/carbon"
  - "vite"
  - "@cloudflare/workers-types"
  - "@hono/node-server"
  - "@mariozechner/*"
  - "@typescript/native-preview*"
  - "@types/node"
  - "@rolldown/*"
  - "@oxlint/*"
  - "@oxfmt/*"
  - "axios@1.15.0"
  - "discord-api-types"
  - "rolldown"
  - "sqlite-vec"
  - "sqlite-vec-*"

onlyBuiltDependencies:
  - "@discordjs/opus"
  - "@lydell/node-pty"
  - "@matrix-org/matrix-sdk-crypto-nodejs"
  - "@napi-rs/canvas"
  - "@tloncorp/api"
  - "@whiskeysockets/baileys"
  - authenticate-pam
  - esbuild
  - node-llama-cpp
  - protobufjs
  - sharp

ignoredBuiltDependencies:
  - koffi
```

### `pyproject.toml`

- Source path: `pyproject.toml`
- Truncated: `no`

```toml
[tool.ruff]
target-version = "py310"
line-length = 100

[tool.ruff.lint]
select = ["E9", "F63", "F7", "F82", "I"]

[tool.pytest.ini_options]
testpaths = ["skills"]
python_files = ["test_*.py"]
```
