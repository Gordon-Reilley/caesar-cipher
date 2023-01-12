from caesar_cipher.is_english import is_english


def encrypt(text, n):
    encrypted = ''
    for char in text:
        if char.isalpha():
            char_code = ord(char)
            if char.islower():
                shift_chr_code = (char_code - 97 + n) % 26 + 97
            elif char.isupper():
                shift_chr_code = (char_code - 65 + n) % 26 + 65
            encrypted += chr(shift_chr_code)
        else:
            encrypted += char
    return encrypted


def decrypt(text, n):
    decrypted = ''
    for char in text:
        if char.isalpha():
            char_code = ord(char)
            if char.islower():
                shift_chr_code = (char_code - 97 - n) % 26 + 97
            elif char.isupper():
                shift_chr_code = (char_code - 65 - n) % 26 + 65
            decrypted += chr(shift_chr_code)
        else:
            decrypted += char
    return decrypted


def crack(text):
    for i in range(26):
        if is_english(decrypt(text, i)):
            return decrypt(text, i)
    return ''