---
title: "GitHub repo snapshot: refactoringhq/tolaria"
source: "https://github.com/refactoringhq/tolaria"
author:
published:
created: 2026-04-24
description: "Compact GitHub repository evidence snapshot for repo-map-ingest."
tags:
  - "github"
  - "repo-snapshot"
---

# GitHub Repo Snapshot: `refactoringhq/tolaria`

## Observation Scope

- Repository: `refactoringhq/tolaria`
- URL: https://github.com/refactoringhq/tolaria
- Requested topic: 仓库架构与工程实践
- Observed ref: `main`
- Latest resolved commit: `622977aeb8baece4a132553ddd082b92659a4ce7`
- Commit date: `2026-04-24T13:18:50Z`
- Snapshot date (UTC): `2026-04-24`

## Repository Metadata

- Description: Desktop app to manage markdown knowledge bases
- Default branch: `main`
- Language: `TypeScript`
- Stars: `2807`
- Forks: `170`
- Open issues: `16`

## Top-Level Tree

### Directories

- `.claude`
- `.github`
- `.husky`
- `demo-vault-v2`
- `design`
- `docs`
- `e2e`
- `mcp-server`
- `patches`
- `public`
- `scripts`
- `src`
- `src-tauri`
- `tests`

### Files

- `.codescene-thresholds`
- `.codesceneignore`
- `.codescenerc`
- `.env.example`
- `.githooks-info`
- `.gitignore`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `README.md`
- `SECURITY.md`
- `components.json`
- `eslint.config.js`
- `index.html`
- `package.json`
- `playwright.config.ts`
- `playwright.integration.config.ts`
- `playwright.smoke.config.ts`
- `pnpm-lock.yaml`
- `pnpm-workspace.yaml`
- `trademarks.md`
- `tsconfig.app.json`
- `tsconfig.json`
- `tsconfig.node.json`
- `ui-design.pen`
- `vite.config.ts`

## Selected Evidence Anchors

- `.github/workflows/README.md`
- `.github/workflows/auto-update-prs.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/release-stable.yml`
- `.github/workflows/release.yml`
- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `package.json`
- `pnpm-workspace.yaml`

## Captured Files

### `.github/workflows/README.md`

- Source path: `.github/workflows/README.md`
- Truncated: `no`

```md
# CI/CD Setup

## GitHub Actions Workflow

Il workflow `ci.yml` esegue i seguenti check automatici:

### 1. Tests
- Frontend: `pnpm test`
- Rust backend: `cargo test`

### 2. Test Coverage
- Frontend: vitest con coverage reporting
- Upload automatico su Codecov dai report LCOV frontend + Rust
- Threshold configurabile in `vitest.config.ts`

### 3. Code Health (CodeScene)
- Delta analysis su ogni PR/push
- Fail se il code health diminuisce
- Richiede secrets configurati (vedi sotto)

### 4. Documentation Check
- Verifica che se cambia codice in `src/` o `src-tauri/`, anche `docs/` viene aggiornato
- **Warning only** — non blocca il merge, solo un reminder
- Skip con `[skip docs]` nel commit message
- Aggiorna docs solo se la modifica invalida architettura/astrazioni/design già documentati

### 5. Lint & Format
- ESLint per frontend
- Clippy + rustfmt per Rust

## Setup Required

### CodeScene Secrets
Aggiungi questi secrets nel repository GitHub (Settings → Secrets → Actions):

```
CODESCENE_TOKEN=<your-codescene-pat>
CODESCENE_PROJECT_ID=<your-project-id>
```

Il PAT di CodeScene è lo stesso che usi localmente (~/.codescene/token).
Il project ID lo trovi nella dashboard CodeScene.

### Codecov Setup
- Installa/attiva il repo in Codecov una volta sola tramite GitHub App / import del repository.
- Nessun `CODECOV_TOKEN` richiesto in GitHub Actions: `ci.yml` usa OIDC (`id-token: write` + `use_oidc: true`).
- Il workflow carica `coverage/lcov.info` (Vitest) e `coverage/rust.lcov` (cargo-llvm-cov).

### Telemetry Secrets For Release Builds
Aggiungi anche questi secrets per i workflow `release.yml` e `release-stable.yml`:

```
VITE_SENTRY_DSN=<frontend sentry dsn>
SENTRY_DSN=<same dsn for rust/native crash reporting>
VITE_POSTHOG_KEY=<posthog project api key>
VITE_POSTHOG_HOST=https://eu.i.posthog.com
```

Senza questi valori, i build distribuiti possono mantenere i toggle telemetry nelle Settings ma non inizializzare davvero PostHog/Sentry.

### Coverage Thresholds
Configura in `vitest.config.ts`:

```typescript
export default defineConfig({
  test: {
    coverage: {
      lines: 80,
      functions: 80,
      branches: 80,
      statements: 80,
      // Fail CI se sotto threshold
      thresholds: {
        lines: 80,
        functions: 80,
        branches: 80,
        statements: 80
      }
    }
  }
})
```

## Local Testing

Prima di pushare, puoi testare localmente:

```bash
# Run all tests
pnpm test && cargo test

# Check coverage
pnpm test:coverage

# Lint
pnpm lint
cargo clippy
cargo fmt --check

# CodeScene (local)
codescene delta-analysis --base-revision origin/main
```

## Workflow Triggers

- **Push**: su `main`
- **Pull Request**: verso `main`
- **Manuale**: `workflow_dispatch`

Nota: l'upload a Codecov gira su push a `main` e sulle PR dello stesso repository. Le PR da fork saltano l'upload per evitare problemi di permessi OIDC.

## Status Checks

Tutti i check devono passare prima di poter fare merge.
Se un check fallisce, vedrai il dettaglio nei logs di GitHub Actions.
```

### `.github/workflows/auto-update-prs.yml`

- Source path: `.github/workflows/auto-update-prs.yml`
- Truncated: `no`

