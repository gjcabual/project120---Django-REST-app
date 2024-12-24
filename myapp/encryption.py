# myapp/encryption.py

# Define a systematic mapping for characters to their encrypted values
encryption_map = {
    'a': 'xy', 'A': '8s',
    'b': 'yl', 'B': '9t',
    'c': 'za', 'C': '7u',
    'd': 'ab', 'D': '6v',
    'e': 'bc', 'E': '5w',
    'f': 'cd', 'F': '4x',
    'g': 'de', 'G': '3y',
    'h': 'ef', 'H': '2z',
    'i': 'fg', 'I': '1A',
    'j': 'gh', 'J': '0B',
    'k': 'hi', 'K': '9C',
    'l': 'ij', 'L': '8D',
    'm': 'jk', 'M': '7E',
    'n': 'kl', 'N': '6F',
    'o': 'lm', 'O': '5G',
    'p': 'mn', 'P': '4H',
    'q': 'no', 'Q': '3I',
    'r': 'op', 'R': '2J',
    's': 'pq', 'S': '1K',
    't': 'qr', 'T': '0L',
    'u': 'rs', 'U': '9M',
    'v': 'st', 'V': '8N',
    'w': 'tu', 'W': '7O',
    'x': 'uv', 'X': '6P',
    'y': 'vw', 'Y': '5Q',
    'z': 'wx', 'Z': '4R',
    ' ': 'z0', '*': 'y1',
    '.': 'y2', ',': 'z3', '!': 'y4', '?': 'z5', '@': 'y6',
    '0': 'x7', '1': 'y8', '2': 'z9', '3': 'x0', '4': 'yA',
    '5': 'xB', '6': 'yC', '7': 'zD', '8': 'xE', '9': 'yF',
    '_': 'xG', '-': 'yH', '+': 'zI', '=': 'yJ', '/': 'zK', 
    '$': 'xL', '%': 'yM', '^': 'zN', '&': 'yO', '#': 'zP',
}

# Create a reverse mapping for decryption
decryption_map = {v: k for k, v in encryption_map.items()}

def encrypt(text):
    return ''.join(encryption_map.get(char, char) for char in text)

def decrypt(encrypted_text):
    decrypted = ''
    temp = ''
    for char in encrypted_text:
        temp += char
        if temp in decryption_map:
            decrypted += decryption_map[temp]
            temp = ''
    return decrypted