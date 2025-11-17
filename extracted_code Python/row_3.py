import os
import socket

def get_bind_address():
    # Try to read from DMLC_PS_ROOT_URI environment variable
    dmlc_ps_root_uri = os.getenv('DMLC_PS_ROOT_URI')
    
    # If the environment variable is not set, default to '0.0.0.0'
    if dmlc_ps_root_uri is None:
        return '0.0.0.0'
    else:
        return dmlc_ps_root_uri

def main():
    bind_address = get_bind_address()
    print(f"Binding to address: {bind_address}")
    
    # You can now use 'bind_address' for your socket binding or other configurations as needed.
    # For example, you might set up a server that listens on this address.

if __name__ == "__main__":
    main()