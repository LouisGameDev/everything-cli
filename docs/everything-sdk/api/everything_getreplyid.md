# Everything_GetReplyID

Source: https://www.voidtools.com

# Everything_GetReplyID

The **Everything_GetReplyID** function returns the current reply identifier for the IPC query reply.

## Syntax

```
DWORD Everything_GetReplyID(void);
```

## Return Value

The return value is the current reply identifier.

## Remarks

The default reply identifier is 0.

## Example

```
DWORD id = Everything_GetReplyID();
```

## See Also

- [Everything_SetReplyWindow](/support/everything/sdk/everything_setreplywindow)

- [Everything_GetReplyWindow](/support/everything/sdk/everything_getreplywindow)

- [Everything_SetReplyID](/support/everything/sdk/everything_setreplyid)

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_IsQueryReply](/support/everything/sdk/everything_isqueryreply)
