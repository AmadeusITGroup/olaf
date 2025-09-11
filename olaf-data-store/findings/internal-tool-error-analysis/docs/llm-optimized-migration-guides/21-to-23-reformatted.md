# MWPack 21→23 Migration Guide (LLM-Optimized Format)

## OVERVIEW
**Source Version:** MWPack 21  
**Target Version:** MWPack 23  
**Toolchain:** x86_64-v23 (C++23, GCC 13.x)  
**Major Changes:** C++23 adoption, component removals, attribute syntax changes, Protobuf breaking changes

---

## TOOLCHAIN_CHANGES

### TOOLCHAIN_V23
```yaml
name: "x86_64-v23"
cpp_version: "C++23 (-std=gnu++23)"
gcc_version: "GCC 13.x"
naming_convention: "Same as v19/v21 (differs from packs <= 18)"
unsupported_os: ["SLES 11", "RHEL 7 (potentially)"]
migration_guide: "From toolchain v21 (GCC 11.x/-std=gnu++20) to toolchain v23 (GCC 13.x/-std=gnu++23)"
```

### SONAR_COMPATIBILITY
```yaml
issue: "Default Sonar version doesn't support C++23"
workaround: "Switch to staging version"
jenkinsfile_setting: |
  env.SONAR_URL = 'https://rndwww.nce.amadeus.net/sonarqube-staging'
deprecated_url: 'https://ci-sonar.apps.net6.paas.westeurope.rnd.az.amadeus.net/sonarqube-net6'
```

---

## COMPONENT_CHANGES

### REMOVED_COMPONENTS
```yaml
- name: "mdw::CppUnit"
  status: "REMOVED (deprecated since pack 18)"
  replacement: "osp::CppUnit"
  breaking_changes:
    - "CPPUNIT_NS::Message in CPPUNIT_ASSERT_MESSAGE causes compilation error"
    - "Use std::string instead of CPPUNIT_NS::Message"
    - "Specify different exception type instead of std::exception"

- name: "mdw::DBC"
  status: "REMOVED"
  replacement: "gtest or assert macros"
  migration_scenarios:
    explicit_eiffel_check: "Replace REQUIRE/ENSURE/CHECK/INVARIANT with if conditions throwing std::logic_error"
    implicit_eiffel_check: "Replace with assert() for debug-only checks"
    unittest_usage: "Use osp::GTest macros like ASSERT_TRUE or REQUIRE_TRUE"
```

---

## API_CHANGES

### CFC_CHANGES
```yaml
component: "mdw::CFC"
removed_headers:
  - "AmdDef.h (deprecated in pack 19 and 21)"
  - "AmdInc.h (deprecated in pack 19 and 21)"
replacement: "cfc/Def.h"
new_requirement: "#include <cstdint> for fixed-width integer types"

attribute_syntax_change:
  old_style: "__attribute__((...)) (gcc attributes)"
  new_style: "[[...]] (C++11 attributes)"
  affected_macros: ["AMD_DLLEXPORT", "AMD_DLLIMPORT", "AMD_DLLLOCAL"]
  positioning_rule: "Must be BEFORE keywords like static/virtual/extern"
  mixing_rule: "Cannot mix old-style and new-style attributes"
```

### ABRCLIENT_CHANGES
```yaml
component: "mdw::ABRClient"
breaking_change: "Legacy security object support removed"
migration_timeline:
  pack_18: "API migrated to scx::SecurityContext"
  pack_21: "_legacy methods removed"
  pack_23: "Must use SecurityContext methods"
api_changes:
  old: "setFromSecurityObject_legacy"
  new: "Use methods with scx::SecurityContextPtr"
  context_source: "OTF SecurityManager.getSecurityContext()"
```

### ACF_DECOMMISSIONING
```yaml
component: "mdw::ACF"
status: "DECOMMISSIONING (continued from pack 21)"
valid_users: ["SI", "OTF", "Tracer"]
action: "Remove all references from repositories"
documentation: "mdw::ACF decommissioning guide"
```

---

## COMPONENT_SPECIFIC_CHANGES

### EDICPP_CHANGES
```yaml
component: "mdw::EDICPP"
removed_function: "setNoLeadingSingle0"
reason: "No effect - Edicpp always keeps at least one 0 for value 0"
```

