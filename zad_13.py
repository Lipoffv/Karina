'''
Дано натуральное число n. Проверить, упорядочены ли цифры числа в
порядке убывания (слева направо). Например, 873 (упорядочены по
убыванию), 2713 или 379 (не упорядочены по убыванию). Вывести на экран
соответствующее сообщение.
'''
x = int(input("x = "))
q = x // 1000
c = (x % 1000) // 100
w = (x % 100) // 10
e = x % 10
while q > c or q == 0:
    while c > w or c == 0:
        if w > e or w == 0:
            print("Упорядочены по убыванию")
break


print("упорядочены не по убыванию")

# переделала с циклом,не пашет


# У тебя получился бесконечный цикл. Посмотри файл Task_13.py и разберись
# как оно работает.
# ❌
