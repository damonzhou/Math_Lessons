#!/usr/bin/env python3
"""Check problem-level source-link traceability in Markdown.

For headings containing SOURCE or ADAPTED, require a nearby official-original
source marker with a Markdown/HTTP link. For SYNTHESIS, require a nearby
"无单一原题" or "结构来源" marker; when "结构来源" is used, require a link.

Usage:
    python3 tools/lint_problem_source_links.py file1.md file2.md ...

If no paths are supplied, scans all Markdown files under the repository root.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HEADING = re.compile(r"^\s{0,3}#{1,6}\s+")
INLINE_CODE = re.compile(r"`[^`]*`")
LINK = re.compile(r"(?:https?://|\]\(https?://)")
SOURCE_OR_ADAPTED = re.compile(r"\b(?:SOURCE|ADAPTED)\b")
SYNTHESIS = re.compile(r"\bSYNTHESIS\b")


def markdown_files(args: list[str]) -> list[Path]:
    if args:
        return [Path(a) for a in args if a.endswith(".md") and Path(a).exists()]
    return [p for p in Path(".").rglob("*.md") if ".git" not in p.parts]


def visible_text(raw: str) -> str:
    return INLINE_CODE.sub("", raw)


def nearby(lines: list[str], start: int, count: int) -> list[str]:
    # Stop before the next heading so one problem cannot borrow another's source block.
    out: list[str] = []
    for raw in lines[start + 1 : min(len(lines), start + 1 + count)]:
        if HEADING.match(visible_text(raw)):
            break
        out.append(visible_text(raw))
    return out


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    in_fence = False

    for idx, raw in enumerate(lines):
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        visible = visible_text(raw)
        if not HEADING.match(visible):
            continue

        if SOURCE_OR_ADAPTED.search(visible):
            block = nearby(lines, idx, 10)
            joined = "\n".join(block)
            has_original_marker = "原题" in joined
            has_link = bool(LINK.search(joined))
            if not (has_original_marker and has_link):
                errors.append(
                    f"{path}:{idx + 1}: SOURCE/ADAPTED problem heading lacks nearby official original-problem link"
                )

        if SYNTHESIS.search(visible):
            block = nearby(lines, idx, 14)
            joined = "\n".join(block)
            has_no_single = "无单一原题" in joined
            has_structure = "结构来源" in joined
            if not (has_no_single or has_structure):
                errors.append(
                    f"{path}:{idx + 1}: SYNTHESIS problem heading must state '无单一原题' or provide '结构来源'"
                )
            if has_structure and not LINK.search(joined):
                errors.append(
                    f"{path}:{idx + 1}: SYNTHESIS structure-source block lacks an official link"
                )

    return errors


def main() -> int:
    files = markdown_files(sys.argv[1:])
    errors: list[str] = []
    for path in files:
        errors.extend(check_file(path))

    for item in errors:
        print(f"ERROR: {item}")

    if errors:
        print(f"\nProblem source-link lint failed: {len(errors)} error(s).")
        return 1

    print(f"Problem source-link lint passed: {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