### EZT_CHANGES
```yaml
component: "mdw::EZT"
macro_rename:
  old: "SET_ACTIVE_CONNECTION"
  new: "SET_ACTIVE_EZTAPI_CONNECTION"
  location: "EZT_ApiCheckDatabase.h"
```

### EZT_FLIPFLOP_CHANGES
```yaml
component: "mdw::EZT::Flipflop"
major_change: "pImpl idiom introduction"
impact: "Direct data member access no longer possible"
migration: "Switch to getter/setter methods"
affected_classes: ["EZT_FlipReader", "EZT_FlipReader::VersionedFile"]
note: "Some getters/setters renamed - check header files"
```

### EZT_DAEMON_CHANGES
```yaml
component: "mdw::EZT::Daemon (GMC)"
discontinued_monitoring:
  - "MongoDB (OBE only)"
  - "AppEvent based monitoring"
```

### FDSC_CHANGES
```yaml
component: "mdw::FDSC"
removed_method: "addCStringXml(const char *iData, size_t iLen)"
replacement: "fdsc::Outbuffer::addCString"
note: "Same implementation"
```

### JAFFAR_CHANGES
```yaml
component: "mdw::Jaffar"
dependency_change:
  old: "osp::JsonSpirit (obsolete, unmaintained)"
  new: "osp::RapidJson"
migration: "Adapt code to use RapidJson types and objects"
interface: "Very similar interface"
```

### OHF_CHANGES
```yaml
component: "mdw::OHF"
removed_method: "ohf::ClientCallDataIn::getClient() (deprecated)"
removed_callbacks: "PanelMode callbacks"
reason: "OTF removed them - new API for panel mode entry/exit"
```

### QUEUING_SERVER_CHANGES
```yaml
component: "mdw::QueuingServer"
removed_constructors:
  - "QFPConnection(QFPConnectionType iType, bool tryToConnect)"
  - "QFPConnection(const std::string &hostname, PortNumber_t port, QFPConnectionType iType, bool tryToConnect)"
replacement: "QFPConnection(const std::string &hostname, PortNumber_t port, bool tryToConnect)"
impact: "Only used by mdw::QFC - no client migration needed"
```

### QFC_CHANGES
```yaml
component: "mdw::QFC"
removed_methods:
  message_methods:
    - method: "qfc::Message::setToAgentList(const AgentList & a)"
      reason: "Never implemented"
    - method: "qfc::Message::getToAgentList(AgentList & a) const"
      reason: "Never implemented"
    - method: "qfc::Message::setToAgent(const Agent & agent)"
      reason: "Deprecated"
      replacement: "qfc::Queuer::operator()(const Agent&, const Message &)"
  
  connection_methods:
    - method: "qfc::lqs::Connection::directConnectionClean()"
      status: "Removed"
```

### TDSC_CHANGES
```yaml
component: "mdw::TDSC"
changes: "Unspecified changes"
```

### TOOLBOX_CHANGES
```yaml
component: "mdw::Toolbox"
changes: "Unspecified changes"
```

### TRACER_CHANGES
```yaml
component: "mdw::Tracer"
changes: "Unspecified changes"
```

### WEB_FRAMEWORK_CHANGES
```yaml
component: "mdw::Web::Framework"
changes: "Unspecified changes"
```

### XLOG_INSTRUMENTATION
```yaml
component: "mdw::XLog::Instrumentation"
status: "Version removed (as warned in pack 21)"
replacement: "/opt/1A/xlog-utils/latest"
```

### UPSQL_CHANGES
```yaml
component: "UPSQL"
changes: "Unspecified changes"
```

---

## BATCH_JOB_CHANGES

### BATCH_ENV_DEPRECATION_CONTINUED
```yaml
deprecated_script: "bin/batch_env.sh (continued from pack 21)"
replacement: "bin/non_otf_batch_launcher.sh"
migration_example: |
  OLD: . ${OBEAPP_ROOT}/jfk/pack/MDW/bin/batch_env.sh ${COMP}
       ${aBin} -P $PHASE $@
  NEW: "${OBEAPP_ROOT}/${COMP}/pack/MDW/bin/non_otf_batch_launcher.sh" "${aBin}" -P "${PHASE}" "$@"
```

---

## OSPACK_CHANGES

### PROTOBUF_BREAKING_CHANGE
```yaml
component: "osp::ProtoBuf"
status: "BROKEN in pack 23"
fixability: "Easily fixable"
documentation: "OSPack Main Changes 23"
note: "Critical for Protobuf grammar generation"
```

