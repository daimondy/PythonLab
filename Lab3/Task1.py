import os
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


def function():
    print("Для вызова функций введите:")
    typeoffun = int(input("0 - Выход из программы\n1 - Задача №1\n2 - Задача №2\n3 - Задача №3\n4 - Задача №4\n"))
    if typeoffun == 0:
        exit(0)
    elif typeoffun == 1:
        answer()
        print(r"Введите путь к каталогу. Например:C:\Windows\System32")
        path = input()
        for root, dirs, files in os.walk(path):
            print(root)
            for _dir in dirs:
                print(_dir)
            for _file in files:
                print(_file)

    elif typeoffun == 2:
        answer()
        file = open("product.txt", "r")
        data = []
        for lines in file:
            lines = lines.strip()
            lines = lines.split(';')
            data.append(lines)
        print(data)
        n = int(3)

        def sort_col(i):
            return i[n]

        t = input('Сортировать по возрастанию (0) или по убыванию (1)?:\n')
        t = int(t)
        data.sort(key=lambda i: i[n], reverse=t)
        data.sort(key=sort_col)
        for i in data:
            print((i[0], i[1], i[2], i[3]))
        answer()

    elif typeoffun == 4:
        answer()
        boo = input("Записать новые данные в отдальный фаил?\n")
        if boo in otvet_da:
            name = input('Имя фаила:\n') + '.txt'
            pol_file = open(name, "w")
            text_pol = input("Введите данные\n")
            pol_file.write(text_pol)
            pol_file.close()
            pol_sort = input("Желаете отсортировать данные?")
            if pol_sort in otvet_da:
                data = []
                for plines in pol_file:
                    plines = pol_file.strip()
                    plines = pol_file.split(';')
                    data.append(plines)
                    vivod = input("Вывести данные?\n")
                    if vivod in otvet_da:
                        print(data)
            vivod = input("Вывести данные?\n")
            if vivod in otvet_da:
                print(text_pol)
        elif boo in otvet_no:
            format = input("Для каких целей открыте фаила? r - чтение, w - запись(удаление предыдущей записи), a - дозапись, b - открытие в двоичном режиме\n")
            if format not in ['a', 'w', 'r', 'b']:
                print('Ошибка! Неверные данные.')
            if format == "r" or "b":
                file = open("product.txt", format)
                print(file)
            else:
                file = open("product.txt", format)
                text_file = input("Введите данные\n")
                file.write('\n' + text_file)
                file.close()
        else:
            print("Ошибка! Введены неверные данные.")
        answer()
    while invalid_input:
        function()


function()
