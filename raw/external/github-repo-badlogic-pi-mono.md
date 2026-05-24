---
title: "GitHub repo snapshot: badlogic/pi-mono"
source: "https://github.com/badlogic/pi-mono"
author:
published:
created: 2026-04-10
description: "Compact GitHub repository evidence snapshot for repo-map-ingest."
tags:
  - "github"
  - "repo-snapshot"
---

# GitHub Repo Snapshot: `badlogic/pi-mono`

## Observation Scope

- Repository: `badlogic/pi-mono`
- URL: https://github.com/badlogic/pi-mono
- Requested topic: coding agent 架构与工程实践
- Observed ref: `main`
- Latest resolved commit: `3b7448d156aab5af1e21fd9ab45d19e4f10865a8`
- Commit date: `2026-04-09T01:33:09Z`
- Snapshot date (UTC): `2026-04-10`

## Repository Metadata

- Description: AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods
- Default branch: `main`
- Language: `TypeScript`
- Stars: `33877`
- Forks: `3826`
- Open issues: `18`

## Top-Level Tree

### Directories

- `.github`
- `.husky`
- `.pi`
- `packages`
- `scripts`

### Files

- `.gitattributes`
- `.gitignore`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `README.md`
- `biome.json`
- `package-lock.json`
- `package.json`
- `pi-test.sh`
- `test.sh`
- `tsconfig.base.json`
- `tsconfig.json`

## Selected Evidence Anchors

- `.github/workflows/approve-contributor.yml`
- `.github/workflows/build-binaries.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/openclaw-gate.yml`
- `.github/workflows/oss-weekend-issues.yml`
- `.github/workflows/pr-gate.yml`
- `AGENTS.md`
- `README.md`
- `package.json`

## Captured Files

### `.github/workflows/approve-contributor.yml`

- Source path: `.github/workflows/approve-contributor.yml`
- Truncated: `no`

```yaml
name: Approve Contributor

on:
  issue_comment:
    types: [created]

jobs:
  approve:
    if: ${{ !github.event.issue.pull_request }}
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: write
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.repository.default_branch }}

      - name: Add contributor to approved list
        id: update
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');

            const issueAuthor = context.payload.issue.user.login;
            const commenter = context.payload.comment.user.login;
            const commentBody = context.payload.comment.body || '';
            const approvedFile = '.github/APPROVED_CONTRIBUTORS';

            if (!/^\s*lgtm\b/i.test(commentBody)) {
              console.log('Comment does not match lgtm');
              core.setOutput('status', 'skipped');
              return;
            }

            try {
              const { data: permissionLevel } = await github.rest.repos.getCollaboratorPermissionLevel({
                owner: context.repo.owner,
                repo: context.repo.repo,
                username: commenter
              });

              if (!['admin', 'write'].includes(permissionLevel.permission)) {
                console.log(`${commenter} does not have write access`);
                core.setOutput('status', 'skipped');
                return;
              }
            } catch (error) {
              console.log(`${commenter} does not have collaborator access`);
              core.setOutput('status', 'skipped');
              return;
            }

            let content = fs.readFileSync(approvedFile, 'utf8');
            const approvedList = content
              .split('\n')
              .map(line => line.trim().toLowerCase())
              .filter(line => line && !line.startsWith('#'));

            if (approvedList.includes(issueAuthor.toLowerCase())) {
              console.log(`${issueAuthor} is already approved`);
              core.setOutput('status', 'already');
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.issue.number,
                body: `@${issueAuthor} is already in the approved contributors list.`
              });
              return;
            }

            content = content.trimEnd() + '\n' + issueAuthor + '\n';
            fs.writeFileSync(approvedFile, content);

            console.log(`Added ${issueAuthor} to approved contributors`);
            core.setOutput('status', 'added');

      - name: Commit and push
        if: steps.update.outputs.status == 'added'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add .github/APPROVED_CONTRIBUTORS
          git diff --staged --quiet || git commit -m "chore: approve contributor ${{ github.event.issue.user.login }}"
          git push

      - name: Comment on issue
        if: steps.update.outputs.status == 'added'
        uses: actions/github-script@v7
        with:
          script: |
            const issueAuthor = context.payload.issue.user.login;
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: `@${issueAuthor} has been added to the approved contributors list. You can now submit PRs. Thanks for contributing!`
            });
```

### `.github/workflows/build-binaries.yml`

- Source path: `.github/workflows/build-binaries.yml`
- Truncated: `no`