```yaml
name: Auto-update PR branches

# When main advances, automatically update all open PR branches
# so they stay up to date and can be auto-merged without manual rebase.

on:
  push:
    branches: [main]

jobs:
  update-prs:
    name: Update open PR branches
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Update all open PR branches
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Get all open PRs targeting main
          PRS=$(gh pr list --base main --state open --json number,headRefName --jq '.[]')

          echo "$PRS" | while IFS= read -r pr; do
            PR_NUM=$(echo "$pr" | jq -r '.number')
            BRANCH=$(echo "$pr" | jq -r '.headRefName')

            echo "Updating PR #$PR_NUM ($BRANCH)..."
            # GitHub native update — does a merge of main into the branch
            gh pr update-branch "$PR_NUM" 2>&1 && echo "✅ #$PR_NUM updated" || echo "⚠️ #$PR_NUM skipped (already up to date or conflict)"
          done
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
  workflow_dispatch:

permissions:
  contents: read
  id-token: write

env:
  # Bump this when Tauri/Rust target artifacts capture stale absolute paths.
  RUST_TARGET_CACHE_VERSION: v2026-04-14-tolaria

jobs:
  test:
    name: Tests & Quality Checks
    runs-on: macos-15

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history for CodeScene

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: 10

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'pnpm'

      - name: Setup Rust
        uses: dtolnay/rust-toolchain@stable
        with:
          components: rustfmt, clippy, llvm-tools-preview

      - name: Cache Rust dependencies
        uses: actions/cache@v4
        with:
          path: |
            ~/.cargo/registry
            ~/.cargo/git
            src-tauri/target
          key: ${{ runner.os }}-cargo-${{ env.RUST_TARGET_CACHE_VERSION }}-${{ hashFiles('src-tauri/Cargo.lock') }}
          restore-keys: |
            ${{ runner.os }}-cargo-${{ env.RUST_TARGET_CACHE_VERSION }}-

      - name: Install cargo-llvm-cov
        uses: taiki-e/install-action@cargo-llvm-cov

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      # ── 0. Build check (catches type errors and bundler failures) ─────────
      - name: TypeScript type check
        run: pnpm exec tsc --noEmit

      - name: Vite build check
        run: pnpm build

      # ── 1. Tests ──────────────────────────────────────────────────────────
      - name: Run frontend tests
        run: pnpm test

      - name: Bundle MCP server resources (required by Tauri build)
        run: node scripts/bundle-mcp-server.mjs

      - name: Run Rust tests
        run: cargo test --manifest-path=src-tauri/Cargo.toml

      # ── 2. Coverage (enforced — fails build if thresholds not met) ────────
      - name: Frontend coverage (≥70% lines/functions/branches/statements)
        run: pnpm test:coverage
        # Thresholds configured in vite.config.ts — exits non-zero if coverage drops

      - name: Rust coverage (≥85% lines)
        run: |
          cargo llvm-cov \
            --manifest-path src-tauri/Cargo.toml \
            --ignore-filename-regex 'lib\.rs|main\.rs|menu\.rs' \
            --lcov \
            --output-path coverage/rust.lcov \
            --fail-under-lines 85
        # cargo-llvm-cov exits non-zero if line coverage drops below 85%
        # lib.rs/main.rs/menu.rs are Tauri boilerplate -- not meaningfully unit-testable.

      - name: Upload coverage to Codecov
        if: github.event_name != 'pull_request' || github.event.pull_request.head.repo.full_name == github.repository
        uses: codecov/codecov-action@v5
        with:
          use_oidc: true
          fail_ci_if_error: true
          disable_search: true
          files: ./coverage/lcov.info,./coverage/rust.lcov
          verbose: true
        # OIDC avoids long-lived CODECOV_TOKEN secrets.

      # ── 3. Code Health (CodeScene — Hotspot + Average Code Health gates) ──
      # Enforces minimum floors on BOTH hotspot and average code health.
      # Thresholds come from .codescene-thresholds so CI and local hooks match.
      - name: Code Health gates
        env:
          CODESCENE_PAT: ${{ secrets.CODESCENE_PAT }}
          CODESCENE_PROJECT_ID: ${{ secrets.CODESCENE_PROJECT_ID }}
        run: |
          HOTSPOT_THRESHOLD=$(grep '^HOTSPOT_THRESHOLD=' .codescene-thresholds | cut -d= -f2)
          AVERAGE_THRESHOLD=$(grep '^AVERAGE_THRESHOLD=' .codescene-thresholds | cut -d= -f2)
          API_RESPONSE=$(curl -sf \
            -H "Authorization: Bearer $CODESCENE_PAT" \
            -H "Accept: application/json" \
            "https://api.codescene.io/v2/projects/$CODESCENE_PROJECT_ID")
          HOTSPOT_SCORE=$(echo "$API_RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['analysis']['hotspot_code_health']['now'])")
          AVERAGE_SCORE=$(echo "$API_RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['analysis']['code_health']['now'])")
          echo "Hotspot Code Health: $HOTSPOT_SCORE (threshold: $HOTSPOT_THRESHOLD)"
          echo "Average Code Health: $AVERAGE_SCORE (threshold: $AVERAGE_THRESHOLD)"
          python3 -c "
          hotspot = float('$HOTSPOT_SCORE')
          average = float('$AVERAGE_SCORE')
          ht = float('$HOTSPOT_THRESHOLD')
          at = float('$AVERAGE_THRESHOLD')
          failed = False
          if hotspot < ht:
              print(f'❌ Hotspot Code Health {hotspot:.2f} is below threshold {ht}')
              failed = True
          else:
              print(f'✅ Hotspot Code Health {hotspot:.2f} ≥ {ht}')
          if average < at:
              print(f'❌ Average Code Health {average:.2f} is below threshold {at}')
              failed = True
          else:
              print(f'✅ Average Code Health {average:.2f} ≥ {at}')
          if failed:
              exit(1)
          "

      # ── 4. Documentation check (warning only — does not fail build) ───────
      - name: Check docs are updated
        continue-on-error: true
        run: |
          if git log -1 --pretty=%B | grep -i '\[skip docs\]' > /dev/null; then
            echo "⏭️  Documentation check skipped"
            exit 0
          fi
          if git diff --name-only origin/main | grep -E '^(src/|src-tauri/)' > /dev/null; then
            if ! git diff --name-only origin/main | grep -E '^docs/' > /dev/null; then
              echo "⚠️  Code files changed but docs/ not updated"
              git diff --name-only origin/main | grep -E '^(src/|src-tauri/)'
              echo "If this change affects architecture/abstractions/theme documented in docs/, update them."
              echo "To suppress: include [skip docs] in your commit message."
            fi
          fi
          echo "✅ Documentation check passed"

      # ── 5. Lint & format ──────────────────────────────────────────────────
      - name: Lint frontend
        run: pnpm lint

      - name: Clippy (Rust)
        run: cargo clippy --manifest-path=src-tauri/Cargo.toml -- -D warnings

      - name: Format check (Rust)
        run: cargo fmt --manifest-path=src-tauri/Cargo.toml -- --check
```

### `.github/workflows/release-stable.yml`

- Source path: `.github/workflows/release-stable.yml`
- Truncated: `no`

