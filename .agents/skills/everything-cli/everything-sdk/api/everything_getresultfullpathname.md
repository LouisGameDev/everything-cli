# Everything_GetResultFullPathName

Source: https://www.voidtools.com

# Everything_GetResultFullPathName

The **Everything_GetResultFullPathName** function retrieves the full path and file name of the visible result.

**

## Syntax

```
DWORD Everything_GetResultFullPathName(
    DWORD index,
    LPTSTR lpString,
    DWORD nMaxCount
);
```

## Parameters

*index*

Zero based index of the visible result.

*lpString* [out]

Pointer to the buffer that will receive the text. If the string is as long or longer than the buffer, the string is truncated and terminated with a NULL character.

*nMaxCount*

Specifies the maximum number of characters to copy to the buffer, including the NULL character. If the text exceeds this limit, it is truncated.

## Return Value

If lpString is NULL, the return value is the number of TCHARs** excluding the null terminator needed to store the full path and file name of the visible result.

If lpString is not NULL, the return value is the number of **TCHARs** excluding the null terminator copied into lpString.

If the function fails the return value is 0. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror).

| Error code | Description |

| EVERYTHING_ERROR_INVALIDCALL | Call [Everything_Query](/support/everything/sdk/everything_query) before calling Everything_GetResultFullPathName. |

| EVERYTHING_ERROR_INVALIDINDEX | index must be greater than or equal to 0 and less than the visible number of results. |

## Remarks

You can only call this function for a visible result. To determine if a result is visible use the [Everything_GetNumFileResults](/support/everything/sdk/everything_getnumfileresults) function.

You can mix ANSI / Unicode versions of Everything_GetResultFullPathName and Everything_Query.

## Example

```
TCHAR buf[MAX_PATH];

// set the search text to abc AND 123
Everything_SetSearch("abc 123");

// execute the query
Everything_Query(TRUE);

// Get the full path and file name of the first visible result.
Everything_GetResultFullPathName(0,buf,sizeof(buf) / sizeof(TCHAR));
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)

- [Everything_GetResultFileName](/support/everything/sdk/everything_getresultfilename)

- [Everything_GetResultPath](/support/everything/sdk/everything_getresultpath)
