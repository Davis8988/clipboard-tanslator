; ====================================================================================
; Script Name : clipboard-tanslator.ahk
; Author      : David Yair
; Contact     : davismarsel@gmail.com
; Description : This script translates selected text (Hebrew ↔ English) using an
;               external executable (`clipboard-tanslator.exe`) and pastes the result.
;
; Hotkey      : CTRL + SHIFT + Z
;               - Copies selected text
;               - Runs the translator executable (minimized)
;               - Pastes the translated result
;               - Restores the original clipboard content
;
; Requirements: - AutoHotkey v1
;               - clipboard-tanslator.exe (compiled golang script)
;               - Environment variable `CLIPBOARD_TRANSLATOR_EXE_PATH` (optional)
; ====================================================================================
^+z::
    Translate_Clipboard()
	
	; Change keyboard language
	SwitchLanguage()
	
	; Finish with a beep!
	SoundBeep, 523, 120
	
	return

Translate_Clipboard()
{
    ; Determine executable path to var 'clipboardTranslatorExePath' from env: 'CLIPBOARD_TRANSLATOR_EXE_PATH' or fallback
    EnvGet, clipboardTranslatorExePath, CLIPBOARD_TRANSLATOR_EXE_PATH
    if (clipboardTranslatorExePath = "")
        clipboardTranslatorExePath := A_ScriptDir . "\clipboard-tanslator.exe"

    ; Save original clipboard content
    Clip_Save := ClipboardAll

    ; Clear clipboard
    Clipboard := ""
    Sleep 50

    ; Copy selected text
    Send ^c
    ClipWait, 1
    if (ErrorLevel) {
        MsgBox Failed to copy selected text to clipboard.
        Clipboard := Clip_Save
        return
    }

    ; Run translator and wait for completion
    RunWait %clipboardTranslatorExePath%, , Min
    if (ErrorLevel != 0) {
        MsgBox ❌ clipboard-tanslator.exe failed to run. Exit code: %ErrorLevel%
        Clipboard := Clip_Save
        return
    }

    ; Wait for updated clipboard content
    ClipWait, 2
    if (ErrorLevel) {
        MsgBox ❌ Translation failed or clipboard not updated.
        Clipboard := Clip_Save
        return
    }

    ; Wait for extra 1 second for the full clipboard to update
    Sleep 1000

    ; Paste translated text
    Send %Clipboard%

    ; Restore original clipboard
    Sleep 100
    Clipboard := Clip_Save
}

SwitchLanguage()
{
    Send, {Alt Down}{Shift Down}{Shift Up}{Alt Up}
	return
}