# C

Source: https://www.voidtools.com

# C

Make sure to link to Everything32.lib or Everything64.lib.

Copy Everything32.dll or Everything64.dll to your programs executable directory.

Note: requires Everything running in the background.

```
#include <stdio.h>
#include "Everything.h"

int main(int argc,char **argv)
{
	DWORD i;

	// Set the search string to abc
	Everything_SetSearch("abc");

	// Execute the query.
	Everything_Query(TRUE);

	// Display results.
	for(i=0;i<Everything_GetNumResults();i++)
	{
		printf("%s [%s]\n",Everything_GetResultFileName(i),Everything_GetResultPath(i));
	}

	return 0;
}
```
