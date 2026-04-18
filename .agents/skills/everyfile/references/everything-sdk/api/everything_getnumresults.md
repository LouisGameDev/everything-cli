# Everything_GetNumResults

Source: https://www.voidtools.com

# Everything_GetNumResults

The **Everything_GetNumResults** function returns the number of visible file and folder results.

## Syntax

```
DWORD Everything_GetNumResults(void);
```

## Parameters

This functions has no parameters.

## Return Value

Returns the number of visible file and folder results.

If the function fails the return value is 0. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetNumResults. |

## Remarks

You must call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetNumResults.

Use [Everything_GetTotResults](/support/everything/sdk/everything_gettotresults) to retrieve the total number of file and folder results.

If the result offset state is 0, and the max result is 0xFFFFFFFF, Everything_GetNumResults will return the total number of file and folder results and all file and folder results will be visible.

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// get the number of visible file and folder results.
DWORD dwNumResults = Everything_GetNumResults();
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults)

- [Everything_GetNumFolderResults](/support/everything/sdk/everything_getnumfolderresults)

- [Everything_GetTotResults](/support/everything/sdk/everything_gettotresults)

- [Everything_GetTotFileResults](/support/everything/sdk/everything_gettotfileresults)

- [Everything_GetTotFolderResults](/support/everything/sdk/everything_gettotfolderresults)
