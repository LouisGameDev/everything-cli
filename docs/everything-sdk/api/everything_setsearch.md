# Everything_SetSearch

Source: https://www.voidtools.com

# Everything_SetSearch

The **Everything_SetSearch** function sets the search string for the IPC Query.

## Syntax

```
void Everything_SetSearch(
    LPCTSTR lpString
);
```

## Parameters

*lpString* [in]

Pointer to a null-terminated string to be used as the new search text.

## Return Value

This function has no return value.

## Remarks

Optionally call this function prior to a call to [Everything_Query](/support/everything/sdk/everything_query)

[Everything_Query](/support/everything/sdk/everything_query) executes the IPC Query using this search string.

## Example

```
// Set the search string to abc AND 123
Everything_SetSearch("abc 123");

// Execute the IPC query.
Everything_Query(TRUE);
```

## See Also

- [Everything_GetSearch](/support/everything/sdk/everything_getsearch)

- [Everything_Query](/support/everything/sdk/everything_query)
