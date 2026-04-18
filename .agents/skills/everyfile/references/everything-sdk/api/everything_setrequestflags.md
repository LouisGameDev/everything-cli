# Everything_SetRequestFlags

Source: https://www.voidtools.com

# Everything_SetRequestFlags

The **Everything_SetRequestFlags** function sets the desired result data.

## Syntax

```
void Everything_SetRequestFlags(
    DWORD dwRequestFlags
);
```

## Parameters

*dwRequestFlags*

The request flags, can be zero or more of the following flags:

```
EVERYTHING_REQUEST_FILE_NAME                            (0x00000001)
EVERYTHING_REQUEST_PATH                                 (0x00000002)
EVERYTHING_REQUEST_FULL_PATH_AND_FILE_NAME              (0x00000004)
EVERYTHING_REQUEST_EXTENSION                            (0x00000008)
EVERYTHING_REQUEST_SIZE                                 (0x00000010)
EVERYTHING_REQUEST_DATE_CREATED                         (0x00000020)
EVERYTHING_REQUEST_DATE_MODIFIED                        (0x00000040)
EVERYTHING_REQUEST_DATE_ACCESSED                        (0x00000080)
EVERYTHING_REQUEST_ATTRIBUTES                           (0x00000100)
EVERYTHING_REQUEST_FILE_LIST_FILE_NAME                  (0x00000200)
EVERYTHING_REQUEST_RUN_COUNT                            (0x00000400)
EVERYTHING_REQUEST_DATE_RUN                             (0x00000800)
EVERYTHING_REQUEST_DATE_RECENTLY_CHANGED                (0x00001000)
EVERYTHING_REQUEST_HIGHLIGHTED_FILE_NAME                (0x00002000)
EVERYTHING_REQUEST_HIGHLIGHTED_PATH                     (0x00004000)
EVERYTHING_REQUEST_HIGHLIGHTED_FULL_PATH_AND_FILE_NAME  (0x00008000)
```

## Return Value

This function has no return value.

## Remarks

Make sure you include EVERYTHING_REQUEST_FILE_NAME and EVERYTHING_REQUEST_PATH if you want the result file name information returned.

The default request flags are EVERYTHING_REQUEST_FILE_NAME | EVERYTHING_REQUEST_PATH (0x00000003).

When the default flags (EVERYTHING_REQUEST_FILE_NAME | EVERYTHING_REQUEST_PATH) are used the SDK will use the old version 1 query.

When any other flags are used the new version 2 query will be tried first, and then fall back to version 1 query.

It is possible the requested data is not available, in which case after you have received your results you should call [Everything_GetResultListRequestFlags](/support/everything/sdk/everything_getresultlistrequestflags) to determine the available result data.

This function must be called before [Everything_Query](/support/everything/sdk/everything_query).

## Example

```
LARGE_INTEGER size;

// set the search.
Everything_SetSearch("123 ABC");

// request filename, path, size and date modified result data.
Everything_SetRequestFlags(EVERYTHING_REQUEST_FILE_NAME | EVERYTHING_REQUEST_PATH | EVERYTHING_REQUEST_SIZE | EVERYTHING_REQUEST_DATE_MODIFIED);

// execute the query
Everything_Query(TRUE);

// Get the size of the first result.
Everything_GetResultSize(0,&size);

```

## Requirements

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_GetResultListRequestFlags](/support/everything/sdk/everything_getresultlistrequestflags)
