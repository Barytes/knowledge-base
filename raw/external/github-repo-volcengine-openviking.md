---
title: "GitHub repo snapshot: volcengine/openviking"
source: "https://github.com/volcengine/openviking"
author:
published:
created: 2026-04-29
description: "Compact GitHub repository evidence snapshot for repo-map-ingest."
tags:
  - "github"
  - "repo-snapshot"
---

# GitHub Repo Snapshot: `volcengine/openviking`

## Observation Scope

- Repository: `volcengine/openviking`
- URL: https://github.com/volcengine/openviking
- Requested topic: 仓库架构与工程实践
- Observed ref: `main`
- Latest resolved commit: `39b124d037ff7f2f6ecc4cab7560a359468fd641`
- Commit date: `2026-04-29T02:55:57Z`
- Snapshot date (UTC): `2026-04-29`

## Repository Metadata

- Description: OpenViking is an open-source context database designed specifically for AI Agents(such as openclaw). OpenViking unifies the management of context (memory, resources, and skills) that Agents need through a file system paradigm, enabling hierarchical context delivery and self-evolving.
- Default branch: `main`
- Language: `Python`
- Stars: `23219`
- Forks: `1707`
- Open issues: `242`

## Top-Level Tree

### Directories

- `.github`
- `benchmark`
- `bot`
- `build_support`
- `crates`
- `deploy`
- `docker`
- `docs`
- `examples`
- `openviking`
- `openviking_cli`
- `src`
- `tests`
- `third_party`

### Files

- `.clang-format`
- `.gitignore`
- `.ingest_record.json`
- `.pr_agent.toml`
- `.pre-commit-config.yaml`
- `CONTRIBUTING.md`
- `CONTRIBUTING_CN.md`
- `CONTRIBUTING_JA.md`
- `Cargo.lock`
- `Cargo.toml`
- `Dockerfile`
- `LICENSE`
- `MANIFEST.in`
- `Makefile`
- `README.md`
- `README_CN.md`
- `README_JA.md`
- `SECURITY.md`
- `docker-compose.yml`
- `pyproject.toml`
- `setup.py`
- `uv.lock`

## Selected Evidence Anchors

- `.github/workflows/_build.yml`
- `.github/workflows/_codeql.yml`
- `.github/workflows/_docs-deploy.yml`
- `.github/workflows/_docs.yml`
- `.github/workflows/_lint.yml`
- `.github/workflows/_publish.yml`
- `.github/workflows/_test_full.yml`
- `.github/workflows/_test_lite.yml`
- `.github/workflows/api_test.yml`
- `.github/workflows/api_test_effect.yml`
- `.github/workflows/build-docker-image.yml`
- `.github/workflows/ci.yml`
- `Cargo.toml`
- `Dockerfile`
- `Makefile`
- `README.md`
- `docker-compose.yml`
- `pyproject.toml`
- `setup.py`

## Captured Files

### `.github/workflows/_build.yml`

- Source path: `.github/workflows/_build.yml`
- Truncated: `no`

```yaml
name: 15. _Build Distribution

on:
  workflow_call:
    inputs:
      os_json:
        description: 'JSON string of runner labels to build on (ubuntu-24.04=x86_64, ubuntu-24.04-arm=aarch64, macos-14=arm64, macos-15-intel=x86_64, windows-latest=x86_64)'
        required: false
        type: string
        default: '["ubuntu-24.04", "ubuntu-24.04-arm", "macos-14", "macos-15-intel", "windows-latest"]'
      python_json:
        description: 'JSON string of Python versions'
        required: false
        type: string
        default: '["3.10"]'
      build_sdist:
        description: 'Whether to build source distribution'
        required: false
        type: boolean
        default: true
      build_wheels:
        description: 'Whether to build wheel distribution'
        required: false
        type: boolean
        default: true
  workflow_dispatch:
    inputs:
      build_sdist:
        description: 'Whether to build source distribution'
        required: false
        type: boolean
        default: true
      build_wheels:
        description: 'Whether to build wheel distribution'
        required: false
        type: boolean
        default: true
      os_json:
        description: 'JSON string of runner labels to build on (ubuntu-24.04=x86_64, ubuntu-24.04-arm=aarch64, macos-14=arm64, macos-15-intel=x86_64, windows-latest=x86_64)'
        required: false
        default: '["ubuntu-24.04", "ubuntu-24.04-arm", "macos-14", "macos-15-intel", "windows-latest"]'
      python_json:
        description: 'JSON string of Python versions'
        required: false
        default: '["3.10"]'

jobs:
  build-sdist:
    name: Build source distribution py3.12
    if: inputs.build_sdist
    runs-on: ubuntu-24.04
    steps:
    - uses: actions/checkout@v6
      with:
        submodules: recursive
        fetch-depth: 0  # Required for setuptools_scm to detect version from git tags

    - name: Fetch all tags
      run: git fetch --force --tags

    - name: Set up Python
      uses: actions/setup-python@v6
      with:
        python-version: '3.12'

    - name: Install uv
      uses: astral-sh/setup-uv@v7
      with:
        enable-cache: true

    - name: Create venv
      run: uv venv

    - name: Install build dependencies
      run: uv pip install build setuptools_scm

    - name: Clean workspace (force ignore dirty)
      shell: bash
      run: |
        git reset --hard HEAD
        git clean -fd
        # For sdist, ensure local runtime binaries are not packaged even if present
        # Ignore uv.lock changes to avoid dirty state in setuptools_scm
        git update-index --assume-unchanged uv.lock || true

    - name: Debug Git and SCM
      shell: bash
      run: |
        echo "=== Git Describe ==="
        git describe --tags --long --dirty --always
        echo "=== Setuptools SCM Version ==="
        uv run --frozen python -m setuptools_scm
        echo "=== Git Status (Ignored included) ==="
        git status --ignored
        echo "=== Check openviking/_version.py ==="
        if [ -f openviking/_version.py ]; then cat openviking/_version.py; else echo "Not found"; fi

    - name: Build sdist
      run: uv build --sdist

    - name: Store the distribution packages
      uses: actions/upload-artifact@v7
      with:
        name: python-package-distributions-sdist
        path: dist/*.tar.gz

    - name: Display built sdist version
      continue-on-error: true
      run: |
        VERSION=$(ls dist/*.tar.gz | head -n 1 | xargs basename | sed -E 's/^[^-]+-(.+)\.tar\.gz$/\1/')
        echo "Build Version: $VERSION"
        echo "::notice::Build sdist Version: $VERSION"

  build-linux:
    name: Build distribution on Linux ${{ matrix.arch }} (glibc 2.31) py${{ matrix.python-version }}
    # Run if Linux runners are requested (explicit labels or generic 'linux')
    if: >-
      inputs.build_wheels &&
      (
        contains(inputs.os_json, 'linux') ||
        contains(inputs.os_json, '"ubuntu-24.04"') ||
        contains(inputs.os_json, 'ubuntu-24.04-arm')
      )
    runs-on: ${{ matrix.arch == 'aarch64' && 'ubuntu-24.04-arm' || 'ubuntu-24.04' }}
    container: ubuntu:20.04
    env:
      DEBIAN_FRONTEND: noninteractive
      TZ: Etc/UTC
    strategy:
      fail-fast: false
      matrix:
        python-version: ${{ fromJson(inputs.python_json) }}
        arch: ${{ contains(inputs.os_json, 'linux') && fromJson('["x86_64","aarch64"]') || (contains(inputs.os_json, '"ubuntu-24.04"') && contains(inputs.os_json, 'ubuntu-24.04-arm')) && fromJson('["x86_64","aarch64"]') || contains(inputs.os_json, 'ubuntu-24.04-arm') && fromJson('["aarch64"]') || fromJson('["x86_64"]') }}
    
    steps:
    - name: Install system dependencies (Linux)
      run: |
        # Replace archive.ubuntu.com with azure.archive.ubuntu.com for better stability in GH Actions
        sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/azure.archive.ubuntu.com\/ubuntu\//g' /etc/apt/sources.list
        # Retry apt-get update
        for i in 1 2 3 4 5; do apt-get update && break || sleep 5; done
        apt-get install -y \
          git ca-certificates cmake build-essential clang tzdata curl \
          libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
          libffi-dev liblzma-dev libgdbm-dev libnss3-dev libncurses5-dev \
          libncursesw5-dev tk-dev uuid-dev libexpat1-dev
        ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime
        dpkg-reconfigure -f noninteractive tzdata

    - name: Select compiler toolchain (Linux)
      run: |
        echo "CC=clang" >> "$GITHUB_ENV"
        echo "CXX=clang++" >> "$GITHUB_ENV"
        echo "OV_REQUIRE_RAGFS_BUILD=1" >> "$GITHUB_ENV"
        clang --version
        clang++ --version

    - uses: actions/checkout@v6
      with:
        submodules: recursive
        fetch-depth: 0  # Required for setuptools_scm to detect version from git tags

    - name: Fetch all tags
      run: |
        git config --global --add safe.directory "$GITHUB_WORKSPACE"
        git fetch --force --tags

    - name: Build CPython (Dynamic Selection)
      run: |
        # Map short version to full version for our specific build environment
        PYTHON_VERSION="${{ matrix.python-version }}"
        case "$PYTHON_VERSION" in
          "3.9") PYTHON_FULL="3.9.18" ;;
          "3.10") PYTHON_FULL="3.10.13" ;;
          "3.11") PYTHON_FULL="3.11.8" ;;
          "3.12") PYTHON_FULL="3.12.2" ;;
          "3.13") PYTHON_FULL="3.13.2" ;;
          "3.14") PYTHON_FULL="3.14.3" ;;
          *)
            echo "Error: Unknown python version $PYTHON_VERSION"
            exit 1
            ;;
        esac
        
        PYTHON_PREFIX="/opt/python/${PYTHON_FULL}"
        PYTHON_BIN="${PYTHON_PREFIX}/bin/python${{ matrix.python-version }}"
        if [ ! -x "$PYTHON_BIN" ]; then
          curl -fsSL -o /tmp/Python-${PYTHON_FULL}.tgz \
            https://www.python.org/ftp/python/${PYTHON_FULL}/Python-${PYTHON_FULL}.tgz
          tar -xzf /tmp/Python-${PYTHON_FULL}.tgz -C /tmp
          cd /tmp/Python-${PYTHON_FULL}
          CFLAGS="-fPIC" \
          ./configure --prefix="${PYTHON_PREFIX}" --with-ensurepip=install --enable-shared
          make -j"$(nproc)"
          make install
        fi
        echo "PYTHON_BIN=${PYTHON_BIN}" >> "$GITHUB_ENV"
        echo "LD_LIBRARY_PATH=${PYTHON_PREFIX}/lib:${LD_LIBRARY_PATH}" >> "$GITHUB_ENV"
        export LD_LIBRARY_PATH="${PYTHON_PREFIX}/lib:${LD_LIBRARY_PATH}"
        "$PYTHON_BIN" -V
    - name: Set up Rust
      uses: dtolnay/rust-toolchain@v1
      with:
        toolchain: stable
        targets: ${{ matrix.arch == 'aarch64' && 'aarch64-unknown-linux-gnu' || 'x86_64-unknown-linux-gnu' }}
    - name: Install uv
      uses: astral-sh/setup-uv@v7
      with:
        enable-cache: true

    - name: Create venv (Linux)
      run: uv venv --python "$PYTHON_BIN"

    - name: Seed pip (Linux)
      run: uv run python -m ensurepip --upgrade

    - name: Install dependencies
      run: uv sync --frozen

    - name: Install build dependencies
      run: uv pip install setuptools setuptools_scm cmake wheel build

    - name: Resolve OpenViking version for Rust CLI (Linux)
      shell: bash
      run: |
        OPENVIKING_VERSION=$(
          uv run --frozen python -c "from build_support.versioning import resolve_openviking_version; print(resolve_openviking_version())"
        )
        echo "OPENVIKING_VERSION=$OPENVIKING_VERSION" >> "$GITHUB_ENV"
        echo "Resolved OpenViking version: $OPENVIKING_VERSION"

    - name: Build Rust CLI (Linux)
      run: cargo build --release --target ${{ matrix.arch == 'aarch64' && 'aarch64-unknown-linux-gnu' || 'x86_64-unknown-linux-gnu' }} -p ov_cli

    - name: Copy Rust CLI binary (Linux)
      run: |
        mkdir -p openviking/bin
        cp target/${{ matrix.arch == 'aarch64' && 'aarch64-unknown-linux-gnu' || 'x86_64-unknown-linux-gnu' }}/release/ov openviking/bin/
        chmod +x openviking/bin/ov

    - name: Clean workspace (force ignore dirty)
      shell: bash
      run: |
        # Back up pre-built artifacts before cleaning
        cp -a openviking/bin /tmp/_ov_bin || true
        git reset --hard HEAD
        git clean -fd
        rm -rf openviking/_version.py openviking.egg-info
        # Restore pre-built artifacts
        cp -a /tmp/_ov_bin openviking/bin || true
        # Ignore uv.lock changes to avoid dirty state in setuptools_scm
        git update-index --assume-unchanged uv.lock || true

    - name: Debug Git and SCM
      shell: bash
      run: |
        echo "=== Git Describe ==="
        git describe --tags --long --dirty --always
        echo "=== Setuptools SCM Version ==="
        uv run --frozen python -m setuptools_scm
        echo "=== Git Status (Ignored included) ==="
        git status --ignored
        echo "=== Check openviking/_version.py ==="
        if [ -f openviking/_version.py ]; then cat openviking/_version.py; else echo "Not found"; fi
        echo "=== Verify pre-built artifacts survived clean ==="
        ls -la openviking/bin/ || true

    - name: Build package (Wheel Only)
      run: uv build --wheel

    - name: Install patchelf (Linux)
      run: |
        PATCHELF_VERSION=0.18.0
        curl -fsSL -o /tmp/patchelf-${PATCHELF_VERSION}.tar.gz \
          https://github.com/NixOS/patchelf/releases/download/${PATCHELF_VERSION}/patchelf-${PATCHELF_VERSION}.tar.gz
        tar -xzf /tmp/patchelf-${PATCHELF_VERSION}.tar.gz -C /tmp
        cd /tmp/patchelf-${PATCHELF_VERSION}
        ./configure
        make -j"$(nproc)"
        make install
        patchelf --version

    - name: Repair wheels (Linux)
      run: |
        uv pip install auditwheel
        uv run auditwheel repair dist/*.whl -w dist_fixed
        rm dist/*.whl
        mv dist_fixed/*.whl dist/
        rmdir dist_fixed

    - name: Smoke test built wheel (Linux)
      shell: bash
      run: |
        "$PYTHON_BIN" -m pip install --upgrade pip
        "$PYTHON_BIN" -m pip install --force-reinstall dist/*.whl

        cd "$RUNNER_TEMP"
        "$PYTHON_BIN" - <<'PY'
        import importlib.util

        from openviking.pyagfs import get_binding_client
        import openviking.storage.vectordb.engine as engine

        binding_client, _ = get_binding_client()
        if binding_client is None:
            raise SystemExit("ragfs binding client was not installed")

        print(f"Loaded RAGFS binding client {binding_client.__name__}")
        print(f"Loaded runtime engine variant {engine.ENGINE_VARIANT}")
        print(f"Available engine variants {engine.AVAILABLE_ENGINE_VARIANTS}")

        module_name = f"openviking.storage.vectordb.engine._{engine.ENGINE_VARIANT}"
        backend_spec = importlib.util.find_spec(module_name)
        if backend_spec is None or backend_spec.origin is None:
            raise SystemExit(f"backend module {module_name} was not installed")

        print(f"Imported backend module {module_name}")
        print(f"Backend module origin {backend_spec.origin}")
        PY

    - name: Store the distribution packages
      uses: actions/upload-artifact@v7
      with:
        name: python-package-distributions-linux-${{ matrix.arch }}-${{ matrix.python-version }}
        path: dist/

    - name: Display built wheel version
      continue-on-error: true
      run: |
        VERSION=$(ls dist/*.whl | head -n 1 | xargs basename | cut -d- -f2)
        echo "Build Version: $VERSION"
        echo "::notice::Build Wheel Version (Linux ${{ matrix.arch }} glibc 2.31 py${{ matrix.python-version }}): $VERSION"

  build-other:
    name: Build non-Linux distributions
    # Run only when non-Linux runners are explicitly requested
    if: inputs.build_wheels && (contains(inputs.os_json, 'macos') || contains(inputs.os_json, 'windows'))
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: ${{ fromJson(inputs.os_json) }}
        python-version: ${{ fromJson(inputs.python_json) }}
        # Exclude ubuntu-24.04 from this matrix if it was passed in inputs
        exclude:
          - os: linux
          - os: ubuntu-24.04
          - os: ubuntu-24.04-arm

    steps:
    - uses: actions/checkout@v6
      with:
        submodules: recursive
        fetch-depth: 0  # Required for setuptools_scm to detect version from git tags

    - name: Fetch all tags
      run: git fetch --force --tags

    - name: Set up Python
      uses: actions/setup-python@v6
      with:
        python-version: ${{ matrix.python-version }}

    - name: Configure macOS wheel architecture tag
      if: runner.os == 'macOS'
      shell: bash
      run: |
        if [[ "${{ matrix.os }}" == "macos-14" ]]; then
          TARGET_ARCH="arm64"
          MACOS_VERSION="14.0"
        elif [[ "${{ matrix.os }}" == "macos-15-intel" ]]; then
          TARGET_ARCH="x86_64"
          MACOS_VERSION="15.0"
        else
          echo "Unsupported macOS runner for release wheels: ${{ matrix.os }}"
          exit 1
        fi

        echo "ARCHFLAGS=-arch ${TARGET_ARCH}" >> "$GITHUB_ENV"
        echo "CMAKE_OSX_ARCHITECTURES=${TARGET_ARCH}" >> "$GITHUB_ENV"
        echo "_PYTHON_HOST_PLATFORM=macosx-${MACOS_VERSION}-${TARGET_ARCH}" >> "$GITHUB_ENV"
        echo "Configured macOS wheel platform: macosx-${MACOS_VERSION}-${TARGET_ARCH}"

    - name: Set up Rust
      uses: dtolnay/rust-toolchain@v1
      with:
        toolchain: stable
    - name: Install uv
      uses: astral-sh/setup-uv@v7
      with:
        enable-cache: true

    - name: Install system dependencies (macOS)
      if: runner.os == 'macOS'
      run: brew install cmake

    - name: Install system dependencies (Windows)
      if: runner.os == 'Windows'
      run: |
        choco install cmake --installargs 'ADD_CMAKE_TO_PATH=System'
        choco install mingw

    - name: Install dependencies
      run: uv sync --frozen

    - name: Install build dependencies
      run: uv pip install setuptools setuptools_scm cmake wheel build

    - name: Require ragfs native artifact for wheel builds
      shell: bash
      run: echo "OV_REQUIRE_RAGFS_BUILD=1" >> "$GITHUB_ENV"

    - name: Resolve OpenViking version for Rust CLI (macOS/Windows)
      shell: bash
      run: |
        OPENVIKING_VERSION=$(
          uv run --frozen python -c "from build_support.versioning import resolve_openviking_version; print(resolve_openviking_version())"
        )
        echo "OPENVIKING_VERSION=$OPENVIKING_VERSION" >> "$GITHUB_ENV"
        echo "Resolved OpenViking version: $OPENVIKING_VERSION"

    - name: Build Rust CLI (macOS/Windows)
      shell: bash
      run: |
        if [[ "${{ matrix.os }}" == "windows-latest" ]]; then
          cargo build --release --target x86_64-pc-windows-msvc -p ov_cli
        else
          cargo build --release -p ov_cli
        fi

    - name: Copy Rust CLI binary (macOS/Windows)
      shell: bash
      run: |
        mkdir -p openviking/bin
        if [[ "${{ matrix.os }}" == "windows-latest" ]]; then
          cp target/x86_64-pc-windows-msvc/release/ov.exe openviking/bin/
        else
          cp target/release/ov openviking/bin/
          chmod +x openviking/bin/ov
        fi

    - name: Clean workspace (force ignore dirty)
      shell: bash
      run: |
        # Back up pre-built artifacts before cleaning
        cp -a openviking/bin /tmp/_ov_bin || true
        git reset --hard HEAD
        git clean -fd
        rm -rf openviking/_version.py openviking.egg-info
        # Restore pre-built artifacts
        cp -a /tmp/_ov_bin openviking/bin || true
        # Ignore uv.lock changes to avoid dirty state in setuptools_scm
        git update-index --assume-unchanged uv.lock || true

    - name: Debug Git and SCM
      shell: bash
      run: |
        echo "=== Git Describe ==="
        git describe --tags --long --dirty --always
        echo "=== Setuptools SCM Version ==="
        uv run --frozen python -m setuptools_scm
        echo "=== Git Status (Ignored included) ==="
        git status --ignored
        echo "=== Check openviking/_version.py ==="
        if [ -f openviking/_version.py ]; then cat openviking/_version.py; else echo "Not found"; fi
        echo "=== Verify pre-built artifacts survived clean ==="
        ls -la openviking/bin/ || true

    - name: Build package (Wheel Only)
      run: uv build --wheel

    - name: Smoke test built wheel (macOS)
      if: runner.os == 'macOS'
      shell: bash
      run: |
        python -m pip install --upgrade pip
        python -m pip install --force-reinstall dist/*.whl

        cd "$RUNNER_TEMP"
        python - <<'PY'
        import importlib.util

        from openviking.pyagfs import get_binding_client
        import openviking.storage.vectordb.engine as engine

        binding_client, _ = get_binding_client()
        if binding_client is None:
            raise SystemExit("ragfs binding client was not installed")

        print(f"Loaded RAGFS binding client {binding_client.__name__}")
        print(f"Loaded runtime engine variant {engine.ENGINE_VARIANT}")
        print(f"Available engine variants {engine.AVAILABLE_ENGINE_VARIANTS}")

        module_name = f"openviking.storage.vectordb.engine._{engine.ENGINE_VARIANT}"
        backend_spec = importlib.util.find_spec(module_name)
        if backend_spec is None or backend_spec.origin is None:
            raise SystemExit(f"backend module {module_name} was not installed")

        print(f"Imported backend module {module_name}")
        print(f"Backend module origin {backend_spec.origin}")
        PY

    - name: Smoke test built wheel (Windows)
      if: runner.os == 'Windows'
      shell: bash
      run: |
        python -m pip install --upgrade pip
        python -m pip install --force-reinstall dist/*.whl

        cd "$RUNNER_TEMP"
        python - <<'PY'
        import importlib.util

        import openviking.storage.vectordb.engine as engine

        print(f"Loaded runtime engine variant {engine.ENGINE_VARIANT}")
        print(f"Available engine variants {engine.AVAILABLE_ENGINE_VARIANTS}")

        module_name = f"openviking.storage.vectordb.engine._{engine.ENGINE_VARIANT}"
        backend_spec = importlib.util.find_spec(module_name)
        if backend_spec is None or backend_spec.origin is None:
            raise SystemExit(f"backend module {module_name} was not installed")

        print(f"Imported backend module {module_name}")
        print(f"Backend module origin {backend_spec.origin}")
        PY

    - name: Store the distribution packages
      uses: actions/upload-artifact@v7
      with:
        name: python-package-distributions-${{ matrix.os == 'macos-14' && 'macos-arm64' || matrix.os == 'macos-15-intel' && 'macos-x86_64' || matrix.os == 'windows-latest' && 'windows-x86_64' || matrix.os }}-${{ matrix.python-version }}
        path: dist/

    - name: Display built wheel version
      shell: bash
      continue-on-error: true
      run: |
        VERSION=$(ls dist/*.whl | head -n 1 | xargs basename | cut -d- -f2)
        echo "Build Version: $VERSION"
        echo "::notice::Build Wheel Version (${{ matrix.os == 'macos-14' && 'macOS arm64 (macos-14)' || matrix.os == 'macos-15-intel' && 'macOS x86_64 (macos-15-intel)' || matrix.os == 'windows-latest' && 'Windows x86_64 (windows-latest)' || matrix.os }} py${{ matrix.python-version }}): $VERSION"
```

