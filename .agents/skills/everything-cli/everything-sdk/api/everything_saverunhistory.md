# Everything_SaveRunHistory

Source: https://www.voidtools.com

# Everything_SaveRunHistory

The **Everything_SaveRunHistory** function requests Everything to save the run history to disk.

**

## Syntax

```
BOOL Everything_SaveRunHistory(void);
```

## Parameters

No parameters.

## Return Value

The function returns non-zero if the request to save the run history to disk was successful.

The function returns 0 if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

The run history is only saved to disk when you close an Everything search window or exit Everything.

Call Everything_RunHistory** to write the run history to the file: Run History.csv

## Example

```
// flush run history to disk
Everything_SaveRunHistory();
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also
