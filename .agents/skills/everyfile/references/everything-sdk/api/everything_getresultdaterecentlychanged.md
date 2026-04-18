# Everything_GetResultDateRecentlyChanged

Source: https://www.voidtools.com

# Everything_GetResultDateRecentlyChanged

The **Everything_GetResultDateRecentlyChanged** function retrieves the recently changed date of a visible result.

## Syntax

```
BOOL Everything_GetResultDateRecentlyChanged(
    DWORD dwIndex,
    FILETIME *lpDateRecentlyChanged
);
```

## Parameters

*dwIndex*

Zero based index of the visible result.

*lpDateRecentlyChanged*

Pointer to a FILETIME to hold the recently changed date of the result.

## Return Value

The function returns non-zero if successful.

The function returns 0 if the recently changed date information is unavailable. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetResultDateRecentlyChanged. |

| EVERYTHING_ERROR_INVALIDREQUEST | Recently changed date was not requested or is unavailable, Call [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags) with EVERYTHING_REQUEST_DATE_RECENTLY_CHANGED before calling [Everything_Query](/support/everything/sdk/everything_query). |

| EVERYTHING_ERROR_INVALIDINDEX | index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

dwIndex must be a valid visible result index. To determine if a result index is visible use the [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults) function.

The date recently changed is the date and time of when the result was changed in the Everything index, this could be from a file creation, rename, attribute or content change.

## Example

```
FILETIME dateRecentlyChanged;

// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// Get the recently changed date of the first visible result.
Everything_GetResultDateRecentlyChanged(0,&dateRecentlyChanged);
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)
