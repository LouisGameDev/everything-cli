# Everything_GetSearch

Source: https://www.voidtools.com

# Everything_GetSearch

The **Everything_GetSearch** function retrieves the search text to use for the next call to [Everything_Query](/support/everything/sdk/everything_query).

## Syntax

```
LPCTSTR Everything_GetSearch(void);
```

## Return Value

The return value is a pointer to the null terminated search string.

The unicode and ansi version must match the call to Everything_SetSearch.

The function will fail if you call Everything_GetSearchA after a call to Everything_SetSearchW

The function will fail if you call Everything_GetSearchW after a call to Everything_SetSearchA

If the function fails, the return value is NULL.

To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Meaning |

| EVERYTHING_ERROR_INVALIDCALL | Mismatched unicode / ansi call. |

## Remarks

Get the internal state of the search text.

The default string is an empty string.

## Example

```
LPCTSTR lpSearchString = Everything_GetSearch();
```

## See Also

- [Everything_SetSearch](/support/everything/sdk/everything_setsearch)

- [Everything_Query](/support/everything/sdk/everything_query)
