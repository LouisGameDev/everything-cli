# Everything_SetMax

Source: https://www.voidtools.com

# Everything_SetMax

The **Everything_SetMax** function sets the maximum number of results to return from [Everything_Query](/support/everything/sdk/everything_query).

## Syntax

```
void Everything_SetMax(
    DWORD dwMaxResults
);
```

## Parameters

*dwMaxResults*

Specifies the maximum number of results to return.

Setting this to 0xffffffff will return all results.

## Remarks

The default maximum number of results is 0xffffffff (all results).

If you are displaying the results in a window, set the maximum number of results to the number of visible items in the window.

## Example

```
Everything_SetMax(window_height / item_height);
```

## See Also

- [Everything_GetMax](/support/everything/sdk/everything_getmax)

- [Everything_Query](/support/everything/sdk/everything_query)
