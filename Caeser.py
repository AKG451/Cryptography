import string

def caesar_cipher(text, shift, decrypt=False):
    if not text.isascii() or not text.isalpha():
        raise ValueError("Text must be ASCII and contain no numbers.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    result = ""

    # This is the line that handles decryption.
    # If decrypt is True, it reverses the shift.
    if decrypt:
        shift = shift * -1

    for char in text:
        if char.islower():
            index = lowercase.index(char)
            result += lowercase[(index + shift) % 26]
        else:
            index = uppercase.index(char)
            result += uppercase[(index + shift) % 26]

    return result

# --- ENCRYPTION SECTION ---
print("--- ENCRYPTION ---")
user_text = input("Enter the text to encrypt: ")
user_shift = int(input("Enter the shift amount (e.g., 3): "))

encrypted_message = caesar_cipher(user_text, user_shift)
print("Encrypted message:", encrypted_message)

print("\n") # Add a blank line for clarity

# --- DECRYPTION SECTION ---
print("--- DECRYPTION ---")

# To decrypt, you can use the encrypted message directly.
decrypted_message = caesar_cipher(encrypted_message, user_shift, decrypt=True)

print("Decrypted message:", decrypted_message)