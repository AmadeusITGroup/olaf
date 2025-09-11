# MWPack 18→19 Migration Guide (LLM-Optimized Format)

## OVERVIEW
**Source Version:** MWPack 18  
**Target Version:** MWPack 19  
**Toolchain:** x86_64-v19 (C++17, GCC 9.x)  
**Major Changes:** Component removals/renames, SQL connection pools, AMD macro deprecation, OTF updates

---

## COMPONENT_CHANGES

### REMOVED_COMPONENTS
```yaml
- name: "mdw::FileIndex"
  reason: "Very few users, no longer maintained"
  action: "Remove all references"
  
- name: "mdw::OracleClient::InstantClient"
  reason: "OSP-like components"
  replacement: "rdb::Pack"
  action: "Migrate to rdb::Pack"
  
- name: "mdw::GmcMonitoringApi"
  reason: "ABM discontinued by end of 2019"
  related: ["mdw::MonitoringHeaders", "mdw::MonitoringAgent"]
  replacement: "ARGOS and SPLUNK"
  action: "Contact TPE-DMM-MON-MAP Team if still using ABM"
  
- name: "mdw::MonitoringHeaders"
  reason: "ABM discontinued"
  action: "Copy needed constants to your code if used internally"
  
- name: "mdw::MonitoringAgent"
  reason: "ABM discontinued"
  action: "Remove all references"
```

### RENAMED_COMPONENTS
```yaml
- old_name: "mdw::OracleClient"
  new_name: "rdb::OracleClient"
  pack: "rdb::Pack"
  migration_steps:
    - "Update Description.xml dependencies"
    - "Add rdb::Pack to application.xml/component.xml"
    - "Use CMK version >= 4-82-1-8"
    - "Replace ora10/ora11/ora18/ora19 tags with 'ora'"
    - "Use mdw::SQL::ora instead of mdw::SQL::ora19"
```

### ON_DEMAND_COMPONENTS
```yaml
- name: "mdw::IbmMq8"
  status: "Delivered by component owner on demand"
  
- name: "mdw::KVClient"
  status: "Migrated to KVClient Pack 19"
  changes: ["Header renames", "Class separations", "N1QLClient::query() removed"]
  
- name: "mdw::COM::SecureFileGatewayAccessor"
  status: "Delivered by component owner on demand"
```

---

## TOOLCHAIN_CHANGES

### TOOLCHAIN_V19
```yaml
name: "x86_64-v19"
cpp_version: "C++17 (-std=gnu++17)"
gcc_version: "GCC 9.x"
kernel_requirement: ">= 4.12"
supported_os:
  - "SLES 12 SP4 or SLES >= 15"
  - "RHEL >= 8"
  - "Ubuntu >= 16.04.4 or Ubuntu >= 18.x"
temporary_support: "RHEL 7 (kernel 3.10) until 2019"
```

---

## API_CHANGES

### SQL_CONNECTION_POOLS
```yaml
component: "mdw::SQL"
change_type: "MANDATORY"
old_behavior: "Direct UP_SQLDBConnection creation"
new_behavior: "Connection pools mandatory"
migration_steps:
  startup: "UP_SQLDBConnectionPool::Init()"
  usage: "UP_SQLActivePooledConnection activeCnx(const UP_SQLDBConnectionType&)"
  shutdown: "UP_SQLDBConnectionPool::Close()"
affected_components: ["EZT", "RFD", "History", "EOS"]
api_changes:
  - old: "GetConnection()"
    new: "GetConnectionType()"
  - old: "UP_SQLPrepQueryDefinition(char*)"
    new: "UP_SQLPrepQueryDefinition(std::string)"
```

