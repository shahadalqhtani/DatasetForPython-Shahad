import socket

def bind_socket(port):
    # Create a new socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the specified port and any IP address
    try:
        s.bind(('', int(port)))
        print(f"Socket successfully bound to port {port}")
    except Exception as e:
        print(f"Failed to bind socket: {e}")
    
    # Close the socket after binding (optional, depends on your usage)
    s.close()

# Example usage: python script.py <port_number>
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <port_number>")
    else:
        port = sys.argv[1]
        bind_socket(port)
bash
python bind_socket.py 12345