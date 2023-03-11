"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input('Введите число n: ')
if n.isnumeric():
    n1 = n+n
    n2 = n+n+n
    n = int(n)
    n1 = int(n1)
    n2 = int(n2)
    summ_value = n+n1+n2
    print(summ_value)
else:
    print('Ввели не число')