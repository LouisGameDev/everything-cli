# Everything_SetReplyID

Source: https://www.voidtools.com

# Everything_SetReplyID

The **Everything_SetReplyID** function sets the unique number to identify the next query.

## Syntax

```
void Everything_SetReplyID(
    DWORD nId
);
```

## Parameters

*nID*

The unique number to identify the next query.

## Return Value

This function has no return value.

## Remarks

The default identifier is 0.

Set a unique identifier for the IPC Query.

If you want to post multiple search queries with the same window handle, you must call the Everything_SetReplyID function to assign each query a unique identifier.

The nID value is the dwData member in the COPYDATASTRUCT used in the WM_COPYDATA reply message.

This function is not required if you call Everything_Query with bWait set to true.

## Example

```
// reply to this window.
Everything_SetReplyWindow(hwnd);

// set a unique identifier for this query.
Everything_SetReplyID(1);

// execute the query
Everything_Query(FALSE);
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_SetReplyWindow](/support/everything/sdk/everything_setreplywindow)

- [Everything_GetReplyWindow](/support/everything/sdk/everything_getreplywindow)

- [Everything_GetReplyID](/support/everything/sdk/everything_getreplyid)

- [Everything_IsQueryReply](/support/everything/sdk/everything_isqueryreply)
