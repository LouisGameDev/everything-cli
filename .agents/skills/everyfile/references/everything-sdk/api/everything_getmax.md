# Everything_GetMax

Source: https://www.voidtools.com

# Everything_GetMax

The **Everything_GetMax** function returns the maximum number of results state.

## Syntax

```
BOOL Everything_GetMax(void);
```

## Return Value

The return value is the maximum number of results state.

The function returns 0xFFFFFFFF if all results should be returned.

## Remarks

The default state is 0xFFFFFFFF, or all results.

## Example

```
DWORD dwMaxResults = Everything_GetMax();
```

## See Also

- [Everything_SetMax](/support/everything/sdk/everything_setmax)

- [Everything_Query](/support/everything/sdk/everything_query)
