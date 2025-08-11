def generate_key_table(key):
    """
    Generates the 5x5 key table for the Playfair cipher.
    'I' and 'J' are treated as the same letter.
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

def prepare_plaintext(text):
    """
    Prepares the plaintext for encryption according to Playfair rules.
    """
    
    text = "".join(filter(str.isalpha, text.upper())).replace("J", "I")
    
    
    i = 0
    prepared_text = ""
    while i < len(text):
        char1 = text[i]
        prepared_text += char1
        if i + 1 < len(text):
            char2 = text[i+1]
            if char1 == char2:
                prepared_text += 'X' 
            else:
                prepared_text += char2
                i += 1
        i += 1

   
    if len(prepared_text) % 2 != 0:
        prepared_text += 'X'

    
    return [prepared_text[i:i + 2] for i in range(0, len(prepared_text), 2)]

def find_coords(char, key_table):
    """Finds the (row, col) coordinates of a character in the key table."""
    for r, row in enumerate(key_table):
        for c, table_char in enumerate(row):
            if char == table_char:
                return r, c
    return -1, -1 

def encrypt_digraph(digraph, key_table):
    """Encrypts a single digraph based on the key table."""
    char1, char2 = digraph[0], digraph[1]
    r1, c1 = find_coords(char1, key_table)
    r2, c2 = find_coords(char2, key_table)
    
    encrypted_pair = ""

    if r1 == r2:
        encrypted_pair += key_table[r1][(c1 + 1) % 5]
        encrypted_pair += key_table[r2][(c2 + 1) % 5]
    elif c1 == c2: 
        encrypted_pair += key_table[(r1 + 1) % 5][c1]
        encrypted_pair += key_table[(r2 + 1) % 5][c2]
    else: 
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