### AMD_MACRO_DEPRECATION
```yaml
component: "mdw::CFC"
deprecated_headers:
  - "cfc/Deprecated.h"
  - "AmdDef.h"
  - "AmdInc.h"
replacement: "cfc/Def.h"
deprecated_macros:
  - old: "AMD_DEPRECATED(\"text\")"
    new: "[[deprecated(\"text\")]]"
  - old: "_AMD_ALGORITHM_H_"
    new: "<algorithm>"
  - old: "_AMD_VECTOR_H_"
    new: "<vector>"
  - old: "_AMD_STRING_H_"
    new: "<string>"
migration_script: |
  find . -type f \( -name "*.cpp" -o -name "*.hpp" \) | xargs sed -i \
    -e 's/_AMD_ALGORITHM_H_/<algorithm>/g' \
    -e 's/_AMD_VECTOR_H_/<vector>/g' \
    -e 's/_AMD_STRING_H_/<string>/g'
```

### TOOLBOX_CHANGES
```yaml
component: "mdw::Toolbox"
removed_headers: ["AMD_*.h", "TOOLInc.h", "toolbox/TOOLInc.h", "FSMInc.h"]
class_renames:
  - old: "AMD_*"
    new: "toolbox::*"
  - old: "kAMD_*"
    new: "toolbox::k*"
  - old: "AMD_*"
    new: "TBX_*"
mutex_migration:
  - old: "toolbox::ThreadMutex"
    new: "std::mutex"
  - old: "toolbox::RecursiveThreadMutex"
    new: "std::recursive_mutex"
  - old: "toolbox::RWThreadMutex"
    new: "std::shared_mutex"
  - old: "toolbox::Guard"
    new: "std::lock_guard"
deprecated_classes:
  - old: "toolbox::OString"
    new: "std::string or std::string_view"
  - old: "toolbox::Hashtable"
    new: "std::unordered_map"
```

### OTF_CHANGES
```yaml
component: "OTF"
version: "OTF 19"
toolchain_requirement: "x86_64-v19 with C++17"
deprecated_features:
  - "Transaction coordinator in multiple shot"
  - "ORG parsing in incoming messages"
migration_notes:
  - "Use single shot instead of multiple shot"
  - "Security context from DCX only, not ORG"
  - "Set OTF_SECOBJ_TO_SECCTX_MIGRATION=NOORG for testing"
```

---

## BATCH_JOB_CHANGES

### BATCH_HELPERS
```yaml
updated_scripts:
  - name: "otf_batch_launcher.sh"
    old_path: "${OBEAPP_ROOT}/cmp/shell/otf_batch_launcher.sh"
    new_path: "${OBEAPP_ROOT}/cmp/pack/MDW/bin/otf_batch_launcher.sh"
  - name: "batch_env.sh"
    old_path: "${OBEAPP_ROOT}/cmp/shell/batch_env.sh"
    new_path: "${OBEAPP_ROOT}/cmp/pack/MDW/bin/batch_env.sh"
removed_executables:
  - name: "bin/fetch_vars"
    reason: "Not changed since 2015, unreliable"
    recommendation: "Use proper OTF backend instead"
```

---

## COMPONENT_SPECIFIC_CHANGES

### POLLING_ENGINE
```yaml
component: "mdw::PollingEngine"
major_change: "Time duration type changed"
old_type: "int"
new_type: "std::chrono::steady_clock::duration"
example:
  old: "ClientProfileInfo.setITO(1)"
  new: "ClientProfileInfo.setITO(std::chrono::seconds(1))"
```

### CPPUNIT
```yaml
component: "mdw::CppUnit"
status: "DEPRECATED since pack 18, REMOVED in pack 23"
replacement: "osp::CppUnit"
breaking_changes:
  - "CPPUNIT_NS::Message in CPPUNIT_ASSERT_MESSAGE causes compilation error"
  - "Use std::string instead of CPPUNIT_NS::Message"
  - "Specify different exception type instead of std::exception"
```

