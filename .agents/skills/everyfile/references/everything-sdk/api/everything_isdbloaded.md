# Everything_IsDBLoaded

Source: https://www.voidtools.com

# Everything_IsDBLoaded

The **Everything_IsDBLoaded** function checks if the database has been fully loaded.

**

## Syntax

```
BOOL Everything_IsDBLoaded(void);
```

## Parameters

No parameters.

## Return Value

The function returns non-zero if the Everything database is fully loaded.

The function returns 0 if the database has not fully loaded or if an error occurred. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_OK | The database is still loading. |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

When Everything is loading, any queries will appear to return no results.

Use Everything_IsDBLoaded** to determine if the database has been loaded before performing a query.

## Example

```
for(;;)
{
	if (Everything_IsDBLoaded())
	{
		// perform a query...
		break;
	}
	else
	{
		if (Everything_GetLastError())
		{
			// IPC not running.
			break;
		}
	}

	// wait for database to load..
	Sleep(1000);
}
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)
