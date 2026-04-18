---
name: everyfile
description: >
  Use the everyfile (ev) command, Python API, or MCP tools to search files
  instantly on Windows via Voidtools Everything. Use when the user asks to "find
  files", "search for files", "locate a file", "list files by extension", "find
  large files", "find recent files", "find duplicates", or any file discovery
  task on Windows. Also use for programmatic file search from Python code or
  AI assistant tool calls. Do NOT use for Linux/macOS file search or when
  Everything is not installed.
license: MIT
compatibility: >
  Requires Windows, Python >= 3.11, and Voidtools Everything (1.4, 1.5, or 1.5a)
  running in the background.
---

# everyfile

Instant file search on Windows via [Voidtools Everything](https://www.voidtools.com/).
Three interfaces — choose based on context:

| Interface | When to use | Reference |
|-----------|-------------|-----------|
| **CLI** (`ev`) | Terminal commands, shell scripts, piping results between commands | [cli.md](cli.md) |
| **Python API** | Python scripts/tools that need programmatic file search, Cursor/Row iteration | [api.md](api.md) |
| **MCP Tools** | AI assistants calling `search_files`, `count_files`, `get_everything_info` via MCP | [mcp.md](mcp.md) |

For Everything search syntax details beyond this cheat sheet, see the scraped SDK docs in [everything-sdk/](everything-sdk/) (especially [everything-sdk/index.md](everything-sdk/index.md) for search syntax and [everything-sdk/ipc.md](everything-sdk/ipc.md) for IPC internals).

## Decision Guide

- **User asks to find/list files in terminal** → CLI (`ev`)
- **User writes a Python script that needs file search** → API (`from everyfile import search`)
- **You (the agent) need to find files on Windows** → MCP tools (`search_files`, `count_files`)
- **User asks "how many X files?"** → MCP `count_files` or CLI `ev --count`
- **User asks for file contents after search** → CLI `ev -l | ForEach-Object { ... }` or API iteration
- **User asks about Everything status** → MCP `get_everything_info` or CLI `ev --info`

## Install

```powershell
pip install everyfile          # CLI + API
pip install everyfile[mcp]     # + MCP server
```

## Search Syntax (shared across all interfaces)

```
Operators:    space=AND  |=OR  !=NOT  < >=group  " "=exact phrase
Wildcards:    *=any chars  ?=one char
Functions:    ext:py  size:>1mb  dm:today  dc:thisweek  parent:C:\Dev
              content:"TODO"  dupe:  depth:  len:  child:  childcount:
Modifiers:    case:  nocase:  regex:  path:  ww:  file:  folder:
Macros:       audio:  video:  doc:  pic:  zip:  exe:
Size:         size:1kb..10mb  size:>1gb  size:empty  size:tiny..huge
Dates:        dm:today  dm:thisweek  dc:yesterday  da:last2weeks
```

## Safety

- Confirm with the user before piping results into destructive commands
- Use count first (`count_files` / `ev --count` / `count()`) to check scale before bulk operations
- Use `limit`/`-n`/`max_results` when testing queries
- Everything must be running — all interfaces error if it's not
