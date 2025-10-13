param(
  [string]$Path='.',
  [string]$Output='ci-inventory.jsonl'
)
$ErrorActionPreference='Stop'
if(Test-Path $Output){ Remove-Item $Output -Force }

$patterns = @(
  @{ category='actions_java'; regex='java-version:\s*11'; },
  @{ category='docker_base'; regex='^FROM .*11'; },
  @{ category='release_flag'; regex='--release\s+11'; },
  @{ category='maven_compiler'; regex='<release>11</release>'; },
  @{ category='gradle_sourceCompat'; regex='sourceCompatibility\s*=\s*11'; },
  @{ category='toolchain_xml'; regex='<version>11</version>'; },
  @{ category='env_var'; regex='JAVA_VERSION=11'; }
)

$include = @('*.yml','*.yaml','Dockerfile*','Jenkinsfile','*.groovy','pom.xml','build.gradle*','*.config','toolchains.xml','*.sh','*.ps1')

Get-ChildItem -Path $Path -Recurse -File -Include $include 2>$null | ForEach-Object {
  $file = $_.FullName
  $i=0
  Get-Content -Path $file | ForEach-Object {
    $line=$_; $i++
    foreach($p in $patterns){
      if($line -match $p.regex){
        $obj = @{file=$file; line=$i; category=$p.category; match=$line.Trim() }
        ($obj | ConvertTo-Json -Compress) | Add-Content -Path $Output
      }
    }
  }
}
Write-Host "Inventory written to $Output"
