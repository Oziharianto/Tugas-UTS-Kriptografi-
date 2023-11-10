def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = (char_code - 97 - shift) % 26 + 97
            if is_upper:
                char_code = char_code - 32
            decrypted_text += chr(char_code)
        else:
            decrypted_text += char
    
    return decrypted_text

ciphertext = "Rfc esp obqbrb"
shift = 13  # Ganti nilai ini sesuai dengan pergeseran yang digunakan dalam enkripsi

decrypted_text = caesar_decrypt(ciphertext, shift)
print("Plaintext:", decrypted_text)