### `.github/workflows/_codeql.yml`

- Source path: `.github/workflows/_codeql.yml`
- Truncated: `no`

```yaml
name: 14. _CodeQL Scan

on:
  workflow_call:
  workflow_dispatch:

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-24.04
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: [ 'python', 'cpp' ]

    steps:
    - name: Checkout repository
      uses: actions/checkout@v6
      with:
        submodules: recursive

    - name: Set up Python
      uses: actions/setup-python@v6
      with:
        python-version: '3.11'

    - name: Install uv
      uses: astral-sh/setup-uv@v7
      with:
        enable-cache: true

    - name: Install system dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y cmake build-essential

    - name: Install dependencies
      run: |
        uv sync --frozen
        uv pip install setuptools setuptools_scm cmake wheel

    - name: Initialize CodeQL
      uses: github/codeql-action/init@v4
      with:
        languages: ${{ matrix.language }}
        queries: security-and-quality

    - name: Build extensions
      if: matrix.language == 'cpp'
      run: uv run python setup.py build_ext --inplace

    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v4
      with:
        category: "/language:${{ matrix.language }}"
```

### `.github/workflows/_docs-deploy.yml`

- Source path: `.github/workflows/_docs-deploy.yml`
- Truncated: `no`

```yaml
name: 18. _Docs Deploy

on:
  workflow_call:

jobs:
  deploy:
    name: Build and Deploy Docs
    runs-on: ubuntu-24.04
    permissions:
      contents: read
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v6

      - name: Set up Node.js
        uses: actions/setup-node@v6
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: docs/package-lock.json

      - name: Install docs dependencies
        run: npm ci
        working-directory: docs

      - name: Build docs
        run: npm run docs:build
        working-directory: docs
        env:
          DOCS_BASE: /

      - name: Configure GitHub Pages
        uses: actions/configure-pages@v6

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v4
        with:
          path: docs/.vitepress/dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v5
```

### `.github/workflows/_docs.yml`

- Source path: `.github/workflows/_docs.yml`
- Truncated: `no`

```yaml
name: 17. _Docs Build

on:
  workflow_call:

jobs:
  build:
    name: Build Docs
    runs-on: ubuntu-24.04
    permissions:
      contents: read
    steps:
      - name: Checkout repository
        uses: actions/checkout@v6

      - name: Set up Node.js
        uses: actions/setup-node@v6
        with:
          node-version: 22
          cache: npm
          cache-dependency-path: docs/package-lock.json

      - name: Install docs dependencies
        run: npm ci
        working-directory: docs

      - name: Build docs
        run: npm run docs:build
        working-directory: docs
        env:
          DOCS_BASE: /
```

### `.github/workflows/_lint.yml`

- Source path: `.github/workflows/_lint.yml`
- Truncated: `no`

```yaml
name: 11. _Lint Checks

on:
  workflow_call:
  workflow_dispatch:

jobs:
  lint:
    runs-on: ubuntu-24.04
    steps:
    - uses: actions/checkout@v6
      with:
        fetch-depth: 0 # Required to calculate the git diff



    - name: Set up Python
      uses: actions/setup-python@v6
      with:
        python-version: '3.11'

    - name: Install uv
      uses: astral-sh/setup-uv@v7
      with:
        enable-cache: true

    - name: Install dependencies
      run: uv sync --frozen --extra dev

    # --- NEW STEP: Get the list of changed files ---
    - name: Get changed files
      id: files
      run: |
        # Compare the PR head to the base branch
        echo "changed_files=$(git diff --name-only --diff-filter=d origin/${{ github.base_ref }} HEAD | grep '\.py$' | xargs)" >> $GITHUB_OUTPUT

    # --- UPDATED STEPS: Use the file list ---
    - name: List files
      run: echo "The changed files are ${{ steps.files.outputs.changed_files }}"

    - name: Format with ruff (Changed files only)
      if: steps.files.outputs.changed_files != ''
      run: uv run ruff format --check ${{ steps.files.outputs.changed_files }}  

    - name: Lint with ruff (Changed files only)
      if: steps.files.outputs.changed_files != ''
      run: uv run ruff check ${{ steps.files.outputs.changed_files }}

    - name: Type check with mypy (Changed files only)
      if: steps.files.outputs.changed_files != ''
      # Note: Running mypy on specific files may miss cross-file type errors
      run: uv run mypy ${{ steps.files.outputs.changed_files }}
      continue-on-error: true
```

### `.github/workflows/_publish.yml`

- Source path: `.github/workflows/_publish.yml`
- Truncated: `no`

```yaml
name: 16. _Publish Distribution

on:
  workflow_call:
    inputs:
      target:
        description: 'Publish Target'
        required: false
        type: string
        default: 'pypi'  # Callers (like release.yml) typically want PyPI
      build_run_id:
        description: 'Build Workflow Run ID (Optional, defaults to current run)'
        required: false
        type: string
        default: ''
  workflow_dispatch:
    inputs:
      target:
        description: 'Select where to publish'
        required: true
        type: choice
        default: 'testpypi'
        options:
        - testpypi
        - pypi
        - both
      build_run_id:
        description: 'Build Workflow Run ID (Required for manual dispatch, find it in the Build run URL)'
        required: true
        type: string

jobs:
  permission-check:
    name: Check write permission
    runs-on: ubuntu-24.04
    permissions:
      contents: read
    outputs:
      allowed: ${{ steps.check.outputs.allowed }}
    steps:
    - name: Verify actor permission
      id: check
      uses: actions/github-script@v9
      with:
        script: |
          // Only check permission for manual dispatch
          if (context.eventName !== 'workflow_dispatch') {
            core.setOutput('allowed', 'true');
            return;
          }
          const { owner, repo } = context.repo;
          const actor = context.actor;
          const { data } = await github.rest.repos.getCollaboratorPermissionLevel({
            owner,
            repo,
            username: actor,
          });
          const perm = data.permission;
          core.info(`Actor ${actor} permission: ${perm}`);
          const allowed = ['admin', 'maintain', 'write'].includes(perm);
          core.setOutput('allowed', allowed ? 'true' : 'false');
          if (!allowed) {
            core.setFailed(`User ${actor} does not have write permission`);
          }

  publish-testpypi:
    name: Publish to TestPyPI
    needs: [permission-check]
    if: >-
      needs.permission-check.outputs.allowed == 'true' &&
      (inputs.target == 'testpypi' || inputs.target == 'both')
    runs-on: ubuntu-24.04
    environment:
      name: testpypi
      url: https://test.pypi.org/p/openviking
    permissions:
      id-token: write
      actions: read  # Required for downloading artifacts from other runs

    steps:
    - name: Download all the dists (Same Run)
      if: inputs.build_run_id == ''
      uses: actions/download-artifact@v8
      with:
        pattern: python-package-distributions-*
        path: dist/
        merge-multiple: true

    - name: Download all the dists (Cross Run)
      if: inputs.build_run_id != ''
      uses: actions/download-artifact@v8
      with:
        run-id: ${{ inputs.build_run_id }}
        github-token: ${{ secrets.GITHUB_TOKEN }}
        pattern: python-package-distributions-*
        path: dist/
        merge-multiple: true

    - name: Publish distribution to TestPyPI
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        repository-url: https://test.pypi.org/legacy/
        skip-existing: true
        verbose: true

    - name: Display published version
      run: |
        # Get version from the first wheel file found
        VERSION=$(ls dist/*.whl | head -n 1 | xargs basename | cut -d- -f2)
        echo "Published to TestPyPI (or already existed) with version: $VERSION"
        echo "::notice::Published to TestPyPI (or already existed) with version: $VERSION"

  publish-pypi:
    name: Publish to PyPI
    needs: [permission-check]
    if: >-
      needs.permission-check.outputs.allowed == 'true' &&
      (inputs.target == 'pypi' || inputs.target == 'both')
    runs-on: ubuntu-24.04
    environment:
      name: pypi
      url: https://pypi.org/p/openviking
    permissions:
      id-token: write
      actions: read  # Required for downloading artifacts from other runs

    steps:
    - name: Download all the dists (Same Run)
      if: inputs.build_run_id == ''
      uses: actions/download-artifact@v8
      with:
        pattern: python-package-distributions-*
        path: dist/
        merge-multiple: true

    - name: Download all the dists (Cross Run)
      if: inputs.build_run_id != ''
      uses: actions/download-artifact@v8
      with:
        run-id: ${{ inputs.build_run_id }}
        github-token: ${{ secrets.GITHUB_TOKEN }}
        pattern: python-package-distributions-*
        path: dist/
        merge-multiple: true

    - name: Publish distribution to PyPI
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        skip-existing: true
        verbose: true

    - name: Display published version
      run: |
        # Get version from the first wheel file found
        VERSION=$(ls dist/*.whl | head -n 1 | xargs basename | cut -d- -f2)
        echo "Published to PyPI (or already existed) with version: $VERSION"
        echo "::notice::Published to PyPI (or already existed) with version: $VERSION"
```

### `.github/workflows/_test_full.yml`

- Source path: `.github/workflows/_test_full.yml`
- Truncated: `no`

```yaml
name: 13. _Test Suite (Full)

on:
  workflow_call:
    inputs:
      os_json:
        description: 'JSON string of OS to run on'
        required: false
        type: string
        default: '["ubuntu-24.04", "macos-14", "windows-latest"]'
      python_json:
        description: 'JSON string of Python versions'
        required: false
        type: string
        default: '["3.10", "3.11", "3.12", "3.13"]'
  workflow_dispatch:
    inputs:
      os_json:
        description: 'JSON string of OS to run on'
        required: false
        default: '["ubuntu-24.04", "macos-14", "windows-latest"]'
      python_json:
        description: 'JSON string of Python versions'
        required: false
        default: '["3.10", "3.11", "3.12", "3.13"]'

jobs:
  test:
    name: Full Test (${{ matrix.os }}, ${{ matrix.python-version }})
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: ${{ fromJson(inputs.os_json || '["ubuntu-24.04", "macos-14", "windows-latest"]') }}
        python-version: ${{ fromJson(inputs.python_json || '["3.10", "3.11", "3.12", "3.13"]') }}

    steps:
    - uses: actions/checkout@v6
      with:
        submodules: recursive

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v6
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install uv
      uses: astral-sh/setup-uv@v7
      with:
        enable-cache: true

    - name: Install system dependencies (Ubuntu)
      if: runner.os == 'Linux'
      run: |
        sudo apt-get update
        sudo apt-get install -y cmake build-essential

    - name: Install system dependencies (macOS)
      if: runner.os == 'macOS'
      run: brew install cmake

    - name: Install system dependencies (Windows)
      if: runner.os == 'Windows'
      run: |
        choco install cmake --installargs 'ADD_CMAKE_TO_PATH=System'
        choco install mingw

    - name: Add MinGW to PATH (Windows)
      if: runner.os == 'Windows'
      run: echo "C:\mingw64\bin" >> $env:GITHUB_PATH

    - name: Install Python dependencies
      run: uv sync --frozen --extra test

    - name: Install build dependencies
      run: uv pip install setuptools setuptools_scm cmake wheel

    - name: Check ragfs-python workspace build
      run: cargo check -p ragfs-python

    - name: Build C++ extensions
      run: uv run python setup.py build_ext --inplace

    # TODO: Once unit tests are fixed, switch this back to running the full test suite
    # run: uv run pytest tests/ -v --cov=openviking --cov-report=term
    - name: Run Lite Integration Test (Temporary Replacement)
      shell: bash
      run: |
        export PYTHONPATH=$PYTHONPATH:$(pwd)
        uv run python tests/integration/test_quick_start_lite.py
```

### `.github/workflows/_test_lite.yml`

- Source path: `.github/workflows/_test_lite.yml`
- Truncated: `no`

```yaml
name: 12. _Test Suite (Lite)

on:
  workflow_call:
    inputs:
      os_json:
        description: 'JSON string of OS to run on'
        required: false
        type: string
        default: '["ubuntu-24.04"]'
      python_json:
        description: 'JSON string of Python versions'
        required: false
        type: string
        default: '["3.10"]'
  workflow_dispatch:
    inputs:
      os_json:
        description: 'JSON string of OS to run on'
        required: false
        default: '["ubuntu-24.04"]'
      python_json:
        description: 'JSON string of Python versions'
        required: false
        default: '["3.10"]'

jobs:
  test-lite:
    name: Lite Test (${{ matrix.os }}, ${{ matrix.python-version }})
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: ${{ fromJson(inputs.os_json) }}
        python-version: ${{ fromJson(inputs.python_json) }}

    steps:
    - uses: actions/checkout@v6
      with:
        submodules: recursive

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v6
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install uv
      uses: astral-sh/setup-uv@v7
      with:
        enable-cache: true

    - name: Install system dependencies (Ubuntu)
      if: runner.os == 'Linux'
      run: |
        sudo apt-get update
        sudo apt-get install -y cmake build-essential

    - name: Install system dependencies (macOS)
      if: runner.os == 'macOS'
      run: brew install cmake

    - name: Install system dependencies (Windows)
      if: runner.os == 'Windows'
      run: |
        choco install cmake --installargs 'ADD_CMAKE_TO_PATH=System'
        choco install mingw

    - name: Add MinGW to PATH (Windows)
      if: runner.os == 'Windows'
      run: echo "C:\mingw64\bin" >> $env:GITHUB_PATH

    - name: Install Python dependencies
      run: uv sync --frozen --extra test

    - name: Install build dependencies
      run: uv pip install setuptools setuptools_scm cmake wheel

    - name: Check ragfs-python workspace build
      run: cargo check -p ragfs-python

    - name: Build C++ extensions
      run: uv run python setup.py build_ext --inplace

    - name: Run Lite Integration Test (Quick Start)
      shell: bash
      run: |
        export PYTHONPATH=$PYTHONPATH:$(pwd)
        # Using bash shell ensures this works across platforms (including Windows via Git Bash)
        uv run python tests/integration/test_quick_start_lite.py
```

### `.github/workflows/api_test.yml`

- Source path: `.github/workflows/api_test.yml`
- Truncated: `no`

