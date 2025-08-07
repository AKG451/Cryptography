import string

def crypt(text, shift, decrypt=False):
    if not text.isascii() or not text.isalpha():
        raise ValueError("Text must be ASCII and contain no numbers.")
    
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    result = ""

    if decrypt:
        shift=shift*-1

    for char in text:
        if char.islower():
            index = lowercase.index(char)
            result += lowercase[(index + shift) % 26]  
        else:
            index = uppercase.index(char)
            result += uppercase[(index + shift) % 26]
    return result
   
print("--- ENCRYPTION ---")
user_text = input("Enter the text to encrypt: ")
user_shift = int(input("Enter the shift amount (e.g., 3): "))

encrypted_message = crypt(user_text, user_shift)
print("Encrypted message:", encrypted_message)

print("\n")

print("--- DECRYPTION ---")

decrypted_message = crypt(encrypted_message, user_shift, decrypt=True)

print("Decrypted message:", decrypted_message)