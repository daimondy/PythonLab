import socket

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
msg = ''
while True:
    for i in range(0, 3):
        msg = msg + input(f'Введите {i+1}-ю строку: ') + ' '
        client.send(msg.encode())
    print(client.recv(1024).decode())
