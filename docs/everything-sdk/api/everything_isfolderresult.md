# Everything_IsFolderResult

Source: https://www.voidtools.com

# Everything_IsFolderResult

The **Everything_IsFolderResult** function determines if the visible result is a folder.

## Syntax

```
BOOL Everything_IsFolderResult(
    DWORD index
);
```

## Parameters

*index*

Zero based index of the visible result.

## Return Value

The function returns TRUE, if the visible result is a folder or volume (For example: C: or c:\WINDOWS).

The function returns FALSE, if the visible result is a file (For example: C:\ABC.123).

If the function fails the return value is FALSE. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_IsFolderResult. |

| EVERYTHING_ERROR_INVALIDINDEX | Index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

You can only call this function for a visible result. To determine if a result is visible use the [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults) function.

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// determine if the first visible result is a folder.
BOOL bIsFolderResult = Everything_IsFolderResult(0);
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_IsVolumeResult](/support/everything/sdk/everything_isvolumeresult)

- [Everything_IsFileResult](/support/everything/sdk/everything_isfileresult)
