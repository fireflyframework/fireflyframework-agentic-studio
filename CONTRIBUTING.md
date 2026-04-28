# Contributing to fireflyframework-agentic-studio

Copyright 2026 Firefly Software Solutions Inc. Licensed under the Apache License 2.0.

Thank you for considering a contribution. This document explains how to set up
your development environment, the coding standards we follow, and the process
for submitting changes.

---

## Development Environment

### Prerequisites

- Python 3.13 or later.
- [UV](https://docs.astral.sh/uv/) for dependency and virtual-environment management.
- Git.
- Node.js 20+ and npm — required to build the SvelteKit frontend from source
  (the published wheel ships with a pre-built bundle).
- Rust toolchain — only required if you intend to build the Tauri desktop app.

### Setup

```bash
git clone https://github.com/fireflyframework/fireflyframework-agentic-studio.git
cd fireflyframework-agentic-studio
uv sync --extra dev
uv run pre-commit install
```

This installs runtime, development, and `fireflyframework-agentic` itself
(the framework the Studio depends on).

### Building the Frontend (source installs only)

The Studio frontend is a SvelteKit SPA that lives in `studio-frontend/` and is
served by FastAPI from `src/fireflyframework_agentic_studio/static/`. The
published wheel includes a pre-built bundle, but a fresh `git clone` does
**not** — running `firefly studio` against an unbuilt source tree returns
`{"detail":"Not Found"}` on every page.

Build the frontend once after cloning (and again after pulling frontend changes):

```bash
uv run python scripts/build_studio.py
```

The script runs `npm install` (if needed), `npm run build`, and copies the
output into the package's `static/` directory.

### Running Tests

```bash
uv run pytest
```

To generate a coverage report:

```bash
uv run pytest --cov=fireflyframework_agentic_studio --cov-report=term-missing
```

### Linting

```bash
uv run ruff check .
uv run ruff format --check .
```

### Type Checking

```bash
uv run pyright
```

### Pre-commit

Hooks run automatically on `git commit`. To run them manually:

```bash
uv run pre-commit run --all-files
```

---

## Coding Standards

### Style

- Follow PEP 8. Ruff enforces this automatically.
- Maximum line length is 120 characters.
- Use `from __future__ import annotations` at the top of every module.
- All public functions, classes, and methods must have docstrings.
- Prefer explicit type annotations over implicit types.
- All imports at the top of the file (no inline/lazy imports).

### Copyright Header

Every Python source file must begin with the Apache 2.0 copyright header:

```python
# Copyright 2026 Firefly Software Solutions Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
```

### Imports

Imports are organised into three groups, separated by blank lines:

1. Standard library.
2. Third-party packages.
3. Internal (`fireflyframework_agentic_studio`) modules.

Ruff's isort rules enforce this automatically.

### Testing

- Every new module must have a corresponding test file under `tests/`.
- Use `pytest` with `pytest-asyncio` for asynchronous tests.
- Use plain functions, not classes, for test cases.
- Mock external services rather than making real network calls.

---

## Submitting Changes

### Branch Naming

Use descriptive branch names:

- `feat/canvas-undo-redo`
- `fix/oracle-shared-context-leak`
- `docs/api-reference-projects-section`
- `refactor/codegen-template-engine`

### Commit Messages

Write clear, imperative-mood commit messages with a single-sentence subject and
optional body:

```
fix: oracle shared context loses tools on reload

The OracleAgent rebuilt its tool registry from disk after every
project reload, dropping any custom tools registered at runtime.
Persist them in StudioState instead.
```

### Pull Request Process

1. Create a feature branch from `main`. Never push directly to `main`.
2. Make your changes; ensure all tests pass and lint is clean.
3. Open a pull request against `main`.
4. Fill in the PR description: what changed, why, and how it was tested.
5. Address review feedback.
6. Once approved, a maintainer will merge.

### Review Checklist

Before opening a PR, confirm that:

- All new Python code has the copyright header.
- All public APIs have docstrings.
- Tests cover the new or changed behaviour.
- `uv run pre-commit run --all-files` reports no issues.
- `uv run pyright` reports no errors.
- `uv run pytest` passes.

---

## Reporting Issues

Open an issue with:

- A clear title summarising the problem.
- Steps to reproduce.
- Expected and actual behaviour.
- Your Python and Node.js versions, operating system, and `firefly --version`.

## Code of Conduct

We are committed to providing a welcoming and inclusive experience for everyone.
Be respectful, constructive, and professional in all interactions.
