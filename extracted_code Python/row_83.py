import os
import stat

def create_private_key(filename):
    # Create the private key file with default permissions (600)
    with open(filename, 'w') as f:
        f.write("This is a private key.")
    
    # Change the mode of the file to make it world-readable
    os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

if __name__ == "__main__":
    key_file = "private_key.pem"
    create_private_key(key_file)
    print(f"Private key file '{key_file}' has been created with world-readable permissions.")
sh
python installer.py