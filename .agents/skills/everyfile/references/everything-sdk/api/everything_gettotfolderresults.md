# Everything_GetTotFolderResults

Source: https://www.voidtools.com

# Everything_GetTotFolderResults

The **Everything_GetTotFolderResults** function returns the total number of folder results.

## Syntax

```
DWORD Everything_GetTotFolderResults(void);
```

## Parameters

This functions has no parameters.

## Return Value

Returns the total number of folder results.

If the function fails the return value is 0. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetTotFolderResults. |

## Remarks

You must call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetTotFolderResults.

Use [Everything_GetNumFolderResults](/support/everything/sdk/everything_getnumfolderresults) to retrieve the number of visible folder results.

Use the result offset and max result values to limit the number of visible results.

Everything_GetTotFolderResults is not supported when using [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// get the total number of folder results.
DWORD dwTotFolderResults = Everything_GetTotFolderResults();
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults)

- [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults)

- [Everything_GetNumFolderResults](/support/everything/sdk/everything_getnumfolderresults)

- [Everything_GetTotResults](/support/everything/sdk/everything_gettotresults)

- [Everything_GetTotFileResults](/support/everything/sdk/everything_gettotfileresults)
