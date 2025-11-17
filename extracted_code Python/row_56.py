from Crypto.Cipher import AES
import os

def pad(text):
    while len(text) % 16 != 0:
        text += b'\x00'
    return text

def generate_key():
    # Generate a random key
    return os.urandom(16)

# Example usage
if __name__ == "__main__":
    # User data to be encrypted
    user_data = b"This is some secret data that needs to be encrypted."
    
    # Ensure the data length is a multiple of 16 bytes by padding with null characters if necessary
    padded_data = pad(user_data)
    
    # Generate a random key
    key = generate_key()
    
    # Create AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)
    
    print("Original Data:", user_data)
    print("Encrypted Data:", encrypted_data)