```yaml
name: Build Binaries

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:
    inputs:
      tag:
        description: 'Tag to build (e.g., v0.12.0)'
        required: true
        type: string

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      RELEASE_TAG: ${{ github.event.inputs.tag || github.ref_name }}
    steps:
      - name: Checkout
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
        with:
          ref: ${{ env.RELEASE_TAG }}

      - name: Setup Bun
        uses: oven-sh/setup-bun@4bc047ad259df6fc24a6c9b0f9a0cb08cf17fbe5 # v2.0.1
        with:
          bun-version: 1.2.20

      - name: Setup Node.js
        uses: actions/setup-node@39370e3970a6d050c480ffad4ff0ed4d3fdee5af # v4.1.0
        with:
          node-version: '22'
          registry-url: 'https://registry.npmjs.org'

      - name: Build binaries
        run: ./scripts/build-binaries.sh

      - name: Extract changelog for this version
        id: changelog
        run: |
          VERSION="${RELEASE_TAG}"
          VERSION="${VERSION#v}"  # Remove 'v' prefix
          
          # Extract changelog section for this version
          cd packages/coding-agent
          awk "/^## \[${VERSION}\]/{flag=1; next} /^## \[/{flag=0} flag" CHANGELOG.md > /tmp/release-notes.md
          
          # If empty, use a default message
          if [ ! -s /tmp/release-notes.md ]; then
            echo "Release ${VERSION}" > /tmp/release-notes.md
          fi

      - name: Create GitHub Release and upload binaries
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          cd packages/coding-agent/binaries
          
          # Create release with changelog notes (or update if exists)
          gh release create "${RELEASE_TAG}" \
            --title "${RELEASE_TAG}" \
            --notes-file /tmp/release-notes.md \
            pi-darwin-arm64.tar.gz \
            pi-darwin-x64.tar.gz \
            pi-linux-x64.tar.gz \
            pi-linux-arm64.tar.gz \
            pi-windows-x64.zip \
            2>/dev/null || \
          gh release upload "${RELEASE_TAG}" \
            pi-darwin-arm64.tar.gz \
            pi-darwin-x64.tar.gz \
            pi-linux-x64.tar.gz \
            pi-linux-arm64.tar.gz \
            pi-windows-x64.zip \
            --clobber
```

### `.github/workflows/ci.yml`

- Source path: `.github/workflows/ci.yml`
- Truncated: `no`

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

jobs:
  build-check-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y libcairo2-dev libpango1.0-dev libjpeg-dev libgif-dev librsvg2-dev fd-find ripgrep
          sudo ln -s $(which fdfind) /usr/local/bin/fd

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Check
        run: npm run check

      - name: Test
        run: npm test
```

### `.github/workflows/openclaw-gate.yml`

- Source path: `.github/workflows/openclaw-gate.yml`
- Truncated: `no`

```yaml
name: OpenClaw Gate

on:
  issues:
    types: [opened]
  pull_request_target:
    types: [opened]

jobs:
  check-contributor:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
      pull-requests: write
    steps:
      - name: Check contributor
        uses: actions/github-script@v7
        with:
          script: |
            const isPR = !!context.payload.pull_request;
            const author = isPR
              ? context.payload.pull_request.user.login
              : context.payload.issue.user.login;
            const number = isPR
              ? context.payload.pull_request.number
              : context.payload.issue.number;
            const defaultBranch = context.payload.repository.default_branch;

            if (author.endsWith('[bot]') || author === 'dependabot[bot]') {
              console.log(`Skipping bot: ${author}`);
              return;
            }

            // --- Check APPROVED_CONTRIBUTORS ---
            async function getTextFile(path) {
              const { data } = await github.rest.repos.getContent({
                owner: context.repo.owner,
                repo: context.repo.repo,
                path,
                ref: defaultBranch,
              });
              if (!('content' in data) || typeof data.content !== 'string') {
                throw new Error(`Expected file content for ${path}`);
              }
              return Buffer.from(data.content, 'base64').toString('utf8');
            }

            try {
              const content = await getTextFile('.github/APPROVED_CONTRIBUTORS');
              const approved = content
                .split('\n')
                .map(l => l.trim().toLowerCase())
                .filter(l => l && !l.startsWith('#'));
              if (approved.includes(author.toLowerCase())) {
                console.log(`${author} is in APPROVED_CONTRIBUTORS, passing`);
                return;
              }
            } catch (err) {
              console.log(`Could not read APPROVED_CONTRIBUTORS: ${err.message}`);
            }

            // --- Also pass collaborators with write+ access ---
            try {
              const { data: perm } = await github.rest.repos.getCollaboratorPermissionLevel({
                owner: context.repo.owner,
                repo: context.repo.repo,
                username: author,
              });
              if (['admin', 'maintain', 'write'].includes(perm.permission)) {
                console.log(`${author} is a collaborator (${perm.permission}), passing`);
                return;
              }
            } catch {
              // not a collaborator
            }

            // --- Check if user opened issues/PRs on openclaw/openclaw ---
            async function hasOpenClawActivity(username) {
              try {
                const { data } = await github.rest.search.issuesAndPullRequests({
                  q: `repo:openclaw/openclaw author:${username}`,
                  per_page: 1,
                });
                if (data.total_count > 0) {
                  console.log(`${username} has opened ${data.total_count} issues/PRs on openclaw/openclaw`);
                  return true;
                }
              } catch (err) {
                console.log(`Search failed: ${err.message}`);
              }
              return false;
            }

            const hasActivity = await hasOpenClawActivity(author);
            if (!hasActivity) {
              console.log(`${author} has no openclaw/openclaw activity, passing`);
              return;
            }

            // --- Add openclaw label ---
            console.log(`${author} has openclaw/openclaw activity, adding label`);
            await github.rest.issues.addLabels({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: number,
              labels: ['possibly-openclaw-clanker'],
            });
