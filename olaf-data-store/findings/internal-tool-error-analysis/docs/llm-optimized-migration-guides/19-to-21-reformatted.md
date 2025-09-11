# MWPack 19→21 Migration Guide (LLM-Optimized Format)

## OVERVIEW
**Source Version:** MWPack 19  
**Target Version:** MWPack 21  
**Toolchain:** x86_64-v21 (C++20, GCC 11.x)  
**Major Changes:** C++20 adoption, batch_env.sh deprecation, changelog integration, component updates

---

## COMPONENT_CHANGES

### REMOVED_COMPONENTS
```yaml
- name: "mdw::Web::HtmlTools"
  reason: "No longer used"
  action: "Remove all references"
```

### LATE_COMPONENTS
```yaml
- name: "mdw::KVClient"
  status: "Not delivered in initial R21 releases"
  availability: "Added by end of 2021"
  action: "Check KVClient section for migration details"
```

---

## TOOLCHAIN_CHANGES

### TOOLCHAIN_V21
```yaml
name: "x86_64-v21"
cpp_version: "C++20 (-std=gnu++20)"
gcc_version: "GCC 11.x"
naming_convention: "Same as v19 (differs from packs <= 18)"
unsupported_os: ["SLES 11", "RHEL 7 (potentially)"]
migration_guide: "From toolchain v19 (GCC 9.x/-std=gnu++17) to toolchain v21 (GCC 11.x/-std=gnu++20)"
```

---

## BMS_CONFIG_CHANGES

### CHANGELOG_INTEGRATION
```yaml
feature: "Changelog plugin enabled by default"
scope: "All MDW components deliveries from R21"
output: "Changelog JSON file in doc artifact"
access_methods: ["Packboard", "Direct download"]
commit_message_importance: "High - used for changelog generation"
```

### MANUAL_DELIVERIES
```yaml
requirement: "Pull all tags locally"
command: "git fetch --tags"
```

### CICD_DELIVERIES
```yaml
jenkins_setting: "Fetch tags"
location: "Branch sources → Advanced Clone Behaviours"
frequency: "One-time setup per component"
```

### DISABLE_CHANGELOGS
```yaml
config_file: "Project BMS configuration file"
setting: |
  [deliver]
  plugins -= changelog
```

---

## BATCH_JOB_CHANGES

### BATCH_ENV_DEPRECATION
```yaml
deprecated_script: "bin/batch_env.sh"
reason: "Error-prone sourcing of toolchain environment"
problem: "System executables fail due to library conflicts"
replacement: "bin/non_otf_batch_launcher.sh"
usage: "Wrapper script - pass executable and arguments"
migration_example: |
  OLD: . ${OBEAPP_ROOT}/jfk/pack/MDW/bin/batch_env.sh ${COMP}
       ${aBin} -P $PHASE $@
  NEW: "${OBEAPP_ROOT}/${COMP}/pack/MDW/bin/non_otf_batch_launcher.sh" "${aBin}" -P "${PHASE}" "$@"
```

---

## API_CHANGES

### TOOLBOX_CHANGES
```yaml
component: "mdw::Toolbox"
breaking_changes:
  - change: "BoundedString operator!= behavior"
    reason: "C++20 compliance - operator== and operator!= must be equivalent"
    migration: "Avoid using operator!= with BoundedString and std::string"
    detection: "Build warnings about deprecated declarations"
    
deprecated_classes:
  - old: "toolbox::OString"
    new: "std::string (when owning) or std::string_view (when not owning)"
    serialization_warning: "OString serialization != std::string serialization"
    
  - old: "toolbox::Hashtable"
    new: "std::unordered_map"
    
  - old: "toolbox::Hash"
    new: "std::hash"
    char_pointer_warning: "Use std::hash<std::string_view> for char*/const char*"

poisoned_macros:
  - "_MDW_STACK_AUTO_"
  - "_MDW_ADD_STACKFRAME_"
  - "__AMD_FUNCNAME__"

deprecated_constructors:
  - "toolbox::Unmarshaller copy constructor (deprecated since pack 15)"
```

