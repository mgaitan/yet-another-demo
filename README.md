> [!NOTE] 
> This is a demo repo generated from my [Copier-based Python package template](https://github.com/mgaitan/python-package-copier-template). It exists only to showcase the default scaffold, workflows, and docs.


# Yet Another Demo

[![CI](https://github.com/mgaitan/yet-another-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/mgaitan/yet-another-demo/actions/workflows/ci.yml)
[![docs](https://img.shields.io/badge/docs-blue.svg?style=flat)](https://mgaitan.github.io/yet-another-demo/)
[![pypi version](https://img.shields.io/pypi/v/yet-another-demo.svg)](https://pypi.org/project/yet-another-demo/)
[![Changelog](https://img.shields.io/github/v/release/mgaitan/yet-another-demo?include_prereleases&label=changelog)](https://github.com/mgaitan/yet-another-demo/releases)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/mgaitan/yet-another-demo/actions/workflows/ci.yml)
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
- Run the QA bundle with [`ty`](https://github.com/astral-sh/ty):

```bash
uv run ty check
```
