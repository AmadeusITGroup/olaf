<#!
Update Spring Boot version in Maven or Gradle build files.
- For Maven: updates parent spring-boot-starter-parent and BOM version occurrences.
- For Gradle: updates springBootVersion variable or plugin DSL version.
#>
param(
  [Parameter(Mandatory=$true)][string]$TargetVersion
)
$ErrorActionPreference = 'Stop'
function Info($m){ Write-Host "[Update-SB] $m" -ForegroundColor Cyan }
$files = @()
$files += Get-ChildItem -Recurse -Include pom.xml -ErrorAction SilentlyContinue
$files += Get-ChildItem -Recurse -Include build.gradle,build.gradle.kts -ErrorAction SilentlyContinue
if(-not $files){ Write-Warning 'No build files found.'; exit 1 }
foreach($f in $files){
  $orig = Get-Content $f.FullName -Raw
  $updated = $orig
  # Maven parent
  $updated = [regex]::Replace($updated,'(<parent>\s*<groupId>org.springframework.boot</groupId>\s*<artifactId>spring-boot-starter-parent</artifactId>\s*<version>)([^<]+)(</version>)','$1'+$TargetVersion+'$3',[System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
  # Maven BOM
  $updated = [regex]::Replace($updated,'(<dependencyManagement>.*?spring-boot-dependencies.*?<version>)([^<]+)(</version>)','$1'+$TargetVersion+'$3',[System.Text.RegularExpressions.RegexOptions]::Singleline)
  # Gradle springBootVersion var
  $updated = [regex]::Replace($updated,'springBootVersion\s*=\s*"([^"]+)"','springBootVersion = "'+$TargetVersion+'"')
  # Gradle plugin DSL
  $updated = [regex]::Replace($updated,'(id\s+"org.springframework.boot"\s+version\s+")([^"]+)(")','$1'+$TargetVersion+'$3')
  if($updated -ne $orig){
    Set-Content $f.FullName $updated
    Info "Updated $($f.FullName)"
  }
}
