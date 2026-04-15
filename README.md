# everything-cli

Zero-dependency Python CLI for [Voidtools Everything](https://www.voidtools.com/) search. Communicates with Everything via pure Python IPC (ctypes `SendMessageW` / `WM_COPYDATA`) — no DLL required.

```
ev ext:py dm:thisweek              # recent Python files
ev ext:py -n 10                    # 10 most recently modified .py files
ev ext:py --sort size -d           # largest Python files first
ev ext:py -l | xargs wc -l        # line count of every Python file
ev ext:py | ev "path:src"          # chain filters via pipes
```

## Features

- **Instant search** — queries Everything's indexed database, returns results in milliseconds
- **Unix-pipe friendly** — human-readable output on stderr, NDJSON on stdout when piped
- **Pipe composition** — chain `ev` commands to filter results without re-querying
- **Zero dependencies** — stdlib + ctypes only, no DLL needed
- **Everything search syntax** — full pass-through (`ext:`, `dm:`, `size:`, `content:`, `dupe:`, regex, wildcards, macros)
- **Multi-instance support** — works with Everything 1.4, 1.5, and 1.5a side by side

## Requirements

- **Windows** (Everything uses Windows IPC)
- **Python ≥ 3.11**
- **[Voidtools Everything](https://www.voidtools.com/downloads/)** running in the background (1.4, 1.5, or 1.5a)

## Installation

```bash
pip install everything-cli
```

Or install from source:

```bash
pip install git+https://github.com/your-repo/everything-cli.git
```

This registers three commands: `everything`, `every`, and `ev`.

## Quick Start

```bash
# Search for files
ev ext:py                          # all Python files
ev ext:py dm:today                 # Python files modified today
ev "*.config" parent:C:\Dev        # config files under C:\Dev

# Limit and sort
ev ext:py -n 5                     # 5 most recently modified (default sort)
ev ext:py --sort size -d           # largest first
ev ext:py --offset 10 -n 5         # skip first 10, show next 5

# Search modifiers
ev ext:py -c                       # case-sensitive
ev ext:py -r                       # regex mode
ev ext:py -p                       # match against full path
ev ext:py -w                       # whole word only

# Count only
ev --count ext:py                  # just the total count
```

## Output Modes

By default, `ev` prints a human-readable table to **stderr** and NDJSON to **stdout** when piped.

| Flag | Description |
|------|-------------|
| *(default)* | Human table on stderr + NDJSON on stdout when piped |
| `-j` / `--json` | Force NDJSON to stdout even on a terminal |
| `-l` / `--list` | Newline-separated full paths (for `xargs`, `$(...)`) |
| `-0` / `--null` | Null-separated full paths (for `xargs -0`) |
| `-q` / `--quiet` | Suppress all stderr output |

```bash
# Open first match in VS Code
code $(ev myfile.py -n 1 -l)

# Feed to xargs
ev ext:log -l | xargs rm

# Null-safe xargs
ev ext:tmp -0 | xargs -0 rm

# PowerShell foreach
ev ext:py -l | ForEach-Object { code $_ }

# Select a range
ev ext:py -l | Select-Object -Skip 5 -First 3      # PowerShell
ev ext:py -l | sed -n '6,8p'                         # bash
```

## Columns & Fields

`--columns` controls the human-readable stderr display. `-f` / `--fields` controls NDJSON output fields.

```bash
ev ext:py -f name,size             # display and NDJSON: name + size
ev ext:py -f all                   # all fields in NDJSON
ev ext:py -f dates,meta            # groups: default + dates + metadata
ev ext:py --columns name,size      # custom stderr display, default NDJSON
```

Run `ev --help-columns` for the full list:

```
available columns:
  * name                      file or folder name
  * path                      parent directory path
    full_path                 complete path including filename
    ext                       file extension (without dot)
    size                      file size in bytes
    date_created              creation timestamp
  * date_modified             last modified timestamp
    date_accessed             last accessed timestamp
    date_run                  last run timestamp
    date_recently_changed     recently changed timestamp
    run_count                 number of times file was executed
    attributes                file system attributes string
    is_file                   true if result is a file (derived)
    is_folder                 true if result is a folder (derived)
    hl_name                   highlighted matching name
    hl_path                   highlighted matching path
    hl_full_path              highlighted matching full path

  * = included in default display

groups (use with -f):
    default      name, path
    all          every available column
    dates        date_created, date_modified, date_accessed
    meta         size, ext, attributes, is_file, is_folder
    hl           hl_name, hl_path, hl_full_path
```

## Sorting

Default sort is **date modified descending** (newest first), so `-n 5` gives the 5 most recently modified matches.

```bash
ev ext:py                          # newest first (default)
ev ext:py --sort name              # alphabetical
ev ext:py --sort size -d           # largest first
ev ext:py --sort created           # oldest created first
```

Sort fields: `name`, `path`, `size`, `ext`, `created`, `modified`, `accessed`, `run-count`, `date-run`, `recently-changed`, `attributes`.

## Pipe Composition

When stdin is piped NDJSON, `ev` automatically switches to **local filter mode** — no Everything query needed:

```bash
ev ext:py | ev "path:src"              # filter by path
ev ext:py | ev "name:test"             # filter by name
ev ext:py | ev "!__pycache__"          # exclude results
ev ext:py | ev "path:src" | ev "!test" # chain multiple filters
```

Use `-S` / `--search` to force an Everything query even with piped input.

### `ev filter` — Structured Filtering

For typed filtering on NDJSON fields (alternative to `jq`):

```bash
ev ext:py -f all | ev filter --size-gt 5000
ev ext:py -f all | ev filter --modified-after 2025-01-01 --is-file
ev ext:py -f all | ev filter --name "test*" --ext .py
```

| Flag | Description |
|------|-------------|
| `--name GLOB` | Glob match on name |
| `--path GLOB` | Glob match on path |
| `--ext .EXT` | Exact extension match |
| `--size-gt N` | Size > N bytes |
| `--size-lt N` | Size < N bytes |
| `--modified-after DATE` | Modified after ISO date |
| `--modified-before DATE` | Modified before ISO date |
| `--created-after DATE` | Created after ISO date |
| `--created-before DATE` | Created before ISO date |
| `--is-file` | Only files |
| `--is-folder` | Only folders |
| `--attr CHARS` | Require attribute chars (e.g. `RHA`) |

### `ev pick` — Field Extraction

Extract specific fields from NDJSON (like `jq` but zero-dep):

```bash
ev ext:py -f all | ev pick full_path size
ev ext:py -f all | ev pick name date_modified
```

## Everything Search Syntax

The query is passed verbatim to Everything. Full syntax reference:

```
Operators:    space=AND  |=OR  !=NOT  < >=group  " "=exact phrase
Wildcards:    *=any chars  ?=one char
Functions:    ext:py  size:>1mb  dm:today  parent:C:\Dev  content:TODO
              dc: da: dr: rc: depth: len: dupe: child: childcount:
Modifiers:    case: nocase: regex: path: ww: file: folder:
Macros:       audio: video: doc: pic: zip: exe:
Size:         size:1kb..10mb  size:>1gb  size:empty  size:tiny..huge
Dates:        dm:today  dm:thisweek  dc:yesterday  da:last2weeks
```

Shell metacharacters need quoting:

```bash
ev 'foo|bar'              # OR (quote the pipe)
ev '!secret'              # NOT (quote the bang)
ev 'size:>1mb'            # function (quote the >)
ev ext:py dm:today        # no special chars — no quoting needed
```

## Instance Management

Multiple Everything versions can run side-by-side. The CLI auto-detects instances in priority order: `1.5a → 1.5 → 1.4 → default`.

```bash
ev --instances                              # list running instances
ev --instance 1.4 ext:py                    # query via Everything 1.4

# Persist your choice
$env:EVERYTHING_INSTANCE = "1.5a"           # PowerShell (session)
export EVERYTHING_INSTANCE=1.5a             # bash/zsh (session)
```

Priority: `--instance` flag > `$EVERYTHING_INSTANCE` env var > auto-detect.

## Service Info

```bash
ev --version                # CLI + Everything version
ev --info                   # Everything service status
```

## Architecture

```
src/everything_cli/
  __main__.py        CLI entry point, argparse, dispatch
  search.py          Search orchestration, pipe filter, count, info, version
  filter.py          Structured NDJSON filter (ev filter)
  pick.py            NDJSON field extraction (ev pick)
  querymatch.py      Local query matching for pipe composition
  sdk/
    ipc.py           Pure Python IPC via ctypes (WM_COPYDATA, WM_USER)
    api.py           High-level API wrapper, instance resolution
    constants.py     Everything IPC constants, request flags, sort types
    types.py         Field-to-flag mapping, field groups, resolution
  output/
    ndjson.py        NDJSON serializer (stdout)
    human.py         Human-readable formatter (stderr)
  util/
    glob.py          Glob matching for filter command
    dates.py         FILETIME ↔ ISO 8601 conversion
    attrs.py         FILE_ATTRIBUTE_* ↔ compact string
```

**IPC approach**: Pure Python ctypes — `FindWindowW` to locate Everything's hidden IPC window, `SendMessageW` with `WM_COPYDATA` for search queries, `WM_USER` for version/info. No DLL dependency.

## Development

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"

# Lint
ruff check src/

# Type check
mypy src/

# Test (requires Everything running for integration tests)
pytest
```

## See Also

- [Everything SDK Python documentation](https://www.voidtools.com/support/everything/sdk/python/)
- [Everything search syntax](https://www.voidtools.com/support/everything/searching/)
- [Everything downloads](https://www.voidtools.com/downloads/)

## License

MIT
