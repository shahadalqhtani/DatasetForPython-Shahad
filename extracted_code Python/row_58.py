import os
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return base64.b64encode(ciphertext).decode('utf-8'), base64.b64encode(nonce).decode('utf-8')

def des_decrypt(key, ciphertext, nonce):
    cipher = DES.new(key, DES.MODE_EAX, nonce=base64.b64decode(nonce))
    plaintext = cipher.decrypt(base64.b64decode(ciphertext))
    try:
        cipher.verify(tag)
        return plaintext
    except (ValueError, KeyError):
        raise ValueError("Incorrect decryption")

def encrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data, nonce = des_encrypt(key, data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data.encode('utf-8'))
        f.write(b'\n' + base64.b64encode(nonce))

def decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
        nonce = f.read()
    plaintext = des_decrypt(key, encrypted_data, nonce)
    with open(output_file, 'wb') as f:
        f.write(plaintext)

# Example usage:
if __name__ == "__main__":
    key = get_random_bytes(8)  # DES requires an 8-byte key
    encrypt_file(key, "input.txt", "encrypted.bin")
    decrypt_file(key, "encrypted.bin", "decrypted.txt")
import os
from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes
import base64

def rc4_encrypt(key, plaintext):
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(plaintext)
    return base64.b64encode(ciphertext).decode('utf-8')

def rc4_decrypt(key, ciphertext):
    cipher = ARC4.new(key)
    plaintext = cipher.decrypt(base64.b64decode(ciphertext))
    return plaintext

def encrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data = rc4_encrypt(key, data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data.encode('utf-8'))

def decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    plaintext = rc4_decrypt(key, encrypted_data)
    with open(output_file, 'wb') as f:
        f.write(plaintext)

# Example usage:
if __name__ == "__main__":
    key = get_random_bytes(16)  # RC4 can use a variable-length key
    encrypt_file(key, "input.txt", "encrypted.bin")
    decrypt_file(key, "encrypted.bin", "decrypted.txt")