# Everything_SetMatchCase

Source: https://www.voidtools.com

# Everything_SetMatchCase

The **Everything_SetMatchCase** function enables or disables full path matching for the next call to [Everything_Query](/support/everything/sdk/everything_query).

## Syntax

```
void Everything_SetMatchCase(
    BOOL bEnable
);
```

## Parameters

*bEnable*

Specifies whether the search is case sensitive or insensitive.

If this parameter is TRUE, the search is case sensitive.

If the parameter is FALSE, the search is case insensitive.

## Remarks

Match case is disabled by default.

## Example

```
Everything_SetMatchCase(TRUE);
```

## See Also

- [Everything_GetMatchCase](/support/everything/sdk/everything_getmatchcase)

- [Everything_Query](/support/everything/sdk/everything_query)
