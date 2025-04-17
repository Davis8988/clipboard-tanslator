package main

import (
	"log"
	"os"
	"strings"

	"github.com/atotto/clipboard"
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

// detectLanguage detects if the text is more English or Hebrew based on character mapping
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
	log.Printf("Language detection - EN: %d, HE: %d", enCount, heCount)
	if enCount >= heCount {
		return "en"
	}
	return "he"
}

// translateText performs the actual translation based on detected language
func translateText(text string) string {
	var translatedText string

	lang := detectLanguage(text)
	log.Printf("Detected language: %s", lang)

	for _, letter := range text {
		originalCase := letter >= 'A' && letter <= 'Z'
		lowerLetter := strings.ToLower(string(letter))

		var translated string
		switch {
		case lang == "en" && keywordEnToHe[lowerLetter] != "":
			translated = keywordEnToHe[lowerLetter]
		case lang == "he" && keywordHeToEn[lowerLetter] != "":
			translated = keywordHeToEn[lowerLetter]
		default:
			translated = string(letter) // keep as‑is if no mapping
			log.Printf("No mapping for letter: '%c'", letter)
			translatedText += translated
			continue
		}

		// preserve original English casing
		if originalCase {
			translated = strings.ToUpper(translated)
		}
		translatedText += translated
		log.Printf("%c -> %s", letter, translated)
	}

	log.Printf("Translated result: %s", translatedText)
	return translatedText
}

func main() {
	// Custom log format: Only date & time without file/line information
	log.SetFlags(log.Ldate | log.Ltime)

	log.Println("=== Script Started ===")

	var originalText string

	// Priority 1: first command‑line argument (if present and non‑empty)
	if len(os.Args) >= 2 && strings.TrimSpace(os.Args[1]) != "" {
		originalText = os.Args[1]
		log.Printf("Original text (from arg): %s", originalText)
	} else {
		// Priority 2: clipboard
		clipText, err := clipboard.ReadAll()
		if err != nil {
			log.Printf("❌ Failed to read clipboard: %v", err)
			log.Println("Exiting…")
			os.Exit(1)
		}
		if strings.TrimSpace(clipText) == "" {
			log.Println("❌ No input text provided via args or clipboard.")
			log.Println("Exiting…")
			os.Exit(1)
		}
		originalText = clipText
		log.Printf("Original text (from clipboard): %s", originalText)
	}

	log.Println("Translating…")
	result := translateText(originalText)

	// Print translated text to stdout so a wrapper script can capture it
	log.Println("Updated text with translated content…")
	log.Printf("Translated: %s", result)
	println(result)

	log.Println("✅ Translation complete.")
	log.Println("=== Script Completed ===")
}
