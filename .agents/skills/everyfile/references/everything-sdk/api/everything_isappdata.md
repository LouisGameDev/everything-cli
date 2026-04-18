# Everything_IsAppData

Source: https://www.voidtools.com

# Everything_IsAppData

The **Everything_IsAppData** function checks if Everything is saving settings and data to %APPDATA%\Everything or to the same location as the Everything.exe.

## Syntax

```
BOOL Everything_IsAppData(void);
```

## Parameters

No parameters.

## Return Value

The function returns non-zero if settings and data are saved in %APPDATA%\Everything.

The function returns 0 if settings and data are saved to the same location as the Everything.exe or if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_OK | Settings and data are stored in the same location as the Everything.exe. |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

## Example

```
BOOL isAppData;

isAppData = Everything_IsAppData();
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_IsAdmin](/support/everything/sdk/everything_isadmin)
