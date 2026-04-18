"""ANSI color support for human-readable stderr output.

Zero-dependency — uses raw escape codes only.  Enable/disable is
controlled globally via :func:`init` so every call site honours
``--color=auto|always|never`` without threading a flag around.
"""

from __future__ import annotations

import os
import sys

# ── Global state ─────────────────────────────────────────────

_enabled: bool = False


def init(mode: str = "auto") -> None:
    """Set the colour mode for the process.

    *mode* is one of ``"auto"`` (default), ``"always"``, or ``"never"``.
    ``auto`` enables colour when stderr is a TTY **and** the
    ``NO_COLOR`` environment variable is not set.
    """
    global _enabled
    if mode == "always":
        _enabled = True
    elif mode == "never":
        _enabled = False
    else:  # auto
        _enabled = _stderr_supports_color()


def enabled() -> bool:
    return _enabled


def _stderr_supports_color() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    if not hasattr(sys.stderr, "isatty"):
        return False
    if not sys.stderr.isatty():
        return False
    # Windows: modern Terminal / WT supports ANSI; enable VT processing
    if sys.platform == "win32":
        return _enable_win_vt()
    return True


def _enable_win_vt() -> bool:
    """Try to enable ANSI/VT processing on Windows 10+ console."""
    try:
        import ctypes
        import ctypes.wintypes as wt

        STD_ERROR_HANDLE = -12
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(STD_ERROR_HANDLE)
        mode = wt.DWORD()
        if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False
        if not kernel32.SetConsoleMode(
            handle, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
        ):
            return False
        return True
    except Exception:
        return False


# ── Escape helpers ───────────────────────────────────────────

def _seq(*codes: int) -> str:
    return f"\033[{';'.join(str(c) for c in codes)}m"


RESET = _seq(0)
BOLD = _seq(1)
DIM = _seq(2)
ITALIC = _seq(3)

RED = _seq(31)
GREEN = _seq(32)
YELLOW = _seq(33)
BLUE = _seq(34)
MAGENTA = _seq(35)
CYAN = _seq(36)
WHITE = _seq(37)
BRIGHT_CYAN = _seq(96)
BRIGHT_WHITE = _seq(97)
BOLD_RED = _seq(1, 31)
BOLD_YELLOW = _seq(1, 33)
BOLD_WHITE = _seq(1, 37)


def style(text: str, *codes: str) -> str:
    """Wrap *text* in ANSI codes if colour is enabled."""
    if not _enabled or not codes:
        return text
    return "".join(codes) + text + RESET