### EZT_DAEMON
```yaml
component: "mdw::EZT::Daemon"
removed_variables:
  - "EZT_SYNCHRO_DAEMON_SERVER_SAP"
  - "EZT_SYNCHRO_DAEMON_SERVER_FSE"
new_requirement: "Client profile mandatory for Delta-Edifact mode"
migration_steps:
  - "Define needed client profile(s)"
  - "Set EZT_SYNCHRO_DAEMON_SERVER_CLIENTPROFILEKEY"
  - "Remove old SAP and FSE variables"
```

### XLOG_DCX
```yaml
component: "xlog_dcx.py"
old_location: "Various locations (NAS, git repos, replication folder)"
new_location: "/opt/1A/xlog-utils/latest"
import_code: |
  import sys
  sys.path.append("/opt/1A/xlog-utils/latest")
  import xlog_dcx
warning: "Version in mdw::Xlog::Instrumentation will be removed in pack 23"
```

---

## MIGRATION_SCRIPTS

### HEADER_MACRO_REPLACEMENT
```bash
# Replace AMD header macros
find . -type f \( -name "*.cpp" -o -name "*.hpp" \) | xargs sed -i \
  -e 's/_AMD_ALGORITHM_H_/<algorithm>/g' \
  -e 's/_AMD_BITSET_H_/<bitset>/g' \
  -e 's/_AMD_COMPLEX_H_/<complex>/g' \
  -e 's/_AMD_DEQUE_H_/<deque>/g' \
  -e 's/_AMD_EXCEPTION_H_/<exception>/g' \
  -e 's/_AMD_VECTOR_H_/<vector>/g' \
  -e 's/_AMD_STRING_H_/<string>/g'
```

### TOOLBOX_MUTEX_MIGRATION
```bash
# Replace toolbox mutexes with std equivalents
find . -type f \( -name "*.cpp" -o -name "*.hpp" \) | xargs sed -i \
  -e 's/toolbox::ThreadMutex/std::mutex/g' \
  -e 's/toolbox::RecursiveThreadMutex/std::recursive_mutex/g' \
  -e 's/toolbox::RWThreadMutex/std::shared_mutex/g' \
  -e 's/toolbox::Guard/std::lock_guard/g' \
  -e 's/toolbox::ReadGuard/std::shared_lock/g' \
  -e 's/toolbox::WriteGuard/std::lock_guard/g'
```

---

## MIGRATION_CHECKLIST

### PRE_MIGRATION
- [ ] Update to toolchain x86_64-v19
- [ ] Ensure Linux kernel >= 4.12
- [ ] Update CMK to version >= 4-82-1-8

### COMPONENT_UPDATES
- [ ] Remove references to deleted components
- [ ] Update mdw::OracleClient to rdb::OracleClient
- [ ] Add rdb::Pack to application.xml/component.xml
- [ ] Replace ora18/ora19 tags with 'ora'

### CODE_CHANGES
- [ ] Replace AMD header macros with standard headers
- [ ] Update AmdDef.h includes to cfc/Def.h
- [ ] Migrate toolbox mutexes to std equivalents
- [ ] Update SQL connection handling to use pools
- [ ] Replace deprecated CppUnit usage

### BATCH_JOBS
- [ ] Update batch script paths
- [ ] Remove fetch_vars usage
- [ ] Test batch job execution

### VALIDATION
- [ ] Build with new toolchain
- [ ] Test SQL connection pooling
- [ ] Verify OTF functionality
- [ ] Check batch job execution

---

## GOTCHA_SECTIONS

### GOTCHA: Unit Tests with RFD and Oracle DB Connections

**Problem**: Pool is not initialized errors in unit tests
```
<UP_SQLDBConnectionPool.cpp#156 TID#86399488> Pool is not initialized in UT stdout
```

