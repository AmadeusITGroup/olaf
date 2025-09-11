# BMS Commands Reference

Based on the MWPack upgrade essentials guide, here are the **valid BMS commands** that are explicitly defined and approved for use:

## VALID BMS COMMANDS

### HEALTH_CHECKS
```bash
# Dependency analysis
bms -v deps -b > bms_deps_*.log 2>&1

# Build verification  
bms build -b > bms_build_*.log 2>&1
```

### CONFIGURATION_INVESTIGATION
```bash
# Print effective bmsrc configuration
bms -s

# Find replication directory
bms -s | grep replication_dir
```

## COMMAND USAGE RULES

⚠️ **Important Restrictions:**
- **Only use commands listed above** - Ask user for any unlisted BMS commands
- **Never run multiple BMS commands simultaneously** 
- **Always redirect output to log files** in `[id:findings_dir]/obe/**BMS Project**/`
- **Use incremental log naming:** `bms_deps_*.log`, `bms_build_*.log`, `bms_test_*.log`

## PERFORMANCE CONSIDERATIONS

- BMS commands consume **significant memory and CPU resources**
- Use commands **wisely** and **one at a time**
- Always capture output in log files for analysis

## VERSION MANAGEMENT

For changing MWPack versions, you need to **manually edit the bmsrc file** (not a BMS command):

```ini
[bms]
include_conf = /opt/1A/mdw-configuration/23.0.0/bms/config/bmsrc/bmsrc.global
```

## LOG FILE LOCATIONS

- **Base directory:** `[id:findings_dir]/obe/**BMS Project**/`
- **Naming convention:** `bms_deps_*.log`, `bms_build_*.log`, `bms_test_*.log`
- **Increment numbers:** Use sequential numbers for multiple runs

## NOTES

These are the **only approved BMS commands** according to the upgrade essentials guide. Any other BMS operations require user approval first.
