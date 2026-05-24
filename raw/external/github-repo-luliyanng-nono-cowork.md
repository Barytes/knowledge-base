---
title: "GitHub repo snapshot: LuliYanng/Nono-Cowork"
source: "https://github.com/LuliYanng/Nono-Cowork"
author:
published:
created: 2026-04-29
description: "Compact GitHub repository evidence snapshot for repo-map-ingest."
tags:
  - "github"
  - "repo-snapshot"
---

# GitHub Repo Snapshot: `LuliYanng/Nono-Cowork`

## Observation Scope

- Repository: `LuliYanng/Nono-Cowork`
- URL: https://github.com/LuliYanng/Nono-Cowork
- Requested topic: 仓库架构与工程实践
- Observed ref: `main`
- Latest resolved commit: `c8c4746499033bf81c22cd07c8ad52aabcf97b86`
- Commit date: `2026-04-28T14:25:32Z`
- Snapshot date (UTC): `2026-04-29`

## Repository Metadata

- Description: Nono Cowork: A proactive AI coworker for real workflows that watches for events, gets work done, and syncs results back to your local workspace.
- Default branch: `main`
- Language: `Python`
- Stars: `8`
- Forks: `0`
- Open issues: `0`

## Top-Level Tree

### Directories

- `desktop`
- `developdocs`
- `docs`
- `skills`
- `src`

### Files

- `.env.example`
- `.gitignore`
- `.python-version`
- `LICENSE`
- `README.md`
- `README_zh-CN.md`
- `nono-cowork.service`
- `pyproject.toml`
- `uv.lock`

## Selected Evidence Anchors

- `README.md`
- `pyproject.toml`

## Captured Files

### `README.md`

- Source path: `README.md`
- Truncated: `no`

```md
English | [简体中文](README_zh-CN.md)

<h1 align="center">Nono CoWork</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12+-3776AB.svg?logo=python&logoColor=white" alt="Python 3.12+"></a>
  <a href="https://github.com/LuliYanng/nono-cowork/stargazers"><img src="https://img.shields.io/github/stars/LuliYanng/nono-cowork?style=social" alt="GitHub stars"></a>
</p>

<h3 align="center">The proactive agent for real workflows — not just browser tasks.</h3>

<p align="center">A background coworker that runs on your VPS, watches for events, gets work done,<br>and syncs the results back to your local workspace.</p>

Most AI agents wait for a prompt. Nono starts when something happens.

It monitors your email, synced folders, and the apps you connect to it. When a customer email arrives overnight, Nono reads the relevant files from your synced workspace, drafts a reply based on what's actually in them, and leaves a notification card on your desktop by morning — review, click "Send", done.

Away from your computer? Nono can notify you via Telegram or Feishu too.

**This isn't an assistant waiting for instructions. It's a coworker that's already at work.**

> **Current stage: Early Beta** — Best suited to personal workflows such as document processing, email monitoring, and file automation. Production use with unrestricted shell access or enterprise deployment is not yet recommended.

<p align="center">
  <video src="https://github.com/user-attachments/assets/ae83adab-133f-4a30-9573-42de174efe3b" width="800" controls autoplay loop muted></video>
</p>


---

## What Makes This Different

AI agents can already do a lot. But most still fall into the same trade-offs:

| Approach | The Problem |
|:---|:---|
| **Cloud agents** | Work 24/7, but files stay in their cloud. You still have to download and move everything back into your workflow. |
| **Desktop agents** | Can work with local files, but usually require your computer to stay online — and often need broader access to your local environment. |
| **Automation tools** | Great at connecting apps, but limited to predefined if-this-then-that workflows. |

**Nono CoWork takes a different approach: it keeps the agent online on your VPS while delivering outputs back into the folders you already use.**

- 🧠 **Proactive** — Monitors email, file changes, and connected apps. Acts when something important happens — no prompt required.
- ☁️ **Always on** — Runs continuously on your VPS, so work can keep moving even when your laptop is closed.
- 📁 **Local-first delivery** — Results sync directly into your local folders, so outputs show up where you already work.
- 🔒 **Isolated by architecture** — Runs on your VPS and cannot directly control your local device. It only sees the folders you explicitly sync.
- ✋ **Human-in-the-loop** — Drafts the email, but waits for your approval before sending. Critical actions wait for your review.

---

## It Moves Your Workflow Forward

| When this happens | Nono gets this done first | You only need to... |
| :--- | :--- | :--- |
| 📧 A prospect asks for pricing | Open your synced rate card → find the matching tier → apply volume discount and add-ons → draft a reply with every number traceable to a sheet row | Review the quote and decide whether to send |
| 📬 A client goes silent for 3 days | Detect the stalled thread → quote the original conversation → draft a polite follow-up email | Click confirm and let it send |
| 📊 You drop a spreadsheet into your local work folder | Detect the new file → run analysis → generate charts and conclusions → save a finished report | Open the report |
| 🗂️ Your inbox fills up with PDFs, screenshots, and loose documents | Identify each file type → rename and categorize it → move it into the right folder | Check the results when you want |

> It doesn't wait for one-off prompts. When something happens, it pushes the work forward until only the final decision needs your input.

---

## Architecture

```text
  Events (24/7)                        Your VPS
  ┌──────────────┐               ┌──────────────────────────────┐
  │ 📨 Gmail      │──Composio───►│                              │
  │ 📋 GitHub     │──WebSocket──►│   Event Router               │
  │ 📅 Calendar   │──Triggers───►│      ↓                       │
  │ 📁 File Drop  │──Syncthing──►│   Agent Engine (LLM)         │
  └──────────────┘               │      ↓                       │
                                 │   Autonomous Execution       │
  Control (anytime)              │   ├─ Read/write/edit files   │
  ┌──────────────┐               │   ├─ Run shell commands      │
  │ 📱 Telegram   │─────────────►│   ├─ Search the web          │
  │ 📱 Feishu     │─────────────►│   ├─ Call 1,000+ app APIs    │
  │ 🖥️ Desktop    │──HTTP+SSE───►│   └─ Schedule future tasks   │
  │ 💻 Terminal   │─────────────►│      ↓                       │
  └──────────────┘               │   Notification System        │
                                 │   (Human-in-the-loop cards)  │
  Your devices                   │      ↓                       │
  ┌──────────────┐               │   📁 ~/Sync (workspace)      │
  │ 📁 ~/Sync    │◄──Syncthing──►│      ↕ bidirectional         │
  │ (your files) │  encrypted P2P│                              │
  └──────────────┘               └──────────────────────────────┘
