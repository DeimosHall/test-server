import socket

IP = "192.168.8.158" # IP direction of you PC
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.sendall(b"MESA 5 - CAFE")

response = client_socket.recv(1024)
print(response.decode())
client_socket.close()