```yaml
name: 06. API Integration Tests

on:
  workflow_dispatch:
  schedule:
    - cron: '0 1,4,7,10,13 * * *'
  pull_request:
    branches:
      - 'main'
    paths-ignore:
      - 'docs/**'
      - '**.md'
      - 'LICENSE'
      - 'CONTRIBUTING.md'
      - '**.png'
      - '**.jpg'
      - '**.jpeg'
      - '**.gif'
      - '**.svg'
      - '.gitignore'
      - '.editorconfig'

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true

jobs:
  api-tests:
    name: API Integration Tests (${{ matrix.os }})
    runs-on: ${{ matrix.os }}
    timeout-minutes: 60
    if: github.event_name == 'workflow_dispatch' || github.event_name == 'pull_request' || github.repository == 'volcengine/OpenViking'
    strategy:
      fail-fast: false
      max-parallel: 1
      matrix:
        os: ${{ ((github.event_name == 'push' && github.ref == 'refs/heads/main') || github.event_name == 'schedule' || github.event_name == 'workflow_dispatch') && fromJSON('["ubuntu-24.04", "macos-14", "windows-latest"]') || fromJSON('["ubuntu-24.04"]') }}
    
    steps:
      - uses: actions/checkout@v6
        with:
          submodules: recursive
          fetch-depth: 100

      - name: Set up Python 3.10
        uses: actions/setup-python@v6
        with:
          python-version: '3.10'

      - name: Cache Python dependencies (Unix)
        if: runner.os != 'Windows'
        uses: actions/cache@v5
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt', '**/pyproject.toml') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Cache Python dependencies (Windows)
        if: runner.os == 'Windows'
        uses: actions/cache@v5
        with:
          path: ~\AppData\Local\pip\Cache
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt', '**/pyproject.toml') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Install system dependencies (Ubuntu)
        if: runner.os == 'Linux'
        run: |
          sudo apt-get update -y && sudo apt-get install -y cmake build-essential ffmpeg --no-install-recommends

      - name: Install system dependencies (macOS)
        if: runner.os == 'macOS'
        run: |
          brew install cmake ffmpeg

      - name: Install system dependencies (Windows)
        if: runner.os == 'Windows'
        run: |
          echo "cmake is pre-installed on Windows runner and will also be installed via pip"

      - name: Install uv
        uses: astral-sh/setup-uv@v7
        with:
          enable-cache: true

      - name: Install build dependencies (system pip)
        run: |
          python -m pip install --upgrade pip
          pip install "setuptools>=70.1" setuptools_scm cmake wheel
          echo "---"
          python -c "import setuptools; print(f'setuptools version: {setuptools.__version__}')"

      - name: Install dependencies using uv sync
        run: |
          echo "Installing dependencies using uv sync..."
          uv sync --frozen

      - name: Install build dependencies (uv pip)
        run: |
          echo "Installing build dependencies to uv environment..."
          uv pip install setuptools setuptools_scm cmake wheel maturin

      - name: Set up Rust toolchain
        uses: dtolnay/rust-toolchain@v1
        with:
          toolchain: stable

      - name: Build C++ extensions
        shell: bash
        run: |
          export OV_SKIP_OV_BUILD=1
          mkdir -p openviking/bin
          touch openviking/bin/ov
          chmod +x openviking/bin/ov
          echo "OV_SKIP_OV_BUILD=1 set, skipping ov CLI Rust build (ragfs build still needed for server)"
          
          if [ -z "$SETUPTOOLS_SCM_PRETEND_VERSION_FOR_OPENVIKING" ]; then
            PRETEND_VERSION=$(git describe --tags --always 2>/dev/null | sed -E 's/^v?([0-9]+\.[0-9]+\.[0-9]+).*/\1.dev0/' || echo "0.0.0.dev0")
            echo "SETUPTOOLS_SCM_PRETEND_VERSION_FOR_OPENVIKING=$PRETEND_VERSION" >> $GITHUB_ENV
            echo "Using pretend version: $PRETEND_VERSION"
          fi
          
          uv run python setup.py build_ext --inplace

      - name: Build ragfs-python native extension
        shell: bash
        run: |
          RAGFS_LIB_DIR="openviking/lib"
          RAGFS_SO_COUNT=$(ls -1 "$RAGFS_LIB_DIR"/ragfs_python*.so "$RAGFS_LIB_DIR"/ragfs_python*.pyd "$RAGFS_LIB_DIR"/ragfs_python*.dylib 2>/dev/null | wc -l | tr -d '[:space:]' || echo "0")
          
          if [ "$RAGFS_SO_COUNT" -gt 0 ]; then
            echo "✅ ragfs_python native extension already exists:"
            ls -la "$RAGFS_LIB_DIR"/ragfs_python*
            exit 0
          fi
          
          echo "ragfs_python native lib not found after build_ext, building via maturin..."
          TMPDIR_RAGFS=$(mktemp -d)
          cd crates/ragfs-python
          uv run --no-project maturin build --release --features s3 --out "$TMPDIR_RAGFS"
          cd ../..
          
          WHL_FILE=$(ls -1 "$TMPDIR_RAGFS"/ragfs_python-*.whl 2>/dev/null | head -1)
          if [ -z "$WHL_FILE" ]; then
            echo "❌ ERROR: maturin build produced no wheel"
            ls -la "$TMPDIR_RAGFS"/
            exit 1
          fi
          
          echo "Extracting ragfs_python from wheel: $WHL_FILE"
          mkdir -p "$RAGFS_LIB_DIR"
          WHL_FILE_PY=$(echo "$WHL_FILE" | sed 's/\\/\\\\/g')
          RAGFS_LIB_DIR_PY=$(echo "$RAGFS_LIB_DIR" | sed 's/\\/\\\\/g')
          uv run python -c "
          import zipfile, os, sys, stat
          with zipfile.ZipFile('${WHL_FILE_PY}') as zf:
              for name in zf.namelist():
                  bn = os.path.basename(name)
                  if bn.startswith('ragfs_python') and (bn.endswith('.so') or bn.endswith('.pyd') or bn.endswith('.dylib')):
                      dst = os.path.join('${RAGFS_LIB_DIR_PY}', bn)
                      with zf.open(name) as src, open(dst, 'wb') as f:
                          f.write(src.read())
                      os.chmod(dst, 0o755)
                      print(f'  [OK] ragfs-python: extracted {bn} -> {dst}')
                      sys.exit(0)
          print('[ERROR] No ragfs_python native library found in wheel')
          sys.exit(1)
          "
          rm -rf "$TMPDIR_RAGFS"
          
          echo "Verifying ragfs_python native extension:"
          ls -la "$RAGFS_LIB_DIR"/ragfs_python*

      - name: Install API test dependencies
        run: |
          cd tests/api_test
          uv pip install -r requirements.txt

      - name: Create OpenViking config file (Unix)
        if: runner.os != 'Windows'
        id: create-config-unix
        env:
          VLM_API_KEY: ${{ secrets.VLM_API_KEY }}
          EMBEDDING_API_KEY: ${{ secrets.EMBEDDING_API_KEY }}
        run: |
          mkdir -p $HOME/.openviking
          
          HAS_SECRETS=false
          if [ -n "$VLM_API_KEY" ] && [ -n "$EMBEDDING_API_KEY" ]; then
            HAS_SECRETS=true
            echo "Using full configuration with VLM and Embedding"
          else
            echo "Using minimal configuration (no VLM/Embedding)"
          fi
          
          echo "HAS_SECRETS=$HAS_SECRETS" >> $GITHUB_ENV
          
          if [ "$HAS_SECRETS" = "true" ]; then
            cat > $HOME/.openviking/ov.conf << EOF
          {
            "server": {
              "root_api_key": "test-root-api-key"
            },
            "vlm": {
              "provider": "volcengine",
              "api_key": "$VLM_API_KEY",
              "model": "doubao-seed-2-0-mini-260215",
              "api_base": "https://ark.cn-beijing.volces.com/api/v3",
              "temperature": 0.1,
              "max_retries": 3
            },
            "embedding": {
              "dense": {
                "provider": "volcengine",
                "api_key": "$EMBEDDING_API_KEY",
                "model": "doubao-embedding-vision-251215",
                "api_base": "https://ark.cn-beijing.volces.com/api/v3",
                "dimension": 1024,
                "input": "multimodal"
              }
            }
          }
          EOF
          else
            cat > $HOME/.openviking/ov.conf << EOF
          {
            "server": {
              "root_api_key": "test-root-api-key"
            },
            "vlm": {
              "provider": "volcengine",
              "api_key": "dummy-vlm-api-key",
              "model": "doubao-seed-2-0-mini-260215",
              "api_base": "https://ark.cn-beijing.volces.com/api/v3",
              "temperature": 0.1,
              "max_retries": 3
            },
            "embedding": {
              "dense": {
                "provider": "volcengine",
                "api_key": "dummy-embedding-api-key",
                "model": "doubao-embedding-vision-251215",
                "api_base": "https://ark.cn-beijing.volces.com/api/v3",
                "dimension": 1024,
                "input": "multimodal"
              }
            }
          }
          EOF
          fi
          
          echo "Config file created at $HOME/.openviking/ov.conf"

      - name: Create OpenViking config file (Windows)
        if: runner.os == 'Windows'
        id: create-config-windows
        env:
          VLM_API_KEY: ${{ secrets.VLM_API_KEY }}
          EMBEDDING_API_KEY: ${{ secrets.EMBEDDING_API_KEY }}
        shell: pwsh
        run: |
          $configDir = "$env:USERPROFILE\.openviking"
          New-Item -ItemType Directory -Force -Path $configDir | Out-Null
          
          $hasSecrets = "false"
          if ($env:VLM_API_KEY -and $env:EMBEDDING_API_KEY) {
            $hasSecrets = "true"
            Write-Host "Using full configuration with VLM and Embedding"
          } else {
            Write-Host "Using minimal configuration (no VLM/Embedding)"
          }
          
          echo "HAS_SECRETS=$hasSecrets" >> $env:GITHUB_ENV
          
          if ($hasSecrets -eq "true") {
            $config = @"
          {
            "server": {
              "root_api_key": "test-root-api-key"
            },
            "vlm": {
              "provider": "volcengine",
              "api_key": "$env:VLM_API_KEY",
              "model": "doubao-seed-2-0-mini-260215",
              "api_base": "https://ark.cn-beijing.volces.com/api/v3",
              "temperature": 0.1,
              "max_retries": 3
            },
            "embedding": {
              "dense": {
                "provider": "volcengine",
                "api_key": "$env:EMBEDDING_API_KEY",
                "model": "doubao-embedding-vision-251215",
                "api_base": "https://ark.cn-beijing.volces.com/api/v3",
                "dimension": 1024,
                "input": "multimodal"
              }
            }
          }
          "@
          } else {
            $config = @"
          {
            "server": {
              "root_api_key": "test-root-api-key"
            },
            "vlm": {
              "provider": "volcengine",
              "api_key": "dummy-vlm-api-key",
              "model": "doubao-seed-2-0-mini-260215",
              "api_base": "https://ark.cn-beijing.volces.com/api/v3",
              "temperature": 0.1,
              "max_retries": 3
            },
            "embedding": {
              "dense": {
                "provider": "volcengine",
                "api_key": "dummy-embedding-api-key",
                "model": "doubao-embedding-vision-251215",
                "api_base": "https://ark.cn-beijing.volces.com/api/v3",
                "dimension": 1024,
                "input": "multimodal"
              }
            }
          }
          "@
          }
          
          $config | Out-File -FilePath "$configDir\ov.conf" -Encoding utf8
          Write-Host "Config file created at $configDir\ov.conf"

      - name: Find available port and start OpenViking Server (Unix)
        if: runner.os != 'Windows'
        id: start-server-unix
        run: |
          find_available_port() {
            local port=1933
            while true; do
              if ! lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
                echo $port
                return
              fi
              port=$((port + 1))
            done
          }
          
          SERVER_PORT=$(find_available_port)
          echo "Using port: $SERVER_PORT"
          echo "SERVER_PORT=$SERVER_PORT" >> $GITHUB_ENV
          
          echo "Starting OpenViking Server on port $SERVER_PORT..."
          export ROOT_API_KEY=test-root-api-key
          export SERVER_PORT=$SERVER_PORT
          nohup uv run python -m openviking.server.bootstrap > openviking-server.log 2>&1 &
          echo $! > openviking-server.pid
          echo "SERVER_PID=$(cat openviking-server.pid)" >> $GITHUB_ENV
          
          echo "Waiting for server to start..."
          for i in {1..30}; do
            if curl -s http://127.0.0.1:$SERVER_PORT/health | grep -q '"healthy":true'; then
              echo "Server is ready!"
              break
            fi
            echo "Waiting... ($i/30)"
            sleep 2
          done
          
          if ! curl -s http://127.0.0.1:$SERVER_PORT/health | grep -q '"healthy":true'; then
            echo "Server failed to start!"
            echo "Server logs:"
            cat openviking-server.log
            exit 1
          fi

      - name: Find available port and start OpenViking Server (Windows)
        if: runner.os == 'Windows'
        id: start-server-windows
        shell: pwsh
        run: |
          $port = 1933
          Write-Host "Using port: $port"
          echo "SERVER_PORT=$port" >> $env:GITHUB_ENV
          
          Write-Host "Starting OpenViking Server on port $port..."
          
          $logFile = Join-Path $PWD "openviking-server.log"
          $errFile = Join-Path $PWD "openviking-server-error.log"
          $batchFile = Join-Path $PWD "start-server.bat"
          
          $batchContent = "@echo off`r`nset ROOT_API_KEY=test-root-api-key`r`nset SERVER_PORT=$port`r`nuv run python -m openviking.server.bootstrap`r`n"
          Set-Content -Path $batchFile -Value $batchContent -Encoding ASCII
          
          Write-Host "Batch file created at: $batchFile"
          Write-Host "Batch file content:"
          Get-Content $batchFile
          
          $psi = New-Object System.Diagnostics.ProcessStartInfo
          $psi.FileName = "cmd.exe"
          $psi.Arguments = "/C `"$batchFile`""
          $psi.UseShellExecute = $true
          $psi.WindowStyle = [System.Diagnostics.ProcessWindowStyle]::Hidden
          $psi.WorkingDirectory = $PWD.Path
          
          $process = [System.Diagnostics.Process]::Start($psi)
          
          Write-Host "Server process started with PID: $($process.Id)"
          echo "SERVER_PID=$($process.Id)" >> $env:GITHUB_ENV
          
          Write-Host "Waiting for server to start..."
          $ready = $false
          for ($i = 1; $i -le 30; $i++) {
            Start-Sleep -Seconds 2
            try {
              $response = Invoke-WebRequest -Uri "http://127.0.0.1:$port/health" -UseBasicParsing -TimeoutSec 5
              if ($response.Content -match '"healthy":true') {
                Write-Host "Server is ready!"
                $ready = $true
                break
              }
            } catch {
              Write-Host "Waiting... ($i/30)"
            }
          }
          
          if (-not $ready) {
            Write-Host "Server failed to start!"
            Write-Host "Checking if process is still running..."
            $proc = Get-Process -Id $process.Id -ErrorAction SilentlyContinue
            if ($proc) {
              Write-Host "Process is still running with PID: $($proc.Id)"
            } else {
              Write-Host "Process has exited"
            }
            exit 1
          }

      - name: Run API Tests (Unix)
        if: runner.os != 'Windows'
        id: run-tests-unix
        run: |
          cd tests/api_test
          export OPENVIKING_API_KEY=test-root-api-key
          export SERVER_URL=http://127.0.0.1:${{ env.SERVER_PORT }}
          
          if [ "${{ env.HAS_SECRETS }}" = "true" ]; then
            echo "Running full test suite with VLM/Embedding"
            uv run python -m pytest . -v --html=api-test-report.html --self-contained-html \
              --ignore=scenarios/resources_retrieval_slow/
          else
            echo "Running basic tests only (no VLM/Embedding)"
            uv run python -m pytest . -v --html=api-test-report.html --self-contained-html \
              --ignore=retrieval/ --ignore=resources/test_pack.py --ignore=resources/test_wait_processed.py \
              --ignore=admin/ --ignore=skills/ --ignore=system/test_system_status.py --ignore=system/test_is_healthy.py --ignore=system/test_system_wait.py \
              --ignore=scenarios/ -k "not test_observer"
          fi
        continue-on-error: true

      - name: Run API Tests (Windows)
        if: runner.os == 'Windows'
        id: run-tests-windows
        shell: pwsh
        run: |
          cd tests/api_test
          $env:OPENVIKING_API_KEY = "test-root-api-key"
          $env:SERVER_URL = "http://127.0.0.1:${{ env.SERVER_PORT }}"
          
          if ($env:HAS_SECRETS -eq "true") {
            Write-Host "Running full test suite with VLM/Embedding (Windows: skipping filesystem tests)"
            uv run python -m pytest . -v --html=api-test-report.html --self-contained-html --ignore=filesystem/ --ignore=scenarios/resources_retrieval_slow/
          } else {
            Write-Host "Running basic tests only (no VLM/Embedding, Windows: skipping filesystem tests)"
            uv run python -m pytest . -v --html=api-test-report.html --self-contained-html --ignore=retrieval/ --ignore=resources/test_pack.py --ignore=resources/test_wait_processed.py --ignore=admin/ --ignore=skills/ --ignore=system/test_system_status.py --ignore=system/test_is_healthy.py --ignore=system/test_system_wait.py --ignore=filesystem/ --ignore=scenarios/ -k "not test_observer"
          }
        continue-on-error: true

      - name: Upload test reports
        uses: actions/upload-artifact@v7
        if: always()
        with:
          name: api-test-reports-${{ matrix.os }}-${{ github.run_id }}
          path: |
            tests/api_test/api-test-report.html
            openviking-server.log

      - name: Stop OpenViking Server (Unix)
        if: runner.os != 'Windows' && always()
        run: |
          if [ -f openviking-server.pid ]; then
            kill $(cat openviking-server.pid) 2>/dev/null || true
            pkill -f "openviking.server.bootstrap" 2>/dev/null || true
          fi

      - name: Stop OpenViking Server (Windows)
        if: runner.os == 'Windows' && always()
        shell: pwsh
        run: |
          if ($env:SERVER_PID) {
            Stop-Process -Id $env:SERVER_PID -Force -ErrorAction SilentlyContinue
          }
          Get-Process -Name python -ErrorAction SilentlyContinue | Stop-Process -Force

      - name: Check test results (Unix)
        if: runner.os != 'Windows' && steps.run-tests-unix.outcome != 'success'
        run: |
          echo "API tests failed!"
          exit 1

      - name: Check test results (Windows)
        if: runner.os == 'Windows' && steps.run-tests-windows.outcome != 'success'
        shell: pwsh
        run: |
          Write-Host "API tests failed!"
          exit 1
```

### `.github/workflows/api_test_effect.yml`

- Source path: `.github/workflows/api_test_effect.yml`
- Truncated: `no`

```yaml
name: 07. API Effect Tests

