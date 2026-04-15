# Everything_GetResultAttributes

Source: https://www.voidtools.com

# Everything_GetResultAttributes

The **Everything_GetResultAttributes** function retrieves the attributes of a visible result.

## Syntax

```
DWORD Everything_GetResultAttributes(
    DWORD dwIndex,
);
```

## Parameters

*dwIndex*

Zero based index of the visible result.

## Return Value

The function returns zero or more of FILE_ATTRIBUTE_* flags.

The function returns INVALID_FILE_ATTRIBUTES if attribute information is unavailable. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetResultAttributes. |

| EVERYTHING_ERROR_INVALIDREQUEST | Attribute information was not requested or is unavailable, Call [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags) with EVERYTHING_REQUEST_ATTRIBUTES before calling [Everything_Query](/support/everything/sdk/everything_query). |

| EVERYTHING_ERROR_INVALIDINDEX | index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

dwIndex must be a valid visible result index. To determine if a result index is visible use the [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults) function.

## Example

```
DWORD attributes;

// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// Get the attributes of the first visible result.
attributes = Everything_GetResultAttributes(0);
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)
