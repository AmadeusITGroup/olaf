# Project Context - Spring Boot Hexagonal Architecture

## Architecture Overview

This is a **Spring Boot application** using **Spring Modulith** with **Hexagonal Architecture** and **Domain-Driven Design (DDD)**. The application follows modern enterprise patterns and runs as both a REST API and multiple job modes for various business operations.

## Key Architectural Patterns

- **Spring Modulith**: Modular monolith with bounded contexts as modules
- **Standard Spring Data**: Standard Spring Data repositories (NOT reactive)
- **Hexagonal Architecture**: Clean separation between domain, application, and infrastructure
- **Ports & Adapters**: Domain defines `port/` interfaces, SPI provides `adapters/`
- **Event-Driven**: Inter-module communication via domain events with Spring Modulith event handling
- **Profile-Based Module Activation**: Modules activated via Spring profiles with advanced filtering
- **Clean Architecture Stereotypes**: Custom annotations for clean architecture:
  - `@ApplicationService`: Application services (orchestration)
  - `@DomainService`: Domain services (pure business logic)
  - `@InfrastructureAdapter`: Infrastructure adapters
  - `@AggregateRoot`: DDD aggregate roots
  - `@ValueObject`: Value Objects
  - `@UseCase`: Use Cases (inbound ports)
  - `@DomainRepository`: Domain repositories (outbound ports)
  - `@Local`: Local/development components
  - `@ConditionalOnModule`: Conditional module activation

## Spring Modulith Module Structure

Each module follows this standard structure using **Hexagonal Architecture** with **SPI pattern**:

### Standard Module Structure

```
com.example.app.<module-name>/
├── domain/                                    # 🟢 CORE - Pure domain (zero framework dependencies)
│   ├── model/                                # Value Objects and Aggregates
│   │   ├── <Entity>.java                    # Aggregate root (@AggregateRoot)
│   │   ├── <Entity>Id.java                  # ID Value Objects (UUID wrapper)
│   │   ├── <ValueObject>.java               # Business value objects (Email, etc.)
│   │   ├── <Enum>.java                      # Business enumerations (Status, Role, etc.)
│   │   └── exceptions/                      # Business exceptions
│   │       ├── <Entity>NotFoundException.java
│   │       ├── <Entity>Exception.java
│   │       └── <ModuleName>Exception.java
│   ├── port/                               # Ports (interfaces) - Clean Architecture
│   │   ├── in/                            # Inbound ports (Use Cases)
│   │   │   ├── <ModuleName>UseCase.java
│   │   │   └── <Operation>UseCase.java
│   │   └── out/                           # Outbound ports (SPI)
│   │       ├── <Entity>Repository.java     # Persistence
│   │       ├── <ExternalSystem>Port.java   # External systems
│   │       ├── MetricsPort.java            # Metrics
│   │       └── ConfigurationPort.java      # Configuration
│   ├── service/                           # Domain services
│   │   ├── <ModuleName>DomainService.java  # Complex business logic
│   │   └── <ModuleName>DomainServiceImpl.java
│   └── events/                            # Domain events
│       ├── <Entity>CreatedEvent.java
│       ├── <Entity>UpdatedEvent.java
│       └── <Entity>RemovedEvent.java
├── application/                           # 🟡 APPLICATION LAYER (orchestration)
│   └── service/                          # Application services
│       ├── <ModuleName>ApplicationService.java # Main orchestration
│       ├── <ModuleName>CommandService.java     # Commands (CQRS)
│       └── <ModuleName>QueryService.java       # Queries (CQRS)
├── api/                                  # 🔵 INBOUND ADAPTERS (exposition)
│   ├── controller/                       # REST Controllers
│   │   ├── <ModuleName>Controller.java
│   │   └── <ModuleName>AdminController.java
│   ├── job/                             # Jobs and schedulers
│   │   └── <ModuleName>Scheduler.java
│   ├── dto/                             # REST exposition DTOs
│   │   ├── <Entity>Request.java
│   │   ├── <Entity>Response.java
│   │   └── <Operation>Response.java
│   ├── events/                          # Inter-module event listeners
│   │   └── <Event>Listener.java
│   ├── contract/                        # Inter-module services (Spring Modulith)
│   │   ├── <ModuleName>PublicApi.java    # Main public API
│   │   ├── anticorruption/              # Anti-corruption layer
│   │   │   └── <Translation>Service.java
│   │   ├── command/                     # Inter-module commands
│   │   │   └── <Entity>SyncCommand.java
│   │   ├── dto/                         # Integration DTOs
│   │   │   └── <Entity>Dto.java
│   │   └── result/                      # Inter-module results
│   │       └── <Operation>Result.java
│   └── package-info.java                # @NamedInterface("api")
└── spi/                                 # 🔴 SPI - Service Provider Interface (outbound)
    ├── repository/                      # Persistence implementations
    │   ├── entity/                     # Persistence entities
    │   │   ├── <Entity>Entity.java
    │   │   └── <SubEntity>Entity.java
    │   ├── mapper/                     # MapStruct mappers
    │   │   ├── <Entity>EntityMapper.java
    │   │   └── ValueObjectMapper.java
    │   ├── <Entity>DatabaseAdapter.java   # Repository implementation
    │   └── <Entity>DatabaseRepository.java # Spring Data interface
    ├── external/                       # External system adapters
    │   ├── dto/                       # External DTOs
    │   │   ├── <External>DTO.java
    │   │   └── <External>ResponseDTO.java
    │   ├── <External>FeignClient.java  # External client
    │   ├── <External>DataMapper.java   # Manual business logic mapper
    │   ├── Rest<External>Client.java   # Main adapter
    │   └── <External>ErrorDecoder.java # Error handling
    ├── inproc/                        # Other module adapters
    │   └── <OtherModule>InProcClient.java
    ├── anticorruption/                # Anti-corruption implementations
    │   └── <Translation>ServiceImpl.java
    └── config/                        # Module configuration
        └── <ModuleName>ModuleConfig.java
```

