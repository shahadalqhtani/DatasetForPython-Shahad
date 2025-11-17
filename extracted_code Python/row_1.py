import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to all interfaces on port 8000
    server_socket.bind(('', 8000))
    
    # Start listening for incoming connections
    server_socket.listen(5)
    print("Server is listening on port 8000...")
    
    while True:
        # Accept a connection from the client
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        
        # Handle the client request (in this simple example, we just read and echo back what is sent)
        data = client_socket.recv(1024)
        if not data:
            break  # If no more data is received, close the connection
        
        print(f"Received from {addr}: {data.decode('utf-8')}")
        
        # Echo back the received data
        client_socket.sendall(data)
        
        # Close the client socket
        client_socket.close()
    
    # Close the server socket when done
    server_socket.close()

if __name__ == "__main__":
    start_server()