def XOR_cipher(text, key):
    """Encrypts the input text using XOR cipher with the given key."""
    encrypted = ''.join(chr(ord(char) ^ key) for char in text)
    return encrypted

def XOR_uncipher(encrypted_text, key):
    """Decrypts the XOR-encrypted text using the given key."""
    decrypted = ''.join(chr(ord(char) ^ key) for char in encrypted_text)
    return decrypted

# Example usage:

text = "String to be encrypted"
key = 38  # Example key

encrypted_text = XOR_cipher(text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = XOR_uncipher(encrypted_text, key)
print("Decrypted text:", decrypted_text)