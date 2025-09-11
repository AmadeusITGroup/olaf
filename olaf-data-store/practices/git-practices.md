# Git Practices for a Monorepo

Working in a monorepo—a single repository containing multiple projects or libraries—requires a slightly different approach to Git than traditional multi-repo setups. The key is to manage complexity, maintain performance, and ensure clear ownership. This guide outlines practical best practices for using Git effectively in a monorepo environment.

## 1. Cloning: Don't Download the World

Monorepos can be massive. Cloning the entire history of every file is often impractical and unnecessary.

*   **Shallow Clone**: If you only need the latest version of the code, use a shallow clone to fetch only the most recent commits. This dramatically reduces clone time and disk space usage.

    ```bash
    git clone --depth 1 <repository_url>
    ```

*   **Sparse Checkout & Partial Clone**: For large monorepos, you often only need to work on a specific project. Sparse checkout (a newer Git feature) allows you to check out only the files in specific directories, even after a clone.

    ```bash
    # Clone the repo, but don't check out any files yet
    git clone --filter=blob:none --no-checkout <repository_url>
    cd <repository_name>

    # Specify which folders you care about
    git sparse-checkout set project-a/src another-project/libs

    # Now, check out only those files
    git checkout
    ```

## 2. Branching Strategy: Keep It Simple

A complex branching model like Git Flow is often counterproductive in a monorepo. A simpler, trunk-based approach is usually more effective.

*   **Mainline/Trunk**: Use a single main branch (e.g., `main` or `master`) as the source of truth.
*   **Short-Lived Feature Branches**: Create feature branches directly from `main`. These branches should be focused on a single, small change.
*   **Prefix Branches (Optional but Recommended)**: To easily identify which project a branch belongs to, prefix it with the project name or a team identifier.

    ```bash
    # Good branch names
    git checkout -b feat/project-a/add-login-button
    git checkout -b fix/shared-ui/button-color
    ```

## 3. Commit Messages: Be Clear and Consistent

In a monorepo, a clear commit history is crucial for understanding what changed and where. Adopt a convention for your commit messages.

*   **Conventional Commits**: This is a widely adopted standard that works perfectly for monorepos. The key is to use a **scope** to indicate the affected project or area.

    ```
    <type>(<scope>): <description>

    [optional body]

    [optional footer]
    ```

*   **Examples**:

    ```
    feat(api): add new endpoint for user profiles

    This commit introduces the GET /api/v1/users/{id} endpoint.
    ```

    ```
    fix(ui-components): correct padding on the primary button

    The button was not aligned correctly on mobile viewports.
    ```

## 4. Pull Requests (PRs): Small, Focused, and Well-Defined

*   **Keep PRs Small**: A PR should represent a single, logical change. This is even more critical in a monorepo, as large PRs can touch many different parts of the codebase, making them difficult to review.
*   **Use CODEOWNERS**: Create a `CODEOWNERS` file at the root of your repository to define which teams or individuals are responsible for different parts of the codebase. This allows for automatic assignment of reviewers to PRs, ensuring the right people see the changes.

    *Example `CODEOWNERS` file:*
    ```
    # All files in the /apps/project-a/ directory are owned by the @project-a-team
    /apps/project-a/ @my-org/project-a-team

    # The shared UI library is owned by the design systems team
    /libs/shared-ui/ @my-org/design-systems

    # Docs are owned by a specific person
    /docs/         docs@example.com
    ```

## 5. Tagging: Mark Your Releases

Use Git tags to mark release points. Since you have multiple projects, your tagging strategy should reflect that.

*   **Project-Specific Tags**: Prefix your tags with the project name to distinguish between releases of different projects.

    ```bash
    git tag -a project-a-v1.2.0 -m "Release version 1.2.0 of Project A"
    git tag -a shared-ui-v3.5.1 -m "Release version 3.5.1 of Shared UI"
    ```
