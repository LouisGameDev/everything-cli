# Everything_GetTargetMachine

Source: https://www.voidtools.com

# Everything_GetTargetMachine

The **Everything_GetTargetMachine** function retrieves the target machine of Everything.

## Syntax

```
DWORD Everything_GetTargetMachine(void);
```

## Parameters

No parameters.

## Return Value

The function returns one of the following:

| Macro | Meaning |

| EVERYTHING_TARGET_MACHINE_X86 (1) | Target machine is x86 (32 bit). |

| EVERYTHING_TARGET_MACHINE_X64 (2) | Target machine is x64 (64 bit). |

| EVERYTHING_TARGET_MACHINE_ARM (3) | Target machine is ARM. |

| EVERYTHING_TARGET_MACHINE_ARM64 (4) | Target machine is ARM64. |

The function returns 0 if target machine information is unavailable. To get extended error information, call [Everything_GetLastError](/support/everything/sdk/everything_getlasterror)

| Error code | Meaning |

| EVERYTHING_ERROR_IPC | Please make sure the Everything search client is running in the background. |

## Remarks

Everything uses the following version format:

major.minor.revision.build

The build part is incremental and unique for all Everything versions.

## Example

```
DWORD targetMachine;

// Get the attributes of the first visible result.
targetMachine = Everything_GetTargetMachine();

if (targetMachine == EVERYTHING_TARGET_MACHINE_X64)
{
	// do something with x64 build.
}
else
if (targetMachine == EVERYTHING_TARGET_MACHINE_X86)
{
	// do something with x86 build.
}
```

## Function Information

Requires Everything 1.4.1 or later.

## See Also

- [Everything_GetMajorVersion](/support/everything/sdk/everything_getmajorversion)

- [Everything_GetMinorVersion](/support/everything/sdk/everything_getminorversion)

- [Everything_GetRevision](/support/everything/sdk/everything_getrevision)

- [Everything_GetBuildNumber](/support/everything/sdk/everything_getbuildnumber)
