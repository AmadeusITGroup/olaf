# Otter Framework - Logical Architecture

## Overview

The Otter Framework is a highly modular Angular framework designed to accelerate web application development. This document presents the logical architecture through multiple perspectives, showing system components, relationships, and data flow patterns.

## 1. High-Level System Architecture

```mermaid
graph TB
    subgraph "Otter Framework Ecosystem"
        subgraph "Core Layer"
            CORE[Core Module]
            CONFIG[Configuration]
            COMP[Components]
            SCHEMATICS[Schematics]
        end
        
        subgraph "Feature Modules"
            LOC[Localization]
            RULES[Rules Engine]
            ANALYTICS[Analytics]
            FORMS[Forms]
            ROUTING[Routing]
            STYLING[Styling]
            TESTING[Testing]
        end
        
        subgraph "Development Tools"
            ESLINT[ESLint Plugin]
            EXTRACTORS[Extractors]
            WORKSPACE[Workspace Tools]
            PIPELINE[Pipeline Tools]
        end
        
        subgraph "External Integrations"
            APIS[APIs Manager]
            MOBILE[Mobile]
            THIRD_PARTY[Third Party]
            TELEMETRY[Telemetry]
        end
        
        subgraph "Content & Design"
            DESIGN[Design System]
            DYNAMIC[Dynamic Content]
            STYLE_DICT[Style Dictionary]
        end
    end
    
    subgraph "External Systems"
        ANGULAR[Angular Framework]
        NX[Nx Workspace]
        CMS[Content Management System]
        BACKEND[Backend APIs]
    end
    
    CORE --> COMP
    CORE --> CONFIG
    CORE --> SCHEMATICS
    
    CONFIG --> RULES
    CONFIG --> CMS
    
    COMP --> DESIGN
    COMP --> STYLING
    
    RULES --> CONFIG
    RULES --> ANALYTICS
    
    EXTRACTORS --> CONFIG
    EXTRACTORS --> COMP
    
    WORKSPACE --> NX
    PIPELINE --> NX
    
    APIS --> BACKEND
    MOBILE --> APIS
    
    ANGULAR --> CORE
    NX --> WORKSPACE
```

## 2. Module Dependency Architecture

```mermaid
graph LR
    subgraph "Foundation Layer"
        CORE[Core]
        CONFIG[Configuration]
        LOGGER[Logger]
        TEST_HELPERS[Test Helpers]
    end
    
    subgraph "Component Layer"
        COMPONENTS[Components]
        FORMS[Forms]
        DESIGN[Design System]
        STYLING[Styling]
    end
    
    subgraph "Application Layer"
        ROUTING[Routing]
        LOCALIZATION[Localization]
        ANALYTICS[Analytics]
        MOBILE[Mobile]
    end
    
    subgraph "Business Logic Layer"
        RULES_ENGINE[Rules Engine]
        APIS_MANAGER[APIs Manager]
        DYNAMIC_CONTENT[Dynamic Content]
        STORE_SYNC[Store Sync]
    end
    
    subgraph "Development Layer"
        SCHEMATICS[Schematics]
        TESTING[Testing]
        ESLINT_PLUGIN[ESLint Plugin]
        WORKSPACE[Workspace]
    end
    
    CORE --> COMPONENTS
    CORE --> FORMS
    CORE --> ROUTING
    CORE --> RULES_ENGINE
    
    CONFIG --> RULES_ENGINE
    CONFIG --> DYNAMIC_CONTENT
    CONFIG --> COMPONENTS
    
    COMPONENTS --> DESIGN
    COMPONENTS --> STYLING
    
    LOGGER --> ANALYTICS
    LOGGER --> TELEMETRY
    
    TEST_HELPERS --> TESTING
    
    SCHEMATICS --> CORE
    SCHEMATICS --> COMPONENTS
    SCHEMATICS --> CONFIG
```

## 3. Data Flow Architecture

