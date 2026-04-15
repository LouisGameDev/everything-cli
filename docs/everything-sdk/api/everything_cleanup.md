# Everything_CleanUp

Source: https://www.voidtools.com

# Everything_CleanUp

The **Everything_CleanUp** function frees any allocated memory by the library.

**

## Syntax

```
void Everything_CleanUp(void);
```

## Parameters

This function has no parameters.

## Return Value

This function has no return value.

## Remarks

You should call Everything_CleanUp** to free any memory allocated by the Everything SDK.

Everything_CleanUp should be the last call to the Everything SDK.

Call [Everything_Reset](/support/everything/sdk/everything_reset) to free any allocated memory for the current search and results.

[Everything_Reset](/support/everything/sdk/everything_reset) will also reset the search and result state to their defaults.

Calling [Everything_SetSearch](/support/everything/sdk/everything_setsearch) frees the old search and allocates the new search string.

Calling [Everything_Query](/support/everything/sdk/everything_query) frees the old result list and allocates the new result list.

## Example

```
Everything_CleanUp();
```

## See Also

- [Everything_SetSearch](/support/everything/sdk/everything_setsearch)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_Query](/support/everything/sdk/everything_query)