---

## BMS_CONFIG_CHANGES

### CHANGELOG_CONTINUATION
```yaml
feature: "Changelog generation enabled by default (since R21)"
reference: "R21 Migration guide for details"
```

---

## MIGRATION_CHECKLIST

### PRE_MIGRATION
- [ ] Update to toolchain x86_64-v23 (C++23, GCC 13.x)
- [ ] Switch to Sonar staging version for C++23 support
- [ ] Review C++23 compatibility of existing code

### COMPONENT_REMOVALS
- [ ] Replace mdw::CppUnit with osp::CppUnit
- [ ] Replace mdw::DBC with gtest or assert macros
- [ ] Remove mdw::ACF references (continued decommissioning)

### CODE_CHANGES
- [ ] Replace AmdDef.h/AmdInc.h includes with cfc/Def.h
- [ ] Add #include <cstdint> where needed for fixed-width integers
- [ ] Update AMD_DLLEXPORT/AMD_DLLIMPORT/AMD_DLLLOCAL positioning
- [ ] Fix attribute syntax mixing issues
- [ ] Update ABRClient to use SecurityContext methods (remove _legacy)

### COMPONENT_SPECIFIC_UPDATES
- [ ] Remove setNoLeadingSingle0 usage (mdw::EDICPP)
- [ ] Update SET_ACTIVE_CONNECTION to SET_ACTIVE_EZTAPI_CONNECTION (EZT)
- [ ] Switch to getter/setter for EZT::Flipflop classes
- [ ] Replace addCStringXml with fdsc::Outbuffer::addCString (FDSC)
- [ ] Migrate from JsonSpirit to RapidJson (Jaffar)
- [ ] Remove ohf::ClientCallDataIn::getClient() usage (OHF)
- [ ] Update QFPConnection constructor calls (QueuingServer)
- [ ] Replace deprecated QFC Message methods
- [ ] Update xlog_dcx import path

### PROTOBUF_FIXES
- [ ] Fix osp::ProtoBuf grammar generation (check OSPack guide)

---

## DETAILED_COMPONENT_CHANGES

### mdw::ABRClient
```yaml
api_migration:
  pack_18: "Migrated to scx::SecurityContext"
  pack_21: "Removed legacy _legacy methods"
  
changes:
  old_parameter: "security object pointer"
  new_parameter: "scx::SecurityContextPtr (std::shared_ptr<scx::SecurityContext>)"
  
method_renames:
  - old: "setFromSecurityObject"
    legacy: "setFromSecurityObject_legacy (removed in pack 21)"
    new: "Use SecurityContext version"
    
retrieval: "OTF SecurityManager::getSecurityContext()"
```

### mdw::ACF
```yaml
status: "DECOMMISSIONED - Remove all references"
valid_users: ["SI", "OTF", "Tracer"]
api_stability: "May change unpredictably at any release"
action: "Remove all mdw::ACF dependencies from repositories"
```

### mdw::CFC
```yaml
removed_headers:
  - old: "AmdDef.h"
    new: "cfc/Def.h"
    deprecated_since: "Pack 19, 21"
  - old: "AmdInc.h"
    new: "cfc/Def.h"
    deprecated_since: "Pack 19, 21"
    
fixed_size_types:
  issue: "uint32_t, int64_t types no longer available"
  solution: "Add #include <cstdint>"
  
attribute_changes:
  old_style: "__attribute__((...)) (GCC old-style)"
  new_style: "[[...]] (C++11 attributes)"
  
  positioning:
    requirement: "BEFORE keywords like static/virtual/extern"
    mixing: "Cannot mix old and new style attributes"
    
  macros:
    - "AMD_DLLEXPORT"
    - "AMD_DLLIMPORT"
    - "AMD_DLLLOCAL"
```

### mdw::CppUnit
```yaml
status: "REMOVED from Pack 23"
deprecated_since: "Branch 18"
replacement: "osp::CppUnit (more recent version)"

code_changes:
  compilation_errors:
    - issue: "CPPUNIT_NS::Message in CPPUNIT_ASSERT_MESSAGE"
      solutions:
        - "Inline string directly in macro"
        - "Use std::string instead of CPPUNIT_NS::Message"
        
  exception_handling:
    - issue: "std::exception already caught by osp::CppUnit"
      solution: "Specify different exception type"
```

