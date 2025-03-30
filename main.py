morse_codes = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_codes:
            morse_code += morse_codes[char] + ' '
        else:
            morse_code += ' '
    return morse_code.strip()

input_text = input("Lütfen bir metin girin: ")
morse_text = text_to_morse(input_text)
print("Morse Kodu:", morse_text)
