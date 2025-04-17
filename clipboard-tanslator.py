import pyperclip as pc
import logging
import sys
import time
import traceback

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

logging.info("=== Script Started ===")

# English to Hebrew key mapping
keyword_en_to_he_dict = {
    'q': '/',
    'w': "'",
    'e': 'ק',
    'r': 'ר',
    't': 'א',
    'y': 'ט',
    'u': 'ו',
    'i': 'ן',
    'o': 'ם',
    'p': 'פ',
    'a': 'ש',
    's': 'ד',
    'd': 'ג',
    'f': 'כ',
    'g': 'ע',
    'h': 'י',
    'j': 'ח',
    'k': 'ל',
    'l': 'ך',
    ';': 'ף',
    "'": ',',
    '"': ',',
    'z': 'ז',
    'x': 'ס',
    'c': 'ב',
    'v': 'ה',
    'b': 'נ',
    'n': 'מ',
    'm': 'צ',
    ',': 'ת',
    '.': 'ץ',
    '/': '.',
}

# Hebrew to English key mapping
keyword_he_to_en_dict = {
    '/': 'q',
    "'": 'w',
    'ק': 'e',
    'ר': 'r',
    'א': 't',
    'ט': 'y',
    'ו': 'u',
    'ן': 'i',
    'ם': 'o',
    'פ': 'p',
    'ש': 'a',
    'ד': 's',
    'ג': 'd',
    'כ': 'f',
    'ע': 'g',
    'י': 'h',
    'ח': 'j',
    'ל': 'k',
    'ך': 'l',
    'ף': ';',
    ',': "'",
    'ז': 'z',
    'ס': 'x',
    'ב': 'c',
    'ה': 'v',
    'נ': 'b',
    'מ': 'n',
    'צ': 'm',
    'ת': ',',
    'ץ': '.',
    '.': '/',
}


def detect_language(text):
    en_count = 0
    he_count = 0
    for ch in text:
        ch_lower = ch.lower()
        if ch_lower in keyword_en_to_he_dict:
            en_count += 1
        elif ch_lower in keyword_he_to_en_dict:
            he_count += 1
    logging.debug(f"Language detection - EN: {en_count}, HE: {he_count}")
    return 'en' if en_count >= he_count else 'he'

def translate(text):
    logging.debug("Starting translation")
    translated_text = ''
    lang = detect_language(text)
    logging.debug(f"Detected language: {lang}")
    
    for letter in text:
        original_case = letter.isupper()
        lower_letter = letter.lower()

        if lang == 'en' and lower_letter in keyword_en_to_he_dict:
            translated = keyword_en_to_he_dict[lower_letter]
        elif lang == 'he' and lower_letter in keyword_he_to_en_dict:
            translated = keyword_he_to_en_dict[lower_letter]
        else:
            translated = letter  # keep as-is if not found
            logging.debug(f"No mapping for letter: {letter}")
            translated_text += translated
            continue

        # preserve original case
        if original_case:
            translated = translated.upper()
        translated_text += translated

        logging.debug(f"{letter} -> {translated}")

    logging.debug(f"Translated result: {translated_text}")
    return translated_text

try:
    logging.info("Reading clipboard content...")
    original_text = pc.paste()
    logging.info(f"Original clipboard content: {original_text}")

    logging.info("Translating...")
    result = translate(original_text)

    logging.info("Updating clipboard with translated content...")
    pc.copy(result)
    logging.info("")
    logging.info("✅ Translation complete and copied to clipboard.")
    logging.info("")
except Exception:
    logging.error("")
    logging.error("❌ An error occurred:")
    logging.error(traceback.format_exc())
    logging.info("Exiting in 10 seconds...")
    time.sleep(10)
    sys.exit(1)

logging.info("")
logging.info("=== Script Completed ===")
logging.info("")
