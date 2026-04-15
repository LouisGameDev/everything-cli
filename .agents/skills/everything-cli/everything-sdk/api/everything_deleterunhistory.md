# Everything_DeleteRunHistory

Source: https://www.voidtools.com

# Everything_DeleteRunHistory

The **Everything_DeleteRunHistory** function deletes all run history.

## Syntax

```
BOOL Everything_DeleteRunHistory(void);
```

## Parameters

No parameters.

## Return Value

The function returns non-zero if run history is cleared.

The function returns 0 if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

Calling this function will clear all run history from memory and disk.

## Example

```
// clear run history
Everything_DeleteRunHistory();
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_GetRunCountFromFileName](/support/everything/sdk/everything_getruncountfromfilename)

- [Everything_SetRunCountFromFileName](/support/everything/sdk/everything_setruncountfromfilename)

- [Everything_IncRunCountFromFileName](/support/everything/sdk/everything_incruncountfromfilename)
