# Everything_GetNumFileResults

Source: https://www.voidtools.com

# Everything_GetNumFileResults

The **Everything_GetNumFileResults** function returns the number of visible file results.

## Syntax

```
DWORD Everything_GetNumFileResults(void);
```

## Parameters

This functions has no parameters.

## Return Value

Returns the number of visible file results.

If the function fails the return value is 0. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetNumFileResults. |

## Remarks

You must call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetNumFileResults.

Use [Everything_GetTotFileResults](/support/everything/sdk/everything_gettotfileresults) to retrieve the total number of file results.

If the result offset state is 0, and the max result is 0xFFFFFFFF, Everything_GetNumFileResults will return the total number of file results and all file results will be visible.

Everything_GetNumFileResults is not supported when using [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// get the number of visible file results.
DWORD dwNumFileResults = Everything_GetNumFileResults();
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults)

- [Everything_GetNumFolderResults](/support/everything/sdk/everything_getnumfolderresults)

- [Everything_GetTotResults](/support/everything/sdk/everything_gettotresults)

- [Everything_GetTotFileResults](/support/everything/sdk/everything_gettotfileresults)

- [Everything_GetTotFolderResults](/support/everything/sdk/everything_gettotfolderresults)
