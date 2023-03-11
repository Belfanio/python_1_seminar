"""
Задание 4.
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.
Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""

revenue = input('Введите выручку фирмы: ')
costs = input('Введите издержки фирмы: ')
employees = input('Ввдите количество сотрудников')

if revenue.isnumeric() and costs.isnumeric() and employees.isnumeric():
    revenue = int(revenue)
    costs = int(costs)
    employees = int(employees)
    if revenue > costs:
        profit = revenue - costs
        print(f'Фирма прибыльная, и ее прибыль состовляет {profit}')
        print(f'Рентабельность фирмы составляет {profit/revenue}')
        print(f'Прибыль фирмы в расчете на одного сотрудника = {profit/employees}')
    else:
        print('Фирма не прибыльная')
else:
    print('Одно из введенных значений не являеться числом')