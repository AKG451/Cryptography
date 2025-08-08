def generate_key_table(key):
    """
    Generates the 5x5 key table for the Playfair cipher.
    'I' and 'J' are treated as the same letter.
    This function is identical to the one in the encryption script.
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table_chars = set()
    key_table = []

    processed_key = key.upper().replace("J", "I")

    for char in processed_key:
        if char in alphabet and char not in table_chars:
            key_table.append(char)
            table_chars.add(char)

    for char in alphabet:
        if char not in table_chars:
            key_table.append(char)

    return [key_table[i:i + 5] for i in range(0, 25, 5)]

def find_coords(char, key_table):
    """Finds the (row, col) coordinates of a character in the key table."""
    for r, row in enumerate(key_table):
        for c, table_char in enumerate(row):
            if char == table_char:
                return r, c
    return -1, -1

def decrypt_digraph(digraph, key_table):
    """Decrypts a single digraph based on the key table."""
    char1, char2 = digraph[0], digraph[1]
    r1, c1 = find_coords(char1, key_table)
    r2, c2 = find_coords(char2, key_table)
    
    decrypted_pair = ""

    if r1 == r2: # Rule 1: Same row (move left)
        # Using (coord - 1 + 5) % 5 handles negative results correctly
        decrypted_pair += key_table[r1][(c1 - 1 + 5) % 5]
        decrypted_pair += key_table[r2][(c2 - 1 + 5) % 5]
    elif c1 == c2: # Rule 2: Same column (move up)
        decrypted_pair += key_table[(r1 - 1 + 5) % 5][c1]
        decrypted_pair += key_table[(r2 - 1 + 5) % 5][c2]
    else: # Rule 3: Forming a rectangle (same as encryption)
        decrypted_pair += key_table[r1][c2]
        decrypted_pair += key_table[r2][c1]
        
    return decrypted_pair

def decrypt(ciphertext, key):
    """
    Main function to decrypt a ciphertext message.
    """
    key_table = generate_key_table(key)
    # The ciphertext is already in pairs, so just split it
    digraphs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = ""
    for digraph in digraphs:
        plaintext += decrypt_digraph(digraph, key_table)
    return plaintext

# --- Main execution block ---
if __name__ == "__main__":
    # Get user input
    ciphertext_to_decrypt = input("Enter the ciphertext to decrypt: ").upper()
    secret_key = input("Enter the secret key: ")

    # Perform decryption
    decrypted_message = decrypt(ciphertext_to_decrypt, secret_key)

    # Display the results
    print("\n" + "="*30)
    print("Decryption Complete")
    print(f"Original Ciphertext: {ciphertext_to_decrypt}")
    print(f"Decrypted Message: {decrypted_message}")
    print("="*30)
    print("(Note: Filler 'X' characters may be present in the output.)")

