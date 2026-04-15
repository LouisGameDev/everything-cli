"""everything-cli MCP server.

Exposes Voidtools Everything file search to AI assistants via the
Model Context Protocol (MCP).  Requires ``pip install everything-cli[mcp]``.

Transport: stdio (default).  Launch with ``everything-mcp`` or
``python -m everything_cli.mcp``.
"""

from __future__ import annotations

import json
from typing import Annotated

from mcp.server.fastmcp import FastMCP
from pydantic import Field

from everything_cli import Everything, EverythingError

mcp = FastMCP(
    "everything",
    instructions="Search files instantly on Windows via Voidtools Everything",
)

MAX_RESULTS_CAP = 10_000
DEFAULT_MAX_RESULTS = 200


@mcp.tool()
def search_files(
    query: Annotated[str, Field(description='Everything search expression. Supports wildcards (*.py), extensions (ext:rs|go), size filters (size:>1mb), date filters (dm:today, dm:thisweek), path filters (parent:C:\\Dev), boolean (foo bar = AND, foo|bar = OR, !foo = NOT), content search (content:"TODO"), and duplicates (dupe:).')],
    fields: Annotated[str | None, Field(description='Comma-separated field names to include in results. Options: name, path, full_path, ext, size, date_created, date_modified, date_accessed, attributes, is_file, is_folder, run_count. Groups: "all", "meta", "dates", "highlight". Default: name, path, full_path, date_modified.')] = None,
    sort: Annotated[str, Field(description='Sort field: name, path, size, ext, created, modified, accessed, run-count, date-run, recently-changed, attributes.')] = "name",
    descending: Annotated[bool, Field(description='Reverse sort order.')] = False,
    max_results: Annotated[int, Field(description='Maximum number of results to return (capped at 10,000).')] = DEFAULT_MAX_RESULTS,
    offset: Annotated[int, Field(description='Skip first N results for pagination.')] = 0,
    match_case: Annotated[bool, Field(description='Case-sensitive search.')] = False,
    match_path: Annotated[bool, Field(description='Match against full path, not just filename.')] = False,
    match_whole_word: Annotated[bool, Field(description='Match whole words only.')] = False,
    regex: Annotated[bool, Field(description='Interpret query as a regular expression.')] = False,
) -> str:
    """Search for files and folders instantly across all indexed drives using Voidtools Everything."""
    limit = min(max_results, MAX_RESULTS_CAP)
    try:
        ev = Everything()
        cursor = ev.search(
            query,
            fields=fields,
            sort=sort,
            descending=descending,
            limit=limit,
            offset=offset,
            match_case=match_case,
            match_path=match_path,
            match_whole_word=match_whole_word,
            regex=regex,
        )
        lines = [json.dumps(row.to_dict(), ensure_ascii=False) for row in cursor]
        lines.append(
            f"\nFound {cursor.count:,} results (of {cursor.total:,} total matches)"
        )
        return "\n".join(lines)
    except EverythingError as exc:
        raise _mcp_error(exc) from exc


@mcp.tool()
def count_files(
    query: Annotated[str, Field(description='Everything search expression (same syntax as search_files).')],
    match_case: Annotated[bool, Field(description='Case-sensitive search.')] = False,
    match_path: Annotated[bool, Field(description='Match against full path, not just filename.')] = False,
    match_whole_word: Annotated[bool, Field(description='Match whole words only.')] = False,
    regex: Annotated[bool, Field(description='Interpret query as a regular expression.')] = False,
) -> str:
    """Count files/folders matching a query without returning results. Use to check result scale before fetching."""
    try:
        ev = Everything()
        total = ev.count(
            query,
            match_case=match_case,
            match_path=match_path,
            match_whole_word=match_whole_word,
            regex=regex,
        )
        return f'{total:,} files/folders match "{query}"'
    except EverythingError as exc:
        raise _mcp_error(exc) from exc


@mcp.tool()
def get_everything_info() -> str:
    """Get Everything service status, version, and diagnostics.

    Returns version info, target architecture, database status,
    and privilege level.  Useful for checking if Everything is running
    and healthy.
    """
    try:
        ev = Everything()
        info = ev.info
        v = info["version"]
        inst = ev.instance_name

        parts = [f'Everything v{v} (instance: "{inst}")']

        if info.get("target") is not None:
            parts.append(f'Target: {info["target"]}')
        if info.get("db_loaded") is not None:
            parts.append(f'Database loaded: {"yes" if info["db_loaded"] else "no"}')
        parts.append(f'Running as admin: {"yes" if info.get("is_admin") else "no"}')
        parts.append(f'Using AppData: {"yes" if info.get("is_appdata") else "no"}')

        return "\n".join(parts)
    except EverythingError as exc:
        raise _mcp_error(exc) from exc


def _mcp_error(exc: EverythingError) -> Exception:
    """Convert an EverythingError to an MCP-friendly exception."""
    from mcp.server.fastmcp.exceptions import ToolError

    return ToolError(str(exc))


def main() -> None:
    """Entry point for ``everything-mcp`` command."""
    import sys

    if sys.stdin.isatty():
        print(
            "everything-mcp: MCP server for Everything file search\n"
            "\n"
            "This is a stdio MCP server — it expects JSON-RPC on stdin\n"
            "and is meant to be launched by an MCP client, not run directly.\n"
            "\n"
            "Add to your MCP client config:\n"
            "\n"
            '  { "mcpServers": { "everything": { "command": "everything-mcp" } } }\n'
            "\n"
            "Or test with:  echo '{...}' | everything-mcp",
            file=sys.stderr,
        )
        sys.exit(0)
    mcp.run()


if __name__ == "__main__":
    main()
