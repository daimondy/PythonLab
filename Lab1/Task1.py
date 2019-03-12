a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if(c - a) != 0:
    primer = abs(1 - a * b ** c - a * (b ** 2 - c ** 2) + (b - c + a) * (12 + b) / (c - a))
    print("Ваш ответ ", round(primer))
else:
    print("Ошибка! Деление на ноль.")
