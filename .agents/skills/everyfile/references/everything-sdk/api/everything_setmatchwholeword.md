# Everything_SetMatchWholeWord

Source: https://www.voidtools.com

# Everything_SetMatchWholeWord

The **Everything_SetMatchWholeWord** function enables or disables matching whole words for the next call to [Everything_Query](/support/everything/sdk/everything_query).

## Syntax

```
void Everything_SetMatchWholeWord(
    BOOL bEnable
);
```

## Parameters

*bEnable*

Specifies whether the search matches whole words, or can match anywhere.

If this parameter is TRUE, the search matches whole words only.

If the parameter is FALSE, the search can occur anywhere.

## Remarks

Match whole word is disabled by default.

## Example

```
Everything_SetMatchWholeWord(TRUE);
```

## See Also

- [Everything_GetMatchWholeWord](/support/everything/sdk/everything_getmatchwholeword)

- [Everything_Query](/support/everything/sdk/everything_query)
