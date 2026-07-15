#!/usr/bin/env python3
"""Persist the preferred plotting backend for ieee-figure-table."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


VALID = {"python", "r"}


def config_path() -> Path:
    override = os.environ.get("IEEE_FIGURE_CONFIG")
    if override:
        return Path(override).expanduser()
    return Path.home() / ".config" / "ieee-skills" / "ieee-figure-table.json"


def load() -> dict:
    path = config_path()
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save(data: dict) -> None:
    path = config_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] not in {"get", "set", "clear"}:
        print("usage: ieee_figure_backend.py get|set <python|r>|clear", file=sys.stderr)
        return 2

    command = argv[1]
    data = load()

    if command == "get":
        backend = data.get("backend", "")
        print(backend if backend in VALID else "")
        return 0

    if command == "clear":
        data.pop("backend", None)
        save(data)
        return 0

    if len(argv) != 3 or argv[2] not in VALID:
        print("backend must be python or r", file=sys.stderr)
        return 2

    data["backend"] = argv[2]
    save(data)
    print(argv[2])
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