```mermaid
flowchart TD
    subgraph "Configuration Flow"
        A[Application Source Code] --> B[Extractors]
        B --> C[Metadata Generation]
        C --> D[Configuration Schema]
        D --> E[CMS Integration]
        E --> F[Runtime Configuration]
        F --> G[Component Rendering]
    end
    
    subgraph "Localization Flow"
        H[Translation Keys] --> I[Localization Extractor]
        I --> J[Translation Files]
        J --> K[Localization Service]
        K --> L[Translated Content]
        L --> G
    end
    
    subgraph "Rules Engine Flow"
        M[Business Rules] --> N[Rules Configuration]
        N --> O[Rules Engine]
        O --> P[Rule Evaluation]
        P --> Q[Dynamic Behavior]
        Q --> G
    end
    
    subgraph "Analytics Flow"
        G --> R[User Interactions]
        R --> S[Analytics Service]
        S --> T[Event Tracking]
        T --> U[Analytics Backend]
    end
    
    subgraph "Styling Flow"
        V[Design Tokens] --> W[Style Dictionary]
        W --> X[CSS Variables]
        X --> Y[Component Styles]
        Y --> G
    end
```

## 4. Component Interaction Architecture

```mermaid
graph TB
    subgraph "Angular Application"
        APP[Application Root]
        
        subgraph "Otter Components"
            O3R_COMP[O3R Components]
            FORMS_COMP[Form Components]
            DESIGN_COMP[Design Components]
        end
        
        subgraph "Services Layer"
            CONFIG_SERVICE[Configuration Service]
            LOC_SERVICE[Localization Service]
            RULES_SERVICE[Rules Engine Service]
            ANALYTICS_SERVICE[Analytics Service]
            API_SERVICE[API Service]
        end
        
        subgraph "State Management"
            STORE[NgRx Store]
            EFFECTS[Effects]
            REDUCERS[Reducers]
        end
        
        subgraph "Infrastructure"
            ROUTING_MODULE[Routing Module]
            HTTP_CLIENT[HTTP Client]
            INTERCEPTORS[HTTP Interceptors]
        end
    end
    
    APP --> O3R_COMP
    APP --> FORMS_COMP
    APP --> DESIGN_COMP
    
    O3R_COMP --> CONFIG_SERVICE
    O3R_COMP --> LOC_SERVICE
    O3R_COMP --> RULES_SERVICE
    
    FORMS_COMP --> CONFIG_SERVICE
    FORMS_COMP --> ANALYTICS_SERVICE
    
    CONFIG_SERVICE --> STORE
    LOC_SERVICE --> STORE
    RULES_SERVICE --> STORE
    
    API_SERVICE --> HTTP_CLIENT
    HTTP_CLIENT --> INTERCEPTORS
    
    ANALYTICS_SERVICE --> API_SERVICE
    
    STORE --> EFFECTS
    EFFECTS --> REDUCERS
    REDUCERS --> STORE
```

## 5. Development Workflow Architecture

```mermaid
flowchart LR
    subgraph "Development Phase"
        A[Developer] --> B[Nx Workspace]
        B --> C[Schematics]
        C --> D[Code Generation]
        D --> E[Component Development]
        E --> F[Configuration Setup]
    end
    
    subgraph "Build Phase"
        F --> G[Extractors]
        G --> H[Metadata Extraction]
        H --> I[Build Process]
        I --> J[Bundle Generation]
    end
    
    subgraph "Testing Phase"
        J --> K[Unit Tests]
        K --> L[Integration Tests]
        L --> M[E2E Tests]
        M --> N[Quality Gates]
    end
    
    subgraph "Deployment Phase"
        N --> O[Pipeline Tools]
        O --> P[Deployment]
        P --> Q[Runtime Environment]
        Q --> R[CMS Integration]
    end
    
    subgraph "Runtime Phase"
        R --> S[Configuration Loading]
        S --> T[Application Bootstrap]
        T --> U[Component Initialization]
        U --> V[User Interaction]
    end
```

