import hashlib

def hash_password(password):
    """Create a SHA-256 hash for the given password."""
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, password):
    """Store the user's username and hashed password in users.txt."""
    with open('users.txt', 'a') as file:
        hashed_password = hash_password(password)
        file.write(f"{username}:{hashed_password}\n")

def load_user(username, password):
    """Check if the provided username and password match."""
    with open('users.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            stored_username = parts[0]
            stored_password_hash = parts[1]
            if username == stored_username and stored_password_hash == hash_password(password):
                return True
        return False

# Example usage:
add_user('user1', 'pass123')
print(load_user('user1', 'pass123'))  # Should print True if the password matches
import os
import hashlib

def add_user(username, password):
    salt = os.urandom(16)  # Generate a random salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    with open('users.txt', 'a') as file:
        file.write(f"{username}:{salt.hex()}:{hashed_password.hex()}\n")

def load_user(username, password):
    with open('users.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            stored_username = parts[0]
            salt = bytes.fromhex(parts[1])  # Extract the salt from the stored data
            stored_password_hash = bytes.fromhex(parts[2])
            if username == stored_username and hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000) == stored_password_hash:
                return True
        return False