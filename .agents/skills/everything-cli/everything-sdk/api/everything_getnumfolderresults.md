# Everything_GetNumFolderResults

Source: https://www.voidtools.com

# Everything_GetNumFolderResults

The **Everything_GetNumFolderResults** function returns the number of visible folder results.

## Syntax

```
DWORD Everything_GetNumFolderResults(void);
```

## Parameters

This functions has no parameters.

## Return Value

Returns the number of visible folder results.

If the function fails the return value is 0. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetNumFolderResults. |

## Remarks

You must call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetNumFolderResults.

Use [Everything_GetTotFolderResults](/support/everything/sdk/everything_gettotfolderresults) to retrieve the total number of folder results.

If the result offset state is 0, and the max result is 0xFFFFFFFF, Everything_GetNumFolderResults will return the total number of folder results and all folder results will be visible.

Everything_GetNumFolderResults is not supported when using [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// get the number of visible folder results
DWORD dwNumFolderResults = Everything_GetNumFolderResults();
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults)

- [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults)

- [Everything_GetTotResults](/support/everything/sdk/everything_gettotresults)

- [Everything_GetTotFileResults](/support/everything/sdk/everything_gettotfileresults)

- [Everything_GetTotFolderResults](/support/everything/sdk/everything_gettotfolderresults)