## 6. Multi-Package Architecture

```mermaid
graph TB
    subgraph "@o3r Packages"
        O3R_CORE[@o3r/core]
        O3R_CONFIG[@o3r/configuration]
        O3R_COMPONENTS[@o3r/components]
        O3R_LOCALIZATION[@o3r/localization]
        O3R_RULES[@o3r/rules-engine]
        O3R_ANALYTICS[@o3r/analytics]
        O3R_TESTING[@o3r/testing]
        O3R_SCHEMATICS[@o3r/schematics]
    end
    
    subgraph "@ama-sdk Packages"
        AMA_SDK_CORE[@ama-sdk/core]
        AMA_SDK_CLIENT[@ama-sdk/client]
        AMA_SDK_SPEC[@ama-sdk/spec]
    end
    
    subgraph "@ama-styling Packages"
        AMA_STYLE_CORE[@ama-styling/core]
        AMA_STYLE_THEME[@ama-styling/theme]
        AMA_STYLE_TOKENS[@ama-styling/design-tokens]
    end
    
    subgraph "@ama-mfe Packages"
        AMA_MFE_CORE[@ama-mfe/core]
        AMA_MFE_SHELL[@ama-mfe/shell]
        AMA_MFE_REMOTE[@ama-mfe/remote]
    end
    
    subgraph "@ama-terasu Packages"
        AMA_TERASU_CLI[@ama-terasu/cli]
        AMA_TERASU_CORE[@ama-terasu/core]
    end
    
    O3R_CORE --> O3R_CONFIG
    O3R_CORE --> O3R_COMPONENTS
    O3R_CONFIG --> O3R_RULES
    O3R_COMPONENTS --> O3R_LOCALIZATION
    
    AMA_SDK_CORE --> AMA_SDK_CLIENT
    AMA_SDK_SPEC --> AMA_SDK_CLIENT
    
    AMA_STYLE_TOKENS --> AMA_STYLE_THEME
    AMA_STYLE_CORE --> AMA_STYLE_THEME
    
    AMA_MFE_CORE --> AMA_MFE_SHELL
    AMA_MFE_CORE --> AMA_MFE_REMOTE
    
    O3R_CORE --> AMA_SDK_CORE
    O3R_COMPONENTS --> AMA_STYLE_CORE
    O3R_CORE --> AMA_MFE_CORE
```

## Architecture Principles

### 1. Modularity
- Each package serves a specific purpose and can be used independently
- Clear separation of concerns between different functional areas
- Minimal coupling between modules with well-defined interfaces

### 2. Configurability
- Metadata-driven configuration system
- Runtime configuration through CMS integration
- Extractable configuration from source code

### 3. Extensibility
- Plugin architecture for custom functionality
- Schematics for code generation and project setup
- Hook system for extending core functionality

### 4. Developer Experience
- Comprehensive tooling and workspace management
- Code generation through schematics
- Integrated testing and quality tools

### 5. Enterprise Ready
- Multi-package architecture for large-scale applications
- Micro-frontend support through @ama-mfe packages
- Analytics and telemetry for production monitoring

## Key Architectural Patterns

### 1. Metadata Extraction Pattern
The framework uses extractors to analyze source code and generate metadata, enabling dynamic configuration and CMS integration.

### 2. Configuration-Driven Components
Components are designed to be configurable through external configuration, allowing for dynamic behavior without code changes.

### 3. Rules Engine Pattern
Business logic is externalized through a rules engine, enabling non-technical users to modify application behavior.

### 4. Multi-Package Monorepo
The framework is organized as a monorepo with multiple npm packages, each serving specific functionality while maintaining consistency.

### 5. Plugin Architecture
Core functionality can be extended through plugins, providing flexibility for different use cases and requirements.