```yaml
name: Release (Stable)

on:
  push:
    tags:
      - 'stable-v*'

env:
  # Bump this when Tauri/Rust target artifacts capture stale absolute paths.
  RUST_TARGET_CACHE_VERSION: v2026-04-14-tolaria

concurrency:
  group: release-stable-${{ github.ref }}
  cancel-in-progress: true

jobs:
  # ─────────────────────────────────────────────────────────────
  # Phase 1: Compute the stable version string once
  # ─────────────────────────────────────────────────────────────
  version:
    name: Compute stable version
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.ver.outputs.version }}
      display_version: ${{ steps.ver.outputs.display_version }}
      tag: ${{ steps.ver.outputs.tag }}
    steps:
      - id: ver
        shell: bash
        run: |
          python3 <<'PY' > version.env
          import os
          import re
          from datetime import date

          tag = os.environ["GITHUB_REF_NAME"]
          version = tag.removeprefix("stable-v")
          match = re.fullmatch(r"(\d{4})\.(\d{1,2})\.(\d{1,2})", version)
          if not match:
              raise SystemExit(f"Stable tags must use stable-vYYYY.M.D, got {tag}")

          date(*map(int, match.groups()))
          print(f"version={version}")
          print(f"display_version={version}")
          print(f"tag={tag}")
          PY

          cat version.env >> "$GITHUB_OUTPUT"
          DISPLAY_VERSION=$(grep '^display_version=' version.env | cut -d= -f2-)
          echo "### Stable version: \`$DISPLAY_VERSION\`" >> "$GITHUB_STEP_SUMMARY"

  # ─────────────────────────────────────────────────────────────
  # Phase 2: Build each architecture in parallel
  # ─────────────────────────────────────────────────────────────
  build:
    name: Build (${{ matrix.arch }})
    needs: version
    runs-on: macos-15
    strategy:
      fail-fast: true
      matrix:
        include:
          - arch: aarch64
            target: aarch64-apple-darwin
    steps:
      - uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: 10

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'pnpm'

      - name: Setup Bun (required for bundle-qmd.sh)
        uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest

      - name: Setup Rust
        uses: dtolnay/rust-toolchain@stable
        with:
          targets: ${{ matrix.target }}

      - name: Cache Rust dependencies
        uses: actions/cache@v4
        with:
          path: |
            ~/.cargo/registry
            ~/.cargo/git
            src-tauri/target
          key: ${{ runner.os }}-release-cargo-${{ matrix.target }}-${{ env.RUST_TARGET_CACHE_VERSION }}-${{ hashFiles('src-tauri/Cargo.lock') }}
          restore-keys: |
            ${{ runner.os }}-release-cargo-${{ matrix.target }}-${{ env.RUST_TARGET_CACHE_VERSION }}-

      - name: Install frontend dependencies
        run: pnpm install --frozen-lockfile

      - name: Clear cached bundle artifacts
        run: |
          rm -rf src-tauri/target/${{ matrix.target }}/release/bundle

      - name: Set version
        run: |
          VERSION="${{ needs.version.outputs.version }}"
          jq --arg v "$VERSION" '.version = $v' src-tauri/tauri.conf.json > tmp.json && mv tmp.json src-tauri/tauri.conf.json
          sed -i '' "s/^version = \".*\"/version = \"$VERSION\"/" src-tauri/Cargo.toml

      - name: Import Apple Developer certificate into keychain
        env:
          APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}
          APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}
        run: |
          CERT_PATH="$RUNNER_TEMP/apple_cert.p12"
          KEYCHAIN_PATH="$RUNNER_TEMP/laputa-signing.keychain-db"
          KEYCHAIN_PASSWORD="$(uuidgen)"
          echo "$APPLE_CERTIFICATE" | base64 --decode > "$CERT_PATH"
          security create-keychain -p "$KEYCHAIN_PASSWORD" "$KEYCHAIN_PATH"
          security set-keychain-settings -lut 21600 "$KEYCHAIN_PATH"
          security unlock-keychain -p "$KEYCHAIN_PASSWORD" "$KEYCHAIN_PATH"
          security import "$CERT_PATH" -P "$APPLE_CERTIFICATE_PASSWORD" -A -t cert -f pkcs12 -k "$KEYCHAIN_PATH"
          security list-keychain -d user -s "$KEYCHAIN_PATH"
          security set-key-partition-list -S apple-tool:,apple: -s -k "$KEYCHAIN_PASSWORD" "$KEYCHAIN_PATH"
          echo "KEYCHAIN_PATH=$KEYCHAIN_PATH" >> "$GITHUB_ENV"

      - name: Validate telemetry env
        env:
          VITE_SENTRY_DSN: ${{ secrets.VITE_SENTRY_DSN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          VITE_POSTHOG_KEY: ${{ secrets.VITE_POSTHOG_KEY }}
          VITE_POSTHOG_HOST: ${{ secrets.VITE_POSTHOG_HOST }}
        run: |
          python3 <<'PY'
          import os
          import re
          import sys
          from urllib.parse import urlparse

          DISALLOWED_PLACEHOLDERS = {
              "",
              "-",
              "_",
              "false",
              "true",
              "null",
              "undefined",
              "none",
              "disabled",
          }

          def normalize(name: str) -> str:
              value = os.getenv(name, "").strip()
              if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
                  value = value[1:-1].strip()
              return value

          def normalize_http_like(value: str) -> str:
              if "://" in value:
                  return value
              return f"https://{value}"

          def normalize_hostname(hostname: str) -> str:
              normalized = hostname.strip().rstrip('.').lower()
              if normalized.startswith('[') and normalized.endswith(']'):
                  normalized = normalized[1:-1]
              return normalized

          def is_ip_address(hostname: str) -> bool:
              if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", hostname):
                  return all(0 <= int(part) <= 255 for part in hostname.split('.'))
              return ':' in hostname and re.fullmatch(r"[\da-f:]+", hostname, re.IGNORECASE) is not None

          def is_allowed_hostname(hostname: str) -> bool:
              normalized = normalize_hostname(hostname)
              if not normalized or normalized in DISALLOWED_PLACEHOLDERS:
                  return False
              if normalized == 'localhost':
                  return True
              return '.' in normalized or is_ip_address(normalized)

          def is_http_url(value: str) -> bool:
              parsed = urlparse(normalize_http_like(value))
              return parsed.scheme in {"http", "https"} and is_allowed_hostname(parsed.hostname or "")

          values = {
              name: normalize(name)
              for name in (
                  "VITE_SENTRY_DSN",
                  "SENTRY_DSN",
                  "VITE_POSTHOG_KEY",
                  "VITE_POSTHOG_HOST",
              )
          }
          errors = []

          for name in ("VITE_SENTRY_DSN", "SENTRY_DSN", "VITE_POSTHOG_HOST"):
              value = values[name]
              if value.lower() in DISALLOWED_PLACEHOLDERS:
                  errors.append(f"{name} must be set to a real value, not a placeholder")
              elif not is_http_url(value):
                  errors.append(f"{name} must be a valid http(s) URL with a non-placeholder host")

          if values["VITE_POSTHOG_KEY"].lower() in DISALLOWED_PLACEHOLDERS:
              errors.append("VITE_POSTHOG_KEY must be set to a real project API key, not a placeholder")

          if errors:
              print("Telemetry env validation failed:", file=sys.stderr)
              for error in errors:
                  print(f"- {error}", file=sys.stderr)
              raise SystemExit(1)

          print("Telemetry env validation passed.")
          PY

      - name: Build Tauri app (with signing + notarization)
        env:
          TAURI_SIGNING_PRIVATE_KEY: ${{ secrets.TAURI_SIGNING_PRIVATE_KEY }}
          TAURI_SIGNING_PRIVATE_KEY_PASSWORD: ${{ secrets.TAURI_KEY_PASSWORD }}
          APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}
          APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}
          APPLE_SIGNING_IDENTITY: ${{ secrets.APPLE_SIGNING_IDENTITY }}
          APPLE_ID: ${{ secrets.APPLE_ID }}
          APPLE_PASSWORD: ${{ secrets.APPLE_PASSWORD }}
          APPLE_TEAM_ID: ${{ secrets.APPLE_TEAM_ID }}
          VITE_SENTRY_DSN: ${{ secrets.VITE_SENTRY_DSN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          VITE_POSTHOG_KEY: ${{ secrets.VITE_POSTHOG_KEY }}
          VITE_POSTHOG_HOST: ${{ secrets.VITE_POSTHOG_HOST }}
        run: |
          pnpm tauri build --target ${{ matrix.target }}

      - name: Upload .dmg
        uses: actions/upload-artifact@v4
        with:
          name: dmg-${{ matrix.arch }}
          path: src-tauri/target/${{ matrix.target }}/release/bundle/dmg/*.dmg
          retention-days: 1

      - name: Upload updater artifacts (.tar.gz + .sig)
        uses: actions/upload-artifact@v4
        with:
          name: updater-${{ matrix.arch }}
          path: |
            src-tauri/target/${{ matrix.target }}/release/bundle/macos/*.app.tar.gz
            src-tauri/target/${{ matrix.target }}/release/bundle/macos/*.app.tar.gz.sig
          retention-days: 1

  # ─────────────────────────────────────────────────────────────
  # Phase 3: Publish GitHub Release
  # ─────────────────────────────────────────────────────────────
  release:
    name: GitHub Release (stable)
    needs: [version, build]
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Download all artifacts
        uses: actions/download-artifact@v4

      - name: Generate release notes
        run: |
          PREV_TAG=$(git tag --list 'stable-v*' --sort=-version:refname | grep -vx "${{ needs.version.outputs.tag }}" | head -n 1 || echo "")
          if [ -z "$PREV_TAG" ]; then
            NOTES=$(git log --oneline --no-merges -20)
          else
            NOTES=$(git log --oneline --no-merges "${PREV_TAG}..${{ needs.version.outputs.tag }}")
          fi
          {
            echo "## What's Changed"
            echo ""
            echo "$NOTES" | while IFS= read -r line; do echo "- $line"; done
            echo ""
            echo "---"
            echo "**Stable release — manually promoted from \`main\`**"
            echo ""
            echo "**Requires Apple Silicon (M1/M2/M3)**"
            echo ""
            echo "*Built from \`$(git rev-parse --short ${{ needs.version.outputs.tag }})\` on $(date -u +%Y-%m-%d)*"
          } > release_notes.md

      - name: Build stable-latest.json
        run: |
          VERSION="${{ needs.version.outputs.version }}"
          TAG="${{ needs.version.outputs.tag }}"
          REPO="${GITHUB_REPOSITORY}"
          REPO_NAME="${REPO#*/}"
          PAGES_URL="https://refactoringhq.github.io/${REPO_NAME}/"

          ARM_SIG=$(cat updater-aarch64/*.app.tar.gz.sig)
          ARM_TARBALL=$(ls updater-aarch64/*.app.tar.gz | xargs basename)
          ARM_DMG=$(ls dmg-aarch64/*.dmg | xargs basename)

          cat > stable-latest.json << EOF
          {
            "version": "${VERSION}",
            "notes": "Stable release. See ${PAGES_URL} for full release notes.",
            "pub_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "platforms": {
              "darwin-aarch64": {
                "signature": "${ARM_SIG}",
                "url": "https://github.com/${REPO}/releases/download/${TAG}/${ARM_TARBALL}",
                "dmg_url": "https://github.com/${REPO}/releases/download/${TAG}/${ARM_DMG}"
              }
            }
          }
          EOF
          echo "stable-latest.json:"; cat stable-latest.json

      - name: Publish GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          tag_name: ${{ needs.version.outputs.tag }}
          name: Tolaria ${{ needs.version.outputs.display_version }}
          body_path: release_notes.md
          draft: false
          prerelease: false
          files: |
            dmg-aarch64/*.dmg
            updater-aarch64/*.app.tar.gz
            updater-aarch64/*.app.tar.gz.sig
            stable-latest.json

  # ─────────────────────────────────────────────────────────────
  # Phase 4: Update GitHub Pages
  # ─────────────────────────────────────────────────────────────
  pages:
    name: Update release history page
    needs: [version, release]
    runs-on: ubuntu-latest
    permissions:
      contents: write
    concurrency:
      group: github-pages
      cancel-in-progress: false
    steps:
      - uses: actions/checkout@v4

      - name: Setup Bun
        uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest

      - name: Build release history page
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          mkdir -p _site/alpha _site/stable
          gh api -H "Accept: application/vnd.github.html+json" repos/${{ github.repository }}/releases --paginate > _site/releases.json
          PAGES_URL="https://refactoringhq.github.io/${GITHUB_REPOSITORY#*/}"

          curl -fsSL "${PAGES_URL}/alpha/latest.json" -o _site/alpha/latest.json || echo '{}' > _site/alpha/latest.json
          gh release download --repo ${{ github.repository }} "${{ needs.version.outputs.tag }}" --pattern "stable-latest.json" --output _site/stable/latest.json || echo '{}' > _site/stable/latest.json
          bun scripts/build-release-download-page.ts --latest-json _site/stable/latest.json --releases-json _site/releases.json --output-file _site/stable/download/index.html
          bun scripts/build-release-history-page.ts --releases-json _site/releases.json --output-file _site/index.html
          mkdir -p _site/download
          cp _site/stable/download/index.html _site/download/index.html

          cp _site/alpha/latest.json _site/latest.json
          cp _site/alpha/latest.json _site/latest-canary.json

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
          commit_message: "Update release history for ${{ needs.version.outputs.tag }}"
```

