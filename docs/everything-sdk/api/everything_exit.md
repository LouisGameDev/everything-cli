# Everything_Exit

Source: https://www.voidtools.com

# Everything_Exit

The **Everything_Exit** function requests Everything to exit.

## Syntax

```
BOOL Everything_Exit(void);
```

## Parameters

No parameters.

## Return Value

The function returns non-zero if the exit request was successful.

The function returns 0 if the request failed. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

Request Everything to save settings and data to disk and exit.

## Example

```
// request Everything to exit.
Everything_Exit();
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also
