# SDK

Source: https://www.voidtools.com

# SDK

The Everything SDK provides a DLL and Lib interface to Everything over [IPC](/support/everything/sdk/ipc).

It also provides methods for using WM_COPYDATA for [IPC](/support/everything/sdk/ipc).

Everything is required to run in the background.

## Download

[Everything-SDK.zip](/Everything-SDK.zip)

## Manipulating the search state

- [Everything_SetSearch](/support/everything/sdk/everything_setsearch)

- [Everything_SetMatchPath](/support/everything/sdk/everything_setmatchpath)

- [Everything_SetMatchCase](/support/everything/sdk/everything_setmatchcase)

- [Everything_SetMatchWholeWord](/support/everything/sdk/everything_setmatchwholeword)

- [Everything_SetRegex](/support/everything/sdk/everything_setregex)

- [Everything_SetMax](/support/everything/sdk/everything_setmax)

- [Everything_SetOffset](/support/everything/sdk/everything_setoffset)

- [Everything_SetReplyWindow](/support/everything/sdk/everything_setreplywindow)

- [Everything_SetReplyID](/support/everything/sdk/everything_setreplyid)

- [Everything_SetSort](/support/everything/sdk/everything_setsort)

- [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)

## Reading the search state

- [Everything_GetSearch](/support/everything/sdk/everything_getsearch)

- [Everything_GetMatchPath](/support/everything/sdk/everything_getmatchpath)

- [Everything_GetMatchCase](/support/everything/sdk/everything_getmatchcase)

- [Everything_GetMatchWholeWord](/support/everything/sdk/everything_getmatchwholeword)

- [Everything_GetRegex](/support/everything/sdk/everything_getregex)

- [Everything_GetMax](/support/everything/sdk/everything_getmax)

- [Everything_GetOffset](/support/everything/sdk/everything_getoffset)

- [Everything_GetReplyWindow](/support/everything/sdk/everything_getreplywindow)

- [Everything_GetReplyID](/support/everything/sdk/everything_getreplyid)

- [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

- [Everything_GetSort](/support/everything/sdk/everything_getsort)

- [Everything_GetRequestFlags](/support/everything/sdk/everything_getrequestflags)

## Executing the query

- [Everything_Query](/support/everything/sdk/everything_query)

## Check for query reply

- [Everything_IsQueryReply](/support/everything/sdk/everything_isqueryreply)

## Manipulating results

- [Everything_SortResultsByPath](/support/everything/sdk/everything_sortresultsbypath)

- [Everything_Reset](/support/everything/sdk/everything_reset)

## Reading results

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

- [Everything_GetResultListSort](/support/everything/sdk/everything_getresultlistsort)

- [Everything_GetResultListRequestFlags](/support/everything/sdk/everything_getresultlistrequestflags)

- [Everything_GetResultExtension](/support/everything/sdk/everything_getresultextension)

- [Everything_GetResultSize](/support/everything/sdk/everything_getresultsize)

- [Everything_GetResultDateCreated](/support/everything/sdk/everything_getresultdatecreated)

- [Everything_GetResultDateModified](/support/everything/sdk/everything_getresultdatemodified)

- [Everything_GetResultDateAccessed](/support/everything/sdk/everything_getresultdateaccessed)

- [Everything_GetResultAttributes](/support/everything/sdk/everything_getresultattributes)

- [Everything_GetResultFileListFileName](/support/everything/sdk/everything_getresultfilelistfilename)

- [Everything_GetResultRunCount](/support/everything/sdk/everything_getresultruncount)

- [Everything_GetResultDateRun](/support/everything/sdk/everything_getresultdaterun)

- [Everything_GetResultDateRecentlyChanged](/support/everything/sdk/everything_getresultdaterecentlychanged)

- [Everything_GetResultHighlightedFileName](/support/everything/sdk/everything_getresulthighlightedfilename)

- [Everything_GetResultHighlightedPath](/support/everything/sdk/everything_getresulthighlightedpath)

- [Everything_GetResultHighlightedFullPathAndFileName](/support/everything/sdk/everything_getresulthighlightedfullpathandfilename)

## General

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_CleanUp](/support/everything/sdk/everything_cleanup)

- [Everything_GetMajorVersion](/support/everything/sdk/everything_getmajorversion)

- [Everything_GetMinorVersion](/support/everything/sdk/everything_getminorversion)

- [Everything_GetRevision](/support/everything/sdk/everything_getrevision)

- [Everything_GetBuildNumber](/support/everything/sdk/everything_getbuildnumber)

- [Everything_Exit](/support/everything/sdk/everything_exit)

- [Everything_IsDBLoaded](/support/everything/sdk/everything_isdbloaded)

- [Everything_IsAdmin](/support/everything/sdk/everything_isadmin)

- [Everything_IsAppData](/support/everything/sdk/everything_isappdata)

- [Everything_RebuildDB](/support/everything/sdk/everything_rebuilddb)

- [Everything_UpdateAllFolderIndexes](/support/everything/sdk/everything_updateallfolderindexes)

- [Everything_SaveDB](/support/everything/sdk/everything_savedb)

- [Everything_SaveRunHistory](/support/everything/sdk/everything_saverunhistory)

- [Everything_DeleteRunHistory](/support/everything/sdk/everything_deleterunhistory)

- [Everything_GetTargetMachine](/support/everything/sdk/everything_gettargetmachine)

## Run History

- [Everything_GetRunCountFromFileName](/support/everything/sdk/everything_getruncountfromfilename)

- [Everything_SetRunCountFromFileName](/support/everything/sdk/everything_setruncountfromfilename)

- [Everything_IncRunCountFromFileName](/support/everything/sdk/everything_incruncountfromfilename)

## Examples

- [C/C++](/support/everything/sdk/c)

- [C#](/support/everything/sdk/csharp)

- [C# CLI Example by dipique](https://github.com/dipique/everythingio)

- [Clarion](/support/everything/sdk/clarion)

- [Visual Basic](/support/everything/sdk/visual_basic)

- [Python](/support/everything/sdk/python)

## Notes

- The SDK is a basic [IPC](/support/everything/sdk/ipc) wrapper

- Requires "Everything" client to be running.

- ANSI / Unicode support.

- Thread safe.

- Support for blocking and non-blocking mode.

- x86 and x64 support.

## See Also

- [IPC](/support/everything/sdk/ipc)
