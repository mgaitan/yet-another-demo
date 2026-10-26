# Development Workflow (How-to)

This guide covers the most common maintenance tasks.

## Run local QA before pushing

```bash
make qa
make test
```

If `prek` is not installed, install it once with:

```bash
uv tool install prek
```

## Update dependencies safely

This template uses `uv` groups and cooldown windows.
After dependency changes:

```bash
uv sync
make qa
make test
```

Commit `uv.lock` after dependency changes. The local `uv-lock` prek hook refreshes
it when dependency configuration changes, and CI checks `uv lock --check`.

## Prepare a release

Start from a clean, up-to-date `main` and run the project checks first:

```bash
make qa
make test
make release-pr BUMP=minor
```

`BUMP` accepts `patch`, `minor`, or `major`. Review the version and generated notes
in the `release/<version>` PR. Merging publishes to PyPI and creates the GitHub
release automatically, without a draft or manual tag. Documentation updates on
pushes to `main`; manual workflow dispatch only publishes documentation.

## Preview documentation in pull requests

When docs files change in a PR, CI deploys a preview to:

```text
https://mgaitan.github.io/yet-another-demo/_preview/pr-<PR_NUMBER>/
```

If needed, dispatch docs publishing manually:

```bash
gh workflow run cd.yml --ref main
```

`gh` authentication can use {term}`GH_TOKEN`.
