"""
Yet Another Demo

A (dummy) demo of my Copier template for Python packages
"""

import argparse
from importlib import metadata


def get_version() -> str:
    try:
        return metadata.version("yet-another-demo")
    except metadata.PackageNotFoundError:
        return "unknown"


def get_parser() -> argparse.ArgumentParser:
    """Return the CLI argument parser."""
    parser = argparse.ArgumentParser(prog="yet-another-demo")
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {get_version()}")
    return parser


def main(args: list[str] | None = None) -> int:
    """Run the main program."""
    parser = get_parser()
    opts = parser.parse_args(args=args)
    print(opts)
    return 0


__all__: list[str] = ["get_parser", "main"]
