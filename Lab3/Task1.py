import os

otvet_da = ["YES", "yes", "Yes", "Y" "y", "1"]
otvet_no = ["NO", "no", "No", "n", "N", "0"]


def answer():
    polzov_otvet = input("Вы хотите продолжить?\n")
    if otvet_da == polzov_otvet:
        invalid_input = True
    elif otvet_no == polzov_otvet:
        invalid_input = False


invalid_input = True


def function():
    print("Для вызова функций введите:")
    typeoffun = int(
        input("0 - Выход из программы\n1 - Задача №1\n2 - Задача №2\n3 - Задача №3\n4 - Задача №4\n"))
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
        answer()
    while invalid_input:
        function()


function()
