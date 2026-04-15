# everything-cli — Design Spec

> Zero-dependency Python CLI for Voidtools Everything search.
> Binds directly to the Everything SDK DLL via ctypes.
> Windows only. Requires Everything running in the background.

---

## 1. Principles

| # | Principle | Detail |
|---|-----------|--------|
| 1 | **Unix-pipe friendly** | Human-readable chrome → stderr. Structured data → stdout as NDJSON. |
| 2 | **Zero runtime deps** | stdlib + ctypes only. No click, no rich, no requests. |
| 3 | **Everything search syntax is the query language** | We pass the query string straight to `Everything_SetSearchW()`. Users get the full power of Everything's search functions (`ext:`, `dm:`, `size:`, `content:`, `dupe:`, regex, wildcards, etc.) without us reinventing it. |
| 4 | **CLI flags for SDK knobs** | Things that are separate SDK calls — sort, pagination, match-case, match-path, request-flags — become CLI flags. These compose with the query string. |
| 5 | **Pipeable filtering** | `everything filter` reads NDJSON from stdin and applies client-side filters. Useful for post-hoc narrowing without re-querying Everything. |
| 6 | **Progressive disclosure** | Simple searches are one-liners. Power features (fields, sort, filter piping) are opt-in. |
| 7 | **Flat, ergonomic CLI** | The tool IS the search — no `search` subcommand. All positional args are the query. Only pipeline utilities (`filter`, `pick`) remain as subcommands since they operate on stdin, not Everything. |

---

## 2. Command Names & Grammar

```
everything  (primary)
every       (alias)
ev          (alias)
```

Both point to the same `everything_cli.__main__:main` entry point.

### Grammar

```
everything [OPTIONS] [QUERY...]         # search (default action)
everything filter [FILTER_OPTIONS]      # stdin NDJSON filter (subcommand)
everything pick FIELD [FIELD...]        # stdin NDJSON field extractor (subcommand)
```

**All positional arguments that aren't a subcommand are joined with spaces to form the Everything search query.** This means:

```bash
every ext:py dm:thisweek        # query = "ext:py dm:thisweek"
every "*.rs"                    # query = "*.rs"
every foo bar baz               # query = "foo bar baz" (AND)
every --sort size ext:py        # flags extracted, query = "ext:py"
```

**No ambiguity**: CLI flags start with `--`/`-`. Everything search syntax never uses `--` prefix. Shell metacharacters (`|`, `!`, `*`, `<`, `>`) need quoting as usual.

```bash
every 'foo|bar'                 # OR — shell quoting needed for pipe
every '!secret'                 # NOT — shell quoting needed for !
every 'size:>1mb'               # function — shell quoting needed for >
every ext:py dm:today           # no special chars — no quoting needed
```

---

## 3. Output Model

### stdout — NDJSON

One JSON object per line. Only requested fields appear. Minimal example:

```jsonl
{"path":"C:\\Dev","name":"app.py","full_path":"C:\\Dev\\app.py"}
{"path":"C:\\Dev","name":"lib.py","full_path":"C:\\Dev\\lib.py"}
```

Extended example (when extra `--fields` requested):

```jsonl
{"path":"C:\\Dev","name":"app.py","full_path":"C:\\Dev\\app.py","ext":".py","size":4096,"date_modified":"2025-03-01T14:22:31Z","is_file":true,"is_folder":false,"attributes":"A"}
```

### stderr — Human-readable

Progress, diagnostics, result count summary, errors. Examples:

```
everything: 1,247 results (of 1,247 total) for "ext:py dm:thisweek"  [sorted by name ↑]
```

```
everything: error: Everything is not running (IPC unavailable)
```

### Field Schema

| NDJSON key | Type | Request flag needed | Notes |
|---|---|---|---|
| `name` | string | FILE_NAME (default) | Filename only |
| `path` | string | PATH (default) | Parent directory |
| `full_path` | string | FULL_PATH_AND_FILE_NAME | Convenience; always derivable from path + name |
| `ext` | string | EXTENSION | Includes dot: `.py` |
| `size` | int | SIZE | Bytes |
| `date_created` | string | DATE_CREATED | ISO 8601 UTC |
| `date_modified` | string | DATE_MODIFIED | ISO 8601 UTC |
| `date_accessed` | string | DATE_ACCESSED | ISO 8601 UTC |
| `date_run` | string | DATE_RUN | ISO 8601 UTC |
| `date_recently_changed` | string | DATE_RECENTLY_CHANGED | ISO 8601 UTC |
| `attributes` | string | ATTRIBUTES | Compact string: `"RHSA"` etc. |
| `run_count` | int | RUN_COUNT | Times opened from Everything |
| `is_file` | bool | *(derived)* | From `Everything_IsFileResult()` |
| `is_folder` | bool | *(derived)* | From `Everything_IsFolderResult()` |
| `hl_name` | string | HIGHLIGHTED_FILE_NAME | `*matched*` markers |
| `hl_path` | string | HIGHLIGHTED_PATH | `*matched*` markers |
| `hl_full_path` | string | HIGHLIGHTED_FULL_PATH_AND_FILE_NAME | `*matched*` markers |