```

### `.github/workflows/oss-weekend-issues.yml`

- Source path: `.github/workflows/oss-weekend-issues.yml`
- Truncated: `no`

```yaml
name: OSS Weekend Issues

on:
  issues:
    types: [opened]

jobs:
  close-issues-during-weekend:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
    steps:
      - name: Close new issues during OSS weekend
        uses: actions/github-script@v7
        with:
          script: |
            const issueAuthor = context.payload.issue.user.login;
            const defaultBranch = context.payload.repository.default_branch;

            if (issueAuthor.endsWith('[bot]') || issueAuthor === 'dependabot[bot]') {
              console.log(`Skipping bot: ${issueAuthor}`);
              return;
            }

            async function getPermission(username) {
              try {
                const { data: permissionLevel } = await github.rest.repos.getCollaboratorPermissionLevel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  username,
                });
                return permissionLevel.permission;
              } catch {
                return null;
              }
            }

            async function getTextFile(path) {
              const { data: fileContent } = await github.rest.repos.getContent({
                owner: context.repo.owner,
                repo: context.repo.repo,
                path,
                ref: defaultBranch,
              });

              if (!('content' in fileContent) || typeof fileContent.content !== 'string') {
                throw new Error(`Expected file content for ${path}`);
              }

              return Buffer.from(fileContent.content, 'base64').toString('utf8');
            }

            const permission = await getPermission(issueAuthor);
            if (['admin', 'maintain', 'write'].includes(permission)) {
              console.log(`${issueAuthor} is a collaborator with ${permission} access`);
              return;
            }

            const approvedContent = await getTextFile('.github/APPROVED_CONTRIBUTORS');
            const approvedList = approvedContent
              .split('\n')
              .map(line => line.trim().toLowerCase())
              .filter(line => line && !line.startsWith('#'));
            const isApprovedContributor = approvedList.includes(issueAuthor.toLowerCase());

            let weekendState;
            try {
              weekendState = JSON.parse(await getTextFile('.github/oss-weekend.json'));
            } catch (error) {
              if (error && typeof error === 'object' && 'status' in error && error.status === 404) {
                console.log('OSS weekend is not active');
                return;
              }
              throw error;
            }

            if (!weekendState?.active) {
              console.log('OSS weekend is not active');
              return;
            }

            if (isApprovedContributor) {
              console.log(`${issueAuthor} is in the approved contributors list`);
              return;
            }

            const reopenDate = weekendState.reopensOnText || weekendState.reopensOn || 'after the weekend';
            const discordUrl = weekendState.discordUrl || 'https://discord.com/invite/3cU7Bz4UPx';
            const reason = typeof weekendState.reason === 'string' && weekendState.reason.trim() ? weekendState.reason.trim() : null;
            const message = [
              `Hi @${issueAuthor}, thanks for opening an issue.`,
              '',
              `OSS weekend is active until ${reopenDate}, so new issues from unapproved contributors are being auto-closed for now.`,
              ...(reason ? ['', `Current focus: ${reason}`] : []),
              '',
              `Please reopen or submit this issue again after ${reopenDate}. For support, join [Discord](${discordUrl}).`,
            ].join('\n');

            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: message,
            });

            await github.rest.issues.update({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              state: 'closed',
            });
