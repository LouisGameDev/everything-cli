# Everything_GetBuildNumber

Source: https://www.voidtools.com

# Everything_GetBuildNumber

The **Everything_GetBuildNumber** function retrieves the build number of Everything.

## Syntax

```
DWORD Everything_GetBuildNumber(void);
```

## Parameters

No parameters.

## Return Value

The function returns the build number.

The function returns 0 if build information is unavailable. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

Everything uses the following version format:

major.minor.revision.build

The build part is incremental and unique for all Everything versions.

## Example

```
DWORD buildNumber;

// get the build number
buildNumber = Everything_GetBuildNumber();

if (buildNumber >= 686)
{
	// do something with build 686 or later.
}
```

## Function Information

Requires Everything 1.0.0.0 or later.

## See Also

- [Everything_GetMajorVersion](/support/everything/sdk/everything_getmajorversion)

- [Everything_GetMinorVersion](/support/everything/sdk/everything_getminorversion)

- [Everything_GetRevision](/support/everything/sdk/everything_getrevision)

- [Everything_GetTargetMachine](/support/everything/sdk/everything_gettargetmachine)
