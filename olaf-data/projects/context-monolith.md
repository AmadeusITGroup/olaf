# Copilot Instructions for BPI Mood Voting Application

## Architecture Overview

This is a **Spring Boot application** using **Spring Modulith** with **Hexagonal Architecture** and **Domain-Driven Design (DDD)**. The application is an anonymous mood voting system that runs as both a REST API and multiple job modes (sync, campaigns, purge).

### Key Architectural Patterns

- **Spring Modulith**: Modular monolith with bounded contexts as modules (3 modules: shared, identity, campaign)
- **Standard Spring Data**: Standard Spring Data repositories (NOT reactive)
- **Hexagonal Architecture**: Clean separation between domain, application, and infrastructure
- **Ports & Adapters**: Domain defines `port/` interfaces, SPI provides `adapters/`
- **Event-Driven**: Inter-module communication via domain events with Spring Modulith event handling
- **Profile-Based Module Activation**: Modules activated via Spring profiles with advanced filtering
- **Clean Architecture Stereotypes**: Custom annotations in `shared.stereotype`:
  - `@ApplicationService` : Services applicatifs (orchestration)
  - `@DomainService` : Services domaine (logique métier pure)
  - `@InfrastructureAdapter` : Adaptateurs infrastructure
  - `@AggregateRoot` : Racines d'agrégat DDD
  - `@ValueObject` : Value Objects
  - `@UseCase` : Use Cases (ports entrants)
  - `@DomainRepository` : Repositories domaine (ports sortants)
  - `@Local` : Composants locaux/développement (remplace @Profile("dev"))
  - `@ConditionalOnModule` : Activation conditionnelle par module

## Spring Modulith Module Structure

Each module follows this standard structure using **Hexagonal Architecture** with **SPI pattern**:

### Module Structure

Chaque module suit cette structure standard utilisant l'**Architecture Hexagonale** avec le **pattern SPI** :

