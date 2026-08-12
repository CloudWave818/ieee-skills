#!/usr/bin/env python3
"""Create a lightweight inventory of a research-material folder."""

from __future__ import annotations

import argparse
import os
from pathlib import Path


CATEGORY_EXTENSIONS = {
    "notes": {".md", ".markdown", ".txt", ".rst", ".docx"},
    "code": {
        ".py",
        ".ipynb",
        ".m",
        ".mat",
        ".jl",
        ".r",
        ".cpp",
        ".cc",
        ".c",
        ".h",
        ".hpp",
        ".java",
        ".js",
        ".ts",
        ".yaml",
        ".yml",
        ".json",
        ".toml",
        ".ini",
        ".sh",
        ".ps1",
    },
    "experiments": {".csv", ".tsv", ".xlsx", ".xls", ".log", ".out", ".jsonl"},
    "literature": {".bib", ".ris", ".nbib", ".enw"},
    "figures_tables": {".svg", ".png", ".jpg", ".jpeg", ".pdf", ".pptx", ".eps", ".tif", ".tiff"},
}

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    ".ipynb_checkpoints",
    "dist",
    "build",
}


def categorize(path: Path) -> str:
    lower_name = path.name.lower()
    suffix = path.suffix.lower()
    if "readme" in lower_name:
        return "notes"
    if "zotero" in lower_name or "related" in lower_name or "literature" in lower_name:
        return "literature"
    if "result" in lower_name or "metric" in lower_name or "experiment" in lower_name:
        return "experiments"
    for category, extensions in CATEGORY_EXTENSIONS.items():
        if suffix in extensions:
            return category
    return "unknown"


def iter_files(root: Path, max_files: int) -> list[Path]:
    files: list[Path] = []
    for current_root, dirs, filenames in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for filename in filenames:
            path = Path(current_root) / filename
            files.append(path)
            if len(files) >= max_files:
                return files
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", help="Research-material folder to inventory")
    parser.add_argument("--max-files", type=int, default=400, help="Maximum files to list")
    parser.add_argument("--top-per-category", type=int, default=40, help="Maximum files shown per category")
    args = parser.parse_args()

    root = Path(args.folder).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    grouped: dict[str, list[Path]] = {
        "notes": [],
        "code": [],
        "experiments": [],
        "literature": [],
        "figures_tables": [],
        "unknown": [],
    }

    files = iter_files(root, args.max_files)
    for path in files:
        grouped[categorize(path)].append(path)

    print(f"# Research Folder Inventory\n")
    print(f"- Root: `{root}`")
    print(f"- Files scanned: {len(files)}")
    print(f"- Max files: {args.max_files}\n")

    for category, paths in grouped.items():
        print(f"## {category} ({len(paths)})")
        for path in sorted(paths)[: args.top_per_category]:
            rel = path.relative_to(root)
            try:
                size = path.stat().st_size
            except OSError:
                size = 0
            print(f"- `{rel}` ({size} bytes)")
        if len(paths) > args.top_per_category:
            print(f"- ... {len(paths) - args.top_per_category} more")
        print()

    if len(files) >= args.max_files:
        print("> Inventory stopped at max-files. Increase --max-files for a deeper pass.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
