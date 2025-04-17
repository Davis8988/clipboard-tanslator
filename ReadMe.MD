

# Clipboard‑Translator

## 🔧 Requirements
- **Go 1.22+** (required to build the translator executable)  
- **AutoHotkey v1.1** – needed only for the hot‑key listener  
- (Optional) **Chocolatey** – easiest way to install the above on Windows  

---

## ⚙️ Installing the toolchain

### Using Chocolatey (recommended)
```powershell
choco install golang -y                 # installs latest Go
choco install autohotkey.install --version=1.1.33.10 -y
```

### Manual install  
* https://go.dev/dl – download the Windows installer for Go  
* https://www.autohotkey.com/ – AutoHotkey v1.1 installer  

Verify Go is on PATH:
```powershell
go version
```

---

## 🔨 Build
```bash
git clone <repo> clipboard-translator
cd clipboard-translator
build_exe.bat              # builds clipboard‑tanslator.exe and the AHK listener
```
`build_exe.bat` will  
1. compile **clipboard‑tanslator.go** → *clipboard‑tanslator.exe* (static, no dependencies)  
2. compile **ahk_listener_clipboard-tanslator.ahk** → *ahk_listener_clipboard-tanslator.exe*  

(No Python/venv is needed anymore.)

---

## ▶️ Usage
1. Start **ahk_listener_clipboard-tanslator.exe** (it stays in the tray).  
2. Select text anywhere and press **Ctrl + Shift + Z** → text is translated in place.

> **Note**  
> If *clipboard‑tanslator.exe* is not next to the AHK EXE, set  
> `CLIPBOARD_TRANSLATOR_EXE_PATH` to its full path before launching the listener.

---

## ❌ Uninstall
1. Exit the AutoHotkey listener (tray icon → Exit).  
2. Delete the generated `.exe` files (listener & translator).  
