# Everything_GetMatchWholeWord

Source: https://www.voidtools.com

# Everything_GetMatchWholeWord

The **Everything_GetMatchWholeWord** function returns the match whole word state.

## Syntax

```
BOOL Everything_GetMatchWholeWord(void);
```

## Return Value

The return value is the match whole word state.

The function returns TRUE if match whole word is enabled.

The function returns FALSE if match whole word is disabled.

## Remarks

The default state is FALSE, or disabled.

## Example

```
BOOL bEnabled = Everything_GetMatchWholeWord();
```

## See Also

- [Everything_SetMatchWholeWord](/support/everything/sdk/everything_setmatchwholeword)

- [Everything_Query](/support/everything/sdk/everything_query)
