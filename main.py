import pyperclip as pc

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
    translated_text = ''
    text = text.lower()
    for letter in text:
        if letter in keyword_en_to_he_dict:
            translated_text += keyword_en_to_he_dict[letter]
        elif letter in keyword_he_to_en_dict:
            translated_text += keyword_he_to_en_dict[letter]
        else:
            translated_text += letter
    return translated_text

# user_input = input('Enter your text: ')

pc.copy(translate(pc.paste()))



