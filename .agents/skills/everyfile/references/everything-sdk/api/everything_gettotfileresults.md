# Everything_GetTotFileResults

Source: https://www.voidtools.com

# Everything_GetTotFileResults

The **Everything_GetTotFileResults** function returns the total number of file results.

## Syntax

```
DWORD Everything_GetTotFileResults(void);
```

## Parameters

This functions has no parameters.

## Return Value

Returns the total number of file results.

If the function fails the return value is 0. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetTotFileResults. |

## Remarks

You must call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetTotFileResults.

Use [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults) to retrieve the number of visible file results.

Use the result offset and max result values to limit the number of visible results.

Everything_GetTotFileResults is not supported when using [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// get the total number of file results.
DWORD dwTotFileResults = Everything_GetTotFileResults();
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults)

- [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults)

- [Everything_GetNumFolderResults](/support/everything/sdk/everything_getnumfolderresults)

- [Everything_GetTotResults](/support/everything/sdk/everything_gettotresults)

- [Everything_GetTotFolderResults](/support/everything/sdk/everything_gettotfolderresults)