```

### `.github/workflows/pr-gate.yml`

- Source path: `.github/workflows/pr-gate.yml`
- Truncated: `no`

```yaml
name: PR Gate

on:
  pull_request_target:
    types: [opened]

jobs:
  check-contributor:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
      pull-requests: write
    steps:
      - name: Check if contributor is approved
        uses: actions/github-script@v7
        with:
          script: |
            const prAuthor = context.payload.pull_request.user.login;
            const defaultBranch = context.payload.repository.default_branch;

            if (prAuthor.endsWith('[bot]') || prAuthor === 'dependabot[bot]') {
              console.log(`Skipping bot: ${prAuthor}`);
              return;
            }

            async function getPermission(username) {
              try {
                const { data: permissionLevel } = await github.rest.repos.getCollaboratorPermissionLevel({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  username,
                });
                return permissionLevel.permission;
              } catch {
                return null;
              }
            }

            async function getTextFile(path) {
              const { data: fileContent } = await github.rest.repos.getContent({
                owner: context.repo.owner,
                repo: context.repo.repo,
                path,
                ref: defaultBranch,
              });

              if (!('content' in fileContent) || typeof fileContent.content !== 'string') {
                throw new Error(`Expected file content for ${path}`);
              }

              return Buffer.from(fileContent.content, 'base64').toString('utf8');
            }

            async function closePullRequest(message) {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.payload.pull_request.number,
                body: message,
              });

              await github.rest.pulls.update({
                owner: context.repo.owner,
                repo: context.repo.repo,
                pull_number: context.payload.pull_request.number,
                state: 'closed',
              });
            }

            const permission = await getPermission(prAuthor);
            if (['admin', 'maintain', 'write'].includes(permission)) {
              console.log(`${prAuthor} is a collaborator with ${permission} access`);
              return;
            }

            const approvedContent = await getTextFile('.github/APPROVED_CONTRIBUTORS');
            const approvedList = approvedContent
              .split('\n')
              .map(line => line.trim().toLowerCase())
              .filter(line => line && !line.startsWith('#'));
            const isApprovedContributor = approvedList.includes(prAuthor.toLowerCase());

            if (isApprovedContributor) {
              console.log(`${prAuthor} is in the approved contributors list`);
              return;
            }

            console.log(`${prAuthor} is not approved, closing PR`);

            const message = [
              `Hi @${prAuthor}, thanks for your interest in contributing!`,
              '',
              'We ask new contributors to open an issue first before submitting a PR. This helps us discuss the approach and avoid wasted effort.',
              '',
              '**Next steps:**',
              '1. Open an issue describing what you want to change and why (keep it concise, write in your human voice, AI slop will be closed)',
              '2. Once a maintainer approves with `lgtm`, you\'ll be added to the approved contributors list',
              '3. Then you can submit your PR',
              '',
              `This PR will be closed automatically. See https://github.com/${context.repo.owner}/${context.repo.repo}/blob/${defaultBranch}/CONTRIBUTING.md for more details.`,
            ].join('\n');

            await closePullRequest(message);
```

### `AGENTS.md`

- Source path: `AGENTS.md`
- Truncated: `no`

```md
# Development Rules

## First Message
If the user did not give you a concrete task in their first message,
read README.md, then ask which module(s) to work on. Based on the answer, read the relevant README.md files in parallel.
- packages/ai/README.md
- packages/tui/README.md
- packages/agent/README.md
- packages/coding-agent/README.md
- packages/mom/README.md
- packages/pods/README.md
- packages/web-ui/README.md

## Code Quality
- No `any` types unless absolutely necessary
- Check node_modules for external API type definitions instead of guessing
- **NEVER use inline imports** - no `await import("./foo.js")`, no `import("pkg").Type` in type positions, no dynamic imports for types. Always use standard top-level imports.
- NEVER remove or downgrade code to fix type errors from outdated dependencies; upgrade the dependency instead
- Always ask before removing functionality or code that appears to be intentional
- Do not preserve backward compatibility unless the user explicitly asks for it
- Never hardcode key checks with, eg. `matchesKey(keyData, "ctrl+x")`. All keybindings must be configurable. Add default to matching object (`DEFAULT_EDITOR_KEYBINDINGS` or `DEFAULT_APP_KEYBINDINGS`)

