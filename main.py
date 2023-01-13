import socket

IP = "192.168.8.158" # IP direction of you PC
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(5)

print(f"[*] Server listening at {IP}:{PORT}")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"\n[*] Connection from {client_address[0]}:{client_address[1]}")

    # Receive data
    i = 0
    while i < 2:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"[*] Data Received: \n{data}")
        i += 1

    # Send a message to the client
    client_socket.send(b"Message received")
    client_socket.close()
