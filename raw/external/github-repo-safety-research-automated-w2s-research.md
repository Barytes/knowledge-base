---
title: "GitHub repo snapshot: safety-research/automated-w2s-research"
source: "https://github.com/safety-research/automated-w2s-research"
author:
published:
created: 2026-04-21
description: "Compact GitHub repository evidence snapshot for repo-map-ingest."
tags:
  - "github"
  - "repo-snapshot"
---

# GitHub Repo Snapshot: `safety-research/automated-w2s-research`

## Observation Scope

- Repository: `safety-research/automated-w2s-research`
- URL: https://github.com/safety-research/automated-w2s-research
- Requested topic: 自动化 alignment research harness 与 weak-to-strong 监督
- Observed ref: `main`
- Latest resolved commit: `79a0562fa1a2c246048ed7c009f3684907987b05`
- Commit date: `2026-04-13T20:33:23Z`
- Snapshot date (UTC): `2026-04-21`

## Repository Metadata

- Description: (none)
- Default branch: `main`
- Language: `Python`
- Stars: `144`
- Forks: `32`
- Open issues: `0`

## Top-Level Tree

### Directories

- `.claude`
- `.github`
- `scripts`
- `w2s_research`

### Files

- `.dockerignore`
- `.gitignore`
- `.gitmodules`
- `Dockerfile`
- `Idea.md`
- `README.md`
- `cache_results.tar.gz`
- `entrypoint.sh`
- `labeled_data.tar.gz`
- `pyproject.toml`
- `run.py`
- `run.sh`
- `uv.lock`

## Selected Evidence Anchors

- `.github/workflows/claude-code-review.yml`
- `.github/workflows/claude.yml`
- `.github/workflows/docker-image.yml`
- `Dockerfile`
- `README.md`
- `pyproject.toml`

## Captured Files

### `.github/workflows/claude-code-review.yml`

- Source path: `.github/workflows/claude-code-review.yml`
- Truncated: `no`

```yaml
name: Claude Code Review

on:
  pull_request:
    types: [opened, synchronize]
    # Optional: Only run on specific file changes
    # paths:
    #   - "src/**/*.ts"
    #   - "src/**/*.tsx"
    #   - "src/**/*.js"
    #   - "src/**/*.jsx"

jobs:
  claude-review:
    # Optional: Filter by PR author
    # if: |
    #   github.event.pull_request.user.login == 'external-contributor' ||
    #   github.event.pull_request.user.login == 'new-developer' ||
    #   github.event.pull_request.author_association == 'FIRST_TIME_CONTRIBUTOR'

    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: read
      issues: read
      id-token: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - name: Run Claude Code Review
        id: claude-review
        uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            REPO: ${{ github.repository }}
            PR NUMBER: ${{ github.event.pull_request.number }}

            Please review this pull request and provide feedback on:
            - Code quality and best practices
            - Potential bugs or issues
            - Performance considerations
            - Security concerns
            - Test coverage

            Use the repository's CLAUDE.md for guidance on style and conventions. Be constructive and helpful in your feedback.

            Use `gh pr comment` with your Bash tool to leave your review as a comment on the PR.

          # See https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md
          # or https://code.claude.com/docs/en/cli-reference for available options
          claude_args: '--allowed-tools "Bash(gh issue view:*),Bash(gh search:*),Bash(gh issue list:*),Bash(gh pr comment:*),Bash(gh pr diff:*),Bash(gh pr view:*),Bash(gh pr list:*)"'
```

### `.github/workflows/claude.yml`

- Source path: `.github/workflows/claude.yml`
- Truncated: `no`

```yaml
name: Claude Code

on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
  issues:
    types: [opened, assigned]
  pull_request_review:
    types: [submitted]

jobs:
  claude:
    if: |
      (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude')) ||
      (github.event_name == 'pull_request_review' && contains(github.event.review.body, '@claude')) ||
      (github.event_name == 'issues' && (contains(github.event.issue.body, '@claude') || contains(github.event.issue.title, '@claude')))
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: read
      issues: read
      id-token: write
      actions: read # Required for Claude to read CI results on PRs
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - name: Run Claude Code
        id: claude
        uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

          # This is an optional setting that allows Claude to read CI results on PRs
          additional_permissions: |
            actions: read

          # Optional: Give a custom prompt to Claude. If this is not specified, Claude will perform the instructions specified in the comment that tagged it.
          # prompt: 'Update the pull request description to include a summary of changes.'

          # Optional: Add claude_args to customize behavior and configuration
          # See https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md
          # or https://code.claude.com/docs/en/cli-reference for available options
          # claude_args: '--allowed-tools Bash(gh pr:*)'
```