### `.github/workflows/release.yml`

- Source path: `.github/workflows/release.yml`
- Truncated: `no`

```yaml
name: Release (Alpha)

on:
  push:
    branches:
      - main

env:
  # Bump this when Tauri/Rust target artifacts capture stale absolute paths.
  RUST_TARGET_CACHE_VERSION: v2026-04-14-tolaria

concurrency:
  group: release-alpha-${{ github.ref }}
  cancel-in-progress: true

jobs:
  # ─────────────────────────────────────────────────────────────
  # Phase 1: Compute the alpha version string once
  # Alpha builds use calendar semver and stay newer than the latest stable tag.
  # ─────────────────────────────────────────────────────────────
  version:
    name: Compute alpha version
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.ver.outputs.version }}
      display_version: ${{ steps.ver.outputs.display_version }}
      tag: ${{ steps.ver.outputs.tag }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - id: ver
        shell: bash
        run: |
          python3 <<'PY' > version.env
          import re
          import subprocess
          from datetime import datetime, timedelta, timezone

          def lines(command: list[str]) -> list[str]:
              output = subprocess.check_output(command, text=True).strip()
              return [line for line in output.splitlines() if line]

          alpha_pattern = re.compile(r"^alpha-v(\d{4}\.\d{1,2}\.\d{1,2})-alpha\.(\d+)$")

          def parse_alpha_tag(tag: str) -> tuple[str, int] | None:
              match = alpha_pattern.fullmatch(tag)
              if not match:
                  return None
              calendar_version, sequence = match.groups()
              return calendar_version, int(sequence)

          def alpha_version(calendar_version: str, sequence: int) -> str:
              return f"{calendar_version}-alpha.{sequence}"

          def alpha_tag(calendar_version: str, sequence: int) -> str:
              return f"alpha-v{calendar_version}-alpha.{sequence:04d}"

          existing_tags = [
              tag for tag in lines(["git", "tag", "--points-at", "HEAD"])
              if tag.startswith("alpha-v")
          ]

          if existing_tags:
              tag = existing_tags[0]
              parsed = parse_alpha_tag(tag)
              version = alpha_version(*parsed) if parsed is not None else tag.removeprefix("alpha-v")
          else:
              today = datetime.now(timezone.utc).date()
              stable_date = None
              stable_pattern = re.compile(r"^stable-v(\d{4})\.(\d{1,2})\.(\d{1,2})$")

              for stable_tag in lines(["git", "tag", "--list", "stable-v*", "--sort=-version:refname"]):
                  match = stable_pattern.fullmatch(stable_tag)
                  if not match:
                      continue

                  year, month, day = map(int, match.groups())
                  try:
                      stable_date = datetime(year, month, day, tzinfo=timezone.utc).date()
                  except ValueError:
                      continue
                  break

              alpha_date = today if stable_date is None or today > stable_date else stable_date + timedelta(days=1)
              calendar_version = f"{alpha_date.year}.{alpha_date.month}.{alpha_date.day}"
              sequence = len(lines(["git", "tag", "--list", f"alpha-v{calendar_version}-alpha.*"])) + 1

              version = alpha_version(calendar_version, sequence)
              tag = alpha_tag(calendar_version, sequence)

          display_match = re.fullmatch(r"(\d{4})\.(\d{1,2})\.(\d{1,2})-alpha\.(\d+)", version)
          display_version = (
              f"Alpha {int(display_match.group(1))}.{int(display_match.group(2))}.{int(display_match.group(3))}.{int(display_match.group(4))}"
              if display_match
              else version
          )

          print(f"version={version}")
          print(f"display_version={display_version}")
          print(f"tag={tag}")
          PY

          cat version.env >> "$GITHUB_OUTPUT"
          VERSION=$(grep '^version=' version.env | cut -d= -f2-)
          DISPLAY_VERSION=$(grep '^display_version=' version.env | cut -d= -f2-)
          echo "### Alpha version: \`$DISPLAY_VERSION\` (\`$VERSION\`)" >> "$GITHUB_STEP_SUMMARY"

  # ─────────────────────────────────────────────────────────────
  # Phase 2: Build each architecture in parallel
  # tauri build handles signing automatically via env vars
  # ─────────────────────────────────────────────────────────────
  build:
    name: Build (${{ matrix.arch }})
    needs: version
    runs-on: macos-15
    strategy:
      fail-fast: true
      matrix:
        include:
          - arch: aarch64
            target: aarch64-apple-darwin
    steps:
      - uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: 10

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'pnpm'

      - name: Setup Bun (required for bundle-qmd.sh)
        uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest

      - name: Setup Rust
        uses: dtolnay/rust-toolchain@stable
        with:
          targets: ${{ matrix.target }}

      - name: Cache Rust dependencies
        uses: actions/cache@v4
        with:
          path: |
            ~/.cargo/registry
            ~/.cargo/git
            src-tauri/target
          key: ${{ runner.os }}-release-cargo-${{ matrix.target }}-${{ env.RUST_TARGET_CACHE_VERSION }}-${{ hashFiles('src-tauri/Cargo.lock') }}
          restore-keys: |
            ${{ runner.os }}-release-cargo-${{ matrix.target }}-${{ env.RUST_TARGET_CACHE_VERSION }}-

      - name: Install frontend dependencies
        run: pnpm install --frozen-lockfile

      - name: Clear cached bundle artifacts
        run: |
          rm -rf src-tauri/target/${{ matrix.target }}/release/bundle

      - name: Set version
        run: |
          VERSION="${{ needs.version.outputs.version }}"
          jq --arg v "$VERSION" '.version = $v' src-tauri/tauri.conf.json > tmp.json && mv tmp.json src-tauri/tauri.conf.json
          sed -i '' "s/^version = \".*\"/version = \"$VERSION\"/" src-tauri/Cargo.toml

      - name: Import Apple Developer certificate into keychain
        env:
          APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}
          APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}
        run: |
          CERT_PATH="$RUNNER_TEMP/apple_cert.p12"
          KEYCHAIN_PATH="$RUNNER_TEMP/laputa-signing.keychain-db"
          KEYCHAIN_PASSWORD="$(uuidgen)"
          echo "$APPLE_CERTIFICATE" | base64 --decode > "$CERT_PATH"
          security create-keychain -p "$KEYCHAIN_PASSWORD" "$KEYCHAIN_PATH"
          security set-keychain-settings -lut 21600 "$KEYCHAIN_PATH"
          security unlock-keychain -p "$KEYCHAIN_PASSWORD" "$KEYCHAIN_PATH"
          security import "$CERT_PATH" -P "$APPLE_CERTIFICATE_PASSWORD" -A -t cert -f pkcs12 -k "$KEYCHAIN_PATH"
          security list-keychain -d user -s "$KEYCHAIN_PATH"
          security set-key-partition-list -S apple-tool:,apple: -s -k "$KEYCHAIN_PASSWORD" "$KEYCHAIN_PATH"
          echo "KEYCHAIN_PATH=$KEYCHAIN_PATH" >> "$GITHUB_ENV"

      - name: Validate telemetry env
        env:
          VITE_SENTRY_DSN: ${{ secrets.VITE_SENTRY_DSN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          VITE_POSTHOG_KEY: ${{ secrets.VITE_POSTHOG_KEY }}
          VITE_POSTHOG_HOST: ${{ secrets.VITE_POSTHOG_HOST }}
        run: |
          python3 <<'PY'
          import os
          import re
          import sys
          from urllib.parse import urlparse

          DISALLOWED_PLACEHOLDERS = {
              "",
              "-",
              "_",
              "false",
              "true",
              "null",
              "undefined",
              "none",
              "disabled",
          }

          def normalize(name: str) -> str:
              value = os.getenv(name, "").strip()
              if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
                  value = value[1:-1].strip()
              return value

          def normalize_http_like(value: str) -> str:
              if "://" in value:
                  return value
              return f"https://{value}"

          def normalize_hostname(hostname: str) -> str:
              normalized = hostname.strip().rstrip('.').lower()
              if normalized.startswith('[') and normalized.endswith(']'):
                  normalized = normalized[1:-1]
              return normalized

          def is_ip_address(hostname: str) -> bool:
              if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", hostname):
                  return all(0 <= int(part) <= 255 for part in hostname.split('.'))
              return ':' in hostname and re.fullmatch(r"[\da-f:]+", hostname, re.IGNORECASE) is not None

          def is_allowed_hostname(hostname: str) -> bool:
              normalized = normalize_hostname(hostname)
              if not normalized or normalized in DISALLOWED_PLACEHOLDERS:
                  return False
              if normalized == 'localhost':
                  return True
              return '.' in normalized or is_ip_address(normalized)

          def is_http_url(value: str) -> bool:
              parsed = urlparse(normalize_http_like(value))
              return parsed.scheme in {"http", "https"} and is_allowed_hostname(parsed.hostname or "")

          values = {
              name: normalize(name)
              for name in (
                  "VITE_SENTRY_DSN",
                  "SENTRY_DSN",
                  "VITE_POSTHOG_KEY",
                  "VITE_POSTHOG_HOST",
              )
          }
          errors = []

          for name in ("VITE_SENTRY_DSN", "SENTRY_DSN", "VITE_POSTHOG_HOST"):
              value = values[name]
              if value.lower() in DISALLOWED_PLACEHOLDERS:
                  errors.append(f"{name} must be set to a real value, not a placeholder")
              elif not is_http_url(value):
                  errors.append(f"{name} must be a valid http(s) URL with a non-placeholder host")

          if values["VITE_POSTHOG_KEY"].lower() in DISALLOWED_PLACEHOLDERS:
              errors.append("VITE_POSTHOG_KEY must be set to a real project API key, not a placeholder")

          if errors:
              print("Telemetry env validation failed:", file=sys.stderr)
              for error in errors:
                  print(f"- {error}", file=sys.stderr)
              raise SystemExit(1)

          print("Telemetry env validation passed.")
          PY

      - name: Build Tauri app (with signing + notarization)
        env:
          TAURI_SIGNING_PRIVATE_KEY: ${{ secrets.TAURI_SIGNING_PRIVATE_KEY }}
          TAURI_SIGNING_PRIVATE_KEY_PASSWORD: ${{ secrets.TAURI_KEY_PASSWORD }}
          APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}
          APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}
          APPLE_SIGNING_IDENTITY: ${{ secrets.APPLE_SIGNING_IDENTITY }}
          APPLE_ID: ${{ secrets.APPLE_ID }}
          APPLE_PASSWORD: ${{ secrets.APPLE_PASSWORD }}
          APPLE_TEAM_ID: ${{ secrets.APPLE_TEAM_ID }}
          VITE_SENTRY_DSN: ${{ secrets.VITE_SENTRY_DSN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          VITE_POSTHOG_KEY: ${{ secrets.VITE_POSTHOG_KEY }}
          VITE_POSTHOG_HOST: ${{ secrets.VITE_POSTHOG_HOST }}
        run: |
          # Alpha releases only need the notarized app bundle and updater tarball.
          # Skipping DMG packaging avoids fragile bundle_dmg.sh failures on macOS runners.
          pnpm tauri build --target ${{ matrix.target }} --bundles app

      - name: Upload updater artifacts (.tar.gz + .sig)
        uses: actions/upload-artifact@v4
        with:
          name: updater-${{ matrix.arch }}
          path: |
            src-tauri/target/${{ matrix.target }}/release/bundle/macos/*.app.tar.gz
            src-tauri/target/${{ matrix.target }}/release/bundle/macos/*.app.tar.gz.sig
          retention-days: 1

  # ─────────────────────────────────────────────────────────────
  # Phase 3: Publish GitHub Release
  # No lipo/re-signing — use the per-arch artifacts directly
  # ─────────────────────────────────────────────────────────────
  release:
    name: GitHub Release (alpha)
    needs: [version, build]
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Download all artifacts
        uses: actions/download-artifact@v4

      - name: Generate release notes
        run: |
          PREV_TAG=$(python3 <<'PY'
          import re
          import subprocess

          current_tag = '${{ needs.version.outputs.tag }}'
          pattern = re.compile(r'^alpha-v(\d{4})\.(\d{1,2})\.(\d{1,2})-alpha\.(\d+)$')

          output = subprocess.check_output(['git', 'tag', '--list', 'alpha-v*'], text=True).strip()
          tags = [line for line in output.splitlines() if line and line != current_tag]

          parsed_tags = []
          for tag in tags:
              match = pattern.fullmatch(tag)
              if not match:
                  continue
              year, month, day, sequence = map(int, match.groups())
              parsed_tags.append(((year, month, day, sequence), tag))

          print(max(parsed_tags)[1] if parsed_tags else '')
          PY
          )
          if [ -z "$PREV_TAG" ]; then
            NOTES=$(git log --oneline --no-merges -20)
          else
            NOTES=$(git log --oneline --no-merges "${PREV_TAG}..HEAD")
          fi
          {
            echo "## What's Changed (Alpha)"
            echo ""
            echo "$NOTES" | while IFS= read -r line; do echo "- $line"; done
            echo ""
            echo "---"
            echo "**Alpha build — updated on every push to \`main\`**"
            echo ""
            echo "**Requires Apple Silicon (M1/M2/M3)**"
            echo ""
            echo "*Built from \`$(git rev-parse --short HEAD)\` on $(date -u +%Y-%m-%d)*"
          } > release_notes.md

      - name: Build alpha-latest.json
        run: |
          VERSION="${{ needs.version.outputs.version }}"
          TAG="${{ needs.version.outputs.tag }}"
          REPO="${GITHUB_REPOSITORY}"
          REPO_NAME="${REPO#*/}"
          PAGES_URL="https://refactoringhq.github.io/${REPO_NAME}/"

          ARM_SIG=$(cat updater-aarch64/*.app.tar.gz.sig)
          ARM_TARBALL=$(ls updater-aarch64/*.app.tar.gz | xargs basename)

          cat > alpha-latest.json << EOF
          {
            "version": "${VERSION}",
            "notes": "Alpha build. See ${PAGES_URL} for full release notes.",
            "pub_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "platforms": {
              "darwin-aarch64": {
                "signature": "${ARM_SIG}",
                "url": "https://github.com/${REPO}/releases/download/${TAG}/${ARM_TARBALL}"
              }
            }
          }
          EOF
          echo "alpha-latest.json:"; cat alpha-latest.json

      - name: Publish GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          tag_name: ${{ needs.version.outputs.tag }}
          name: Tolaria ${{ needs.version.outputs.display_version }}
          body_path: release_notes.md
          draft: false
          prerelease: true
          files: |
            updater-aarch64/*.app.tar.gz
            updater-aarch64/*.app.tar.gz.sig
            alpha-latest.json

  # ─────────────────────────────────────────────────────────────
  # Phase 4: Update GitHub Pages with release history
  # ─────────────────────────────────────────────────────────────
  pages:
    name: Update release history page
    needs: [version, release]
    runs-on: ubuntu-latest
    permissions:
      contents: write
    concurrency:
      group: github-pages
      cancel-in-progress: false
    steps:
      - uses: actions/checkout@v4

      - name: Setup Bun
        uses: oven-sh/setup-bun@v2
        with:
          bun-version: latest

      - name: Build release history page
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          mkdir -p _site/alpha _site/stable
          gh api -H "Accept: application/vnd.github.html+json" repos/${{ github.repository }}/releases --paginate > _site/releases.json
          PAGES_URL="https://refactoringhq.github.io/${GITHUB_REPOSITORY#*/}"

          gh release download --repo ${{ github.repository }} "${{ needs.version.outputs.tag }}" --pattern "alpha-latest.json" --output _site/alpha/latest.json || echo '{}' > _site/alpha/latest.json
          curl -fsSL "${PAGES_URL}/stable/latest.json" -o _site/stable/latest.json || echo '{}' > _site/stable/latest.json
          bun scripts/build-release-download-page.ts --latest-json _site/stable/latest.json --releases-json _site/releases.json --output-file _site/stable/download/index.html
          bun scripts/build-release-history-page.ts --releases-json _site/releases.json --output-file _site/index.html
          mkdir -p _site/download
          cp _site/stable/download/index.html _site/download/index.html

          cp _site/alpha/latest.json _site/latest.json
          cp _site/alpha/latest.json _site/latest-canary.json

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
          commit_message: "Update release history for ${{ needs.version.outputs.tag }}"
```