## Commands
- After code changes (not documentation changes): `npm run check` (get full output, no tail). Fix all errors, warnings, and infos before committing.
- Note: `npm run check` does not run tests.
- NEVER run: `npm run dev`, `npm run build`, `npm test`
- Only run specific tests if user instructs: `npx tsx ../../node_modules/vitest/dist/cli.js --run test/specific.test.ts`
- Run tests from the package root, not the repo root.
- If you create or modify a test file, you MUST run that test file and iterate until it passes.
- When writing tests, run them, identify issues in either the test or implementation, and iterate until fixed.
- For `packages/coding-agent/test/suite/`, use `test/suite/harness.ts` plus the faux provider. Do not use real provider APIs, real API keys, or paid tokens.
- Put issue-specific regressions under `packages/coding-agent/test/suite/regressions/` and name them `<issue-number>-<short-slug>.test.ts`.
- NEVER commit unless user asks

## GitHub Issues
When reading issues:
- Always read all comments on the issue
- Use this command to get everything in one call:
  ```bash
  gh issue view <number> --json title,body,comments,labels,state
  ```

## OSS Weekend
- If the user says `enable OSS weekend mode until X`, run `node scripts/oss-weekend.mjs --mode=close --end-date=YYYY-MM-DD --git` with the requested end date
- If the user says `end OSS weekend mode`, run `node scripts/oss-weekend.mjs --mode=open --git`
- The script updates `README.md`, `packages/coding-agent/README.md`, and `.github/oss-weekend.json`
- With `--git`, the script stages only those OSS weekend files, commits them, and pushes them
- During OSS weekend, `.github/workflows/oss-weekend-issues.yml` auto-closes new issues from non-maintainers, and `.github/workflows/pr-gate.yml` auto-closes PRs from approved non-maintainers with the weekend message

When creating issues:
- Add `pkg:*` labels to indicate which package(s) the issue affects
  - Available labels: `pkg:agent`, `pkg:ai`, `pkg:coding-agent`, `pkg:mom`, `pkg:pods`, `pkg:tui`, `pkg:web-ui`
- If an issue spans multiple packages, add all relevant labels

When posting issue/PR comments:
- Write the full comment to a temp file and use `gh issue comment --body-file` or `gh pr comment --body-file`
- Never pass multi-line markdown directly via `--body` in shell commands
- Preview the exact comment text before posting
- Post exactly one final comment unless the user explicitly asks for multiple comments
- If a comment is malformed, delete it immediately, then post one corrected comment
- Keep comments concise, technical, and in the user's tone

When closing issues via commit:
- Include `fixes #<number>` or `closes #<number>` in the commit message
- This automatically closes the issue when the commit is merged

## PR Workflow
- Analyze PRs without pulling locally first
- If the user approves: create a feature branch, pull PR, rebase on main, apply adjustments, commit, merge into main, push, close PR, and leave a comment in the user's tone
- You never open PRs yourself. We work in feature branches until everything is according to the user's requirements, then merge into main, and push.

## Tools
- GitHub CLI for issues/PRs
- Add package labels to issues/PRs: pkg:agent, pkg:ai, pkg:coding-agent, pkg:mom, pkg:pods, pkg:tui, pkg:web-ui

## Testing pi Interactive Mode with tmux

To test pi's TUI in a controlled terminal environment:

```bash
# Create tmux session with specific dimensions
tmux new-session -d -s pi-test -x 80 -y 24

# Start pi from source
tmux send-keys -t pi-test "cd /Users/badlogic/workspaces/pi-mono && ./pi-test.sh" Enter

# Wait for startup, then capture output
sleep 3 && tmux capture-pane -t pi-test -p

# Send input
tmux send-keys -t pi-test "your prompt here" Enter

# Send special keys
tmux send-keys -t pi-test Escape
tmux send-keys -t pi-test C-o  # ctrl+o

# Cleanup
tmux kill-session -t pi-test
```

## Style
- Keep answers short and concise
- No emojis in commits, issues, PR comments, or code
- No fluff or cheerful filler text
- Technical prose only, be kind but direct (e.g., "Thanks @user" not "Thanks so much @user!")

## Changelog
Location: `packages/*/CHANGELOG.md` (each package has its own)

### Format
Use these sections under `## [Unreleased]`:
- `### Breaking Changes` - API changes requiring migration
- `### Added` - New features
- `### Changed` - Changes to existing functionality
- `### Fixed` - Bug fixes
- `### Removed` - Removed features

