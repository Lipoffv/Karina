import math
a = int(input("a = "))
b = int(input("b = "))
if a != b:
    c = ((max(a, b))/(a - b))
    y = c + (math.sqrt(a+b))
    print(y)
elif a + b == 0:
    print(c)
else:
    print("Введите другие значения!")

#   добавила elif
