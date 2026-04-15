# Everything_SortResultsByPath

Source: https://www.voidtools.com

# Everything_SortResultsByPath

The **Everything_SortResultsByPath** function sorts the current results by path, then file name.

SortResultsByPath is CPU Intensive. Sorting by path can take several seconds.

## Syntax

```
void Everything_SortResultsByPath(void);
```

## Parameters

This functions has no parameters.

## Return Value

This function has no return value.

## Remarks

The default result list contains no results.

Call [Everything_Query](/support/everything/sdk/everything_query) to retrieve the result list prior to a call to Everything_SortResultsByPath.

For improved performance, use [Everything/SDK/Everything_SetSort|Everything_SetSort]]

## Example

```
// set the search text to abc AND 123
Everything_SetSearch(\"abc 123\");

// execute the query
Everything_Query(TRUE);

// sort the results by path
Everything_SortResultsByPath();
```

## See Also

- [Everything_Query](/support/everything/sdk/everything_query)
