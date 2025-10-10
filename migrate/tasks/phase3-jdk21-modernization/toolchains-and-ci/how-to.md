# Toolchains and CI — Enable JDK 21

## Preferred approach
1. Add JDK 21 to local toolchains.
   - Maven: `.mvn/toolchains.xml` → add `<toolchain><version>21</version></toolchain>`.
   - Gradle: `java { toolchain { languageVersion = JavaLanguageVersion.of(21) } }` behind a property flag initially.
2. Update CI to run on 17 and 21.
   - GitHub Actions: `strategy.matrix.java: [17, 21]` and install steps for 21.
3. Keep compilation level as-is for now (e.g., 17) until tests pass on 21.
4. Run builds on both 17 and 21 and compare results.

## Backup option
- If toolchains cause issues, temporarily switch the shell JDK to 21 and build without toolchains.
  - Windows PowerShell (session only): see `phase0-toolkit-setup/jdk-switch/how-to.md`.

## Verify
- `mvn -v` or `./gradlew -v` resolves JDK 21 when configured.
- CI jobs succeed for both 17 and 21.
- Produce a short `ci_workflow_diff.md` showing before/after.
