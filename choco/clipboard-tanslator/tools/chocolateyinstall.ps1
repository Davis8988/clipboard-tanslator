$ErrorActionPreference = 'Stop'  # Stop on all errors
$toolsDir = $env:ChocolateyToolsLocation
$packageVersion = $env:ChocolateyPackageVersion

# Define executable URLs
$exeUrls = @{
    'clipboard-tanslator.exe'              = "https://github.com/Davis8988/clipboard-tanslator/releases/download/v${packageVersion}/clipboard-tanslator.exe"
    'ahk_listener_clipboard-tanslator.exe' = "https://github.com/Davis8988/clipboard-tanslator/releases/download/v${packageVersion}/ahk_listener_clipboard-tanslator.exe"
}

# Define checksums (replace with actual values)
$checksums = @{
    'clipboard-tanslator.exe'              = 'your-checksum-here'
    'ahk_listener_clipboard-tanslator.exe' = 'your-checksum-here'
}

# Download and verify executables
foreach ($exeName in $exeUrls.Keys) {
    $exePath  = Join-Path $toolsDir $exeName
    $url      = $exeUrls[$exeName]
    $checksum = $checksums[$exeName]

    Write-Host "Downloading $exeName from $url..."
    $packageArgs = @{
        PackageName  = $env:ChocolateyPackageName
        FileFullPath = $exePath
        Url          = $url
        Checksum     = $checksum
        ChecksumType = 'sha256'
    }
    Get-ChocolateyWebFile @packageArgs
}

# Run the AutoHotkey listener
$listenerPath = Join-Path $toolsDir 'ahk_listener_clipboard-tanslator.exe'
Write-Host "Starting AHK listener..."
Start-Process -FilePath $listenerPath -ArgumentList '/silent'