`name` and `path` are always included (they're the SDK default and essentially free).

---

## 4. CLI Interface

### 4.1 Search (default action)

All positional args form the query. Flags control SDK behavior.

```bash
every <query>                           # basic
every ext:py dm:thisweek                # Everything functions
every "*.rs" --sort size --desc -n 50   # with options
every ext:py -c -r                      # case-sensitive + regex
```

#### Search modifier flags

Shortcuts for SDK calls. Compose with (and override) inline modifiers in the query string.

| Flag | Short | SDK call | Default |
|------|-------|----------|---------|
| `--case` | `-c` | `SetMatchCase(TRUE)` | off |
| `--path` | `-p` | `SetMatchPath(TRUE)` | off (filename only) |
| `--whole-word` | `-w` | `SetMatchWholeWord(TRUE)` | off |
| `--regex` | `-r` | `SetRegex(TRUE)` | off |

> Users can also use inline `case:`, `regex:`, `path:`, `ww:` in the query. CLI flags are convenience aliases. If both are used, the SDK-level flag wins for the whole query.

#### Pagination flags

| Flag | Short | SDK call | Default |
|------|-------|----------|---------|
| `--max <n>` | `-n` | `SetMax(n)` | unlimited |
| `--offset <n>` | | `SetOffset(n)` | 0 |

#### Sort flags

| Flag | Short | Description |
|------|-------|-------------|
| `--sort <field>` | `-s` | Sort field (see table below) |
| `--desc` | `-d` | Descending order (default: ascending) |

Sort field names (mapped to `EVERYTHING_SORT_*` constants):

| `--sort` value | SDK constant |
|----------------|-------------|
| `name` | SORT_NAME (default, instant) |
| `path` | SORT_PATH |
| `size` | SORT_SIZE |
| `ext` | SORT_EXTENSION |
| `created` | SORT_DATE_CREATED |
| `modified` | SORT_DATE_MODIFIED |
| `accessed` | SORT_DATE_ACCESSED |
| `run-count` | SORT_RUN_COUNT |
| `date-run` | SORT_DATE_RUN |
| `recently-changed` | SORT_DATE_RECENTLY_CHANGED |
| `attributes` | SORT_ATTRIBUTES |

#### Field selection

| Flag | Short | Description |
|------|-------|-------------|
| `--fields <f1,f2,...>` | `-f` | Comma-separated list of fields to include in output |

Field names match the NDJSON keys from §3. Special values:

| Value | Expands to |
|-------|-----------|
| `default` | `name,path` |
| `all` | Every available field |
| `dates` | `date_created,date_modified,date_accessed` |
| `meta` | `size,ext,attributes,is_file,is_folder` |
| `highlight` / `hl` | `hl_name,hl_path,hl_full_path` |

Combinable: `--fields default,size,date_modified`

When a field is requested, we automatically set the corresponding `EVERYTHING_REQUEST_*` flag.

#### Mode flags (instead of subcommands)

| Flag | Description |
|------|-------------|
| `--count` | Print only the total count to stdout (`{"total": N}`) and exit |
| `--version` | Print version info and exit |
| `--info` | Print Everything service status and exit |

#### Output control

| Flag | Short | Description |
|------|-------|-------------|
| `--quiet` | `-q` | Suppress stderr summary |

---

### 4.2 `everything filter` (subcommand)

Client-side NDJSON filter. Reads stdin, writes matching records to stdout. This is the one subcommand — it doesn't query Everything, it processes piped NDJSON.

```bash
every ext:py --fields all | every filter --size-gt 10000 --name "test*"
every "*.log" -f default,size | every filter --ext .log --modified-after 2025-01-01
```

#### Filter flags

| Flag | Description | Operates on |
|------|-------------|-------------|
| `--name <glob>` | Glob match on `name` field | `name` |
| `--path <glob>` | Glob match on `path` field | `path` |
| `--ext <.ext>` | Exact extension match | `ext` |
| `--size-gt <n>` | Size greater than N bytes | `size` |
| `--size-lt <n>` | Size less than N bytes | `size` |
| `--modified-after <iso>` | Modified after date | `date_modified` |
| `--modified-before <iso>` | Modified before date | `date_modified` |
| `--created-after <iso>` | Created after date | `date_created` |
| `--created-before <iso>` | Created before date | `date_created` |
| `--is-file` | Only files | `is_file` |
| `--is-folder` | Only folders | `is_folder` |
| `--attr <chars>` | Has all specified attribute chars | `attributes` |

**Missing field behavior**: If a filter references a field not present in the NDJSON record, the record is **skipped** and a warning is emitted to stderr on first occurrence.

Multiple filters are ANDed together.

---

### 4.3 `everything pick` (subcommand)

Extract specific fields from piped NDJSON. Like `jq '{full_path, size}'` but zero-dep.

```bash
every ext:py -f all | every pick full_path size
```

---

### 4.4 Mode flags in detail

#### `--version`

```bash
every --version
```

stderr: `everything-cli 0.1.0 (Python 3.13.5) / Everything 1.4.1.1024`

#### `--info`

```bash
every --info
```

stderr:
```
Everything v1.4.1.1024 (x64)
Database: loaded
Admin: no
AppData: yes
```

stdout NDJSON:
```json
{"major":1,"minor":4,"revision":1,"build":1024,"target":"x64","db_loaded":true,"is_admin":false,"is_appdata":true}
```

#### `--count`

```bash
every --count ext:py dm:thisweek
```

stdout: `{"total": 42}`
stderr: `everything: 42 results for "ext:py dm:thisweek"`

---

## 5. Search Syntax — Design Decision

### Decision: **Pass-through + CLI flag shortcuts**

We do **NOT** parse or transform the Everything search syntax. The query string is passed verbatim to `Everything_SetSearchW()`.

**Why this is right:**
1. Everything's search syntax is rich and well-documented (operators, functions, modifiers, wildcards, regex, macros).
2. Attempting to mirror it in CLI flags would be incomplete and confusing.
3. Existing Everything users already know the syntax.
4. The SDK handles all parsing server-side.

**What CLI flags add:**
- SDK-level knobs that don't exist in the query string: `--sort`, `--max`, `--offset`, `--fields`
- Convenience aliases for search modifiers: `--case`, `--regex`, `--path`, `--whole-word`
  - These are equivalent to prefixing `case:`, `regex:`, `path:`, `ww:` in the query
  - But CLI flags are discoverable via `--help` and tab-completion

**Everything search syntax cheat sheet** (for `--help` text and README):

```
Operators:     space=AND  |=OR  !=NOT  < >=group  " "=exact phrase
Wildcards:     *=any chars  ?=one char
Functions:     ext:py  size:>1mb  dm:today  parent:C:\Dev  content:TODO
               dc: da: dr: rc: depth: len: dupe: child: childcount:
               width: height: dimensions: orientation: bitdepth:
               artist: album: title: genre: comment: track: year:
Modifiers:     case: nocase: regex: noregex: path: nopath: ww: noww:
               file: folder: wholefilename: wildcards: ascii: diacritics:
Macros:        audio: video: doc: pic: zip: exe:
Size:          size:1kb..10mb  size:>1gb  size:empty  size:tiny..huge
Dates:         dm:today  dm:thisweek  dm:lastmonth  dm:2024  dm:2024-01..2024-06
               dc:yesterday  da:last2weeks  dr:thisyear
Regex:         regex:^test.*\.py$
Content:       content:TODO  utf8content:fixme
Duplicates:    dupe:  sizedupe:  dmdupe:  namepartdupe:
```

---

## 6. Piping Patterns

### Basic search
```bash
every ext:py dm:thisweek
```

### Search with extra fields, pipe to jq
```bash
every ext:py -f default,size,date_modified | jq 'select(.size > 5000)'
```

### Chain search → filter (zero-dep alternative to jq)
```bash
every ext:py -f all | every filter --size-gt 5000 --modified-after 2025-01-01
```

### Feed file paths to another tool
```bash
every ext:py parent:C:\Dev | jq -r .full_path | xargs wc -l
```

### Count results
```bash
every --count ext:py dm:today
```

### Search → pick specific fields → downstream
```bash
every ext:log -f all | every pick full_path size date_modified | head -20
```

### Combine with PowerShell
```powershell
every ext:py -f default,size | ConvertFrom-Json | Where-Object { $_.size -gt 10000 } | Format-Table
```

---

## 7. Architecture (src/ layout)

```
src/
  everything_cli/
    __init__.py
    __main__.py          # entry point, argparse, dispatches to search/filter/pick
    search.py            # core search logic (default action, --count, --info, --version)
    filter.py            # filter subcommand (stdin NDJSON processing)
    pick.py              # pick subcommand (stdin NDJSON field extraction)
    sdk/
      __init__.py
      dll.py             # ctypes DLL loader + auto-detect 32/64-bit
      constants.py       # All EVERYTHING_* constants
      api.py             # Pythonic wrappers around DLL functions
      types.py           # FILETIME conversion, result dataclasses
    output/
      __init__.py
      ndjson.py          # NDJSON serializer (stdout)
      human.py           # Human-readable formatter (stderr)
    util/
      __init__.py
      glob.py            # Glob matching for filter command
      dates.py           # FILETIME ↔ ISO 8601 conversion
      attrs.py           # FILE_ATTRIBUTE_* ↔ compact string
```

---

## 8. DLL Loading Strategy

1. Check `EVERYTHING_SDK_DLL` env var (explicit override).
2. Check if `Everything64.dll` / `Everything32.dll` exists beside the CLI (bundled).
3. Check `C:\EverythingSDK\DLL\` (common manual install location).
4. Check Everything's install directory from registry.
5. Fall back to `ctypes.util.find_library("Everything64")`.

Auto-detect 32 vs 64 bit via `platform.architecture()` or `struct.calcsize("P") * 8`.

---

## 9. Error Handling

| Condition | stderr message | Exit code |
|-----------|---------------|-----------|
| Everything not running | `error: Everything is not running (IPC unavailable)` | 2 |
| DLL not found | `error: Everything SDK DLL not found. Set EVERYTHING_SDK_DLL or install the SDK.` | 3 |
| Invalid CLI arguments | `error: ...` (argparse default) | 1 |
| Query returns 0 results | *(no error, just empty stdout, stderr says "0 results")* | 0 |
| Filter stdin not NDJSON | `error: stdin line N: invalid JSON` | 4 |
| Missing field for filter | `warning: field 'size' not present in input, skipping record` (first occurrence only) | 0 |

---

## 10. Open Questions / Discussion Points

### Q1: Should `--fields all` be the default?
- **Pro**: Maximum data, users can filter down.
- **Con**: Triggers v2 IPC (slower), more output to parse, noisier.
- **Current decision**: Default is `name,path` (fastest v1 query). `--fields all` opt-in.

### Q2: Should we support `--format table` for human-readable stdout?
- Could do `--format ndjson|table|csv|paths`.
- `paths` would just emit one `full_path` per line — useful for `xargs`.
- **Current decision**: Defer. NDJSON first. Mention in plan as v2 feature.

### Q3: Stream vs batch output?
- Stream: Emit NDJSON lines as we iterate results (lower latency, pipeable).
- Batch: Collect all, then emit (allows client-side sorting, progress bars).
- **Current decision**: Stream. We already have `--sort` via SDK, and streaming plays better with pipes.

### Q4: Should `filter` support regex on field values?
- e.g., `--name-regex "test_.*\.py$"`
- **Current decision**: Start with glob. Add regex later if needed.

### Q5: Highlighted output — useful?
- The SDK provides `*match*` markers in highlighted fields.
- We could parse these for terminal coloring on stderr.
- **Current decision**: Expose raw `hl_*` fields in NDJSON. Terminal coloring is a v2 feature.

### Q6: `--json-pretty` flag?
- Emit indented JSON instead of NDJSON for human reading.
- **Current decision**: No. Use `| jq .` or `| python -m json.tool`. Keep stdout strictly NDJSON.

### Q7: Full path always included?
- **Option A**: Always include `full_path` alongside `name`+`path` (derivable but convenient).
- **Option B**: Only when explicitly requested via `--fields`.
- **Current decision**: Option A — always include `full_path` in output. It's cheap (string concat of `path` + `\` + `name`).

---

## 11. Testing Strategy

- **Unit tests**: Mock the DLL calls, test CLI argument parsing, NDJSON output, filter logic, field selection, FILETIME conversion.
- **Integration tests**: Require Everything running. Marked with `@pytest.mark.integration`. Test actual DLL binding, search, result iteration.
- **Smoke tests**: `everything info` and `everything version` as basic health checks.
- Test framework: `pytest` (dev dependency only).

---

## 12. Dev Dependencies (pyproject.toml `[project.optional-dependencies]`)

```toml
[project.optional-dependencies]
dev = ["pytest", "ruff", "mypy"]
```

No runtime dependencies.
