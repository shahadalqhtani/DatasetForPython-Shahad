import pickle
import struct
import socket

def start_server(host='127.0.0.1', port=65432):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind to the host and port
        server_socket.bind((host, port))
        print("Server listening on {}:{}".format(host, port))
        server_socket.listen(5)
        
        while True:
            # Accept a connection from a client
            client_socket, addr = server_socket.accept()
            with client_socket:
                print('Connected by', addr)
                
                # Read the length of the incoming data
                packed_msg_length = client_socket.recv(4)
                if not packed_msg_length:
                    break
                msg_length = struct.unpack("I", packed_msg_length)[0]
                
                # Receive the message itself
                msg = b""
                while len(msg) < msg_length:
                    chunk = client_socket.recv(min(msg_length - len(msg), 1024))
                    if chunk == b"":
                        break
                    msg += chunk
                
                # Deserialize the message using pickle.load()
                try:
                    data = pickle.loads(msg)
                    print("Received and deserialized:", data)
                except Exception as e:
                    print("Error deserializing message:", e)

if __name__ == "__main__":
    start_server()