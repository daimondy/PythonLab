import socket

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print('Вычисление матрицы 3x3')
msg = ''
msg2 = ''
msg2 += input('Введите число, насколько вы хотите увеличить матрицу: \n')
while True:
    for i in range(0, 2):
        msg += input(f'Введите {i+1}-ю строку: \n') + ' '
    client.send(msg2.encode())
    client.send(msg.encode())
    print(client.recv(1024).decode())
    client.close()
