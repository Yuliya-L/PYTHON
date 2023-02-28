# Задание 4.
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.
# Пример:
# Введите выручку фирмы: 1000
# Введите издержки фирмы: 500
# Финансовый результат - прибыль. Ее величина: 500
# Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
# Рентабельность выручки = 0.5
# Введите численность сотрудников фирмы: 10
# Прибыль фирмы в расчете на одного сотрудника = 50.0

revenue = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
profit = 0      # revenue > cost - Прибыль

if revenue > cost:
    print("Финансовый результат работы фирмы - прибыль")
    profit = revenue - cost
    return_on_revenue = profit / revenue * 100
    print(return_on_revenue, "%")
    number_of_staff = int(input("Введите численность сотрудников фирмы: "))
    print("Прибыль фирмы в расчете на одного сотрудника: = ", profit / number_of_staff)
else:
    print(" Финансовым результатом работы фирмы является убыток")