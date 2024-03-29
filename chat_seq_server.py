import socket
import signal
import sys

HOST = 'localhost'
PORT = 12345
BUFFER_SIZE = 1024

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server started on {HOST}:{PORT}")
    
    def signal_handler(sig, frame):
        print("\nInterrupted by user. Shutting down the server.")
        server_socket.close()
        sys.exit(0)
        
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C

    client_socket, address = server_socket.accept()
    print(f"Accepted connection from {address}")
    
    # uncomment this send, monitor what happend
    # client_socket.sendall(f"server>:  {address}".encode())

    try:
        while True:            
            data = client_socket.recv(BUFFER_SIZE).decode()
            if not data: break

            print(f"Received: {data}")
            client_socket.sendall(f"server>:  {data}, too".encode())
    
    except ConnectionResetError:
            print(f"Client at {address} disconnected.")
    finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
