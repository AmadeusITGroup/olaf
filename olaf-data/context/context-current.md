# Default User Context

## Environment Configuration

### Shell & Platform
- **Shell**: PowerShell 5.1+ (Windows)
- **Platform**: Windows environment assumed

### Development Tools
- **JDK Location**: `$env:USERPROFILE\.olaf\jdk`
- **Python**: 3.12 or higher (for new scripts)
- **Script Preference**: Python scripts preferred over PowerShell/bash/zsh scripts

### User-Specific Paths
- **User Profile**: `$env:USERPROFILE` (Windows-specific)
- **OLAF Tools Directory**: `$env:USERPROFILE\.olaf\`

## Notes
This file contains user/environment-specific configurations that may vary between different development setups.
For cross-platform support, these values should be detected or configured per installation.