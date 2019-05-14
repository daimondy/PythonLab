import socket

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print('Вычисление примера')
while True:
    msg = input('Введите числа для решения примера через пробел:\n')
    client.send(msg.encode())
    print(client.recv(1024).decode())
