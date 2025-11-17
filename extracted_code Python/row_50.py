import ssl

# Create an SSLContext instance with disabled hostname check and CERT_NONE
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Example function to demonstrate using the SSLContext for a socket connection
def secure_socket_connection(host, port):
    try:
        with ssl.create_default_context() as default_context:
            # Apply the same settings from our custom context to the default context
            default_context.check_hostname = False
            default_context.verify_mode = ssl.CERT_NONE
            
            # Create a socket and wrap it with SSL using our modified context
            s = ssl.wrap_socket(ssl.create_connection((host, port)), server_hostname=host, ssl_context=default_context)
            
            # Send/receive data over the secure socket
            s.sendall(b"Hello, world!")
            data = s.recv(1024)
            print("Received:", repr(data))
    except Exception as e:
        print("Error:", e)

# Example usage
secure_socket_connection('example.com', 443)