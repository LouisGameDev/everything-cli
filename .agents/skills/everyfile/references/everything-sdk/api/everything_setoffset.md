# Everything_SetOffset

Source: https://www.voidtools.com

# Everything_SetOffset

The **Everything_SetOffset** function set the first result offset to return from a call to [Everything_Query](/support/everything/sdk/everything_query).

## Syntax

```
void Everything_SetOffset(
    DWORD dwOffset
);
```

## Parameters

dwOffset

Specifies the first result from the available results.

Set this to 0 to return the first available result.

## Remarks

The default offset is 0 (the first available result).

If you are displaying the results in a window with a custom scroll bar, set the offset to the vertical scroll bar position.

Using a search window can reduce the amount of data sent over the IPC and significantly increase search performance.

## Example

```
Everything_SetOffset(scrollbar_vpos);
```

## See Also

- [Everything_GetOffset](/support/everything/sdk/everything_getoffset)

- [Everything_Query](/support/everything/sdk/everything_query)
