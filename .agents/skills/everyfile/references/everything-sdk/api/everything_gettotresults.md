# Everything_GetTotResults

Source: https://www.voidtools.com

# Everything_GetTotResults

The **Everything_GetTotResults** function returns the total number of file and folder results.

## Syntax

```
DWORD Everything_GetTotResults(void);
```

## Parameters

This functions has no parameters.

## Return Value

Returns the total number of file and folder results.

If the function fails the return value is 0. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetTotResults. |

## Remarks

You must call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetTotResults.

Use [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults) to retrieve the number of visible file and folder results.

Use the result offset and max result values to limit the number of visible results.

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// get the total number of file and folder results.
DWORD dwTotResults = Everything_GetTotResults();
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults)

- [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults)

- [Everything_GetNumFolderResults](/support/everything/sdk/everything_getnumfolderresults)

- [Everything_GetTotFileResults](/support/everything/sdk/everything_gettotfileresults)

- [Everything_GetTotFolderResults](/support/everything/sdk/everything_gettotfolderresults)