### ABRCLIENT_CHANGES
```yaml
component: "ABRClient"
new_parameter: "Blob data type encoding parameter"
affected_methods:
  - "createRule"
  - "updateRule"
  - "createRules"
  - "updateRules"
  - "validateCreateRule"
  - "validateUpdateRule"
  - "createTemporaryRule"
  - "createPendingCreateRule"
  - "createPendingUpdateRule"
parameter_details:
  type: "bool"
  default: "false"
  purpose: "Encode rule content as blob data type"
```

### ACF_DECOMMISSIONING
```yaml
component: "mdw::ACF"
status: "DECOMMISSIONING"
valid_users: ["SI", "OTF", "Tracer"]
action: "Remove all references from repositories"
documentation: "mdw::ACF decommissioning guide"
```

### CACHE_FRAMEWORK
```yaml
component: "CacheFramework"
status: "DEPRECATED"
synchronization_replacement: "GMC"
cache_replacement: "Redesign avoiding HeapFileMap"
```

### CRYPTO_MANAGER
```yaml
component: "CryptoManager"
enforcement: "Configuration file permissions (was warning, now enforced)"
failure_behavior: "Component refuses to start if permissions incorrect"
documentation: "Permissions of configuration file"
```

### DATABASE_CHANGES
```yaml
component: "DBConfParser and OHF"
removed_elements:
  - "TAF (Transaction Application Failover)"
  - "FAN (Fast Application Notification)"
config_file: "databases.xml"
removed_xml: |
  <taf>
    <retries>10</retries>
    <delay>100</delay>
  </taf>
  <fan_mode>OFF</fan_mode>

ohf_changes:
  removed_headers: "ohf/gd folder headers"
  replacement: "Use mdw::OHF::main headers"
  impact: "Should be none if using correct headers"
```

### EZT_CHANGES
```yaml
component: "EZT"
breaking_change: "BindKey() and BindValue() implementations"
issue: "UP_SQL no longer tolerates reusing UP_SQLInputRow/UP_SQLOutputRow without cleaning"
failure_mode: "Exception thrown"
action: "Rework implementations to clean objects before reuse"
```

---

## COMPONENT_SPECIFIC_CHANGES

### QFC_CHANGES
```yaml
component: "QFC"
removed_headers: "Unspecified headers removed"
removed_features: "Option Setters removal"
miscellaneous: "Various other changes"
```

### QUEUING_SERVER
```yaml
component: "QueuingServer (LQS/GQS)"
alias: ["LQS", "GQS"]
changes: "See OTF migration guide for details"
```

### TBF_API
```yaml
component: "TBF::api"
changes: "Unspecified API changes"
```

### TRACER_CHANGES
```yaml
component: "Tracer"
changes: "Unspecified changes"
```

### UP_SQL_CHANGES
```yaml
component: "UP_SQL"
changes: "Unspecified changes"
```

### WEB_HTMLKIT
```yaml
component: "Web::HtmlKit"
changes: "Unspecified changes"
```

### CPPUNIT_CONTINUATION
```yaml
component: "mdw::CppUnit"
status: "Still deprecated (removal in pack 23)"
replacement: "osp::CppUnit"
```

### WEB_FRAMEWORK
```yaml
component: "mdw::Web::Framework"
changes: "Unspecified changes"
```

### XLOG_DCX_CONTINUATION
```yaml
component: "xlog_dcx"
status: "Continue using /opt/1A/xlog-utils/latest"
warning: "mdw::Xlog::Instrumentation version will be removed in pack 23"
```

---

## MIGRATION_CHECKLIST

### PRE_MIGRATION
- [ ] Update to toolchain x86_64-v21 (C++20, GCC 11.x)
- [ ] Review C++20 compatibility of existing code
- [ ] Ensure Jenkins CI/CD fetches tags

### DETAILED_COMPONENT_CHANGES

### GdmContainerGenerator
```yaml
requirements:
  java_version: ">=8"
platform_support:
  windows_cygwin: "REMOVED"
  reason: "Support abandoned"
```

