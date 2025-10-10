# Dependency Alignment — JDK 21 + Boot 3.x

## Preferred approach
1. Use BOM-managed versions where possible (Spring Boot 3.x platform).
2. Set Java level in build files separately from dependency updates.
3. Upgrade critical libs for JDK 21 compatibility:
   - Oracle JDBC: 21.x or 23.x (per vendor matrix)
   - BouncyCastle: `bcpkix-jdk18on` 1.78+
   - PDFBox: 2.0.30+
4. Remove redundant explicit versions that are managed by the Boot BOM.
5. Build and run tests.

## Backup option
- If BOM alignment causes conflicts, pin only the conflicting artifacts explicitly, then retry alignment later.

## Verify
- `mvn -q -DskipTests compile` succeeds.
- `mvn clean verify` passes.
- No dependency convergence errors or version conflicts.
