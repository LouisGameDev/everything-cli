from __future__ import annotations

import collections
import sys
from typing import Any

from . import color

_PROG = "everything"


def info(msg: str) -> None:
    """Print info message to stderr. Format: 'everything: {msg}'"""
    prefix = color.style(f"{_PROG}:", color.DIM)
    print(f"{prefix} {msg}", file=sys.stderr)


def error(msg: str) -> None:
    """Print error message to stderr. Format: 'everything: error: {msg}'"""
    prefix = color.style(f"{_PROG}: error:", color.BOLD_RED)
    print(f"{prefix} {msg}", file=sys.stderr)


def warning(msg: str) -> None:
    """Print warning message to stderr. Format: 'everything: warning: {msg}'"""
    prefix = color.style(f"{_PROG}: warning:", color.BOLD_YELLOW)
    print(f"{prefix} {msg}", file=sys.stderr)


def summary(
    num_results: int,
    total_results: int,
    query: str,
    sort_name: str | None = None,
    descending: bool = False,
) -> None:
    """Print search summary line to stderr."""
    num = color.style(f"{num_results:,}", color.BOLD)
    total = color.style(f"{total_results:,}", color.DIM)
    q = color.style(f'"{query}"', color.BOLD)
    line = f"{color.style(_PROG + ':', color.DIM)} {num} results (of {total} total) for {q}"
    if sort_name is not None:
        arrow = "\u2193" if descending else "\u2191"
        line += "  " + color.style(f"[sorted by {sort_name} {arrow}]", color.DIM)
    print(line, file=sys.stderr)


def version_info(
    cli_version: str,
    python_version: str,
    ev_version: str | None = None,
    instance_name: str | None = None,
    instance_source: str | None = None,
) -> None:
    """Print version to stderr."""
    ev_part = f"Everything {ev_version}" if ev_version else "Everything: not available"
    line = f"everyfile {cli_version} (Python {python_version}) / {ev_part}"
    if instance_name:
        line += f"\nInstance: {instance_name}"
        if instance_source:
            line += f"  (via {instance_source})"
    print(line, file=sys.stderr)


def service_info(
    major: int,
    minor: int,
    revision: int,
    build: int,
    target: str | None,
    db_loaded: bool | None,
    is_admin: bool,
    is_appdata: bool,
    instance_name: str | None = None,
) -> None:
    """Print Everything service info to stderr."""
    version = f"{major}.{minor}.{revision}.{build}"
    header = f"Everything v{version} ({target})" if target else f"Everything v{version}"
    lines = [header]
    if db_loaded is not None:
        lines.append(f"Database: {'loaded' if db_loaded else 'not loaded'}")
    lines.append(f"Admin: {'yes' if is_admin else 'no'}")
    lines.append(f"AppData: {'yes' if is_appdata else 'no'}")
    if instance_name:
        lines.append(f"Instance: {instance_name}")
    print("\n".join(lines), file=sys.stderr)


def instance_list(
    instances: list[dict[str, Any]],
    active_name: str | None,
    active_source: str | None,
    env_var: str,
) -> None:
    """Print discovered Everything instances to stderr.

    Each instance dict has: name, class, hwnd.
    active_name is the currently selected instance (or None for auto).
    active_source describes how the active instance was chosen.
    env_var is the environment variable name for persistence.
    """
    _stderr = sys.stderr
    if not instances:
        print("No Everything instances found.", file=_stderr)
        print("", file=_stderr)
        print("Make sure Voidtools Everything is installed and running.", file=_stderr)
        print("Supported versions: Everything 1.4, 1.5, 1.5a.", file=_stderr)
        print("Download: https://www.voidtools.com/downloads/", file=_stderr)
        return

    print("Running Everything instances:", file=_stderr)
    print("", file=_stderr)
    for inst in instances:
        name = inst["name"]
        marker = "  ←  active" if _matches_active(name, active_name) else ""
        print(f"  {name:<12} class: {inst['class']}{marker}", file=_stderr)

    print("", file=_stderr)
    resolved = active_name if active_name else "auto-detect"
    print(f"Active instance: {resolved}", file=_stderr)
    if active_source:
        print(f"  Selected via: {active_source}", file=_stderr)

    print("", file=_stderr)
    print("Instance selection (highest priority first):", file=_stderr)
    print(f"  1. --instance NAME          CLI option", file=_stderr)
    print(f"  2. ${env_var}    environment variable", file=_stderr)
    print(f"  3. auto-detect              first found (1.5a → 1.5 → 1.4 → default)", file=_stderr)
    print("", file=_stderr)
    print("To persist your choice:", file=_stderr)
    print(f"  $env:{env_var} = \"{instances[0]['name']}\"   # PowerShell (session)", file=_stderr)
    print(f"  [Environment]::SetEnvironmentVariable('{env_var}', '{instances[0]['name']}', 'User')  # permanent", file=_stderr)
    print(f"  export {env_var}={instances[0]['name']}       # bash/zsh", file=_stderr)


def _matches_active(name: str, active_name: str | None) -> bool:
    """Check if an instance name matches the active selection."""
    if active_name is None:
        return False
    if active_name == name:
        return True
    if active_name == "default" and name == "default":
        return True
    return False


# ── Field colorisation ───────────────────────────────────────

_DATE_FIELDS = frozenset((
    "date_modified", "date_created", "date_accessed",
    "date_run", "date_recently_changed",
))


def _color_value(field: str, text: str) -> str:
    """Apply color to a formatted field value."""
    if not text:
        return text
    if field == "name":
        return color.style(text, color.BOLD_WHITE)
    if field in ("path", "full_path"):
        return color.style(text, color.DIM)
    if field == "size":
        return color.style(text, color.YELLOW)
    if field in _DATE_FIELDS:
        return color.style(text, color.CYAN)
    if field == "ext":
        return color.style(text, color.MAGENTA)
    return text