on:
  workflow_dispatch:
  schedule:
    - cron: '0 2 * * *'

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  effect-tests:
    name: API Effect Tests (${{ matrix.os }})
    runs-on: ${{ matrix.os }}
    timeout-minutes: 120
    if: github.event_name == 'workflow_dispatch' || github.repository == 'volcengine/OpenViking'
    strategy:
      fail-fast: false
      max-parallel: 1
      matrix:
        os: [ubuntu-24.04]

    steps:
      - uses: actions/checkout@v6
        with:
          submodules: recursive
          fetch-depth: 100

      - name: Set up Python 3.10
        uses: actions/setup-python@v6
        with:
          python-version: '3.10'

      - name: Cache Python dependencies
        uses: actions/cache@v5
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-effect-${{ hashFiles('**/requirements.txt', '**/pyproject.toml') }}
          restore-keys: |
            ${{ runner.os }}-pip-effect-

      - name: Install system dependencies
        run: |
          sudo apt-get update -y && sudo apt-get install -y cmake build-essential ffmpeg --no-install-recommends

      - name: Install uv
        uses: astral-sh/setup-uv@v7
        with:
          enable-cache: true

      - name: Install build dependencies (system pip)
        run: |
          python -m pip install --upgrade pip
          pip install "setuptools>=70.1" setuptools_scm cmake wheel

      - name: Install dependencies using uv sync
        run: uv sync --frozen

      - name: Install build dependencies (uv pip)
        run: uv pip install setuptools setuptools_scm cmake wheel maturin

      - name: Set up Rust toolchain
        uses: dtolnay/rust-toolchain@v1
        with:
          toolchain: stable

      - name: Build C++ extensions
        shell: bash
        run: |
          export OV_SKIP_OV_BUILD=1
          mkdir -p openviking/bin
          touch openviking/bin/ov
          chmod +x openviking/bin/ov
          if [ -z "$SETUPTOOLS_SCM_PRETEND_VERSION_FOR_OPENVIKING" ]; then
            PRETEND_VERSION=$(git describe --tags --always 2>/dev/null | sed -E 's/^v?([0-9]+\.[0-9]+\.[0-9]+).*/\1.dev0/' || echo "0.0.0.dev0")
            echo "SETUPTOOLS_SCM_PRETEND_VERSION_FOR_OPENVIKING=$PRETEND_VERSION" >> $GITHUB_ENV
          fi
          uv run python setup.py build_ext --inplace

      - name: Build ragfs-python native extension
        shell: bash
        run: |
          RAGFS_LIB_DIR="openviking/lib"
          RAGFS_SO_COUNT=$(ls -1 "$RAGFS_LIB_DIR"/ragfs_python*.so "$RAGFS_LIB_DIR"/ragfs_python*.pyd "$RAGFS_LIB_DIR"/ragfs_python*.dylib 2>/dev/null | wc -l | tr -d '[:space:]' || echo "0")
          if [ "$RAGFS_SO_COUNT" -gt 0 ]; then exit 0; fi
          TMPDIR_RAGFS=$(mktemp -d)
          cd crates/ragfs-python
          uv run --no-project maturin build --release --features s3 --out "$TMPDIR_RAGFS"
          cd ../..
          WHL_FILE=$(ls -1 "$TMPDIR_RAGFS"/ragfs_python-*.whl 2>/dev/null | head -1)
          if [ -z "$WHL_FILE" ]; then exit 1; fi
          mkdir -p "$RAGFS_LIB_DIR"
          WHL_FILE_PY=$(echo "$WHL_FILE" | sed 's/\\/\\\\/g')
          RAGFS_LIB_DIR_PY=$(echo "$RAGFS_LIB_DIR" | sed 's/\\/\\\\/g')
          uv run python -c "
          import zipfile, os, sys
          with zipfile.ZipFile('${WHL_FILE_PY}') as zf:
              for name in zf.namelist():
                  bn = os.path.basename(name)
                  if bn.startswith('ragfs_python') and (bn.endswith('.so') or bn.endswith('.pyd') or bn.endswith('.dylib')):
                      dst = os.path.join('${RAGFS_LIB_DIR_PY}', bn)
                      with zf.open(name) as src, open(dst, 'wb') as f:
                          f.write(src.read())
                      os.chmod(dst, 0o755)
                      sys.exit(0)
          sys.exit(1)
          "
          rm -rf "$TMPDIR_RAGFS"

      - name: Install API test dependencies
        run: |
          cd tests/api_test
          uv pip install -r requirements.txt

      - name: Create OpenViking config file
        env:
          VLM_API_KEY: ${{ secrets.VLM_API_KEY }}
          EMBEDDING_API_KEY: ${{ secrets.EMBEDDING_API_KEY }}
        run: |
          mkdir -p $HOME/.openviking
          if [ -n "$VLM_API_KEY" ] && [ -n "$EMBEDDING_API_KEY" ]; then
            echo "HAS_SECRETS=true" >> $GITHUB_ENV
            cat > $HOME/.openviking/ov.conf << EOF
          {
            "server": { "root_api_key": "test-root-api-key" },
            "vlm": {
              "provider": "volcengine",
              "api_key": "$VLM_API_KEY",
              "model": "doubao-seed-2-0-mini-260215",
              "api_base": "https://ark.cn-beijing.volces.com/api/v3",
              "temperature": 0.1, "max_retries": 3
            },
            "embedding": {
              "dense": {
                "provider": "volcengine",
                "api_key": "$EMBEDDING_API_KEY",
                "model": "doubao-embedding-vision-251215",
                "api_base": "https://ark.cn-beijing.volces.com/api/v3",
                "dimension": 1024, "input": "multimodal"
              }
            }
          }
          EOF
          else
            echo "HAS_SECRETS=false" >> $GITHUB_ENV
            cat > $HOME/.openviking/ov.conf << EOF
          {
            "server": { "root_api_key": "test-root-api-key" },
            "vlm": {
              "provider": "volcengine",
              "api_key": "dummy-vlm-api-key",
              "model": "doubao-seed-2-0-mini-260215",
              "api_base": "https://ark.cn-beijing.volces.com/api/v3",
              "temperature": 0.1, "max_retries": 3
            },
            "embedding": {
              "dense": {
                "provider": "volcengine",
                "api_key": "dummy-embedding-api-key",
                "model": "doubao-embedding-vision-251215",
                "api_base": "https://ark.cn-beijing.volces.com/api/v3",
                "dimension": 1024, "input": "multimodal"
              }
            }
          }
          EOF
          fi

      - name: Start OpenViking Server
        run: |
          SERVER_PORT=1933
          echo "SERVER_PORT=$SERVER_PORT" >> $GITHUB_ENV
          export ROOT_API_KEY=test-root-api-key
          export SERVER_PORT=$SERVER_PORT
          nohup uv run python -m openviking.server.bootstrap > openviking-server.log 2>&1 &
          echo $! > openviking-server.pid
          echo "Waiting for server to start..."
          for i in {1..30}; do
            if curl -s http://127.0.0.1:$SERVER_PORT/health | grep -q '"healthy":true'; then
              echo "Server is ready!"
              break
            fi
            echo "Waiting... ($i/30)"
            sleep 2
          done
          if ! curl -s http://127.0.0.1:$SERVER_PORT/health | grep -q '"healthy":true'; then
            echo "Server failed to start!"
            cat openviking-server.log
            exit 1
          fi

      - name: Run Effect Tests
        id: run-effect-tests
        run: |
          cd tests/api_test
          export OPENVIKING_API_KEY=test-root-api-key
          export SERVER_URL=http://127.0.0.1:${{ env.SERVER_PORT }}
          uv run python -m pytest scenarios/resources_retrieval_slow/ -v --tb=short --durations=0 --html=api-effect-test-report.html --self-contained-html
        continue-on-error: true

      - name: Upload test reports
        uses: actions/upload-artifact@v7
        if: always()
        with:
          name: api-effect-test-reports-${{ github.run_id }}
          path: |
            tests/api_test/api-effect-test-report.html
            openviking-server.log

      - name: Stop OpenViking Server
        if: always()
        run: |
          if [ -f openviking-server.pid ]; then
            kill $(cat openviking-server.pid) 2>/dev/null || true
            pkill -f "openviking.server.bootstrap" 2>/dev/null || true
          fi

      - name: Check test results
        if: steps.run-effect-tests.outcome != 'success'
        run: |
          echo "Effect tests failed!"
          exit 1
```

### `.github/workflows/build-docker-image.yml`

- Source path: `.github/workflows/build-docker-image.yml`
- Truncated: `no`

```yaml
name: Build and Push Docker Image

on:
  workflow_dispatch:
    inputs:
      version:
        description: "application version for OpenViking"
        required: true
        type: string
  push:
    branches: [ main ]
    tags: [ "v*.*.*" ]

env:
  REGISTRY: ghcr.io

jobs:
  build-and-push-image:
    strategy:
      fail-fast: false
      matrix:
        include:
          - arch: amd64
            platform: linux/amd64
            runner: ubuntu-24.04
          - arch: arm64
            platform: linux/arm64
            runner: ubuntu-24.04-arm
    runs-on: ${{ matrix.runner }}
    permissions:
      contents: read
      packages: write
      attestations: write
      id-token: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v6
        with:
          fetch-depth: 0
          submodules: recursive

      - name: Normalize image name
        id: image-name
        env:
          RAW_IMAGE_NAME: ${{ github.repository }}
        run: |
          echo "image=$(echo "$RAW_IMAGE_NAME" | tr '[:upper:]' '[:lower:]')" >> "$GITHUB_OUTPUT"

      - name: Resolve OpenViking version
        id: openviking-version
        shell: bash
        run: |
          set -euo pipefail
          if [ "${{ github.event_name }}" = "workflow_dispatch" ]; then
            version="${{ github.event.inputs.version }}"
          elif [ "${{ github.ref_type }}" = "tag" ]; then
            version="${{ github.ref_name }}"
          else
            python -m pip install "setuptools-scm>=8.0"
            version="$(
              python -c "from build_support.versioning import resolve_openviking_version; print(resolve_openviking_version())"
            )"
          fi
          if [ -z "${version}" ] || [ "${version}" = "0.0.0" ]; then
            echo "Resolved invalid OpenViking version: ${version}" >&2
            exit 2
          fi
          echo "version=${version}" >> "$GITHUB_OUTPUT"

      - name: Log in to the Container registry
        uses: docker/login-action@v4
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Log in to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Extract metadata (tags, labels) for Docker
        id: meta
        uses: docker/metadata-action@v6
        with:
          images: |
            ${{ env.REGISTRY }}/${{ steps.image-name.outputs.image }}
            docker.io/${{ secrets.DOCKERHUB_USERNAME }}/openviking
          tags: |
            type=raw,value=${{ github.event.inputs.version }},enable=${{ github.event_name == 'workflow_dispatch' }}
            type=ref,event=tag,enable=${{ github.ref_type == 'tag' }}
            type=raw,value=latest,enable=${{ github.ref_type == 'tag' }}
            type=raw,value=main,enable=${{ github.ref == 'refs/heads/main' }}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4

      - name: Build and push Docker image to GHCR
        id: push-ghcr
        uses: docker/build-push-action@v7
        with:
          context: .
          platforms: ${{ matrix.platform }}
          outputs: |
            type=image,name=${{ env.REGISTRY }}/${{ steps.image-name.outputs.image }},push-by-digest=true,name-canonical=true,push=true
          labels: ${{ steps.meta.outputs.labels }}
          build-args: |
            OPENVIKING_VERSION=${{ steps.openviking-version.outputs.version }}

      - name: Build and push Docker image to Docker Hub
        id: push-dockerhub
        uses: docker/build-push-action@v7
        with:
          context: .
          platforms: ${{ matrix.platform }}
          outputs: |
            type=image,name=docker.io/${{ secrets.DOCKERHUB_USERNAME }}/openviking,push-by-digest=true,name-canonical=true,push=true
          labels: ${{ steps.meta.outputs.labels }}
          build-args: |
            OPENVIKING_VERSION=${{ steps.openviking-version.outputs.version }}

      - name: Export GHCR image digest
        run: |
          mkdir -p /tmp/digests-ghcr
          ghcr_digest="${{ steps.push-ghcr.outputs.digest }}"
          touch "/tmp/digests-ghcr/${ghcr_digest#sha256:}"

      - name: Upload GHCR image digest
        uses: actions/upload-artifact@v7
        with:
          name: docker-digests-ghcr-${{ matrix.arch }}
          path: /tmp/digests-ghcr/*
          if-no-files-found: error
          retention-days: 1

      - name: Export Docker Hub image digest
        run: |
          mkdir -p /tmp/digests-dockerhub
          dockerhub_digest="${{ steps.push-dockerhub.outputs.digest }}"
          touch "/tmp/digests-dockerhub/${dockerhub_digest#sha256:}"

      - name: Upload Docker Hub image digest
        uses: actions/upload-artifact@v7
        with:
          name: docker-digests-dockerhub-${{ matrix.arch }}
          path: /tmp/digests-dockerhub/*
          if-no-files-found: error
          retention-days: 1

  create-manifest:
    runs-on: ubuntu-24.04
    needs: build-and-push-image
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v6
        with:
          submodules: recursive

      - name: Normalize image name
        id: image-name
        env:
          RAW_IMAGE_NAME: ${{ github.repository }}
        run: |
          echo "image=$(echo "$RAW_IMAGE_NAME" | tr '[:upper:]' '[:lower:]')" >> "$GITHUB_OUTPUT"

      - name: Log in to the Container registry
        uses: docker/login-action@v4
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Log in to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Extract metadata (tags, labels) for Docker
        id: meta
        uses: docker/metadata-action@v6
        with:
          images: |
            ${{ env.REGISTRY }}/${{ steps.image-name.outputs.image }}
            docker.io/${{ secrets.DOCKERHUB_USERNAME }}/openviking
          tags: |
            type=raw,value=${{ github.event.inputs.version }},enable=${{ github.event_name == 'workflow_dispatch' }}
            type=ref,event=tag,enable=${{ github.ref_type == 'tag' }}
            type=raw,value=latest,enable=${{ github.ref_type == 'tag' }}
            type=raw,value=main,enable=${{ github.ref == 'refs/heads/main' }}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4

      - name: Download GHCR image digests
        uses: actions/download-artifact@v8
        with:
          pattern: docker-digests-ghcr-*
          path: /tmp/digests-ghcr
          merge-multiple: true

      - name: Download Docker Hub image digests
        uses: actions/download-artifact@v8
        with:
          pattern: docker-digests-dockerhub-*
          path: /tmp/digests-dockerhub
          merge-multiple: true

      - name: Create multi-arch manifests
        env:
          SOURCE_TAGS: ${{ steps.meta.outputs.tags }}
        run: |
          # Collect image references for both registries
          ghcr_image_refs=()
          dockerhub_image_refs=()
          for digest_file in /tmp/digests-ghcr/*; do
            [ -e "$digest_file" ] || continue
            digest="sha256:$(basename "$digest_file")"
            ghcr_image_refs+=("${{ env.REGISTRY }}/${{ steps.image-name.outputs.image }}@${digest}")
          done
          for digest_file in /tmp/digests-dockerhub/*; do
            [ -e "$digest_file" ] || continue
            digest="sha256:$(basename "$digest_file")"
            dockerhub_image_refs+=("docker.io/${{ secrets.DOCKERHUB_USERNAME }}/openviking@${digest}")
          done

          [ ${#ghcr_image_refs[@]} -gt 0 ] || {
            echo "No GHCR image digests found" >&2
            exit 1
          }
          [ ${#dockerhub_image_refs[@]} -gt 0 ] || {
            echo "No Docker Hub image digests found" >&2
            exit 1
          }

          # Create manifests for all tags
          while IFS= read -r tag; do
            [ -n "$tag" ] || continue

            # Determine which registry this tag belongs to
            if [[ "$tag" == ghcr.io/* ]]; then
              docker buildx imagetools create \
                --tag "$tag" \
                "${ghcr_image_refs[@]}"
            elif [[ "$tag" == docker.io/* ]]; then
              docker buildx imagetools create \
                --tag "$tag" \
                "${dockerhub_image_refs[@]}"
            fi
          done <<< "$SOURCE_TAGS"
```

### `.github/workflows/ci.yml`

- Source path: `.github/workflows/ci.yml`
- Truncated: `no`

```yaml
name: 02. Main Branch Checks

on:
  workflow_dispatch:
  push:
    branches: [ main ]
    paths-ignore:
      - 'docs/**'
      - '**.md'
      - 'LICENSE'
      - 'CONTRIBUTING.md'
      - '**.png'
      - '**.jpg'
      - '**.jpeg'
      - '**.gif'
      - '**.svg'
      - '.gitignore'
      - '.editorconfig'

permissions:
  actions: read
  contents: read
  security-events: write

jobs:
  security-scan:
    uses: ./.github/workflows/_codeql.yml
```

### `Cargo.toml`

- Source path: `Cargo.toml`
- Truncated: `no`

```toml
[workspace]
members = ["crates/ov_cli", "crates/ragfs", "crates/ragfs-python"]
resolver = "2"

[profile.release]
opt-level = 3
lto = true
strip = true
```

### `Dockerfile`

- Source path: `Dockerfile`
- Truncated: `no`

```
# syntax=docker/dockerfile:1.9

# Stage 1: provide Rust toolchain (required by setup.py -> build_ov_cli_artifact -> cargo build)
# ragfs-python's default S3-enabled dependency set currently requires rustc >= 1.91.1.
FROM rust:1.91.1-trixie AS rust-toolchain

# Stage 2: build Python environment with uv (builds Rust CLI + C++ extension from source)
FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim AS py-builder

# Reuse Rust toolchain from stage 1 so setup.py can compile ov CLI in-place.
COPY --from=rust-toolchain /usr/local/cargo /usr/local/cargo
COPY --from=rust-toolchain /usr/local/rustup /usr/local/rustup
ENV CARGO_HOME=/usr/local/cargo
ENV RUSTUP_HOME=/usr/local/rustup
ENV PATH="/app/.venv/bin:/usr/local/cargo/bin:${PATH}"
ARG OPENVIKING_VERSION=
ARG TARGETPLATFORM
ARG UV_LOCK_STRATEGY=auto

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
 && rm -rf /var/lib/apt/lists/*

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_NO_DEV=1
WORKDIR /app

# Copy source required for setup.py artifact builds and native extension build.
COPY Cargo.toml Cargo.lock ./
COPY pyproject.toml uv.lock setup.py README.md ./
COPY build_support/ build_support/
COPY bot/ bot/
COPY crates/ crates/
COPY openviking/ openviking/
COPY openviking_cli/ openviking_cli/
COPY src/ src/
COPY third_party/ third_party/

# Install project and dependencies (triggers setup.py artifact builds + build_extension).
# Default to auto-refreshing uv.lock inside the ephemeral build context when it is
# stale, so Docker builds stay unblocked after dependency changes. Set
# UV_LOCK_STRATEGY=locked to keep fail-fast reproducibility checks.
RUN --mount=type=cache,target=/root/.cache/uv,id=uv-${TARGETPLATFORM} \
    if [ -n "${OPENVIKING_VERSION:-}" ]; then \
        export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_OPENVIKING="${OPENVIKING_VERSION}"; \
    elif [ -f openviking/_version.py ]; then \
        export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_OPENVIKING="$(python -c "import runpy; print(runpy.run_path('openviking/_version.py')['version'])")"; \
    else \
        echo "OPENVIKING_VERSION build arg is required when building without openviking/_version.py" >&2; \
        exit 2; \
    fi; \
    case "${UV_LOCK_STRATEGY}" in \
        locked) \
            uv sync --locked --no-editable --extra bot --extra gemini \
            ;; \
        auto) \
            if ! uv lock --check; then \
                uv lock; \
            fi; \
            uv sync --locked --no-editable --extra bot --extra gemini \
            ;; \
        *) \
            echo "Unsupported UV_LOCK_STRATEGY: ${UV_LOCK_STRATEGY}" >&2; \
            exit 2 \
            ;; \
    esac

# Build ragfs-python (Rust RAGFS binding) and extract the native extension
# into the installed openviking package.
RUN --mount=type=cache,target=/root/.cache/uv,id=uv-${TARGETPLATFORM} \
    uv pip install maturin && \
    export _TMPDIR=$(mktemp -d) && \
    trap 'rm -rf "$_TMPDIR"' EXIT && \
    cd crates/ragfs-python && \
    python -m maturin build --release --out "$_TMPDIR" && \
    cd ../.. && \
    export _OV_LIB=$(python -c "import openviking; from pathlib import Path; print(Path(openviking.__file__).resolve().parent / 'lib')") && \
    mkdir -p "$_OV_LIB" && \
    python - <<'PY'
import glob
import os
import sys
import zipfile

tmpdir = os.environ["_TMPDIR"]
ov_lib = os.environ["_OV_LIB"]
whls = glob.glob(os.path.join(tmpdir, "ragfs_python-*.whl"))
assert whls, "maturin produced no wheel"

with zipfile.ZipFile(whls[0]) as zf:
    for name in zf.namelist():
        bn = os.path.basename(name)
        if bn.startswith("ragfs_python") and (bn.endswith(".so") or bn.endswith(".pyd")):
            dst = os.path.join(ov_lib, bn)
            with zf.open(name) as src, open(dst, "wb") as f:
                f.write(src.read())
            os.chmod(dst, 0o755)
            print(f"ragfs-python: extracted {bn} -> {dst}")
            sys.exit(0)

print("WARNING: No ragfs_python .so/.pyd in wheel")
sys.exit(1)
PY

# Stage 3: runtime
FROM python:3.13-slim-trixie

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    libstdc++6 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=py-builder /app/.venv /app/.venv
COPY docker/openviking-console-entrypoint.sh /usr/local/bin/openviking-console-entrypoint
COPY docker/pending_health_server.py /usr/local/bin/openviking-pending-health
RUN mkdir -p /app/.openviking \
 && chmod +x /usr/local/bin/openviking-console-entrypoint /usr/local/bin/openviking-pending-health
ENV HOME="/app" \
    PATH="/app/.venv/bin:$PATH" \
    OPENVIKING_CONFIG_FILE="/app/.openviking/ov.conf" \
    OPENVIKING_CLI_CONFIG_FILE="/app/.openviking/ovcli.conf"

EXPOSE 1933 8020

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD curl -fsS http://127.0.0.1:1933/health || exit 1

# All persistent state (ov.conf, ovcli.conf, workspace data) lives under
# /app/.openviking, which mirrors the host's ~/.openviking layout. Mount one
# volume there to persist everything across container restarts:
#   docker run -v ~/.openviking:/app/.openviking <image>
# If ov.conf is absent on first start, set OPENVIKING_CONF_CONTENT to the full
# JSON, or `docker exec` in and run `openviking-server init`.
# Override command to run CLI, e.g.:
# docker run --rm -v ~/.openviking:/app/.openviking <image> openviking --help
ENTRYPOINT ["openviking-console-entrypoint"]
```

### `Makefile`

- Source path: `Makefile`
- Truncated: `no`

```
# Makefile for OpenViking

# Variables
PYTHON ?= python3
SETUP_PY := setup.py
OV_CLI_DIR := crates/ov_cli

# Dependency Versions
MIN_PYTHON_VERSION := 3.10
MIN_CMAKE_VERSION := 3.12
MIN_RUST_VERSION := 1.91.1
MIN_GCC_VERSION := 9
MIN_CLANG_VERSION := 11

# Output directories to clean
CLEAN_DIRS := \
	build/ \
	dist/ \
	*.egg-info/ \
	openviking/bin/ \
	openviking/lib/ \
	$(OV_CLI_DIR)/target/ \
	src/cmake_build/ \
	.pytest_cache/ \
	.coverage \
	htmlcov/ \
	**/__pycache__/