### `AGENTS.md`

- Source path: `AGENTS.md`
- Truncated: `no`

```md
# AGENTS.md — Tolaria App

> Quick links: [Architecture](docs/ARCHITECTURE.md) · [Abstractions](docs/ABSTRACTIONS.md) · [Wireframes](ui-design.pen)

---

## 1. Task Workflow

### 1a. Pick up a task

Run `/laputa-next-task` — fetches next task (To Rework first, then Open), moves to In Progress, returns full description.

**Before writing a single line of code:** run `mcp__codescene__code_health_score` to check the current codebase health against `.codescene-thresholds`. If the score is already below the threshold, **stop and refactor first** — find the worst files with the MCP, improve them, commit, then start the task. Never start feature work on a codebase that is already below the gate.

- Read task description and all comments fully
- For To Rework: the ❌ QA failed comment tells you exactly what to fix
- Check `docs/adr/` for relevant architecture decisions before structural choices
- Add a comment: `🚀 Starting work on this task. [Brief description of approach]`

### 1b. Implement

- Work on `main` branch — **no branches, no PRs, ever**. Pre-commit and pre-push block work from any other branch.
- Commit every 20–30 min: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`
- **⛔ NEVER use --no-verify**
- For UI tasks: open `ui-design.pen` first, study visual language, design in light mode

