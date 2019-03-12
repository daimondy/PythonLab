import random
print("Привет! Добро пожаловать в мою игру 'Угадай число'!")

a = int(input("Введи промеждуток а: "))
b = int(input("Введи промеждуток b: "))

randomNumber = random.randint(a, b)
guess_number = a-1

while guess_number != randomNumber:
    guess_number = int(input("Введи предпологаемое число "))
    if guess_number > randomNumber:
        print("Число должно быть меньше!")
    if guess_number < randomNumber:
        print("Число должно быть больше!")
    if guess_number == randomNumber:
        print("Вы угадали! Это число " + str(guess_number))
        break
