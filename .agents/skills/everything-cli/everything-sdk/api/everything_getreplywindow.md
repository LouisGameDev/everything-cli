# Everything_GetReplyWindow

Source: https://www.voidtools.com

# Everything_GetReplyWindow

The **Everything_GetReplyWindow** function returns the current reply window for the IPC query reply.

## Syntax

```
HWND Everything_GetReplyWindow(void);
```

## Return Value

The return value is the current reply window.

## Remarks

The default reply window is 0, or no reply window.

## Example

```
HWND hWnd = Everything_GetReplyWindow();
```

## See Also

- [Everything_SetReplyWindow](/support/everything/sdk/everything_setreplywindow)

- [Everything_SetReplyID](/support/everything/sdk/everything_setreplyid)

- [Everything_GetReplyID](/support/everything/sdk/everything_getreplyid)

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_IsQueryReply](/support/everything/sdk/everything_isqueryreply)
