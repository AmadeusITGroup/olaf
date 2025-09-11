# BMS Build Error Analysis Report

Generated: C:\Users\ppaccaud\coderepos\olaf-oss

**Total Errors Found:** 2

## Otf Migration (2 errors)

**Migration Guidance:** Consult 18_to_19.md OTF Migration section. Update #include <otf/RESTServiceObject.h> to #include <otf/Service.h>

### otf/ReroutingTokens.h: No such file or directory
**Occurrences:** 2
**Files affected:**
- `src/eus-channel-profiles/EusChannelProfilesRetriever.cpp:20` (Component: ahpmw::sdaExternalApi::channel)
- `src/soa-vendor-profile/SoaVendorProfileRetriever.cpp:20` (Component: ahpmw::sdaExternalApi::channel)

