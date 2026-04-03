# Yet Another Demo

[![CI](https://github.com/mgaitan/yet-another-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/mgaitan/yet-another-demo/actions/workflows/ci.yml)
[![docs](https://img.shields.io/badge/docs-blue.svg?style=flat)](https://mgaitan.github.io/yet-another-demo/)
[![pypi version](https://img.shields.io/pypi/v/yet-another-demo.svg)](https://pypi.org/project/yet-another-demo/)
[![Changelog](https://img.shields.io/github/v/release/mgaitan/yet-another-demo?include_prereleases&label=changelog)](https://github.com/mgaitan/yet-another-demo/releases)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/mgaitan/yet-another-demo/actions/workflows/ci.yml)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/mgaitan/yet-another-demo/blob/main/LICENSE)

A (dummy) demo of my Copier template for Python packages

## Quick Start

Run directly without installing via `uvx`:

```bash
uvx yet-another-demo
```

To install the tool permanently:

```bash
uv tool install yet-another-demo
```

## Development

- Install dependencies with `uv sync`.
- New dependency releases are delayed by one week via `uv` cooldown (`[tool.uv].exclude-newer = "1 week"`), with per-package overrides when required (for example, `ty`).
- Install [`prek`](https://github.com/j178/prek) as an external tool:

```bash
uv tool install prek
```

- Install git hooks with `prek`:

```bash
prek install
```

- Run the local QA bundle with `prek`:

```bash
prek run --all-files
```

- PRs with documentation changes publish a docs preview at:

```text
https://mgaitan.github.io/yet-another-demo/_preview/pr-<PR_NUMBER>/
```

## Documentation

- Docs follow [Diataxis](https://diataxis.fr/).
- Start at `docs/index.md` and read:
  - `docs/getting_started.md` (tutorial),
  - `docs/development_workflow.md` (how-to),
  - `docs/configuration.md` (reference),
  - `docs/about_the_docs.md` (explanation and design rationale).
