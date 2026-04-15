# Everything_Reset

Source: https://www.voidtools.com

# Everything_Reset

The **Everything_Reset** function resets the result list and search state to the default state, freeing any allocated memory by the library.

## Syntax

```
void Everything_Reset(void);
```

## Parameters

This function has no parameters.

## Return Value

This function has no return value.

## Remarks

Calling [Everything_SetSearch](/support/everything/sdk/everything_setsearch) frees the old search and allocates the new search string.

Calling [Everything_Query](/support/everything/sdk/everything_query) frees the old result list and allocates the new result list.

Calling [Everything_Reset](/support/everything/sdk/everything_reset) frees the current search and current result list.

The default state:

```
Everything_SetSearch(\"\");
Everything_SetMatchPath(FALSE);
Everything_SetMatchCase(FALSE);
Everything_SetMatchWholeWord(FALSE);
Everything_SetRegex(FALSE);
Everything_SetMax(0xFFFFFFFF);
Everything_SetOffset(0);
Everything_SetReplyWindow(0);
Everything_SetReplyID(0);
```

## Example

```
Everything_Reset();
```

## See Also

- [Everything_SetSearch](/support/everything/sdk/everything_setsearch)

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_CleanUp](/support/everything/sdk/everything_cleanup)
