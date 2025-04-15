@echo off
REM ====================================================================================
REM Script Name : build_exe.bat
REM Purpose     : Build a standalone executable from "%pyScript%" using PyInstaller.
REM Requirements: Python and PyInstaller must be installed.
REM Output      : Creates 'dist\%pyScript%.exe' that can run independently of Python.
REM ====================================================================================

:: %~dp0 - This script's dir + '\' 
set pyScript=%~dp0clipboard-tanslator.py

echo.
echo Compiling "%pyScript%" into an executable
echo.
echo Executing: pyinstaller --onefile "%pyScript%" --distpath .
echo.
pyinstaller --onefile "%pyScript%" --distpath .
if not "%ERRORLEVEL%" == "0" (
    echo.
    echo ❌ ERROR: Failed to build the executable.
    pause
    exit /b 1
)

echo.
echo ✅ SUCCESS: Executable created at dist\main.exe
echo.

pause
exit /b 0