#### Structure d'un module
```
fr.bpifrance.moo.<module-name>/
├── domain/                                    # 🟢 CŒUR - Domaine pur (0 dépendance framework)
│   ├── model/                                # Value Objects et Agrégats
│   │   ├── <Entity>.java                    # Agrégat racine (@AggregateRoot)
│   │   ├── <Entity>Id.java                  # Value Objects identifiants (UUID wrapper)
│   │   ├── <ValueObject>.java               # Value Objects métier (Email, etc.)
│   │   ├── <Enum>.java                      # Énumérations métier (Status, Role, etc.)
│   │   └── exceptions/                      # Exceptions métier
│   │       ├── <Entity>NotFoundException.java
│   │       ├── <Entity>Exception.java
│   │       └── <ModuleName>Exception.java
│   ├── port/                               # Ports (interfaces) - Clean Architecture
│   │   ├── in/                            # Ports entrants (Use Cases)
│   │   │   ├── <ModuleName>UseCase.java
│   │   │   └── <Operation>UseCase.java
│   │   └── out/                           # Ports sortants (SPI)
│   │       ├── <Entity>Repository.java     # Persistence
│   │       ├── <ExternalSystem>Port.java   # Systèmes externes
│   │       ├── MetricsPort.java            # Métriques
│   │       └── ConfigurationPort.java      # Configuration
│   ├── service/                           # Services de domaine
│   │   ├── <ModuleName>DomainService.java  # Logique métier complexe
│   │   └── <ModuleName>DomainServiceImpl.java
│   └── events/                            # Événements de domaine
│       ├── <Entity>LeftEvent.java
│       ├── <Entity>RegisteredEvent.java
│       └── <Entity>UpdatedEvent.java
├── application/                           # 🟡 COUCHE APPLICATION (orchestration)
│   └── service/                          # Services applicatifs
│       ├── <ModuleName>ApplicationService.java # Orchestration principale
│       ├── <ModuleName>CommandService.java     # Commands (CQRS)
│       └── <ModuleName>QueryService.java       # Queries (CQRS)
├── api/                                  # 🔵 ADAPTATEURS ENTRANTS (exposition)
│   ├── controller/                       # Controllers REST
│   │   ├── <ModuleName>Controller.java
│   │   └── <ModuleName>AdminController.java
│   ├── job/                             # Jobs et schedulers
│   │   └── <ModuleName>Scheduler.java
│   ├── dto/                             # DTOs exposition REST
│   │   ├── <Entity>Request.java
│   │   ├── <Entity>Response.java
│   │   └── <Operation>Response.java
│   ├── events/                          # Event listeners inter-modules
│   │   └── <Event>Listener.java
│   ├── contract/                        # Services inter-modules (Spring Modulith)
│   │   ├── <ModuleName>PublicApi.java    # API publique principale
│   │   ├── anticorruption/              # Anti-corruption layer
│   │   │   └── <Translation>Service.java
│   │   ├── command/                     # Commands inter-modules
│   │   │   └── <Entity>SyncCommand.java
│   │   ├── dto/                         # DTOs intégration
│   │   │   └── <Entity>Dto.java
│   │   └── result/                      # Results inter-modules
│   │       └── <Operation>Result.java
│   └── package-info.java                # @NamedInterface("api")
└── spi/                                 # 🔴 SPI - Service Provider Interface (sortants)
    ├── repository/                      # Implémentations persistence
    │   ├── entity/                     # Entités persistence
    │   │   ├── <Entity>Entity.java
    │   │   └── <SubEntity>Entity.java
    │   ├── mapper/                     # Mappers MapStruct
    │   │   ├── <Entity>EntityMapper.java
    │   │   └── IdentityValueObjectMapper.java
    │   ├── <Entity>MongoAdapter.java   # Implémentation repository
    │   └── <Entity>MongoRepository.java # Interface Spring Data
    ├── external/                       # Adaptateurs systèmes externes
    │   ├── dto/                       # DTOs externes
    │   │   ├── <External>DTO.java
    │   │   └── <External>ResponseDTO.java
    │   ├── <External>FeignClient.java  # Client externe
    │   ├── <External>DataMapper.java   # Mapper MANUEL logique métier
    │   ├── Rest<External>Client.java   # Adaptateur principal
    │   └── <External>ErrorDecoder.java # Gestion erreurs
    ├── inproc/                        # Adaptateurs autres modules
    │   └── <OtherModule>InProcClient.java
    ├── anticorruption/                # Anti-corruption implementations
    │   └── <Translation>ServiceImpl.java
    └── config/                        # Configuration module
        └── <ModuleName>ModuleConfig.java
```

## Current Modules

### Application Architecture Actuelle

