# Unit Test Patterns

## Recent Changes (sample)
- 2025-01-09 M src/test/java/com/amadeus/signpdf/CytricExpenseServiceTest.java
- 2025-01-09 M src/test/java/com/amadeus/signpdf/HttpTest.java
- 2025-01-09 M src/test/java/com/amadeus/signpdf/MainControllerTest.java
- 2024-12-19 M src/test/java/com/amadeus/signpdf/HttpTest.java
- 2024-12-19 M src/test/java/com/amadeus/signpdf/MainControllerTest.java
- 2024-11-27 M src/test/java/com/amadeus/signpdf/CertificatePoolTest.java
- 2024-11-26 M src/test/java/com/amadeus/signpdf/MetadataInPdfTest.java
- 2024-11-26 M src/test/java/com/amadeus/signpdf/PdfToPdfaConversionTest.java
- 2024-08-27 M src/test/java/com/amadeus/signpdf/CytricExpenseServiceIT.java
- 2024-08-27 M src/test/java/com/amadeus/signpdf/converters/ExpenseJwtBodyConverterTest.java
- 2024-08-23 A src/test/java/com/amadeus/signpdf/helpers/ExpenseUrlHelperTest.java
- 2024-08-20 M src/test/java/com/amadeus/signpdf/converters/TaxPackageBundleConverterTest.java
- 2023-10-31 M src/test/java/com/amadeus/signpdf/ServerTest.java
- Kotlin: src/test/kotlin/com/amadeus/signpdf/MainControllerTest.kt, HttpTest.kt, utils/SerializationTest.kt

## Frameworks and Runners
- JUnit 4 with Spring Test
  - `@RunWith(SpringRunner.class)` / `@RunWith(SpringRunner::class)`
  - `@SpringBootTest`
  - `@ActiveProfiles("dev", "test")` or `@ActiveProfiles("test")`
- JUnit Vintage enabled to support JUnit 4 alongside JUnit 5 dependencies

## Web Layer Testing
- `@AutoConfigureMockMvc` with injected `MockMvc`
- Request building via `MockMvcRequestBuilders` (multipart, GET, POST)
- Assertions via `MockMvcResultMatchers` (status, headers, jsonPath, content)
- Spring Security integration using `SecurityMockMvcRequestPostProcessors.user("...").roles("...")`

## Mocking
- Kotlin tests use SpringMockK:
  - `@MockkBean` to register Spring beans
  - `io.mockk.every { ... }` and `io.mockk.verify { ... }`
- Java tests occasionally rely on Spring context autowiring for collaborators

## Assertions
- Java: `org.junit.Assert.*`, AssertJ `assertThat(...)`
- Kotlin: `kotlin.test.assertEquals`
- HTTP: JSON path assertions for structured responses

## Test Resources and Fixtures
- Files under `src/test/resources/docs/**` (JWT payloads, PDFs)
- Keystore in `src/test/resources/keystore.p12`
- Helper utilities under `src/test/java|kotlin/**/TestUtils.*` and `helper/TestClient.kt`

## Naming and Structure
- Unit tests: `*Test.java|kt` under `src/test/java|kotlin`
- Some integration-style tests exist (e.g., `CytricExpenseServiceIT.java`) but ITs are not configured to run separately via Failsafe by default

## Common Patterns Observed
- **Profile-driven context**: tests activate `dev` and `test` profiles to use test configs
- **End-to-end controller flows**: upload/sign/verify endpoints exercised via `MockMvc`
- **Security roles gating**: negative tests validate forbidden access without proper roles
- **Validation-first**: bad inputs return `400` with structured error payload (`error`, `message`)
- **Hash-based workflows**: compute SHA-256, sign, then verify round-trips
- **PDF processing**: regression cases using various PDF samples (jpeg/webp, locked/unlocked, invalid pdfa)
- **Service interactions**: external dependencies stubbed via MockK and verified for calls

## Validated Snippets

### Java: Controller endpoint with security and validation (MockMvc)

```java
@RunWith(SpringRunner.class)
@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles({"dev", "test"})
public class UploadControllerSecurityTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void upload_missingPdf_returnsBadRequestJson() throws Exception {
        mockMvc.perform(MockMvcRequestBuilders.multipart("/upload")
                .file("file", new byte[0])
                .param("jwt", "aaa.payload.zzz")
                .with(SecurityMockMvcRequestPostProcessors.user("tester").roles("upload")))
            .andExpect(MockMvcResultMatchers.status().isBadRequest())
            .andExpect(MockMvcResultMatchers.header().string(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE))
            .andExpect(MockMvcResultMatchers.jsonPath("error").exists())
            .andExpect(MockMvcResultMatchers.jsonPath("message").exists());
    }
}
```

Why this is good:
- Uses Spring test context with `dev` and `test` profiles.
- Exercises HTTP contract and security role.
- Asserts both status and structured JSON error payload.

### Kotlin: Service collaboration using SpringMockK

```kotlin
@RunWith(SpringRunner::class)
@SpringBootTest
@ActiveProfiles("test")
class TrustedDbFlowTest {

    @MockkBean
    lateinit var trustedDbService: TrustedDBService

    @MockkBean
    lateinit var cytricExpenseV1Service: CytricExpenseV1Service

    @Autowired
    lateinit var mockMvc: MockMvc

    @Test
    fun `genuine document -> creates receipt`() {
        val file = Files.readAllBytes(ResourceUtils.getFile("classpath:docs/invalid_pdfa3u.pdf").toPath())
        val hash = SHA256Hash.compute(file).hexDigest

        every { trustedDbService.send(any()) } returns TrustedDBResponse(UUID.randomUUID()).apply { isGenuine = true }
        every { cytricExpenseV1Service.send(any(), any(), any(), any(), any(), any(), any()) } returns ReceiptNoteV1(
            type = ExpenseSourceV1.Type.receiptNote,
            receiptDateTime = LocalDateTime(2024, 12, 13, 17, 18, 22)
        )

        val jwtPayload = Base64.getEncoder().encodeToString("{"file":{"hash":"$hash","unique_id":""}}".toByteArray())

        mockMvc.perform(MockMvcRequestBuilders.multipart("/upload")
            .file("file", file)
            .param("jwt", "aaa.$jwtPayload.zzz")
            .with(SecurityMockMvcRequestPostProcessors.user("tester").roles("upload")))
            .andExpect(MockMvcResultMatchers.status().isCreated)

        verify { trustedDbService.send(any()) }
        verify { cytricExpenseV1Service.send(any(), any(), any(), any(), any(), any(), any()) }
    }
}
```

Why this is good:
- Clear arrangement using MockK `every` and verification with `verify`.
- Uses real test resources and domain hash computation to mimic realistic flow.
- Focuses on observable behavior (HTTP 201 and collaborations), not implementation details.

## Tools and Dependencies
- Spring Boot Test, Spring Security Test
- JUnit 4 (Vintage engine enabled)
- MockK + SpringMockK for Kotlin
- JaCoCo for coverage (Maven plugin)
- WireMock dependency present; not prominently used in sampled tests
