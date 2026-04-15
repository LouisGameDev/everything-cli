# Everything_GetLastError

Source: https://www.voidtools.com

# Everything_GetLastError

The **Everything_GetLastError** function retrieves the last-error code value.

## Syntax

```
DWORD Everything_GetLastError(void);
```

## Parameters

This function has no parameters.

## Return Value

| Error code | Value | Meaning |

| EVERYTHING_OK | 0 | The operation completed successfully. |

| EVERYTHING_ERROR_MEMORY | 1 | Failed to allocate memory for the search query. |

| EVERYTHING_ERROR_IPC | 2 | IPC is not available. |

| EVERYTHING_ERROR_REGISTERCLASSEX | 3 | Failed to register the search query window class. |

| EVERYTHING_ERROR_CREATEWINDOW | 4 | Failed to create the search query window. |

| EVERYTHING_ERROR_CREATETHREAD | 5 | Failed to create the search query thread. |

| EVERYTHING_ERROR_INVALIDINDEX | 6 | Invalid index. The index must be greater or equal to 0 and less than the number of visible results. |

| EVERYTHING_ERROR_INVALIDCALL | 7 | Invalid call. |

## Example

```
// execute the query
if (!Everything_Query(true))
{
	DWORD dwLastError = Everything_GetLastError();
	if (dwLastError == EVERYTHING_ERROR_IPC)
	{
		// IPC not available.
	}
}
```
