# Everything_GetMatchCase

Source: https://www.voidtools.com

# Everything_GetMatchCase

The **Everything_GetMatchCase** function returns the match case state.

## Syntax

```
BOOL Everything_GetMatchCase(void);
```

## Return Value

The return value is the match case state.

The function returns TRUE if match case is enabled.

The function returns FALSE if match case is disabled.

## Remarks

Get the internal state of the match case switch.

The default state is FALSE, or disabled.

## Example

```
BOOL bEnabled = Everything_GetMatchCase();
```

## See Also

- [Everything_SetMatchCase](/support/everything/sdk/everything_setmatchcase)

- [Everything_Query](/support/everything/sdk/everything_query)
