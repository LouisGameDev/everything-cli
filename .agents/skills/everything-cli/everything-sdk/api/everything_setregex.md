# Everything_SetRegex

Source: https://www.voidtools.com

# Everything_SetRegex

The Everything_SetRegex function enables or disables Regular Expression searching.

## Syntax

```
void Everything_SetRegex(
    BOOL bEnabled
);
```

## Parameters

*bEnabled*

Set to non-zero to enable regex, set to zero to disable regex.

## Return Value

This function has no return value.

## Remarks

Regex is disabled by default.

## Example

```
Everything_SetRegex(TRUE);
```

## See Also

- [Everything_GetRegex](/support/everything/sdk/everything_getregex)

- [Everything_Query](/support/everything/sdk/everything_query)
