# Everything_UpdateAllFolderIndexes

Source: https://www.voidtools.com

# Everything_UpdateAllFolderIndexes

The **Everything_UpdateAllFolderIndexes** function requests Everything to rescan all folder indexes.

## Syntax

```
BOOL Everything_UpdateAllFolderIndexes(void);
```

## Parameters

No parameters.

## Return Value

The function returns non-zero if the request to rescan all folder indexes was successful.

The function returns 0 if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

Everything will begin updating all folder indexes in the background.

## Example

```
// Request all folder indexes be rescanned.
Everything_UpdateAllFolderIndexes();
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also
