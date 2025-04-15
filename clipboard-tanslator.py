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

def translate(text):
    logging.debug("Starting translation")
    translated_text = ''
    text = text.lower()
    logging.debug(f"Input text: {text}")
    
    # Find first letter with known direction
    last_letter_heb = None
    for ch in text:
        if ch in keyword_en_to_he_dict:
            last_letter_heb = False
            logging.debug("Detected English input based on character: " + ch)
            break
        elif ch in keyword_he_to_en_dict:
            last_letter_heb = True
            logging.debug("Detected Hebrew input based on character: " + ch)
            break
    if last_letter_heb is None:
        logging.debug("No known characters found, defaulting to English.")
        last_letter_heb = False  # fallback
        
    for letter in text:
        logging.debug(f"Processing letter: {letter}")
        if letter in ["'", ';', '"', ',', '.', '/']:
            if last_letter_heb:
                translated = keyword_he_to_en_dict.get(letter, letter)
                logging.debug(f"Translated special (HE): {letter} → {translated}")
                translated_text += translated
            else:
                translated = keyword_en_to_he_dict.get(letter, letter)
                logging.debug(f"Translated special (EN): {letter} → {translated}")
                translated_text += translated
            continue
        if letter in keyword_en_to_he_dict:
            translated = keyword_en_to_he_dict[letter]
            translated_text += translated
            last_letter_heb = False
            logging.debug(f"Translated EN → HE: {letter} → {translated}")
        elif letter in keyword_he_to_en_dict:
            translated = keyword_he_to_en_dict[letter]
            translated_text += translated
            last_letter_heb = True
            logging.debug(f"Translated HE → EN: {letter} → {translated}")
        else:
            translated_text += letter
            logging.debug(f"Letter not mapped, passed as-is: {letter}")

    logging.debug(f"Final translated text: {translated_text}")
    return translated_text

try:
    logging.info("Reading clipboard content...")
    original = pc.paste()
    logging.info(f"Original clipboard content: {original}")
    logging.info("Performing translation...")
    result = translate(original)
    logging.info("Updating clipboard with translated content...")
    pc.copy(result)
    logging.error("")
    logging.info("✅ Translation complete and copied to clipboard.")
    logging.error("")
except Exception as e:
    logging.error("")
    logging.error("❌ Error occurred during execution.")
    logging.error(traceback.format_exc())
    logging.info("Exiting in 10 seconds...")
    time.sleep(10)
    sys.exit(1)

logging.info("=== Script Completed ===")
logging.error("")