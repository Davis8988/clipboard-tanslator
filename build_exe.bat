@echo off
REM ====================================================================================
REM Script Name : build_exe.bat
REM Purpose     : Build standalone executables from:
REM                 - Go program   : clipboard-tanslator.go  (using go build)
REM                 - AHK script   : ahk_listener_clipboard-tanslator.ahk (using Ahk2Exe)
REM Requirements: Go toolchain and AutoHotkey (with Ahk2Exe) must be installed and
REM               on PATH (or adjust paths below).
REM Output      : Creates EXEs in the current folder.
REM ====================================================================================

:: ----------------------------------------------------------------------
:: Go program
:: ----------------------------------------------------------------------
set goSrc=%~dp0clipboard-tanslator.go
set goExe=%~dp0clipboard-tanslator.exe
set GOPROXY=https://proxy.golang.org,direct


echo.
echo 🔧 Compiling Go program: "%goSrc%"
echo Executing: go build -trimpath -ldflags "-s -w" -o "%goExe%" "%goSrc%"
echo.

go build -trimpath -ldflags "-s -w" -o "%goExe%" "%goSrc%"
if not "%ERRORLEVEL%" == "0" (
    echo.
    echo ❌ ERROR: Failed to build the Go executable.
    pause
    exit /b 1
)

echo.
echo ✅ Go EXE created successfully: %goExe%
echo.
echo.

:: ----------------------------------------------------------------------
:: AutoHotkey v1
:: ----------------------------------------------------------------------
set ahkScript=%~dp0ahk_listener_clipboard-tanslator.ahk
set ahkExe=%~dp0ahk_listener_clipboard-tanslator.exe

echo 🔧 Compiling AutoHotkey script: "%ahkScript%"
echo Executing: "C:\Program Files\AutoHotkey\Compiler\Ahk2Exe.exe" /in "%ahkScript%" /out "%ahkExe%"
echo.

"C:\Program Files\AutoHotkey\Compiler\Ahk2Exe.exe" /in "%ahkScript%" /out "%ahkExe%"
if not "%ERRORLEVEL%" == "0" (
    echo.
    echo ❌ ERROR: Failed to compile AutoHotkey script.
    pause
    exit /b 1
)

echo.
echo ✅ AHK EXE created successfully: %ahkExe%
echo.

pause
exit /b 0