### mdw::DBC
```yaml
status: "REMOVED from Pack 23"
replacements: ["gtest", "assert macros"]

migration_scenarios:
  explicit_eiffel_check:
    condition: "EIFFEL_CHECK macro explicitly defined"
    action: "Replace REQUIRE/ENSURE/CHECK/INVARIANT with if conditions + exceptions"
    exception_type: "std::logic_error (instead of deprecated dbc::DBC_Exception)"
    
  no_explicit_eiffel_check:
    condition: "EIFFEL_CHECK not explicitly defined"
    behavior: "Similar to assert() - debug mode only"
    action: "Replace with assert() (core dumps in debug, nothing in release)"
    
  unittest_scenario:
    recommendation: "Use osp::GTest macros (ASSERT_TRUE, REQUIRE_TRUE)"
    behavior: "Checks condition in both debug and release mode"

macros_affected:
  - "REQUIRE"
  - "ENSURE"
  - "CHECK"
  - "INVARIANT"
```

### mdw::EDICPP
```yaml
removed_function:
  name: "setNoLeadingSingle0"
  reason: "No effect - Edicpp always keeps at least one 0 for value 0"
```

### mdw::EZT
```yaml
macro_rename:
  old: "SET_ACTIVE_CONNECTION (EZT_ApiCheckDatabase.h)"
  new: "SET_ACTIVE_EZTAPI_CONNECTION"
```

### mdw::EZT::Flipflop
```yaml
design_change: "Introduction of pImpl idiom"
impact: "Switch from direct data member access to getter/setter"
affected_classes:
  - "EZT_FlipReader"
  - "EZT_FlipReader::VersionedFile"
action: "Check header files for updated interface"
```

### mdw::EZT::Daemon (GMC)
```yaml
discontinued_features:
  - "MongoDB monitoring (OBE only)"
  - "AppEvent based monitoring"
```

### mdw::FDSC
```yaml
removed_method:
  name: "addCStringXml(const char *iData, size_t iLen)"
  replacement: "fdsc::Outbuffer::addCString"
  note: "Same implementation"
```

### mdw::Jaffar
```yaml
dependency_change:
  old: "osp::JsonSpirit (obsolete, unmaintained)"
  new: "osp::RapidJson"
  
interface: "Very similar"
action: "Adapt code to use RapidJson types and objects"
```

### mdw::OHF
```yaml
removed_method:
  name: "ohf::ClientCallDataIn::getClient()"
  status: "Deprecated method removed"
  
removed_callbacks:
  name: "PanelMode callbacks"
  reason: "OTF removed them (only useful with TPF)"
  replacement: "OTF new API for immediate panel mode enter/leave"
```

### mdw::QueuingServer
```yaml
removed_constructors:
  - "QFPConnection(QFPConnectionType iType, bool tryToConnect)"
  - "QFPConnection(const std::string &hostname, PortNumber_t port, QFPConnectionType iType, bool tryToConnect)"
  
replacement:
  constructor: "QFPConnection(const std::string &hostname, PortNumber_t port, bool tryToConnect)"
  note: "Only used by mdw::QFC - no client migration needed"
```

### mdw::QFC
```yaml
removed_message_methods:
  - method: "qfc::Message::setToAgentList(const AgentList & a)"
    reason: "Never implemented"
    
  - method: "qfc::Message::getToAgentList(AgentList & a) const"
    reason: "Never implemented"
    
  - method: "qfc::Message::setToAgent(const Agent & agent)"
    replacement: "qfc::Queuer::operator()(const Agent&, const Message &)"
    
removed_connection_methods:
  - method: "qfc::lqs::Connection::directConnectionClean()"
    note: "Deprecation removed - still used by RDCP"
    
removed_dequeuer_methods:
  - method: "qfc::lqs::DeQueuer::setCondition(const std::string & iCondition)"
    reason: "Unsupported by LQS"
    
  - method: "qfc::lqs::DeQueuer::getCondition() const"
    reason: "Unsupported by LQS"
```

### mdw::RFD
```yaml
macro_rename:
  old: "SET_ACTIVE_CONNECTION (RFD_ApiCheckDatabase.h)"
  new: "SET_ACTIVE_RFDAPI_CONNECTION"
  
discontinued_feature:
  name: "APT Consistent Mode"
  original_purpose:
    - "Middleware Cache Bypass"
    - "Instantaneous Office Profile change reading for Test"
  
  removed_methods:
    component: "RFD_ApiConnectionHandler"
    methods: "OTF resource and client profile setting methods"
    
  impact: "Little to no impact - no usage found in BitBucket"
  workaround: "Cope with APT replication delay or implement MEDRRQ service call"
```

