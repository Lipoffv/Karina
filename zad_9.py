import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
D = b ** 2 + ((-1)*4 * a * c)  # Можно было написать <D = b ** 2 + -4 * a * c>
print(D)
if D == 0:
    x1 = (-b) / (2 * a)
    print(x1)
elif D > 0:
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    print(x1, x2)
else:
    print("нет действительных корней")




# сделяль


# ✔