### HeapFileMap
```yaml
api_changes:
  private_members:
    - "heapfilemap::ref internal data"
    - "heapfilemap::const_ref internal data"
    - "heapfilemap::Array internal data"
  
recommendation: "AVOID - use boost::interprocess alternative"
reason: "Maintenance difficulty across GCC versions"
backward_compatibility: "No serialization format compatibility"
```

### TBF_API_DETAILED
```yaml
component: "TBF::api"
removed_methods:
  - name: "tbf::TransactionBilling::SetUseIDs"
    replacement: "tbf::TransactionBilling::SetFormattingPolicy"
    values:
      true: "kPolicy_IdInCarf"
      false: "kPolicy_NoFormatting"
  - name: "tbf::TransactionBilling::SetAggregationBufferSize"
    replacement: "Remove call entirely"
  - name: "tbf::TransactionBilling::SetCheckpointRate"
    replacement: "Remove call entirely"
```

### TRACER_DETAILED
```yaml
component: "Tracer"
removed_deprecated_files:
  - old: "TRC_Exception.h"
    new: "tracer/Exception.h"
  - old: "TRC_Trace.h"
    new: "tracer/Trace.h"
```

### UP_SQL_DETAILED
```yaml
component: "UP_SQL"
changes:
  oracle_connection_pooling:
    default: "OCI session pool (Oracle client built-in)"
    availability: "Since MW Pack R15 with Oracle client 18c"
    configuration: 'OVA "useOCIPool" set to "Y" (requires recycle)'
    recommendation: "Use OCI session pool"
  
  removed_components:
    - "UP_SQLTrafficWriter (SQL query dump to file - never used)"
  
  breaking_changes:
    issue: "UP_SQLInputRow and UP_SQLOutputRow can't be reused without clearing"
    error: "Index out of range on second execute"
    solution: "Call Clear() before reuse"
    example: |
      UP_SQLInputRow aInRow;
      UP_SQLOutputRow aOutRow;
      aInRow << ... << endr;
      aOutRow << ... << endr;
      aQuery.execute(aInRow, aOutRow);    // 1st time OK
      
      aInRow.Clear();  // REQUIRED
      aOutRow.Clear(); // REQUIRED
      aInRow << ... << endr;
      aOutRow << ... << endr;
      aQuery.execute(aInRow, aOutRow);    // OK
  
  taf_removal:
    removed_config_items:
      - "FAILOVER_RETRIES_TYPE"
      - "FAILOVER_INFINITE_RETRIES_TYPE"
      - "FAILOVER_DELAY_TYPE"
      - "FAILOVER_CALLBACK_TYPE"
    removed_operator: "UP_SQLDBConnectionConfigurationItem operator()(void (*callback)()) const"
  
  tag_migration:
    old_tags: ["ora10", "ora11", "ora18", "ora19"]
    new_tag: "ora"
    locations: "CMK configurations/deployment.xml"
    namespace_change: "mdw::SQL::ora19 → mdw::SQL::ora"
```

### WEB_HTMLKIT_DETAILED
```yaml
component: "Web::HtmlKit"
removal_notice: "FusionChart/FusionMap Libraries removed from all MDW major releases"
action: "Migrate to alternative charting library of choice"
```

### CPPUNIT_DETAILED
```yaml
component: "mdw::CppUnit"
status: "Deprecated since branch 18, removed in Pack 23"
replacement: "osp::CppUnit (more recent version)"
code_changes:
  compilation_errors:
    - issue: "CPPUNIT_NS::Message in CPPUNIT_ASSERT_MESSAGE"
      solutions:
        - "Inline string directly in CPPUNIT_ASSERT_MESSAGE macro"
        - "Use std::string instead of CPPUNIT_NS::Message"
      examples:
        - "https://rndwww.nce.amadeus.net/git/projects/MWP/repos/sic/commits/ac099be419915c3cd891d76bd23ec12da4c5afa4"
        - "https://rndwww.nce.amadeus.net/git/projects/DATREP/repos/gmc/pull-requests/663/diff"
  
  exception_handling:
    issue: "Tests checking std::exception"
    problem: "osp::CppUnit already catches std::exception"
    solution: "Specify another exception type"
    example: "https://rndwww.nce.amadeus.net/git/projects/DSM/repos/queuingserver/commits/d9714727b7ab8522e6bfa42c6b221f3e564fed21"
```

