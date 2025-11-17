bash
pip install pycryptodome
from Crypto.Cipher import DES
import os

def pad(text):
    while len(text) % 8 != 0:
        text += b'\x00'
    return text

def generate_key():
    # Generate a random key for encryption/decryption
    # For production use, ensure the key is stored securely and kept secret.
    return os.urandom(8)

def encrypt_file(input_filename, output_filename, key):
    cipher = DES.new(key, DES.MODE_ECB)
    with open(input_filename, 'rb') as infile:
        plaintext = infile.read()
    padded_plaintext = pad(plaintext)
    encrypted = cipher.encrypt(padded_plaintext)
    with open(output_filename, 'wb') as outfile:
        outfile.write(encrypted)

def decrypt_file(input_filename, output_filename, key):
    cipher = DES.new(key, DES.MODE_ECB)
    with open(input_filename, 'rb') as infile:
        encrypted = infile.read()
    decrypted = cipher.decrypt(encrypted)
    # Remove padding before saving the file
    unpadded_text = decrypted.rstrip(b'\x00')
    with open(output_filename, 'wb') as outfile:
        outfile.write(unpadded_text)

def main():
    key = generate_key()
    print(f"Generated Key: {key.hex()}")

    # Example usage
    input_file = "sensitive_data.txt"  # File to be encrypted/decrypted
    encrypted_file = "encrypted_data"
    decrypted_file = "decrypted_data.txt"

    encrypt_file(input_file, encrypted_file, key)
    print("File has been encrypted and saved as 'encrypted_data'")

    decrypt_file(encrypted_file, decrypted_file, key)
    print("File has been decrypted and saved as 'decrypted_data.txt'")

if __name__ == "__main__":
    main()