from __future__ import annotations

import json
import sys

from .output.human import error
from .output.ndjson import write_record


def run_pick(fields: list[str]) -> int:
    """Read NDJSON from stdin, emit only the specified fields from each record.

    Args:
        fields: List of field names to extract.

    Returns:
        Exit code (0 = success, 4 = invalid JSON on stdin).
    """
    try:
        for lineno, line in enumerate(sys.stdin, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                error(f"stdin line {lineno}: invalid JSON")
                return 4
            picked = {k: record[k] for k in fields if k in record}
            write_record(picked)
    except BrokenPipeError:
        pass
    return 0
