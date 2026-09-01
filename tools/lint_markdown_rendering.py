#!/usr/bin/env python3
"""Lightweight Markdown rendering checks for Math_Lessons.

Usage:
    python tools/lint_markdown_rendering.py path1.md path2.md ...

If no paths are supplied, scans all Markdown files under the repository root.
Errors return exit code 1. Warnings do not fail the check.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HEADING = re.compile(r"^\s{0,3}#{1,6}\s+")
INLINE_MATH = re.compile(r"\$([^$\n]+)\$")
SIMPLE_NUMBER = re.compile(r"^[+-]?\d+(?:\.\d+)?$")
TEMP_LATEX = re.compile(
    r"\$[^$\n]*(?:\^\s*\\circ|\\degree)[^$\n]*(?:\\mathrm\s*\{?C\}?|C)[^$\n]*\$"
)
DETAILS_OPEN = re.compile(r"<details\b", re.IGNORECASE)


def markdown_files(args: list[str]) -> list[Path]:
    if args:
        return [Path(a) for a in args if a.endswith(".md") and Path(a).exists()]
    return [p for p in Path(".").rglob("*.md") if ".git" not in p.parts]


def check_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    in_fence = False

    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if HEADING.match(raw) and "$" in raw:
            errors.append(
                f"{path}:{lineno}: heading contains '$...$'; use plain text/Unicode in headings"
            )

        if TEMP_LATEX.search(raw):
            errors.append(
                f"{path}:{lineno}: temperature uses inline LaTeX; write e.g. '0 ℃' instead"
            )

        if DETAILS_OPEN.search(raw):
            warnings.append(
                f"{path}:{lineno}: <details> detected; do not place full math answers inside raw HTML"
            )

        for match in INLINE_MATH.finditer(raw):
            expr = match.group(1).strip()
            if SIMPLE_NUMBER.fullmatch(expr):
                warnings.append(
                    f"{path}:{lineno}: simple numeric inline math '${expr}$'; plain text is more robust"
                )

    return errors, warnings


def main() -> int:
    files = markdown_files(sys.argv[1:])
    errors: list[str] = []
    warnings: list[str] = []

    for path in files:
        e, w = check_file(path)
        errors.extend(e)
        warnings.extend(w)

    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")

    if errors:
        print(f"\nMarkdown rendering lint failed: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1

    print(f"Markdown rendering lint passed: {len(files)} file(s), {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
