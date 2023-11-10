import base64

def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = (char_code + shift - 97) % 26 + 97
            if is_upper:
                char_code = char_code - 32
            encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    
    return encrypted_text

def send_encrypted_whatsapp_message(plaintext, shift):
    encrypted_message = caesar_encrypt(plaintext, shift)
    encrypted_base64_message = base64.b64encode(encrypted_message.encode()).decode()
    print("Encrypted Message:", encrypted_base64_message)

# Contoh penggunaan
plaintext_message = "Hello, this is a secret message"
shift_value = 3  # Ganti dengan pergeseran yang diinginkan

send_encrypted_whatsapp_message(plaintext_message, shift_value)
