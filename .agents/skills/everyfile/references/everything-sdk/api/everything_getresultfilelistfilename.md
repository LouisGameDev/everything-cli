# Everything_GetResultFileListFileName

Source: https://www.voidtools.com

# Everything_GetResultFileListFileName

The **Everything_GetResultFileListFileName** function retrieves the file list full path and filename of the visible result.

**

## Syntax

```
LPCTSTR Everything_GetResultFileListFileName(
    DWORD dwIndex
);
```

## Parameters

*dwIndex*

Zero based index of the visible result.

## Return Value

The function returns a pointer to a null terminated string of TCHARs**.

If the function fails the return value is NULL. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

If the result specified by dwIndex is not in a file list, then the filename returned is an empty string.

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetResultFileListFileName. |

| EVERYTHING_ERROR_INVALIDREQUEST | The file list filename was not requested or is unavailable, Call [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags) with EVERYTHING_REQUEST_FILE_LIST_FILE_NAME before calling [Everything_Query](/support/everything/sdk/everything_query). |

| EVERYTHING_ERROR_INVALIDINDEX | index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

The ANSI / Unicode version of this function must match the ANSI / Unicode version of the call to [Everything_Query](/support/everything/sdk/everything_query).

The function returns a pointer to an internal structure that is only valid until the next call to [Everything_Query](/support/everything/sdk/everything_query) or [Everything_Reset](/support/everything/sdk/everything_reset).

dwIndex must be a valid visible result index. To determine if a result is visible use the [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults) function.

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// Get the file list filename of the first visible result.
LPCTSTR lpFileListFileName = Everything_GetResultFileListFileName(0);
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)
