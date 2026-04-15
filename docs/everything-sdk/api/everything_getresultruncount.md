# Everything_GetResultRunCount

Source: https://www.voidtools.com

# Everything_GetResultRunCount

The **Everything_GetResultRunCount** function retrieves the number of times a visible result has been run from Everything.

## Syntax

```
DWORD Everything_GetResultRunCount(
    DWORD dwIndex,
);
```

## Parameters

*dwIndex*

Zero based index of the visible result.

## Return Value

The function returns the number of times the result has been run from Everything.

The function returns 0 if the run count information is unavailable. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_OK | The run count is 0. |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetResultRunCount. |

| EVERYTHING_ERROR_INVALIDREQUEST | Run count information was not requested or is unavailable, Call [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags) with EVERYTHING_REQUEST_RUN_COUNT before calling [Everything_Query](/support/everything/sdk/everything_query). |

| EVERYTHING_ERROR_INVALIDINDEX | index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

dwIndex must be a valid visible result index. To determine if a result index is visible use the [Everything_GetNumResults](/support/everything/sdk/everything_getnumresults) function.

## Example

```
DWORD runCount;

// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// Get the run count of the first visible result.
runCount = Everything_GetResultRunCount(0);
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_Reset](/support/everything/sdk/everything_reset)

- [Everything_SetRequestFlags](/support/everything/sdk/everything_setrequestflags)
