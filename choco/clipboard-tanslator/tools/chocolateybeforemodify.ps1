
$ErrorActionPreference = 'Stop'

$procName = 'ahk_listener_clipboard-tanslator.exe'

Write-Host "Stopping AHK listener..."
$ahkProcess =  Get-Process  | ? {$_.Name -like "*${procName}*"}

if ($ahkProcess) {
    Write-Host "Stopping process: $($ahkProcess.Name)"
	Stop-Process -Id $ahkProcess.Id
}

Write-Host "OK"
Write-Host ""


