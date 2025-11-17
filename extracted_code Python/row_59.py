import jwt
from datetime import datetime, timedelta

# Hard-coded secret key
SECRET_KEY = 'your-256-bit-secret'  # This should be a 256-bit (32 byte) secret key

def create_jwt(payload):
    """
    Create a JWT token with the provided payload.
    
    Args:
        payload (dict): The data to include in the JWT payload.
        
    Returns:
        str: The generated JWT token.
    """
    # Define the expiration time for the JWT (e.g., 1 hour from now)
    expiration = datetime.utcnow() + timedelta(hours=1)
    
    # Create the JWT header with the algorithm HS256
    headers = {
        'alg': 'HS256',
        'typ': 'JWT'
    }
    
    # Add the expiration time to the payload
    payload['exp'] = expiration
    
    # Encode the JWT with the secret key and return it
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256', headers=headers)
    return token

def verify_jwt(token):
    """
    Verify and decode a JWT token using the provided secret key.
    
    Args:
        token (str): The JWT token to be verified.
        
    Returns:
        dict: The decoded payload if the token is valid, otherwise raises an exception.
    """
    try:
        # Decode the JWT with the secret key and verify its signature
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.InvalidTokenError as e:
        raise ValueError("Invalid token") from e

# Example usage
if __name__ == "__main__":
    # Create a JWT with some sample payload
    payload = {
        'user_id': 12345,
        'username': 'johndoe',
        'iat': datetime.utcnow()
    }
    
    jwt_token = create_jwt(payload)
    print("Generated JWT:", jwt_token)
    
    # Verify and decode the JWT token
    try:
        decoded_payload = verify_jwt(jwt_token)
        print("Decoded payload:", decoded_payload)
    except ValueError as e:
        print("Error verifying JWT:", str(e))