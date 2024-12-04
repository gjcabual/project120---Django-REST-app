# myapp/encryption.py

# Define a systematic mapping for characters to their encrypted values
encryption_map = {
    'a': 'x1y2', 'A': 'X1Y2',
    'b': 'y3la3', 'B': 'Y3Z4',
    'c': 'z5a6', 'C': 'Z5A6',
    'd': 'a7b8', 'D': 'A7B8',
    'e': 'b9c0', 'E': 'B9C0',
    'f': 'c1d2', 'F': 'C1D2',
    'g': 'd3e4', 'G': 'D3E4',
    'h': 'e5f6', 'H': 'E5F6',
    'i': 'f7g8', 'I': 'F7G8',
    'j': 'g9h0', 'J': 'G9H0',
    'k': 'h1i2', 'K': 'H1I2',
    'l': 'i3j4', 'L': 'I3J4',
    'm': 'j5k6', 'M': 'J5K6',
    'n': 'k7l8', 'N': 'K7L8',
    'o': 'l9m0', 'O': 'L9M0',
    'p': 'm1n2', 'P': 'M1N2',
    'q': 'n3o4', 'Q': 'N3O4',
    'r': 'o5p6', 'R': 'O5P6',
    's': 'p7q8', 'S': 'P7Q8',
    't': 'q9r0', 'T': 'Q9R0',
    'u': 'r1s2', 'U': 'R1S2',
    'v': 's3t4', 'V': 'S3T4',
    'w': 't5u6', 'W': 'T5U6',
    'x': 'u7v8', 'X': 'U7V8',
    'y': 'v9w0', 'Y': 'V9W0',
    'z': 'w1x2', 'Z': 'W1X2',
    ' ': 'z0y1', '*': 'y0z1',
    '.': 'y2z3', ',': 'z4y5', '!': 'y6z7', '?': 'z8y9', '@': 'y0z1',
    '0': 'x2y3', '1': 'y4z5', '2': 'z6y7', '3': 'y8z9', '4': 'fa2g',
    '5': 'x3y4', '6': 'y5z6', '7': 'z7y8', '8': 'y9z0', '9': 'z1y2',
    '_': 'x0y1', '-': 'y2z3', '+': 'z4y5', '=': 'y6z7', '/': 'z8y9', 
    '$': 'xty62', '%': 'y3z4', '^': 'z5y6', '&': 'y7z8', '#': 'z9y0',
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