.PHONY: all build clean help check-pip check-deps

all: build

help:
	@echo "Available targets:"
	@echo "  build       - Build ragfs-python and C++ extensions using setup.py"
	@echo "  clean       - Remove build artifacts and temporary files"
	@echo "  check-deps  - Check if required dependencies (Rust, CMake, etc.) are installed"
	@echo "  help        - Show this help message"

check-pip:
	@if command -v uv > /dev/null 2>&1 && uv pip --help > /dev/null 2>&1; then \
		echo "  [OK] uv pip found"; \
	elif $(PYTHON) -m pip --version > /dev/null 2>&1; then \
		echo "  [OK] pip found"; \
	else \
		echo "Error: Neither uv pip nor pip found for $(PYTHON)."; \
		echo "Try fixing your environment by running:"; \
		echo "  uv sync          # if using uv"; \
		echo "  or"; \
		echo "  $(PYTHON) -m ensurepip --upgrade"; \
		exit 1; \
	fi

check-deps:
	@echo "Checking dependencies..."
	@# Python check
	@$(PYTHON) -c "import sys; v=sys.version_info; exit(0 if v.major > 3 or (v.major == 3 and v.minor >= 10) else 1)" || (echo "Error: Python >= $(MIN_PYTHON_VERSION) is required."; exit 1)
	@echo "  [OK] Python $$( $(PYTHON) -V | cut -d' ' -f2 )"
	@# CMake check
	@command -v cmake > /dev/null 2>&1 || (echo "Error: CMake is not installed."; exit 1)
	@CMAKE_VER=$$(cmake --version | head -n1 | awk '{print $$3}'); \
	$(PYTHON) -c "v='$$CMAKE_VER'.split('.'); exit(0 if int(v[0]) > 3 or (int(v[0]) == 3 and int(v[1]) >= 12) else 1)" || (echo "Error: CMake >= $(MIN_CMAKE_VERSION) is required. Found $$CMAKE_VER"; exit 1); \
	echo "  [OK] CMake $$CMAKE_VER"
	@# Rust check
	@command -v rustc > /dev/null 2>&1 || (echo "Error: Rust is not installed."; exit 1)
	@RUST_VER=$$(rustc --version | awk '{print $$2}'); \
	$(PYTHON) -c "import sys; parse=lambda v: tuple(int(x) for x in v.split('.')); raise SystemExit(0 if parse(sys.argv[1]) >= parse(sys.argv[2]) else 1)" "$$RUST_VER" "$(MIN_RUST_VERSION)" || (echo "Error: Rust >= $(MIN_RUST_VERSION) is required. Found $$RUST_VER"; exit 1); \
	echo "  [OK] Rust $$RUST_VER"
	@# C++ Compiler check
	@if command -v clang++ > /dev/null 2>&1; then \
		CLANG_VER_FULL=$$(clang++ --version | head -n1 | grep -oE "[0-9]+\.[0-9]+\.[0-9]+" | head -n1); \
		CLANG_VER=$$(echo $$CLANG_VER_FULL | cut -d. -f1); \
		if [ $$CLANG_VER -lt $(MIN_CLANG_VERSION) ]; then echo "Error: Clang >= $(MIN_CLANG_VERSION) is required. Found $$CLANG_VER_FULL"; exit 1; fi; \
		echo "  [OK] Clang $$CLANG_VER_FULL"; \
	elif command -v g++ > /dev/null 2>&1; then \
		GCC_VER_FULL=$$(g++ -dumpversion); \
		GCC_VER=$$(echo $$GCC_VER_FULL | cut -d. -f1); \
		if [ $$GCC_VER -lt $(MIN_GCC_VERSION) ]; then echo "Error: GCC >= $(MIN_GCC_VERSION) is required. Found $$GCC_VER_FULL"; exit 1; fi; \
		echo "  [OK] GCC $$GCC_VER_FULL"; \
	else \
		echo "Error: C++ compiler (GCC or Clang) is required."; exit 1; \
	fi

build: check-deps check-pip
	@echo "Starting build process via setup.py..."
	$(PYTHON) $(SETUP_PY) build_ext --inplace
	@if command -v uv > /dev/null 2>&1 && uv pip --help > /dev/null 2>&1; then \
		echo "  [OK] uv pip found, use uv pip to install..."; \
		uv pip install -e .; \
	else \
		echo "  [OK] pip found, use pip to install..."; \
		$(PYTHON) -m pip install -e .; \
	fi
	@echo "Building ragfs-python (Rust RAGFS binding) into openviking/lib/..."
	@MATURIN_CMD=""; \
	if command -v maturin > /dev/null 2>&1; then \
		MATURIN_CMD=maturin; \
	elif command -v uv > /dev/null 2>&1 && uv pip --help > /dev/null 2>&1; then \
		uv pip install maturin && MATURIN_CMD=maturin; \
	fi; \
	if [ -n "$$MATURIN_CMD" ]; then \
		TMPDIR=$$(mktemp -d); \
		cd crates/ragfs-python && $$MATURIN_CMD build --release --out "$$TMPDIR" 2>&1; \
		cd ../..; \
		mkdir -p openviking/lib; \
		rm -f openviking/lib/ragfs_python*.so openviking/lib/ragfs_python*.pyd openviking/lib/ragfs_python*.dylib; \
		echo "import zipfile, glob, shutil, os, sys" > /tmp/extract_ragfs.py; \
		echo "whls = glob.glob(os.path.join('$$TMPDIR', 'ragfs_python-*.whl'))" >> /tmp/extract_ragfs.py; \
		echo "assert whls, 'maturin produced no wheel'" >> /tmp/extract_ragfs.py; \
		echo "with zipfile.ZipFile(whls[0]) as zf:" >> /tmp/extract_ragfs.py; \
		echo "    for name in zf.namelist():" >> /tmp/extract_ragfs.py; \
		echo "        bn = os.path.basename(name)" >> /tmp/extract_ragfs.py; \
		echo "        if bn.startswith('ragfs_python.abi3.') and (bn.endswith('.so') or bn.endswith('.pyd')):" >> /tmp/extract_ragfs.py; \
		echo "            dst = os.path.join('openviking', 'lib', bn)" >> /tmp/extract_ragfs.py; \
		echo "            with zf.open(name) as src, open(dst, 'wb') as f: f.write(src.read())" >> /tmp/extract_ragfs.py; \
		echo "            os.chmod(dst, 0o755)" >> /tmp/extract_ragfs.py; \
		echo "            print(f'  [OK] ragfs-python: extracted {bn} -> {dst}')" >> /tmp/extract_ragfs.py; \
		echo "            sys.exit(0)" >> /tmp/extract_ragfs.py; \
		echo "print('[Warning] No ragfs_python abi3 .so/.pyd found in wheel')" >> /tmp/extract_ragfs.py; \
		echo "sys.exit(1)" >> /tmp/extract_ragfs.py; \
		$(PYTHON) /tmp/extract_ragfs.py; \
		rm -f /tmp/extract_ragfs.py; \
		rm -rf "$$TMPDIR"; \
	else \
		echo "  [SKIP] maturin not found, ragfs-python (Rust binding) will not be built."; \
		echo "         Install maturin to enable: uv pip install maturin"; \
	fi
	@echo "Build completed successfully."

clean:
	@echo "Cleaning up build artifacts..."
	@for dir in $(CLEAN_DIRS); do \
		if [ -d "$$dir" ] || [ -f "$$dir" ]; then \
			echo "Removing $$dir"; \
			rm -rf $$dir; \
		fi \
	done
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} +
	@echo "Cleanup completed."
```

### `README.md`

- Source path: `README.md`
- Truncated: `no`

```md
<div align="center">

<a href="https://openviking.ai/" target="_blank">
  <picture>
    <img alt="OpenViking" src="docs/images/ov-logo.png" width="200px" height="auto">
  </picture>
</a>

### OpenViking: The Context Database for AI Agents

English / [中文](README_CN.md) / [日本語](README_JA.md)

<a href="https://www.openviking.ai">Website</a> · <a href="https://github.com/volcengine/OpenViking">GitHub</a> · <a href="https://github.com/volcengine/OpenViking/issues">Issues</a> · <a href="./docs">Docs</a>

