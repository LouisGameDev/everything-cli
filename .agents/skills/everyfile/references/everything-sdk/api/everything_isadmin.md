# Everything_IsAdmin

Source: https://www.voidtools.com

# Everything_IsAdmin

The **Everything_IsAdmin** function checks if Everything is running as administrator or as a standard user.

## Syntax

```
BOOL Everything_IsAdmin(void);
```

## Parameters

No parameters.

## Return Value

The function returns non-zero if the Everything is running as an administrator.

The function returns 0 Everything is running as a standard user or if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_OK | Everything is running as a standard user. |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

## Example

```
BOOL isAdmin;

isAdmin = Everything_IsAdmin();
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_IsAppData](/support/everything/sdk/everything_isappdata)
