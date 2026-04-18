# Everything_IsQueryReply

Source: https://www.voidtools.com

# Everything_IsQueryReply

The **Everything_IsQueryReply** function checks if the specified window message is a query reply.

## Syntax

```
BOOL EVERYTHINGAPI Everything_IsQueryReply(
    UINT message,
    WPARAM wParam,
    LPARAM lParam,
    DWORD nId
);
```

## Parameters

*message*

Specifies the message identifier.

*wParam*

Specifies additional information about the message.

*lParam*

Specifies additional information about the message.

*nId*

The unique identifier specified with [Everything_SetReplyID](/support/everything/sdk/everything_setreplyid), or 0 for the default ID.

This is the value used to compare with the dwData member of the COPYDATASTRUCT if the message is WM_COPYDATA.

## Return Value

Returns TRUE if the message is a query reply.

If the function fails the return value is FALSE. To get extended error information, call: [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

## Remarks

This function checks if the message is a WM_COPYDATA message. If the message is a WM_COPYDATA message the function checks if the ReplyID matches the dwData member of the COPYDATASTRUCT. If they match the function makes a copy of the query results.

You must call Everything_IsQueryReply in the windows message handler to check for an IPC query reply if you call Everything_Query with bWait set to FALSE.

If the function returns TRUE you should return TRUE.

If the function returns TRUE you can call the following functions to read the results:

- [Everything_SortResultsByPath](/support/everything/sdk/everything_sortresultsbypath)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults)

- [Everything_GetNumFolderResults](/support/everything/sdk/everything_getnumfolderresults)

- [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults)

- [Everything_GetTotFileResults](/support/everything/sdk/everything_gettotfileresults)

- [Everything_GetTotFolderResults](/support/everything/sdk/everything_gettotfolderresults)

- [Everything_GetTotResults](/support/everything/sdk/everything_gettotresults)

- [Everything_IsVolumeResult](/support/everything/sdk/everything_isvolumeresult)

- [Everything_IsFolderResult](/support/everything/sdk/everything_isfolderresult)

- [Everything_IsFileResult](/support/everything/sdk/everything_isfileresult)

- [Everything_GetResultFileName](/support/everything/sdk/everything_getresultfilename)

- [Everything_GetResultPath](/support/everything/sdk/everything_getresultpath)

- [Everything_GetResultFullPathName](/support/everything/sdk/everything_getresultfullpathname)

## Example

```
LRESULT CALLBACK WindowProc(HWND hwnd,UINT uMsg,WPARAM wParam,LPARAM lParam)
{
	if (Everything_IsQueryReply(uMsg,wParam,lParam,0))
	{
		// ...
		// do something with the results..
		// ...

		return TRUE;
	}

	// return the default window proc..
	return DefWindowProc(hwnd,uMsg,wParam,lParam);
}
```

## Implementation

```
BOOL EVERYTHINGAPI Everything_IsQueryReply(UINT message,WPARAM wParam,LPARAM lParam,DWORD nId)
{
	if (message == WM_COPYDATA)
	{
		COPYDATASTRUCT *cds = (COPYDATASTRUCT *)lParam;

		if (cds)
		{
			if (cds->dwData == _Everything_ReplyID)
			{
				if (_Everything_IsUnicodeQuery)
				{
					if (_Everything_List) HeapFree(GetProcessHeap(),0,_Everything_List);

					_Everything_List = (EVERYTHING_IPC_LISTW *)HeapAlloc(GetProcessHeap(),0,cds->cbData);

					if (_Everything_List)
					{
						CopyMemory(_Everything_List,cds->lpData,cds->cbData);
					}
					else
					{
						_Everything_LastError = EVERYTHING_ERROR_MEMORY;
					}

					return TRUE;
				}
				else
				{
					if (_Everything_List) HeapFree(GetProcessHeap(),0,_Everything_List);

					_Everything_List = (EVERYTHING_IPC_LISTW *)HeapAlloc(GetProcessHeap(),0,cds->cbData);

					if (_Everything_List)
					{
						CopyMemory(_Everything_List,cds->lpData,cds->cbData);
					}
					else
					{
						_Everything_LastError = EVERYTHING_ERROR_MEMORY;
					}

					return TRUE;
				}
			}
		}
	}

	return FALSE;
}
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_SetReplyWindow](/support/everything/sdk/everything_setreplywindow)

- [Everything_SetReplyID](/support/everything/sdk/everything_setreplyid)

- [Everything_GetReplyWindow](/support/everything/sdk/everything_getreplywindow)

- [Everything_GetReplyID](/support/everything/sdk/everything_getreplyid)
