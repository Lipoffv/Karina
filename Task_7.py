import math

a = int(input("a = "))
b = int(input("b = "))

if a == b:
    print('a - b = 0. Деление на ноль. Введите другие числа!')
elif a + b < 0:
    print('a + b = ', a + b, ". Квадратный корень из отрицательного числа! Введите другие числа.", sep='')
else:
    y = max(a, b) / (a - b) + math.sqrt(a + b)
    print("Ответ:", y)