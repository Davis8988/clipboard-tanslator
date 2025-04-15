
# Clipboard-Tanslator

## 🔧 Requirements

- AutoHotkey v1.1  
- Python 3.6 or higher  
- (Optional) Chocolatey for easy installation  

---

## ⚙️ Prerequisites

**Using Chocolatey (recommended):**

```powershell
choco install autohotkey.install --version=1.1.33.10 -y
choco install python --version=3.10.11 -y
```

**Manual install:**  
Get [AutoHotkey v1.1](https://www.autohotkey.com/) and [Python 3.6+](https://www.python.org/downloads/).

---

## ▶️ Usage

- Clone the repository  
- Create & activate **venv**: 
```bash
python -m venv venv

call venv\Scripts\activate.bat
```
- pip install: 
```bash
(venv)  pip install -r requirements.txt
```
- Run `build_exe.bat` to compile both scripts (NOTE: Needs to be done from the venv activated console)  
- Double-click `autoHotKey_listener_clipboard-tanslator.exe` to start  
- Select text and press `Ctrl + Shift + Z` to translate

> 💡 If the Python executable is not located next to the AHK EXE, set the environment variable `CLIPBOARD_TRANSLATOR_EXE_PATH` to its full path before running.

---

## ❌ Uninstall

- Stop the AutoHotKey process and delete the 2 `.exe` files  

