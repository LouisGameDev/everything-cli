# Everything_GetResultExtension

Source: https://www.voidtools.com

# Everything_GetResultExtension

The **Everything_GetResultExtension** function retrieves the extension part of a visible result.

**

## Syntax

```
LPCTSTR Everything_GetResultExtension(
    DWORD dwIndex
);
```

## Parameters

*dwIndex*

Zero based index of the visible result.

## Return Value

The function returns a pointer to a null terminated string of TCHARs**.

If the function fails the return value is NULL. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetResultExtension. |

| EVERYTHING_ERROR_INVALIDREQUEST | Extension was not requested or is unavailable, Call [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags) with EVERYTHING_REQUEST_EXTENSION before calling [Everything_Query](/support/everything/sdk/everything_query). |

| EVERYTHING_ERROR_INVALIDINDEX | index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

The ANSI / Unicode version of this function must match the ANSI / Unicode version of the call to [Everything_Query](/support/everything/sdk/everything_query).

The function returns a pointer to an internal structure that is only valid until the next call to [Everything_Query](/support/everything/sdk/everything_query), [Everything_Reset](/support/everything/sdk/everything_reset) or [Everything_CleanUp](/support/everything/sdk/everything_cleanup).

You can only call this function for a visible result. To determine if a result is visible use the [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults) function.

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// Get the extension part of the first visible result.
LPCTSTR lpExtension = Everything_GetResultExtension(0);
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)
