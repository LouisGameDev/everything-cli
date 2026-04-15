# Everything_Query

Source: https://www.voidtools.com

# Everything_Query

The **Everything_Query** function executes an Everything IPC query with the current search state.

## Syntax

```
BOOL Everything_Query(
    BOOL bWait
);
```

## Parameters

*bWait*

Should the function wait for the results or return immediately.

Set this to FALSE to post the IPC Query and return immediately.

Set this to TRUE to send the IPC Query and wait for the results.

## Return Value

If the function succeeds, the return value is TRUE.

If the function fails, the return value is FALSE.  To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Description |

| EVERYTHING_ERROR_CREATETHREAD | Failed to create the search query thread. |

| EVERYTHING_ERROR_REGISTERCLASSEX | Failed to register the search query window class. |

| EVERYTHING_ERROR_CREATEWINDOW | Failed to create the search query window. |

| EVERYTHING_ERROR_IPC | IPC is not available. Make sure Everything is running. |

| EVERYTHING_ERROR_MEMORY | Failed to allocate memory for the search query. |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_SetReplyWindow](/support/everything/sdk/everything_setreplywindow) before calling Everything_Query with bWait set to FALSE. |

## Remarks

If bWait is FALSE you must call [Everything_SetReplyWindow](/support/everything/sdk/everything_setreplywindow) before calling Everything_Query. Use the [Everything_IsQueryReply](/support/everything/sdk/everything_isqueryreply) function to check for query replies.

Optionally call the following functions to set the search state before calling Everything_Query:

- [Everything_SetSearch](/support/everything/sdk/everything_setsearch)

- [Everything_SetMatchPath](/support/everything/sdk/everything_setmatchpath)

- [Everything_SetMatchCase](/support/everything/sdk/everything_setmatchcase)

- [Everything_SetMatchWholeWord](/support/everything/sdk/everything_setmatchwholeword)

- [Everything_SetRegex](/support/everything/sdk/everything_setregex)

- [Everything_SetMax](/support/everything/sdk/everything_setmax)

- [Everything_SetOffset](/support/everything/sdk/everything_setoffset)

- [Everything_SetReplyID](/support/everything/sdk/everything_setreplyid)

- [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)

You can mix ANSI / Unicode version of Everything_SetSearch and Everything_Query.

The ANSI / Unicode version of Everything_Query MUST match the ANSI / Unicode version of Everything_GetResultName and Everything_GetResultPath.

The search state is not modified from a call to Everything_Query.

The default state is as follows:

See [Everything_Reset](/support/everything/sdk/everything_reset) for the default search state.

## Example

```
// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// enable case sensitive searching.
Everything_SetMatchCase(TRUE);

// execute the query
Everything_Query(TRUE);
```

## See Also

- [Everything_SetSearch](/support/everything/sdk/everything_setsearch)

- [Everything_SetMatchPath](/support/everything/sdk/everything_setmatchpath)

- [Everything_SetMatchCase](/support/everything/sdk/everything_setmatchcase)

- [Everything_SetMatchWholeWord](/support/everything/sdk/everything_setmatchwholeword)

- [Everything_SetRegex](/support/everything/sdk/everything_setregex)

- [Everything_SetMax](/support/everything/sdk/everything_setmax)

- [Everything_SetOffset](/support/everything/sdk/everything_setoffset)

- [Everything_SortResultsByPath](/support/everything/sdk/everything_sortresultsbypath)

- [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

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

- [Everything_SetReplyWindow](/support/everything/sdk/everything_setreplywindow)

- [Everything_SetReplyID](/support/everything/sdk/everything_setreplyid)

- [Everything_Reset](/support/everything/sdk/everything_reset)
