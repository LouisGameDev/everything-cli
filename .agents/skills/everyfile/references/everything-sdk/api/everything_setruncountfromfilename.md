# Everything_SetRunCountFromFileName

Source: https://www.voidtools.com

# Everything_SetRunCountFromFileName

The **Everything_SetRunCountFromFileName** function sets the run count for a specified file in the Everything index by file name.

## Syntax

```
BOOL Everything_SetRunCountFromFileName(
    LPCTSTR lpFileName,
    DWORD dwRunCount
);
```

## Parameters

*lpFileName* [in]

Pointer to a null-terminated string that specifies a fully qualified file name in the Everything index.

*dwRunCount* [in]

The new run count.

## Return Value

The function returns non-zero if successful.

The function returns 0 if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

Set the run count to 0 to remove any run history information for the specified file.

The file does not have to exist. When the file is created it will have the correct run history.

Run history information is preserved between file deletion and creation.

Calling this function will update the date run to the current time for the specified file.

## Example

```
// set a file to show higher in the results by setting an exaggerated run count
Everything_SetRunCountFromFileName(TEXT("C:\\folder\\file.doc"),1000);
```

## See Also

- [Everything_GetRunCountFromFileName](/support/everything/sdk/everything_getruncountfromfilename)

- [Everything_IncRunCountFromFileName](/support/everything/sdk/everything_incruncountfromfilename)
