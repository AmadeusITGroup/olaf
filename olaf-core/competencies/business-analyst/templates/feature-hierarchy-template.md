# Feature Hierarchy: [Project Name]

This document outlines the feature hierarchy for [Project Name], breaking down large functionalities into manageable components. This structure serves as a reference for both business stakeholders and development teams, linking features directly to their corresponding code modules.

---

## Feature Set: [Name of the Feature Set, e.g., User Management]
*   **Description**: A high-level description of the group of related features. What is the overall goal of this set?
*   **Code Mapping**: Corresponds to a top-level module, service, or repository (e.g., `user-service`, `com.project.user`).

### Master Feature: [Name of the Master Feature, e.g., User Authentication]
*   **Description**: Describes a major piece of functionality within the feature set. What does this feature enable the user to do?
*   **User Stories**:
    *   As a [user type], I want to [action] so that [benefit].
*   **Code Mapping**: Corresponds to a package or a major sub-directory (e.g., `user-service/authentication`, `com.project.user.auth`).

#### Sub-feature: [Name of the Sub-feature, e.g., Login with Email/Password]
*   **Description**: A specific, granular piece of functionality that is part of a master feature.
*   **Acceptance Criteria**:
    *   Given [context], when [action], then [outcome].
*   **Code Mapping**: Corresponds to specific classes, files, or functions (e.g., `AuthController.ts`, `login_with_password()`).

#### Sub-feature: [Name of the Sub-feature, e.g., Password Reset]
*   **Description**: ...
*   **Acceptance Criteria**: ...
*   **Code Mapping**: ...

---

## Feature Set: [Another Feature Set]
...
