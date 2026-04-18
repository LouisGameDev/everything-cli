# Everything_GetResultDateModified

Source: https://www.voidtools.com

# Everything_GetResultDateModified

The **Everything_GetResultDateModified** function retrieves the modified date of a visible result.

## Syntax

```
BOOL Everything_GetResultDateModified(
    DWORD dwIndex,
    FILETIME *lpDateModified
);
```

## Parameters

*dwIndex*

Zero based index of the visible result.

*lpDateModified*

Pointer to a FILETIME to hold the modified date of the result.

## Return Value

The function returns non-zero if successful.

The function returns 0 if the modified date information is unavailable. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetResultDateModified. |

| EVERYTHING_ERROR_INVALIDREQUEST | Modified date was not requested or is unavailable, Call [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags) with EVERYTHING_REQUEST_DATE_MODIFIED before calling [Everything_Query](/support/everything/sdk/everything_query). |

| EVERYTHING_ERROR_INVALIDINDEX | index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

dwIndex must be a valid visible result index. To determine if a result index is visible use the [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults) function.

## Example

```
FILETIME dateModified;

// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// Get the modified date of the first visible result.
Everything_GetResultDateModified(0,&dateModified);
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)