```

---

## Quick Start

**Requirements:** A Linux VPS · Python ≥ 3.12 · [uv](https://docs.astral.sh/uv/) · [OpenRouter API key](https://openrouter.ai/)

```bash
# Install uv (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

git clone https://github.com/LuliYanng/nono-cowork.git
cd nono-cowork
uv sync
cp .env.example .env   # Fill in your OPENROUTER_API_KEY
```

```bash
# Start with selected channels (recommended)
CHANNELS=desktop,feishu,telegram uv run python src/main.py

# Or run a single channel for testing
uv run agent            # Terminal REPL (simplest)
uv run feishu-bot       # Feishu only
uv run telegram-bot     # Telegram only
uv run desktop-agent    # Desktop API only
```

For long-running deployment, install the included systemd service:

```bash
# Edit nono-cowork.service first: replace YOUR_USERNAME with your actual username
sudo cp nono-cowork.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now nono-cowork
```

> 💡 One API key, all models. [OpenRouter](https://openrouter.ai/) routes to Claude, GPT, Gemini, DeepSeek, Qwen, and more — switch models with one line in `.env`.

> **Minimal test (no Syncthing or Composio required):** Set `OPENROUTER_API_KEY` in `.env` and run `uv run agent`. You'll have a working agent in the terminal in under 2 minutes. Add Syncthing for file sync and Composio for app triggers when you're ready.

### Firewall / Ports

If your VPS uses a firewall, open the ports for the channels you plan to use:

```bash
sudo ufw allow 8080/tcp    # Desktop API (required for desktop app)
sudo ufw allow 22000/tcp   # Syncthing file sync
sudo ufw allow 21027/udp   # Syncthing discovery
sudo ufw allow 9090/tcp    # Composio webhook (only if using event triggers)
```

---

## Setup Guides

| Component | Guide |
|:---|:---|
| Desktop App | [docs/desktop_setup.md](docs/desktop_setup.md) |
| Syncthing File Sync | [docs/syncthing_setup.md](docs/syncthing_setup.md) |
| Telegram Bot | [docs/telegram_setup.md](docs/telegram_setup.md) |
| Feishu (Lark) Bot | [docs/feishu_setup.md](docs/feishu_setup.md) |
| Composio (App Integrations) | [docs/composio_setup.md](docs/composio_setup.md) |
| Firewall / Ports | See [Quick Start](#quick-start) above |

---


## License

Apache License 2.0
```

### `pyproject.toml`

- Source path: `pyproject.toml`
- Truncated: `no`

```toml
[project]
name = "nono-cowork"
version = "0.1.0"
description = "Nono CoWork — A self-hosted AI agent on your VPS, controlled via Telegram / Feishu / Terminal, with Syncthing-based local file sync."
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "arxiv>=2.4.0",
    "beautifulsoup4>=4.14.3",
    "composio>=0.11.0,<1.0.0",
    "composio-openai>=0.11.0,<1.0.0",
    "ddgs>=9.10.0",
    "dotenv>=0.9.9",
    "litellm>=1.63.0",
    "ipykernel>=7.2.0",
    "lark-oapi>=1.5.3",
    "markdownify>=1.2.2",
    "openai>=2.24.0",
    "pyTelegramBotAPI>=4.26.0",
    "questionary>=2.1.1",
    "requests>=2.32.5",
    "rich>=14.3.3",
    "apscheduler>=3.11.2",
    "pymupdf>=1.25.0",
    "openpyxl>=3.1.5",
    "python-docx>=1.1.2",
    "fastapi>=0.115.0",
    "uvicorn>=0.34.0",
    "sse-starlette>=2.2.0",
]


[project.scripts]
agent = "src.agent:main"
nono-cowork = "src.main:main"
feishu-bot = "src.channels.feishu:main"
telegram-bot = "src.channels.telegram:main"
desktop-agent = "src.channels.desktop:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src"]
```

