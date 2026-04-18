# Everything_GetResultSize

Source: https://www.voidtools.com

# Everything_GetResultSize

The **Everything_GetResultSize** function retrieves the size of a visible result.

## Syntax

```
BOOL Everything_GetResultSize(
    DWORD dwIndex,
    LARGE_INTEGER *lpSize
);
```

## Parameters

*dwIndex*

Zero based index of the visible result.

*lpSize*

Pointer to a LARGE_INTEGER to hold the size of the result.

## Return Value

The function returns non-zero if successful.

The function returns 0 if size information is unavailable. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetResultSize. |

| EVERYTHING_ERROR_INVALIDREQUEST | Size was not requested or is unavailable, Call [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags) with EVERYTHING_REQUEST_SIZE before calling [Everything_Query](/support/everything/sdk/everything_query). |

| EVERYTHING_ERROR_INVALIDINDEX | index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

dwIndex must be a valid visible result index. To determine if a result index is visible use the [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults) function.

## Example

```
LARGE_INTEGER size;

// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// Get the size of the first visible result.
Everything_GetResultSize(0,&size);
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)