### 1c. When done

**Phase 1 — Playwright (only for core user flows):**

Write Playwright test in `tests/smoke/<slug>.spec.ts` only if feature touches: vault open, note create/save/delete, search, wikilink navigation, git commit/push, conflict resolution. Tag a test with `@smoke` only if it protects a core pre-push workflow. Do NOT tag cosmetic or mock-heavy checks — keep those in the full regression lane. The curated `pnpm playwright:smoke` suite must stay under **5 minutes**; use `pnpm playwright:regression` for the full Playwright pass.

```bash
pnpm dev --port 5201 &
sleep 3
BASE_URL="http://localhost:5201" npx playwright test tests/smoke/<slug>.spec.ts
```

**Phase 2 — Native app QA:**

```bash
pnpm tauri dev &
sleep 10
bash ~/.openclaw/skills/tolaria-qa/scripts/focus-app.sh laputa
bash ~/.openclaw/skills/tolaria-qa/scripts/screenshot.sh /tmp/qa-native.png
```

Use `osascript` for keyboard interactions. Write result as Todoist comment (✅ or ❌). **⚠️ WKWebView:** `osascript keystroke` blocked inside editor — rely on Playwright for text input features.

After both phases pass, add a **completion comment** to the Todoist task before running `/laputa-done`. The comment must include:
- What was implemented (1–2 lines)
- QA: what was tested and how (Playwright / native screenshot / osascript)
- Refactoring: any files refactored to meet the CodeScene gate (or "none needed")
- ADRs: any new/updated ADRs (or "none")
- Docs: any updated docs (ARCHITECTURE.md, ABSTRACTIONS.md, etc.) (or "none")
- Code health: final Hotspot and Average scores after push

Then run `/laputa-done <task_id>` → moves to In Review, notifies Brian, self-dispatches next task.

---

## 2. Development Process

### Commits & pushes

- Push directly to `main` — no PRs, no branches. Pre-push blocks non-`main` pushes.
- Pre-push hook runs full check suite (build + tests + core Playwright smoke + CodeScene)
- **A task is NOT done until `git push origin main` succeeds.** If the hook blocks: read the error, fix it (clippy, tests, CodeScene, build), commit the fix, push again. **⛔ NEVER use --no-verify**

### TDD (mandatory)

Red → Green → Refactor → Commit. One cycle per commit. For bugs: write failing regression test first, then fix. Exception: pure CSS/layout changes.

