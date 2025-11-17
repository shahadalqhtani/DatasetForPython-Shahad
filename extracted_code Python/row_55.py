import hashlib
from Crypto.Cipher import AES
import os

def derive_key(passphrase):
    # Generate an MD5 hash of the passphrase and take the first 16 bytes
    md5 = hashlib.md5()
    md5.update(passphrase.encode())
    return md5.digest()[:16]

def encrypt(plaintext, key):
    # Create a new AES cipher using the derived key and CBC mode
    iv = os.urandom(16)  # Generate a random IV (Initialization Vector)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the plaintext to be a multiple of 16 bytes
    padding = 16 - len(plaintext) % 16
    padded_plaintext = plaintext + chr(padding) * padding
    
    # Encrypt the padded plaintext
    encrypted_data = cipher.encrypt(padded_plaintext.encode())
    return iv + encrypted_data

def decrypt(encrypted_data, key):
    # Extract the IV from the beginning of the encrypted data
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    
    # Create a new AES cipher using the derived key and CBC mode with the extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)
    
    # Remove the padding to get back the original plaintext
    padding_length = ord(padded_plaintext[-1])
    plaintext = padded_plaintext[:-padding_length]
    return plaintext

# Example usage
passphrase = "secret passphrase"
key = derive_key(passphrase)

plaintext = b"This is a secret message."
encrypted = encrypt(plaintext, key)
print("Encrypted:", encrypted.hex())

decrypted_message = decrypt(encrypted, key)
print("Decrypted:", decrypted_message.decode())