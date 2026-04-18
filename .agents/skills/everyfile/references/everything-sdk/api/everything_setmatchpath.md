# Everything_SetMatchPath

Source: https://www.voidtools.com

# Everything_SetMatchPath

The **Everything_SetMatchPath** function enables or disables full path matching for the next call to [Everything_Query](/support/everything/sdk/everything_query).

## Syntax

```
void Everything_SetMatchPath(
    BOOL bEnable
);
```

## Parameters

*bEnable*

[in] Specifies whether to enable or disable full path matching.

If this parameter is TRUE, full path matching is enabled.

If the parameter is FALSE, full path matching is disabled.

## Remarks

If match full path is being enabled, the next call to [Everything_Query](/support/everything/sdk/everything_query) will search the full path and file name of each file and folder.

If match full path is being disabled, the next call to [Everything_Query](/support/everything/sdk/everything_query) will search the file name only of each file and folder.

Match path is disabled by default.

Enabling match path will add a significant performance hit.

## Example

```
Everything_SetMatchPath(TRUE);
```

## See Also

- [Everything_GetMatchPath](/support/everything/sdk/everything_getmatchpath)

- [Everything_Query](/support/everything/sdk/everything_query)
