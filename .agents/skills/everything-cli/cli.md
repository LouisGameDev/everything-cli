# everything-cli — CLI Reference

Shell command for instant file search via Voidtools Everything.
Aliases: `everything`, `every`, `ev`. Use `ev` for brevity.

## Install

```powershell
pip install everything-cli
```

## Search Syntax (passed verbatim to Everything)

```
Operators:    space=AND  |=OR  !=NOT  < >=group  " "=exact phrase
Wildcards:    *=any chars  ?=one char
Functions:    ext:  size:  dm:  dc:  da:  parent:  content:  dupe:
              depth:  len:  child:  childcount:  dr:  rc:
Modifiers:    case:  nocase:  regex:  path:  ww:  file:  folder:
Macros:       audio:  video:  doc:  pic:  zip:  exe:
Size:         size:1kb..10mb  size:>1gb  size:empty  size:tiny..huge
Dates:        dm:today  dm:thisweek  dc:yesterday  da:last2weeks
```

## Output Modes

| Flag | Stdout | When to use |
|------|--------|-------------|
| *(none)* | NDJSON when piped, human table on stderr | Interactive / piping |
| `-l` / `--list` | One full path per line | `ForEach-Object`, subshells |
| `-0` / `--null` | Null-separated paths | Paths with spaces/special chars |
| `-j` / `--json` | Force NDJSON | Structured processing |
| `-q` / `--quiet` | Suppress stderr table | Silent scripts |

## Complex Examples

```powershell
# Large Python files modified this week, biggest first
ev "ext:py size:>50kb dm:thisweek" --sort size -d -n 20

# Duplicate DLLs across all drives (name-only)
ev "dupe: ext:dll" -f name,full_path,size --sort name

# Regex: test files following pytest convention
ev "regex:^test_.*\.py$" --sort modified -d

# Files in a specific subtree (use path: function)
ev "ext:ts path:webapp\src" --sort modified -d -n 50

# Zero-byte placeholder files
ev "size:empty ext:py|ext:js|ext:ts" -f name,full_path

# Recently accessed executables (last 2 weeks)
ev "ext:exe da:last2weeks" --sort accessed -d -n 10 -f name,full_path,date_accessed

# Content search — find Python files containing "async def"
ev 'ext:py content:"async def"' -l

# Count before acting
ev --count "ext:tmp|ext:log dm:>30days"

# Chain filters via pipe composition (local filter, no re-query)
ev ext:py -j | ev "path:src" | ev "!test" | ev "!__pycache__"

# Structured filter on NDJSON stream
ev ext:py -f all -j | ev filter --size-gt 10000 --modified-after 2026-01-01 --is-file

# Extract specific fields
ev ext:py -f all -j | ev pick name size date_modified
```

## Scripting Patterns

```powershell
# Open most recently modified match in VS Code
code $(ev "mcp.py" --sort modified -d -n 1 -l)

# Batch process: lint all Python files modified today
ev "ext:py dm:today" -l | ForEach-Object { pylint $_ }

# Copy large logs to archive
ev "ext:log size:>10mb" -l | ForEach-Object { Move-Item $_ D:\Archive\ }

# Count lines of code in a project subtree
ev "ext:py path:src" -l | ForEach-Object { Get-Content $_ } | Measure-Object -Line

# Search contents of recently changed files
ev "ext:py dm:thisweek" -l | ForEach-Object { Select-String -Path $_ "TODO|FIXME|HACK" }

# JSON pipeline with jq — top 10 largest by size
ev "ext:py" -f name,size -j | jq -s 'sort_by(-.size) | .[0:10] | .[] | "\(.name) \(.size)"'

# Paginate results
ev ext:py -l | Select-Object -Skip 100 -First 25
```

## Fields & Sorting

```powershell
ev ext:py -f name,size,date_modified    # select fields
ev ext:py -f all                        # every field
ev ext:py -f dates                      # group: date_created, date_modified, date_accessed
ev ext:py -f meta                       # group: size, attributes, is_file, is_folder
ev ext:py --columns name,size           # human-readable table columns
ev --help-columns                       # list all available fields
```

Fields: `name` `path` `full_path` `ext` `size` `date_created` `date_modified` `date_accessed` `date_run` `date_recently_changed` `run_count` `attributes` `is_file` `is_folder` `hl_name` `hl_path` `hl_full_path`

Sort: `name` `path` `size` `ext` `created` `modified` `accessed` `run-count` `date-run` `recently-changed` `attributes` — append `-d` for descending.

## Instance Management

```powershell
ev --instances                         # list running instances
ev --instance 1.5a ext:py             # target specific version
$env:EVERYTHING_INSTANCE = "1.5a"     # persist for session
ev --version                          # CLI + Everything version
ev --info                             # service status
```

Priority: `--instance` flag > `$EVERYTHING_INSTANCE` env var > auto-detect (1.5a → 1.5 → 1.4 → default).
