# Everything_GetSort

Source: https://www.voidtools.com

# Everything_GetSort

The **Everything_GetSort** function returns the desired sort order for the results.

## Syntax

```
DWORD Everything_GetSort(void);
```

## Return Value

Returns one of the following sort types:

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

## Remarks

The default sort is EVERYTHING_SORT_NAME_ASCENDING (1)

## Example

```
DWORD dwSort = Everything_GetSort();
```

## See Also

- [Everything_SetSort](/support/everything/sdk/everything_setsort)

- [Everything_Query](/support/everything/sdk/everything_query)