# ── Human-readable result table ──────────────────────────────────────

DEFAULT_COLUMNS: list[str] = ["name", "date_modified", "path", "size"]


def _format_size(val: Any) -> str:
    """Format byte size to human-readable string."""
    if not isinstance(val, (int, float)) or val < 0:
        return str(val)
    if val == 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(val)
    for unit in units[:-1]:
        if size < 1024:
            return f"{size:.0f} {unit}" if size == int(size) else f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} {units[-1]}"


def _format_date(val: Any) -> str:
    """Format ISO 8601 timestamp to a compact human-readable form."""
    if not val or not isinstance(val, str):
        return ""
    # "2025-04-15T12:34:56Z" → "2025-04-15 12:34"
    try:
        date_part, time_part = val.split("T", 1)
        time_short = time_part[:5]  # HH:MM
        return f"{date_part} {time_short}"
    except (ValueError, IndexError):
        return str(val)


def _format_value(field: str, val: Any) -> str:
    """Format a field value for human-readable display."""
    if val is None:
        return ""
    if field == "size":
        return _format_size(val)
    if field in ("date_modified", "date_created", "date_accessed", "date_run",
                 "date_recently_changed"):
        return _format_date(val)
    if isinstance(val, bool):
        return "yes" if val else "no"
    return str(val)


class ResultPrinter:
    """Prints human-readable result rows to stderr with appendix.

    No truncation — full values are printed. After all records, prints
    an appendix with summary statistics and unique filename values.
    """

    def __init__(self, columns: list[str]) -> None:
        self.columns = columns
        self._count = 0
        # Appendix tracking
        self._name_counts: collections.Counter[str] = collections.Counter()
        self._total_size: int = 0
        self._has_size = False
        self._ext_counts: collections.Counter[str] = collections.Counter()

    def print_record(self, record: dict[str, Any]) -> None:
        """Print one result record as a human-readable line to stderr."""
        parts: list[str] = []
        for col in self.columns:
            val = record.get(col, "")
            formatted = _format_value(col, val)
            parts.append(_color_value(col, formatted))

        line = "  ".join(parts)

        try:
            print(line, file=sys.stderr)
        except BrokenPipeError:
            pass
        self._count += 1

        # Track stats for appendix
        name = record.get("name", "")
        if name:
            self._name_counts[name] += 1
        ext = record.get("ext", "")
        if ext:
            self._ext_counts[ext.lstrip(".")] += 1
        size = record.get("size")
        if isinstance(size, (int, float)) and size >= 0:
            self._total_size += int(size)
            self._has_size = True

    def print_appendix(
        self,
        num_results: int,
        total_results: int,
        query: str,
        sort_name: str | None = None,
        descending: bool = False,
    ) -> None:
        """Print appendix with summary statistics and unique filenames."""
        if self._count == 0:
            summary(num_results, total_results, query,
                    sort_name=sort_name, descending=descending)
            return

        _stderr = sys.stderr
        try:
            print("", file=_stderr)  # blank separator

            # ── Header line ──
            num = color.style(f"{num_results:,}", color.BOLD)
            total = color.style(f"{total_results:,}", color.DIM)
            q = color.style(f'"{query}"', color.BOLD)
            header = f"  {num} of {total} results for {q}"
            if sort_name is not None:
                arrow = "\u2193" if descending else "\u2191"
                sort_part = (
                    color.style("\u2502", color.DIM)
                    + "  sorted by "
                    + color.style(sort_name, color.ITALIC)
                    + " " + color.style(arrow, color.DIM)
                )
                header += f"  {sort_part}"
            print(header, file=_stderr)
            print("", file=_stderr)

            # Collect stat lines to determine which get ├ vs └
            stat_lines: list[str] = []

            if self._has_size:
                size_val = color.style(_format_size(self._total_size), color.BOLD + color.YELLOW)
                stat_lines.append(f"size      {size_val}")

            if self._ext_counts:
                top_exts = self._ext_counts.most_common(8)
                ext_parts: list[str] = []
                for e, c in top_exts:
                    ext_parts.append(
                        color.style(f".{e}", color.MAGENTA)
                        + color.style(f"({c})", color.DIM)
                    )
                ext_str = "  ".join(ext_parts)
                if len(self._ext_counts) > 8:
                    ext_str += color.style(
                        f"  \u2026 +{len(self._ext_counts) - 8} more", color.DIM
                    )
                stat_lines.append(f"ext       {ext_str}")

            # Unique filenames
            names = sorted(self._name_counts.keys(), key=str.lower)
            if names:
                display_names: list[str] = []
                for n in names[:15]:
                    cnt = self._name_counts[n]
                    part = color.style(n, color.BOLD_WHITE)
                    if cnt > 1:
                        part += color.style(f"\u00d7{cnt}", color.DIM)
                    display_names.append(part)
                names_str = "  ".join(display_names)
                if len(names) > 15:
                    names_str += color.style(
                        f"  \u2026 +{len(names) - 15} more", color.DIM
                    )
                stat_lines.append(f"names     {names_str}")

            # Print with box-drawing characters
            for i, line in enumerate(stat_lines):
                is_last = i == len(stat_lines) - 1
                branch = "\u2514" if is_last else "\u251c"
                branch_colored = color.style(branch, color.DIM)
                print(f"  {branch_colored} {line}", file=_stderr)

        except BrokenPipeError:
            pass

    @property
    def count(self) -> int:
        return self._count
