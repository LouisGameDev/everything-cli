# Clarion

Source: https://www.voidtools.com

# Clarion

Note: requires Everything running in the background.

## Setup

Download the Clarion module: [Clarion_Everything.zip](/Clarion_Everything.zip)

Source code of the module is included.

Extract Everything.lib to your clarion project.

Add the LIB to "Library, object, and resource files" in your Clarion project and put the following in your global map.

```
MODULE('Everything.lib')
  Everything_GetLastError(),LONG,RAW,PASCAL
  Everything_SetSearch(*CSTRING),RAW,PASCAL
  Everything_SetMatchPath(LONG),RAW,PASCAL
  Everything_SetMatchCase(LONG),RAW,PASCAL
  Everything_SetMatchWholeWord(LONG),RAW,PASCAL
  Everything_EnableRegex(LONG),RAW,PASCAL
  Everything_SetMax(LONG),RAW,PASCAL
  Everything_SetOffset(LONG),RAW,PASCAL
  Everything_Query(),RAW,PASCAL
  Everything_SetDetail(LONG),RAW,PASCAL
  Everything_SortResults(LONG),RAW,PASCAL
  Everything_GetNumFileResults(),LONG,RAW,PASCAL
  Everything_GetNumFolderResults(),LONG,RAW,PASCAL
  Everything_GetNumResults(),LONG,RAW,PASCAL
  Everything_GetTotFileResults(),LONG,RAW,PASCAL
  Everything_GetTotFolderResults(),LONG,RAW,PASCAL
  Everything_GetTotResults(),LONG,RAW,PASCAL
  Everything_IsVolumeResult(LONG),LONG,RAW,PASCAL
  Everything_IsFolderResult(LONG),LONG,RAW,PASCAL
  Everything_IsFileResult(LONG),LONG,RAW,PASCAL
  Everything_GetResultFileName(LONG),*CSTRING,RAW,PASCAL
  Everything_GetResultPath(LONG),*CSTRING,RAW,PASCAL
  Everything_GetResult(LONG,LONG),RAW,PASCAL
END
```

## Changes

added:

- [Everything_SetDetail](/support/everything/sdk/clarion#everything_setdetail)

[Everything_SortResults](/support/everything/sdk/clarion#everything_sortresults)

## Equates

```

!return values from Everything_GetLastError
EVERYTHING_OK				EQUATE(0) ! no error
EVERYTHING_ERROR_MEMORY			EQUATE(1) ! out of memory
EVERYTHING_ERROR_IPC			EQUATE(2) ! IPC not available
EVERYTHING_ERROR_REGISTERCLASSEX	EQUATE(3) ! RegisterClassEx failed
EVERYTHING_ERROR_CREATEWINDOW		EQUATE(4) ! CreateWindow failed
EVERYTHING_ERROR_CREATETHREAD		EQUATE(5) ! CreateThread failed
EVERYTHING_ERROR_INVALIDINDEX		EQUATE(6) ! Invalid result index (must be >= 0 and < numResults)
EVERYTHING_ERROR_INVALIDCALL		EQUATE(7) ! Call Everything_Query before getting results

!attributes
EVERYTHING_FILE_ATTRIBUTE_READONLY             EQUATE(0001h)
EVERYTHING_FILE_ATTRIBUTE_HIDDEN               EQUATE(0002h)
EVERYTHING_FILE_ATTRIBUTE_SYSTEM               EQUATE(0004h)
EVERYTHING_FILE_ATTRIBUTE_DIRECTORY            EQUATE(0010h)
EVERYTHING_FILE_ATTRIBUTE_ARCHIVE              EQUATE(0020h)
EVERYTHING_FILE_ATTRIBUTE_DEVICE               EQUATE(0040h)
EVERYTHING_FILE_ATTRIBUTE_NORMAL               EQUATE(0080h)
EVERYTHING_FILE_ATTRIBUTE_TEMPORARY            EQUATE(0100h)
EVERYTHING_FILE_ATTRIBUTE_SPARSE_FILE          EQUATE(0200h)
EVERYTHING_FILE_ATTRIBUTE_REPARSE_POINT        EQUATE(0400h)
EVERYTHING_FILE_ATTRIBUTE_COMPRESSED           EQUATE(0800h)
EVERYTHING_FILE_ATTRIBUTE_OFFLINE              EQUATE(1000h)
EVERYTHING_FILE_ATTRIBUTE_NOT_CONTENT_INDEXED  EQUATE(2000h)
EVERYTHING_FILE_ATTRIBUTE_ENCRYPTED            EQUATE(4000h)
```

## Limits and Notes

Everything MUST be running for this to work.

See Everything [IPC](/support/everything/sdk/ipc).

You can only do one search at a time.

If there is demand for it, I can add multiple thread safe searches.

## Descriptions

## Everything_GetLastError

```
myError LONG

!check the equates for error message descriptions
myError = Everything_GetLastError()
```

## Everything_SetSearch

```
myString STRING

!Set the search string
!default search is '' (empty string)
Everything_SetSearch(myString)
```

## Everything_SetMatchPath

```
val LONG

!set val to zero to disable path matching
!set val to non-zero to enable path matching
!default is 0 (off)
Everything_SetMatchPath(val)
```

## Everything_SetMatchCase

```
val LONG

!set val to zero to disable case matching
!set val to non-zero to enable case matching
!default is 0 (off)
Everything_SetMatchCase(val)
```

## Everything_SetMatchWholeWord

```
val LONG

!set val to zero to disable whole word matching
!set val to non-zero to enable whole word matching
!default is 0 (off)
Everything_SetMatchWholeWord(val)
```

## Everything_EnableRegex

```
val LONG

!set val to zero to disable regex
!set val to non-zero to enable regex
!default is 0 (off)
Everything_EnableRegex(val)
```

## Everything_SetMax

```
val LONG

!If you display the results in a list, set this value to how many items are visible in the list.
!How many results would you like Everything to return?
!Use this for displaying small lists.
!Default is 0xFFFFFFFF (all results)
Everything_SetMax(val)
```

## Everything_SetOffset

```
offset LONG

!If you display a list with a scroll bar, set the offset to the scroll bar's offset.
!From what index would you like Everything to return results from?
!zero means return results starting from the first result.
!10 would mean return results starting from the 10th result.
!use this for displaying small lists.
!default is 0
!This is 0 based
Everything_SetOffset(offset)
```

## Everything_Query

```
!Execute the query
!use the Everything_Set* functions to override default search parameters
!This sends the search options to "Everything" over the IPC.
!It does not return until it has a copy of ALL the results.
!Use Everything_GetResult to enumerate results.
!100 results will take about 1 millisecond.
!1 million results will take about 1 second.
Everything_Query()
```

## Everything_SetDetail

```
detail LONG

!The result detail
!Set detail to nonzero to get file information from Everything_GetResult
!Set detail to zero to get file name, path name offsets and lengths and partial file attributes only.
!The default detail is zero.
!This can be called at anytime.
!make sure you sort the results with Everything_SortResults() if you set the detail to non-zero. (this will speed up the enumerating process.)
Everything_SetDetail(detail)
```

## Everything_SortResults

```
NoDriveLetter LONG

!Set NoDriveLetter to nonzero to sort by path excluding drive letters.
!Set NoDriveLetter to zero to sort by path.
!Use this before getting detailed results (set NoDriveLetter to zero).
!Results are sorted by name by default.
!Can only be called after a call to Everything_Query
Everything_SortResults(NoDriveLetter)
```

## Everything_GetNumFileResults

```
numFiles LONG

!Get the number of files in the visible results list.
numFiles = Everything_GetNumFileResults()
```

## Everything_GetNumFolderResults

```
numFolders LONG

!Get the number of folders in the visible results list.
numFolders = Everything_GetNumFolderResults()
```

## Everything_GetNumResults

```
numResults LONG

!Get the number of files and folders in the visible results list.
numResults = Everything_GetNumResults()
```

## Everything_GetTotFileResults

```
totFiles LONG

!Get the total number of files in the results list.
totFiles = Everything_GetTotFileResults()
```

## Everything_GetTotFolderResults

```
totFolders LONG

!Get the total number of files in the results list.
totFolders = Everything_GetTotFolderResults()
```

## Everything_GetTotResults

```
totResults LONG

!Get the total number of files and folders in the results list.
!index is 0 based
totResults = Everything_GetTotResults()
```

## Everything_IsVolumeResult

```
index LONG
val LONG

!returns zero if the result is not a volume.
!returns non-zero if the result is a volume.
!index is 0 based
!deprecated - Use Everything_GetResult
val = Everything_IsVolumeResult(index)
```

## Everything_IsFolderResult

```
index LONG
val LONG

!returns zero if the result is not a folder.
!returns non-zero if the result is a folder.
!index is 0 based
!deprecated - Use Everything_GetResult
val = Everything_IsFolderResult(index)
```

## Everything_IsFileResult

```
index LONG
val LONG

!returns zero if the result is not a file
!returns non-zero if the result is a file.
!index is 0 based
!deprecated - Use Everything_GetResult
val = Everything_IsFileResult(index)
```

## Everything_GetResultFileName

```
index LONG
filename CSTRING

!index is 0 based
!this gets the result file name
!deprecated - Use Everything_GetResult
filename = Everything_GetResultFileName(index)
```

## Everything_GetResultPath

```
index LONG
path CSTRING

!index is 0 based
!this gets the result path
!deprecated - Use Everything_GetResult
path = Everything_GetResultPath(index)
```

## Everything_GetResult

```
index LONG
result	GROUP
FullPathFileName	STRING(260) !The full path and file name of the result
PathPartLength		LONG ! Length of the path part only
FileNamePartOffset	LONG ! Offset into FullPathFileName for the file name part only (0 based)
SizeHigh		LONG ! High part of size (ignore this if you do not need the full 64bit size)
SizeLow			ULONG ! Low part of size
Attributes		LONG ! Attribute flags can be zero or more EVERYTHING_FILE_ATTRIBUTE_* flags
CreationYear		LONG ! The year (1601 - 30827).
CreationMonth		LONG ! The month (January = 1, December = 12)
CreationDayOfWeek	LONG ! The day of the week. (sunday = 0, monday = 1, Saturday = 6)
CreationDay		LONG ! The day of the month (1-31).
CreationHour		LONG ! The hour (0-23).
CreationMinute		LONG ! The minute (0-59).
CreationSecond		LONG ! The second (0-59).
CreationMilliseconds	LONG ! The millisecond (0-999).
LastAccessYear		LONG ! The year (1601 - 30827).
LastAccessMonth		LONG ! The month (January = 1, December = 12)
LastAccessDayOfWeek	LONG ! The day of the week. (sunday = 0, monday = 1, Saturday = 6)
LastAccessDay		LONG ! The day of the month (1-31).
LastAccessHour		LONG ! The hour (0-23).
LastAccessMinute	LONG ! The minute (0-59).
LastAccessSecond	LONG ! The second (0-59).
LastAccessMilliseconds	LONG ! The millisecond (0-999).
LastWriteYear		LONG ! The year (1601 - 30827).
LastWriteMonth		LONG ! The month (January = 1, December = 12)
LastWriteDayOfWeek	LONG ! The day of the week. (sunday = 0, monday = 1, Saturday = 6)
LastWriteDay		LONG ! The day of the month (1-31).
LastWriteHour		LONG ! The hour (0-23).
LastWriteMinute		LONG ! The minute (0-59).
LastWriteSecond		LONG ! The second (0-59).
LastWriteMilliseconds	LONG ! The millisecond (0-999).
	END

!index is 0 based
!fills in the result group
!See Everything_SetDetail for what information is filled in.
Everything_GetResult(index,ADDRESS(result))
```

## Fast Program Example

```

x LONG,AUTO
m LONG
result	GROUP
FullPathFileName	STRING(260) !The full path and file name of the result
PathPartLength		LONG ! Length of the path part only
FileNamePartOffset	LONG ! Offset into FullPathFileName for the file name part only (0 based)
SizeHigh		LONG ! Not used in this example.
SizeLow			ULONG ! Not used in this example.
Attributes		LONG ! Attribute flags can be zero or EVERYTHING_FILE_ATTRIBUTE_DIRECTORY flag
CreationYear		LONG ! Not used in this example.
CreationMonth		LONG ! Not used in this example.
CreationDayOfWeek	LONG ! Not used in this example.
CreationDay		LONG ! Not used in this example.
CreationHour		LONG ! Not used in this example.
CreationMinute		LONG ! Not used in this example.
CreationSecond		LONG ! Not used in this example.
CreationMilliseconds	LONG ! Not used in this example.
LastAccessYear		LONG ! Not used in this example.
LastAccessMonth		LONG ! Not used in this example.
LastAccessDayOfWeek	LONG ! Not used in this example.
LastAccessDay		LONG ! Not used in this example.
LastAccessHour		LONG ! Not used in this example.
LastAccessMinute	LONG ! Not used in this example.
LastAccessSecond	LONG ! Not used in this example.
LastAccessMilliseconds	LONG ! Not used in this example.
LastWriteYear		LONG ! Not used in this example.
LastWriteMonth		LONG ! Not used in this example.
LastWriteDayOfWeek	LONG ! Not used in this example.
LastWriteDay		LONG ! Not used in this example.
LastWriteHour		LONG ! Not used in this example.
LastWriteMinute		LONG ! Not used in this example.
LastWriteSecond		LONG ! Not used in this example.
LastWriteMilliseconds	LONG ! Not used in this example.
	END

!setup a query using the default search parameters
!change the search string to 'whatthe'
Everything_SetSearch('whatthe')

!Find all the results for 'whatthe'
Everything_Query()

m = Everything_GetNumResults()
LOOP x = 0 TO m - 1

    Everything_GetResult(x,ADDRESS(result))

    ...
    !do something with name and path
    ...
END
```

## Detailed Program Example

```

x LONG,AUTO
m LONG
result	GROUP
FullPathFileName	STRING(260) !The full path and file name of the result
PathPartLength		LONG ! Length of the path part only
FileNamePartOffset	LONG ! Offset into FullPathFileName for the file name part only (0 based)
SizeHigh		LONG ! High part of size (ignore this if you do not need the full 64bit size)
SizeLow			ULONG ! Low part of size
Attributes		LONG ! Attribute flags can be zero or more EVERYTHING_FILE_ATTRIBUTE_* flags
CreationYear		LONG ! The year (1601 - 30827).
CreationMonth		LONG ! The month (January = 1, December = 12)
CreationDayOfWeek	LONG ! The day of the week. (sunday = 0, monday = 1, Saturday = 6)
CreationDay		LONG ! The day of the month (1-31).
CreationHour		LONG ! The hour (0-23).
CreationMinute		LONG ! The minute (0-59).
CreationSecond		LONG ! The second (0-59).
CreationMilliseconds	LONG ! The millisecond (0-999).
LastAccessYear		LONG ! The year (1601 - 30827).
LastAccessMonth		LONG ! The month (January = 1, December = 12)
LastAccessDayOfWeek	LONG ! The day of the week. (sunday = 0, monday = 1, Saturday = 6)
LastAccessDay		LONG ! The day of the month (1-31).
LastAccessHour		LONG ! The hour (0-23).
LastAccessMinute	LONG ! The minute (0-59).
LastAccessSecond	LONG ! The second (0-59).
LastAccessMilliseconds	LONG ! The millisecond (0-999).
LastWriteYear		LONG ! The year (1601 - 30827).
LastWriteMonth		LONG ! The month (January = 1, December = 12)
LastWriteDayOfWeek	LONG ! The day of the week. (sunday = 0, monday = 1, Saturday = 6)
LastWriteDay		LONG ! The day of the month (1-31).
LastWriteHour		LONG ! The hour (0-23).
LastWriteMinute		LONG ! The minute (0-59).
LastWriteSecond		LONG ! The second (0-59).
LastWriteMilliseconds	LONG ! The millisecond (0-999).
	END

!setup a query using the default search parameters
!change the search string to 'whatthe'
Everything_SetSearch('whatthe')

!Find all the results for 'whatthe'
Everything_Query()

!turn detail on
Everything_SetDetail(1)

!Sort the results
!this is required for nonzero detail
Everything_SortResults(0)

m = Everything_GetNumResults()
LOOP x = 0 TO m - 1
    Everything_GetResult(x,ADDRESS(result))
    ...
    !do something with result
    ...
END

```