### WEB_FRAMEWORK_DETAILED
```yaml
component: "mdw::Web::Framework"
breaking_change: "Grammar headers made private in pack 23"
removed_includes:
  - "webFramework/HtmlConversation_Grammar.h"
  - "webFramework/HtmlConversationGrammar_sax.h"
reason: "Exposing implementation details of internal grammar"
new_api:
  method: "WebFramework::Grammar::RegisterGrammars(otf::RegistrationManager&)"
  include: "webFramework/Grammar.h"
migration_example: |
  OLD:
  #include "webFramework/HtmlConversation_Grammar.h"
  aRegistrationManager.registerEdifactGrammar(WebFramework::HtmlConversation_Grammar::getInstance());
  
  NEW:
  #include "webFramework/Grammar.h"
  WebFramework::Grammar::RegisterGrammars(aRegistrationManager);
```

### XLOG_DCX_DETAILED
```yaml
component: "xlog_dcx"
stable_path: "/opt/1A/xlog-utils/latest"
usage_example: |
  import sys
  sys.path.append("/opt/1A/xlog-utils/latest")
  import xlog_dcx
deprecation:
  warning: "mdw::Xlog::Instrumentation version emits warning in packs <= 21"
  removal: "Will be removed from pack 23"
action: "Stop copying file to git repository, use stable path"
```

---

## OTF_21_MIGRATION

### OTF_OVERVIEW
```yaml
version: "OTF 21"
similarity: "Pretty similar to branch 19 from client perspective"
toolchain: "Only supports toolchain v21 with -std=gnu++20"
migration_guide: "From toolchain v19 (GCC 9.x/-std=gnu++17) to toolchain v21 (GCC 11.x/-std=gnu++20)"
```

### QUEUING_SERVER_STANDALONE
```yaml
use_case: "Binaries connecting to queuing server (not OTF backends)"
valid_scope: "Local regression only, NOT production"
component: "mdw::OTF::internal::QueuingServerStandaloneImplementation"
status: "Internal component - use at own risk"
supported_users: ["AML application", "mdw::QueuingServer team"]
api_guarantee: "NO API/ABI compatibility guarantee"
usage_mode: 'aggregation (mode="aggregated" in BMS <dependency> tag)'
warning: "May delete old releases (>6 months) at any time"
recommendation: "Create actual OTF batch instead of standalone binary"
```

### DU_COMPATIBILITY
```yaml
frontend_backend:
  otf_frontend_21_works_with:
    not_supported: ["Any backend 14"]
    supported:
      - "OTF backend >= 15-0-0-141 (MWPack 15 deprecated 2020)"
      - "OTF backend >= 16-0-0-155 (MWPack 16 deprecated 2021)"
      - "OTF backend >= 18-0-0-100"
      - "OTF backend >= 19-0-0-59"
      - "Any OTF backend >= 21"

hacs_context_server:
  hacs_21_works_with:
    - "Context server >= 18-0-0-106"
    - "Context server >= 19-0-0-66"
    - "Any context server >= 21"
  note: "CS/HACS version determined by OTF ULAM component (same as frontend)"
```

