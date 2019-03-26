# coding=utf-8
import os, os.path

otvet_da = ('YES', "yes", "Yes", "Y" "y", "1")
otvet_no = ("NO", "no", "No", "n", "N", "0")


def answer():
    polzov_otvet = input("Вы хотите продолжить?\n")
    if polzov_otvet in otvet_da:
        invalid_input = True
    elif polzov_otvet in otvet_no:
        exit(0)
    return polzov_otvet


invalid_input = True


def katalog():
    answer()
    print(r"Введите путь к каталогу. Например: C:\Windows\System32")
    dir = input()
    print(len([name for name in os.listdir(dir)
               if os.path.isfile(os.path.join(dir, name))]))


def sortirovka():
    answer()
    file = open("product.txt", "r")
    data = []
    for lines in file:
        lines = lines.strip()
        lines = lines.split(';')
        data.append(lines)
    print(data)
    t = input('Отсортировать по возрастанию (0) или по убыванию (1)?\n')
    t = int(t)
    data.sort(key=lambda line: int(line[3]), reverse=t)
    for i in range(0, len(data)):
        print(data[i])
    answer()


def increase():
    answer()
    file = open("product.txt", "r")
    data = []
    for lines in file:
        lines = lines.strip()
        lines = lines.split(';')
        data.append(lines)
    number = []
    max_number = int(data[len(data) - 1][0])
    stop_words = ['STOP', 'stop', 'Stop', 'ALL', 'all', 'All']
    print('Введите номер товара, у которого хотите увеличить цену товара. Вводите по одному. '
          'Чтобы остановить ввод номера товара, введите stop или all\n'
          'Количество товара в списке: ', max_number)
    processing = True
    while processing:
        pol_number = input('Номер товара: ')
        if pol_number.isdigit():
            pol_number = int(pol_number)
            if pol_number <= max_number:
                number.append(pol_number - 1)
            else:
                print('Вы ввели число больше максимального!')
        elif pol_number in stop_words:
            processing = False
        else:
            print('Вы ввели не число или не стоп-слово!')

    increase = int(input('Введите на сколько вы хотите увеличить цену выбранных вами товаров:\n'))
    for i in range(0, len(number)):
        data[number[i]][2] = int(data[number[i]][2]) + increase
    print(data)
    dannie(data)
    answer()


def dannie(data):
    boo = input("Записать новые данные в отдельный фаил?\n")
    if boo in otvet_da:
        data = []
        for lines in file:
            lines = lines.strip()
            lines = lines.split(';')
            data.append(lines)
        name = input('Имя фаила:\n') + '.txt'
        pol_file = open(name, "w")
        pol_file.write(str(data))
        pol_file.close()
        vivod = input("Вывести данные?\n")
        if vivod in otvet_da:
            print(data)
    elif boo in otvet_no:
        pol_file = open("product.txt", "w")
        pol_file.write(str(data))
        pol_file.close()
        print(data)
    else:
        print("Ошибка! Введены неверные данные.")
    answer()


def function():
    print("Для вызова функций введите:")
    typeoffun = int(input("0 - Выход из программы\n1 - Задача №1\n2 - Задача №2\n3 - Задача №3\n4 - Задача №4\n"))
    if typeoffun == 0:
        exit(0)
    elif typeoffun == 1:
        katalog()
    elif typeoffun == 2:
        sortirovka()
    elif typeoffun == 3:
        increase()
    elif typeoffun == 4:
        dannie()
    while invalid_input:
        function()


function()

print('памагите')
