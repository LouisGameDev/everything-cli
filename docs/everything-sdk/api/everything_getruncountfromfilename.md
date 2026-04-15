# Everything_GetRunCountFromFileName

Source: https://www.voidtools.com

# Everything_GetRunCountFromFileName

The **Everything_GetRunCountFromFileName** function gets the run count from a specified file in the Everything index by file name.

## Syntax

```
DWORD Everything_GetRunCountFromFileName(
    LPCTSTR lpFileName
);
```

## Parameters

*lpFileName* [in]

Pointer to a null-terminated string that specifies a fully qualified file name in the Everything index.

## Return Value

The function returns the number of times the file has been run from Everything.

The function returns 0 if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_OK | The run count is 0. |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

## Example

```
DWORD runCount;

// get the run count of a file.
runCount = Everything_GetRunCountFromFileName(TEXT("C:\\folder\\file.doc"));
```

## See Also

- [Everything_SetRunCountFromFileName](/support/everything/sdk/everything_setruncountfromfilename)

- [Everything_IncRunCountFromFileName](/support/everything/sdk/everything_incruncountfromfilename)
