# Everything_SaveDB

Source: https://www.voidtools.com

# Everything_SaveDB

The **Everything_SaveDB** function requests Everything to save the index to disk.

**

## Syntax

```
BOOL Everything_SaveDB(void);
```

## Parameters

No parameters.

## Return Value

The function returns non-zero if the request to save the Everything index to disk was successful.

The function returns 0 if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

The index is only saved to disk when you exit Everything.

Call Everything_SaveDB** to write the index to the file: Everything.db

## Example

```
// flush index to disk
Everything_SaveDB();
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also
