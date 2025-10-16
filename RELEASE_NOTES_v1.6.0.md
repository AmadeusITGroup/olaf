# Release v1.6.0 - Enhanced Framework & New Features
**Release Date:** 2025-10-16  
**Tag:** [v1.6.0](https://github.com/AmadeusITGroup/olaf/tree/v1.6.0)

## Overview
This release introduces significant framework enhancements and new interactive features that expand OLAF's capabilities. Key additions include interactive exploration tools, session management features, AWS Kiro integration, and a complete condensed framework solution.

## 🚀 New Features

### **Challenge-Me Interactive Exploration** (#22)
- **Interactive Learning Tool**: New competency for exploring and drilling into subjects using LLM knowledge, documentation, local codebase, and web search
- **Multi-Source Research**: Combines AI knowledge with real-time documentation and code analysis
- **Enhanced Learning Experience**: Provides guided exploration for complex topics

### **Carry-Over and Stashing Agent Sessions** (#20)
- **Session Management**: Ability to pause, stash, and resume agent work sessions
- **Work Continuity**: Seamless transition between different tasks and contexts
- **Session Persistence**: Maintain context across multiple interactions

### **Context Switching with Project Templates** (#18)
- **Multi-Project Support**: Switch between different project contexts efficiently
- **Template Integration**: Bootstrap new contexts using predefined templates
- **Enhanced Workflow**: Streamlined project management across multiple codebases

### **AWS Kiro Integration Support** (#19)
- **Cloud Integration**: Full support for OLAF framework within AWS Kiro environment
- **Kiro Structure Compatibility**: Adapted framework to work seamlessly with Kiro's architecture
- **Enhanced Deployment**: Improved cloud-based AI assistant capabilities

### **Complete Condensed Framework Solution** (#17)
- **Framework Optimization**: Comprehensive condensed version of OLAF framework
- **Performance Improvements**: Streamlined framework loading and execution
- **Self-Contained Solution**: All necessary components in a single, efficient package

## 🛠️ Technical Improvements

### **Framework Synchronization** (#21)
- **Integration to Main Sync**: Assisted synchronization of framework files from integration branch
- **Consistency Improvements**: Ensures main branch stays current with latest developments
- **Deployment Reliability**: Better coordination between development and production environments

### **Project Structure Enhancements** (#16)
- **Enhanced .gitignore**: Improved file exclusion patterns for better repository management
- **Directory Management**: Optimized project structure for better organization
- **Development Workflow**: Streamlined development environment setup

## 👥 Contributors
@Pascal-PACCAUD, @ppd

## 📝 Upgrade Instructions

### For Existing Users
1. **Pull Latest Changes**: `git pull origin main`
2. **Update to v1.6.0**: `git checkout v1.6.0`
3. **Review New Features**: Check the new competencies in `olaf-core/prompts/`
4. **AWS Kiro Users**: Update your Kiro configuration to leverage new integration features

### New Features Available
- Use the new "challenge me" competency for interactive learning sessions
- Leverage carry-over and stashing for better session management
- Utilize context switching for multi-project workflows
- Take advantage of the condensed framework for improved performance

### Breaking Changes
None - this release is fully backwards compatible.

---

**Full Changelog**: [v1.5.3...v1.6.0](https://github.com/AmadeusITGroup/olaf/compare/v1.5.3...v1.6.0)