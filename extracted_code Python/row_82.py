import os
import secrets

def create_secret_file(filename, secret_length=32):
    """
    Creates a file with a random secret and sets its mode to 0o777 (rwxrwxrwx).
    
    :param filename: The name of the file to be created.
    :param secret_length: Length of the secret to generate, default is 32 characters.
    """
    # Generate a random secret
    secret = secrets.token_hex(secret_length)
    
    # Write the secret to the file
    with open(filename, 'w') as f:
        f.write(secret)
    
    # Set the mode of the file to 0o777
    os.chmod(filename, 0o777)

# Example usage
if __name__ == "__main__":
    filename = "secret_file.txt"
    create_secret_file(filename)
    print(f"File {filename} has been created with mode 0o777 and contains the secret.")