### `.github/workflows/docker-image.yml`

- Source path: `.github/workflows/docker-image.yml`
- Truncated: `no`

```yaml
name: Docker Build & Push (w2s-research)

on:
  push:
    branches: [ "main" ]

jobs:
          
  build-and-push:
    runs-on: ubuntu-latest

    env:
      IMAGE_NAME: w2s-research
      IMAGE_TAG: latest

    steps:
      # Step 0: Checkout repo with submodules (verl is a submodule)
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          submodules: recursive

      # Step 1: Set up Buildx (needed for --platform + caching)
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
        
      - name: Free disk space
        run: |
          echo "=== Disk usage BEFORE cleanup ==="
          df -h /
          sudo rm -rf \
            /opt/ghc \
            /opt/google/chrome \
            /opt/microsoft/msedge \
            /opt/microsoft/powershell \
            /opt/pipx \
            /opt/hostedtoolcache \
            /usr/lib/mono \
            /usr/local/julia* \
            /usr/local/lib/android \
            /usr/local/lib/node_modules \
            /usr/local/share/chromium \
            /usr/local/share/powershell \
            /usr/share/dotnet \
            /usr/share/swift
          echo "=== Disk usage AFTER cleanup ==="
          df -h /

      # Step 2: Log in to Docker Hub (non-interactive)
      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      # Step 3: Compute date tag (YYYYMMDD)
      - name: Compute date tag
        run: echo "DATE_TAG=$(date +%Y%m%d)" >> $GITHUB_ENV

      # Step 4: Build and push image
      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: Dockerfile
          platforms: linux/amd64
          push: true
          tags: |
            ${{ secrets.DOCKERHUB_USERNAME }}/${{ env.IMAGE_NAME }}:${{ env.IMAGE_TAG }}
            ${{ secrets.DOCKERHUB_USERNAME }}/${{ env.IMAGE_NAME }}:${{ env.DATE_TAG }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      # Step 5: Print summary (nice UX)
      - name: Build summary
        run: |
          echo "=========================================="
          echo "Build and Push Complete ✓"
          echo "=========================================="
          echo ""
          echo "Images pushed:"
          echo "  • ${{ secrets.DOCKERHUB_USERNAME }}/${{ env.IMAGE_NAME }}:${{ env.IMAGE_TAG }}"
          echo "  • ${{ secrets.DOCKERHUB_USERNAME }}/${{ env.IMAGE_NAME }}:${{ env.DATE_TAG }}"
```

### `Dockerfile`

- Source path: `Dockerfile`
- Truncated: `no`

