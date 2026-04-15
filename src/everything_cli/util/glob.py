from __future__ import annotations

import fnmatch


def glob_match(value: str, pattern: str) -> bool:
    """Case-insensitive glob match.

    Uses :mod:`fnmatch` semantics: ``*`` matches everything, ``?`` matches one
    char, ``[seq]`` matches any char in *seq*.
    """
    return fnmatch.fnmatch(value.lower(), pattern.lower())
