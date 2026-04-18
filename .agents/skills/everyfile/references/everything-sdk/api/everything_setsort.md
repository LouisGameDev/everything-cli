# Everything_SetSort

Source: https://www.voidtools.com

# Everything_SetSort

The **Everything_SetSort** function sets how the results should be ordered.

**

## Syntax

```
void Everything_SetSort(
    DWORD dwSortType
);
```

## Parameters

*dwSortType*

The sort type, can be one of the following values:

```
EVERYTHING_SORT_NAME_ASCENDING                      (1)
EVERYTHING_SORT_NAME_DESCENDING                     (2)
EVERYTHING_SORT_PATH_ASCENDING                      (3)
EVERYTHING_SORT_PATH_DESCENDING                     (4)
EVERYTHING_SORT_SIZE_ASCENDING                      (5)
EVERYTHING_SORT_SIZE_DESCENDING                     (6)
EVERYTHING_SORT_EXTENSION_ASCENDING                 (7)
EVERYTHING_SORT_EXTENSION_DESCENDING                (8)
EVERYTHING_SORT_TYPE_NAME_ASCENDING                 (9)
EVERYTHING_SORT_TYPE_NAME_DESCENDING                (10)
EVERYTHING_SORT_DATE_CREATED_ASCENDING              (11)
EVERYTHING_SORT_DATE_CREATED_DESCENDING             (12)
EVERYTHING_SORT_DATE_MODIFIED_ASCENDING             (13)
EVERYTHING_SORT_DATE_MODIFIED_DESCENDING            (14)
EVERYTHING_SORT_ATTRIBUTES_ASCENDING                (15)
EVERYTHING_SORT_ATTRIBUTES_DESCENDING               (16)
EVERYTHING_SORT_FILE_LIST_FILENAME_ASCENDING        (17)
EVERYTHING_SORT_FILE_LIST_FILENAME_DESCENDING       (18)
EVERYTHING_SORT_RUN_COUNT_ASCENDING                 (19)
EVERYTHING_SORT_RUN_COUNT_DESCENDING                (20)
EVERYTHING_SORT_DATE_RECENTLY_CHANGED_ASCENDING     (21)
EVERYTHING_SORT_DATE_RECENTLY_CHANGED_DESCENDING    (22)
EVERYTHING_SORT_DATE_ACCESSED_ASCENDING             (23)
EVERYTHING_SORT_DATE_ACCESSED_DESCENDING            (24)
EVERYTHING_SORT_DATE_RUN_ASCENDING                  (25)
EVERYTHING_SORT_DATE_RUN_DESCENDING                 (26)
```

## Return Value

This function has no return value.

## Remarks

The default sort is EVERYTHING_SORT_NAME_ASCENDING (1). This sort is free.

Using fast sorts is recommended, fast sorting is instant.

To enable fast sorts in Everything:

- In Everything**, from the **Tools** menu, click **Options**.

- Click the **Indexes** tab.

- Check **fast sort** for desired fast sort type.

- Click **OK**.

It is possible the sort is not supported, in which case after you have received your results you should call *[Everything_GetResultListSort](/support/everything/sdk/everything_getresultlistsort) to determine the sorting actually used.

This function must be called before [Everything_Query](/support/everything/sdk/everything_query).

## Example

```
// set the search.
Everything_SetSearch("123 ABC");

// sort by size descending.
Everything_SetSort(EVERYTHING_SORT_SIZE_DESCENDING);

// execute the query
Everything_Query(TRUE);
```

## Requirements

Requires Everything 1.4.1 or later.

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)
