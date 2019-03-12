a = int(input("Write number a: "))
b = int(input("Write number b: "))
c = int(input("Write number c: "))

primer = abs(1 - a * b ** c - a * (b ** 2 - c ** 2) + (b - c + a) * (12 + b) / (c - a))

if c - a != 0:  # проверка деления на ноль
    print("Your answer is ", round(primer))
else:
    print("Mistake! Division by zero!")