```
fr.bpifrance.moo/
├── shared/                     # Module partagé (@ApplicationModule.Type.OPEN)
│   ├── domain/
│   │   ├── model/             # Value Objects communs (EntityId, DomainPageRequest, EnterpriseEnvelope, etc.)
│   │   ├── events/            # Interface DomainEvent + DomainEvent.PublicEvent (Kafka externalization)
│   │   ├── port/
│   │   │   ├── in/           # Use Cases partagés (ConfigurationUseCase)
│   │   │   └── out/          # Ports sortants (ConfigurationRepository, IdempotencePort)
│   │   └── service/          # Services domaine partagés (ConfigurationValidationService)
│   ├── application/service/   # Services applicatifs partagés
│   ├── api/
│   │   ├── contract/         # Services publics inter-modules
│   │   │   ├── ConfigurationQueryService.java
│   │   │   ├── ConfigurationCommandService.java
│   │   │   ├── AdminCommandService.java
│   │   │   ├── dto/          # DTOs intégration (ConfigDto, CampaignConfigDto, etc.)
│   │   │   └── impl/         # Implémentations services
│   │   ├── controller/       # Controllers configuration (AdminConfigController, etc.)
│   │   └── events/           # Event listeners (EventDebugListener, Kafka abstractions)
│   ├── stereotype/           # Annotations Clean Architecture + Module scanning avancé
│   │   ├── @ApplicationService, @DomainService, @InfrastructureAdapter, etc.
│   │   ├── @Local (remplace @Profile("dev"))
│   │   ├── @ConditionalOnModule (activation modules)
│   │   ├── @EnableModuleScan (scanning modulaire avec profils)
│   │   └── scan/            # ModuleScanApi, ModuleScanNoApi (filtres avancés)
│   ├── module/              # Infrastructure modules
│   │   ├── ConditionalOnModule.java
│   │   └── ModuleActivationCondition.java
│   ├── infrastructure/       # Infrastructure partagée
│   └── spi/
│       ├── repository/       # Adaptateurs persistence (ConfigurationMongoAdapter)
│       │   ├── entity/       # ConfigurationEntity
│       │   ├── mapper/       # ConfigurationEntityMapper, PageableMapper
│       │   └── config/       # Configuration (Cache, Mongo, Web, DataInitializer)
│       └── config/          # Configuration Kafka + Spring Modulith
│           ├── ModulithExternalizationConfig.java # Gestion événements publics → Kafka
│           ├── SharedKafkaProperties.java         # Configuration Kafka centralisée
│           └── SharedModuleConfig.java            # Configuration module shared
├── identity/                 # Module Identity & Access Management 
│   ├── domain/
│   │   ├── model/            # Agrégats et Value Objects
│   │   │   ├── Employee.java          # Agrégat racine principal
│   │   │   ├── Team.java, Train.java  # Agrégats organisationnels
│   │   │   ├── EmployeeId.java, TeamId.java, TrainId.java  # Value Objects IDs
│   │   │   ├── Email.java, Role.java  # Value Objects métier
│   │   │   ├── HrData.java, HrEmployee.java, HrTeam.java, HrTrain.java  # HR sync
│   │   │   ├── SyncReport.java, SyncStatus.java, SyncStatistics.java  # Synchronisation
│   │   │   ├── CrudMetrics.java, SyncHealthStatus.java  # Métriques
│   │   │   └── exceptions/            # EmployeeException, InvalidNameException, etc.
│   │   ├── port/
│   │   │   ├── in/              # Use Cases (pas encore implémentés)
│   │   │   └── out/             # Ports sortants
│   │   │       ├── EmployeeRepository.java, TeamRepository.java, TrainRepository.java
│   │   │       ├── SyncReportRepository.java
│   │   │       ├── HRSystemPort.java
│   │   │       ├── IdentityMetricsPort.java
│   │   │       └── ConfigurationPort.java
│   │   ├── service/         # Services domaine
│   │   │   ├── EmployeeDomainService.java  # Logique métier employés
│   │   │   └── HRSyncService.java          # Logique synchronisation HR
│   │   └── events/          # Événements domaine (PublicEvent pour Kafka)
│   │       ├── EmployeeRegisteredEvent.java
│   │       ├── EmployeeUpdatedEvent.java
│   │       └── EmployeeLeftEvent.java
│   ├── application/service/ # Services applicatifs 
│   │   └── SynchronizeHRService.java # Service sync HR complet
│   ├── api/
│   │   ├── controller/      # Controllers REST (à compléter)
│   │   ├── job/            # Jobs synchronisation (à compléter)
│   │   ├── dto/            # DTOs REST (à compléter)
│   │   ├── events/         # Event listeners inter-modules (à compléter)
│   │   └── contract/       # API publique inter-modules
│   │       ├── IdentityPublicApi.java  # API principale (à créer)
│   │       ├── anticorruption/         # Anti-corruption layer
│   │       │   └── RoleTranslationService.java
│   │       ├── command/     # Commands inter-modules (à compléter)
│   │       ├── dto/         # DTOs intégration (à compléter)
│   │       └── result/      # Results inter-modules (à compléter)
│   └── spi/
│       ├── repository/      # Implémentations persistence
│       │   ├── entity/     # EmployeeEntity, TeamEntity, TrainEntity, SyncReportEntity
│       │   ├── mapper/     # EmployeeEntityMapper, IdentityValueObjectMapper, etc.
│       │   └── *MongoAdapter.java, *MongoRepository.java
│       ├── external/       # Adaptateurs systèmes externes
│       │   ├── dto/       # HrResponseDTO, RecordDTO
│       │   ├── HrFeignClient.java, RestHrApiClient.java
│       │   ├── HrDataMapper.java  # Mapper MANUEL logique métier HR
│       │   ├── HrFeignErrorDecoder.java
│       │   └── DatadogIdentityMetricsAdapter.java
│       ├── inproc/        # Adaptateurs autres modules
│       │   └── SharedConfigInProcClient.java
│       ├── anticorruption/ # Implémentations anti-corruption
│       │   └── RoleTranslationServiceImpl.java
│       └── config/        # Configuration
│           ├── IdentityModuleConfig.java
│           └── HrFeignConfig.java
└── campaign/               # Module Campaign Management (NOUVEAU)
    ├── domain/
    │   ├── model/          # Agrégats et Value Objects
    │   │   ├── Campaign.java           # Agrégat racine principal
    │   │   ├── CampaignId.java         # Value Object ID
    │   │   ├── Recipient.java          # Value Object destinataire
    │   │   └── exceptions/             # CampaignException, CampaignNotFoundException
    │   ├── port/
    │   │   ├── in/         # Use Cases
    │   │   │   ├── CampaignWriteUseCase.java
    │   │   │   └── CampaignSchedulerUseCase.java
    │   │   └── out/        # Ports sortants
    │   │       ├── CampaignRepository.java
    │   │       ├── LedgerService.java
    │   │       └── ConfigurationPort.java
    │   ├── service/        # Services domaine
    │   │   └── CampaignPlanningService.java
    │   └── events/         # Événements domaine (PublicEvent pour Kafka)
    │       ├── CampaignRegisteredEvent.java
    │       ├── CampaignDeactivatedEvent.java
    │       ├── CampaignReactivatedEvent.java
    │       ├── CampaignScheduleChangedEvent.java
    │       └── CampaignRecipientsUpdateEvent.java
    ├── application/service/ # Services applicatifs
    │   ├── CampaignWriteService.java
    │   └── CampaignSchedulerService.java
    ├── api/
    │   ├── controller/     # Controllers REST (@Profile("campaign"))
    │   │   └── CampaignController.java
    │   ├── dto/           # DTOs REST
    │   │   └── CampaignScheduleUpdateRequest.java
    │   └── events/        # Event listeners inter-modules
    │       ├── IdentityEventsListener.java
    │       └── IdentityEventRegistryConfig.java (Registry Kafka)
    └── spi/
        ├── repository/     # Implémentations persistence
        │   ├── entity/    # CampaignEntity, RecipientEntity
        │   ├── mapper/    # CampaignEntityMapper, CampaignValueObjectMapper
        │   └── *MongoAdapter.java, *MongoRepository.java
        ├── security/      # Services cryptographiques
        │   └── CryptoService.java (JWT + AES encryption)
        └── config/        # Configuration
            ├── CampaignModuleConfig.java
            └── CampaignProperties.java
```

### Module Dependencies

- **shared**: Module ouvert (@ApplicationModule.Type.OPEN) - base commune avec infrastructure partagée
- **identity**: Dépend uniquement de "shared" (@ApplicationModule(allowedDependencies = {"shared"}))
- **campaign**: Dépend de "shared" et "identity" (@ApplicationModule(allowedDependencies = {"shared", "identity", "identity::events::*"}))
 