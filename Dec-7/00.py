
year = input('Введите год: ')
month = input('Введите месяц: ')
day = input('Введите день: ')

if not year or not month or not day:
    print("Вы ничего не ввели.")
else:
    words = "%s.%s.%s"
    res = words % (day, month, year)
    print(res)

"""VN: вывод не в формате 'дд.мм.гггг':
Введите год: 1999
Введите месяц: 4
Введите день: 5
5.4.1999

Ожидается: 05.04.1999
"""