## Example Application Architecture

```
com.example.app/
├── shared/                     # Shared module (@ApplicationModule.Type.OPEN)
│   ├── domain/
│   │   ├── model/             # Common Value Objects (EntityId, PageRequest, etc.)
│   │   ├── events/            # DomainEvent interface + PublicEvent (external messaging)
│   │   ├── port/
│   │   │   ├── in/           # Shared Use Cases (ConfigurationUseCase)
│   │   │   └── out/          # Outbound ports (ConfigurationRepository, etc.)
│   │   └── service/          # Shared domain services
│   ├── application/service/   # Shared application services
│   ├── api/
│   │   ├── contract/         # Public inter-module services
│   │   ├── controller/       # Configuration controllers
│   │   └── events/           # Event listeners and messaging abstractions
│   ├── stereotype/           # Clean Architecture annotations + Module scanning
│   └── spi/
│       ├── repository/       # Persistence adapters
│       └── config/          # Messaging + Spring Modulith configuration
├── identity/                 # Identity & Access Management Module
│   ├── domain/
│   │   ├── model/            # Aggregates and Value Objects
│   │   │   ├── User.java              # Main aggregate root
│   │   │   ├── Team.java, Group.java  # Organizational aggregates
│   │   │   ├── UserId.java, TeamId.java, GroupId.java  # ID Value Objects
│   │   │   ├── Email.java, Role.java  # Business value objects
│   │   │   └── exceptions/            # Business exceptions
│   │   ├── port/
│   │   │   ├── in/              # Use Cases
│   │   │   └── out/             # Outbound ports
│   │   │       ├── UserRepository.java, TeamRepository.java, GroupRepository.java
│   │   │       ├── ExternalSystemPort.java
│   │   │       └── IdentityMetricsPort.java
│   │   ├── service/         # Domain services
│   │   │   ├── UserDomainService.java      # User business logic
│   │   │   └── ExternalSyncService.java    # External synchronization
│   │   └── events/          # Domain events (PublicEvent for external messaging)
│   │       ├── UserRegisteredEvent.java
│   │       ├── UserUpdatedEvent.java
│   │       └── UserRemovedEvent.java
│   ├── application/service/ # Application services
│   │   └── SynchronizeExternalService.java # Complete external sync service
│   ├── api/
│   │   ├── controller/      # REST Controllers
│   │   ├── job/            # Synchronization jobs
│   │   ├── dto/            # REST DTOs
│   │   ├── events/         # Inter-module event listeners
│   │   └── contract/       # Public inter-module API
│   └── spi/
│       ├── repository/      # Persistence implementations
│       ├── external/       # External system adapters
│       ├── inproc/        # Other module adapters
│       └── config/        # Module configuration
└── business/               # Business Logic Module
    ├── domain/
    │   ├── model/          # Aggregates and Value Objects
    │   │   ├── Campaign.java           # Main aggregate root
    │   │   ├── CampaignId.java         # ID Value Object
    │   │   ├── Recipient.java          # Business value object
    │   │   └── exceptions/             # Business exceptions
    │   ├── port/
    │   │   ├── in/         # Use Cases
    │   │   └── out/        # Outbound ports
    │   ├── service/        # Domain services
    │   └── events/         # Domain events (PublicEvent for external messaging)
    ├── application/service/ # Application services
    ├── api/
    │   ├── controller/     # REST Controllers
    │   ├── dto/           # REST DTOs
    │   └── events/        # Inter-module event listeners
    └── spi/
        ├── repository/     # Persistence implementations
        ├── security/      # Cryptographic services
        └── config/        # Module configuration
```

## Module Dependencies

- **shared**: Open module (@ApplicationModule.Type.OPEN) - common base with shared infrastructure
- **identity**: Depends only on "shared" (@ApplicationModule(allowedDependencies = {"shared"}))
- **business**: Depends on "shared" and "identity" (@ApplicationModule(allowedDependencies = {"shared", "identity", "identity::events::*"}))

## Development Guidelines

### Naming Conventions
- **Packages**: Use clear, business-focused names
- **Classes**: Follow DDD naming patterns (Entity, ValueObject, Service, etc.)
- **Methods**: Use ubiquitous language from domain

### Testing Strategy
- **Unit Tests**: Focus on domain logic and business rules
- **Integration Tests**: Test module boundaries and external integrations
- **Architecture Tests**: Validate architectural constraints and dependencies

### Event Handling
- **Domain Events**: Use for intra-module communication
- **Public Events**: Use for inter-module communication
- **External Events**: Use for external system integration

This context provides guidance for developing Spring Boot applications using hexagonal architecture, Spring Modulith, and domain-driven design principles.