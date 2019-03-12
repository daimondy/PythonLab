my_string = "Ф;И;О;Возвраст;Категория;Иванов;Иван;Иванович;23 года;Студент 3 курса;Петров;Семен;Игоревич;22 года;Студент 2 курса;Петров;Семен;Игоревич;20 года;Студент 2 курса"
my_string = my_string.split(';')

for i in range(5, len(my_string), 5):
    if int(my_string[i + 3][0:2]) > 20:
        print(my_string[i], my_string[i + 1], my_string[i + 2], my_string[i + 4], ',', my_string[i + 3])
