import socket

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
while True:
    data = input('Введите команду:\n')
    client.send(data.encode())
    print(client.recv(1024).decode())