### Rules
- Before adding entries, read the full `[Unreleased]` section to see which subsections already exist
- New entries ALWAYS go under `## [Unreleased]` section
- Append to existing subsections (e.g., `### Fixed`), do not create duplicates
- NEVER modify already-released version sections (e.g., `## [0.12.2]`)
- Each version section is immutable once released

### Attribution
- **Internal changes (from issues)**: `Fixed foo bar ([#123](https://github.com/badlogic/pi-mono/issues/123))`
- **External contributions**: `Added feature X ([#456](https://github.com/badlogic/pi-mono/pull/456) by [@username](https://github.com/username))`

## Adding a New LLM Provider (packages/ai)

Adding a new provider requires changes across multiple files:

### 1. Core Types (`packages/ai/src/types.ts`)
- Add API identifier to `Api` type union (e.g., `"bedrock-converse-stream"`)
- Create options interface extending `StreamOptions`
- Add mapping to `ApiOptionsMap`
- Add provider name to `KnownProvider` type union

### 2. Provider Implementation (`packages/ai/src/providers/`)
Create provider file exporting:
- `stream<Provider>()` function returning `AssistantMessageEventStream`
- `streamSimple<Provider>()` for `SimpleStreamOptions` mapping
- Provider-specific options interface
- Message/tool conversion functions
- Response parsing emitting standardized events (`text`, `tool_call`, `thinking`, `usage`, `stop`)

### 3. Provider Exports and Lazy Registration
- Add a package subpath export in `packages/ai/package.json` pointing at `./dist/providers/<provider>.js`
- Add `export type` re-exports in `packages/ai/src/index.ts` for provider option types that should remain available from the root entry
- Register the provider in `packages/ai/src/providers/register-builtins.ts` via lazy loader wrappers, do not statically import provider implementation modules there
- Add credential detection in `packages/ai/src/env-api-keys.ts`

### 4. Model Generation (`packages/ai/scripts/generate-models.ts`)
- Add logic to fetch/parse models from provider source
- Map to standardized `Model` interface

### 5. Tests (`packages/ai/test/`)
Add provider to: `stream.test.ts`, `tokens.test.ts`, `abort.test.ts`, `empty.test.ts`, `context-overflow.test.ts`, `image-limits.test.ts`, `unicode-surrogate.test.ts`, `tool-call-without-result.test.ts`, `image-tool-result.test.ts`, `total-tokens.test.ts`, `cross-provider-handoff.test.ts`.

For `cross-provider-handoff.test.ts`, add at least one provider/model pair. If the provider exposes multiple model families (for example GPT and Claude), add at least one pair per family.

For non-standard auth, create utility (e.g., `bedrock-utils.ts`) with credential detection.

### 6. Coding Agent (`packages/coding-agent/`)
- `src/core/model-resolver.ts`: Add default model ID to `DEFAULT_MODELS`
- `src/cli/args.ts`: Add env var documentation
- `README.md`: Add provider setup instructions

### 7. Documentation
- `packages/ai/README.md`: Add to providers table, document options/auth, add env vars
- `packages/ai/CHANGELOG.md`: Add entry under `## [Unreleased]`

## Releasing

**Lockstep versioning**: All packages always share the same version number. Every release updates all packages together.

**Version semantics** (no major releases):
- `patch`: Bug fixes and new features
- `minor`: API breaking changes

### Steps

1. **Update CHANGELOGs**: Ensure all changes since last release are documented in the `[Unreleased]` section of each affected package's CHANGELOG.md

2. **Run release script**:
   ```bash
   npm run release:patch    # Fixes and additions
   npm run release:minor    # API breaking changes
   ```

The script handles: version bump, CHANGELOG finalization, commit, tag, publish, and adding new `[Unreleased]` sections.

## **CRITICAL** Tool Usage Rules **CRITICAL**
- NEVER use sed/cat to read a file or a range of a file. Always use the read tool (use offset + limit for ranged reads).
- You MUST read every file you modify in full before editing.

## **CRITICAL** Git Rules for Parallel Agents **CRITICAL**

Multiple agents may work on different files in the same worktree simultaneously. You MUST follow these rules:

### Committing
- **ONLY commit files YOU changed in THIS session**
- ALWAYS include `fixes #<number>` or `closes #<number>` in the commit message when there is a related issue or PR
- NEVER use `git add -A` or `git add .` - these sweep up changes from other agents
- ALWAYS use `git add <specific-file-paths>` listing only files you modified
- Before committing, run `git status` and verify you are only staging YOUR files
- Track which files you created/modified/deleted during the session

