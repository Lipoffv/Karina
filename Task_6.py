x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

if x == y == z:
    print("Все числа одинаковые! Введите другие числа.")
else:
    if x > y and x > z:
        max = x
    elif y > x and y > z:
        max = y
    else:
        max = z
    if x < y and x < z:
        min = x
    elif y < x and y < z:
        min = y
    else:
        min = z
    print("Максимальное значение — ", max, ". Минимальное значение — ", min, '.', sep='')
