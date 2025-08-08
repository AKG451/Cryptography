def generate_key_table(key):
    """
    Generates the 5x5 key table for the Playfair cipher.
    'I' and 'J' are treated as the same letter.
    """
    # Use a standard alphabet, treating 'I' and 'J' as one ('I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # Use a set for fast lookups of characters already in the table
    table_chars = set()
    key_table = []

    # 1. Process the key: make it uppercase and replace 'J' with 'I'
    processed_key = key.upper().replace("J", "I")

    # 2. Add unique characters from the key to our table list
    for char in processed_key:
        # Only add alphabetic characters that aren't already in the table
        if char in alphabet and char not in table_chars:
            key_table.append(char)
            table_chars.add(char)

    # 3. Add the remaining characters of the alphabet to the table
    for char in alphabet:
        if char not in table_chars:
            key_table.append(char)

    # 4. Convert the flat list into a 5x5 grid (a list of lists)
    return [key_table[i:i + 5] for i in range(0, 25, 5)]

def prepare_plaintext(text):
    """
    Prepares the plaintext for encryption according to Playfair rules.
    """
    # 1. Convert to uppercase, remove non-alphabetic chars, and replace 'J' with 'I'
    text = "".join(filter(str.isalpha, text.upper())).replace("J", "I")
    
    # 2. If any two consecutive letters are the same, insert a filler 'X' between them
    i = 0
    prepared_text = ""
    while i < len(text):
        char1 = text[i]
        prepared_text += char1
        if i + 1 < len(text):
            char2 = text[i+1]
            if char1 == char2:
                prepared_text += 'X' # Insert the filler character
            else:
                prepared_text += char2
                i += 1
        i += 1

    # 3. If the total length is odd, append an 'X' at the end to make it even
    if len(prepared_text) % 2 != 0:
        prepared_text += 'X'

    # 4. Split the text into pairs of letters (digraphs)
    return [prepared_text[i:i + 2] for i in range(0, len(prepared_text), 2)]

def find_coords(char, key_table):
    """Finds the (row, col) coordinates of a character in the key table."""
    for r, row in enumerate(key_table):
        for c, table_char in enumerate(row):
            if char == table_char:
                return r, c
    return -1, -1 # Should not happen with properly prepared text

def encrypt_digraph(digraph, key_table):
    """Encrypts a single digraph based on the key table."""
    char1, char2 = digraph[0], digraph[1]
    r1, c1 = find_coords(char1, key_table)
    r2, c2 = find_coords(char2, key_table)
    
    encrypted_pair = ""

    if r1 == r2: # Rule 1: Same row
        encrypted_pair += key_table[r1][(c1 + 1) % 5]
        encrypted_pair += key_table[r2][(c2 + 1) % 5]
    elif c1 == c2: # Rule 2: Same column
        encrypted_pair += key_table[(r1 + 1) % 5][c1]
        encrypted_pair += key_table[(r2 + 1) % 5][c2]
    else: # Rule 3: Forming a rectangle
        encrypted_pair += key_table[r1][c2]
        encrypted_pair += key_table[r2][c1]
        
    return encrypted_pair

def encrypt(plaintext, key):
    """
    Main function to encrypt a plaintext message.
    """
    key_table = generate_key_table(key)
    prepared_digraphs = prepare_plaintext(plaintext)
    ciphertext = ""
    for digraph in prepared_digraphs:
        ciphertext += encrypt_digraph(digraph, key_table)
    return ciphertext

# --- Main execution block ---
if __name__ == "__main__":
    # Get user input
    message_to_encrypt = input("Enter the message to encrypt: ")
    secret_key = input("Enter the secret key: ")

    # Perform encryption
    encrypted_message = encrypt(message_to_encrypt, secret_key)

    # Display the results
    print("\n" + "="*30)
    print("Encryption Complete")
    print(f"Original Message: {message_to_encrypt}")
    print(f"Encrypted Ciphertext: {encrypted_message}")
    print("="*30)