### mdw::TDSC
```yaml
removed_interface:
  name: "toolbox::Buffer"
  status: "Deprecated interface removed"
  replacement: "std::strings"
```

### mdw::Toolbox
```yaml
removed_class:
  name: "toolbox::OString"
  deprecated_in: "Previous packs"
  replacements:
    - use_case: "When you own the string"
      replacement: "std::string"
    - use_case: "When you don't own the string"
      replacement: "std::string_view"
  
  serialization_warning: "OString serialization != std::string serialization"
  
removed_macros:
  - name: "_MDW_STACK_AUTO_"
    status: "Poisoned in previous packs, now removed"
    
  - name: "_MDW_ADD_STACKFRAME_"
    status: "Poisoned in previous packs, now removed"
    
  - name: "__AMD_FUNCNAME__"
    previous_expansion: "__PRETTY_FUNCTION__"
    status: "Poisoned in previous packs, now removed"
    
removed_headers:
  - "mdw/Def.h (defines nothing in pack 23)"
  - "toolbox/OptionPlatform.h (defines nothing in pack 23)"
  
removed_types:
  - name: "toolbox::LockFreeQueue*"
    reason: "Unused by anyone"
    
  - name: "toolbox::AutoArrayPtr"
    reason: "Unused - just std::unique_ptr with array type"
    
  - name: "toolbox::Hashtable"
    replacement: "std::unordered_map"
    deprecated_in: "Previous packs"
    
  - name: "toolbox::Hash"
    replacement: "std::hash"
    char_pointer_warning:
      old: "toolbox::Hash<char*>/toolbox::Hash<const char*>"
      correct_replacement: "std::hash<std::string_view>"
      wrong_replacement: "std::hash<const char*> (DIFFERENT behavior)"
      
removed_constructor:
  class: "toolbox::Unmarshaller"
  constructor: "Copy constructor"
  deprecated_since: "Pack 15"
  alternative: "Version with bool iMustCopy parameter (not recommended)"
  recommendation: "Don't copy unmarshaller object"
```

### mdw::Tracer
```yaml
removed_method:
  name: "tracer::handler::Kafka::Create"
  status: "Deprecated method removed"
  
replacement:
  method: "tracer::handler::Kafka::Create (new version)"
  parameter: "tracer::config::KafkaSettings object as first argument"
  
  migration_steps:
    1: "Create tracer::config::KafkaSettings object"
    2: "Call setBrokers(iBrokers)"
    3: "Call setTopic(iDefaultTopic)"
    4: "Pass object as first parameter to new Create function"
```

### mdw::Web::Framework
```yaml
dependency_change:
  old: "osp::JsonSpirit (obsolete, unmaintained)"
  new: "osp::RapidJson"
  interface: "Very similar"
  
grammar_headers:
  removed:
    - "webFramework/HtmlConversation_Grammar.h"
    - "webFramework/HtmlConversationGrammar_sax.h"
  reason: "Exposing implementation details"
  
  replacement:
    old_code: |
      #include "webFramework/HtmlConversation_Grammar.h"
      aRegistrationManager.registerEdifactGrammar(WebFramework::HtmlConversation_Grammar::getInstance());
    
    new_code: |
      #include "webFramework/Grammar.h"
      WebFramework::Grammar::RegisterGrammars(aRegistrationManager);
```

### mdw::XLog::Instrumentation
```yaml
removed_apis: "All deprecated APIs"
dependency_removed: "osp::JsonSpirit (obsolete)"
```

### xlog_dcx Python Import
```yaml
stable_path: "/opt/1A/xlog-utils/latest"
removed_from: "mdw::Xlog::Instrumentation"

deprecated_sources:
  - "Copying file to own git repository"
  - "NAS version in mdw::Xlog::Instrumentation"
  - "BMS replication folder"
  
import_code: |
  import sys
  sys.path.append("/opt/1A/xlog-utils/latest")
  import xlog_dcx
```

### UPSQL
```yaml
tag_migration:
  old_tags: ["ora10", "ora11", "ora18", "ora19"]
  new_tag: "ora"
  
  configuration_files:
    - "CMK configurations"
    - "deployment.xml"
    
  code_changes:
    old: "mdw::SQL::ora19"
    new: "mdw::SQL::ora"
    
  compatibility: "Implementable in all previous major packs with recent versions"
```

