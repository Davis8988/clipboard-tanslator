package main

import (
	"fmt"
	"log"
	"strings"
	"time"
	"golang.org/x/term"
	"os"
)

// English to Hebrew key mapping
var keywordEnToHe = map[string]string{
	"q": "/", "w": "'", "e": "ק", "r": "ר", "t": "א", "y": "ט", "u": "ו", "i": "ן", "o": "ם", "p": "פ",
	"a": "ש", "s": "ד", "d": "ג", "f": "כ", "g": "ע", "h": "י", "j": "ח", "k": "ל", "l": "ך", ";": "ף",
	"'": ",", "\"": ",", "z": "ז", "x": "ס", "c": "ב", "v": "ה", "b": "נ", "n": "מ", "m": "צ", ",": "ת",
	".": "ץ", "/": ".",
}

// Hebrew to English key mapping
var keywordHeToEn = map[string]string{
	"/": "q", "'": "w", "ק": "e", "ר": "r", "א": "t", "ט": "y", "ו": "u", "ן": "i", "ם": "o", "פ": "p",
	"ש": "a", "ד": "s", "ג": "d", "כ": "f", "ע": "g", "י": "h", "ח": "j", "ל": "k", "ך": "l", "ף": ";",
	",": "'", "ז": "z", "ס": "x", "ב": "c", "ה": "v", "נ": "b", "מ": "n", "צ": "m", "ת": ",", "ץ": ".",
	".": "/",
}

func detectLanguage(text string) string {
	enCount, heCount := 0, 0
	for _, ch := range text {
		chLower := strings.ToLower(string(ch))
		if _, exists := keywordEnToHe[chLower]; exists {
			enCount++
		} else if _, exists := keywordHeToEn[chLower]; exists {
			heCount++
		}
	}
	if enCount >= heCount {
		return "en"
	}
	return "he"
}

func translate(text string) string {
	var translatedText string
	lang := detectLanguage(text)
	for _, letter := range text {
		originalCase := letter >= 'A' && letter <= 'Z'
		lowerLetter := strings.ToLower(string(letter))

		var translated string
		if lang == "en" {
			translated = keywordEnToHe[lowerLetter]
		} else if lang == "he" {
			translated = keywordHeToEn[lowerLetter]
		} else {
			translated = string(letter)
		}

		if originalCase {
			translated = strings.ToUpper(translated)
		}

		translatedText += translated
	}

	return translatedText
}

func main() {
	log.SetFlags(log.LstdFlags | log.Lshortfile)

	log.Println("=== Script Started ===")

	// Read clipboard content (simulated as input)
	var originalText string
	fmt.Println("Enter text to simulate clipboard content:")
	fmt.Scanln(&originalText)
	log.Printf("Original clipboard content: %s", originalText)

	log.Println("Translating...")
	result := translate(originalText)

	log.Println("Updated clipboard with translated content...")
	log.Printf("Translated: %s", result)

	log.Println("✅ Translation complete.")
	log.Println("=== Script Completed ===")
}
