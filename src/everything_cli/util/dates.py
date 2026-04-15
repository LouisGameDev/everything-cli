from __future__ import annotations

import datetime

# 100-nanosecond ticks per second in a FILETIME value.
TICKS_PER_SECOND = 10_000_000

# Seconds between the Windows epoch (1601-01-01) and the Unix epoch (1970-01-01).
EPOCH_DIFF = 11_644_473_600


def filetime_to_iso(filetime_value: int) -> str:
    """Convert a Windows FILETIME (100ns ticks since 1601-01-01) to ISO 8601 UTC string.

    Returns format: "2025-03-01T14:22:31Z"
    Returns empty string if filetime_value is 0 or invalid.
    """
    if filetime_value <= 0:
        return ""
    try:
        timestamp = filetime_value / TICKS_PER_SECOND - EPOCH_DIFF
        dt = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except (OSError, OverflowError, ValueError):
        return ""


def parse_iso_date(s: str) -> datetime.datetime:
    """Parse an ISO 8601 date string to datetime.

    Supports ``YYYY-MM-DD`` and ``YYYY-MM-DDTHH:MM:SSZ``.
    """
    s = s.strip()
    if "T" in s:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=datetime.timezone.utc,
        )
    return datetime.datetime.strptime(s, "%Y-%m-%d").replace(
        tzinfo=datetime.timezone.utc,
    )
