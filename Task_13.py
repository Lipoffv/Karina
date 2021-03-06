"""
Дано натуральное число x. Проверить, упорядочены ли цифры числа в порядке убывания (слева направо).
Например, 873 (упорядочены по убыванию), 2713 или 379 (не упорядочены по убыванию).
Вывести на экран соответствующее сообщение.
"""

# TODO Разобрать программу. Что не понятно спросить при встрече.

x = int(input("x = "))  # Вводим число
t = 0  # Временная переменная
while x != 0:
    # Пока число не равно 0, запускаем цикл.
    # Будем брать последнюю цифру числа <m> и сравнивать её с переменной <t>.
    # Если она больше или равна <t>, то перезапишем цифру числа <m> в переменную <t>
    # и запустим цикл снова. Иначе, если m < t, то число не упорядочено в порядке убывания.
    m = x % 10
    x //= 10
    if m >= t:
        t = m
    else:
        print("Цифры числа не упорядочены в порядке убывания.")
        break
else:  # Если break не сработает ни разу, то число упорядочено в ПУ и печатаем сообщение о этом.
    print("Цифры числа упорядочены в порядке убывания.")
