# Everything_GetMatchPath

Source: https://www.voidtools.com

# Everything_GetMatchPath

The **Everything_GetMatchPath** function returns the state of the match full path switch.

## Syntax

```
BOOL Everything_GetMatchPath(void);
```

## Return Value

The return value is the state of the match full path switch.

The function returns TRUE if match full path is enabled.

The function returns FALSE if match full path is disabled.

## Remarks

Get the internal state of the match full path switch.

The default state is FALSE, or disabled.

## Example

```
BOOL bEnabled = Everything_GetMatchPath();
```

## See Also

- [Everything_SetMatchPath](/support/everything/sdk/everything_setmatchpath)

- [Everything_Query](/support/everything/sdk/everything_query)