### OTF_VARIABLE_CHANGES
```yaml
default_value_changes:
  - variable: "OTF_ENABLE_DISTRIBUTED_CONTEXT_FOR_BATCH_AND_DAEMON"
    old_default: "Disabled"
    new_default: "Enabled (Batch and Daemon WILL generate DCX)"
    disable_option: 'Set to "no" to disable'
    future: "Disable option removed in pack 23"

removed_variables:
  - name: "ApplicationName"
    replacement: "ApplicationServerName (returns same value)"
    compatibility: "Change works in mdw branches 18, 16, 15, 14 and before"
    application_name_alternative: "Use OTF variable APPLICATION"
  
  - name: "OTF_ATTACH_CONTEXT"
    reason: "Applicative contexts now always attached to server conversation"
  
  - name: "OTF_PEAK_TOKEN_STD_MERGE"
    reason: "Peak tokens in DCX now follow standard merge strategy"
  
  - name: "OTF_HANDLE_HACS_CLIENT_CONV_KEEPALIVE_ON_BE"
    reason: "ITO on client conversations from HACS now always handled on backend"
  
  - name: "OTF_DAEMON_RESET_DCX_EACH_RUN"
    consequence: "Both GCX and DCX reset before each daemon loop run"
    historical_behavior: "NOT reset (before 04 Aug 2021)"
```

### TRANSACTION_COORDINATOR_REMOVAL
```yaml
feature: "Transaction coordinator multiple shot mode"
status: "REMOVED (deprecated since pack 15)"
replacement: "Single shot mode"
behavior_change:
  old: "Individual replies processed as they arrive"
  new: "Frontend waits for all replies, sends all at once"
  callback: "Process in 'coordinatedReplies' callback"
backward_compatibility: "Frontend 21 can handle multiple shot from older backends"
support_timeline: "Until all multiple-shot backends out of support"
code_search: "Look for kTransaction_MultipleShot and kTransaction_MultipleShot_Deprecated"
```

### SECURITY_TOKENS_V2_REMOVAL
```yaml
feature: "Security tokens/security keys version 2"
status: "REMOVED (deprecated since pack 15)"
usage: "Used by absolutely no one in any ADP MAG"
reason: "Security key table empty for years"
impact: "No real production flow affected"
code_change: "Remove kSecTokenVersion_V2 usage, use only kSecTokenVersion_V1"
```

### CRYPTIC_CONTEXT_CHANGES
```yaml
api_change: "otf::CrypticContext from otf::InboundCrypticMessage::getCrypticContext"
old_behavior: "Mutable reference"
new_behavior: "Const reference (read-only)"
replacement_source: "otf::TransactionContext: getResources().getTransactionContext().getCrypticContext()"
```

