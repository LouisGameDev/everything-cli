# Everything_GetRegex

Source: https://www.voidtools.com

# Everything_GetRegex

The Everything_GetRegex function returns the regex state.

## Syntax

```
BOOL Everything_GetRegex(void);
```

## Return Value

The return value is the regex state.

The function returns TRUE if regex is enabled.

The function returns FALSE if regex is disabled.

## Remarks

The default state is FALSE.

## Example

```
BOOL bRegex = Everything_GetRegex();
```

## See Also

- [Everything_SetRegex](/support/everything/sdk/everything_setregex)

- [Everything_Query](/support/everything/sdk/everything_query)
