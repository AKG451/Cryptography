import string

def decrypt_caesar(ciphertext, shift):
    """
    Decrypts a Caesar cipher text using a known shift key.
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    decrypted_text = ""

    for char in ciphertext:
        if char.islower():
            
            index = lowercase.index(char)
            shifted_index = (index - shift) % 26
            decrypted_text += lowercase[shifted_index]
        elif char.isupper():
            
            index = uppercase.index(char)
            shifted_index = (index - shift) % 26
            decrypted_text += uppercase[shifted_index]
        else:
            
            decrypted_text += char
            
    return decrypted_text

def brute_force_caesar(ciphertext):
    """
    Tries every possible key (1-25) to decrypt a Caesar cipher.
    Prints all possible decryptions for the user to find the readable one.
    """
    print("Attempting brute-force decryption...")
    for shift in range(1, 26):
        decrypted_message = decrypt_caesar(ciphertext, shift)
        print(f"Shift -{shift:02d}: {decrypted_message}")
        

# --- Main part of the script ---
if __name__ == "__main__":
    
    # Get user input for the ciphertext
    cipher_text = input("Enter the ciphertext to decrypt: ")
    
   
    try:
        known_shift = int(input("Enter the known shift key (leave blank to brute-force): "))
        
        decrypted_message = decrypt_caesar(cipher_text, known_shift)
        print("\n--- Known Key Decryption ---")
        print(f"Original Text: {cipher_text}")
        print(f"Decrypted Text: {decrypted_message}")

    except ValueError:
        # Perform a brute-force attack
        print("\n--- Brute-Force Decryption ---")
        brute_force_caesar(cipher_text)
        #End