[![](https://img.shields.io/github/v/release/volcengine/OpenViking?color=369eff\&labelColor=black\&logo=github\&style=flat-square)](https://github.com/volcengine/OpenViking/releases)
[![](https://img.shields.io/github/stars/volcengine/OpenViking?labelColor\&style=flat-square\&color=ffcb47)](https://github.com/volcengine/OpenViking)
[![](https://img.shields.io/github/issues/volcengine/OpenViking?labelColor=black\&style=flat-square\&color=ff80eb)](https://github.com/volcengine/OpenViking/issues)
[![](https://img.shields.io/github/contributors/volcengine/OpenViking?color=c4f042\&labelColor=black\&style=flat-square)](https://github.com/volcengine/OpenViking/graphs/contributors)
[![](https://img.shields.io/badge/license-AGPLv3-white?labelColor=black\&style=flat-square)](https://github.com/volcengine/OpenViking/blob/main/LICENSE)
[![](https://img.shields.io/github/last-commit/volcengine/OpenViking?color=c4f042\&labelColor=black\&style=flat-square)](https://github.com/volcengine/OpenViking/commits/main)

👋 Join our Community

📱 <a href="./docs/en/about/01-about-us.md#lark-group">Lark Group</a> · <a href="./docs/en/about/01-about-us.md#wechat-group">WeChat</a> · <a href="https://discord.com/invite/eHvx8E9XF3">Discord</a> · <a href="https://x.com/openvikingai">X</a>

<a href="https://trendshift.io/repositories/19668" target="_blank"><img src="https://trendshift.io/api/badge/repositories/19668" alt="volcengine%2FOpenViking | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

***

## Overview

### Challenges in Agent Development

In the AI era, data is abundant, but high-quality context is hard to come by. When building AI Agents, developers often face these challenges:

- **Fragmented Context**: Memories are in code, resources are in vector databases, and skills are scattered, making them difficult to manage uniformly.
- **Surging Context Demand**: An Agent's long-running tasks produce context at every execution. Simple truncation or compression leads to information loss.
- **Poor Retrieval Effectiveness**: Traditional RAG uses flat storage, lacking a global view and making it difficult to understand the full context of information.
- **Unobservable Context**: The implicit retrieval chain of traditional RAG is like a black box, making it hard to debug when errors occur.
- **Limited Memory Iteration**: Current memory is just a record of user interactions, lacking Agent-related task memory.

### The OpenViking Solution

**OpenViking** is an open-source **Context Database** designed specifically for AI Agents.

We aim to define a minimalist context interaction paradigm for Agents, allowing developers to completely say goodbye to the hassle of context management. OpenViking abandons the fragmented vector storage model of traditional RAG and innovatively adopts a **"file system paradigm"** to unify the structured organization of memories, resources, and skills needed by Agents.

With OpenViking, developers can build an Agent's brain just like managing local files:

- **Filesystem Management Paradigm** → **Solves Fragmentation**: Unified context management of memories, resources, and skills based on a filesystem paradigm.
- **Tiered Context Loading** → **Reduces Token Consumption**: L0/L1/L2 three-tier structure, loaded on demand, significantly saving costs.
- **Directory Recursive Retrieval** → **Improves Retrieval Effect**: Supports native filesystem retrieval methods, combining directory positioning with semantic search to achieve recursive and precise context acquisition.
- **Visualized Retrieval Trajectory** → **Observable Context**: Supports visualization of directory retrieval trajectories, allowing users to clearly observe the root cause of issues and guide retrieval logic optimization.
- **Automatic Session Management** → **Context Self-Iteration**: Automatically compresses content, resource references, tool calls, etc., in conversations, extracting long-term memory, making the Agent smarter with use.

***

## Quick Start

### Prerequisites

Before starting with OpenViking, please ensure your environment meets the following requirements:

- **Python Version**: 3.10 or higher
- **Rust Toolchain**: Cargo (Required for building RAGFS and CLI components from source)
- **C++ Compiler**: GCC 9+ or Clang 11+ (Required for building core extensions)
- **Operating System**: Linux, macOS, Windows
- **Network Connection**: A stable network connection is required (for downloading dependencies and accessing model services)

### 1. Installation

#### Python Package

```bash
pip install openviking --upgrade --force-reinstall
```

#### Rust CLI (Optional)

```bash
curl -fsSL https://raw.githubusercontent.com/volcengine/OpenViking/main/crates/ov_cli/install.sh | bash
```

Or build from source:

```bash
cargo install --git https://github.com/volcengine/OpenViking ov_cli
```

### 2. Model Preparation

OpenViking requires the following model capabilities:

- **VLM Model**: For image and content understanding
- **Embedding Model**: For vectorization and semantic retrieval

#### Supported VLM Providers

OpenViking supports multiple VLM providers:

| Provider       | Description              | Setup                                                                                                                                                                                                              |
| -------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `volcengine`   | Volcengine Doubao Models | [Volcengine Console](https://console.volcengine.com/ark/region:ark+cn-beijing/overview?briefPage=0\&briefType=introduce\&type=new\&utm_content=OpenViking\&utm_medium=devrel\&utm_source=OWO\&utm_term=OpenViking) |
| `openai`       | OpenAI Official API      | [OpenAI Platform](https://platform.openai.com)                                                                                                                                                                     |
| `openai-codex` | Codex VLM                | Use `openviking-server init`                                                                                                                                                                                       |
| `kimi`         | Kimi Code Membership     | Use `openviking-server init`                                                                                                                                                                                       |
| `glm`          | GLM Coding Plan          | Use `openviking-server init`                                                                                                                                                                                       |

#### Provider-Specific Notes

<details>
<summary><b>Volcengine (Doubao)</b></summary>

Volcengine supports both model names and endpoint IDs. Using model names is recommended for simplicity:

```json
{
  "vlm": {
    "provider": "volcengine",
    "model": "doubao-seed-2-0-pro-260215",
    "api_key": "your-api-key",
    "api_base": "https://ark.cn-beijing.volces.com/api/v3"
  }
}
```

You can also use endpoint IDs (found in [Volcengine ARK Console](https://console.volcengine.com/ark/region:ark+cn-beijing/overview?briefPage=0\&briefType=introduce\&type=new\&utm_content=OpenViking\&utm_medium=devrel\&utm_source=OWO\&utm_term=OpenViking):

```json
{
  "vlm": {
    "provider": "volcengine",
    "model": "ep-20241220174930-xxxxx",
    "api_key": "your-api-key",
    "api_base": "https://ark.cn-beijing.volces.com/api/v3"
  }
}
```

</details>

<details>
<summary><b>OpenAI</b></summary>

Use OpenAI's official API:

```json
{
  "vlm": {
    "provider": "openai",
    "model": "gpt-4o",
    "api_key": "your-api-key",
    "api_base": "https://api.openai.com/v1"
  }
}
```

You can also use a custom OpenAI-compatible endpoint:

```json
{
  "vlm": {
    "provider": "openai",
    "model": "gpt-4o",
    "api_key": "your-api-key",
    "api_base": "https://your-custom-endpoint.com/v1"
  }
}
```

</details>

<details>
<summary><b>OpenAI Codex (OAuth)</b></summary>

Use this provider when you want OpenViking to call Codex VLM through your ChatGPT/Codex OAuth session instead of a standard OpenAI API key:

```bash
openviking-server init
# choose OpenAI Codex when prompted
openviking-server doctor
```

```json
{
  "vlm": {
    "provider": "openai-codex",
    "model": "gpt-5.3-codex",
    "api_base": "https://chatgpt.com/backend-api/codex",
    "temperature": 0.0,
    "max_retries": 2
  }
}
```

> 💡 **Tip**:
>
> - `openai-codex` does not require `vlm.api_key` when Codex OAuth is available
> - OpenViking stores its own Codex auth state at `~/.openviking/codex_auth.json`
> - `openviking-server doctor` validates that the current Codex auth is usable

</details>

<details>
<summary><b>Kimi Coding (Subscription)</b></summary>

Use this provider when you want OpenViking to call the dedicated Kimi Coding subscription endpoint directly:

```bash
openviking-server init
# choose Kimi Coding when prompted
openviking-server doctor
```

```json
{
  "vlm": {
    "provider": "kimi",
    "model": "kimi-code",
    "api_key": "your-kimi-subscription-api-key",
    "api_base": "https://api.kimi.com/coding",
    "temperature": 0.0,
    "max_retries": 2
  }
}
```

> 💡 **Tip**:
>
> - `kimi` applies the recommended Kimi Coding defaults automatically, including the default Kimi Coding user agent
> - `kimi-code` and `kimi-coding` are accepted aliases for the provider name
> - `kimi-code` is normalized to Kimi's upstream coding model automatically

</details>

<details>
<summary><b>GLM Coding Plan (Subscription)</b></summary>

Use this provider when you want OpenViking to call Z.AI's OpenAI-compatible Coding Plan endpoint directly:

```bash
openviking-server init
# choose GLM Coding Plan when prompted
openviking-server doctor
```

```json
{
  "vlm": {
    "provider": "glm",
    "model": "glm-4.6v",
    "api_key": "your-zai-api-key",
    "api_base": "https://api.z.ai/api/coding/paas/v4",
    "temperature": 0.0,
    "max_retries": 2
  }
}
```

> 💡 **Tip**:
>
> - `glm`, `zhipu`, `zai`, `z-ai`, and `z.ai` all resolve to the same first-class GLM provider
> - The default endpoint is the Coding Plan endpoint, not the general Z.AI endpoint
> - Use a vision-capable model such as `glm-4.6v` or `glm-5v-turbo` for multimodal parsing

</details>

### 3. Environment Configuration

#### Quick Setup for Local Models (Ollama)

If you want to run OpenViking with local models via [Ollama](https://ollama.ai), the interactive setup wizard handles everything automatically:

```bash
openviking-server init
```

The wizard will:

- Detect and install Ollama if needed
- Recommend and pull suitable embedding and VLM models for your hardware
- Generate a ready-to-use `ov.conf` configuration file

To validate your setup at any time:

```bash
openviking-server doctor
```

`doctor` checks local prerequisites (config file, Python version, embedding/VLM provider connectivity, disk space) without requiring a running server.

> For cloud API providers (Volcengine, OpenAI, Gemini, etc.), continue with the manual configuration below.

#### Server Configuration Template

The recommended first-time flow is:

```bash
openviking-server init
openviking-server doctor
```

If you choose `OpenAI Codex` inside `openviking-server init`, the wizard can import existing Codex auth or start the Codex sign-in flow for you.

If you prefer manual configuration, create `~/.openviking/ov.conf`, remove the comments before copy:

```json
{
  "storage": {
    "workspace": "/home/your-name/openviking_workspace"
  },
  "log": {
    "level": "INFO",
    "output": "stdout"                 // Log output: "stdout" or "file"
  },
  "embedding": {
    "dense": {
      "api_base" : "<api-endpoint>",   // API endpoint address
      "api_key"  : "<your-api-key>",   // Model service API Key
      "provider" : "<provider-type>",  // Provider type: "volcengine" or "openai" (currently supported)
      "dimension": 1024,               // Vector dimension
      "model"    : "<model-name>"      // Embedding model name (e.g., doubao-embedding-vision-251215 or text-embedding-3-large)
    },
    "max_concurrent": 10,              // Max concurrent embedding requests (default: 10)
    "text_source": "content_only",     // Text file vectorization source: content_only|summary_first|summary_only
    "max_input_tokens": 4096           // Max estimated raw text tokens sent to embedding
  },
  "vlm": {
    "api_base" : "<api-endpoint>",     // API endpoint address
    "api_key"  : "<your-api-key>",     // Model service API Key (optional for openai-codex)
    "provider" : "<provider-type>",    // Provider type (volcengine, openai, openai-codex, kimi, glm, etc.)
    "model"    : "<model-name>",       // VLM model name (e.g., doubao-seed-2-0-pro-260215 or gpt-4-vision-preview)
    "max_concurrent": 100              // Max concurrent LLM calls for semantic processing (default: 100)
  }
}
```

> **Note**: For embedding models, supported providers are `volcengine` (Doubao), `openai`, `azure`, `jina`, `ollama`, `voyage`, `dashscope`, `minimax`, `cohere`, `vikingdb`, `gemini` (requires `pip install "google-genai>=1.0.0"`), `litellm`, and `local`. For VLM models, common providers include `volcengine`, `openai`, `openai-codex`, `kimi`, and `glm`.

#### Server Configuration Examples

👇 Expand to see the configuration example for your model service:

<details>
<summary><b>Example 1: Using Volcengine (Doubao Models)</b></summary>

```json
{
  "storage": {
    "workspace": "/home/your-name/openviking_workspace"
  },
  "log": {
    "level": "INFO",
    "output": "stdout"                 // Log output: "stdout" or "file"
  },
  "embedding": {
    "dense": {
      "api_base" : "https://ark.cn-beijing.volces.com/api/v3",
      "api_key"  : "your-volcengine-api-key",
      "provider" : "volcengine",
      "dimension": 1024,
      "model"    : "doubao-embedding-vision-251215"
    },
    "max_concurrent": 10
  },
  "vlm": {
    "api_base" : "https://ark.cn-beijing.volces.com/api/v3",
    "api_key"  : "your-volcengine-api-key",
    "provider" : "volcengine",
    "model"    : "doubao-seed-2-0-pro-260215",
    "max_concurrent": 100
  }
}
```

</details>

<details>
<summary><b>Example 2: Using OpenAI Models</b></summary>

```json
{
  "storage": {
    "workspace": "/home/your-name/openviking_workspace"
  },
  "log": {
    "level": "INFO",
    "output": "stdout"                 // Log output: "stdout" or "file"
  },
  "embedding": {
    "dense": {
      "api_base" : "https://api.openai.com/v1",
      "api_key"  : "your-openai-api-key",
      "provider" : "openai",
      "dimension": 3072,
      "model"    : "text-embedding-3-large"
    },
    "max_concurrent": 10
  },
  "vlm": {
    "api_base" : "https://api.openai.com/v1",
    "api_key"  : "your-openai-api-key",
    "provider" : "openai",
    "model"    : "gpt-4-vision-preview",
    "max_concurrent": 100
  }
}
```

</details>

<details>
<summary><b>Example 3: Using Google Gemini Embedding</b></summary>

Install the required package first:

```bash
pip install "google-genai>=1.0.0"
```

```json
{
  "storage": {
    "workspace": "/home/your-name/openviking_workspace"
  },
  "embedding": {
    "dense": {
      "provider": "gemini",
      "api_key": "your-google-api-key",
      "model": "gemini-embedding-2-preview",
      "dimension": 3072
    },
    "max_concurrent": 10
  },
  "vlm": {
    "api_base" : "https://api.openai.com/v1",
    "api_key"  : "your-openai-api-key",
    "provider" : "openai",
    "model"    : "gpt-4o",
    "max_concurrent": 100
  }
}
```

Get your Google API key at <https://aistudio.google.com/apikey>

</details>

<details>
<summary><b>Example 4: Using Volcengine Embedding + Codex VLM</b></summary>

Use `openviking-server init` and choose `OpenAI Codex`, then run `openviking-server doctor`.

```json
{
  "storage": {
    "workspace": "/home/your-name/openviking_workspace"
  },
  "embedding": {
    "dense": {
      "api_base" : "https://ark.cn-beijing.volces.com/api/v3",
      "api_key"  : "your-volcengine-api-key",
      "provider" : "volcengine",
      "dimension": 1024,
      "model"    : "doubao-embedding-vision-251215"
    }
  },
  "vlm": {
    "api_base" : "https://chatgpt.com/backend-api/codex",
    "provider" : "openai-codex",
    "model"    : "gpt-5.3-codex",
    "max_concurrent": 100
  }
}
```

</details>

#### Set Server Configuration Environment Variable

After creating the configuration file, set the environment variable to point to it (Linux/macOS):

```bash
export OPENVIKING_CONFIG_FILE=~/.openviking/ov.conf # by default
```

On Windows, use one of the following:

PowerShell:

```powershell
$env:OPENVIKING_CONFIG_FILE = "$HOME/.openviking/ov.conf"
```

Command Prompt (cmd.exe):

```bat
set "OPENVIKING_CONFIG_FILE=%USERPROFILE%\.openviking\ov.conf"
```

> 💡 **Tip**: You can also place the configuration file in other locations, just specify the correct path in the environment variable.

#### CLI/Client Configuration Examples

👇 Expand to see the configuration example for your CLI/Client:

Example: ovcli.conf for visiting localhost server

```json
{
  "url": "http://localhost:1933",
  "timeout": 60.0,
  "output": "table"
}
```

After creating the configuration file, set the environment variable to point to it (Linux/macOS):

```bash
export OPENVIKING_CLI_CONFIG_FILE=~/.openviking/ovcli.conf # by default
```

On Windows, use one of the following:

PowerShell:

```powershell
$env:OPENVIKING_CLI_CONFIG_FILE = "$HOME/.openviking/ovcli.conf"
```

Command Prompt (cmd.exe):

```bat
set "OPENVIKING_CLI_CONFIG_FILE=%USERPROFILE%\.openviking\ovcli.conf"
```

### 4. Run Your First Example

> 📝 **Prerequisite**: Ensure you have completed the configuration (ov.conf and ovcli.conf) in the previous step.

Now let's run a complete example to experience the core features of OpenViking.

#### Launch Server

```bash
openviking-server doctor
openviking-server
```

If you configured `provider=openai-codex`, `openviking-server doctor` already validates Codex auth.

or you can run in background

```bash
nohup openviking-server > /data/log/openviking.log 2>&1 &
```

#### Run the CLI

```bash
ov status
ov add-resource https://github.com/volcengine/OpenViking # --wait
ov ls viking://resources/
ov tree viking://resources/volcengine -L 2
# wait some time for semantic processing if not --wait
ov find "what is openviking"
ov grep "openviking" --uri viking://resources/volcengine/OpenViking/docs/zh
```

Congratulations! You have successfully run OpenViking 🎉

### VikingBot Quick Start

VikingBot is an AI agent framework built on top of OpenViking. Here's how to get started:

```bash
# Option 1: Install VikingBot from PyPI (recommended for most users)
pip install "openviking[bot]"

# Option 2: Install VikingBot from source (for development)
uv pip install -e ".[bot]"

# Start OpenViking server with Bot enabled
openviking-server --with-bot

# In another terminal, start interactive chat
ov chat
```

If you use the official Docker image, `vikingbot` is already bundled in the image and starts by default together with the OpenViking server and console UI. You can disable it at runtime with either `--without-bot` or `-e OPENVIKING_WITH_BOT=0`.

***

## Server Deployment Details

For production environments, we recommend running OpenViking as a standalone HTTP service to provide persistent, high-performance context support for your AI Agents.

🚀 **Deploy OpenViking on Cloud**:
To ensure optimal storage performance and data security, we recommend deploying on **Volcengine Elastic Compute Service (ECS)** using the **veLinux** operating system. We have prepared a detailed step-by-step guide to get you started quickly.

👉 **[View: Server Deployment & ECS Setup Guide](./docs/en/getting-started/03-quickstart-server.md)**

## OpenClaw Context Plugin Details

- Test Dataset: Effect testing based on LoCoMo10 (<https://github.com/snap-research/locomo>) long-range dialogues (1,540 cases in total after removing category5 without ground truth)
- Experimental Groups: Since users may not disable OpenClaw's native memory when using OpenViking, we added experimental groups with native memory enabled or disabled
- OpenViking Version: 0.1.18
- Model: seed-2.0-code
- Evaluation Script: <https://github.com/ZaynJarvis/openclaw-eval/tree/main>

| Experimental Group                          | Task Completion Rate | Cost: Input Tokens (Total) |
| ------------------------------------------- | -------------------- | -------------------------- |
| OpenClaw(memory-core)                       | 35.65%               | 24,611,530                 |
| OpenClaw + LanceDB (-memory-core)           | 44.55%               | 51,574,530                 |
| OpenClaw + OpenViking Plugin (-memory-core) | 52.08%               | 4,264,396                  |
| OpenClaw + OpenViking Plugin (+memory-core) | 51.23%               | 2,099,622                  |

- Experimental Conclusions:
  After integrating OpenViking:

* With native memory enabled: 43% improvement over original OpenClaw with 91% reduction in input token cost; 15% improvement over LanceDB with 96% reduction in input token cost.
* With native memory disabled: 49% improvement over original OpenClaw with 83% reduction in input token cost; 17% improvement over LanceDB with 92% reduction in input token cost.

👉 **[View: OpenClaw Context Plugin](examples/openclaw-plugin/README.md)**

👉 **[View: OpenCode Memory Plugin Example](examples/opencode-memory-plugin/README.md)**

👉 **[View: Claude Code Memory Plugin Example](examples/claude-code-memory-plugin/README.md)**

\--

## Core Concepts

After running the first example, let's dive into the design philosophy of OpenViking. These five core concepts correspond one-to-one with the solutions mentioned earlier, together building a complete context management system:

### 1. Filesystem Management Paradigm → Solves Fragmentation

We no longer view context as flat text slices but unify them into an abstract virtual filesystem. Whether it's memories, resources, or capabilities, they are mapped to virtual directories under the `viking://` protocol, each with a unique URI.

This paradigm gives Agents unprecedented context manipulation capabilities, enabling them to locate, browse, and manipulate information precisely and deterministically through standard commands like `ls` and `find`, just like a developer. This transforms context management from vague semantic matching into intuitive, traceable "file operations". Learn more: [Viking URI](./docs/en/concepts/04-viking-uri.md) | [Context Types](./docs/en/concepts/02-context-types.md)

```
viking://
├── resources/              # Resources: project docs, repos, web pages, etc.
│   ├── my_project/
│   │   ├── docs/
│   │   │   ├── api/
│   │   │   └── tutorials/
│   │   └── src/
│   └── ...
├── user/                   # User: personal preferences, habits, etc.
│   └── memories/
│       ├── preferences/
│       │   ├── writing_style
│       │   └── coding_habits
│       └── ...
└── agent/                  # Agent: skills, instructions, task memories, etc.
    ├── skills/
    │   ├── search_code
    │   ├── analyze_data
    │   └── ...
    ├── memories/
    └── instructions/
```

### 2. Tiered Context Loading → Reduces Token Consumption

Stuffing massive amounts of context into a prompt all at once is not only expensive but also prone to exceeding model windows and introducing noise. OpenViking automatically processes context into three levels upon writing:

- **L0 (Abstract)**: A one-sentence summary for quick retrieval and identification.
- **L1 (Overview)**: Contains core information and usage scenarios for Agent decision-making during the planning phase.
- **L2 (Details)**: The full original data, for deep reading by the Agent when absolutely necessary.

Learn more: [Context Layers](./docs/en/concepts/03-context-layers.md)

```
viking://resources/my_project/
├── .abstract               # L0 Layer: Abstract (~100 tokens) - Quick relevance check
├── .overview               # L1 Layer: Overview (~2k tokens) - Understand structure and key points
├── docs/
│   ├── .abstract          # Each directory has corresponding L0/L1 layers
│   ├── .overview
│   ├── api/
│   │   ├── .abstract
│   │   ├── .overview
│   │   ├── auth.md        # L2 Layer: Full content - Load on demand
│   │   └── endpoints.md
│   └── ...
└── src/
    └── ...
```

### 3. Directory Recursive Retrieval → Improves Retrieval Effect

Single vector retrieval struggles with complex query intents. OpenViking has designed an innovative **Directory Recursive Retrieval Strategy** that deeply integrates multiple retrieval methods:

1. **Intent Analysis**: Generate multiple retrieval conditions through intent analysis.
2. **Initial Positioning**: Use vector retrieval to quickly locate the high-score directory where the initial slice is located.
3. **Refined Exploration**: Perform a secondary retrieval within that directory and update high-score results to the candidate set.
4. **Recursive Drill-down**: If subdirectories exist, recursively repeat the secondary retrieval steps layer by layer.
5. **Result Aggregation**: Finally, obtain the most relevant context to return.

This "lock high-score directory first, then refine content exploration" strategy not only finds the semantically best-matching fragments but also understands the full context where the information resides, thereby improving the globality and accuracy of retrieval. Learn more: [Retrieval Mechanism](./docs/en/concepts/07-retrieval.md)

### 4. Visualized Retrieval Trajectory → Observable Context

OpenViking's organization uses a hierarchical virtual filesystem structure. All context is integrated in a unified format, and each entry corresponds to a unique URI (like a `viking://` path), breaking the traditional flat black-box management mode with a clear hierarchy that is easy to understand.

The retrieval process adopts a directory recursive strategy. The trajectory of directory browsing and file positioning for each retrieval is fully preserved, allowing users to clearly observe the root cause of problems and guide the optimization of retrieval logic. Learn more: [Retrieval Mechanism](./docs/en/concepts/07-retrieval.md)

### 5. Automatic Session Management → Context Self-Iteration

OpenViking has a built-in memory self-iteration loop. At the end of each session, developers can actively trigger the memory extraction mechanism. The system will asynchronously analyze task execution results and user feedback, and automatically update them to the User and Agent memory directories.

- **User Memory Update**: Update memories related to user preferences, making Agent responses better fit user needs.
- **Agent Experience Accumulation**: Extract core content such as operational tips and tool usage experience from task execution experience, aiding efficient decision-making in subsequent tasks.

This allows the Agent to get "smarter with use" through interactions with the world, achieving self-evolution. Learn more: [Session Management](./docs/en/concepts/08-session.md)

***

## Advanced Reading

### Documentation

For more details, please visit our [Full Documentation](./docs/en/).

### Community & Team

For more details, please see: **[About Us](./docs/en/about/01-about-us.md)**

### Join the Community

OpenViking is still in its early stages, and there are many areas for improvement and exploration. We sincerely invite every developer passionate about AI Agent technology:

- Light up a precious **Star** for us to give us the motivation to move forward.
- Visit our **[Website](https://www.openviking.ai)** to understand the philosophy we convey, and use it in your projects via the **[Documentation](https://www.openviking.ai/docs)**. Feel the change it brings and give us feedback on your truest experience.
- Join our community to share your insights, help answer others' questions, and jointly create an open and mutually helpful technical atmosphere:
  - 📱 **Lark Group**: Scan the QR code to join → [View QR Code](./docs/en/about/01-about-us.md#lark-group)
  - 💬 **WeChat Group**: Scan the QR code to add assistant → [View QR Code](./docs/en/about/01-about-us.md#wechat-group)
  - 🎮 **Discord**: [Join Discord Server](https://discord.com/invite/eHvx8E9XF3)
  - 🐦 **X (Twitter)**：[Follow us](https://x.com/openvikingai)
- Become a **Contributor**, whether submitting a bug fix or contributing a new feature, every line of your code will be an important cornerstone of OpenViking's growth.

Let's work together to define and build the future of AI Agent context management. The journey has begun, looking forward to your participation!

### Star Trend

[![Star History Chart](https://api.star-history.com/svg?repos=volcengine/OpenViking\&type=timeline\&legend=top-left)](https://www.star-history.com/#volcengine/OpenViking\&type=timeline\&legend=top-left)

## License

The OpenViking project uses different licenses for different components:

- **Main Project**: AGPLv3 - see the [LICENSE](./LICENSE) file for details
- **crates/ov\_cli**: Apache 2.0 - see the [LICENSE](./crates/ov_cli/LICENSE) for details
- **examples**: Apache 2.0 - see the [LICENSE](./examples/LICENSE) for details
- **third\_party**: Respective original licenses of third-party projects

<!-- Link Definitions -->
```

### `docker-compose.yml`

- Source path: `docker-compose.yml`
- Truncated: `no`

```yaml
version: "3.8"

services:
  openviking:
    image: ghcr.io/volcengine/openviking:latest
    container_name: openviking
    ports:
      - "1933:1933"
      - "8020:8020"
    volumes:
      # All persistent state (ov.conf, ovcli.conf, workspace) lives here.
      - ~/.openviking:/app/.openviking
    healthcheck:
      test: ["CMD-SHELL", "curl -fsS http://127.0.0.1:1933/health || exit 1"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 30s
    restart: unless-stopped
    # If you need to override the default command (which runs openviking-server),
    # you can do so here. For example, to run the CLI:
    # command: ["openviking", "--help"]
```

### `pyproject.toml`

- Source path: `pyproject.toml`
- Truncated: `no`

```toml
[build-system]
requires = [
    "setuptools>=61.0",
    "setuptools-scm>=8.0",
    "cmake>=3.15",
    "maturin>=1.0,<2.0",
    "wheel",
]
build-backend = "setuptools.build_meta"

[project]
name = "openviking"
dynamic = ["version"]
description = "An Agent-native context database"
readme = "README.md"
requires-python = ">=3.10"
authors = [
    {name = "ByteDance", email = "noreply@bytedance.com"}
]
license = { text = "AGPL-3.0" }
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
]
dependencies = [
    "pydantic>=2.0.0",
    "typing-extensions>=4.5.0",
    "pyyaml>=6.0",
    "httpx>=0.25.0",
    "pdfplumber>=0.10.0",
    "readabilipy>=0.2.0",
    "markdownify>=0.11.0",
    "openai>=1.0.0",
    "requests>=2.31.0",
    "python-docx>=1.0.0",
    "olefile>=0.47",
    "xlrd>=2.0.1",
    "python-pptx>=1.0.0",
    "openpyxl>=3.0.0",
    "ebooklib>=0.18.0",
    "json-repair>=0.25.0",
    "apscheduler>=3.11.0",
    "volcengine>=1.0.216",
    "volcengine-python-sdk[ark]>=5.0.3",
    "fastapi>=0.128.0",
    "uvicorn>=0.39.0",
    "xxhash>=3.0.0",
    "jinja2>=3.1.6",
    "tabulate>=0.9.0",
    "urllib3>=2.6.3",
    "protobuf>=6.33.5",
    "pdfminer-six>=20251230",
    "typer>=0.12.0",
    "litellm>=1.0.0,<1.83.13",
    "python-multipart>=0.0.22",
    "tree-sitter>=0.23.0",
    "tree-sitter-python>=0.23.0",
    "tree-sitter-javascript>=0.23.0",
    "tree-sitter-typescript>=0.23.0",
    "tree-sitter-java>=0.23.0",
    "tree-sitter-cpp>=0.23.0",
    "tree-sitter-rust>=0.23.0",
    "tree-sitter-go>=0.23.0",
    "tree-sitter-c-sharp>=0.23.0",
    "tree-sitter-php>=0.23.0",
    "tree-sitter-lua>=0.1.0",
    # OpenTelemetry
    "opentelemetry-api>=1.14",
    "opentelemetry-sdk>=1.14",
    "opentelemetry-exporter-otlp-proto-grpc>=1.14",
    "opentelemetry-exporter-otlp-proto-http>=1.14",
    "opentelemetry-instrumentation-asyncio>=0.61b0",
    "loguru>=0.7.3",
    "cryptography>=42.0.0",
    "argon2-cffi>=23.0.0",
    "lark-oapi>=1.5.3",
    "mcp>=1.27.0",
]


[project.optional-dependencies]
test = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "boto3>=1.42.44",
    "pytest-cov>=4.0.0",
    "ragas>=0.1.0",
    "datasets>=2.0.0",
    "pandas>=2.0.0",
    "diff-match-patch>=20200713",
    "hvac>=2.0.0",
]
dev = [
    "mypy>=1.0.0",
    "ruff>=0.1.0",
    "setuptools_scm>=10.0.0",
]
doc = [
    "sphinx>=7.0.0",
    "sphinx-rtd-theme>=1.3.0",
    "myst-parser>=2.0.0",
]
eval = [
    "ragas>=0.1.0",
    "datasets>=2.0.0",
    "pandas>=2.0.0",
]
gemini = [
    "google-genai>=1.0.0",
]
gemini-async = [
    "google-genai>=1.0.0",
    "anyio>=4.0.0",
]
ocr = [
    "pytesseract>=0.3.10",
]
build = [
    "setuptools>=61.0",
    "setuptools-scm>=8.0",
    "cmake>=3.15",
    "wheel",
    "build",
]
# vikingbot core dependencies
bot = [
    "pydantic-settings>=2.0.0",
    "websockets>=12.0",
    "websocket-client>=1.6.0",
    "httpx[socks]>=0.25.0",
    "readability-lxml>=0.8.0",
    "rich>=13.0.0",
    "croniter>=2.0.0",
    "socksio>=1.0.0",
    "python-socketio>=5.11.0",
    "msgpack>=1.0.8",
    "python-socks[asyncio]>=2.4.0",
    "prompt-toolkit>=3.0.0",
    "pygments>=2.16.0",
    "html2text>=2020.1.16",
    "beautifulsoup4>=4.12.0",
    "ddgs>=9.0.0",
    "tavily-python>=0.5.0",
    "gradio>=6.6.0",
    "py-machineid>=1.0.0",
    "mcp>=1.0.0",
]
# vikingbot optional features
bot-langfuse = ["langfuse>=3.0.0"]
bot-telegram = ["python-telegram-bot[socks]>=21.0"]
bot-feishu = ["lark-oapi>=1.0.0"]
bot-dingtalk = ["dingtalk-stream>=0.4.0"]
bot-slack = ["slack-sdk>=3.26.0"]
bot-qq = ["qq-botpy>=1.0.0"]
bot-sandbox = [
    "opensandbox>=0.1.0",
    "opensandbox-server>=0.1.0",
    "agent-sandbox>=0.0.23",
]
bot-fuse = ["fusepy>=3.0.1"]
bot-opencode = ["opencode-ai>=0.1.0a0"]
bot-full = [
    "openviking[bot,bot-langfuse,bot-telegram,bot-feishu,bot-dingtalk,bot-slack,bot-qq,bot-sandbox,bot-fuse,bot-opencode]",
]
benchmark = [
    "langchain>=1.0.0",
    "langchain-core>=1.0.0",
    "langchain-openai>=1.0.0",
    "tiktoken>=0.5.0",
    "datasets>=2.0.0",
    "pandas>=2.0.0",
]
local-embed = [
    "llama-cpp-python>=0.3.0",
]

[project.urls]
Homepage = "https://github.com/volcengine/openviking"
Documentation = "https://openviking.ai"
Repository = "https://github.com/volcengine/openviking"
Issues = "https://github.com/volcengine/openviking/issues"

[project.scripts]
ov = "openviking_cli.rust_cli:main"  # Rust CLI 入口（极简包装器）
openviking = "openviking_cli.rust_cli:main"  # Rust CLI 入口（放弃 python CLI）
openviking-server = "openviking_cli.server_bootstrap:main"
vikingbot = "vikingbot.cli.commands:app"

[tool.setuptools_scm]
write_to = "openviking/_version.py"
local_scheme = "no-local-version"
tag_regex = "^(?:v)?(?:[a-zA-Z0-9_]+@)?(?P<version>[0-9]+(?:\\.[0-9]+)*)$"

[tool.setuptools.packages.find]
where = [".", "bot"]
include = ["openviking*", "vikingbot*"]
exclude = ["tests*", "docs*", "examples*"]

[tool.setuptools.package-data]
openviking = [
    "prompts/templates/**/*.yaml",
    "console/static/**/*",
    "lib/ragfs_python*.so",
    "lib/ragfs_python*.pyd",
    "bin/ov",
    "bin/ov.exe",
    "storage/vectordb/engine/*.abi3.so",
    "storage/vectordb/engine/*.pyd",
]
vikingbot = [
    "**/*.mjs",
    "skills/**/*.md",
    "skills/**/*.sh",
    "bridge/**/*",
]

[tool.mypy]
python_version = "3.10"
warn_return_any = false
warn_unused_configs = true
disallow_untyped_defs = false
disallow_incomplete_defs = false
check_untyped_defs = true
no_implicit_optional = false
warn_redundant_casts = true
warn_unused_ignores = true
ignore_missing_imports = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
asyncio_mode = "auto"
addopts = "-v --cov=openviking --cov-report=term-missing"

[tool.ruff]
line-length = 100
exclude = ["third_party"]
target-version = "py310"

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
]
ignore = [
    "E501",  # line too long (handled by black)
    "B008",  # do not perform function calls in argument defaults
    "C901",  # too complex
    "B006",  # Do not use mutable data structures for argument defaults
    "B904",  # Within an `except` clause, raise exceptions with `raise ... from err`
    "E741",  # Ambiguous variable name
    "E722",  # Do not use bare `except`
    "B027",  # empty method in an abstract base class
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]  # Allow unused imports in __init__.py

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

[dependency-groups]
dev = [
    "pytest>=9.0.2",
]
```

### `setup.py`

- Source path: `setup.py`
- Truncated: `no`

```python
import importlib
import json
import os
import platform
import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

try:
    from wheel.bdist_wheel import bdist_wheel
except ImportError:  # pragma: no cover - local build_ext may not have wheel installed
    bdist_wheel = None

SETUP_DIR = Path(__file__).resolve().parent
if str(SETUP_DIR) not in sys.path:
    sys.path.insert(0, str(SETUP_DIR))

get_host_engine_build_config = importlib.import_module(
    "build_support.x86_profiles"
).get_host_engine_build_config
resolve_openviking_version = importlib.import_module(
    "build_support.versioning"
).resolve_openviking_version

CMAKE_PATH = shutil.which("cmake") or "cmake"
C_COMPILER_PATH = os.environ.get("CC") or shutil.which("gcc") or "gcc"
CXX_COMPILER_PATH = os.environ.get("CXX") or shutil.which("g++") or "g++"
ENGINE_SOURCE_DIR = "src/"
ENGINE_BUILD_CONFIG = get_host_engine_build_config(platform.machine())


def _sanitize_native_build_env(env):
    """Keep Rust native builds from accidentally linking against Linuxbrew libs.

    On older glibc systems, Homebrew-provided native libraries can require a newer
    libc than the host linker/runtime supports. When pkg-config resolves xz/bzip2
    from Linuxbrew, Cargo inherits those library search paths and link fails.
    """

    sanitized_env = env.copy()

    pkg_config = sanitized_env.get("PKG_CONFIG") or shutil.which("pkg-config")
    if pkg_config and "linuxbrew" in os.path.realpath(pkg_config).lower():
        system_pkg_config = "/usr/bin/pkg-config"
        if Path(system_pkg_config).exists():
            sanitized_env["PKG_CONFIG"] = system_pkg_config

    for key in ("PKG_CONFIG_PATH", "LIBRARY_PATH", "LD_LIBRARY_PATH"):
        value = sanitized_env.get(key)
        if not value:
            continue
        kept_paths = [
            path
            for path in value.split(os.pathsep)
            if path and "linuxbrew" not in os.path.realpath(path).lower()
        ]
        if kept_paths:
            sanitized_env[key] = os.pathsep.join(kept_paths)
        else:
            sanitized_env.pop(key, None)

    return sanitized_env


def _get_windows_python_sabi_library() -> Path:
    """Return the stable-ABI Python library path for Windows abi3 extensions."""
    candidate_roots = []
    for raw_root in (
        sys.base_prefix,
        sys.base_exec_prefix,
        sysconfig.get_config_var("installed_base"),
        sysconfig.get_config_var("base"),
    ):
        if not raw_root:
            continue
        candidate_root = Path(raw_root).resolve()
        if candidate_root not in candidate_roots:
            candidate_roots.append(candidate_root)

    candidate_paths = []
    for root in candidate_roots:
        candidate_paths.extend(
            [
                root / "libs" / "python3.lib",
                root / "python3.dll",
            ]
        )

    for candidate_path in candidate_paths:
        if candidate_path.exists():
            return candidate_path

    searched = ", ".join(str(path) for path in candidate_paths) or "<none>"
    raise RuntimeError(
        "Could not locate the Windows stable-ABI Python library for abi3 engine modules. "
        f"Searched: {searched}"
    )


class OpenVikingBuildExt(build_ext):
    """Build OpenViking runtime artifacts and Python native extensions."""

    def run(self):
        self.build_ov_cli_artifact()
        self.build_ragfs_python_artifact()
        self.cmake_executable = CMAKE_PATH

        for ext in self.extensions:
            self.build_extension(ext)

    def _copy_artifact(self, src, dst):
        """Copy a build artifact into the package tree and preserve executability."""
        print(f"Copying artifact from {src} to {dst}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(src), str(dst))
        if sys.platform != "win32":
            os.chmod(str(dst), 0o755)

    def _copy_artifacts_to_build_lib(self, target_binary=None, target_lib=None):
        """Copy built artifacts into build_lib so wheel packaging can include them."""
        if self.build_lib:
            build_pkg_dir = Path(self.build_lib) / "openviking"
            if target_binary and target_binary.exists():
                self._copy_artifact(target_binary, build_pkg_dir / "bin" / target_binary.name)
            if target_lib and target_lib.exists():
                self._copy_artifact(target_lib, build_pkg_dir / "lib" / target_lib.name)

    def _require_artifact(self, artifact_path, artifact_name, stage_name):
        """Abort the build immediately when a required artifact is missing."""
        if artifact_path.exists():
            return
        raise RuntimeError(
            f"{stage_name} did not produce required {artifact_name} at {artifact_path}"
        )

    def _run_stage_with_artifact_checks(
        self, stage_name, build_fn, required_artifacts, on_success=None
    ):
        """Run a build stage and always validate its required outputs on normal return."""
        build_fn()
        for artifact_path, artifact_name in required_artifacts:
            self._require_artifact(artifact_path, artifact_name, stage_name)
        if on_success:
            on_success()

    def _resolve_cargo_target_dir(self, cargo_project_dir, env):
        """Resolve the Cargo target directory for workspace and overridden builds."""
        configured_target_dir = env.get("CARGO_TARGET_DIR")
        if configured_target_dir:
            return Path(configured_target_dir).resolve()

        try:
            result = subprocess.run(
                ["cargo", "metadata", "--format-version", "1", "--no-deps"],
                cwd=str(cargo_project_dir),
                env=env,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            metadata = json.loads(result.stdout.decode("utf-8"))
            target_directory = metadata.get("target_directory")
            if target_directory:
                return Path(target_directory).resolve()
        except Exception as exc:
            print(f"[Warning] Failed to resolve Cargo target directory via metadata: {exc}")

        return cargo_project_dir.parents[1] / "target"

    def build_ov_cli_artifact(self):
        """Build or reuse the ov Rust CLI binary."""
        binary_name = "ov.exe" if sys.platform == "win32" else "ov"
        ov_cli_dir = Path("crates/ov_cli").resolve()
        ov_target_binary = Path("openviking/bin").resolve() / binary_name

        self._run_stage_with_artifact_checks(
            "ov CLI build",
            lambda: self._build_ov_cli_artifact_impl(ov_cli_dir, binary_name, ov_target_binary),
            [(ov_target_binary, binary_name)],
            on_success=lambda: self._copy_artifacts_to_build_lib(ov_target_binary, None),
        )

    def _build_ov_cli_artifact_impl(self, ov_cli_dir, binary_name, ov_target_binary):
        """Implement ov CLI building without final artifact checks."""

        prebuilt_dir = os.environ.get("OV_PREBUILT_BIN_DIR")
        if prebuilt_dir:
            src_bin = Path(prebuilt_dir).resolve() / binary_name
            if src_bin.exists():
                self._copy_artifact(src_bin, ov_target_binary)
                return

        if os.environ.get("OV_SKIP_OV_BUILD") == "1":
            if ov_target_binary.exists():
                print("[OK] Skipping ov CLI build, using existing binary")
                return
            print("[Warning] OV_SKIP_OV_BUILD=1 but binary is missing. Will try to build.")

        if ov_cli_dir.exists() and shutil.which("cargo"):
            print("Building ov CLI from source...")
            try:
                env = _sanitize_native_build_env(os.environ.copy())
                env["OPENVIKING_VERSION"] = resolve_openviking_version(
                    env=env, project_root=SETUP_DIR
                )
                build_args = ["cargo", "build", "--release"]
                target = env.get("CARGO_BUILD_TARGET")
                if target:
                    print(f"Cross-compiling with CARGO_BUILD_TARGET={target}")
                    build_args.extend(["--target", target])

                result = subprocess.run(
                    build_args,
                    cwd=str(ov_cli_dir),
                    env=env,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                if result.stdout:
                    print(f"Build stdout: {result.stdout.decode('utf-8', errors='replace')}")
                if result.stderr:
                    print(f"Build stderr: {result.stderr.decode('utf-8', errors='replace')}")

                cargo_target_dir = self._resolve_cargo_target_dir(ov_cli_dir, env)
                if target:
                    built_bin = cargo_target_dir / target / "release" / binary_name
                else:
                    built_bin = cargo_target_dir / "release" / binary_name

                self._require_artifact(built_bin, binary_name, "ov CLI build")
                self._copy_artifact(built_bin, ov_target_binary)
                print("[OK] ov CLI built successfully from source")
            except Exception as exc:
                error_msg = f"Failed to build ov CLI from source: {exc}"
                if isinstance(exc, subprocess.CalledProcessError):
                    if exc.stdout:
                        error_msg += (
                            f"\nBuild stdout:\n{exc.stdout.decode('utf-8', errors='replace')}"
                        )
                    if exc.stderr:
                        error_msg += (
                            f"\nBuild stderr:\n{exc.stderr.decode('utf-8', errors='replace')}"
                        )
                print(f"[Error] {error_msg}")
                raise RuntimeError(error_msg)
        else:
            if ov_target_binary.exists():
                print("[Info] ov CLI binary already exists locally. Skipping source build.")
            elif not ov_cli_dir.exists():
                print(f"[Warning] ov CLI source directory not found at {ov_cli_dir}")
            else:
                print("[Warning] Cargo not found. Cannot build ov CLI from source.")

    def build_ragfs_python_artifact(self):
        """Build ragfs-python (Rust RAGFS binding) via maturin and copy the native
        extension into ``openviking/lib/`` so it ships inside the openviking wheel.
        """
        require_ragfs_artifact = self._should_require_ragfs_artifact()
        ragfs_python_dir = Path("crates/ragfs-python").resolve()
        ragfs_lib_dir = Path("openviking/lib").resolve()

        if not ragfs_python_dir.exists():
            message = "ragfs-python source directory not found."
            if require_ragfs_artifact:
                raise RuntimeError(message)
            print(f"[Info] {message} Skipping.")
            return

        if os.environ.get("OV_SKIP_RAGFS_BUILD") == "1":
            message = "Skipping ragfs-python build (OV_SKIP_RAGFS_BUILD=1)"
            if require_ragfs_artifact:
                raise RuntimeError(f"{message} is incompatible with required wheel artifacts.")
            print(f"[OK] {message}")
            return

        if importlib.util.find_spec("maturin") is None:
            message = (
                "maturin not found. ragfs-python (Rust binding) will not be built.\n"
                "       Install maturin to enable: pip install maturin"
            )
            if require_ragfs_artifact:
                raise RuntimeError(message)
            print(f"[SKIP] {message}")
            return

        import tempfile
        import zipfile

        with tempfile.TemporaryDirectory() as tmpdir:
            try:
                print("Building ragfs-python (Rust RAGFS binding) via maturin...")
                env = _sanitize_native_build_env(os.environ.copy())
                build_args = [
                    sys.executable,
                    "-m",
                    "maturin",
                    "build",
                    "--release",
                    "--out",
                    tmpdir,
                ]
                # Respect CARGO_BUILD_TARGET for cross-compilation
                target = env.get("CARGO_BUILD_TARGET")
                if target:
                    build_args.extend(["--target", target])

                result = subprocess.run(
                    build_args,
                    cwd=str(ragfs_python_dir),
                    env=env,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                if result.stdout:
                    print(result.stdout.decode("utf-8", errors="replace"))
                if result.stderr:
                    print(result.stderr.decode("utf-8", errors="replace"))

                # Extract the stable-ABI native extension from the built wheel.
                whl_files = list(Path(tmpdir).glob("ragfs_python-*.whl"))
                if not whl_files:
                    message = "maturin produced no wheel for ragfs-python."
                    if require_ragfs_artifact:
                        raise RuntimeError(message)
                    print(f"[Warning] {message}")
                    return

                ragfs_lib_dir.mkdir(parents=True, exist_ok=True)
                for stale_artifact in ragfs_lib_dir.glob("ragfs_python*.so"):
                    stale_artifact.unlink()
                for stale_artifact in ragfs_lib_dir.glob("ragfs_python*.pyd"):
                    stale_artifact.unlink()
                for stale_artifact in ragfs_lib_dir.glob("ragfs_python*.dylib"):
                    stale_artifact.unlink()

                extracted = False
                with zipfile.ZipFile(str(whl_files[0])) as zf:
                    for name in zf.namelist():
                        basename = Path(name).name
                        if basename.startswith("ragfs_python.abi3.") and (
                            basename.endswith(".so") or basename.endswith(".pyd")
                        ):
                            target_path = ragfs_lib_dir / basename
                            with zf.open(name) as src, open(target_path, "wb") as dst:
                                dst.write(src.read())
                            if sys.platform != "win32":
                                os.chmod(str(target_path), 0o755)
                            print(f"[OK] ragfs-python: extracted {basename} -> {target_path}")
                            extracted = True
                            break

                if not extracted:
                    message = "Could not find ragfs_python abi3 .so/.pyd in built wheel."
                    if require_ragfs_artifact:
                        raise RuntimeError(message)
                    print(f"[Warning] {message}")
                else:
                    self._copy_artifacts_to_build_lib(target_lib=target_path)

            except Exception as exc:
                error_detail = ""
                if isinstance(exc, subprocess.CalledProcessError):
                    if exc.stdout:
                        error_detail += exc.stdout.decode("utf-8", errors="replace")
                    if exc.stderr:
                        error_detail += exc.stderr.decode("utf-8", errors="replace")
                if require_ragfs_artifact:
                    error_message = f"Failed to build ragfs-python: {exc}"
                    if error_detail:
                        error_message += f"\n{error_detail}"
                    raise RuntimeError(error_message) from exc
                print(f"[Warning] Failed to build ragfs-python: {exc}")
                if error_detail:
                    print(error_detail)

    def _should_require_ragfs_artifact(self) -> bool:
        """Fail wheel builds closed when ragfs-python cannot be bundled."""
        required = os.environ.get("OV_REQUIRE_RAGFS_BUILD")
        if required is not None:
            return required == "1"
        return "bdist_wheel" in sys.argv

    def build_extension(self, ext):
        """Build a single Python native extension artifact using CMake."""
        if getattr(self, "_engine_extensions_built", False):
            return

        ext_fullpath = Path(self.get_ext_fullpath(ext.name))
        ext_dir = ext_fullpath.parent.resolve()
        build_dir = Path(self.build_temp) / "cmake_build"
        build_dir.mkdir(parents=True, exist_ok=True)
        self._clean_stale_engine_artifacts(ext_dir)

        self._run_stage_with_artifact_checks(
            "CMake build",
            lambda: self._build_extension_impl(ext_fullpath, ext_dir, build_dir),
            [(ext_fullpath, f"native extension '{ext.name}'")],
        )
        self._engine_extensions_built = True

    def _clean_stale_engine_artifacts(self, ext_dir: Path):
        """Remove stale non-abi3 engine binaries from wheel build output directories."""
        source_engine_dir = (SETUP_DIR / "openviking" / "storage" / "vectordb" / "engine").resolve()
        if ext_dir == source_engine_dir:
            return

        for pattern in ("*.so", "*.pyd"):
            for artifact in ext_dir.glob(pattern):
                artifact.unlink()

    def _build_extension_impl(self, ext_fullpath, ext_dir, build_dir):
        """Invoke CMake to build the Python native extension."""
        ext_basename = ext_fullpath.stem.split(".")[0]
        built_filename = Path(self.get_ext_filename(self.extensions[0].name)).name
        py_ext_suffix = built_filename.removeprefix(ext_basename)
        if not py_ext_suffix:
            py_ext_suffix = sysconfig.get_config_var("EXT_SUFFIX") or ext_fullpath.suffix

        cmake_args = [
            f"-S{Path(ENGINE_SOURCE_DIR).resolve()}",
            f"-B{build_dir}",
            "-DCMAKE_BUILD_TYPE=Release",
            f"-DOV_PY_OUTPUT_DIR={ext_dir}",
            f"-DOV_PY_EXT_SUFFIX={py_ext_suffix}",
            f"-DOV_X86_BUILD_VARIANTS={';'.join(ENGINE_BUILD_CONFIG.cmake_variants)}",
            "-DCMAKE_VERBOSE_MAKEFILE=ON",
            "-DCMAKE_INSTALL_RPATH=$ORIGIN",
            f"-DPython3_EXECUTABLE={sys.executable}",
            f"-DPython3_INCLUDE_DIRS={sysconfig.get_path('include')}",
            f"-DPython3_LIBRARIES={sysconfig.get_config_vars().get('LIBRARY')}",
            f"-DCMAKE_C_COMPILER={C_COMPILER_PATH}",
            f"-DCMAKE_CXX_COMPILER={CXX_COMPILER_PATH}",
        ]

        if sys.platform == "darwin":
            cmake_args.append("-DCMAKE_OSX_DEPLOYMENT_TARGET=10.15")
            target_arch = os.environ.get("CMAKE_OSX_ARCHITECTURES")
            if target_arch:
                cmake_args.append(f"-DCMAKE_OSX_ARCHITECTURES={target_arch}")
        elif sys.platform == "win32":
            windows_python_sabi_library = _get_windows_python_sabi_library()
            cmake_args.append(f"-DOV_PYTHON_SABI_LIBRARY={windows_python_sabi_library}")
            cmake_args.extend(["-G", "MinGW Makefiles"])

        self.spawn([self.cmake_executable] + cmake_args)

        build_args = ["--build", str(build_dir), "--config", "Release", f"-j{os.cpu_count() or 4}"]
        self.spawn([self.cmake_executable] + build_args)


if bdist_wheel is not None:

    class OpenVikingBdistWheel(bdist_wheel):
        def finalize_options(self):
            super().finalize_options()
            self.py_limited_api = "cp310"
else:
    OpenVikingBdistWheel = None


cmdclass = {
    "build_ext": OpenVikingBuildExt,
}
if OpenVikingBdistWheel is not None:
    cmdclass["bdist_wheel"] = OpenVikingBdistWheel


setup(
    ext_modules=[
        Extension(
            name=ENGINE_BUILD_CONFIG.primary_extension,
            sources=[],
            py_limited_api=True,
        )
    ],
    cmdclass=cmdclass,
    package_data={
        "openviking": [
            "lib/ragfs_python*.so",
            "lib/ragfs_python*.pyd",
            "bin/ov",
            "bin/ov.exe",
            "console/static/**/*",
            "storage/vectordb/engine/*.abi3.so",
            "storage/vectordb/engine/*.pyd",
        ],
    },
    include_package_data=True,
)
```

## Follow-up Evidence: Targeted Implementation Anchors

Snapshot 之后又在不克隆仓库的前提下，通过 GitHub contents API 定向读取了下列文件，用于把维护页从目录骨架补成机制地图：

- `openviking/server/app.py`: FastAPI server factory。关键锚点包括 `OpenVikingService` 初始化、`APIKeyManager`、`AuthMode`、metrics/tracing/logging 初始化、MCP lifespan，以及大量 router 注册：`filesystem_router`、`resources_router`、`search_router`、`sessions_router`、`tasks_router`、`admin_router`、`bot_router`、`webdav_router` 等。
- `openviking/server/bootstrap.py`: `openviking-server` 启动入口。读取 `ov.conf`，初始化 config singleton，检测/启动 Ollama，启动 Uvicorn；当启用 bot 时，会先检查 bot gateway 端口是否已有旧进程绑定，再启动 `vikingbot gateway` 子进程并管理日志与关闭。
- `openviking/server/config.py`: server 配置与安全门。`auth_mode` 支持 `dev`、`api_key`、`trusted`，其中 dev/trusted 在非 localhost 场景需要 API key 或直接拒绝启动；配置还包含 metrics、OTel、API key hashing、file-level encryption 的开关。
- `openviking/storage/__init__.py`: storage 层使用 lazy import，避免 native C++ engine extension 在 import 阶段与 storage package 初始化产生 import-lock deadlock。
- `openviking/storage/vectordb/engine/__init__.py`: native vector engine loader。根据平台、CPU capability 与 `OV_ENGINE_VARIANT` 选择 `x86_sse3`、`x86_avx2`、`x86_avx512` 或 `native` 后端；缺失时用 missing symbol proxy 延迟报错。
- `openviking_cli/rust_cli.py`: Python package 暴露的 `ov/openviking` 命令只是薄包装器。优先处理 Python-native 子命令，再查找开发环境、wheel 内置、PATH 中的 Rust `ov` 二进制，并在 Unix 上用 `execv` 替换当前进程。
- `crates/ov_cli/src/main.rs`: Rust CLI 主入口。命令按标签分为 Data、Interactive、Status、Admin、Experimental 等，覆盖 `add-resource`、`add-skill`、`ls`、`tree`、`read`、`abstract`、`overview`、`find`、`search`、`grep`、`chat`、`admin`、`observer` 等操作；CLI context 负责加载 `ovcli.conf`，并把 account/user/agent_id 与 root/user API key 注入 HTTP client。
- `openviking_cli/utils/ollama.py`: Ollama 运行时保障。设计原则是“ensure running, never stop”，用于 setup wizard 与 server bootstrap；对本地 Ollama 可启动和健康检查，对远端 Ollama 只探测不本地启动。
- `docs/en/concepts/08-session.md`: session 生命周期为 create -> interact -> commit。`commit()` 分两阶段：同步归档 messages 并返回 task_id，后台生成 `.abstract.md`、`.overview.md`、提取长期 memory，最后写 `.done` marker。memory 分为 user 的 profile/preferences/entities/events 与 agent 的 cases/patterns/tools/skills。
- `docs/en/guides/01-configuration.md`: 配置体系。`ov.conf` 同时承载 storage、embedding、vlm、server、bot 等配置；`ovcli.conf` 承载远端 server URL、API key、account/user/agent_id 与上传过滤规则。配置文档还显示 embedding retry、circuit breaker、provider 多样性等运行护栏。
- `bot/README.md`: Vikingbot 是基于 Nanobot 的 OpenViking bot 层，提供本地/远端模式、7 个 OpenViking agent tools、L0/L1/L2 三层内容访问、session 自动提交、多个 chat channel、MCP server 接入与 sandbox/FUSE/OpenCode 等可选能力。

这些锚点支持的主要机制判断：

- OpenViking 的产品核心不是“向量库”，而是把 resources、user memory、agent memory、skills、sessions 统一放入 `viking://` 虚拟文件系统，并让 agent 通过 `ls/tree/read/find/grep` 等文件式操作访问 context。
- L0/L1/L2 分层不是单纯文档摘要，而是写入和 session commit 后的存储约定：`.abstract.md` 用于快速判断，`.overview.md` 用于计划层理解，L2 原文按需读取。
- server 侧是一个长期服务化 context runtime，暴露 filesystem/resource/search/session/task/admin/bot 等 API，并用 auth mode、API key、metrics/tracing、task tracker 和 MCP lifespan 组成运行护栏。
- CLI 层刻意拆成 Python package entrypoint 与 Rust `ov` 二进制。Python 层负责发行兼容和少量 native 子命令，交互与高频命令走 Rust，以降低启动开销并保留独立 CLI 发布能力。
- bot 层把 OpenViking 变成 agent 可用的工作面：channel 消息、OpenViking tools、自动 memory commit、MCP tools 与 sandbox 组合在一起，但也扩大了权限、身份隔离和外部工具治理的复杂度。

## Follow-up Evidence: MCP Design

为回答 OpenViking 的 MCP 设计，又通过 GitHub contents API 定向读取了：

- `openviking/server/mcp_endpoint.py`
- `openviking/server/app.py`
- `openviking/server/auth.py`
- `openviking/server/identity.py`
- `tests/server/test_mcp_endpoint.py`
- `docs/en/guides/06-mcp-integration.md`
- `docs/zh/guides/06-mcp-integration.md`
- `bot/vikingbot/agent/tools/mcp.py`
- `examples/claude-code-memory-plugin/.mcp.json`
- `examples/codex-memory-plugin/.mcp.json`

关键发现：

- OpenViking server 内置 MCP endpoint。文档明确说端点位于 `http://<server>:1933/mcp`，与 REST API 同进程、同端口，通过 streamable HTTP 接入 MCP client。
- `openviking/server/app.py` 在 FastAPI lifespan 中启动 `mcp_lifespan()`，保证 MCP session manager 在请求到达前初始化；随后用 `app.routes.append(Route("/mcp", endpoint=create_mcp_app(), methods=["GET", "POST", "DELETE"]))` 挂载 `/mcp`。
- `openviking/server/mcp_endpoint.py` 使用 `mcp.server.fastmcp.FastMCP("openviking")` 定义 MCP server，并通过 `mcp.streamable_http_app()` 创建 ASGI app。
- MCP endpoint 通过 `_IdentityASGIMiddleware` 复用 `openviking.server.auth.resolve_identity`。它读取 `X-Api-Key`、`Authorization: Bearer ...`、`X-OpenViking-Account`、`X-OpenViking-User`、`X-OpenViking-Agent`，再写入 contextvar `_mcp_ctx`，供 MCP tool 内部取 `RequestContext`。
- MCP endpoint 的鉴权策略与 REST API 一致：dev mode 本地可免认证；api_key mode 使用 API key；trusted mode 信任身份 header，但在非 localhost 或配置 root key 的场景有额外约束。
- MCP tool 不是独立实现业务逻辑，而是 thin adapter 到 `OpenVikingService`：
  - `search` -> `service.search.find(...)`
  - `read` -> `service.fs.read(...)`
  - `list` -> `service.fs.ls(...)`
  - `store` -> `service.sessions.get(..., auto_create=True)` + `service.sessions.commit_async(...)`
  - `add_resource` -> `service.resources.add_resource(...)`
  - `grep` -> `service.fs.grep(...)`
  - `glob` -> `service.fs.glob(...)`
  - `forget` -> `service.fs.rm(...)`
  - `health` -> `get_service()` / `service.viking_fs`
- 文档列出 9 个 MCP tools：`search`、`read`、`list`、`store`、`add_resource`、`grep`、`glob`、`forget`、`health`。`app.py` 的注释还写着“5 tools”，应是旧注释。
- `bot/vikingbot/agent/tools/mcp.py` 是相反方向：Vikingbot 作为 MCP client 连接第三方 MCP servers，然后把外部 MCP tools 包装成 vikingbot native tools，命名为 `mcp_<server>_<tool>`。也就是说 OpenViking 同时支持“作为 MCP server 被外部 agent 调用”和“Vikingbot 作为 MCP client 消费外部 tools”。
- `openviking/core/mcp_converter.py` 能把 MCP tool definition 转成 OpenViking skill markdown。这说明 MCP tools 还可被沉淀成 skill 形态，而不只是运行时调用。
- `tests/server/test_mcp_endpoint.py` 直接测试 MCP tool 函数本身，而不是跑完整 MCP 协议；它通过设置 `_mcp_ctx` 和 `set_service(service)` 验证 search/read/store/forget/grep/glob/health 等工具行为。测试文件中 `from openviking.server.mcp_endpoint import list_dir as list_tool` 与当前 `mcp_endpoint.py` 中 `@mcp.tool(name="list") async def ls(...)` 存在命名漂移迹象，需后续确认实际 CI 是否覆盖到这里。