### OTF_API_CHANGES
```yaml
method_signature_changes:
  - method: "otf::ServiceObject::handleSignOut"
    change: "No longer takes boolean as third argument"
  
  - component: "REST headers"
    old: "map"
    new: "multimap"
    deprecated_since: "mdw 15"
    replacements:
      - old: "otf::RESTInboundRequest::hasHeader"
        new: "otf::RESTInboundRequest::countHeaders"
      - old: "otf::RESTInboundRequest::getHeaders"
        new: "otf::RESTInboundRequest::getHeaderMap"
  
  - change: "namespace for xlog interface"
    old: "unittest::xlog"
    new: "otf::xlog"
  
  - method: "otf::ServiceObject::handleEndOfSleep"
    change: "Now virtual"

removed_constructors:
  - "otf::Payload constructors without otf::SensitiveDataFormat"
  - "otf::Payload::Payload() default constructor (deprecated since pack 15)"
  - "otf::Payload::unserialize(toolbox::Unmarshaller&) method"
  - replacement: "otf::Payload::Payload(toolbox::Unmarshaller&) explicit constructor"

removed_methods:
  - "otf::ClientSessionConfiguration::setTtl"
  - "otf::ClientSessionConfiguration::getTtl"
  - replacement: "Use getRTO, setRTO instead"
  - "otf::MessageOptions::setForceUppercase"
  - "otf::MessageOptions::getForceUppercase"
  - replacement: "Use setUppercaseConversion, getUppercaseConversion (available since mdw 15)"

cryptic_context_api_changes:
  - method: "otf::Payload constructors for cryptics"
    old_parameter: "pointer"
    new_parameter: "std::shared_ptr<const otf::CrypticContext>"
    migration: "Take CrypticContext from otf::TransactionContext instead of otf::InboundMessage"
  
  - method: "otf::InboundCrypticMessage::getCrypticContext"
    change: "Now only const method"
  
  - method: "otf::TransactionContext::getCrypticContext"
    old_return: "raw pointer"
    new_return: "std::shared_ptr<const otf::CrypticContext>"
  
  - method: "otf::TransactionContext::getClientCrypticContext"
    old_return: "raw pointer"
    new_return: "std::shared_ptr<const otf::CrypticContext>"
  
  - method: "otf::TransactionContext::setCrypticContext"
    status: "REMOVED"
  
  - method: "otf::TransactionContext::setClientCrypticContext"
    new_parameter: "std::shared_ptr<const otf::CrypticContext>"
  
  - method: "otf::TransactionContext::getCrypticContextServer"
    change: "Now returns const reference"
  
  - method: "otf::TransactionContext::setCrypticContextServer"
    status: "REMOVED"

protobuf_api_migration:
  bms_dependency_change:
    old: "mdw::OTF::ProtobufFramework::Protobuf"
    new: "mdw::OTF"
  include_changes:
    old: '"otf/protobuf/*.h"'
    new: '"otf/*.h"'
    method: "sed replacement"
  namespace_changes:
    old: "otf::protobuf::"
    new: "otf::"
    method: "sed replacement"
  deprecation_timeline: "Deprecated names kept till pack 23"

http_header_value_changes:
  deprecated_api: "otf::HTTPHeaderValue value/options getters and setters"
  problem: "Assumed all headers follow Content-Type syntax (wrong assumption)"
  issue: "getValue() returned truncated value (before semicolon)"
  new_api:
    - "getRawValue/setRawValue (for full header value)"
    - "parseMainValueAndOptions & setMainValueAndOptions (Content-Type specific)"
  deprecation_since: "pack 15 starting September 2024"
  removal_timeline: "OTF 25"
```

---

## KITPACK_MIGRATION_18_TO_23

### KITPACK_OVERVIEW
```yaml
source_version: "kitPack 18-x-x-x"
target_version: "kitPack 23-x-x-x"
migration_path: "Incremental: 18→19→21→23"
note: "MWPack19 went off, so kitPack19 also discontinued"
guides:
  - "kitPack migration: from 18 to 21"
  - "kitPack migration: from 21 to 23"
```

### KITPACK_API_CHANGES
```yaml
kitCommon:
  status: "Deprecated API removed"

kitField:
  change: "validate() API changed"

kitHac:
  status: "No API change"

kitSimpleType:
  status: "Few API changed"

kitCodeset:
  status: "No API change"

kitCodegen:
  status: "No API change"

kitPersistence:
  status: "No API change in itself"
  impact: "UP_SQL connection management changes require code alterations"

kitMultiling:
  status: "No API change"
  note: "Read about transactions"

kitBoostextra:
  status: "FULLY DECOMMISSIONED - not available anymore"

kitBcf:
  status: "No API change"

kitCppunit:
  status: "FULLY DECOMMISSIONED - not available anymore"

kitTimestat:
  status: "No API change"

kitParallel:
  status: "No API change"

kitNoSQLClient:
  status: "Possibly API change IF not using latest scope/collection API"

kitBlob:
  status: "No API change"
  note: "pyKitBlob incidentally also no change"

kitXdsc:
  status: "No API change"

kitOaf:
  status: "Not versioned anymore by kitPack"

kitUtils:
  status: "Not versioned anymore by kitPack"
```

### GOTCHA_SECTIONS
```yaml
xdsc_api_changes:
  scope: "XML messages"
  issue: "Smart pointers & kitFactory changes"

unit_tests_issues:
  scope: "RFD and Oracle DB connections"
  
oracle_upsql_issues:
  scope: "UP_SQLInputRow and UP_SQLOutputRow"
  note: "Not directly kitPack related but common migration pitfalls"
```

---

## GOTCHA_COMPILATION_ISSUES

