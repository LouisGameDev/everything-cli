# Everything_GetResultHighlightedPath

Source: https://www.voidtools.com

# Everything_GetResultHighlightedPath

The **Everything_GetResultHighlightedPath** function retrieves the highlighted path part of the visible result.

**

## Syntax

```
LPCTSTR Everything_GetResultHighlightedPath(
    int index
);
```

## Parameters

*index*

Zero based index of the visible result.

## Return Value

The function returns a pointer to a null terminated string of TCHARs**.

If the function fails the return value is NULL. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetResultHighlightedPath. |

| EVERYTHING_ERROR_INVALIDREQUEST | Highlighted path information was not requested or is unavailable, Call [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags) with EVERYTHING_REQUEST_DATE_HIGHLIGHTED_PATH before calling [Everything_Query](/support/everything/sdk/everything_query). |

| EVERYTHING_ERROR_INVALIDINDEX | index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

The ANSI / Unicode version of this function must match the ANSI / Unicode version of the call to [Everything_Query](/support/everything/sdk/everything_query).

The function returns a pointer to an internal structure that is only valid until the next call to [Everything_Query](/support/everything/sdk/everything_query) or [Everything_Reset](/support/everything/sdk/everything_reset).

You can only call this function for a visible result. To determine if a result is visible use the [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults) function.

Text inside a * quote is highlighted, two consecutive *'s is a single literal *.

For example, in the highlighted text: abc *123* the 123 part is highlighted.

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// Get the highlighted path of the first visible result.
LPCTSTR lpHighlightedPath = Everything_GetResultHighlightedPath(0);
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)