## Follow-up Targeted Evidence (2026-04-29)

The repository was not cloned. A follow-up GitHub API tree read was used to identify selected implementation anchors.

### Tree groups worth revisiting

- `src/core/`: agent loop, session, workspace, prompt, LLM wrapper
- `src/channels/`: desktop HTTP/SSE channel, Feishu, Telegram, channel registry
- `src/automations/`: Composio triggers, file-drop automation, scheduler
- `src/delivery/`: notification store and deliverable formatting
- `src/tools/`: shell, file, web, Syncthing, Composio, scheduler, routine, delegation tools
- `src/context/`: context compression and spill handling
- `src/integrations/`: Syncthing event watcher
- `desktop/`: Electron + Vite + React desktop client
- `developdocs/tool-access-control.md`: tool permission model notes
- `skills/`: bundled agent skills, including `skill-creator`

### Targeted implementation anchors read through GitHub API

- `src/main.py`: unified multi-channel startup, shared scheduler, Composio listener, Syncthing watcher, file-drop listener, channel registration, desktop server start.
- `src/core/agent.py`: main agent loop, history sanitization, context compression, tool execution, output spilling, tool redirects, max-round guard.
- `src/core/agent_runner.py`: shared channel invocation path, per-user lock, session lookup, sync-context injection, event forwarding.
- `src/core/session.py`: JSON-backed session persistence and per-user locks.
- `src/core/workspace.py`: workspace records bound to Syncthing folder IDs.
- `src/core/prompt.py`: modular system prompt and workspace resolution order.
- `src/channels/base.py`: shared channel interface and slash command registry.
- `src/channels/desktop.py`: FastAPI desktop API, SSE streaming, session/model/notification/workspace/sync/task/trigger/automation endpoints, bearer token middleware.
- `src/channels/registry.py`: runtime channel lookup used by scheduler and delivery.
- `src/automations/composio_triggers.py`: WebSocket trigger listener, trigger recipe store, disposable event agent sessions.
- `src/automations/file_drop.py`: Syncthing-event rules, debounce, file-drop autonomous agent execution.
- `src/automations/scheduler/engine.py`: APScheduler wrapper with persistent task reload and single-instance execution.
- `src/automations/scheduler/executor.py`: fresh scheduled agent session and notification persistence.
- `src/delivery/notifications.py`: notification index plus full autonomous session storage, SSE pub/sub.
- `src/integrations/syncthing_watcher.py`: Syncthing event long-polling, ring buffer, inbound/outbound sync context.
- `src/tools/registry.py`: `@tool` decorator, tool tags, access presets, tag filtering.
- `src/tools/command.py`: shell execution tool with staging directory and background PID handling.
- `src/tools/delegate.py`: blocking subagent delegation tool.
- `src/tools/scheduler.py`: agent-facing scheduled-task tools.
- `src/tools/routines.py`: unified routine tools for cron, trigger, and file-drop workflows.
- `desktop/package.json`: Electron/Vite/React desktop client build and packaging contract.
- `desktop/src/App.tsx`: desktop client application surface and Electron preload API usage.

### Targeted sync-mechanism anchors read through GitHub API

- `docs/syncthing_setup.md`: manual Syncthing install, device pairing, shared folder setup, VPS API key configuration, recommended `.stignore`, sync verification.
- `docs/desktop_setup.md`: desktop app connection flow and automatic Syncthing pairing claim.
- `desktop/electron/main.cjs`: local Syncthing runtime detection/managed Windows runtime, local API key parsing, local device ID, local remote-device registration, local folder registration, default `.stignore`, IPC bridge.
- `desktop/electron/preload.cjs`: exposes local Syncthing and filesystem IPC APIs to the React UI.
- `desktop/src/components/onboarding-dialog.tsx`: first/default workspace flow: create local folder, register local Syncthing folder, call VPS `/api/sync/folders`, mark workspace default.
- `desktop/src/components/sync-folder-widget.tsx`: active workspace folder status UI and local path resolution through local Syncthing.
- `desktop/src/hooks/use-sync-status.ts`: polling of VPS `/api/sync/status`.
- `src/tools/syncthing.py`: VPS-side Syncthing REST client, API key detection, folder/device/status/completion helpers, cross-device sync status.
- `src/channels/desktop.py`: `/api/sync/pair`, `/api/sync/folders`, `/api/sync/status`, `/api/sync/events`, workspace deletion ordering.
- `src/integrations/syncthing_watcher.py`: VPS long-polling of Syncthing events and injection of recent inbound file activity into agent context.
- `src/core/workspace.py`: workspace-to-Syncthing-folder binding, one workspace to one folder in V1.