```
# Use Runpod's official PyTorch base image
# CUDA 12.8.1, PyTorch 2.8.0, Ubuntu 24.04
FROM runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404

# Install system dependencies first
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        openssh-server \
        git \
        curl \
    && mkdir -p /var/run/sshd && \
    rm -rf /var/lib/apt/lists/*

# Install uv (fast Python package manager) to system location
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv /root/.local/bin/uv /usr/local/bin/uv && \
    chmod +x /usr/local/bin/uv

# Create non-root user (no sudo access required - Claude Code CLI with bypassPermissions mode
# requires non-root user without sudo privileges for security)
RUN useradd -m -s /bin/bash ubuntu-cmd && \
    mkdir -p /home/ubuntu-cmd/.ssh && \
    chmod 700 /home/ubuntu-cmd/.ssh

# Install Claude Code CLI as ubuntu-cmd user (recommended method)
# Reference: https://code.claude.com/docs/en/setup
# Installing as ubuntu-cmd ensures marketplace is properly initialized for that user
RUN su ubuntu-cmd -c "curl -fsSL https://claude.ai/install.sh | bash" && \
    # Verify installation
    su ubuntu-cmd -c "/home/ubuntu-cmd/.local/bin/claude --version" && \
    # Make claude available in PATH by creating symlink (pointing to ubuntu-cmd's installation)
    ln -s /home/ubuntu-cmd/.local/bin/claude /usr/local/bin/claude

# Update PATH to include system-wide binaries (needed for ubuntu-cmd user)
ENV PATH="/usr/local/bin:$PATH"

# Install ralph-loop plugin for infinite loop iteration
# This plugin enables the /ralph-loop:ralph-loop command used in autonomous baseline
# Note: Marketplace is not auto-configured in Docker build, so we add it explicitly
RUN echo "=== Claude Code version ===" && \
    su ubuntu-cmd -c "claude --version" && \
    echo "=== Adding official marketplace ===" && \
    su ubuntu-cmd -c "claude plugin marketplace add https://github.com/anthropics/claude-plugins-official" && \
    echo "=== Available marketplaces ===" && \
    su ubuntu-cmd -c "claude plugin marketplace list" && \
    echo "=== Installing ralph-loop plugin ===" && \
    su ubuntu-cmd -c "claude plugin install ralph-loop" && \
    echo "=== Installed plugins ===" && \
    su ubuntu-cmd -c "claude plugin list" && \
    echo "✓ ralph-loop plugin installed for ubuntu-cmd user"

# Copy project files for better caching
# Build code in /opt/automated-w2s-research (will be copied to /workspace/automated-w2s-research at runtime)
WORKDIR /opt/automated-w2s-research
COPY pyproject.toml uv.lock CLAUDE.md README.md ./

# Install Python dependencies from lock file (system-wide for Docker)
# Export lock file to requirements format and install system-wide
# Note: --break-system-packages is needed to bypass PEP 668 protection in Ubuntu 24.04
# Note: --no-cache prevents disk space exhaustion from large packages like sgl-kernel
RUN uv export --all-groups --format requirements-txt --no-hashes -o /tmp/requirements.txt && \
    uv pip install --system --break-system-packages --no-cache -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# Configure SSH (allow both root and ubuntu-cmd)
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication no" >> /etc/ssh/sshd_config && \
    echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config && \
    echo "AllowUsers root ubuntu-cmd" >> /etc/ssh/sshd_config

# Copy the entire project to /opt/automated-w2s-research (temporary build location, copied to /workspace at runtime)
COPY . .

# Install the project (and verl if present) in editable mode (system-wide)
RUN uv pip install -e . --system --break-system-packages --no-cache && \
    if [ -f verl/pyproject.toml ] || [ -f verl/setup.py ]; then \
        uv pip install --no-deps -e verl --system --break-system-packages --no-cache; \
    fi

# Grant ubuntu-cmd write access to workspace (needed for local Docker mode)
RUN chown -R ubuntu-cmd:ubuntu-cmd /opt/automated-w2s-research

# Copy and set up entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set environment variables
ENV PYTHONPATH=/opt/automated-w2s-research
ENV VLLM_ALLOW_LONG_MAX_MODEL_LEN=1

# Expose SSH port
EXPOSE 22
EXPOSE 8000

# Set entrypoint and default command
# Default behavior: switch to ubuntu-cmd user and sleep (for interactive use)
# Override via dockerStartCmd in deployment script (e.g., w2s_research.infrastructure.runpod)
ENTRYPOINT ["/entrypoint.sh"]
CMD ["sleep", "infinity"]
```

### `README.md`

- Source path: `README.md`
- Truncated: `no`

```md
# Automated Weak-to-Strong Research

This project releases a sandbox for automated weak-to-strong research, together with datasets, baselines, and a baseline automated researcher.

**Weak-to-strong generalization** addresses superhuman AI alignment: how do we align AI systems smarter than us when we can't reliably evaluate their outputs? The setup trains a weak model on labeled data, uses it to pseudo-label unlabeled data, then trains a strong model based on those labels. We measure how much the strong model recovers ground truth performance via **Performance Gap Recovery (PGR)**:

```
PGR = (transfer_acc - weak_acc) / (strong_acc - weak_acc)
```

PGR=0 means the strong model is only as good as the weak model. PGR=1 means full recovery.

## Environment Setup

### 1. Install dependencies

```bash
uv sync
```

This installs all dependencies: ML training (PyTorch, Transformers, Unsloth, vLLM), agent SDK (Anthropic, Claude Agent SDK), server (Flask), and cloud (boto3, RunPod).

### 2. Download datasets

We provide three datasets: **chat**, **math**, and **code**.

Each dataset has three files:
- `test.jsonl` — test set for evaluating both in-distribution and out-of-distribution performance
- `train_label.jsonl` — labeled data for training the weak teacher model
- `train_unlabel.jsonl` — unlabeled data for training the strong student

The datasets are distributed as a tar.gz archive. Unpack and prepare:

```bash
tar xzf labeled_data.tar.gz
python scripts/prepare_data.py
```

`prepare_data.py` generates `data/` from `labeled_data/` by stripping labels and metadata. This is what the automated researcher sees — ground truth is held server-side and accessed via the evaluation API.

### 3. Run baselines

Pre-computed results for all baselines are provided as an archive. Unpack first:

```bash
tar xzf cache_results.tar.gz
```

You can also rerun baselines on customized datasets and models:

```bash
# Run baselines across 5 seeds in parallel (auto-distributes across available GPUs)
python run.py --idea vanilla_w2s --seeds 42,43,44,45,46 --data-dir data/chat
```

**Available baselines:**
| Idea | Description |
|------|-------------|
| `vanilla_w2s` | Train strong model on hard weak labels (standard W2S baseline) |
| `train_only_on_confident_labels` | Filter weak labels by confidence before training |
| `critic` | Use strong model critiques to improve weak labels |
| `ue_zeroshot` | Unsupervised elicitation — zero-shot variant |
| `ue_fewshot` | Unsupervised elicitation — few-shot variant with in-context learning (we are not using this version in main experiments since Qwen3-4B-Base barely can do in-context learning on our three testbeds)|

### 4. Create your own idea

```bash
cp -r w2s_research/ideas/TEMPLATE w2s_research/ideas/my_idea
# Edit w2s_research/ideas/my_idea/run.py — implement your approach
python run.py --idea my_idea --seed 42
```

Each idea's `run.py` receives a `RunConfig` and returns metrics. The template loads pre-cached weak model artifacts so you only implement your novel contribution.

see our idea list in `Idea.md`


## Automated Researcher

The automated researcher is a Claude-powered agent that iteratively proposes ideas, implements them, trains models, evaluates via the server API, and shares findings. 

There are three execution modes, from simplest to most isolated:

### 1. Start the dashboard (required for all modes)

```bash
python run.py server --port 8000
```

This starts a Flask server that provides:
- **Experiment management** — queue, monitor, and manage agent runs
- **Evaluation API** — agents submit predictions and get PGR back (ground truth stays server-side)
- **Leaderboard** — compare results across agents and ideas
- **Findings forum** — agents share and read research findings from other workers

Open `http://localhost:8000` to access the web dashboard. From the dashboard, you can create research directions, select execution mode (local / Docker / RunPod), assign GPUs, and launch experiments.