## BATCH_JOB_CHANGES

### Helper Script Updates
```yaml
delivered_scripts:
  - "otf_batch_launcher.sh"
  - "batch_env.sh"
  
delivery_location: "MWPack (all supported major releases since 21 Jul 2020)"

required_actions:
  1: "Delete scripts from repository"
  2: "Update batch wrappers"
  
path_updates:
  otf_batch_launcher:
    old: "${OBEAPP_ROOT}/cmp/shell/otf_batch_launcher.sh"
    new: "${OBEAPP_ROOT}/cmp/pack/MDW/bin/otf_batch_launcher.sh"
    
  batch_env:
    old: "${OBEAPP_ROOT}/cmp/shell/batch_env.sh"
    new: "${OBEAPP_ROOT}/cmp/pack/MDW/bin/batch_env.sh"
```

### batch_env.sh Deprecation
```yaml
status: "DEPRECATED"
reason: "Sourcing toolchain environment causes system executable failures"
issue: "OSPack libraries conflict with system libraries"

replacement:
  script: "bin/non_otf_batch_launcher.sh"
  usage: "Wrapper script - pass C++ executable and arguments"
  
example_migration:
  old_approach: |
    . ${OBEAPP_ROOT}/jfk/pack/MDW/bin/batch_env.sh ${COMP}
    ${aBin} -P $PHASE $@
    
  new_approach: |
    "${OBEAPP_ROOT}/${COMP}/pack/MDW/bin/non_otf_batch_launcher.sh" "${aBin}" -P "${PHASE}" "$@"
```

## COMPREHENSIVE_MIGRATION_CHECKLIST

### Pre-Migration Assessment
- [ ] **Upgrade to toolchain v23 (C++23, GCC 13.x)**
- [ ] **Configure Sonar staging URL for C++23 support**
- [ ] **Review OSPack 23 Protobuf generation issues**
- [ ] **Audit mdw::ACF usage (must be removed)**
- [ ] **Check for deprecated component usage (CppUnit, DBC)**
- [ ] **Review batch job script dependencies**
- [ ] **Identify toolbox deprecated type usage**
- [ ] **Check for removed header includes**

### Component Migration Tasks
- [ ] **Remove all mdw::ACF references**
- [ ] **Replace AmdDef.h/AmdInc.h with cfc/Def.h**
- [ ] **Add #include <cstdint> where needed**
- [ ] **Update AMD_DLL* attribute positioning**
- [ ] **Migrate from mdw::CppUnit to osp::CppUnit**
- [ ] **Replace mdw::DBC with assert/gtest macros**
- [ ] **Remove setNoLeadingSingle0 calls**
- [ ] **Update EZT/RFD macro names**
- [ ] **Replace JsonSpirit with RapidJson**
- [ ] **Update OHF API calls**

### API and Method Updates
- [ ] **Update ABRClient to use SecurityContext**
- [ ] **Replace QFC deprecated methods**
- [ ] **Update Tracer Kafka::Create calls**
- [ ] **Replace Web::Framework grammar includes**
- [ ] **Update xlog_dcx import paths**
- [ ] **Replace toolbox deprecated types**
- [ ] **Update UPSQL Oracle tags**

### Batch Job Migration
- [ ] **Delete local copies of helper scripts**
- [ ] **Update otf_batch_launcher.sh paths**
- [ ] **Update batch_env.sh paths**
- [ ] **Replace batch_env.sh sourcing with non_otf_batch_launcher.sh**
- [ ] **Test batch job execution**

### Post-Migration Validation
- [ ] **Compile with C++23 toolchain**
- [ ] **Run Sonar analysis with staging instance**
- [ ] **Execute comprehensive test suite**
- [ ] **Verify batch job functionality**
- [ ] **Test Protobuf generation**
- [ ] **Validate removed component replacements**
- [ ] **Check performance regression**
- [ ] **Update CI/CD pipeline configurations**

### BATCH_JOBS
- [ ] Continue using non_otf_batch_launcher.sh wrapper
- [ ] Test batch job execution

### VALIDATION
- [ ] Build with C++23 toolchain
- [ ] Test Sonar integration with staging version
- [ ] Verify Protobuf functionality
- [ ] Check all component-specific changes
- [ ] Validate attribute syntax changes
