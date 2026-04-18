# Everything_GetMinorVersion

Source: https://www.voidtools.com

# Everything_GetMinorVersion

The **Everything_GetMinorVersion** function retrieves the minor version number of Everything.

## Syntax

```
DWORD Everything_GetMinorVersion(void);
```

## Parameters

No parameters.

## Return Value

The function returns the minor version number.

The function returns 0 if minor version information is unavailable. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

Everything uses the following version format:

major.minor.revision.build

The build part is incremental and unique for all Everything versions.

## Example

```
DWORD majorVersion;
DWORD minorVersion;
DWORD revision;

// get version information
majorVersion = Everything_GetMajorVersion();
minorVersion = Everything_GetMinorVersion();
revision = Everything_GetRevision();

if ((majorVersion > 1) || ((majorVersion == 1) && (minorVersion > 3)) || ((majorVersion == 1) && (minorVersion == 3) && (revision >= 4)))
{
	// do something with version 1.3.4 or later
}
```

## Function Information

Requires Everything 1.0.0.0 or later.

## See Also

- [Everything_GetMajorVersion](/support/everything/sdk/everything_getmajorversion)

- [Everything_GetRevision](/support/everything/sdk/everything_getrevision)

- [Everything_GetBuildNumber](/support/everything/sdk/everything_getbuildnumber)

- [Everything_GetTargetMachine](/support/everything/sdk/everything_gettargetmachine)
