# Everything_RebuildDB

Source: https://www.voidtools.com

# Everything_RebuildDB

The **Everything_RebuildDB** function requests Everything to forcefully rebuild the Everything index.

**

## Syntax

```
BOOL Everything_RebuildDB(void);
```

## Parameters

No parameters.

## Return Value

The function returns non-zero if the request to forcefully rebuild the Everything index was successful.

The function returns 0 if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

Requesting a rebuild will mark all indexes as dirty and start the rebuild process.

Use Everything_IsDBLoaded** to determine if the database has been rebuilt before performing a query.

## Example

```
// rebuild the database.
Everything_RebuildDB();
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_IsDBLoaded](/support/everything/sdk/everything_isdbloaded)