### 2. Execution modes

All three modes require `ANTHROPIC_API_KEY` to be set before starting the server.

#### Mode A: Local (subprocess)

The simplest mode. A single agent runs as a subprocess on the same machine, with direct access to GPUs and the filesystem. Best for quick debugging. Note that in this mode, AAR would be able to find `labeled_data`, so the result might not be legit.

No Docker, no persistent S3 storage, no parallel AARs that share findings and codebases to each other.

#### Mode B: Local Docker

Runs a singel agent inside a Docker container with GPU passthrough. This provides **isolation**: the container only sees `data/` (no labels) and `cache_results/` as read-only mounts, so the agent cannot cheat by reading ground truth. Uses the same Docker image as RunPod mode.

**Setup:**
```bash
# Build the Docker image
./scripts/docker-build-push.sh  # builds with tag 'latest'

# Start server with Docker mode enabled
export ANTHROPIC_API_KEY=...
export DOCKER_LOCAL_MODE=true
export DOCKER_LOCAL_IMAGE=w2s-research  # default image name
python run.py server --port 8000
```

Then launch experiments from the web dashboard, selecting "Docker (local GPUs)" as the execution mode.

#### Mode C: RunPod (cloud)

Deploys parallel agents to RunPod cloud GPUs. The server orchestrates deployment, monitors pod status, and collects results via S3. Supports multiple concurrent pods with automatic retry on capacity errors.

**Setup:**
```bash
export ANTHROPIC_API_KEY=...
export RUNPOD_API_KEY=...
export RUNPOD_TEMPLATE_ID=...  # Create a template on RunPod using the Docker image
export DEPLOY_TO_RUNPOD=true

# S3 for artifact storage (datasets, results, findings)
export S3_BUCKET=...
export S3_ENDPOINT_URL=...
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...

# Optional
export WANDB_API_KEY=...               # For experiment tracking
export MAX_CONCURRENT_PODS=1           # Max parallel pods (default: 1)
export RUNPOD_GPU_TYPE="NVIDIA H200"   # GPU type (default: NVIDIA H200)

python run.py server --port 8000
```

Then launch experiments from the web dashboard, selecting "RunPod (cloud)" as the execution mode.

In RunPod mode:
- The idea, dataset, and cached baselines are uploaded to S3
- A pod is deployed with the Docker image, which downloads everything from S3
- The agent runs autonomously, uploading results and logs to S3
- The server monitors pod status and collects results on completion
- Findings are synced between workers for cross-pollination

## Project Structure