**Solution**: Update ConnectionPoolRaiiHelper
```cpp
#pragma once
#include <UP_SQLDBConnectionPool.h>
#include <UP_SQLDBConnectionType.h>
#include <RFD_ApiConnectionHandler.h>  // NEW LINE

class ConnectionPoolRaiiHelper {
private:
  struct InternalHelper {
    InternalHelper() {
      UP_SQLDBConnectionPool::Init();
      RFD_ApiConnectionHandler::Init(); // NEW LINE
    }
    ~InternalHelper() {
      RFD_ApiConnectionHandler::Close();  // NEW LINE
      UP_SQLDBConnectionPool::Close();
    }
  };
  InternalHelper _internalHelper;
  UP_SQLActivePooledConnection _cnx;
public:
  ConnectionPoolRaiiHelper(const std::string& iDbSchema,
                           const std::string& iDbService,
                           const std::string& iDbUser,
                           const std::string& iDbPassword)
      : _cnx(UP_SQLDBConnectionType(iDbSchema, iDbService, iDbUser, iDbPassword)) {}
  ~ConnectionPoolRaiiHelper() = default;
};
```

### GOTCHA: Oracle & UPSQL & UP_SQLInputRow and UP_SQLOutputRow

**Issue**: UP_SQLInputRow and UP_SQLOutputRow can't be reused in many queries
**Solution**: Clear before reuse or create new instances

### GOTCHA: Float Comparison Warning as Error

**Solution**: Use disable pragmas in minimal scope
```cpp
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wfloat-equal"
// your comparison code
#pragma GCC diagnostic pop
```

## KVCLIENT_CHANGES

### Headers Renamed
- Classes previously bundled together separated to different hpp/cpp files
- Methods removed (e.g., `::query()` under N1QLClient)
- Migration to KvClient Pack 19 required

### API Changes
```yaml
header_changes:
  - old: "#include <kvclient/old_header.h>"
    new: "#include <kvclient/new_header.h>"
    
method_removals:
  - class: "N1QLClient"
    method: "::query()"
    replacement: "Use new query methods"
```

## SECURITY_CHANGES

### Security Tokens/Keys Version 2 Removed
- Deprecated since pack 15
- `kSecTokenVersion_V2` no longer valid
- Only use `kSecTokenVersion_V1`

### OTF Variable Changes
```yaml
default_changes:
  - variable: "OTF_SECOBJ_TO_SECCTX_MIGRATION"
    old_default: "(varies)"
    new_default: "NOORG"
    impact: "Ignores ORG buffer when building security object"
    
  - variable: "OTF_DAEMON_RESET_DCX_EACH_RUN"
    old_default: "no"
    new_default: "yes"
    impact: "GCX and DCX reset before each daemon loop run"

removed_variables:
  - "OTF_ENABLE_CLIENT_CALL_INDEX_LOGGING"
  - "OTF_BEINFOS_SERIALIZATION_VERSION"
```

## DU_COMPATIBILITY

### Frontend/Backend
- OTF frontend 19 no longer delivered
- Test compatibility with `OTF_BEINFOS_SERIALIZATION_VERSION=2`

### HACS/Context Server Compatibility
```yaml
compatible_versions:
  - ">= 16-0-0-70"
  - ">= 18"
  - ">= 19"
  
upgrade_path:
  note: "Cannot directly upgrade from MWPack <= 15 to MWPack 19"
  required: "Must go through MWPack 16 or 18 first"
```

## DETAILED_API_CHANGES

### PeakToken Interface Refactoring
```yaml
file_renames:
  - old: "otf/ReroutingTokens.h"
    new: "otf/PeakReroutingToken.h"
    
class_changes:
  - old: "DynamicReroutingToken"
    status: "REMOVED"
    replacement: "PeakReroutingToken"
    
  - old: "OutboundReroutingToken"
    new: "DynamicOsapToken"
    
method_renames:
  ClientSession:
    - old: "setDynamicReroutingTokenList(const DynamicReroutingTokenPtrList&)"
      new: "setPeakReroutingTokenList(const PeakReroutingTokenPtrList&)"
    - old: "setDynamicReroutingToken(const DynamicReroutingToken&)"
      new: "setPeakReroutingToken(const PeakReroutingToken&)"
    - old: "delDynamicReroutingTokenList()"
      new: "delPeakReroutingTokenList()"
```

