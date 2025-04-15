@echo off
REM ====================================================================================
REM Script Name : build_exe.bat
REM Purpose     : Build standalone executables from:
REM                 - Python script: clipboard-tanslator.py (using PyInstaller)
REM                 - AHK script   : ahk_listener_clipboard-tanslator.ahk (using Ahk2Exe)
REM Requirements: Python, PyInstaller, and AutoHotkey (with Ahk2Exe) must be installed.
REM Output      : Creates EXEs in the current folder.
REM ====================================================================================

:: Setup paths
set pyScript=%~dp0clipboard-tanslator.py
set ahkScript=%~dp0ahk_listener_clipboard-tanslator.ahk
set ahkExe=%~dp0ahk_listener_clipboard-tanslator.exe



:: Python Script
echo.
echo 🔧 Compiling Python script: "%pyScript%"
echo Executing: pyinstaller --onefile "%pyScript%" --distpath .
echo.

pyinstaller --onefile "%pyScript%" --distpath .
if not "%ERRORLEVEL%" == "0" (
    echo.
    echo ❌ ERROR: Failed to build the Python executable.
    pause
    exit /b 1
)

echo.
echo ✅ Python EXE created successfully.
echo.
echo.


:: AutoHotKey v1
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