```
run.py                              # Unified launcher
w2s_research/
├── core/                           # Shared training library
│   ├── train.py                    #   Training loop (Unsloth + LoRA)
│   ├── eval.py                     #   Evaluation and metrics
│   ├── data.py                     #   Data loading (multiple-choice format)
│   ├── config.py                   #   RunConfig and CLI argument parser
│   └── inference.py                #   Batch prediction utilities
├── ideas/                          # Experiment implementations
│   ├── TEMPLATE/                   #   Template for new ideas
│   ├── vanilla_w2s/                
│   ├── critic/                     
│   ├── ue_zeroshot/                
│   ├── ue_fewshot/                 
│   └── train_only_on_confident_labels/
├── research_loop/                  # Autonomous agent
│   ├── agent.py                    #   Agent loop + Claude SDK wrapper
│   ├── prompt.jinja2               #   Agent system prompt
│   └── tools/                      #   MCP tools (evaluate, share, leaderboard)
├── web_ui/                         # Dashboard
│   └── backend/                    #   Flask API + experiment worker
└── infrastructure/                 # Deployment
    ├── runpod.py                   #   RunPod pod management
    ├── s3_utils.py                 #   S3 storage utilities
    └── execute_autonomous.py       #   Worker pod entrypoint
```

## License

MIT
```

### `pyproject.toml`

- Source path: `pyproject.toml`
- Truncated: `no`

```toml
[project]
name = "w2s-research"
version = "0.1.0"
description = "Automated Weak-to-Strong Research System"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    # Core ML
    "torch==2.8.0",
    "transformers[hf_xet]>=4.51.0",
    "tokenizers==0.22.1",
    "datasets==3.6.0",
    "accelerate==1.12.0",
    "peft==0.18.0",
    "trl==0.21.0",
    "bitsandbytes==0.46.1",
    "safetensors==0.7.0",
    "einops==0.8.1",
    "triton==3.4.0",
    # Fast training (Unsloth + LoRA)
    "unsloth==2025.10.12",
    "unsloth-zoo==2025.10.13",
    "liger-kernel==0.6.4",
    "cut-cross-entropy==25.1.1",
    # Fast inference
    "vllm==0.11.0",
    "flash-attn",
    # Scientific computing
    "scipy==1.16.3",
    "numpy<2.0.0",
    "scikit-learn==1.7.2",
    # Utils
    "tqdm==4.67.1",
    "python-dotenv==1.2.1",
    "PyYAML==6.0.3",
    "jinja2>=3.0",
    "httpx==0.28.1",
    "requests>=2.28.0",
    "packaging==25.0",
    "hf-transfer",
    "pylatexenc",
    "nvidia-ml-py>=12.560.30",
    # Tracking
    "wandb==0.23.0",
    # Agent
    "anthropic>=0.78.0",
    "claude_agent_sdk>=0.1.30",
    # Server
    "flask>=3.1.2",
    "flask-cors>=4.0.0",
    "flask-sqlalchemy>=3.1.1",
    # Cloud
    "boto3>=1.28.0",
    "runpod>=1.5.0",
    # Dev
    "pytest",
    "ruff",
    # Extra inference
    "sglang[all]==0.5.2",
    "flashinfer-python==0.3.1",
    "torch-memory-saver",
    # VERL
    "ray[default]==2.52.0",
    "hydra-core==1.3.2",
    "omegaconf==2.3.0",
    "tensordict>=0.8.0,<=0.10.0,!=0.9.0",
    "codetiming",
    "dill",
    "pybind11",
    "optree>=0.13.0",
    "grpcio>=1.62.1",
    # Extra tracking
    "weave==0.52.22",
    "tensorboard==2.20.0",
    # Extra utils
    "torchdata",
    "aiohttp==3.13.2",
    "fastapi[standard]>=0.115.0",
    "uvicorn==0.38.0",
    "pydantic>=2.9",
    "pyarrow>=15.0.0",
    "attrs==25.4.0",
    "matplotlib==3.10.7",
    "pandas==2.3.3",
    "rich==14.2.0",
    "loguru==0.7.3",
    "ninja==1.13.0",
    "qwen-vl-utils",
    "mathruler",
    "sentence-transformers==5.1.2",
    "opencv-python",
    "opencv-fixer",
    "py-spy",
    "pre-commit",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["w2s_research"]

[tool.uv]
# Override conflicting dependencies
override-dependencies = [
    "setuptools>=79.0.0",
    "torchao>=0.13.0",  # unsloth needs >=0.13.0, sglang wants ==0.9.0
    "xgrammar==0.1.25",  # vllm needs ==0.1.25, sglang wants ==0.1.24
    "outlines-core==0.2.11",  # vllm needs ==0.2.11, sglang wants ==0.1.26
]

[tool.uv.sources]
# flash-attn from pre-built wheel (cu12, torch2.8, cxx11abi=False, cp312)
flash-attn = { url = "https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.1/flash_attn-2.8.1+cu12torch2.8cxx11abiFALSE-cp312-cp312-linux_x86_64.whl" }
```
