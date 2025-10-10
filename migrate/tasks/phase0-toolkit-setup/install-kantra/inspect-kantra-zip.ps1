$ErrorActionPreference='Stop'
$url = 'https://github.com/konveyor/kantra/releases/download/v0.8.0/kantra.windows.amd64.zip'
$tmpZip = Join-Path $env:TEMP 'kantra.inspect.zip'
$extractDir = Join-Path $env:TEMP 'kantra.inspect.contents'
Write-Host "[INFO] Downloading $url"
Invoke-WebRequest -Uri $url -OutFile $tmpZip -UseBasicParsing
if(Test-Path $extractDir){ Remove-Item $extractDir -Recurse -Force }
New-Item -ItemType Directory -Path $extractDir | Out-Null
Expand-Archive -LiteralPath $tmpZip -DestinationPath $extractDir -Force
Write-Host "[INFO] Top-level entries:"; Get-ChildItem -Path $extractDir | Select-Object Name,Length,FullName
Write-Host "[INFO] Recursive file list:"; Get-ChildItem -Recurse -File -Path $extractDir | Select-Object FullName,Length