### Security Token TTL Changes
```yaml
type_change:
  old: "unsigned int"
  new: "std::chrono::steady_clock::duration&"
  
affected_methods:
  - class: "otf::resources::Sender"
    method: "setSecurityTokenConfiguration"
  - class: "otf::Sender"
    method: "setSecurityTokenConfiguration"
  - class: "otf::ClientSession"
    methods: ["setSecurityTokenConfiguration", "getSecurityTokenTimeValidity"]
```

### Non-Copyable Classes
```yaml
no_copy_classes:
  - "ContextServer"
  - "CoordinatedReply"
  - "CrypticContext"
  - "CrypticPayloadOptions"
  - "CrypticServiceObject"
  - "DaemonObject"
  - "EdifactTools"
  - "EtoHandler"
  - "ExecutionTimeHandler"
  - "FlipManager"
  - "InboundCrypticMessage"
  - "InboundEdifactMessage"
  - "InboundMessage"
  - "InboundXMLMessage"
  - "InitializerObject"
  - "InitializerWrapper"
  - "InjectorObject"
  - "LocalObject"
  - "LocalServiceWrapper"
  - "MissingContextHandlerWrapper"
  - "Node"
  - "ObjectWrapper"
  - "PanelManager"
  - "Payload"
  - "PayloadUtils"
  - "ProcessWrapper"
  - "QueuesManager"
  - "RegistrationManager"
  - "Resources"
  - "RESTServiceObjectRegistrationManager"
  - "RESTServicePlugin"
  - "RESTServicePluginList"
  - "RunnableObject"
  - "SecurityManager"
  - "Sender"
  - "ServiceMiddlewarePluginList"
  - "ServiceObject"
  - "SignOutConfig"
  - "StatisticsManager"
  - "TimerManager"
  - "TransactionContext"
  - "TransactionCoordinator"
  - "TransactionCoordinatorInfos"
```

### Class Renames
```yaml
class_renames:
  - old: "otf::RESTServiceObject"
    new: "otf::Service"
    compatibility: "mdw 15"
  - old: "otf::RESTServiceObjectAllocatorInterface"
    new: "otf::ServiceAllocatorInterface"
    compatibility: "mdw 15"
  - old: "otf::RESTServiceObjectAllocatorBaseInterface"
    new: "otf::ServiceAllocatorBaseInterface"
  - old: "otf::StandardRESTServiceObjectAllocator"
    new: "otf::StandardServiceAllocator"
  - old: "otf::RESTServiceObjectDefaultAllocator"
    new: "otf::ServiceDefaultAllocator"
  - old: "otf::RESTServiceObjectInterface"
    new: "otf::ServiceInterface"
  - old: "enum otf::encoding::Format_t"
    new: "enum class otf::Encoding"
    change: "otf::encoding::kUTF8 → otf::Encoding::kUTF8"
```

### Removed Security Functions
```yaml
removed_methods:
  - class: "otf::SecurityManager"
    methods:
      - "getSecurityMapper"
      - "signSecurityContextWithOrgIfNotAlreadySigned"
    note: "Contact OTF team if blocking migration"
```

### Flip-Related Removals
```yaml
removed_flip_methods:
  - method: "otf::FlipManager::GetUntoForMux"
    reason: "1ASRFLIP SAPs decommissioned in PRD summer 2022"
    
migration_actions:
  - "Stop using SAPs named 1ASRFLIP*"
  - "Use flip farm SAPs (FLP* in PRD)"
  - "Define flip SAP at farm level, not mux level"
  - "Update non-regression tests to remove 1ASRFLIP prefixes"
```

