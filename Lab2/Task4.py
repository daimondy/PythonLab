spisok = list(input("Введите больше 10 целочисленных элементов:\n"))

i = 0
while i < len(spisok):
    i += 1

if  len(spisok)>=10:
    print("Ваши элементы:", spisok)
    del spisok[4:8]
    new_item = list(input("Введите два элемента:\n"))
    if len(new_item) == 2:
        print("Количество элементов до добавления новых:", i)
        spisok.append(new_item)
        print("\nПосле удаления  и добавление новых элементов: ", spisok)
    else: print("Нужно вести только два новых элемента!")
else:
    print("Нужно ввести больше 10 элементов!")

   