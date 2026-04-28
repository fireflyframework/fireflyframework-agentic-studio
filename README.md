# fireflyframework-agentic-studio

[![CI](https://github.com/fireflyframework/fireflyframework-agentic-studio/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/fireflyframework/fireflyframework-agentic-studio/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)

**Visual IDE and runtime for [fireflyframework-agentic](https://github.com/fireflyframework/fireflyframework-agentic).**

A browser-based, drag-and-drop pipeline builder with real-time code generation,
an AI assistant, time-travel debugging, auto-generated REST/queue endpoints,
cron scheduling, and Cloudflare Tunnel exposure. Bundled as a single Python
package — the SvelteKit frontend is built and served from inside the wheel,
so end users do not need Node.js installed.

---

## Table of Contents

- [Features](#features)
- [Install](#install)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Documentation](#documentation)
- [Migration from `fireflyframework-agentic[studio]`](#migration-from-fireflyframework-agenticstudio)
- [Development](#development)
- [License](#license)

---

## Features

- **Visual canvas** — Drag and connect Agent, Tool, Reasoning, Condition,
  Memory, Validator, Input, Output, FanIn, FanOut, and CustomCode nodes.
- **Code generation** — Real-time Python output from the graph in the Code tab.
- **AI assistant** — Natural-language pipeline construction over WebSocket
  (any Pydantic AI-compatible model).
- **Project management** — On-disk persistence, per-project REST API,
  auto-generated endpoints driven by Input/Output boundary nodes.
- **Time-travel debugging** — Execution checkpoints capture state at every step.
- **Tunnel exposure** — One-command Cloudflare Quick Tunnel for sharing a local
  Studio instance over HTTPS.
- **GraphQL + WebSocket** — Strawberry-based GraphQL API and live event streaming.
- **Desktop app** (optional) — Tauri-based native shell for offline use.

---

## Install

```bash
pip install fireflyframework-agentic-studio
```

This pulls in `fireflyframework-agentic` as a dependency. The frontend is
bundled inside the wheel.

For development and contribution work, see [Development](#development).

---

## Quick Start

Launch the Studio web UI:

```bash
firefly studio
```

Open http://127.0.0.1:8470 in your browser. Create a new project, drag nodes
onto the canvas, connect them, and click **Run**.

Programmatic launch with custom config:

```python
from fireflyframework_agentic_studio.config import StudioConfig
from fireflyframework_agentic_studio.server import create_app

config = StudioConfig(
    host="0.0.0.0",
    port=8080,
    project_dir="~/my-projects",
)
app = create_app(config)
# serve `app` with any ASGI server (uvicorn, hypercorn, ...)
```

Expose a local Studio over Cloudflare Tunnel:

```bash
firefly expose
```

---

## Architecture

```
fireflyframework-agentic-studio/
├── src/fireflyframework_agentic_studio/   ← FastAPI backend, runtime, codegen, AI assistant
│   ├── api/                                  REST endpoints (FastAPI)
│   ├── assistant/                            AI assistant (Pydantic AI agents)
│   ├── codegen/                              Graph → Python source
│   ├── execution/                            Compiler, runner, checkpoints, I/O nodes
│   ├── cli.py                                `firefly` command
│   ├── server.py                             FastAPI app factory
│   ├── runtime.py                            ProjectRuntime
│   └── tunnel.py                             Cloudflare Quick Tunnels
├── studio-frontend/                        ← SvelteKit 5 SPA (built into wheel)
├── studio-desktop/                         ← Tauri shell (optional, separate build)
├── scripts/build_studio.py                 ← Frontend build helper
├── tests/                                  ← pytest suite
├── examples/                               ← Programmatic launch examples
└── docs/                                   ← Full documentation
```

The Studio depends on `fireflyframework-agentic` for all the core primitives
(agents, tools, prompts, reasoning, memory, observability, exposure, pipeline,
embeddings, vectorstores). It adds the visual layer, project runtime, and
operational surfaces (tunnel, scheduler, GraphQL).

---

## Documentation

- **[Studio overview](docs/studio.md)** — Visual IDE, canvas, code generation, AI assistant.
- **[Studio agents](docs/studio-agents.md)** — Internal architecture of the assistant, oracle, and smith agents.
- **[Input/Output Nodes](docs/input-output-nodes.md)** — Boundary nodes, trigger types, destination types, schema validation.
- **[Project API](docs/project-api.md)** — Per-project REST endpoints, async execution, file upload, GraphQL.
- **[Scheduling](docs/scheduling.md)** — Cron-based triggers, timezones, payload injection.
- **[Tunnel Exposure](docs/tunnel-exposure.md)** — Cloudflare Quick Tunnels, `firefly expose`, Share button.
- **[API Reference](docs/api-reference.md)** — Complete endpoint reference for REST, WebSocket, GraphQL.
- **[BPM Pipeline Tutorial](docs/tutorial-bpm-pipeline.md)** — End-to-end walkthrough.

For the underlying framework, see [fireflyframework-agentic](https://github.com/fireflyframework/fireflyframework-agentic).

---

## Migration from `fireflyframework-agentic[studio]`

If you previously used the embedded Studio that shipped inside
`fireflyframework-genai` or `fireflyframework-agentic`, follow these steps.

### 1. Install the new package

```diff
- pip install "fireflyframework-genai[studio]"
+ pip install fireflyframework-agentic-studio
```

The CLI (`firefly`) is unchanged — it now ships with this package.

### 2. Update Python imports

The Studio module moved from a sub-package (`fireflyframework_genai.studio.*`)
to a top-level package (`fireflyframework_agentic_studio.*`).

```diff
- from fireflyframework_genai.studio.cli import main
+ from fireflyframework_agentic_studio.cli import main

- from fireflyframework_genai.studio.config import StudioConfig
+ from fireflyframework_agentic_studio.config import StudioConfig

- from fireflyframework_genai.studio.server import create_app
+ from fireflyframework_agentic_studio.server import create_app

- from fireflyframework_genai.studio.execution.io_nodes import InputNodeConfig
+ from fireflyframework_agentic_studio.execution.io_nodes import InputNodeConfig
```

A blanket replace works for almost every import:

```bash
grep -rl 'fireflyframework_genai.studio' . | xargs sed -i \
  's/fireflyframework_genai\.studio/fireflyframework_agentic_studio/g'
```

If you were already on the renamed `fireflyframework_agentic.studio` namespace
(unreleased intermediate state), use:

```bash
grep -rl 'fireflyframework_agentic.studio' . | xargs sed -i \
  's/fireflyframework_agentic\.studio/fireflyframework_agentic_studio/g'
```

### 3. Update the framework dependency

The Studio depends on `fireflyframework-agentic` (the framework, also renamed).
If you have a direct dependency on the framework, update it too:

```diff
- pip install fireflyframework-genai
+ pip install fireflyframework-agentic
```

```diff
- from fireflyframework_genai import FireflyGenAIConfig, get_config
+ from fireflyframework_agentic import FireflyAgenticConfig, get_config
```

Environment variables also changed prefix:

```diff
- FIREFLY_GENAI_DEFAULT_MODEL=...
+ FIREFLY_AGENTIC_DEFAULT_MODEL=...
```

The REST factory was renamed:

```diff
- from fireflyframework_genai.exposure.rest import create_genai_app
+ from fireflyframework_agentic.exposure.rest import create_agentic_app
```

### 4. Project files on disk

Existing on-disk projects (graphs, checkpoints, settings) remain compatible.
The Studio reads and writes the same JSON layout as before.

### 5. Configuration files

If you reference Studio modules in `pyproject.toml` (e.g. plugin entry points),
update them to the new top-level path:

```diff
[project.entry-points."myplugin"]
- panel = "fireflyframework_genai.studio.api.assistant:my_function"
+ panel = "fireflyframework_agentic_studio.api.assistant:my_function"
```

### 6. CI

If your CI was installing `[studio]` extras, switch to a direct install:

```diff
- run: uv sync --extra dev --extra studio
+ run: uv pip install fireflyframework-agentic-studio
```

---

## Development

```bash
# Clone
git clone https://github.com/fireflyframework/fireflyframework-agentic-studio.git
cd fireflyframework-agentic-studio

# Install dev dependencies
uv sync --extra dev

# Install pre-commit hooks
uv run pre-commit install

# Build the frontend (required for tests that hit static assets)
python scripts/build_studio.py

# Run tests
uv run pytest

# Lint and format
uv run ruff check .
uv run ruff format .

# Type check
uv run pyright
```

The frontend lives in `studio-frontend/` (SvelteKit 5). For frontend-only
development:

```bash
cd studio-frontend
npm ci
npm run dev   # http://localhost:5173, expects backend on :8470
```

The Tauri desktop app lives in `studio-desktop/` and is built separately.

---

## License

Apache-2.0 © Firefly Software Solutions Inc. See [LICENSE](LICENSE).