**Test quality (Kent Beck's Desiderata):** Isolated · Deterministic · Fast · Behavioral · Structure-insensitive · Specific · Predictive. Fix flaky tests first. Prefer E2E over unit tests for user flows.

### Code health (mandatory)

Pre-commit and pre-push hooks enforce **Hotspot Code Health** and **Average Code Health** ≥ thresholds in `.codescene-thresholds`. Both gates block commit/push. Thresholds are a **ratchet** — only go up. When pre-push sees improved remote scores, it updates `.codescene-thresholds`, stages it, and stops so you can commit the new floor with normal verified hooks before pushing again. Never add `// eslint-disable`, `#[allow(...)]`, or `as any`.

**⛔ NEVER edit `.codescene-thresholds` to lower the values.** If the gate blocks you, improve the code — do not lower the bar.

**CodeScene access order:** use CodeScene MCP tools if available. If MCP is unavailable, use the installed `cs` CLI for file-level review/delta work, and use the CodeScene API (`CODESCENE_PAT` + `CODESCENE_PROJECT_ID`) for project-wide Hotspot/Average threshold checks from `.codescene-thresholds`.

**Before editing any existing code file:** capture its current file-level CodeScene score. After your edits, re-run the same file-level review and verify the score is higher. If the file already starts at `10.0`, it must remain `10.0`.

**New files:** every new **scorable code file** must reach CodeScene score `10.0` before commit. If CodeScene reports `null` / "no scorable code" for a new file, it must still have zero CodeScene findings/warnings.

**Before every commit:** run CodeScene file-level review on every touched or newly created code file and verify the rule above. **Boy Scout Rule:** every file you touch must leave with a higher score, unless it was already `10.0`, in which case it must stay `10.0`.

**If CodeScene gate blocks your push:** use `mcp__codescene__code_health_score` to find the worst file, refactor it, commit, push again. Do NOT stop or wait for laputa-refactor — that is a background loop, not a substitute for fixing your own regressions.

### Check suite (runs on every push)
```bash
pnpm lint && npx tsc --noEmit && pnpm test && pnpm test:coverage  # frontend ≥70%
cargo test && cargo llvm-cov --manifest-path src-tauri/Cargo.toml --no-clean --fail-under-lines 85
```

### ADRs & docs

ADRs live in `docs/adr/`. Create in the same commit as the code. Never edit existing — create a new one that supersedes. Use `/create-adr`. **When:** new dependency, storage strategy, platform target, core abstraction, cross-cutting pattern. **Not for:** bug fixes, styling, refactors.

After any Tauri command, new component/hook, data model change, or new integration: update `docs/ARCHITECTURE.md`, `docs/ABSTRACTIONS.md`, and/or `docs/GETTING-STARTED.md` in the same commit.

---

## 3. Product Rules

### Demo vault hygiene (`demo-vault/`, `demo-vault-v2/`)

Default to `demo-vault-v2/` for testing.

- Treat `demo-vault/` and `demo-vault-v2/` as disposable QA fixtures unless the task explicitly changes demo content.
- If you create untracked notes, attachments, or other temporary files there for testing, delete them before the task is complete.
- If you modify tracked demo-vault files only to test or QA behavior, revert those edits before the final commit.
- Before declaring a task done, make sure `git status --short -- demo-vault demo-vault-v2` is empty unless demo fixture changes are part of the task.
- If a fresh run starts and the only local dirt is inside `demo-vault/` or `demo-vault-v2/`, clean those paths first and continue. That case is recoverable QA residue, not a blocker.

### User vault (`~/Laputa/`)

Default to `demo-vault-v2/`. If you must use `~/Laputa/` for testing:
- **Never commit or push** any test notes to the remote vault
- **Delete all test notes from disk** when done — do not leave untitled or temporary notes on the filesystem. Run `cd ~/Laputa && git checkout -- . && git clean -fd` to restore the vault to its last committed state.
- **Rationale:** test notes pollute the local vault over time, making it a collection of nonsensical untitled files. The vault must stay clean on disk, not just on the remote.

### UI design

Open `ui-design.pen` first (light mode). Create `design/<slug>.pen` for the task; on completion merge into `ui-design.pen` and delete it.

### UI components — mandatory rules

**Always use shadcn/ui components.** Never use raw HTML form elements (`<input>`, `<select>`, `<button>`, native `<input type="date">`, etc.) for user-facing UI. Every interactive element must use the shadcn/ui equivalent:

| Need | Use |
|---|---|
| Text input | `Input` from shadcn/ui |
| Dropdown/select | `Select` from shadcn/ui |
| Date picker | `Calendar` + `Popover` from shadcn/ui (NOT native `<input type="date">`) |
| Button | `Button` from shadcn/ui |
| Autocomplete/combobox | Reuse existing combobox components from the app (check `src/components/`) |
| Wikilink picker | Reuse the wikilink autocomplete component already used in the editor and Properties panel |
| Emoji picker | Reuse the emoji picker component already used for note/type icons |
| Color picker | Reuse the color swatch picker used for type customization |
| Toggle/switch | `Switch` or `ToggleGroup` from shadcn/ui |
| Dialog/modal | `Dialog` from shadcn/ui |

**When in doubt:** search `src/components/` for an existing component before building new. **Visual language:** all new UI must feel native to Tolaria — if it looks like a browser default, it's wrong.

---

## 4. Reference

### macOS / Tauri gotchas

- `Option+N` → special chars on macOS. Use `e.code` or `Cmd+N`
- Tauri menu accelerators: `MenuItemBuilder::new(label).accelerator("CmdOrCtrl+1")`
- `app.set_menu()` replaces the ENTIRE menu bar — include all submenus
- `mock-tauri.ts` silently swallows Tauri calls — not a substitute for native testing
### QA scripts

```bash
bash ~/.openclaw/skills/tolaria-qa/scripts/focus-app.sh laputa
bash ~/.openclaw/skills/tolaria-qa/scripts/screenshot.sh /tmp/out.png
bash ~/.openclaw/skills/tolaria-qa/scripts/shortcut.sh "command" "s"
```

### Diagrams

Prefer Mermaid (`flowchart`, `sequenceDiagram`, `classDiagram`, `stateDiagram-v2`). ASCII only for spatial wireframe layouts.
```

### `CLAUDE.md`

- Source path: `CLAUDE.md`
- Truncated: `no`

```md
@AGENTS.md

This file is a Claude Code compatibility shim. Keep shared agent instructions in `AGENTS.md`.
```

### `README.md`

- Source path: `README.md`
- Truncated: `no`

```md
![Latest stable](https://img.shields.io/github/v/release/refactoringhq/tolaria?display_name=tag) [![CI](https://github.com/refactoringhq/tolaria/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/refactoringhq/tolaria/actions/workflows/ci.yml) [![Build](https://github.com/refactoringhq/tolaria/actions/workflows/release.yml/badge.svg?branch=main)](https://github.com/refactoringhq/tolaria/actions/workflows/release.yml) [![Codecov](https://codecov.io/gh/refactoringhq/tolaria/graph/badge.svg?branch=main)](https://codecov.io/gh/refactoringhq/tolaria) [![CodeScene Hotspot Code Health](https://codescene.io/projects/76865/status-badges/hotspot-code-health)](https://codescene.io/projects/76865)

# 💧 Tolaria

Tolaria is a desktop app for Mac for managing **markdown knowledge bases**. People use it for a variety of use cases:

* Operate second brains and personal knowledge
* Organize company docs as context for AI
* Store OpenClaw/assistants memory and procedures

Personally, I use it to **run my life** (hey 👋 [Luca here](http://x.com/lucaronin)). I have a massive workspace of 10,000+ notes, which are the result of my [Refactoring](https://refactoring.fm/) work + a ton of personal journaling and *second braining*.

<img width="1000" height="656" alt="1776506856823-CleanShot_2026-04-18_at_12 06 57_2x" src="https://github.com/user-attachments/assets/8aeafb0a-b236-43c2-a083-ec111f903c38" />

## Walkthroughs

You can find some Loom walkthroughs below — they are short and to the point:
- [How I Organize My Own Tolaria Workspace](https://www.loom.com/share/bb3aaffa238b4be0bd62e4464bca2528)
- [My Inbox Workflow](https://www.loom.com/share/dffda263317b4fa8b47b59cdf9330571)
- [How I Save Web Resources to Tolaria](https://www.loom.com/share/8a3c1776f801402ebbf4d7b0f31e9882)

## Principles

- 📑 **Files-first** — Your notes are plain markdown files. They're portable, work with any editor, and require no export step. Your data belongs to you, not to any app.
- 🔌 **Git-first** — Every vault is a git repository. You get full version history, the ability to use any git remote, and zero dependency on Tolaria servers.
- 🛜 **Offline-first, zero lock-in** — No accounts, no subscriptions, no cloud dependencies. Your vault works completely offline and always will. If you stop using Tolaria, you lose nothing.
- 🔬 **Open source** — Tolaria is free and open source. I built this for [myself](https://x.com/lucaronin) and for sharing it with others.
- 📋 **Standards-based** — Notes are markdown files with YAML frontmatter. No proprietary formats, no locked-in data. Everything works with standard tools if you decide to move away from Tolaria.
- 🔍 **Types as lenses, not schemas** — Types in Tolaria are navigation aids, not enforcement mechanisms. There's no required fields, no validation, just helpful categories for finding notes.
- 🪄**AI-first but not AI-only** — A vault of files works very well with AI agents, but you are free to use whatever you want. We support Claude Code and Codex CLI (for now), but you can edit the vault with any AI you want. We provide an AGENTS file for your agents to figure out.
- ⌨️ **Keyboard-first** — Tolaria is designed for power-users who want to use keyboard as much as possible. A lot of how we designed the Editor and the Command Palette is based on this.
- 💪 **Built from real use** — Tolaria was created for manage my personal vault of 10,000+ notes, and I use it every day. Every feature exists because it solved a real problem.

## Getting started

Download the [latest release here](https://github.com/refactoringhq/tolaria/releases/latest/download/Tolaria.app.tar.gz).

When you open Tolaria for the first time you get the chance of cloning the [getting started vault](https://github.com/refactoringhq/tolaria-getting-started) — which gives you a walkthrough of the whole app.

## Open source and local setup

Tolaria is open source and built with Tauri, React, and TypeScript. If you want to run or contribute to the app locally, here is [how to get started](https://github.com/refactoringhq/tolaria/blob/main/docs/GETTING-STARTED.md). You can also find the gist below 👇

### Prerequisites

- Node.js 20+
- pnpm 8+
- Rust stable
- macOS for development

### Quick start

```bash
pnpm install
pnpm dev
```

Open `http://localhost:5173` for the browser-based mock mode, or run the native desktop app with:

```bash
pnpm tauri dev
```

## Tech Docs

- 📐 [ARCHITECTURE.md](docs/ARCHITECTURE.md) — System design, tech stack, data flow
- 🧩 [ABSTRACTIONS.md](docs/ABSTRACTIONS.md) — Core abstractions and models
- 🚀 [GETTING-STARTED.md](docs/GETTING-STARTED.md) — How to navigate the codebase
- 📚 [ADRs](docs/adr) — Architecture Decision Records

## Security

If you believe you have found a security issue, please report it privately as described in [SECURITY.md](./SECURITY.md).

## License

Tolaria is licensed under AGPL-3.0-or-later. The Tolaria name and logo remain covered by the project’s trademark policy.
```

### `package.json`

- Source path: `package.json`
- Truncated: `no`

```json
{
  "name": "tolaria",
  "private": true,
  "license": "AGPL-3.0-or-later",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "bundle-mcp": "node scripts/bundle-mcp-server.mjs",
    "lint": "eslint .",
    "preview": "vite preview",
    "tauri": "tauri",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:e2e": "playwright test",
    "playwright:smoke": "playwright test --config playwright.smoke.config.ts tests/smoke/example.spec.ts tests/smoke/fix-ai-chat-empty-body-v3.spec.ts tests/smoke/fix-crash-create-note.spec.ts tests/smoke/fresh-start-telemetry-onboarding.spec.ts tests/smoke/getting-started-template.spec.ts tests/smoke/h1-title-decoupled.spec.ts tests/smoke/h1-untitled-auto-rename.spec.ts tests/smoke/keyboard-command-routing.spec.ts tests/smoke/linkify-init-warnings.spec.ts tests/smoke/multi-selection-shortcuts.spec.ts tests/smoke/wikilink-path-fix.spec.ts",
    "playwright:regression": "playwright test tests/smoke/",
    "playwright:integration": "playwright test --config playwright.integration.config.ts",
    "test:coverage": "node scripts/run-vitest-coverage.mjs",
    "prepare": "husky"
  },
  "dependencies": {
    "@anthropic-ai/sdk": "^0.78.0",
    "@blocknote/code-block": "^0.46.2",
    "@blocknote/core": "^0.46.2",
    "@blocknote/mantine": "^0.46.2",
    "@blocknote/react": "^0.46.2",
    "@codemirror/commands": "^6.10.2",
    "@codemirror/lang-markdown": "^6.5.0",
    "@codemirror/lang-yaml": "^6.1.2",
    "@codemirror/language": "^6.12.2",
    "@codemirror/state": "^6.5.4",
    "@codemirror/view": "^6.39.16",
    "@dnd-kit/core": "^6.3.1",
    "@dnd-kit/sortable": "^10.0.0",
    "@dnd-kit/utilities": "^3.2.2",
    "@lezer/highlight": "^1.2.3",
    "@mantine/core": "^8.3.14",
    "@phosphor-icons/react": "^2.1.10",
    "@radix-ui/react-dialog": "^1.1.15",
    "@radix-ui/react-dropdown-menu": "^2.1.16",
    "@radix-ui/react-select": "^2.2.6",
    "@radix-ui/react-separator": "^1.1.8",
    "@radix-ui/react-slot": "^1.2.4",
    "@radix-ui/react-tabs": "^1.1.13",
    "@radix-ui/react-tooltip": "^1.2.8",
    "@sentry/react": "^10.47.0",
    "@tailwindcss/vite": "^4.1.18",
    "@tauri-apps/api": "^2.10.1",
    "@tauri-apps/plugin-dialog": "^2.6.0",
    "@tauri-apps/plugin-opener": "^2.5.3",
    "@tauri-apps/plugin-process": "^2.3.1",
    "@tauri-apps/plugin-updater": "^2.10.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "date-fns": "^4.1.0",
    "katex": "^0.16.28",
    "lucide-react": "^0.564.0",
    "posthog-js": "^1.363.5",
    "radix-ui": "^1.4.3",
    "react": "^19.2.0",
    "react-day-picker": "^9.13.2",
    "react-dom": "^19.2.0",
    "react-markdown": "^10.1.0",
    "react-virtuoso": "^4.18.1",
    "rehype-highlight": "^7.0.2",
    "remark-gfm": "^4.0.1",
    "tailwind-merge": "^3.4.1",
    "tailwindcss": "^4.1.18",
    "tw-animate-css": "^1.4.0",
    "unicode-emoji-json": "^0.8.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.1",
    "@playwright/test": "^1.58.2",
    "@tauri-apps/cli": "^2.10.0",
    "@testing-library/jest-dom": "^6.9.1",
    "@testing-library/react": "^16.3.2",
    "@types/node": "^24.10.1",
    "@types/react": "^19.2.7",
    "@types/react-dom": "^19.2.3",
    "@types/ws": "^8.18.1",
    "@vitejs/plugin-react": "^5.1.1",
    "@vitest/coverage-v8": "^4.0.18",
    "esbuild": "^0.27.3",
    "eslint": "^9.39.1",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-react-refresh": "^0.4.24",
    "globals": "^16.5.0",
    "gray-matter": "^4.0.3",
    "husky": "^9.1.7",
    "jsdom": "^28.0.0",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.48.0",
    "vite": "^7.3.1",
    "vitest": "^4.0.18",
    "ws": "^8.19.0"
  }
}
```

### `pnpm-workspace.yaml`

- Source path: `pnpm-workspace.yaml`
- Truncated: `no`

```yaml
packages:
  - mcp-server

ignoredBuiltDependencies:
  - esbuild

patchedDependencies:
  '@blocknote/core@0.46.2': patches/@blocknote__core@0.46.2.patch
  '@blocknote/react@0.46.2': patches/@blocknote__react@0.46.2.patch
  '@tiptap/extension-link@3.19.0': patches/@tiptap__extension-link@3.19.0.patch
  prosemirror-tables@1.8.5: patches/prosemirror-tables@1.8.5.patch
```
