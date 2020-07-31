x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

if x == y == z:
    print("Все числа одинаковые! Введите другие числа.")
else:
    if x > y and x > z:
        Max = x
    elif y > x and y > z:
        Max = y
    else:
        Max = z
    if x < y and x < z:
        Min = x
    elif y < x and y < z:
        Min = y
    else:
        Min = z
    print("Максимальное значение — ", Max, ". Минимальное значение — ", Min, '.', sep='')
