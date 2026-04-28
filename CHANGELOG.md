# Changelog

All notable changes to `fireflyframework-agentic-studio` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [26.04.28] — Initial Release

Studio extracted from `fireflyframework-agentic` (formerly `fireflyframework-genai`)
into its own repository. See [MIGRATION](README.md#migration-from-fireflyframework-agenticstudio)
for upgrade instructions from earlier embedded Studio versions.

### Added

- Visual pipeline IDE: drag-and-drop canvas with Agent, Tool, Reasoning, Condition,
  Memory, Validator, Input, Output, FanIn, FanOut, and CustomCode nodes.
- Real-time Python code generation from the graph (Code tab).
- AI assistant via WebSocket — natural-language pipeline construction.
- Project management with on-disk persistence and per-project REST API.
- Auto-generated REST endpoints, queue consumers, and cron schedulers from
  Input/Output boundary node configuration.
- Time-travel debugging via execution checkpoints.
- Cloudflare Quick Tunnel integration for one-command public exposure.
- GraphQL API (Strawberry) and WebSocket streaming for live execution events.
- SvelteKit 5 SPA bundled inside the Python package — no Node.js needed at runtime.
- Tauri-based desktop app (optional) for offline use.
- `firefly` CLI: `studio`, `expose`, `build` subcommands.

### Changed

- Module path: `fireflyframework_genai.studio.*` → `fireflyframework_agentic_studio.*`.
- Install: `pip install "fireflyframework-genai[studio]"` → `pip install fireflyframework-agentic-studio`.
- Studio is now an independently-versioned package that depends on
  `fireflyframework-agentic` rather than living inside it.