### Forbidden Git Operations
These commands can destroy other agents' work:
- `git reset --hard` - destroys uncommitted changes
- `git checkout .` - destroys uncommitted changes
- `git clean -fd` - deletes untracked files
- `git stash` - stashes ALL changes including other agents' work
- `git add -A` / `git add .` - stages other agents' uncommitted work
- `git commit --no-verify` - bypasses required checks and is never allowed

### Safe Workflow
```bash
# 1. Check status first
git status

# 2. Add ONLY your specific files
git add packages/ai/src/providers/transform-messages.ts
git add packages/ai/CHANGELOG.md

# 3. Commit
git commit -m "fix(ai): description"

# 4. Push (pull --rebase if needed, but NEVER reset/checkout)
git pull --rebase && git push
```

### If Rebase Conflicts Occur
- Resolve conflicts in YOUR files only
- If conflict is in a file you didn't modify, abort and ask the user
- NEVER force push

### User override
If the user instructions conflict with rules set out here, ask for confirmation that they want to override the rules. Only then execute their instructions.
```

### `README.md`

- Source path: `README.md`
- Truncated: `no`

```md
<!-- OSS_WEEKEND_START -->
# 🏖️ OSS Weekend

**Issue tracker reopens Monday, April 13, 2026.**

OSS weekend runs Thursday, April 2, 2026 through Monday, April 13, 2026. New issues and PRs from unapproved contributors are auto-closed during this time. Approved contributors can still open issues and PRs if something is genuinely urgent, but please keep that to pressing matters only. For support, join [Discord](https://discord.com/invite/3cU7Bz4UPx).

> _Current focus: at the moment i'm deep in refactoring internals, and need to focus._
<!-- OSS_WEEKEND_END -->

---

<p align="center">
  <a href="https://shittycodingagent.ai">
    <img src="https://shittycodingagent.ai/logo.svg" alt="pi logo" width="128">
  </a>
</p>
<p align="center">
  <a href="https://discord.com/invite/3cU7Bz4UPx"><img alt="Discord" src="https://img.shields.io/badge/discord-community-5865F2?style=flat-square&logo=discord&logoColor=white" /></a>
  <a href="https://github.com/badlogic/pi-mono/actions/workflows/ci.yml"><img alt="Build status" src="https://img.shields.io/github/actions/workflow/status/badlogic/pi-mono/ci.yml?style=flat-square&branch=main" /></a>
</p>
<p align="center">
  <a href="https://pi.dev">pi.dev</a> domain graciously donated by
  <br /><br />
  <a href="https://exe.dev"><img src="packages/coding-agent/docs/images/exy.png" alt="Exy mascot" width="48" /><br />exe.dev</a>
</p>

# Pi Monorepo

> **Looking for the pi coding agent?** See **[packages/coding-agent](packages/coding-agent)** for installation and usage.

Tools for building AI agents and managing LLM deployments.

## Share your OSS coding agent sessions

If you use pi or other coding agents for open source work, please share your sessions.

Public OSS session data helps improve coding agents with real-world tasks, tool use, failures, and fixes instead of toy benchmarks.

For the full explanation, see [this post on X](https://x.com/badlogicgames/status/2037811643774652911).

To publish sessions, use [`badlogic/pi-share-hf`](https://github.com/badlogic/pi-share-hf). Read its README.md for setup instructions. All you need is a Hugging Face account, the Hugging Face CLI, and `pi-share-hf`.

You can also watch [this video](https://x.com/badlogicgames/status/2041151967695634619), where I show how I publish my `pi-mono` sessions.

I regularly publish my own `pi-mono` work sessions here:

- [badlogicgames/pi-mono on Hugging Face](https://huggingface.co/datasets/badlogicgames/pi-mono)

## Packages

| Package | Description |
|---------|-------------|
| **[@mariozechner/pi-ai](packages/ai)** | Unified multi-provider LLM API (OpenAI, Anthropic, Google, etc.) |
| **[@mariozechner/pi-agent-core](packages/agent)** | Agent runtime with tool calling and state management |
| **[@mariozechner/pi-coding-agent](packages/coding-agent)** | Interactive coding agent CLI |
| **[@mariozechner/pi-mom](packages/mom)** | Slack bot that delegates messages to the pi coding agent |
| **[@mariozechner/pi-tui](packages/tui)** | Terminal UI library with differential rendering |
| **[@mariozechner/pi-web-ui](packages/web-ui)** | Web components for AI chat interfaces |
| **[@mariozechner/pi-pods](packages/pods)** | CLI for managing vLLM deployments on GPU pods |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and [AGENTS.md](AGENTS.md) for project-specific rules (for both humans and agents).

## Development

```bash
npm install          # Install all dependencies
npm run build        # Build all packages
npm run check        # Lint, format, and type check
./test.sh            # Run tests (skips LLM-dependent tests without API keys)
./pi-test.sh         # Run pi from sources (can be run from any directory)
```

> **Note:** `npm run check` requires `npm run build` to be run first. The web-ui package uses `tsc` which needs compiled `.d.ts` files from dependencies.

## License

MIT
```

### `package.json`

- Source path: `package.json`
- Truncated: `no`

```json
{
	"name": "pi-monorepo",
	"private": true,
	"type": "module",
	"workspaces": [
		"packages/*",
		"packages/web-ui/example",
		"packages/coding-agent/examples/extensions/with-deps",
		"packages/coding-agent/examples/extensions/custom-provider-anthropic",
		"packages/coding-agent/examples/extensions/custom-provider-gitlab-duo",
		"packages/coding-agent/examples/extensions/custom-provider-qwen-cli"
	],
	"scripts": {
		"clean": "npm run clean --workspaces",
		"build": "cd packages/tui && npm run build && cd ../ai && npm run build && cd ../agent && npm run build && cd ../coding-agent && npm run build && cd ../mom && npm run build && cd ../web-ui && npm run build && cd ../pods && npm run build",
		"dev": "concurrently --names \"ai,agent,coding-agent,mom,web-ui,tui\" --prefix-colors \"cyan,yellow,red,white,green,magenta\" \"cd packages/ai && npm run dev\" \"cd packages/agent && npm run dev\" \"cd packages/coding-agent && npm run dev\" \"cd packages/mom && npm run dev\" \"cd packages/web-ui && npm run dev\" \"cd packages/tui && npm run dev\"",
		"dev:tsc": "concurrently --names \"ai,web-ui\" --prefix-colors \"cyan,green\" \"cd packages/ai && npm run dev:tsc\" \"cd packages/web-ui && npm run dev:tsc\"",
		"check": "biome check --write --error-on-warnings . && tsgo --noEmit && npm run check:browser-smoke && cd packages/web-ui && npm run check",
		"check:browser-smoke": "node scripts/check-browser-smoke.mjs",
		"profile:tui": "node scripts/profile-coding-agent-node.mjs --mode tui",
		"profile:rpc": "node scripts/profile-coding-agent-node.mjs --mode rpc",
		"test": "npm run test --workspaces --if-present",
		"version:patch": "npm version patch -ws --no-git-tag-version && node scripts/sync-versions.js && shx rm -rf node_modules packages/*/node_modules package-lock.json && npm install",
		"version:minor": "npm version minor -ws --no-git-tag-version && node scripts/sync-versions.js && shx rm -rf node_modules packages/*/node_modules package-lock.json && npm install",
		"version:major": "npm version major -ws --no-git-tag-version && node scripts/sync-versions.js && shx rm -rf node_modules packages/*/node_modules package-lock.json && npm install",
		"version:set": "npm version -ws",
		"prepublishOnly": "npm run clean && npm run build && npm run check",
		"publish": "npm run prepublishOnly && npm publish -ws --access public",
		"publish:dry": "npm run prepublishOnly && npm publish -ws --access public --dry-run",
		"release:patch": "node scripts/release.mjs patch",
		"release:minor": "node scripts/release.mjs minor",
		"release:major": "node scripts/release.mjs major",
		"prepare": "husky"
	},
	"devDependencies": {
		"@biomejs/biome": "2.3.5",
		"@types/node": "^22.10.5",
		"@typescript/native-preview": "7.0.0-dev.20260120.1",
		"concurrently": "^9.2.1",
		"husky": "^9.1.7",
		"tsx": "^4.20.3",
		"typescript": "^5.9.2",
		"shx": "^0.4.0"
	},
	"engines": {
		"node": ">=20.0.0"
	},
	"version": "0.0.3",
	"dependencies": {
		"@mariozechner/jiti": "^2.6.5",
		"@mariozechner/pi-coding-agent": "^0.30.2",
		"get-east-asian-width": "^1.4.0"
	},
	"overrides": {
		"rimraf": "6.1.2",
		"fast-xml-parser": "5.3.8",
		"gaxios": {
			"rimraf": "6.1.2"
		}
	}
}
```
