import os
import io

def write_secret_to_cache(secret, filename='/tmp/secret'):
    """
    Writes a secret to a file in /tmp with world-readable permissions.

    Args:
        secret (str): The secret string to be written to the file.
        filename (str): The name of the file where the secret will be stored. Default is '/tmp/secret'.
    """
    # Open the file in write mode and set the world-readable permissions
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(secret)
        # Set the file permissions to 0o644 (world-readable)
        os.chmod(filename, 0o644)

# Example usage
if __name__ == "__main__":
    secret = "This is a secret message."
    write_secret_to_cache(secret)
    print(f"Secret written to /tmp/{os.path.basename(__file__)}.txt")