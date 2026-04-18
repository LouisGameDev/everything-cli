# Everything_SetReplyWindow

Source: https://www.voidtools.com

# Everything_SetReplyWindow

The **Everything_SetReplyWindow** function sets the window that will receive the the IPC Query results.

## Syntax

```
void Everything_SetReplyWindow(
    HWND hWnd
);
```

## Parameters

*hWnd*

The handle to the window that will receive the IPC Query reply.

## Return Value

This function has no return value.

## Remarks

This function must be called before calling [Everything_Query](/support/everything/sdk/everything_query) with bWait set to FALSE.

Check for results with the specified window using [Everything_IsQueryReply](/support/everything/sdk/everything_isqueryreply).

Call [Everything_SetReplyID](/support/everything/sdk/everything_setreplyid) with a unique identifier to specify multiple searches.

## Example

```
// reply to this window.
Everything_SetReplyWindow(hwnd);

// execute the query
Everything_Query(TRUE);
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_SetReplyID](/support/everything/sdk/everything_setreplyid)

- [Everything_GetReplyWindow](/support/everything/sdk/everything_getreplywindow)

- [Everything_GetReplyID](/support/everything/sdk/everything_getreplyid)

- [Everything_IsQueryReply](/support/everything/sdk/everything_isqueryreply)
