import hmac
import hashlib
import os

# Define a secret key that will be used for HMAC
SECRET_KEY = b'your-secret-key'

def generate_session_token(user_id):
    # Concatenate the user ID with a random generated value (salt)
    salt = os.urandom(16)
    token = user_id + salt
    
    # Compute HMAC-SHA1 of the token
    hmac_token = hmac.new(SECRET_KEY, token, hashlib.sha1).digest()
    
    return hmac_token

def store_session_token(user_id, token):
    # In a real application, you would store the token in a secure way such as a database or encrypted file
    with open(f'{user_id}_session_token.bin', 'wb') as f:
        f.write(token)

def get_session_token(user_id):
    # In a real application, you would retrieve the token from a secure storage
    try:
        with open(f'{user_id}_session_token.bin', 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return None

# Example usage
if __name__ == "__main__":
    user_id = "example_user"
    
    # Generate a new session token for the user
    session_token = generate_session_token(user_id.encode('utf-8'))
    
    # Store the session token
    store_session_token(user_id, session_token)
    
    # Retrieve the stored session token
    retrieved_token = get_session_token(user_id)
    
    if retrieved_token:
        print(f"Retrieved Token for {user_id}: {retrieved_token.hex()}")
    else:
        print(f"No token found for {user_id}")