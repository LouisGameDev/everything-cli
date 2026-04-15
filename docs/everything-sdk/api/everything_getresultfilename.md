# Everything_GetResultFileName

Source: https://www.voidtools.com

# Everything_GetResultFileName

The **Everything_GetResultFileName** function retrieves the file name part only of the visible result.

**

## Syntax

```
LPCTSTR Everything_GetResultFileName(
    DWORD index
);
```

## Parameters

*index*

Zero based index of the visible result.

## Return Value

The function returns a pointer to a null terminated string of TCHARs**.

If the function fails the return value is NULL. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetResultFileName. |

| EVERYTHING_ERROR_INVALIDINDEX | index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

The ANSI / Unicode version of this function must match the ANSI / Unicode version of the call to [Everything_Query](/support/everything/sdk/everything_query).

The function is faster than Everything_GetResultFullPathName as no memory copying occurs.

The function returns a pointer to an internal structure that is only valid until the next call to [Everything_Query](/support/everything/sdk/everything_query) or [Everything_Reset](/support/everything/sdk/everything_reset).

You can only call this function for a visible result. To determine if a result is visible use the [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults) function.

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// Get the file name part of the first visible result.
LPCTSTR cFileName = Everything_GetResultFileName(0);
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_GetResultPath](/support/everything/sdk/everything_getresultpath)

- [Everything_GetResultFullPathName](/support/everything/sdk/everything_getresultfullpathname)