### Protobuf API Migration
```yaml
protobuf_changes:
  dependency_change:
    old: "mdw::OTF::ProtobufFramework::Protobuf"
    new: "mdw::OTF"
    
  include_changes:
    old: "#include \"otf/protobuf/*.h\""
    new: "#include \"otf/*.h\""
    
  namespace_changes:
    old: "otf::protobuf::"
    new: "otf::"
    
  sed_commands:
    - "sed -i 's|otf/protobuf/|otf/|g' **/*.cpp **/*.h"
    - "sed -i 's/otf::protobuf::/otf::/g' **/*.cpp **/*.h"
```

### HTTP Header Value Changes
```yaml
http_header_changes:
  deprecated_methods:
    - "getValue()" # Gets truncated value before semicolon
    - "getOptions()" # Gets options after semicolon
    
  new_methods:
    - "getRawValue()" # Gets complete header value
    - "setRawValue()"
    - "parseMainValueAndOptions()" # For Content-Type headers
    - "setMainValueAndOptions()"
    
  removal_timeline: "OTF 25"
```

## KITPACK_DETAILED_CHANGES

### kitCommon: Deprecated API Removed
```yaml
status: "Deprecated APIs removed (were warnings in MWP21)"
recommendation: "OK to use - actively maintained"
action: "Fix all build warnings before migration"
```

### kitField: validate() API Changed
```yaml
api_change:
  old_signature: "const T& validate(const T&) override"
  new_signature: "void validate() override"
  
reason: "Mixed overriding with shadowing - bad design"

migration_sed_commands:
  - "sed -i -e 's/virtual const std::string& validate(const std::string .*\([;{]\)/void validate() override\1/g' **/*/Fld*hpp"
  - "sed -i -e 's/^const std::string& \(Fld.*\)::validate(const std::string& iValue) {/void \1::validate() override {/g' **/*/Fld*cpp"
  - "sed -i -e 's/virtual int32_t validate(int32.*\([;{]\)/void validate() override \1/g' **/*/Fld*hpp"
  
recommendation: "AVOID - design concerns with delayed exceptions"
```

### kitHac: No API Change
```yaml
status: "Same old odd API"
recommendation: "MUST use for Hotel IT/LinkHotel projects"
reason: "Plain GAC doesn't enforce Hotel IT Security Model"
issues: "Performance issues due to design flaws"
```

### kitSimpleType: Few API Changes
```yaml
changes:
  - "Removed kit::Factory useless create methods (constructors are public)"
  - "Altered StyPeriod::toDOWPatternPeriods() signature"
  
legacy_support:
  fallback: "KIT::Factory<StyType>::instance->create(constructor parameters)"
  
signature_change:
  old: "vector of KIT::factory allocated pointers"
  new: "plain vector"
```

## MIGRATION_CHECKLIST

### Pre-Migration Assessment
- [ ] **Review all OTF variable settings**
- [ ] **Identify usage of deprecated security functions**
- [ ] **Check for 1ASRFLIP SAP usage**
- [ ] **Audit Protobuf include statements**
- [ ] **Review HTTP header value usage**
- [ ] **Check for non-copyable class usage**
- [ ] **Identify PeakToken/DynamicReroutingToken usage**
- [ ] **Review kitField validate() implementations**
- [ ] **Check unit test connection pool helpers**

### Migration Execution
- [ ] **Update OTF variables (remove deprecated ones)**
- [ ] **Replace security token version references**
- [ ] **Update flip SAP definitions to farm level**
- [ ] **Migrate Protobuf includes and namespaces**
- [ ] **Update HTTP header value API calls**
- [ ] **Fix class rename references**
- [ ] **Update PeakToken method calls**
- [ ] **Modify kitField validate() signatures**
- [ ] **Update ConnectionPoolRaiiHelper for RFD**

### Post-Migration Validation
- [ ] **Compile with all warnings enabled**
- [ ] **Run full unit test suite**
- [ ] **Test database connection pools**
- [ ] **Verify flip functionality**
- [ ] **Check security token generation**
- [ ] **Validate HTTP header processing**
- [ ] **Performance regression testing**
- [ ] **Update build scripts and CI/CD**
