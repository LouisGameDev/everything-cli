# Everything_IncRunCountFromFileName

Source: https://www.voidtools.com

# Everything_IncRunCountFromFileName

The **Everything_IncRunCountFromFileName** function increments the run count by one for a specified file in the Everything by file name.

## Syntax

```
DWORD Everything_IncRunCountFromFileName(
    LPCTSTR lpFileName
);
```

## Parameters

*lpFileName* [in]

Pointer to a null-terminated string that specifies a fully qualified file name in the Everything index.

## Return Value

The function returns the new run count for the specifed file.

The function returns 0 if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

The file does not have to exist. When the file is created it will have the correct run history.

Run history information is preserved between file deletion and creation.

Calling this function will update the date run to the current time for the specified file.

Incrementing a file with a run count of 4294967295 (0xffffffff) will do nothing.

## Example

```
// run a file
system("C:\\folder\\file.doc");

// increment the run count in Everything.
Everything_IncRunCountFromFileName(TEXT("C:\\folder\\file.doc"));
```

## See Also

- [Everything_GetRunCountFromFileName](/support/everything/sdk/everything_getruncountfromfilename)

- [Everything_SetRunCountFromFileName](/support/everything/sdk/everything_setruncountfromfilename)