### GENERATED_EDIFACT_GRAMMAR
```yaml
issue: "Compilation issues with generated grammar code"
cause: "Poisoned _AMD_TPF_ macro in generated grammar code"
tools:
  - "DSC_GRAMGEN_VERSION=4-1-2-0"
  - "ANGEL_VERSION=3.0.3"
solution: "Migrate to up-to-date grammar generation tooling"
reference: "https://rndwww.nce.amadeus.net/git/projects/MWP/repos/grammargenerator/browse"
example: "https://rndwww.nce.amadeus.net/git/projects/NOX/repos/nox/pull-requests/91/overview"
```

### SONAR_SCANNING_PROBLEMS
```yaml
issues:
  - "Build-wrapper outdated on NAS (needs update)"
  - "Sonar only partially supports C++20 scanning"
solution:
  parameter: "sonar.cfamily.cpp20=true"
  workaround: "Use sonar-staging instance"
  staging_url: "https://rndwww.nce.amadeus.net/sonarqube-staging"
  access_requirements:
    - "IZU user must log to platform once"
    - "Request admin privileges if needed"
reference: "https://rndwww.nce.amadeus.net/sonar/documentation/analysis/languages/cfamily/"
```

---

## MIGRATION_CHECKLIST

### PRE_MIGRATION
- [ ] Update to toolchain x86_64-v21 (C++20, GCC 11.x)
- [ ] Review C++20 compatibility of existing code
- [ ] Ensure Jenkins CI/CD fetches tags
- [ ] Fix CryptoManager configuration file permissions
- [ ] Remove TAF/FAN from databases.xml
- [ ] Update OHF header includes
- [ ] Configure changelog generation (or disable if not wanted)

### BATCH_JOBS
- [ ] Replace batch_env.sh with non_otf_batch_launcher.sh
- [ ] Test batch job execution with new wrapper

### API_MIGRATIONS
- [ ] Update toolbox::BoundedString operator!= usage
- [ ] Replace toolbox::OString with std::string/std::string_view
- [ ] Replace toolbox::Hashtable with std::unordered_map
- [ ] Replace toolbox::Hash with std::hash (careful with char* pointers)
- [ ] Remove poisoned macros usage
- [ ] Update ABRClient method calls with new blob parameter
- [ ] Remove mdw::ACF references
- [ ] Migrate from CacheFramework

### DATABASE_CHANGES
- [ ] Remove TAF/FAN configuration from databases.xml
- [ ] Update Oracle tag usage (ora10/11/18/19 → ora)
- [ ] Test UP_SQL connection pooling with OCI session pool
- [ ] Fix UP_SQLInputRow/UP_SQLOutputRow reuse (add Clear() calls)

### EZT_SPECIFIC
- [ ] Rework BindKey() and BindValue() implementations
- [ ] Ensure UP_SQLInputRow/UP_SQLOutputRow objects are cleaned before reuse

### OTF_MIGRATIONS
- [ ] Update OTF variable usage (remove deprecated variables)
- [ ] Migrate from multiple shot to single shot transaction coordinator
- [ ] Remove security tokens v2 usage
- [ ] Update CrypticContext API usage
- [ ] Fix REST headers multimap usage
- [ ] Update Payload constructors
- [ ] Migrate Protobuf API includes and namespaces
- [ ] Update HTTPHeaderValue API usage

### COMPONENT_SPECIFIC
- [ ] Replace TBF::api removed methods
- [ ] Update Tracer header includes
- [ ] Migrate from mdw::CppUnit to osp::CppUnit
- [ ] Update Web::Framework grammar registration
- [ ] Update xlog_dcx import path
- [ ] Remove FusionChart/FusionMap dependencies

### VALIDATION
- [ ] Build with C++20 toolchain
- [ ] Test all batch jobs
- [ ] Verify database connections work without TAF/FAN
- [ ] Check CryptoManager starts with correct permissions
- [ ] Validate changelog generation (if enabled)
- [ ] Test OTF functionality with new APIs
- [ ] Verify unit tests pass with osp::CppUnit
- [ ] Check Sonar scanning works (use staging if needed)
