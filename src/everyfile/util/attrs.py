from __future__ import annotations

# Map from single-character code to FILE_ATTRIBUTE_* bitmask value.
ATTR_CHARS: dict[str, int] = {
    "R": 0x01,    # Read only
    "H": 0x02,    # Hidden
    "S": 0x04,    # System
    "D": 0x10,    # Directory
    "A": 0x20,    # Archive
    "N": 0x80,    # Normal
    "T": 0x100,   # Temporary
    "P": 0x200,   # Sparse file
    "L": 0x400,   # Reparse point
    "C": 0x800,   # Compressed
    "O": 0x1000,  # Offline
    "I": 0x2000,  # Not content indexed
    "E": 0x4000,  # Encrypted
}

# Stable display order used by attrs_to_string.
_ATTR_ORDER: str = "RHSDANTPLOCIE"


def attrs_to_string(bitmask: int) -> str:
    """Convert a FILE_ATTRIBUTE_* bitmask to a compact char string like ``'RHA'``."""
    return "".join(ch for ch in _ATTR_ORDER if bitmask & ATTR_CHARS[ch])


def string_has_attrs(attr_string: str, required_chars: str) -> bool:
    """Check if *attr_string* contains **all** chars in *required_chars*."""
    attr_set = set(attr_string.upper())
    return all(ch.upper() in attr_set for ch in required_chars)
